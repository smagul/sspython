import re

string = " Two tro."

m = re.findall("t[wr]o", string, re.IGNORECASE)

print(m)
