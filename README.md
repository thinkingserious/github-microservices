# GitHub Multi-Repo Management Monolith

This is sample code for a OSCON 2019 tutorial: https://conferences.oreilly.com/oscon/oscon-or/public/schedule/detail/76039

## Pre-requisites

* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [Docker](https://docs.docker.com/install)
* [MiniKube](https://kubernetes.io/docs/tasks/tools/install-minikube)
* [Kompose](https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/#install-kompose)
* [Clone GitHub Monolith](https://github.com/thinkingserious/github-monolith)

## Installation

Update `.env_example`.

```bash
mv ./.env_example ./.env
source .env
docker-machine create -d virtualbox github-manager-microservices
eval "$(docker-machine env github-manager-microservices)"
export GITHUB_MANAGER_MICROSERVICES_IP="$(docker-machine ip github-manager-microservices)"
docker-compose -f docker-compose.yml up -d --build
```

## Quickstart

Go to `http://<$GITHUB_MANAGER_MICROSERVICES_IP>` in your browser. If you see "There are a total...", you're good to go.

Open `examples/*` and update the repos in `all_repos`.

Open `examples/send_emails` and update the email in the `send_email` function.

Open `examples/send_sms` and update the to and from phone numbers in the `send_sms` function.

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r web/requirements.txt
export GITHUB_MANAGER_MICROSERVICES_IP="$(docker-machine ip github-manager-microservices)"
python examples/get_all_issues.py
python examples/get_all_prs.py
python examples/send_email.py
python examples/send_sms.py
```

# References
* https://github.com/thinkingserious/github-monolith
* https://github.com/sendgrid/github-automation
* https://github.com/sendgrid/dx-automator
* https://github.com/miguelgrinberg
* https://github.com/testdrivenio/testdriven-app-2.5
* https://github.com/realpython/orchestrating-docker
* http://flask.pocoo.org/docs/1.0