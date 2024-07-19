# flake8: noqa
import argparse
import datetime
import subprocess

filename = "normalize-list.txt"
weekago = datetime.datetime.now() - datetime.timedelta(days=7)
format = "%Y-%m-%d"

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--repo", dest="repository", help="A repository on Digital Ocean Container Registry", type=str)
args = parser.parse_args()
count = 1

with open(filename) as file:
    while line := file.readline():
        if count <= 5:
            data = line.rstrip().split()
            data[1] = data[1][1:-1]
            print(f"keep tag:{data[1]} as 5 latest image")
            count += 1
        else:
            data = line.rstrip().split()
            data[1] = data[1][1:-1]
            data_time = datetime.datetime.strptime(data[2], format)
            if data_time < weekago:
                # subprocess.run(["echo", "" +data[1] + " " +data[2]])
                print(f"Untag {data[1]} from repository")
                subprocess.run(["doctl", "registry", "repository", "dt", args.repository, data[1], "-f"])
            else:
                print(f"tag: {data[1]} on {data[2]} is not outdated yet")