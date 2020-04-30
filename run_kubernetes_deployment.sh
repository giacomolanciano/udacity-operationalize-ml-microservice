#!/usr/bin/env bash

# This runs the container through a Kubernetes deployment and makes it accessible from the host

# Docker image ID
dockerpath="glanciano/udacity-flask-sklearn"

# Create a deployment in kubernetes
kubectl create deployment flasksklearndemo --image="$dockerpath":latest

# Expose the deployment as a kubernetes service
# - taget-port: the port on the container that the service should direct traffic to (must match with the one the
#   application is listening on)
# - port: the port that the service should serve on (can be different from target port, not related to the application)
kubectl expose deployment flasksklearndemo --type="NodePort" --port=80 --target-port=80

# Show service details
kubectl describe service flasksklearndemo

echo
echo "The service is available at localhost:<NodePort> (see 'kubectl describe service flasksklearndemo' output)."
