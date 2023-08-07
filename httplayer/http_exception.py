from fastapi import HTTPException, status

from service.service_exception import NotFoundServiceException


def handle_exception(e: Exception):
    if isinstance(e, NotFoundServiceException):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="something went wrong")
