import json
import requests

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Comment


def json_response(something=None):
    return HttpResponse(
        json.dumps(something),
        content_type='application/json; charset=UTF-8')


def render_to_react_string(component_name, ctx=None):
    if ctx is None:
        ctx = {}

    try:
        response = requests.get(settings.NODE_SERVER,
                            params={'component_name': component_name, 'data': json.dumps(ctx)})

        if response.status_code == requests.codes.ok:
            return mark_safe(response.text)
        else:
            return ''
    except Exception as exc:
        print exc
        return ''


def get_comments():
    return list(Comment.objects.values('id', 'name', 'text'))


def load_comments(request):
    return json_response({"comments": get_comments()})


def post_comment(request):
    Comment.objects.create(name=request.POST['name'], text=request.POST['text'])
    return json_response({"success": True})


def index(request):

    return render(request, 'index.html')
