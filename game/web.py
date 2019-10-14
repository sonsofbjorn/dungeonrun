from flask import Flask
from .dungeon import Map

app = Flask(__name__)

@app.route('/')
ef hello_world():

    dungeon = Map(4)
    something = dungeon.print_monsters()
    return something
