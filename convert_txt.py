import re
import collections
import csv


def output_csv():
    with open('./out/小红书_笔记_评论.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        comments = [row[1] for row in reader]
        with open('./小红书_评论.txt', 'w+') as f:
            f.write('\n'.join(comments))

    # read the 8th column of the csv
    with open('./out/小红书_笔记.csv', 'r') as f:
        reader = csv.reader(f)
        # skip the header
        next(reader)
        # read the 8th column
        comments = [row[7] for row in reader]
        # write the 8th column to a txt
        with open('./out/小红书_笔记.txt', 'w+') as f:
            f.write('\n'.join(comments))

    with open('./out/小红书_笔记.csv', 'r') as f:
        reader = csv.reader(f)
        # skip the header
        next(reader)
        # read the 8th column
        comments = [row[1] for row in reader]
        # write the 8th column to a txt
        with open('./out/小红书_笔记.txt', 'w+') as f:
            f.write('\n'.join(comments))


output_csv()
