from datetime import datetime, timedelta

# Pola shift per user
shift_patterns = {
    "Ahmad": ["P", "P", "S", "S", "M", "M", "L"],
    "Vidi":  ["S", "S", "M", "M", "L", "L", "P", "S"],
    "Yono":  ["M", "M", "P", "L", "P", "P", "M"],
    "Yohan": ["L", "P", "P", "P", "S", "P", "L", "S", "S", "P", "S", "P", "S", "P"]
}

# Tanggal mulai pola
start_date = datetime.strptime("2024-12-26", "%Y-%m-%d").date()

def get_shift_for_user(user_name, date):
    if user_name not in shift_patterns:
        return "User tidak ditemukan"
    pattern = shift_patterns[user_name]
    delta_days = (date - start_date).days
    shift = pattern[delta_days % len(pattern)]
    return shift

def get_schedule_for_user(user_name, start_date_str, end_date_str):
    result = {}
    start = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    current = start
    while current <= end:
        result[current.strftime("%Y-%m-%d")] = get_shift_for_user(user_name, current)
        current += timedelta(days=1)
    return result
