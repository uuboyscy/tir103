docker run -it -d \
    --name selenium-dev \
    -p 14444:4444 \
    -p 15900:5900 \
    -p 17900:7900 \
    -v /dev/shm:/dev/shm \
    -e SE_NODE_OVERRIDE_MAX_SESSIONS=true \
    -e SE_NODE_MAX_SESSIONS=5 \
    -e JAVA_OPTS=-XX:ActiveProcessorCount=5 \
    selenium/standalone-chrome:120.0
