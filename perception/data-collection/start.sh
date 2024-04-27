xhost local:root

docker pull luxonis/depthai-library
# docker run -it --rm \
#     --privileged \
#     -v /dev/bus/usb:/dev/bus/usb \
#     -v $PWD:/workspace/ \
#     --device-cgroup-rule='c 189:* rmw' \
#     -e DISPLAY=$DISPLAY \
#     -v /tmp/.X11-unix:/tmp/.X11-unix \
#     luxonis/depthai-library:latest \
#     /bin/bash

docker run -it --rm \
    --privileged \
    -v /dev/bus/usb:/dev/bus/usb \
    -v $PWD:/workspace/ \
    -v $PWD/videos/:/workspace/videos \
    --device-cgroup-rule='c 189:* rmw' \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    luxonis/depthai-library:latest \
    python3 /workspace/rgb_video.py
