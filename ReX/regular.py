import re

data = """
Lee 950623-1245634
Kim 950623-7800056
"""

sec = re.compile("(\d{6})[-]\d{7}")
print(sec.sub("\g<1>-*******", data))
