from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    print("Hostname : ", hostname)
    print("IP : ", host_ip)
    return str(hostname), str(host_ip)
 
@app.route("/")
def hello_world():
    return "<p>Hello, Python World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)