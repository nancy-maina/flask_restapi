import json
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'nancy',
                        'email': 'mainanancy700@gmail.com'})
app.run()