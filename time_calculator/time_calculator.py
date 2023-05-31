def add_time(start_time, duration, start_day=None):
    # Extract the hours, minutes, and period (AM/PM) from the start time
    start_time, period = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Extract the hours and minutes from the duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start time to 24-hour format
    if period == 'PM':
        start_hour += 12

    # Calculate the total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Calculate the final hours and minutes
    final_minutes = total_minutes % 60
    final_hours = total_minutes // 60

    # Determine the number of days later
    days_later = final_hours // 24

    # Adjust the final hours to 12-hour format
    final_hours %= 12
    if final_hours == 0:
        final_hours = 12

    # Determine the new period (AM/PM)
    if (total_minutes // 60) % 24 < 12:
        new_period = 'AM'
    else:
        new_period = 'PM'

    # Determine the day of the week if start_day is provided
    if start_day:
        start_day = start_day.lower()
        days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index].capitalize()
    else:
        new_day = ''

    # Prepare the final output
    if days_later == 0:
        result = f'{final_hours:02d}:{final_minutes:02d} {new_period}'
    elif days_later == 1:
        result = f'{final_hours:02d}:{final_minutes:02d} {new_period} (next day)'
    else:
        result = f'{final_hours:02d}:{final_minutes:02d} {new_period} ({days_later} days later)'

    if new_day:
        result += f', {new_day}'

    return result
    
#example
print(add_time("9:15 PM", "5:30"))
print(add_time("11:10 AM", "2:30", "Monday"))
