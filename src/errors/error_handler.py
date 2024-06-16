from src.http_types.http_response import HttpResponse
from .error_types.http_conflict import HttpConflictError
from .error_types.http_not_found import HttpNotFoundError


def handler_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpConflictError, HttpNotFoundError)):
        return HttpResponse(body={
            "errors": [{
                "title": error.name,
                "detail": error.message
            }]
        }, status_code=error.status_code)
    else:
        return HttpResponse(body={
            "errors": [{
                "title": "error",
                "detail": str(error)
            }]
        }, status_code=500)
