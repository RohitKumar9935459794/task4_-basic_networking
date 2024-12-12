from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received data:", data)

    # Mock response, you can customize it as needed
    response = {
        "status": "success",
        "message": "Data received successfully"
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
