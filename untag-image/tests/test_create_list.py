import re
import datetime
from dateutil.relativedelta import relativedelta


def compare_date(data_time, threshold_time):
    return data_time <= threshold_time


def create_untag_images_list(file, keep_days=None, keep_tags=None, tag_list=None, version_list=None):
    # setup data
    latest_tag = ""
    selected_tag = ""
    untag_list = []
    date_format = "%Y-%m-%d"
    semver_pattern = r'^\d+\.\d+\.\d+$'
    with open(file) as file:
        while data := file.readline():
            data_tags = re.search(r'\[(.*?)\]', str(data)).group(0)[1:-1]
            tags = data_tags.split(' ')
            for tag in tags:
                if tag == "develop" or tag == "staging" or tag == "production" or tag == "latest":
                    selected_tag = "env"
                    break
                if bool(re.match(semver_pattern, tag)):
                    selected_tag = tag
                    break
                else:
                    selected_tag = ""
            data_time = datetime.datetime.strptime(re.search(r'\d{4}-\d{2}-\d{2}', str(data)).group(0), date_format)
            if keep_days is not None:
                if compare_date(data_time, keep_days):
                    #print(f"Untag {data_tags} from repository")
                    untag_list.append(data_tags)
                else:
                    print(f"tag: {data_tags} on {data_time} is not outdated yet")
            if keep_tags is not None:
                if selected_tag != "env":
                    tag_list.append(selected_tag)
                if compare_date(data_time, keep_tags):
                    #print(f"Untag {data_tags} from repository")
                    if selected_tag != "env":
                        untag_list.append(selected_tag)
                    else:
                        print(f"tag is deployed version on dev or staging or production")
                else:
                    print(f"tag: {selected_tag} on {data_time} is not outdated yet")
        if "" in untag_list:
            untag_list.remove("")
    return untag_list


file_1 = "tests/normalize-version-list.txt"
file_2 = "tests/normalize-version-list2.txt"

keep_tag1 = datetime.datetime.now() - relativedelta(months=6)
keep_tag2 = datetime.datetime.now() - relativedelta(months=5)

expect_version_list1 = []
expect_version_list2 = ['1.0.34']


def test_create_untag_version_images_list():
    empyty_list = []
    version_list1 = create_untag_images_list(file_1, keep_tags=keep_tag1, tag_list=empyty_list)
    version_list2 = create_untag_images_list(file_2, keep_tags=keep_tag2, tag_list=empyty_list)
    print(version_list2)
    assert version_list1 == expect_version_list1
    assert version_list2 == expect_version_list2