from flask import Flask, request, jsonify, render_template
from node_manager import NodeManager
from pod_scheduler import PodScheduler
from health_monitor import HealthMonitor

app = Flask(__name__)
node_manager = NodeManager()
pod_scheduler = PodScheduler(node_manager)
health_monitor = HealthMonitor(node_manager)

@app.route('/nodes', methods=['POST'])
def add_node():
    data = request.get_json()
    if not data or 'cpu_cores' not in data:
        return jsonify({'error': 'cpu_cores required'}), 400
    node_id = node_manager.add_node(data['cpu_cores'])
    return jsonify({'node_id': node_id, 'status': 'added'}), 201

@app.route('/nodes', methods=['GET'])
def list_nodes():
    health_monitor.check_health()
    nodes = node_manager.get_nodes()
    return jsonify({
        node_id: {
            'cpu_cores': node.cpu_cores,
            'available_cores': node.available_cores,
            'status': node.status,
            'pods': node.pods
        } for node_id, node in nodes.items()
    })

@app.route('/pods', methods=['POST'])
def launch_pod():
    data = request.get_json()
    if not data or 'cpu_cores' not in data:
        return jsonify({'error': 'cpu_cores required'}), 400
    pod_id, node_id = pod_scheduler.schedule_pod(data['cpu_cores'])
    if pod_id:
        return jsonify({'pod_id': pod_id, 'node_id': node_id, 'status': 'scheduled'}), 201
    return jsonify({'error': 'No suitable node found'}), 400

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.get_json()
    if not data or 'node_id' not in data:
        return jsonify({'error': 'node_id required'}), 400
    if health_monitor.record_heartbeat(data['node_id']):
        return jsonify({'status': 'received'}), 200
    return jsonify({'error': 'Node not found'}), 404

@app.route('/')
def dashboard():
    health_monitor.check_health()
    nodes = node_manager.get_nodes()
    return render_template('dashboard.html', nodes=nodes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
