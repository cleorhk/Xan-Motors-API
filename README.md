# Xan-Motors-API
Welcome to the Xan Motors API, a simple REST API built with Python and Flask. This project provides a basic implementation of CRUD (Create, Read, Update, Delete) operations for managing a collection of electric motors. It's a great starting point for learning how to build RESTful APIs and can be extended for more complex applications.

Features
Get all motors: Retrieve a list of all available motors.
Get a motor by ID: Retrieve details of a specific motor by its ID.
Create a new motor: Add a new motor to the collection.
Update a motor: Update the details of an existing motor.
Delete a motor: Remove a motor from the collection.

git clone https://github.com/yourusername/xan-motors-api.git
cd xan-motors-api

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

The API will be accessible at http://127.0.0.1:5000/.

API Endpoints
GET /motors: Get all motors
GET /motors/int:id: Get motor by ID
POST /motors: Create a new motor
PUT /motors/int:id: Update a motor
DELETE /motors/int:id: Delete a motor

Get all motors:

curl http://127.0.0.1:5000/motors

Get all motors by Id
curl http://127.0.0.1:5000/motors/1

create new motor
curl -X POST -H "Content-Type: application/json" -d '{"id": 3, "type": "AC", "power": "150W"}' http://127.0.0.1:5000/motors
update motor 
curl -X PUT -H "Content-Type: application/json" -d '{"type": "DC", "power": "300W"}' http://127.0.0.1:5000/motors/1
Delete a motor 
curl -X DELETE http://127.0.0.1:5000/motors/1

