from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def hello_world():
        return "Hello world!"

@app.route('/api/images_list')
def images_list(path):
    image_files = os.listdir("static/images")
    image_file = [ f for f in image_files if ".jpeg" in f]
    print(image_files)
    return send_from_directory("api", "images.json")

@app.route('/static/<path:path>', methods=['GET'])
def serve_file_in_dir(path):
    return send_from_directory("static", path)