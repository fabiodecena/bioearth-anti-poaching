from flask import Flask

app = Flask(__name__)

@app.after_request
def add_release_header(response):
    response.headers["X-BioEarth-Release"] = "release-6"
    return response

@app.route("/")
def home():
    return "Protect Wildlife!!! v5"

@app.route("/health")
def health():
    return {"status": "ok", "version": "v3"}, 200

@app.route("/version")
def version():
    return {"version": "v3"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)