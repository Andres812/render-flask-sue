from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Si jalo bien :)"

if __name__ == "__main__":
    app.run()