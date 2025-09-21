from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Melvine | Cloud Engineer</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #1E3C72, #2A5298);
                color: #fff;
                text-align: center;
            }
            header {
                padding: 60px 20px;
            }
            header h1 {
                font-size: 50px;
                margin-bottom: 10px;
            }
            header p {
                font-size: 20px;
                margin-top: 0;
                color: #ddd;
            }
            section {
                background: #fff;
                color: #333;
                margin: 40px auto;
                padding: 40px;
                max-width: 900px;
                border-radius: 15px;
                box-shadow: 0 6px 18px rgba(0,0,0,0.2);
                text-align: left;
            }
            section h2 {
                color: #1E3C72;
                border-bottom: 2px solid #2A5298;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            ul li {
                margin: 10px 0;
                font-size: 18px;
            }
            footer {
                background: #111;
                padding: 20px;
                margin-top: 40px;
                font-size: 14px;
                color: #aaa;
            }
            footer a {
                color: #4CAF50;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>🌍 Cloud Engineering Journey</h1>
            <p>Hi, I’m <strong>Melvine</strong> — Cloud Engineering & Architecture Student at Qucoon Academy 🚀</p>
        </header>

        <section>
            <h2>About This Project</h2>
            <p>This web application is a <strong>Flask project</strong> deployed on <strong>AWS EC2</strong> using 
            <strong>GitHub Actions</strong>.  
            It is a proof of concept that shows how <em>automation</em>, <em>cloud deployment</em>, and 
            <em>continuous integration</em> come together in real-world projects.</p>
        </section>

        <section>
            <h2>Skills I’m Building</h2>
            <ul>
                <li>☁️ Cloud Platforms: AWS (EC2, S3, Lambda, RDS, VPC)</li>
                <li>⚙️ Infrastructure as Code: Terraform, CloudFormation</li>
                <li>🐧 Linux Systems: Shell scripting, automation</li>
                <li>🔄 CI/CD Pipelines: GitHub Actions, Jenkins</li>
                <li>📦 Containers & Deployment: Docker</li>
                <li>🛡️ Security: IAM, Networking & Firewalls</li>
            </ul>
        </section>

        <section>
            <h2>How It Works</h2>
            <ol>
                <li>Code is written in Python (Flask).</li>
                <li>Changes are pushed to GitHub.</li>
                <li>GitHub Actions workflow deploys automatically to EC2.</li>
                <li>The app runs as a systemd service, always available.</li>
            </ol>
        </section>

        <footer>
            © 2025 | Built by Melvine | Cloud Engineering & Architecture 🚀  
        </footer>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
