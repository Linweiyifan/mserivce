from flask import Flask, jsonify


app = Flask(__name__)  # 可以更改为自己想要的任意名字


@app.route("/api")
def my_microservice():
    return jsonify({'Hello': 'world'})  # 返回json对象


if __name__ == "__main__":
    app.run()
