docker run -it --rm --device /dev/bus/usb:/dev/bus/usb my-local-image main.py
docker run -it --rm \
    --device /dev/bus/usb/000/005 \
    --privileged \
    my-local-image \
    main.py

