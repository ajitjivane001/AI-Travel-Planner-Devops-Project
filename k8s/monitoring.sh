#!/bin/bash
set -e

echo "Setting up Prometheus and Grafana on the Kubernetes Cluster..."

# Add Helm repositories
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Create namespace
kubectl create namespace monitoring || true

# Install Prometheus
echo "Installing Prometheus..."
helm upgrade --install prometheus prometheus-community/prometheus \
  --namespace monitoring \
  --set alertmanager.persistentVolume.storageClass="gp2",server.persistentVolume.storageClass="gp2"

# Install Grafana
echo "Installing Grafana..."
helm upgrade --install grafana grafana/grafana \
  --namespace monitoring \
  --set persistence.storageClassName="gp2" \
  --set persistence.enabled=true \
  --set adminPassword='admin' # Change this in production!

echo "Monitoring setup complete!"
echo "To access Grafana locally, run: kubectl port-forward namespace/monitoring svc/grafana 3000:80"
