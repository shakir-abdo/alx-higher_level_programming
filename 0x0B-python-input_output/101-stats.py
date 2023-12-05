#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size:", size)
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")

if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        while True:
            try:
                line = input()
            except EOFError:
                break

            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            try:
                fields = line.split()
                size += int(fields[-1])
                if fields[-2] in valid_codes:
                    status_codes[fields[-2]] = status_codes.get(fields[-2], 0) + 1
            except (IndexError, ValueError):
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
