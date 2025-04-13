# Kubernetes Simulator (018_020_023_025)

A mini-project simulating core Kubernetes features, including node management, pod scheduling, health monitoring, a command-line interface (CLI), and a web-based UI dashboard. Built with Python, Flask, Docker, and a custom API server, this project demonstrates a simplified Kubernetes-like cluster for educational purposes.

## Team
- **SRNs**: 018, 020, 023, 025
- **Name**: Abhishek Patil ,Abhishek G M , Achyuth K , Adarsh 
- **Institution**: PES University
- **Course**:  Cloud Computing


## Project Overview
The Kubernetes Simulator replicates key Kubernetes functionalities in a lightweight, local environment:
- **Node Management**: Add and track nodes with CPU core allocations.
- **Pod Scheduling**: Assign pods to nodes based on resource requirements using a First-Fit algorithm.
- **Health Monitoring**: Detect node failures (no heartbeats for 30 seconds) and mark nodes as "failed."
- **CLI**: User-friendly commands (`add-node`, `launch-pod`) to interact with the cluster.
- **UI Dashboard**: A Flask-based web interface (`http://localhost:5000`) to visualize nodes, pods, and their statuses in real-time.
- **Docker Integration**: Nodes run as Docker containers for scalability and isolation.

This project was developed over two weeks:
- **Week 1**: Focused on node management and API setup.
- **Week 2**: Added pod scheduling, health monitoring, CLI improvements, and the UI dashboard.

## Weekly Progress
### Week 1
- **Node Addition**:
  - Implemented CLI command: `add-node <cores>` to create nodes with specified CPU cores.
  - Built API endpoint: `POST /nodes` to register nodes.
  - Created `node_service.py` to run nodes as Docker containers, reporting CPU and status.
- **API Server**:
  - Developed `api_server/app.py` with Flask to handle node registration.
  - Added `GET /nodes` to list all nodes (ID, cores, status).
- **Docker Setup**:
  - Created `node/Dockerfile` for containerized node services.
  - Tested node creation and listing via CLI and API.

### Week 2
- **Pod Scheduling**:
  - Added CLI command: `launch-pod <cores>` to schedule pods on nodes.
  - Implemented `POST /pods` API to assign pods using a First-Fit algorithm (selects first node with sufficient cores).
  - Updated `node_manager.py` and `pod_scheduler.py` for resource tracking.
- **Health Monitoring**:
  - Built `health_monitor.py` to track node heartbeats.
  - Nodes failing to send heartbeats for 30 seconds are marked "failed" (status reflected in API and UI).
- **CLI Improvements**:
  - Fixed parsing errors in `client/cli.py`.
  - Optimized commands for reliability (e.g., validated core inputs).
- **UI Dashboard**:
  - Developed `api_server/templates/dashboard.html` using Flask.
  - Visualizes nodes (ID, cores, status) and pods (ID, assigned node) in a table.
  - Accessible at `http://localhost:5000`, updates in real-time.

## Project Structure
