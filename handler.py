

from pprint import pprint
import os

content_path = "./content/sonnets.txt"
content_path = os.path.join(os.path.dirname(__file__), content_path)


def run(event, context):
    print("Hello World!")
    # parse content/sonnet.txt
    with open(content_path, "r") as f:
        lines = f.readlines()
        # filter out pattern [ (number) ]
        for line in lines:
            if line.startswith("["):
                continue
            print(line)

    # return either a line or multiple lines if under 280 characters

    # maybe save entry into a db to avoid duplicates
    # send payload to twitter api
