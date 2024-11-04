activate:
	if [ -d "venv" ]; then \
        echo "Python 🐍 environment was activated"; \
    else \
        echo "The folder environment doesn't exist"; \
		python -m venv venv; \
        echo "The environment folder was created and the python 🐍 environment was activated"; \
    fi
	. ./venv/bin/activate

install:
	pip3 install -r requirements.txt

run:
	@if [ -z "$(strip $(PORT))" ]; then \
		flask run; \
	else \
		flask run -p $(PORT); \
	fi



run-docker:
ifeq ($(strip $(PORT)),)
	flask run -h 0.0.0.0
else
	flask run -p $(PORT) -h 0.0.0.0
endif

run-tests:
	 make docker-test-up
	 FLASK_ENV=test python -m unittest discover -s tests -p '*Test.py' -v
	 make docker-test-down

run-tests-coverage:
	 make docker-test-up
	 FLASK_ENV=test coverage run -m unittest discover -s tests -p '*Test.py' -v
	 coverage report -m
	 coverage html
	 coverage report --fail-under=50
	 make docker-test-down

docker-gunicorn:
	  gunicorn -w 4 --bind 127.0.0.1:$(PORT) wsgi:app

docker-up:
	docker compose up --build

docker-down:
	docker compose down

docker-dev-up:
	docker compose -f=docker-compose.develop.yml up --build

docker-dev-down:
	docker compose -f=docker-compose.develop.yml down

docker-test-up:
	docker compose -f=docker-compose.test.yml up --build -d
	sleep 2

docker-test-down:
	make docker-db-truncate
	docker compose -f=docker-compose.test.yml down

create-database:
	docker exec customer-local-db psql -U develop -d customer-db -f /docker-entrypoint-initdb.d/init.sql

docker-db-truncate:
	docker exec customer-test-db psql -U develop -d customer-db  -c  "TRUNCATE TABLE channel_plan CASCADE;"
	docker exec customer-test-db psql -U develop -d customer-db  -c  "TRUNCATE TABLE customer CASCADE;"
	docker exec customer-test-db psql -U develop -d customer-db  -c  "TRUNCATE TABLE plan CASCADE;"
	docker exec customer-test-db psql -U develop -d customer-db  -c  "TRUNCATE TABLE channel CASCADE;"


kubernetes-up:
	kubectl apply -f kubernetes/k8s-configMap.yaml
	kubectl apply -f kubernetes/k8s-secrets.yaml
	kubectl apply -f kubernetes/k8s-deployment.yaml
	kubectl apply -f kubernetes/k8s-ingress.yaml

kubernetes-dev-up:
	make kubernetes-dev-up
	minikube tunnel

kubernetes-dev-down:
	kubectl delete configMap/customer-configmap
	kubectl delete secrets/customer-secrets
	kubectl delete deploy/abcall-customer-api
	kubectl delete ingress/abcall-customer-ingress


