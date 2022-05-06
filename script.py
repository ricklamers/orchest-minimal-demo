import os
import sys
import orchest
import random

if "KEY_FILE_LOCATION" not in os.environ:
    print("KEY_FILE_LOCATION is a required environment variable. Exiting...")
    sys.exit()
    

some_data = list(range(100))

for k, v in enumerate(some_data):
    if k > 0:
        some_data[k] = some_data[k-1] + random.randint(-5, 5)
    
orchest.output(some_data, name='sequence')
