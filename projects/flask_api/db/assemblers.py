from projects.flask_api.utils.dt_utils import DatetimeUtils
from .models import Task


def assemble_task(task_name, priority, owner, status):
    task = Task()
    task.task = task_name
    task.priority = priority
    task.owner = owner
    task.status = status
    task.create_time = DatetimeUtils.timestamp_delta()
    task.update_time = DatetimeUtils.timestamp_delta()

    return task
