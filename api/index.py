from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")

# Vercel handler
def handler(request, response):
    return app(request.environ, response.start_response)
