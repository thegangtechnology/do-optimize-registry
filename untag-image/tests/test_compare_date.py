import datetime

date1 = datetime.datetime.now()
date2 = datetime.datetime.now() - datetime.timedelta(days=1)
date3 = datetime.datetime.now() + datetime.timedelta(days=1)
def compare_date(data_time, threshold_time):
    return data_time <= threshold_time
def test_compare_date():
    # Test case where data_time is before threshold_time
    assert compare_date(date1, date3) == True

    # Test case where data_time is after threshold_time
    assert compare_date(date1, date2) == False

    # Test case where data_time is equal to threshold_time
    assert compare_date(date1, date1) == True