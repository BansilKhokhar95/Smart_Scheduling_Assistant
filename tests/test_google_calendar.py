from datetime import datetime
from app.services.calendar.google_calendar import create_event_with_meet

if __name__ == "__main__":
    # Set event details
    event_summary = "Team Sync Meeting"
    start_time = datetime(2025, 5, 10, 15, 0)  # 3:00 PM (local time)
    duration_minutes = 30
    attendees = ["bansilkhokhar81@gmail.com"]  # Replace with a real email

    # Create event
    event = create_event_with_meet(
        summary=event_summary,
        start_time=start_time,
        duration_minutes=duration_minutes,
        attendees_emails=attendees
    )

    # Output result
    print("✅ Event Created Successfully:")
    print(f"Title      : {event['summary']}")
    print(f"Start Time : {event['start']}")
    print(f"End Time   : {event['end']}")
    print(f"Meet Link  : {event['meet_link']}")
