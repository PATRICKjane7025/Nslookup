from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def nslookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        return {"domain": domain, "ip": ip, "error": None}
    except socket.gaierror as e:
        return {"domain": domain, "ip": None, "error": f"Error resolving domain: {e}"}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        domain = request.form.get("domain")
        if domain:
            result = nslookup(domain)
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=True)
