Bandwidth limiter
=================

Very simple web UI to limit bandwidth usage for a given amount of time.
You can configure the following in the limiter.sh script:

* interface : name of the network interface to use (default eth0)
* download_speed : maximum download speed in kbits/s (kb/s * 8)
* upload_speed : maximum upload speed in kbits/s
* duration : how long the limitation is effective (default: 2 hours)

Requirements
------------

* Python
* cherrypy
* wondershaper

Note
----

Wondershaper is executed with sudo. TO remove any password prompt add
this to your sudoers file and replace username and hostname with
appropriate values::

    username hostname=(root) NOPASSWD: /sbin/wondershaper
