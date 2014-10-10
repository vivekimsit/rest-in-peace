class Task(object):

    def __init__(self, description, done=False):
        self.uid = 0
        self.description = description
        self.done = done

    def is_valid(self):
        return bool(self.description)
