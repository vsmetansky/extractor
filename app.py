if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('website', dest='website')
    parser.add_argument('-n', '--page-num', dest='page_num', type=int, default=1)

    args = parser.parse_args()
