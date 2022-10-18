import data_read
import data_write
class clasa():
    def __init__(self, nr_elevi, nr_subiecte):
        self.nr =nr_elevi
        self.nr_d =nr_subiecte
        self.elevi = {}
        self.registru =[]
    def adaugare(self):
        for i in range(self.nr):
            name = input("name")
            self.elevi.update({"Name": name})
        for j in range(self.nr_d):
            self.elevi.update(
                {"math":8}
            )

    def read(self):
        for i in self.registru:
            print(i["name"], i["math"])



while 1:
    try:
        alegere = int(input("1 for add\n2 for read"))
    except:
        print("Wrong Data")

