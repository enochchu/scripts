#!/bin/bash

# Refer to docs here:
# https://docs.docker.com/engine/install/centos/

# Set up the repositry first
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo