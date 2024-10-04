from flask import Flask, render_template, request, redirect
import requests
import api as api
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ip')
def ip():
    ip = request.args.get('ip')
    print(ip)
    if ip == None: return redirect('/', 302)
    return render_template('ip.html', result= api.getip(ip))


if __name__ == "__main__":
    app.run("0.0.0.0", 8000, True)