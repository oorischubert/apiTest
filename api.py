from flask import Flask, jsonify, request
import json

response = ''
# creating the instance of our flask application
app = Flask(__name__)
@app.route('/upload',method = ['GET', 'POST'])
def uploadRoute():
    global response
    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        upload = request_data['upload']
        responce = f'Upload: {upload}'
        return " "
    else:
        return jsonify({'upload', response})


if __name__ == "__main__":
    app.run(debug=True)