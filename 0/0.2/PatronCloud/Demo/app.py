from flask import Flask, request, jsonify
from prometheus_client import Counter
from redis import Redis
import uuid
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  
redis = Redis(host='redis', port=6379)


appointments_created = metrics.counter('appointments_created', 'Total number of appointments created')
appointments_processed = metrics.counter('appointments_processed', 'Number of appointments processed')

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    appointment_id = str(uuid.uuid4())
    redis.rpush('appointments', appointment_id)

    return jsonify({'id': appointment_id}), 201

@app.route('/appointments/<id>', methods=['GET'])
def get_appointment(id):
    appointments = redis.lrange('appointments', 0, -1)
    if id.encode() in appointments:
        return jsonify({'id': id}), 200
    return jsonify({'error': 'Appointment not found'}), 404

@app.route('/appointments/<id>', methods=['DELETE'])
def delete_appointment(id):
    result = redis.lrem('appointments', 0, id)
    if result == 0:
        return jsonify({'error': 'Appointment not found'}), 404
    return jsonify({'message': 'Appointment deleted'}), 200

@app.route('/appointments', methods=['GET'])
def list_appointments():
    appointments = redis.lrange('appointments', 0, -1)
    return jsonify([a.decode('utf-8') for a in appointments]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
