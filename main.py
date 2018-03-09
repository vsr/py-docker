from __future__ import print_function
import time
import os
from colorprint import *

MAX_RUNS = int(os.environ.get('runs', '100000'))
message = os.environ.get('message', 'Hello')
time_interval = 5
count = 0

while True:
    if count >= MAX_RUNS:
        exit(1)
    print(message, color='blue')
    count += 1
    time.sleep(time_interval)