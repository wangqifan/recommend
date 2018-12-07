from flask import Flask,jsonify
from analyse import analyse
import py_eureka_client.eureka_client as eureka_client
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route("/<text>")
def analysetext(text):
    return  jsonify({"code":200,"data":analyse(text)})



server_port=8020
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init_registry_client(eureka_server="http://127.0.0.1:8761/eureka",
                                app_name="comment-analyse-service",
                                instance_port=server_port)


if __name__ == '__main__':
    app.run(port=server_port)
