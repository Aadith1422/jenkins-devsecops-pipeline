
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing application dependencies...'
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt bandit
                '''
            }
        }

        stage('Automated Testing') {
            steps {
                echo 'Running Pytest...'
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('SAST - Bandit Security Scan') {
            steps {
                echo 'Scanning Python source code with Bandit...'
                sh '''
                    .venv/bin/bandit -r app/ \
                        -f json \
                        -o bandit-report.json \
                        --exit-zero
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'bandit-report.json',
                                     allowEmptyArchive: true
                }
            }
        }

        stage('SonarQube Cloud Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQubeCloud-DevSecOps') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=Aadith1422_jenkins-devsecops-pipeline \
                            -Dsonar.organization=aadith1422 \
                            -Dsonar.sources=app \
                            -Dsonar.tests=tests \
                            -Dsonar.test.inclusions=**/test_*.py \
                            -Dsonar.exclusions=.venv/**,**/__pycache__/**,.pytest_cache/**
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'DevSecOps pipeline completed successfully!'
        }
        failure {
            echo 'DevSecOps pipeline failed. Check the stage logs.'
        }
    }
}
