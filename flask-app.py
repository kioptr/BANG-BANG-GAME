from flask import Flask
app = Flask(__name__)
@app.route("/")
def joke():
    return "I haven't slept for three days, because that would be too long"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)