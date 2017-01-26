from flask import Flask, jsonify,request,session
from helpers import *
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/get_quote', methods=['GET'])
def get_quotes():
    query = request.args.get('query',type=str)
    num_of_quotes = request.args.get('number_of_quotes',3,type=int)
    language = requests.args.get('lang','en',type=str)
    return jsonify({'quotes': give_quote(query, number_of_quotes=num_of_quotes, set_lang=language)})

@app.route("/api/quote_of_the_day", methods=['GET'])
def get_quote_of_the_day():
    language = request.args.get('lang','en',type=str)
    return jsonify({'quote_of_the_day' : quote_of_day(set_lang=language)})

@app.route('/api/random_quote', methods=['GET'])
def get_random_quote():
    query = request.args.get('query',type=str)
    return jsonify({'random_quote' : random_quote(query)})


if __name__ == '__main__':
    app.run(debug=True,threaded=True)