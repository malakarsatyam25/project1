from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, my name is satyam malakar!"

if __name__ == "__main__":
    app.run(debug=True)
