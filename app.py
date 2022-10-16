from flask import Flask, request, jsonify
from url_summarizer import url_summary
app = Flask(__name__)

@app.route('/')
def hello_world():
    args = request.args
    url = args["url"]
    us = url_summary()
    return us.summarizeURL(url,5)

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)