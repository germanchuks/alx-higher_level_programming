#!/usr/bin/python3
"""Function to read stdin line by line and computes metrics."""


def print_metrics(size, status_codes):
    """
    This function prints accumulated metrics such as file size and status
    code counts.

    Args:
        size (int): The accumulated file size.
        status_codes (dict): A dictionary containing the accumulated count
        of status codes.
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")


if __name__ == "__main__":
    import sys

    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_codes = {}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(total_size, status_codes)
                line_count = 1
            else:
                line_count += 1

            line = line.split()

            try:
                total_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
