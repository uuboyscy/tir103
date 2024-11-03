from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello!</h1><h2>hello</h2>"
    # return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
