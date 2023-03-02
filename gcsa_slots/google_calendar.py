from gcsa.google_calendar import GoogleCalendar as _GoogleCalendar

from .slots import Slot, SlotsService

__all__ = ("GoogleCalendar",)


class GoogleCalendar(_GoogleCalendar, SlotsService):
    pass
