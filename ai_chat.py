from flask import Blueprint, request, jsonify, session
import openai
from database import get_connection

ai_chat_bp = Blueprint("ai_chat", __name__)

# Replace with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@ai_chat_bp.route("/chat", methods=["POST"])
def chat():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Login required to chat with AI"}), 401

    data = request.json
    message = data.get("message", "")
    language = data.get("language", "en")  # "en" or "ar"

    if not message:
        return jsonify({"error": "Message is required"}), 400

    # Construct AI prompt
    prompt = f"You are a helpful assistant for Mohammed Hamdan AlShehhi Ladies Tailoring & Embroidery.\n"
    prompt += f"Language: {language}\n"
    prompt += f"User message: {message}\n"
    prompt += "Provide a helpful, concise, and professional response."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional assistant for a fashion e-commerce website."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        reply = response.choices[0].message['content'].strip()
    except Exception as e:
        reply = f"AI response error: {str(e)}"

    # Optional: save conversation in DB
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT,
            response TEXT
        )
    """)
    cursor.execute("INSERT INTO ai_chat (user_id, message, response) VALUES (?, ?, ?)",
                   (user_id, message, reply))
    conn.commit()
    conn.close()

    return jsonify({"reply": reply})
