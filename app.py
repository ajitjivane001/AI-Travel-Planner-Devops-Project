from google import genai
from flask import Flask, render_template, request

client = genai.Client(api_key="AIzaSyAhnW7vrJAtyyG3GHHcvD0GbOTSTXPbjVc")
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        v1=request.form.get('inp1')
        v2=int(request.form.get('inp2'))
        v3=int(request.form.get('inp3'))
        v4=request.form.get('inp4')

        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=f"user want to plan a trip to{v1} and his budget is {v2} users want to stay for{v3} days and users intrest is {v4} mandeterilly genrate the output in html format"
        )
        result=response.text
        return render_template('result.html',res=result)

app.run(debug=True)