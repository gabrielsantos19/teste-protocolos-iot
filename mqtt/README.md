docker run -it --rm -p 1883:1883 -p 9001:9001 -v "$PWD/mqtt/mosquitto.conf":/mosquitto/config/mosquitto.conf eclipse-mosquitto
