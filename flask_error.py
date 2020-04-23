from flask import Flask, jsonify


app = Flask(__name__)  # 可以更改为自己想要的任意名字


@app.errorhandler(500)
def error_handling(error):
    return jsonify({'Error': str(error), 'code': 500}, 500)

@app.route("/api")
def my_microservice():
    raise ValueError("====")


if __name__ == "__main__":
    app.run()
