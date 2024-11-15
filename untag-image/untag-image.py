# flake8: noqa
import argparse
import datetime
from dateutil.relativedelta import relativedelta
import requests
import subprocess
import re


# Get current version of each Environment
def get_version(repository, staging_url, production_url):
    # Set path to get version
    if repository == 'admin':
        version_path = '/admin/assets/git-info.json'
    elif repository == 'backend':
        version_path = '/backend/v1/version/'
    elif repository == 'frontend':
        version_path = '/assets/git-info.json'

    # Send request to get version
    staging_response = requests.get(f"{staging_url}{version_path}")
    staging_result = staging_response.json()
    production_response = requests.get(f"{production_url}{version_path}")
    production_result = production_response.json()
    return [staging_result['commitTag'], production_result['commitTag']]


# Sort version
def parse_version(version):
    # Regex pattern to split the version by periods and hyphens
    version_parts = re.split(r'[.-]', version)
    # Convert the version parts into integers, where applicable
    return tuple(int(part) if part.isdigit() else part for part in version_parts)


# Check if time is older than set threshold
def compare_date(data_time, threshold_time):
    if data_time < threshold_time:
        return True
    else:
        return False


# Untag old image
def create_untag_images_list(file, repository, keep_days=None, keep_tags=None, untag_list=[], tag_list=[]):
    # setup data
    date_format = "%Y-%m-%d"
    with open(file) as file:
        while data := file.readline():
            data_tags = re.search(r'\[(.*?)\]', str(data)).group(0)[1:-1]
            tags = data_tags.split(' ')
            data_time = datetime.datetime.strptime(re.search(r'\d{4}-\d{2}-\d{2}', str(data)).group(0), date_format)
            if keep_days is not None:
                if compare_date(data_time, keep_days):
                    #print(f"Untag {data_tags} from repository")
                    untag_list.append(data_tags)
                else:
                    print(f"tag: {data_tags} on {data_time} is not outdated yet")
            if keep_tags is not None:
                tag_list.append(tags[-1])
                if compare_date(data_time, keep_tags):
                    #print(f"Untag {data_tags} from repository")
                    untag_list.append(tags[-1])
                else:
                    print(f"tag: {tags[-1]} on {data_time} is not outdated yet")


def untag_image(untag_list, repository):
    for image in untag_list:
        print(f"untag: {image}")
        subprocess.run(["doctl", "registry", "repository", "dt", repository, image, "-f"])


# Main Execution Function
def main():
    # Setup variables
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument("--repo", dest="repository", default="backend",
                        help="A repository on Digital Ocean Container Registry", type=str)
    parser.add_argument("--keep-sha", dest="days", default=7,
                        help="Number of days for keeping images. Default to 0 if specific keep-latest,  default to 7 "
                             "if not specific keep-latest",
                        type=int)
    parser.add_argument("--keep-tag", dest="months", default=6,
                        help="Untag versions from imgages older than x months, Default to 6 months", type=int)
    args = parser.parse_args()
    staging_url = f"https://staging.app.ruammitr.io"
    production_url = f"https://app.ruammitr.io"
    untag_sha_list = []
    untag_verison_list = []
    tag_list = []
    keep_list = []

    # Set keep threshold and untag image
    # Untag only sha images
    if args.days is not None:
        keep_days = datetime.datetime.now() - datetime.timedelta(days=args.days)
        sha_filename = "normalize-list.txt"
        create_untag_images_list(sha_filename, args.repository, keep_days=keep_days, untag_list=untag_sha_list)

    # # Untag version images
    if args.months is not None:
        keep_tags = datetime.datetime.now() - relativedelta(months=args.months)
        version_list = get_version(repository=args.repository, staging_url=staging_url, production_url=production_url)
        # version_list = ['0.2.0-4', '0.1.10']
        version_filename = "normalize-version-list.txt"
        create_untag_images_list(version_filename, args.repository, keep_tags=keep_tags, untag_list=untag_verison_list, tag_list=tag_list)
        # Sort list
        tag_list.remove("develop")
        sorted_tag = sorted(tag_list, key=parse_version, reverse=True )
        sorted_tag = ["develop"] + sorted_tag
        for tag in sorted_tag:
            if tag in version_list or tag == "develop":
                index_keep = sorted_tag.index(tag)
                for i in range(5):
                    keep_list.append(sorted_tag[index_keep+i])
        sorted_untag_versions_list = sorted(untag_verison_list, key=parse_version, reverse=True)
        print(f"keep version list : {keep_list}")
        # remove keep version from untag list
        for keep_version in keep_list:
            if keep_version in sorted_untag_versions_list:
                sorted_untag_versions_list.remove(keep_version)
    # Untag image
    print(f"untag sha list: {untag_sha_list}")
    untag_image(untag_sha_list, args.repository)
    print(f"untag version list: {sorted_untag_versions_list}")
    untag_image(sorted_untag_versions_list, args.repository)


# Standard Script Entry Point
if __name__ == "__main__":
    main()
