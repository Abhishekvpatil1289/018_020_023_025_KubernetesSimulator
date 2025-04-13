import time

class HealthMonitor:
    def __init__(self, node_manager, heartbeat_timeout=30):
        self.node_manager = node_manager
        self.heartbeat_timeout = heartbeat_timeout
        self.last_heartbeat = {}

    def record_heartbeat(self, node_id):
        if node_id in self.node_manager.get_nodes():
            self.last_heartbeat[node_id] = time.time()
            return True
        return False

    def check_health(self):
        current_time = time.time()
        for node_id, node in self.node_manager.get_nodes().items():
            last_beat = self.last_heartbeat.get(node_id, 0)
            node.status = "failed" if current_time - last_beat > self.heartbeat_timeout else "running"
