from flask import Flask, jsonify, request
import json

details = {
  "8782": {"name": "Box", "details": "This is Ooris Box!"},
  "8363": {"name": "Glasses", "details": "This is Ooris glasses case!"},
  "5435": {"name": "Speaker", "details": "This is Ooris speaker!"},
  "8025": {"name": "Bottle", "details": "This is Ooris water bottle!"},
  "9835": {"name": "IPad", "details": "This is Ooris IPad!"},
  "3718": {"name": "Drone", "details": "This is Ooris Drone!"},
  "1026": {"name": "Bag", "details": "This is Ooris school bag!"},
  "6281": {"name": "Kindle", "details": "This is Ooris Kindle!"},
}

# creating the instance of our flask application
app = Flask(__name__)
@app.route('/uid',methods = ['GET', 'POST'])
def uploadRoute():
    global response
    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        return ' '
    else:
        return jsonify({'uid' : details[request_data["uid"]]})
       

if __name__ == "__main__":
    app.run(debug=True)
