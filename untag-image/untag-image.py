# flake8: noqa
import argparse
import datetime
from dateutil.relativedelta import relativedelta
import subprocess
import re

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--repo", dest="repository", help="A repository on Digital Ocean Container Registry", type=str)
parser.add_argument("--days", dest="days" , default=7,help="Number of days for keeping images. Default to 0 if specific keep-latest,  default to 7 if not specific keep-latest", type=int)
parser.add_argument("--keep-tag", dest="keep_latest_tags", default=6, help="Untag versions from imgages older than keep_latest images, Default to 6 months", type=int)
args = parser.parse_args()
count = 1
num_latest_image = 5

if args.days is not None:
    keep_days = datetime.datetime.now() - datetime.timedelta(days=args.days)
if args.keep_latest_tags is not None:
    keep_tags = datetime.datetime.now() - relativedelta(months=args.keep_latest_tags)
format = "%Y-%m-%d"

def untag_images(num, count):
    tags = re.search(r'\[(.*?)\]', str(line)).group(0)
    if count <= num:
        print(f"keep tag: {tags} as {num} recent image version")
        count += 1
    else:
        data_time = datetime.datetime.strptime(re.search(r'\d{4}-\d{2}-\d{2}', str(line)).group(0), format)
        if count == num + 1:
            print(f"!!! images that updated before {keep_days} will be removed !!!")
            count += 1
        if data_time < keep_tags:
            if data_time < keep_days:
                # subprocess.run(["echo", "" +data[1] + " " +data[2]])
                print(f"Untag {tags} from repository")
                #subprocess.run(["doctl", "registry", "repository", "dt", args.repository, tags, "-f"])
        else:
            print(f"tag: {tags} on {data_time} is not outdated yet")
    return True

filename = "normalize-version-list.txt" if args.keep_latest_tags else "normalize-list.txt"

with open(filename) as file:
    while line := file.readline():
        untag_images(num_latest_image, count)
        count +=1