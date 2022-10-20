import datetime

registru = {}
materii = []
note = []

def add():
    c2 = input("Care este numele elevului?")
    registru.update({"Nume": c2})

    c3 = int(input('Ce calsa e '+c2+" ? "))
    registru.update({"Clasa": c3})

    c4 = int(input("Cate materii are "+c2+" ?"))
    for i in range(0, c4):
        materii.append(input("Materia:"))
        note.append(int(input("Nota:")))
    for l in range(0, len(materii)):
        registru.update({materii[l]: note[l]})

    data = datetime.datetime.now()
    registru.update({"Data cand a avut loc inregistrarea":data})

    a = input("Doresti sa vezi datele din registru? da/nu  ")
    if a == "da":
        print(registru)
    else:
        print("OK")