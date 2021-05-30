import re
p = re.compile(".+(?=:)")
m = p.search("http://naver.com")
print(m.group())
