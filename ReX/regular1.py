import re

data = """
물,100,1
물,100,1.1
불,100,1.1
전기,100,1.1
바위,100,1.1
"""

Po1 = re.compile("[물]{1,2},[0-9]{3},[0-9]{1}.[0-9]{1}")
Po = re.compile("[가-핳]{1,2},[0-9]{3},[0-9]{1}.[0-9]{1}")
za = re.compile("[가-핳]{1,2},[0-9]{3},\d*.?\d+")

print(Po1.findall(data))
print(Po.findall(data))
print(za.findall(data))
