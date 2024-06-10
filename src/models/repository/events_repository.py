from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as datbase:
            try:
                event = Events(
                    id=eventsInfo.get("uuid"),
                    title=eventsInfo.get("title"),
                    details=eventsInfo.get("details"),
                    slug=eventsInfo.get("slug"),
                    maximum_attendees=eventsInfo.get("maximum_attendees")
                )
                datbase.session.add(event)
                datbase.session.commit()

                return eventsInfo
            except IntegrityError:
                raise Exception("event already registered!")
            except Exception as exception:
                datbase.session.rollback()
                raise exception

    def get_event_by_id(self, event_id: str) -> Events | None:
        with db_connection_handler as datbase:
            try:
                event = (
                    datbase.session
                    .query(Events)
                    .filter(Events.id == event_id)
                    .one()
                )
                return event
            except NoResultFound:
                return None
