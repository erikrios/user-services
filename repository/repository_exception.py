class RepositoryException(Exception):
    message: str

    def __init__(self, message: str):
        super().__init__(message)


class NotFoundRepositoryException(RepositoryException):
    message: str

    def __init__(self, message: str):
        super().__init__(message)


class UnimplementedRepositoryException(RepositoryException):
    def __init__(self):
        super().__init__("Unimplemented repository.")


class UnknownRepositoryException(RepositoryException):
    def __init__(self):
        super().__init__("Unknown exception.")
