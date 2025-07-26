from scheduler import get_shift_for_user
from datetime import datetime, timedelta
from tabulate import tabulate

def display_schedule_table(user_list, start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    date_range = [
        start_date + timedelta(days=i)
        for i in range((end_date - start_date).days + 1)
    ]

    headers = ["ID", "Nama"] + [d.strftime("%Y-%m-%d") for d in date_range]
    table = []

    for idx, user in enumerate(user_list, start=1):
        row = [idx, user]
        for d in date_range:
            shift = get_shift_for_user(user, d)
            row.append(shift)
        table.append(row)

    print(tabulate(table, headers=headers, tablefmt="grid"))

# Contoh pemanggilan
if __name__ == "__main__":
    user_list = ["Ahmad", "Vidi", "Yono", "Yohan"]
    display_schedule_table(user_list, "2024-12-26", "2025-01-02")
