from scheduler import get_schedule_range
import datetime

user = "Ahmad"
start = datetime.date(2025, 1, 5)
end = datetime.date(2025, 1, 8)

schedule = get_schedule_range(user, start, end)
print(f"Jadwal {user}:")
for date, shift in schedule.items():
    print(f"{date} => {shift}")
from utils import export_all_user_schedule_to_csv

export_all_user_schedule_to_csv(
    datetime.date(2025, 1, 5),
    datetime.date(2025, 1, 8)
)
