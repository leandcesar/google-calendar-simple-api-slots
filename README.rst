Google Calendar Simple API Slots
================================

`Google Calendar Simple API Slots` or `gcsa-slots` is an extension for `Google Calendar Simple API`_ library with slots (dates and times available for scheduling).

Installation
------------

.. code-block:: console

    pip install gcsa-slots


See `Getting started page`_ for more details and installation options.

Example usage
-------------

List slots from free ranges (dates and times without events, available for scheduling)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from gcsa_slots.google_calendar import GoogleCalendar

    calendar = GoogleCalendar("your_email@gmail.com")
    for slot in calendar.get_slots():
        print(slot)


List slots from slot-event ranges (an event that determines availability for scheduling)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from gcsa_slots.google_calendar import GoogleCalendar

    calendar = GoogleCalendar("your_email@gmail.com")
    for slot in calendar.get_slots(slot_summary="Free"):
        print(slot)


List slots specifying time range, slot interval, max events per slot and calendar ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from gcsa_slots.google_calendar import GoogleCalendar

    calendar = GoogleCalendar("your_email@gmail.com")
    calendar_id = "your calendar id"
    for slot in calendar.get_slots(
        slot_summary="fReE",
        case_sensitive=False,
        time_min=datetime(2023, 3, 6),
        time_max=datetime(2023, 3, 7),
        slot_duration=90,
        events_per_slot=3,
        calendar_id=calendar_id,
    ):
        print(slot)


Create event in first available slot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from gcsa_slots.google_calendar import GoogleCalendar

    calendar = GoogleCalendar("your_email@gmail.com")
    slots = calendar.get_slots()
    slot = next(slots)
    slot.summary = "This is a test!"
    calendar.add_event(slot)


.. _`Google Calendar Simple API`: https://github.com/kuzmoyev/google-calendar-simple-api
.. _`Getting started page`: https://google-calendar-simple-api.readthedocs.io/en/latest/getting_started.html
