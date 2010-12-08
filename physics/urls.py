from django.conf.urls.defaults import *

urlpatterns = patterns('canvas.physics.views',
    (r'^physics/index/', 'index'),
    (r'^physics/scene_data', 'get_scene'),
    (r'^physics/reset', 'reset_scene'),
    (r'^physics/add_block', 'add_block'),
    (r'^physics/add_circle', 'add_circle'),

)


