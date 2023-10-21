# https://stackoverflow.com/questions/61443935/ssh-service-running-on-multiple-ports-with-custom-rules-in-linux
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04
# https://flask.palletsprojects.com/en/3.0.x/deploying/nginx/
# https://flask.palletsprojects.com/en/3.0.x/deploying/proxy_fix/
from flask import Flask, render_template, request
import requests
import socket
from werkzeug.middleware.proxy_fix import ProxyFix
app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

pico_addr = 'http://' +'192.168.1.27:5001' + '/'
@app.route("/")
def home():
    print('test')
    return render_template('home.html')

@app.route("/pico_test")
def pico_test():
    global pico_addr
    try:
        pico_addr= socket.gethostbyname('picow')
    except:
        print("Can't get picow, going by default")
    print("Pinging Pico Server")
    p_ret = requests.get(pico_addr+'test')
    print(p_ret.content)
    return p_ret.content
