# хорошая документация: https://docs.python.org/3/library/argparse.html

import argparse

parser = argparse.ArgumentParser(description='Process some integers.', epilog='Good bye')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
