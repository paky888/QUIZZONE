from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Add more routes as needed

if __name__ == "__main__":
    # Set the host to 0.0.0.0 for external access and use the port from the environment or default to 5000
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
