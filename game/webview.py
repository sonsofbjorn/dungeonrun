import requests
from dungeon import Map
from forms import SubmitForm
from flask import Flask, render_template

class WebView():
    def __init__(self):
        wrapper = FlaskWrapper('game')
        wrapper.add_endpoint(endpoint='/',endpoint_name='root',
                             handler=self.hello_world, methods=['GET','POST'])
        wrapper.run()

    def print_main_menu(self):
        return 'Hello, world'

    def handle_input(self):
        pass

    def hello_world(self):
        form = SubmitForm()
        if form.mapsize.data:
            dungeon = Map(form.mapsize.data)
        else:
            dungeon = Map(4)
        return render_template('home.html', dungeon=dungeon, form=form)

class EndpointAction:

    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        return self.action()

class FlaskWrapper:
    def __init__(self, name):
        self.app = Flask(name)
        self.app.config['SECRET_KEY'] = 'blabla'

    """
    add_endpoint creates a new endpoint for the server to listen to
    methods MUST be methods=methods, but why?
    """
    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=None):
        self.app.add_url_rule(endpoint, endpoint_name,
                              EndpointAction(handler), methods=methods)

    def run(self):
        self.app.run(debug=True)
