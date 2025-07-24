import csv
import sys
import json

reader = csv.DictReader(sys.stdin)
for record in reader:
   sys.stdout.write(json.dumps(record))
   sys.stdout.write('\n')
