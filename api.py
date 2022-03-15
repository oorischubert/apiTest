from flask import Flask, jsonify, request
import json
import pickle

response = ''
# creating the instance of our flask application
app = Flask(__name__)
@app.route('/upload',methods = ['GET', 'POST'])
def uploadRoute():
    global response
    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        response = request_data['post']
        pickle.dump(response, open("post.txt", 'wb'))
        return " "
    else:
        pickledResp = pickle.load(response, open("post.txt", 'rb'))
        return jsonify({'post': pickledResp})


if __name__ == "__main__":
    app.run(debug=True)
