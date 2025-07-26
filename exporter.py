import csv
from datetime import datetime, timedelta
from scheduler import get_shift_for_user

def export_schedule_to_csv(user_list, start_date_str, end_date_str, filename):
    start = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end = datetime.strptime(end_date_str, "%Y-%m-%d").date()

    # Buat list tanggal header
    date_list = []
    current = start
    while current <= end:
        date_list.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nama"] + date_list)

        for idx, user in enumerate(user_list, start=1):
            row = [f"U{idx:03d}", user]
            for date_str in date_list:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                shift = get_shift_for_user(user, date_obj)
                row.append(shift)
            writer.writerow(row)
