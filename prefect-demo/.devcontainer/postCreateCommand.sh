#!/bin/bash
set -x

sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="xiong-chiamiov-plus"/' /root/.zshrc \
&& sed -i '/HIST_STAMPS="mm\/dd\/yyyy"/s/^#*//;s/mm\/dd\/yyyy/yyyy-mm-dd/' /root/.zshrc

cp /root/.gitconfig_mounted /root/.gitconfig \
&& cp -r /root/.ssh_mounted/* /root/.ssh/ \
&& ls /root/.ssh/* | grep -v pub | xargs chmod 400

chmod 755 /root/.ssh/config
chmod 755 /root/.ssh/known_hosts

git config --global --add safe.directory /workspaces/*

zsh
