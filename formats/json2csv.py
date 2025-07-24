import csv
import sys
import json

writer = None

for line in sys.stdin:
   j = json.loads(line)
   if writer is None:
     writer = csv.DictWriter(f=sys.stdout, fieldnames=list(k.keys()))
   writer.writerow(j.values())
