import os
import requests
import time

NODE_ID = os.getenv("NODE_ID", "node-default")
CPU_CORES = os.getenv("CPU_CORES", "4")
API_SERVER_URL = "http://localhost:5000"

def send_heartbeat():
    while True:
        try:
            response = requests.post(
                f"{API_SERVER_URL}/heartbeat",
                json={"node_id": NODE_ID}
            )
            print(f"Heartbeat sent: {response.json()}")
        except Exception as e:
            print(f"Heartbeat failed: {e}")
        time.sleep(10)

if __name__ == "__main__":
    print(f"Node {NODE_ID} started with {CPU_CORES} CPU cores")
    send_heartbeat()
