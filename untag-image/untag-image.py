# flake8: noqa
import argparse
import datetime
import subprocess
import re

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--repo", dest="repository", help="A repository on Digital Ocean Container Registry", type=str)
parser.add_argument("--days", dest="days" ,help="Number of days for keeping images. Default to 0 if specific keep-latest,  default to 7 if not specific keep-latest", type=int)
parser.add_argument("--keep-latest", dest="keep_latest_tags", help="Untag versions from imgages older than keep_latest images, Default to 0 (Disable)", type=int)
args = parser.parse_args()
count = 1
num_latest_image = 5

keep_days = datetime.datetime.now() - datetime.timedelta(days=args.days)
format = "%Y-%m-%d"

def untag_images(num, count):
    tags = re.search(r'\[(.*?)\]', str(line)).group(0)
    if count <= num:
        print(f"keep tag: {tags} as {num} latest image")
        count += 1
    else:
        data_time = datetime.datetime.strptime(re.search(r'\d{4}-\d{2}-\d{2}', str(line)).group(0), format)
        if count == num + 1:
            print(f"!!! images that updated before {keep_days} will be removed !!!")
            count += 1
        if data_time < keep_days:
            # subprocess.run(["echo", "" +data[1] + " " +data[2]])
            print(f"Untag {tags} from repository")
            subprocess.run(["doctl", "registry", "repository", "dt", args.repository, tags, "-f"])
        else:
            print(f"tag: {tags} on {data_time} is not outdated yet")
    return True

filename = "normalize-version-list.txt" if args.keep_latest_tags else "normalize-list.txt"
num = args.keep_latest_tags if args.keep_latest_tags else num_latest_image

with open(filename) as file:
    while line := file.readline():
        untag_images(num, count)
        count +=1