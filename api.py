from flask import Flask, jsonify, request
import json

f1 = open('post.txt','w')
f2 = open('post.txt','r')
# creating the instance of our flask application
app = Flask(__name__)
@app.route('/upload',methods = ['GET', 'POST'])
def uploadRoute():
    global response
    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        f1.write(request_data['post'])
        return " "
    else:
        responce = f2.read()
        return responce.jsonify({'post': response})


if __name__ == "__main__":
    app.run(debug=True)