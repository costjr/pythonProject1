import addData
import readData

print("Vom creea o 'Agenda' pentru un elev")
print("Va trebui sa introduci Numele, Clasa, Materiile si notele elevului.")
print("---------Aveti doua optiuni-----------")
print("1.Adaugi date in resgistru")
print("2.Citesti datele din resgistru")

optiunea = int(input("Optiunea ta: "))

if optiunea == 1:
    addData.add()
elif optiunea == 2:
    readData.read()
else:
    print("Alege dintre 1 si 2")


