class WebView:
    def __init__(self):
        wrapper = FlaskWrapper('wrap')
        wrapper.add_endpoint(endpoint='/',endpoint_name='root',
                             handler=self.print_main_menu)
        wrapper.run()

    def print_main_menu(self):
        return 'Hello, world'

    def handle_input(self):
        pass


from flask import Flask
import requests

class EndpointAction:

    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        return self.action()

class FlaskWrapper:
    def __init__(self, name):
        self.app = Flask(name)


    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))

    def run(self):
        self.app.run()
