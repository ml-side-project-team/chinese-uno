pipeline {
	agent any

	environment {
		PYTHON_TEST = "python3.7 -m unittest"
	}

	stages {
		stage('Test') {
			steps {
				sh "${PYTHON_TEST} model_tests.py"
			}
		}
	}
}
