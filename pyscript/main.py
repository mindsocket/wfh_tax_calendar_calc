import datetime
import recurring_ical_events
import icalendar
import js

current_calendar = None

async def handle_file_upload(event):
    global current_calendar
    file = event.target.files.item(0)
    my_bytes: bytes = await get_bytes_from_file(file)
    current_calendar = icalendar.Calendar.from_ical(my_bytes)
    update_analysis(None)
    
async def get_bytes_from_file(file):
    array_buf = await file.arrayBuffer()
    return array_buf.to_bytes()

def update_analysis(event):
    if not current_calendar:
        return
    
    fyear = int(js.document.getElementById('fyear').value)
    output = analyze_calendar(current_calendar, fyear)
    js.document.getElementById('output').innerHTML = output

from collections import Counter
def analyze_calendar(cal, fyear):
    start_date = datetime.datetime(fyear - 1, 7, 1)
    end_date = datetime.datetime(fyear, 6, 30)
    events = recurring_ical_events.of(current_calendar).between(start_date, end_date)

    total_hours = 0
    day_total_hours = Counter()
    for event in events:
        start = event["DTSTART"].dt
        end = event["DTEND"].dt
        duration = end - start
        if isinstance(duration, datetime.timedelta):
            duration = duration.total_seconds() / 3600
        else:
            duration = 0

        total_hours += duration
        try:
            day_total_hours[start.date()] += duration
        except AttributeError:
            # Handle the case where start.date() is not available
            day_total_hours[start] += duration
    result = f"Total hours (use this to calculate your deduction): {total_hours} hours\n\n"
    result += "The following information is for verifying the analysis:\n"
    result += f"Total days with entries: {len(day_total_hours)}\n"
    result += "Daily hours breakdown:\n"
    for day, hours in sorted(day_total_hours.items()):
        if hours > 10:
            result += f"<span style='color: red;'>More than 10 hours...</span>\n"
        # If weekend, highlight
        if day.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            result += f"<span style='color: orange;'>Weekend hours...</span>\n"
        result += f"{day}: {hours} hours\n"
    return result
