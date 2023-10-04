from flask import Flask, request

app = Flask("regulation-service")


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/api/regulation/receive-data', methods=['POST'])
def print_data():
    data = request.get_json()  # Assumes the incoming data is in JSON format
    if data:
        print("Received data:", data)
        return 'Data received and printed!'
    else:
        return 'No data received.'


if __name__ == '__main__':
    app.run(port=8081)
