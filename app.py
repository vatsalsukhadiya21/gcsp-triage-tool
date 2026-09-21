import os
import uuid
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from realitydefender import RealityDefender
from triage import analyze_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    description = request.form.get('description', '')
    
    if file.filename == '':
        return "No file selected", 400

    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4()}_{filename}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(filepath)

    # 1. Run Reality Defender
    try:
        api_key = os.environ.get("REALITY_DEFENDER_API_KEY")
        if not api_key:
            return "REALITY_DEFENDER_API_KEY environment variable is not set.", 500

        client = RealityDefender(api_key=api_key)
        rd_result = client.detect_file(filepath)
    except Exception as e:
        rd_result = {"error": str(e)}
        
    # 2. Text Triage Analysis
    triage_result = analyze_text(description)

    # Clean up temp file
    if os.path.exists(filepath):
        os.remove(filepath)

    return render_template('result.html', description=description, rd_result=rd_result, triage=triage_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
