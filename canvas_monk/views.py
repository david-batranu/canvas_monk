from werkzeug import redirect
from werkzeug.exceptions import NotFound
from utils import expose, url_for, render_template, render_string
import json
import physics


phy = physics.Physics()
def add_blocks():
    phy.add_block(320, 5, 640, 10, True)
    phy.add_block(300, 250, 50, 50)
    phy.add_block(450, 200, 270, 10, True)


@expose('/')
def index(request):
    return render_template('index.html')

@expose('/scene_data')
def get_scene(request):
    phy.update()
    return render_string(phy.json_dump(), mimetype='text/javascript+json')

@expose('/add_block')
def add_block(request):
    specs = json.loads(request.values.get('poly'))
    phy.add_block(*specs)
    return render_string('OK!')

@expose('/add_circle')
def add_circle(request):
    specs = json.loads(request.values.get('circle'))
    phy.add_circle(*specs)
    return render_string('OK!')

@expose('/reset')
def reset_scene(request):
    phy.reset()
    add_blocks()
    return render_string('OK!')

add_blocks()
