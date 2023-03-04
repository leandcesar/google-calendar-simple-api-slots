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

.. raw:: html

    <h1 align="center">
        <img src="https://github.com/leandcesar/google-calendar-simple-api-slots/blob/main/docs/images/example_1.png?raw=true" alt="List slots from free ranges"/>
    </h1>

.. code-block:: python

    from gcsa_slots.google_calendar import GoogleCalendar

    calendar = GoogleCalendar("your_email@gmail.com")
    for slot in calendar.get_slots(60):  # 60 minutes
        print(slot)

    # 2023-03-06 09:00:00-03:00 - 2023-03-06 10:00:00-03:00
    # 2023-03-06 11:00:00-03:00 - 2023-03-06 12:00:00-03:00
    # 2023-03-06 14:00:00-03:00 - 2023-03-06 15:00:00-03:00
    # 2023-03-06 15:00:00-03:00 - 2023-03-06 16:00:00-03:00
    # 2023-03-07 09:00:00-03:00 - 2023-03-07 10:00:00-03:00
    # 2023-03-07 10:00:00-03:00 - 2023-03-07 11:00:00-03:00
    # 2023-03-07 11:00:00-03:00 - 2023-03-07 12:00:00-03:00
    # 2023-03-08 09:00:00-03:00 - 2023-03-08 10:00:00-03:00
    # 2023-03-08 10:00:00-03:00 - 2023-03-08 11:00:00-03:00
    # 2023-03-08 14:00:00-03:00 - 2023-03-08 15:00:00-03:00
    # 2023-03-08 15:00:00-03:00 - 2023-03-08 16:00:00-03:00
    # ...


List slots from slot-event ranges (an event that determines availability for scheduling)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <h1 align="center">
        <img src="https://github.com/leandcesar/google-calendar-simple-api-slots/blob/main/docs/images/example_2.png?raw=true" alt="List slots from free ranges"/>
    </h1>

.. code-block:: python

    from gcsa_slots.google_calendar import GoogleCalendar

    calendar = GoogleCalendar("your_email@gmail.com")
    for slot in calendar.get_slots(60, slot_summary="Free"):  # 60 minutes
        print(slot)

    # 2023-03-06 09:00:00-03:00 - 2023-03-06 10:00:00-03:00
    # 2023-03-06 11:00:00-03:00 - 2023-03-06 12:00:00-03:00
    # 2023-03-06 14:00:00-03:00 - 2023-03-06 15:00:00-03:00
    # 2023-03-06 15:00:00-03:00 - 2023-03-06 16:00:00-03:00
    # 2023-03-07 09:00:00-03:00 - 2023-03-07 10:00:00-03:00
    # 2023-03-07 10:00:00-03:00 - 2023-03-07 11:00:00-03:00
    # 2023-03-07 11:00:00-03:00 - 2023-03-07 12:00:00-03:00
    # 2023-03-08 09:00:00-03:00 - 2023-03-08 10:00:00-03:00
    # 2023-03-08 10:00:00-03:00 - 2023-03-08 11:00:00-03:00
    # 2023-03-08 14:00:00-03:00 - 2023-03-08 15:00:00-03:00
    # 2023-03-08 15:00:00-03:00 - 2023-03-08 16:00:00-03:00
    # ...


List slots specifying time range, slot interval, max events per slot and calendar ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from gcsa_slots.google_calendar import GoogleCalendar

    calendar = GoogleCalendar("your_email@gmail.com")
    calendar_id = "your calendar id"
    for slot in calendar.get_slots(
        45,
        slot_summary="fReE",
        case_sensitive=False,
        time_min=datetime(2023, 3, 6),
        time_max=datetime(2023, 3, 7),
        events_per_slot=3,
        calendar_id=calendar_id,
    ):
        print(slot)


Create event in first available slot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from gcsa_slots.google_calendar import GoogleCalendar

    calendar = GoogleCalendar("your_email@gmail.com")
    slots = calendar.get_slots(90, slot_summary="Free")
    slot = next(slots)
    slot.summary = "This is a test!"
    calendar.add_event(slot)

.. raw:: html

    <h1 align="center">
        <img src="https://github.com/leandcesar/google-calendar-simple-api-slots/blob/main/docs/images/example_3.png?raw=true" alt="List slots from free ranges"/>
    </h1>


.. _`Google Calendar Simple API`: https://github.com/kuzmoyev/google-calendar-simple-api
.. _`Getting started page`: https://google-calendar-simple-api.readthedocs.io/en/latest/getting_started.html
