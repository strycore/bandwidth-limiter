import os
import cherrypy
import subprocess


class Limiter(object):
    @cherrypy.expose
    def index(self):
        return file('index.html')

    @cherrypy.expose
    def limit(self):
        subprocess.Popen(["./limiter.sh"])
        return "ok"


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(Limiter(), '/', conf)
