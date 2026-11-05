from flask import Flask, jsonify,request

app = Flask(__name__)

# Smart fan initial state

device = {
    "device_id": "FAN001",
    "connected": True,
    "online": True,
    "fan_speed": 1,
    "temperature": 28
}


@app.route('/', methods=['GET'])
def home():

    return jsonify({
        "message": "Welcome to Smart Device Automation System",
        "status": "Running"
    })


# Get device status

@app.route('/device/status', methods=['GET'])
def device_status():

    return jsonify(device)

# Update fan speed

@app.route('/device/speed', methods=['POST'])
def update_speed():

    data = request.get_json()

    speed = data.get('speed')

    if not isinstance(speed, int) or isinstance(speed, bool):
        return jsonify({
            "error": "Speed must be an integer"
        }), 400

    if speed < 1 or speed > 5:
        return jsonify({
            "error": "Speed must be between 1 and 5"
        }), 400

    if not device["connected"]:
        return jsonify({
            "error": "Device is disconnected"
        }), 409

    device["fan_speed"] = speed

    return jsonify({
        "message": "Fan speed updated successfully",
        "fan_speed": device["fan_speed"]
    }), 200

# Connect the smart device

@app.route('/device/connect', methods=['POST'])
def connect_device():

    device["connected"] = True
    device["online"] = True

    return jsonify({
        "message": "Device connected successfully",
        "connected": True
    }), 200
# Disconnect the smart device

@app.route('/device/disconnect', methods=['POST'])
def disconnect_device():

    device["connected"] = False
    device["online"] = False

    return jsonify({
        "message": "Device disconnected successfully",
        "connected": False
    }), 200

if __name__ == '__main__':

    app.run(debug=True)