#!/bin/bash

interface=eth0
download_speed=800
upload_speed=160
duration="2 hours"

sudo wondershaper $interface $download_speed $upload_speed
sudo wondershaper clear $interface | at now + $duration
