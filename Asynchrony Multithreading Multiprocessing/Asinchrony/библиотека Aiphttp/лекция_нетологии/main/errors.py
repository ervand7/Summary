class HttpException(Exception):

    def __init__(self, message, *args, **kwargs):
        self.message = message


class NotFound(HttpException):
    reason = 'Not found'
    status_code = 404


class BadRequest(HttpException):
    reason = 'Bad Request'
    status_code = 400
