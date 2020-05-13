from json import JSONEncoder

class ResponseEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__

class Response():

    def __init__(self, status="OK"):
        self.status = status