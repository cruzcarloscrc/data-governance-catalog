from flask import Flask

# main.py
"""
Data Governance Catalog
Author: [Your Name]
Description: Main entry point for the Data Governance Catalog project.
"""


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Data Governance Catalog!"

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)