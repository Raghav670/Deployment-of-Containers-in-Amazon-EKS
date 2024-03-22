# Project: Deployment of Containers in Amazon EKS

## Overview

This project focuses on demonstrating the deployment of containers in Amazon EKS (Elastic Kubernetes Service). For this demonstration, a PySpark application has been containerized and deployed using Amazon EKS.

## Architecture

![Poc-jupyterMoney drawio-dark](https://github.com/Raghav670/Deployment-of-Containers-in-Amazon-EKS/assets/74827764/65ff0608-2ca0-4655-af32-c14b6237da0b)



## Objectives

- Demonstrate the deployment process of containers in Amazon EKS.
- Containerize a PySpark application for demonstration purposes.

## Technologies Used

- Python
- Docker
- AWS EKS (Elastic Kubernetes Service)
- AWS ECS (Elastic Container Service)
- Kubernetes
- Apache Airflow
- Windows Subsystem for Linux (Ubuntu)

## Steps

### Step 1: Containerization of PySpark Application

- Install and import PySpark.
- Example PySpark files:
  - `t1.py`: Filters trip distance more than 5.
  - `t2.py`: Calculates total fare.
- **Benefits of Containerizing and Deploying PySpark Files**:
  - **Flexibility**: Containerizing PySpark applications allows for easy deployment across various environments without worrying about dependencies or compatibility issues.
  - **Scalability**: Containers can be scaled horizontally to handle large-scale data processing tasks efficiently, ensuring optimal resource utilization.
  - **Resource Efficiency**: Containers consume fewer resources compared to traditional virtual machines, leading to cost savings and improved performance.
  - **Isolation**: Each PySpark application runs within its container, providing isolation and preventing interference from other applications or processes.
  - **Consistency**: Docker containers ensure consistent behavior across different environments, making it easier to reproduce results and debug issues.
  - **Integration**: Deploying PySpark applications in Kubernetes (EKS) allows seamless integration with other cloud services and tools for monitoring, logging, and orchestration.
- Dockerfile specifications:
  - Base image: `python:3.8-slim`.
  - Set the working directory to `/app`.
  - Copy files into the container.
  - Install PySpark.
  - Expose port 8080 (if needed).
  - Set Python version for PySpark.
  - Specify default command.

### Step 2: Pushing Docker Image to ECS

- Create a new repository in ECS (Elastic Container Registry).

- Retrieve an authentication token and authenticate your Docker client to your registry:
  ```bash
  aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin <id>.dkr.ecr.<region>.amazonaws.com

- Build your Docker image using the following command:
  ```bash
  docker build -t <image name> .
- After the build completes, tag your image so you can push the image to this repository:
  ```bash
  docker tag <image_name>:latest <id>.dkr.ecr.<region>.amazonaws.com/<repo_name>:latest

### Step 3: Deploying in EKS

- Install `kubectl`.
- Create an EKS cluster and node group.
- Configure `kubectl` with cluster credentials.
- Write a deployment YAML file (you can find the sample in the deployment.yaml file above).
- Apply the deployment to the EKS cluster.
  ```bash
  kubectl apply -f deployment.yaml
- Verify Deployment
  ```bash
  kubectl get deployment
  kubectl get pods

### Airflow

Note: Working Airflow in Windows is confusing. So for Airflow, I have utilized WSL(Windows Subsystem for Linux- ubuntu )

1. Install Apache Airflow using pip.
3. Optionally, set up the Airflow home directory.
4. Initialize the database and create an admin user.
   ```bash
   airflow users create --username <username> --firstname <firstname> --lastname <lastname> --role <role> --email <email>

5. To initialize db
    ```bash
    airflow db init
    
6. Access Airflow Web UI.
   ```bash
   airflow webserver -p 8080

8. Create a DAGs folder and place custom DAG files.
   -This command creates a directory named dags inside the ~/airflow directory.
   ```bash
   mkdir ~/airflow/dags

   cp airflow_scheduler.py ~/airflow/dags/
   
10. Run custom DAGs by refreshing and starting the Airflow webserver.

-To  start scheduler
  ```bash
     airflow scheduler
