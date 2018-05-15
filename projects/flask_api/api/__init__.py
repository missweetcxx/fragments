from flask import Flask

from .task import CreateTask, GetTask, GetTaskList, task

app = Flask(__name__)

app.register_blueprint(task)
