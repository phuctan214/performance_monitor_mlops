from flask import Flask, request

PORT = 6789

app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def test():
    data = request.json
    print(data)
    ## Add trigger training here
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
