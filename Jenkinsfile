pipeline {
    agent { docker 'python' }

    stages {
        stage('build') {
            steps {
                sh 'echo "测试开始 run run run"'
                sh 'pip install -r requirements.txt -i http://pypi.douban.com --trusted-host pypi.douban.com'
                sh 'python -m pytest test_*.py'
            }
        }
        stage('end') {
            steps {
                sh 'echo "测试结束"'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
    }
}

