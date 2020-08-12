#coding=utf-8

import codecs
import glob 
import sys
import os
import argparse
import csv
import re
PATTERN = re.compile(r'circuitbr|circuit br|Circuit Br|CircuitBr|Circuit br|Circuitbr|Lockdown|lockdown|covid|Covid|COVID|coronavirus|Coronavirus')

def process(file):
    with open(file, newline='') as csvfile:
        data = []
        n = 0
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            text = row["text"]
            if re.search(PATTERN, text):
                # print(text)
                n += 1
                data.append(row)
    return n, data

def write(data, file):
    with open(file, 'w', newline='') as csvfile:
        fieldnames = ['source', 'shared_from', 'date', 'text', 'reactions', 'likes', 'ahah', 'love', 'wow', 'sigh', 'grrr', 'comments', 'post_id', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(description='filter covid data.',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input_dir', help='input directory')
    parser.add_argument('output', help='output directory')

    args = parser.parse_args()

    filenames = glob.glob(os.path.join(args.input_dir, '*.csv'))
    if  os.path.exists(args.output) == False: os.makedirs(args.output)
    n = 0
    for file in filenames:
        basename = os.path.basename(file)
        output_filename = os.path.join(args.output, basename)
        match_n, data = process(file)
        n += match_n
        print(basename, match_n)
        write(data, output_filename)
    print(n)


main()