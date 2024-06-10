def handler_error(error: Exception) -> dict:
    return {
        "message": str(error),
        "status_code": 500
    }