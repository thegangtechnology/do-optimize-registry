import re
import datetime
from dateutil.relativedelta import relativedelta

def compare_date(data_time, threshold_time):
    return data_time <= threshold_time


def create_untag_images_list(file, keep_days=None, keep_tags=None, tag_list=None):
    # setup data
    untag_list = []
    date_format = "%Y-%m-%d"
    with open(file) as file:
        while data := file.readline():
            data_tags = re.search(r'\[(.*?)\]', str(data)).group(0)[1:-1]
            tags = data_tags.split(' ')
            data_time = datetime.datetime.strptime(re.search(r'\d{4}-\d{2}-\d{2}', str(data)).group(0), date_format)
            if keep_days is not None:
                if compare_date(data_time, keep_days):
                    print(f"Untag {data_tags} from repository")
                    untag_list.append(data_tags)
                else:
                    print(f"tag: {data_tags} on {data_time} is not outdated yet")
            if keep_tags is not None:
                tag_list.append(tags[-1])
                if compare_date(data_time, keep_tags):
                    # print(f"Untag {data_tags} from repository")
                    untag_list.append(tags[-1])
                else:
                    print(f"tag: {tags[-1]} on {data_time} is not outdated yet")
    return untag_list


keep_day1 = datetime.datetime.now() - datetime.timedelta(days=2)
keep_day2 = datetime.datetime.now() + datetime.timedelta(days=2)
keep_day3 = datetime.datetime.now() - datetime.timedelta(days=7)
expect_sha_list1 = ['sha-6fec643', 'sha-3af5855', 'sha-76adecb', 'sha-9970f23']
expect_sha_list2 = ['sha-1d097b7', 'sha-6fec643', 'sha-3af5855', 'sha-76adecb', 'sha-9970f23']
expect_sha_list3 = ['sha-76adecb', 'sha-9970f23']


def test_create_untag_sha_images_list():
    sha_list1 = create_untag_images_list('normalize-list.txt', keep_days=keep_day1)
    sha_list2 = create_untag_images_list('normalize-list.txt', keep_days=keep_day2)
    sha_list3 = create_untag_images_list('normalize-list.txt', keep_days=keep_day3)
    print("sha older than 2 days")
    assert sha_list1 == expect_sha_list1
    print("sha newer than 5 days")
    assert sha_list2 == expect_sha_list2
    print("sha older than 7 days")
    assert sha_list3 == expect_sha_list3


expect_version_list1 = ['0.2.6', '0.2.5-7', '0.2.5-6', '0.2.5-5', '0.2.5-4', '0.2.5-3', '0.2.5-2', '0.2.4-7', '0.2.5-1',
                        '0.2.5', '0.2.4-6', '0.2.4-5', '0.2.4-4', '0.2.4-3', '0.2.3-10', '0.2.3-9', '0.2.3-8',
                        '0.2.4-1', '0.2.4', '0.2.3-7', '0.2.3-6', '0.2.3-5', '0.2.3-4', '0.2.3-3', '0.2.3-2', '0.2.3-1',
                        '0.2.2-12', '0.2.2-11', '0.2.2-10', '0.2.2-9', '0.2.2-8', '0.2.2-7', '0.2.2-6', '0.2.2-5',
                        '0.2.2-4', '0.2.2-3', '0.2.1-12', '0.2.1-11', '0.2.1-10', '0.2.2-2', '0.2.1-9', '0.2.2-1',
                        '0.2.2', '0.2.1-8', '0.2.1-7', '0.2.1-6', '0.2.1-5', '0.2.1-4', '0.2.1-3', '0.2.1-2', '0.2.1-1',
                        '0.2.1', '0.2.0-6', '0.2.0-5', '0.2.0-4', '0.2.0-3', '0.2.0-2', '0.2.0-1', '0.2.0', '0.1.28-1',
                        '0.1.28', '0.1.27-2', '0.1.27-1', '0.1.27', '0.1.26', '0.1.25', '0.1.24', '0.1.23', '0.1.22',
                        '0.1.21', '0.1.20-3', '0.1.20-2', '0.1.20-1', '0.1.20', '0.1.19', '0.1.18', '0.1.17', '0.1.16',
                        '0.1.15', '0.1.14', '0.1.13-1', '0.1.13', '0.1.12', '0.1.11', '0.1.10', '0.1.9-1', '0.1.9',
                        '0.1.8-3', '0.1.8-2', '0.1.8-1', '0.1.8', '0.1.7', '0.1.6', '0.1.5', '0.1.4', '0.1.3', '0.1.2',
                        '0.1.1', '0.1.0']
expect_version_list2 = ['0.1.20', '0.1.19', '0.1.18', '0.1.17', '0.1.16', '0.1.15', '0.1.14', '0.1.13-1', '0.1.13',
                        '0.1.12', '0.1.11', '0.1.10', '0.1.9-1', '0.1.9', '0.1.8-3', '0.1.8-2', '0.1.8-1', '0.1.8',
                        '0.1.7', '0.1.6', '0.1.5', '0.1.4', '0.1.3', '0.1.2', '0.1.1', '0.1.0']
keep_tag1 = datetime.datetime.now() - relativedelta(months=6)
keep_tag2 = datetime.datetime.now() - relativedelta(months=8)

def test_create_untag_version_images_list():
    empyty_list=[]
    version_list1 = create_untag_images_list('normalize-version-list.txt', keep_tags=keep_tag1, tag_list=empyty_list)
    version_list2 = create_untag_images_list('normalize-version-list.txt', keep_tags=keep_tag2, tag_list=empyty_list)

    assert version_list1 == expect_version_list1
    assert version_list2 == expect_version_list2

