from src.models.repository.check_ins_repository import CheckInRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class CheckInHandler:
    def __init__(self):
        self.check_in_repository = CheckInRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        check_in = http_request.param["attendee_id"]
        attendee_id = self.check_in_repository.insert_check_in(check_in)
        return HttpResponse(body={"attendeeId": attendee_id}, status_code=201)
