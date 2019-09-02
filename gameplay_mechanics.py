class Action:

    def __init__(self, title, description, execute):
        if not callable(execute) and execute is not None:
            raise TypeError("execute must be callable")
        self.execute = execute
        self.title = title
        self.description = description
