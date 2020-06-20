from flask import Flask, redirect, url_for, request, render_template, Response, jsonify
from gevent.pywsgi import WSGIServer

# Declare a Flask app
app = Flask(__name__)

print(' Loading complete. Check http://127.0.0.1:5000/')

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template("index.html")

if __name__ == '__main__':
    # Server the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
