import Flask, redirect, url_for, request, render_template, Response, jsonify

# Declare a Flask app
app = Flask(__name__)

print(' Loading complete. Check http://127.0.0.1:5000/')

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template("index.html")
