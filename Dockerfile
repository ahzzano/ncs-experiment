# FROM ubuntu:22.04
FROM python:3


RUN apt-get update && apt-get install -y --no-install-recommends \ 
    python3 python3-pip curl git 

ADD https://astral.sh/uv/0.8.22/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

ADD . /app
WORKDIR /app

RUN uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

# CMD ["uv", "run", "main.py"]
# ENTRYPOINT ["python"]
ENTRYPOINT ["python"]
CMD ["uv", "run", "main.py"]

# run docker run -it --device /dev/dri:/dev/dri --device-cgroup-rule='c 189:* rmw' -v /dev/bus/usb:/dev/bus/usb --rm openvino/ubuntu20_dev:latest
