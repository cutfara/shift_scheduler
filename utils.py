import pandas as pd
from scheduler import user_patterns, get_schedule_range

def export_all_user_schedule_to_csv(start_date, end_date, filename="schedule.csv"):
    data = []
    for idx, user in enumerate(user_patterns.keys(), start=1):
        schedule = get_schedule_range(user, start_date, end_date)
        row = {"ID": str(idx).zfill(3), "Nama": user}
        row.update(schedule)
        data.append(row)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV berhasil dibuat: {filename}")
