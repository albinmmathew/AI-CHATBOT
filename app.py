from flask import Flask, render_template, request
from amm_geminiassist import get_response
from dotenv import load_dotenv

load_dotenv(override=True)  # This will now work

app = Flask(__name__)

# Store previous queries & responses
history = []

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_input = request.form.get("user_text")

        if not user_input.strip():
            response = "❌ Please enter some text."
        else:
            try:
                # Call your Gemini AI helper function
                response = get_response(user_input)
                print(response)
            except Exception as e:
                response = f"⚠️ Error: {e}"

            history.append({"query": user_input, "response": response})

    return render_template("index.html",
                           response=response,
                           history=history)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
