import sys
sys.path.insert(0, '/')
from utils.date_utils import get_next_day

class TestDateUtils():

    def test_forecast_get_nex_day_simple_date(self):
        assert get_next_day("2022-01-01") == "2022-01-02"
    
    def test_forecast_get_nex_day_end_of_month_31_days(self):
        assert get_next_day("2022-01-31") == "2022-02-01"
    
    def test_forecast_get_nex_day_end_of_month_30_days(self):
        assert get_next_day("2022-04-30") == "2022-05-01"
    
    def test_forecast_get_nex_day_february_leap_year(self):
        assert get_next_day("2020-02-28") == "2020-02-29"
    
    def test_forecast_get_nex_day_february_non_leap_year(self):
        assert get_next_day("2021-02-28") == "2021-03-01"