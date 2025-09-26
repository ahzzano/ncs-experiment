FROM openvino/ubuntu22_runtime:latest

RUN uv sync

CMD ["uv", "run", "main.py"]

# run docker run -it --device /dev/dri:/dev/dri --device-cgroup-rule='c 189:* rmw' -v /dev/bus/usb:/dev/bus/usb --rm openvino/ubuntu20_dev:latest

