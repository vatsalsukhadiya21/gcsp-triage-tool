import re

CATEGORIES = [
    {
        "name": "Operational deception",
        "keywords": ["surrender", "ceasefire", "retreat", "withdraw", "stand down"],
        "urgency": "Critical",
        "decision": "Soldiers may alter tactical posture / civilians shift support believing a ceasefire occurred.",
        "consequence": "Vulnerability to ambush and loss of strategic advantage.",
        "action": "Cross-reference with internal military comms. Wait for confirmation."
    },
    {
        "name": "Authority impersonation",
        "keywords": ["emergency", "government", "alert", "official", "police", "president", "warning"],
        "urgency": "Critical",
        "decision": "Misdirection of the public, false evacuation, or false shelter orders.",
        "consequence": "Risk of unsafe civilian movement and eroded trust in official channels.",
        "action": "Verify with official channels immediately. Do not share."
    },
    {
        "name": "Context laundering",
        "keywords": ["old", "past", "breaking", "happening now", "just happened", "live footage", "old footage", "recycled"],
        "urgency": "High",
        "decision": "Misallocation of resources or diplomatic pressure based on old events.",
        "consequence": "Responding to non-existent threats and unwarranted diplomatic fallout.",
        "action": "Perform reverse image search. Check metadata."
    },
    {
        "name": "Fabricated event evidence",
        "keywords": ["strike", "casualty", "dead", "explosion", "bombing", "attack", "destroyed", "massacre"],
        "urgency": "High",
        "decision": "Escalation or retaliatory strikes based on fake strike footage.",
        "consequence": "Risk of real-world retaliatory action based on unverified evidence.",
        "action": "Await confirmation from ground or satellite sources."
    }
]

def analyze_text(text):
    text_lower = text.lower()
    
    # We will just do simple keyword matching, returning the first match found based on priority (or list order)
    for category in CATEGORIES:
        for kw in category["keywords"]:
            # Check if keyword is in text (word boundary is better but simple substring is fine too; let's use regex for word boundary to avoid false positives)
            if re.search(r'\b' + re.escape(kw) + r'\b', text_lower):
                return category
    
    # Default fallback
    return {
        "name": "Low priority / routine review",
        "urgency": "Low",
        "decision": "None immediate.",
        "consequence": "Standard baseline risk.",
        "action": "Standard review queue."
    }
