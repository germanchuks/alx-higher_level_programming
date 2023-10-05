#!/usr/bin/python3

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Description of script')

    parser.add_argument('integers', type=int, nargs='*', default=[0],
                        help='List of integers')
    parser.add_argument('--sum', dest='operation', action='store_const',
                        const=sum, default=sum, help='Sum the integers')

    args = parser.parse_args()

    if args.operation is None:
        result = args.integers[0]
    else:
        result = args.operation(args.integers)

    print(result)
