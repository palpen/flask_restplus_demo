from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)

# NEW!
api = Api(app, version='1.0', title='TODO',
    description='A simple TODO API',
    )

# NEW!
ns = api.namespace('TODO Namespace', description='Todo Operations')

todo = api.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

# Initialize TodoDAO with a few tasks
DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)