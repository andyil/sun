import csv
import sys
import json

writer = None

for line in sys.stdin:
   j = json.loads(line)
   if writer is None:
     writer = csv.DictWriter()
   writer.writerow(j.values())
