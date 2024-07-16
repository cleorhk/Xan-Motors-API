from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
motors = [
    {'id': 1, 'type': 'AC', 'power': '100W'},
    {'id': 2, 'type': 'DC', 'power': '200W'}
]


# Home route
@app.route('/')
def home():
    return "Welcome to the Xan Motors API!"


# Get all motors
@app.route('/motors', methods=['GET'])
def get_motors():
    return jsonify(motors)

# Get motor by ID
@app.route('/motors/<int:id>', methods=['GET'])
def get_motor(id):
    motor = next((motor for motor in motors if motor['id'] == id), None)
    if motor:
        return jsonify(motor)
    return jsonify({'message': 'Motor not found'}), 404

# Create a new motor
@app.route('/motors', methods=['POST'])
def create_motor():
    new_motor = request.get_json()
    motors.append(new_motor)
    return jsonify(new_motor), 201

# Update a motor
@app.route('/motors/<int:id>', methods=['PUT'])
def update_motor(id):
    motor = next((motor for motor in motors if motor['id'] == id), None)
    if motor:
        updates = request.get_json()
        motor.update(updates)
        return jsonify(motor)
    return jsonify({'message': 'Motor not found'}), 404


# Delete a motor
@app.route('/motors/<int:id>', methods=['DELETE'])
def delete_motor(id):
    motor = next((motor for motor in motors if motor['id'] == id), None)
    if motor:
        motors.remove(motor)
        return jsonify({'message': 'Motor deleted'})
    return jsonify({'message': 'Motor not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
