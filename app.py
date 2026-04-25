import os
import google.generativeai as genai
from flask import Flask, render_template, request

# Configure API key securely
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        v1 = request.form.get('inp1')
        v2 = int(request.form.get('inp2'))
        v3 = int(request.form.get('inp3'))
        v4 = request.form.get('inp4')

        prompt = f"""
        User wants to plan a trip to {v1}.
        Budget: {v2}
        Duration: {v3} days
        Interests: {v4}

        Generate the output in clean HTML format.
        """

        response = model.generate_content(prompt)

        result = response.text

        return render_template('result.html', res=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
