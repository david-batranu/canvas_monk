from os import path
from werkzeug import Local, LocalManager
from werkzeug.routing import Map, Rule
from werkzeug import Response
from mako.lookup import TemplateLookup


local = Local()
local_manager = LocalManager([local])
application = local('application')


url_map = Map([
    Rule('/static/<file>', endpoint='static', build_only=True),
])

def expose(rule, **kw):
    def decorate(f):
        kw['endpoint'] = f.__name__
        url_map.add(Rule(rule, **kw))
        return f
    return decorate

def url_for(endpoint, **values):
    return local.url_adapter.build(endpoint, values)


root_path = path.abspath(path.dirname(__file__))

template_lookup = TemplateLookup(directories=[path.join(root_path, 'templates')],
                                 input_encoding='utf-8')

def render_template(template, **context):
    tmpl = template_lookup.get_template(template)
    return Response(tmpl.render_unicode(url_for=url_for, **context),
                    mimetype='text/html')

def render_string(string, mimetype='text/plain'):
    return Response(string)
