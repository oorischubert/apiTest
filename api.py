from flask import Flask, jsonify, request

details = {
  "046f43223d7080": {"name": "Box", "details": "This is Ooris Box!"},
  "8363": {"name": "Glasses", "details": "This is Ooris glasses case!"},
  "5435": {"name": "Speaker", "details": "This is Ooris speaker!"},
  "046f49223d7080": {"name": "Bottle", "details": "This is Ooris water bottle!"},
  "9835": {"name": "IPad", "details": "This is Ooris IPad!"},
  "3718": {"name": "Drone", "details": "This is Ooris Drone!"},
  "1026": {"name": "Bag", "details": "This is Ooris school bag!"},
  "6281": {"name": "Kindle", "details": "This is Ooris Kindle!"},
}

# creating the instance of our flask application
app = Flask(__name__)
@app.route('/uid',methods = ['GET', 'POST'])
def downloadRoute():
    if(request.method == 'GET'):
        return jsonify(details)
       
if __name__ == "__main__":
    app.run(debug=True)
