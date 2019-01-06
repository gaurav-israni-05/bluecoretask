from rest_framework.exceptions import APIException


class GenericException(APIException):
    """
    Generic Exception class to raise all types of exceptions 
    """
    detail = None
    status_code = 400

    def __init__(self, detail, http_code=400):
        self.status_code = http_code
        self.detail = detail
