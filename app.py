import json

from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request
from werkzeug.exceptions import HTTPException, NotFound

from interactor.todointeractor import TodoInteractor

_API_TODO = '/api/todo/v1/tasks/'

url_map = Map([
    Rule(_API_TODO, endpoint='get_tasks', methods=['GET']),
    Rule(_API_TODO + '<int:id>', endpoint='get_task', methods=['GET']),
    Rule(_API_TODO, endpoint='create_task', methods=['POST']),
    Rule(_API_TODO + '<int:id>', endpoint='update_task', methods=['PUT']),
    Rule(_API_TODO + '<int:id>', endpoint='delete_task', methods=['DELETE'])
])


def application(environ, start_response):
    urls = url_map.bind_to_environ(environ)
    try:
        request = Request(environ)
        endpoint, args = urls.match()
        todointeractor = TodoInteractor()
        if request.get_data():
            print 'DATA', request.get_data()
            data = json.loads(request.get_data())
            print getattr(todointeractor, endpoint)(data)
        else:
            print getattr(todointeractor, endpoint)(args['id'])
    except HTTPException, e:
        return e(environ, start_response)
    start_response('200 OK', [('Content-Type', 'application/json')])
    return ['Rule points to %s with arguments %s' % (endpoint, args)]


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 5000, application, use_debugger=True,
            use_reloader=True)

#ALL   : curl -i http://127.0.0.1:5000/api/todo/v1/tasks
#CREATE: curl -iX POST http://127.0.0.1:5000/api/todo/v1/tasks
#UPDATE: curl -iX PUT http://127.0.0.1:5000/api/todo/v1/tasks/1
#GET   : curl -iX GET http://127.0.0.1:5000/api/todo/v1/tasks/1
#DELETE: curl -iX DELETE http://127.0.0.1:5000/api/todo/v1/tasks/1
#POST Data:  curl -iX POST -d '{"description":"Foo", "done":"false"}' http://127.0.0.1:5000/api/todo/v1/tasks/ -H "Content-Type:application/json"
