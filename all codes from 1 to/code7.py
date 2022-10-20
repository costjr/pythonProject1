"""
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

y = datetime.datetime(2020, 5, 17)
print(y)"""

"""
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)"""

"""
x = abs(-7.25)#functia pentru calcularea modulului
x = pow(4, 3)#returneaza valoarea lui x
"""

"""
import math
z = math.sqrt(64)

x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)
print(z)"""

"""
import json
# exemple of JSON
x = '{ "name":"Alex", "age":20, "city":"Falesti"}'

# parese x:
y = json.loads(x)
print(y["age"])
"""

"""
import json
x = {
    "name":"Alex",
    "age":20, "city":
    "Falesti"
}
y = json.dumps(x)
print(y)
"""

"""
import json
print(json.dumps({"n": 'John', "age": 30}))
print(json.dumps(["s", "lol"]))
print(json.dumps(("s", "lol")))
print(json.dumps('hello'))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#x = ident 4
"""

"""
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print('yes! We have a match')
else:
    print("No match")
"""

