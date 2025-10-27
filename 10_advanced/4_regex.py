import re

data = "Hello, Anderso Anderson!"

pattern = re.compile("Anderson")

print(re.fullmatch(pattern, data)) # None

print(re.search(pattern, data)) # <re.Match object; span=(7, 15), match='Anderson'>

print(re.findall(pattern, data)) # ['Anderson']

# -------------------------------------------------------------------

pattern_email = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
data = "andconc@gmail.com"
pattern = re.compile(pattern_email)
print(re.fullmatch(pattern, data))



