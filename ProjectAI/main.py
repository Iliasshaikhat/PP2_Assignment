from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from openai import OpenAI
import os

# OpenAI client (API key is taken from environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(title="AI Health Consultant")

SYSTEM_PROMPT = """
You are an AI health consultant.
You are NOT a doctor.

STRICTLY FORBIDDEN:
- Making medical diagnoses
- Prescribing medications or dosages

YOU ARE ALLOWED TO:
- Explain possible causes of symptoms
- Assess urgency level (low / medium / high)
- Recommend which doctor to consult

ALWAYS:
- State that this is not a medical diagnosis
- Advise seeing a doctor if symptoms are severe or worsening
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Health Consultant</title>
    </head>
    <body>
        <h2>🩺 AI Health Consultant</h2>
        <p><b>⚠️ This is NOT a medical diagnosis</b></p>

        <form method="post" action="/consult">
            <textarea name="symptoms" rows="6" style="width:100%;"
            placeholder="Describe your symptoms..."></textarea><br><br>
            <button type="submit">Get Consultation</button>
        </form>
    </body>
    </html>
    """

@app.post("/consult", response_class=HTMLResponse)
def consult(symptoms: str = Form(...)):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": symptoms}
        ],
        temperature=0.4
    )

    answer = response.choices[0].message.content

    return f"""
    <html>
    <body>
        <h2>📋 Consultation Result</h2>
        <p>{answer.replace(chr(10), "<br>")}</p>
        <hr>
        <p><b>⚠️ This AI does not replace a medical professional.</b></p>
        <a href="/">← Back</a>
    </body>
    </html>
    """
