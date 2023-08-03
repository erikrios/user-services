class ServiceException(Exception):
    message: str

    def __init__(self, message: str):
        super().__init__(message)


class NotFoundServiceException(ServiceException):
    message: str

    def __init__(self, message: str):
        super().__init__(message)


class UnimplementedServiceException(ServiceException):
    def __init__(self):
        super().__init__("Unimplemented service.")


class UnknownServiceException(ServiceException):
    def __init__(self):
        super().__init__("Unknown exception.")
