import uuid

class Node:
    def __init__(self, cpu_cores):
        self.id = str(uuid.uuid4())
        self.cpu_cores = cpu_cores
        self.available_cores = cpu_cores
        self.status = "running"
        self.pods = []

class Pod:
    def __init__(self, cpu_cores):
        self.id = str(uuid.uuid4())
        self.cpu_cores = cpu_cores
