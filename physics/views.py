from django.http import HttpResponse
from django.shortcuts import render_to_response
import physics
import json

phy = physics.Physics()
def add_blocks():
    phy.add_block(320, 5, 640, 10, True)
    phy.add_block(300, 250, 50, 50)
    phy.add_block(450, 200, 270, 10, True)

def index(request):
    return render_to_response("physics/index.html")

def get_scene(request):
    phy.update()
    return HttpResponse(phy.json_dump(), content_type='text/javascript+json; charset=utf-8')

def add_block(request):
    specs = json.loads(request.POST.get('poly'))
    phy.add_block(*specs)
    return HttpResponse('OK!')

def reset_scene(request):
    phy.reset()
    add_blocks()
    return HttpResponse('OK!')

add_blocks()