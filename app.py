from flask import Flask, jsonify, request
from flask_ngrok import run_with_ngrok
from dotenv import load_dotenv
import os
import openai


load_dotenv()

app = Flask(__name__)
run_with_ngrok(app)




@app.route('/')
def appname():  
   return "Hello World!"



@app.route("/demo", methods=['POST'])
def keywords():

    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    ptext = request.json['ptext']
    response = openai.Completion.create(
  model="text-davinci-002",
  prompt= ptext,
  temperature=0.3,
  max_tokens=2500,
  top_p=1,
  frequency_penalty=0.8,
  presence_penalty=0
)

    print(response.choices[0].text)
    keywords = response.choices[0].text
    return jsonify(keywords)
    









if __name__ == "__main__":
    
    app.run()

    