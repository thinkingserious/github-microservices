# Resetting MiniKube

```bash
minikube stop
minikube delete
minikube start
```

# Updating a Kubernetes Service

```bash
docker login
docker build -t <dockerhub username>/<service name> ./services/<service name>
docker push <dockerhub username>/<service name>
kubectl delete -f ./kubernetes/<service name>-deploy.yml
kubectl create -f ./kubernetes/<service name>-deploy.yml
export GITHUB_MANAGER_MICROSERVICES_IP="hello.world"
python examples/get_all_issues.py
http://hello.world
```

# Updating your Docker Services

```bash
eval "$(docker-machine env github-manager-microservices)"
export GITHUB_MANAGER_MICROSERVICES_IP="$(docker-machine ip github-manager-microservices)"
docker-compose -f docker-compose.yml up -d --build
```