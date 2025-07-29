
from flask import Flask, render_template_string # type: ignore
import requests

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Gautam IP Address</title>
    <style>
        body { font-family: Arial; background: #f2f2f2; text-align: center; padding-top: 100px; }
        .card { background: white; padding: 40px; margin: auto; width: 400px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Your Public IP:</h1>
        <h2>{{ ip }}</h2>
    </div>
</body>
</html>
"""

@app.route("/")
def show_ip():
    ip = requests.get('https://api.ipify.org').text
    return render_template_string(TEMPLATE, ip=ip)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
