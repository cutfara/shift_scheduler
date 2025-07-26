import datetime

user_patterns = {
    "Ahmad": ['P', 'P', 'S', 'S', 'M', 'M', 'L'],
    "Vidi": ['S', 'S', 'M', 'M', 'L', 'L', 'P', 'S'],
    "Yono": ['M', 'M', 'P', 'L', 'P', 'P', 'M'],
    "Yohan": ['L', 'P', 'P', 'P', 'S', 'P', 'L', 'S', 'S', 'P', 'S', 'P', 'S', 'P'],
}

start_date_base = datetime.date(2024, 12, 26)

def get_shift_for_date(user, target_date):
    pattern = user_patterns.get(user)
    if not pattern:
        return None
    days_diff = (target_date - start_date_base).days
    index = days_diff % len(pattern)
    return pattern[index]

def get_schedule_range(user, start_date, end_date):
    current_date = start_date
    schedule = {}
    while current_date <= end_date:
        shift = get_shift_for_date(user, current_date)
        schedule[str(current_date)] = shift
        current_date += datetime.timedelta(days=1)
    return schedule
