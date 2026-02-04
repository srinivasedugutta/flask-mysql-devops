pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'srinivasedugutta'
        IMAGE_NAME = 'flask-mysql-app'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/srinivasedugutta/flask-mysql-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKERHUB_USER/$IMAGE_NAME:latest .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh 'docker push $DOCKERHUB_USER/$IMAGE_NAME:latest'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh '''
                docker rm -f mysql two-tier-app || true
                docker compose down || true
                docker compose up -d
                '''
            }
        }

    }
}
