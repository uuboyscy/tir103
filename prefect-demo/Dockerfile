FROM --platform=linux/amd64 python:3.12-slim-bullseye

ENV TZ=Asia/Taipei

COPY requirements.txt requirements.txt
COPY ./src/ app/src/

RUN apt-get update && \
    apt-get install git zsh vim curl wget zip procps gcc python3-dev -y && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    echo "Y" | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Prefect config
RUN prefect config set PREFECT_LOGGING_LOG_PRINTS=True

ENV PYTHONPATH="$PYTHONPATH:/app/src"
