# DataFlows Project

This project contains an Airflow setup using Docker and Docker Compose to create data pipelines. It includes:
- Airflow DAGs
- Custom scripts
- Preloaded data

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/theosato/dataflows.git
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Access the Airflow web UI at `http://localhost:8080`.

## Directory Structure

dataflows<br>
├── dags/<br>
├── data/<br>
├── output/ (optional; typically excluded)<br>
├── plugins/<br>
├── scripts/<br>
├── Dockerfile<br>
├── docker-compose.yml<br>
├── requirements.txt<br>
└── README.md (optional but recommended)