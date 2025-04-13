from models import Pod

class PodScheduler:
    def __init__(self, node_manager):
        self.node_manager = node_manager

    def schedule_pod(self, cpu_cores):
        pod = Pod(cpu_cores)
        nodes = self.node_manager.get_nodes()
        for node_id, node in nodes.items():
            if node.status == "running" and node.available_cores >= cpu_cores:
                node.available_cores -= cpu_cores
                node.pods.append(pod.id)
                return pod.id, node_id
        return None, None
