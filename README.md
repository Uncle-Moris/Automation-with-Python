# Flask-React AWS CI/CD Project

This project aims to build a complete infrastructure for a web application composed of a Flask backend and a React frontend, using AWS services. The project includes the setup of continuous integration and continuous deployment (CI/CD) pipelines using GitHub Actions and deployment of the application on AWS Elastic Container Service (ECS).

## Project Overview

- **Backend**: Flask, a lightweight Python web framework, is used to handle server-side logic and API requests.
- **Frontend**: React, a popular JavaScript library, is used for building the user interface.
- **Containerization**: Both the Flask and React applications are containerized using Docker.
- **AWS Infrastructure**: The infrastructure is provisioned on AWS using services such as ECS (Elastic Container Service) and ECR (Elastic Container Registry) to manage and deploy Docker containers.
- **CI/CD Pipeline**: GitHub Actions is used to automate the build, test, and deployment process for both the frontend and backend components.

## Features

- **Automated Testing**: Unit tests are executed for both Flask and React applications to ensure code quality.
- **Dockerization**: The project includes Dockerfiles for both the Flask and React applications, enabling consistent and reproducible environments.
- **AWS Deployment**: The project is designed to deploy the application on AWS ECS, leveraging container orchestration for scalability and high availability.
- **Continuous Integration/Continuous Deployment (CI/CD)**: GitHub Actions are configured to automatically build, test, and deploy the application whenever changes are pushed to the repository.

## Getting Started

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Uncle-Moris/Flask_React_Deploy_AWS.git
   cd Flask_React_Deploy_AWS
   ```


2. **Backend (Flask)**:

Navigate to the ``cd src/server`` directory.
```bash
    #Install dependencies
    pip install -r requirements.txt
    #Run the Flask server
    python app.py
```


3. **Frontend (React)**

Navigate to the ``cd src/client`` directory.
```bash
    #Install dependencies
    npm install
    #Start the React development server
    npm start
```

## Deployment

### Dockerization

The project uses Docker to containerize the Flask and React applications. Dockerfiles are located in their respective directories (`src/server` and `src/client`).

### CI/CD Pipeline

GitHub Actions is used for CI/CD, which automates the following steps:

- **Testing**: Runs unit tests for both Flask and React applications.
- **Building Docker Images**: Builds Docker images for both applications.
- **Pushing to ECR**: Pushes the Docker images to Amazon Elastic Container Registry (ECR).
- **Deployment to ECS**: Updates the ECS service with the new Docker images.

### AWS Deployment

The application is deployed on AWS ECS, ensuring scalability and management of Docker containers. The deployment process is fully automated via the CI/CD pipeline.

## Technologies Used

- **Flask**: Python web framework
- **React**: JavaScript library for building user interfaces
- **Docker**: Containerization
- **AWS ECS**: Container orchestration
- **AWS ECR**: Docker image storage
- **GitHub Actions**: CI/CD automation
