from entity.task import Task

class TodoInteractor(object):

    def __init__(self):
        self.uid = 0
        self.tasks = []

    def create_task(self, args):
        description = args.get('description', False)
        done = args.get('done', False)
        task = Task(description)
        if task.is_valid:
            self.uid += 1
            task.uid = self.uid
            self.tasks.append(task)
        return self.uid

    def get_tasks(self, args):
        return self.tasks

    def get_task(self, id):
        for task in self.tasks:
            return task if taks.uid == id else None

    def update_task(self, args):
        id = args.get('id', False)
        description = args.get('description', False)
        done = args.get('done', False)
        task = self.get_task(id)
        if not task: return False
        task.description = description
        taks.done = done
        return task

    def delete_task(self, id):
        task = self.get_task(id)
        self.tasks.remove(task)
        return task
