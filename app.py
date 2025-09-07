from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Abusive words list (English + Roman Urdu)
abusive_words = [
    "badword1", "badword2", "stupid", "idiot", "chutiya", "bhosda", "kamina",
    "haramkhor", "ullu", "bitch", "bastard", "fuck", "gandu", "madarchod",
    "lavde", "randi", "kanjar", "bewakoof", "nalayak", "harami", "chod",
    "lund", "gaand", "kutte", "suvar", "tatti", "bhosri", "chakka", "idiot", "stupid", "fuck", "bitch", "loser", "trash", "kill", "die", "slut", "whore",     "badword", "stupid", "idiot", "nonsense", "fool", "hate",
    "dumb", "loser", "shut up", "ugly", "trash", "garbage",
    "moron", "nasty", "kill", "disgusting", "dirty", "crazy",
    "noob", "psycho", "pathetic", "toxic", "bloody", "suck",
    "jerk", "mad", "useless", "worthless", "creep", "evil",
    "pig", "dog", "donkey", "coward", "failure", "shit", "bitch",
    "bastard", "fuck", "asshole", "slut", "dick", "pervert", "cunt",     "badtameez", "ganda", "ullu", "ullu ka pattha", "pagal", "chutiya",
    "haramzada", "haramzadi", "lanat", "ghatiya", "bewakoof", "nalayak",
    "kamina", "kamini", "kutti", "kutta", "gadha", "gandi soch",
    "chor", "besharam", "beghairat", "kanjar", "randi", "bhosda",
    "gaand", "choot", "jhant", "kamzor", "budtameez", "bakwas",
    "faltu", "nalayiq", "lutera", "dhoka", "cheap", "fattu",
    "ghanda", "tharki", "tatti", "faaltu", "bewaqoof", "buray", "gndy", "chutiya", "bsdk", "bkl", "behn ka lora", "gaand", "fuck you", "go to hell", "bc" 
]


def is_abusive(message: str) -> bool:
    text = message.lower()
    for word in abusive_words:
        # \b ensures only whole words match (not substrings)
        if re.search(rf"\b{re.escape(word)}\b", text):
            return True
    return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_comment", methods=["POST"])
def check_comment():
    data = request.get_json()
    comment = data.get("comment", "").strip()

    if not comment:  # empty check
        return jsonify({"status": "blocked", "message": "⚠️ Please type something!"})

    if is_abusive(comment):
        return jsonify({"status": "blocked", "message": "⚠️ Comment Blocked!"})
    else:
        return jsonify({"status": "allowed", "message": "✅ Comment Posted!"})

if __name__ == "__main__":
    app.run(debug=True)