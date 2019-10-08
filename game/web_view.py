from django.http import HttpResponse
from .dungeon import Map


def index(request):
    dungeon = Map(4)
    monsters = dungeon.print_monsters()
    return HttpResponse(monsters)
