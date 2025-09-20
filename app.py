from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>Qucoon Academy</title></head>
        <body>
            <h1>Welcome to Qucoon Academy</h1>
            <p>Qucoon Academy is a tech training academy in Lagos.</p>
            <p>Hi! I’m learning <strong>cloud engineering and architecture</strong> here. This project is a demonstration of my skills.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
