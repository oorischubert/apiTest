from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users',methods = ['GET'])
def index():
    return jsonify({'greetings' : "Hi this is Oori"})

if __name__ == "__main__":
    app.run(debug = True) 