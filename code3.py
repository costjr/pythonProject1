"""litera = "q"
user = ""

while 1:
    user = input("Introduceti o litera")

    if litera == user:
        print("Felicitari")
        break
    else:
        print("Mai incearca")"""


"""test = []
l = int(input('Enter the array lenght'))
for i in range(0,l):
    test.append(int(input('Enter element with index' + str(i) + '\n')))"""


"""a = [3, 4, 5, 6, 7, 8, 9, 23, 45]

a.append(2)
print(a)

b = a.copy()
print(a, b)

c = a.count(3)
print(c)

b.extend(a)
print(b, a)

print(a.index(45))

a.insert(8, 'Sui')
print(a)

print(a.pop(8))
print(a)

a.remove(3)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

a.clear()
print(a)"""


"""tuple_ex = ('hola', 5, 'Test', 4.55, False)
print(tuple_ex[0])
print(tuple_ex + ('New', 'data', 1))"""


"""simple_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
set_array_2 = {4, 3, 2, 4, 5, 5, 41, 2}
set_array = set(simple_array)
print(simple_array)
print(set_array)
print(set_array_2)"""


"""dictionary = {'Key' : 'Value', "Int": 3, "Float": 23.4, "Bool": True}
print(dictionary.get('Key'))
dictionary.update({'Int': 4})
dictionary['Key'] = "New value"
print(dictionary)"""


register=[]
student={}
st_num = int(input("How Many students do you want to add"))
sub_num = int(input("How Many Subjetc do they have?"))

for a in range(0, st_num):
    s_name = input("name")
    student.update({"name": s_name})

    for b in range(0, sub_num):
        subject = input('subject')
        mark = int(input("Mark:"))

        student.update({subject: mark})

    register.append(student.copy())

print(register)



