from typing import List, Iterable, Union, Literal
from datetime import datetime, date, timedelta

from beautiful_date import BeautifulDate
from gcsa.google_calendar import EventsService
from gcsa.event import Event
from gcsa.util.date_time_util import ensure_localisation
from tzlocal import get_localzone_name

__all__ = ("Slot", "SlotsService")


class Slot(Event):
    def __init__(
        self,
        summary: str,
        start: Union[date, datetime, BeautifulDate],
        end: Union[date, datetime, BeautifulDate] = None,
        *,
        timezone: str = get_localzone_name(),
        events_per_slot: int = 1,
        **kwargs,
    ):
        self.events_per_slot = events_per_slot
        self._events = 0
        super().__init__(summary, start, end, timezone=timezone, **kwargs)

    def __str__(self):
        return '{} - {}'.format(self.start, self.end)

    def __repr__(self):
        return '<Slot {}>'.format(self.__str__())

    def __eq__(self, other):
        return (
            isinstance(other, Slot)
            and self.summary == other.summary
            and self.start == other.start
            and self.end == other.end
            and self.timezone == other.timezone
            and self.events_per_slot == other.events_per_slot
        )


class SlotsService(EventsService):

    def get_slots(
        self,
        slot_summary: str = None,
        slot_duration: Union[int, timedelta] = 60,  # in minutes
        time_min: Union[date, datetime, BeautifulDate] = datetime.utcnow(),
        time_max: Union[date, datetime, BeautifulDate] = datetime.utcnow() + timedelta(days=7),
        calendar_id: str = None,
        case_sensitive: bool = True,
        events_per_slot: int = 1,
        timezone: str = get_localzone_name(),
        **kwargs,
    ) -> Iterable[Slot]:
        kwargs.pop("query", None)
        slots = []

        if slot_summary:
            for event in self.get_events(
                time_min=time_min,
                time_max=time_max,
                order_by="startTime",
                timezone=timezone,
                single_events=True,
                query=slot_summary,
                calendar_id=calendar_id,
            ):
                if (
                    (case_sensitive and event.summary != slot_summary)
                    or (not case_sensitive and event.summary.lower() != slot_summary.lower())
                ):
                    continue
                if isinstance(event.start, datetime):
                    start_datetime = event.start
                elif isinstance(event.start, date):
                    start_datetime = datetime.combine(event.start, datetime.min.time())
                if isinstance(event.end, datetime):
                    end_datetime = event.end
                elif isinstance(event.end, date):
                    end_datetime = datetime.combine(event.end, datetime.max.time())
                delta = end_datetime - start_datetime
                delta_minutes = int(delta.total_seconds() / 60)
                if delta_minutes < slot_duration:
                    continue
                for i in range(0, delta_minutes, slot_duration):
                    start = start_datetime + timedelta(minutes=i)
                    end = start + timedelta(minutes=slot_duration)
                    if end > end_datetime:
                        break
                    slot = Slot(
                        summary=slot_summary,
                        start=start,
                        end=end,
                        timezone=event.timezone,
                        events_per_slot=events_per_slot,
                    )
                    if slot not in slots:
                        slots.append(slot)
        else:
            delta = time_max - time_min
            delta_minutes = int(delta.total_seconds() / 60)
            if delta_minutes >= slot_duration:
                for i in range(0, delta_minutes, slot_duration):
                    start = time_min + timedelta(minutes=i)
                    end = start + timedelta(minutes=slot_duration)
                    if end > time_max:
                        break
                    slot = Slot(
                        summary=slot_summary,
                        start=start,
                        end=end,
                        timezone=timezone,
                        events_per_slot=events_per_slot,
                    )
                    if slot not in slots:
                        slots.append(slot)

        if slots:
            for event in self.get_events(single_events=True, order_by="startTime", calendar_id=calendar_id):
                if (
                    (case_sensitive and event.summary == slot_summary)
                    or (not case_sensitive and event.summary.lower() == slot_summary.lower())
                ):
                    continue
                for slot in slots:
                    if slot.start.day > event.start.day:
                        break
                    elif slot.start.day < event.start.day:
                        continue
                    elif event.start <= slot.start < event.end or event.start < slot.end <= event.end:
                        slot._events += 1
            slots = [slot for slot in slots if slot._events < slot.events_per_slot]
            slots.sort()

        return iter(slots)
