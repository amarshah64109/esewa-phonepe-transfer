from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/verify_esewa', methods=['POST'])
def verify_esewa():
    data = request.json
    # Add your verification logic here
    return jsonify({"message": "eSewa verified successfully"})

@app.route('/transfer_phonepe', methods=['POST'])
def transfer_phonepe():
    data = request.json
    # Add your transfer logic here
    return jsonify({"message": "Money transferred to PhonePe successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
