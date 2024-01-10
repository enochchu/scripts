#!/bin/bash

# Refer to docs here:
# https://docs.docker.com/engine/install/centos/

# Remove existing Docker first

sudo yum remove docker \
	docker-client \
	docker-client-latest \
	docker-common \
	docker-latest \
	docker-latest-logrotate \
	docker-logrotate \
	docker-engine	