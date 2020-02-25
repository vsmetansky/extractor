import argparse

parser = argparse.ArgumentParser()

parser.add_argument('website', dest='website')
parser.add_argument('--page-num', dest='page_num', type=int, default=1)

args = parser.parse_args()
