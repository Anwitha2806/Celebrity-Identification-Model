from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hi"

#image is converted into a base64 encoded string when passed on to UI and passed into the backend
#other option could be convert the image into a s3 url and pass it via URL

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)