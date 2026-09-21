# Conflict Misinformation Triage Tool

A Python Flask web application that adds a consequence-aware triage 
layer on top of an existing media-authenticity detection API. Instead 
of returning a flat "real or fake" signal, it classifies flagged 
content into four conflict-relevant deception patterns — authority 
impersonation, operational deception, context laundering, and 
fabricated event evidence — and outputs the decision at risk, 
potential consequence, urgency, and a recommended response.

Built on Flask, using the Reality Defender API as an authenticity 
input signal, not a verdict.

## Setup
1. Install dependencies:
```bash
   pip install -r requirements.txt
```
2. Set your Reality Defender API key as an environment variable:
```bash
   REALITY_DEFENDER_API_KEY=your_key_here
```
3. Run the application:
```bash
   python app.py
```

## Notes
This is an early-stage prototype. Category matching currently uses 
rule-based keyword logic, which works reliably for explicit language 
and provides a clear, auditable foundation to build on. Planned next 
steps include semantic matching to catch deception implied through 
context, multilingual support, and testing with real-world users.
