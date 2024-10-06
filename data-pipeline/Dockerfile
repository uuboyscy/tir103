FROM python:3.12-slim-bullseye

ENV TZ=Asia/Taipei

RUN apt-get update && \
    apt-get install git zsh vim curl wget zip make procps gcc python3-dev -y && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    echo "Y" | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN pip install --upgrade pip
