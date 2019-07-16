# GitHub Multi-Repo Management Microservices

This is sample code for a OSCON 2019 tutorial: https://conferences.oreilly.com/oscon/oscon-or/public/schedule/detail/76039

Please find the corresponding slides [here](https://docs.google.com/presentation/d/1nGDy4w70doTdc9TVRqDp9KK-mnOpVXz9VYZ3X4dBZlA)

## Pre-requisites

### If installing using a thumb drive

Install the binaries in the appropriate folder `osx`, `windows`, `linux`

Docker images are also included in the `docker-images` folder so you don't need to download them. Move them to your local machine and then install them like so.

```bash
cd DIRECTORY_WHERE_YOU_COPIED_THE_DOCKER_IMAGES
docker load -i python.tar
docker load -i nginx.tar
```

### If installing from the Internet

* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
  * [OS X](https://download.virtualbox.org/virtualbox/6.0.8/VirtualBox-6.0.8-130520-OSX.dmg)
  * [Windows](https://download.virtualbox.org/virtualbox/6.0.8/VirtualBox-6.0.8-130520-Win.exe)
  * [Ubuntu 18.04 / 18.10 / 19.04 / Debian 10](https://download.virtualbox.org/virtualbox/6.0.8/virtualbox-6.0_6.0.8-130520~Ubuntu~bionic_amd64.deb)
  * [openSUSE 15.0](https://download.virtualbox.org/virtualbox/6.0.8/VirtualBox-6.0-6.0.8_130520_openSUSE150-1.x86_64.rpm)
  * [Fedora 29 / 30](https://download.virtualbox.org/virtualbox/6.0.8/VirtualBox-6.0-6.0.8_130520_fedora29-1.x86_64.rpm)
* [Docker](https://docs.docker.com/install)
  * [OS X](https://download.docker.com/mac/stable/Docker.dmg)
  * [Windows](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe)
  * [Linux x86](https://download.docker.com/linux/static/stable/x86_64/docker-17.03.0-ce.tgz)
* [MiniKube](https://kubernetes.io/docs/tasks/tools/install-minikube)
  * [OS X](https://storage.googleapis.com/minikube/releases/v1.2.0/minikube-darwin-amd64)
  * [Linux](https://storage.googleapis.com/minikube/releases/v1.2.0/minikube-linux-amd64)
  * [Windows](https://storage.googleapis.com/minikube/releases/v1.2.0/minikube-windows-amd64.exe)
* [Kompose](https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/#install-kompose)
  * [OS X](https://github.com/kubernetes/kompose/releases/download/v1.18.0/kompose-darwin-amd64.tar.gz)
  * [Linux AMD](https://github.com/kubernetes/kompose/releases/download/v1.18.0/kompose-linux-amd64.tar.gz)
  * [Linux ARM](https://github.com/kubernetes/kompose/releases/download/v1.18.0/kompose-linux-arm.tar.gz)
  * [Windows](https://github.com/kubernetes/kompose/releases/download/v1.18.0/kompose-windows-amd64.exe.tar.gz)
* [Clone GitHub Monolith](https://github.com/thinkingserious/github-monolith)

## Installation

* Update `.env_example`.
* Update `examples/config.example`.

```bash
mv ./.env_example ./.env
mv ./examples/config.example ./examples/config.py
source .env
docker-machine create -d virtualbox github-manager-microservices
eval "$(docker-machine env github-manager-microservices)"
export GITHUB_MANAGER_MICROSERVICES_IP="$(docker-machine ip github-manager-microservices)"
docker-compose -f docker-compose.yml up -d --build
```

## Quickstart

Go to `http://<$GITHUB_MANAGER_MICROSERVICES_IP>` in your browser. If you see "There are a total...", you're good to go.

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r services/web/requirements.txt
source .env
export GITHUB_MANAGER_MICROSERVICES_IP="$(docker-machine ip github-manager-microservices)"
python examples/get_all_issues.py
python examples/get_all_prs.py
python examples/send_email.py
python examples/send_sms.py
```

## Local Kubernetes Setup

* Update `kubernetes/secret.example`.

```bash
minikube start
mv ./kubernetes/secret.example ./kubernetes/secret.yml
kubectl apply -f ./kubernetes/secret.yml
minikube dashboard // Verify secrets are deployed
minikube addons enable ingress
docker login
docker build -t <YOUR DOCKER HUB USERNAME>/github ./services/github
docker push <YOUR DOCKER HUB USERNAME>/github
docker build -t <YOUR DOCKER HUB USERNAME>/sms ./services/sms
docker push <YOUR DOCKER HUB USERNAME>/sms
docker build -t <YOUR DOCKER HUB USERNAME>/email ./services/email
docker push <YOUR DOCKER HUB USERNAME>/email
docker build -t <YOUR DOCKER HUB USERNAME>/web ./services/web
docker push <YOUR DOCKER HUB USERNAME>/web
kubectl create -f ./kubernetes/github-deploy.yml
kubectl create -f ./kubernetes/github-service.yml
kubectl create -f ./kubernetes/sms-deploy.yml
kubectl create -f ./kubernetes/sms-service.yml
kubectl create -f ./kubernetes/email-deploy.yml
kubectl create -f ./kubernetes/email-service.yml
kubectl create -f ./kubernetes/web-deploy.yml
kubectl create -f ./kubernetes/web-service.yml
kubectl apply -f ./kubernetes/minikube-ingress.yml
echo "$(minikube ip) hello.world" | sudo tee -a /etc/hosts // Add minikube ip to /etc/hosts
export GITHUB_MANAGER_MICROSERVICES_IP="hello.world"
python examples/get_all_issues.py
python examples/get_all_prs.py
python examples/send_email.py
python examples/send_sms.py
```

## Troubleshooting

### kubectl
When installing `kubectl` using `brew` you might run into schema errors. You can fix this by relinking.

```bash
rm /usr/local/bin/kubectl
brew link --overwrite kubernetes-cli
```

And also optionally:

```bash
brew link --overwrite --dry-run kubernetes-cli. 
```

# References
* https://github.com/thinkingserious/github-monolith
* https://github.com/sendgrid/github-automation
* https://github.com/sendgrid/dx-automator
* https://github.com/miguelgrinberg
* https://github.com/testdrivenio/testdriven-app-2.5
* https://github.com/testdrivenio/flask-vue-kubernetes
* https://github.com/realpython/orchestrating-docker
* http://flask.pocoo.org/docs/1.0