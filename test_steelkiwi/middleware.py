#!-*- coding: utf-8 -*-
from django.db import connection
from django.template import Template, Context

class Middleware(object):
    def process_response(self, request, response):
        content_types = ['text/plain', 'text/html']
        if request.META['CONTENT_TYPE'] not in content_types:
            return response
        time =  sum([float(q['time']) for q in connection.queries])
        template = Template("""<div>
                <h3>Count of queries:{{count}}</h3>
                <h3>Time of queries:{{time}}</h3>
        </div>
        """)
        data = dict(time=time, count = len(connection.queries))
        render_template = template.render(Context(data))
        content = response.content.decode('utf-8')
        body_tag_position = content.find('</body')
        content = content[:body_tag_position] + render_template + content[body_tag_position:]
        response.content = content.encode('utf-8')
        return response

