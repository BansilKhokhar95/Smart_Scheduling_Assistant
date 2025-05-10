# app/services/calendar/google_calendar.py

from datetime import datetime, timedelta
from app.utils.oauth import get_calendar_service
import pytz

def create_event_with_meet(summary, start_time, duration_minutes, attendees_emails=[]):
    service = get_calendar_service()

    timezone = 'Asia/Kolkata'  # Change to your local timezone
    start = start_time.astimezone(pytz.timezone(timezone))
    end = start + timedelta(minutes=duration_minutes)

    event = {
        'summary': summary,
        'start': {
            'dateTime': start.isoformat(),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end.isoformat(),
            'timeZone': timezone,
        },
        'attendees': [{'email': email} for email in attendees_emails],
        'conferenceData': {
            'createRequest': {
                'conferenceSolutionKey': {'type': 'hangoutsMeet'},
                'requestId': f"meet-{datetime.now().timestamp()}"
            }
        },
    }

    created_event = service.events().insert(
        calendarId='primary',
        body=event,
        conferenceDataVersion=1
    ).execute()

    meet_link = created_event.get('hangoutLink')
    return {
        'summary': created_event['summary'],
        'start': created_event['start']['dateTime'],
        'end': created_event['end']['dateTime'],
        'meet_link': meet_link
    }
