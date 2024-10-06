#!/bin/bash
set -x

pip install pipenv \
&& pipenv lock --dev \
&& pipenv requirements --dev > requirements.txt \
&& pip install -r requirements.txt

sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="xiong-chiamiov-plus"/' /root/.zshrc \
&& sed -i '/HIST_STAMPS="mm\/dd\/yyyy"/s/^#*//;s/mm\/dd\/yyyy/yyyy-mm-dd/' /root/.zshrc

# cp /root/.gitconfig_mounted /root/.gitconfig \
# && cp -r /root/.ssh_mounted/* /root/.ssh/ \
# && ls /root/.ssh/id_* | grep -v pub | xargs chmod 400 \
# && chmod 755 /root/.ssh/config

git config --global --add safe.directory /workspaces/*

zsh
