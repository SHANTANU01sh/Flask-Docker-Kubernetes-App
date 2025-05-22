# 📝 Task Management App

A lightweight Flask web application for managing personal tasks, designed with simplicity and scalability in mind. Dockerized for containerization and deployed using Kubernetes for easy scaling and orchestration.

---

## 🚀 Features

- Add, complete, and delete tasks
- Persistent storage using SQLite
- Docker support for easy deployment
- Kubernetes configuration for scaling and service exposure

---

## 📁 Project Structure

task-manager/
├── app/ # Flask app logic (routes, models)
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ └── templates/
│ └── index.html
├── static/ # CSS styles
│ └── style.css
├── app.py # Entry point of the Flask app
├── config.py # App configuration
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image definition
├── .dockerignore # Docker ignore file
└── k8s/ # Kubernetes manifests
├── deployment.yaml
└── service.yaml

---

## 🧪 Run Locally (Dev Mode)

### Prerequisites

- Python 3.11+
- pip

### Instructions

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
Visit http://localhost:5000

🐳 Run with Docker

Build & Run
docker build -t task-manager .
docker run -d -p 5000:5000 task-manager

☸️ Deploy with Kubernetes
Prerequisites
Docker
Kubernetes (e.g., Minikube or cloud)
kubectl CLI

Steps
1. Replace the image name in k8s/deployment.yaml with your DockerHub repo.
2. Push the image:
docker tag task-manager your-dockerhub-username/task-manager:latest
docker push your-dockerhub-username/task-manager:latest

3. Deploy to Kubernetes:
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

4. If using Minikube:
minikube service task-manager-service

🛠 Technologies Used
Python 3.11
Flask
SQLite
Docker
Kubernetes

🙋‍♂️ Author
Shantanu
