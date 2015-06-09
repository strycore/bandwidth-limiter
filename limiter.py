import os
import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return file('index.html')

    @cherrypy.expose
    def limit(self):
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
    cherrypy.quickstart(HelloWorld(), '/', conf)
