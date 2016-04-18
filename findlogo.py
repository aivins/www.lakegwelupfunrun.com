from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from os import listdir
from os.path import isfile, join

import sys

imagefiles = [f for f in listdir("sponsor_logos") if f.endswith("jpg")]

for line in sys.stdin:
    (name, url) = line.split(',')
    name = name.strip()
    url = url.strip()
    found = False
    for file in imagefiles:
        score = fuzz.ratio(name, file)
        if score > 40:
            found = True
            print(",".join((name,url,file)))
    
    if not found:
        print(",".join((name,url,"")))

