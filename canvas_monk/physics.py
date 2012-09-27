import pymunk
import json
from math import pi
from random import randrange


def to_pygame(p):
    return int(p.x), int(-p.y+480)

def random_color():
    return randrange(255), randrange(255), randrange(255)

class Block(object):
    def __init__(self, space, posx, posy, width, height, static=False):
        density = .0007
        if static:
            body = pymunk.Body(pymunk.inf, pymunk.inf)
        else:
            body = pymunk.Body(density * width * height, 1000 * density * width * height)
        body.position = (posx, posy)
        corners = [(0, 0), (width, 0), (width, height), (0, height)]
        contour = pymunk.Poly(body, corners, offset=(-width/2, -height/2))
        space.add(contour)
        if not static:
            space.add(body)
        self.contour = contour
        self.body = body
        self.contour.friction = .5
        self.color = random_color()

    def dump(self):
        datasheet = [to_pygame(point) for point in self.contour.get_points()]
        datasheet.append(self.color)
        return datasheet

class Circle(object):
    def __init__(self, space, pos_x, pos_y, radius):
        density = .0007
        mass = density * (pi * (radius ** 2))
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
        body = pymunk.Body(mass, inertia)
        body.position = (pos_x, pos_y)
        contour = pymunk.Circle(body, radius, (0, 0))
        space.add(body, contour)
        self.contour = contour
        self.body = body
        self.color = random_color()

    def dump(self):
        datasheet = []
        datasheet.extend(to_pygame(self.body.position))
        datasheet.append(self.contour.radius)
        datasheet.append(self.color)
        return datasheet

class Physics(object):
    try:
        #old pymunk
        pymunk.init_pymunk()
    except AttributeError:
        #new pymunk
        pass
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    objects = []

    def add_block(self, *args):
        block = Block(self.space, *args)
        self.objects.append(block)

    def add_circle(self, *args):
        circle = Circle(self.space, *args)
        self.objects.append(circle)

    def rm_obj(self, obj):
        self.space.remove(obj.contour)
        try:
            self.space.remove(obj.body)
        except KeyError:
            pass
        self.objects = [x for x in self.objects if x is not obj]

    def reset(self):
        for obj in self.objects:
            self.rm_obj(obj)

    def update(self):
        for obj in self.objects:
            if obj.body.position.y < 0:
                self.rm_obj(obj)
        self.space.step(1/50.0)

    def space_dump(self):
        dump = {'poly': [], 'circle': []}
        for obj in self.objects:
            if isinstance(obj, Block):
                dump['poly'].append(obj.dump())
            elif isinstance(obj, Circle):
                dump['circle'].append(obj.dump())
        return dump

    def json_dump(self):
        return json.dumps(self.space_dump())
