from __init__ import app

import py_eureka_client.eureka_client as eureka_client


server_port=8010
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init_registry_client(eureka_server="http://127.0.0.1:8761/eureka",
                                app_name="recommend-service",
                                instance_port=server_port)

if __name__ =='__main__': 
    app.run(port=server_port)
