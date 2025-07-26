import datetime
from scheduler import get_shift_for_date

def test_shift_ahmad_day_0():
    assert get_shift_for_date("Ahmad", datetime.date(2024, 12, 26)) == 'P'

def test_shift_ahmad_day_7():
    assert get_shift_for_date("Ahmad", datetime.date(2025, 1, 2)) == 'P'

def test_shift_yono_day_2():
    assert get_shift_for_date("Yono", datetime.date(2024, 12, 28)) == 'P'
