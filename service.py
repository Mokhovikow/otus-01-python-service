from flask import Flask, redirect, url_for, request, json
from response import Response, ResponseEncoder

app = Flask(__name__)

@app.route("/health/", methods=['GET'])
def health():
    if request.method == "GET":
        status = Response()
        statusJson = json.dumps(status, indent=4, cls=ResponseEncoder)
        return statusJson
    else: 
        return redirect(url_for("index"))

@app.errorhandler(404)
def notFoundHandler(error):
    return redirect(url_for("health"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)