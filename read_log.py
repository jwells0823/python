#!/usr/bin/python3

import sys
import pathlib

log_path=sys.argv[1] if len(sys.argv) > 1 else "/var/log"
log_filename = sys.argv[2] if len(sys.argv) > 2 else "syslog"
log_file = pathlib.Path(log_path) / log_filename

def find_errors():
    with log_file.open() as f:
        for line in f:
            if "error" in line.lower():
                print(line.strip())


def main():
    if log_file.exists():
        find_errors()
    else:
        print("Log file {log_file} does not exist.")

    
if __name__ == "__main__":
    main()
