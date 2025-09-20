from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
      <head><title>Qucoon Academy — Lagos</title></head>
      <body style="font-family:system-ui;line-height:1.6;padding:2rem;">
        <h1>Qucoon Academy — Lagos</h1>
        <p>Qucoon Academy is a tech training academy located in Lagos focused on cloud engineering, architecture, and hands-on training.</p>
        <p>Specialties: cloud engineering, backend development, mentorship, and job-readiness.</p>
        <p>Prepared by: Melvin</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
