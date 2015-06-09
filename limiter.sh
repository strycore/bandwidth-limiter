#!/bin/bash

interface=eth0
download_speed=80
upload_speed=40
duration="3 hours"

wondershaper $interface $download_speed $upload_speed
wondershaper clear $interface | at now + $duration
