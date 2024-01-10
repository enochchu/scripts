#!/bin/bash

# Refer to docs here:
# https://k3s.io/

# Install k3s
curl -sfL https://get.k3s.io | sh - 

# Check for Ready node, takes ~30 seconds 
sudo k3s kubectl get node