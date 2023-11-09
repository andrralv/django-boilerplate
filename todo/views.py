from django.http import JsonResponse
from .models import Todo
from django.core import serializers
import json

# Create your views here.
def all_todos(req):
  if req.method == 'GET':
    data = Todo.objects.all()
    ret = []
    _json = serializers.serialize("json", data)
    obj = json.loads(_json)
    for i in obj:
      ret.append(i['fields'])
    return JsonResponse(ret, safe=False)
  if req.method == 'POST':
    _item = req.body
    item = {'title': 'a', 'description': 'b', 'completed': True}
    if (_item): 
      Todo.save(_item)
    else:
      Todo.save(item)

def todo_view(req, title):
  todo = Todo.objects.get(title=title)
  data = {
    'title': todo.title,
    'description': todo.description,
    'completed': todo.completed
  }

  return JsonResponse(data, safe=False)