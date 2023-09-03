from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """
    This is the home url functoin.

    args: None
    returns: html
    """
    return render_template("index.html", title="Hello")

if __name__ == "__main__":
    app.run()
