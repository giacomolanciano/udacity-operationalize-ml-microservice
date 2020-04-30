# Operationalize a Machine Learning Microservice API

[![CircleCI](https://circleci.com/gh/giacomolanciano/udacity-operationalize-ml-microservice.svg?style=svg)](https://circleci.com/gh/giacomolanciano/udacity-operationalize-ml-microservice)

## Project Overview

In this project, you will apply the skills you have acquired in this course to operationalize a Machine Learning
Microservice API.

You are given a pre-trained, `sklearn` model that has been trained to predict housing prices in Boston according to
several features, such as average rooms in a home and data about highway access, teacher-to-pupil ratios, and so on. You
can read more about the data, which was initially taken from Kaggle, on [the data source
site](https://www.kaggle.com/c/boston-housing). This project tests your ability to operationalize a Python flask app—in
a provided file, `app.py`—that serves out predictions (inference) about housing prices through API calls. This project
could be extended to any pre-trained machine learning model, such as those for image recognition and data labeling.

### Project Tasks

Your project goal is to operationalize this working, machine learning microservice using
[kubernetes](https://kubernetes.io/), which is an open-source system for automating the management of containerized
applications. In this project you will:

* Test your project code using linting
* Complete a Dockerfile to containerize this application
* Deploy your containerized application using Docker and make a prediction
* Improve the log statements in the source code for this application
* Configure Kubernetes and create a Kubernetes cluster
* Deploy a container using Kubernetes and make a prediction
* Upload a complete Github repo with CircleCI to indicate that your code has been tested

You can find a detailed [project rubric, here](https://review.udacity.com/#!/rubrics/2576/view).

**The final implementation of the project will showcase your abilities to operationalize production microservices.**

---

## Setup the Environment

* Create a virtualenv and activate it

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh` (**NOTE:** requires uploading the container to Docker Hub via
   `./upload_docker.sh`)
4. Run in Kubernetes (deployment):  `./run_kubernetes_deployment.sh` (**NOTE:** requires uploading the container to
   Docker Hub via `./upload_docker.sh`)

### Kubernetes Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
* Create Flask app in Container
* Run via kubectl

### Linting

Run `make lint` (or `make lint-local` if do not have `hadolint` installed in your local environment) to lint app code
and `Dockerfile`. Linting will be also automatically run by CircleCI.

### Unit Tests

Run `make test` to check whether the app is behaving as expected. Tests will be also automatically run by CircleCI.

### Cleaning up

* If the app has been launched with `./run_docker.sh`, no action is required (the container will be automatically
  deleted).
* If the app has been launched with `./run_kubernetes.sh`, run `kubectl delete pod flasksklearndemo`
* If the app has been launched with `./run_kubernetes_deployment.sh`, run `./clean_kubernetes_deployment.sh`
