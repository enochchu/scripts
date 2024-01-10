#!/bin/bash

# Refer to docs here:
# https://docs.docker.com/engine/install/centos/

# Install Docker CE
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# Start Docker using systemctl
sudo systemctl start docker