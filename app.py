from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Brain cards is alive"

@app.route("/health")
def health():
    return {"status": "ok", "app": "brain-cards"}

if __name__ == "__main__":
    app.run(debug=True, port=5001)