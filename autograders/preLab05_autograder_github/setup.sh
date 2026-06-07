#!/usr/bin/env bash

apt-get update
apt-get upgrade
apt-get install -y python3 python3-pip python3-dev git jq

pip3 install -r /autograder/source/requirements.txt