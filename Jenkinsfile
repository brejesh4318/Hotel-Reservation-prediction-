pipeline{
    agent any

    stages{
        stage("Cloning Github repo to Jenkins")
            steps{
                scripts{
                    echo 'Cloning Github repo to Jenkins.......'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/brejesh4318/Hotel-Reservation-prediction-.git']])
                }
            }

    }
}