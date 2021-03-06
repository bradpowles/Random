class Order:
    def new(self, parts):
        wholeprice = 0
        order = {}
        for item in parts:
            valid = False
            while valid == False:
                print("-----{}-----".format(item))
                for component in parts[item]:
                    print("{}: £{} Remaining stock: {}".format(component[0], component[1], component[2]))
                partchoice = input("{}: ".format(item[0]))
                for component in parts[item]:
                    if partchoice == component[0]:
                        order[item] = component
                        valid = True
                if valid == False:
                    print("Try again.")
            print(order)


        print("Order Finished")
        print(order)
        for i in range(len(parts)):
            print(parts[i][0], order[i])

        wholeprice = wholeprice * 120
        wholeprice = int(wholeprice) / 100
        print("Price is £", wholeprice, " (Including VAT 20%)", sep="")
        print("")
        input("Press enter to order another computer")

class Menu:
    def __init__(self):
        self.parts = {
            "Processor": [["p3", 100, 10], ["p5", 120, 10], ["p7", 80, 10]],
            "RAM": [["16", 75, 10], ["32", 150, 10]],
            "Storage": [["1TB", 50, 10], ["2TB", 100, 10]],
            "Screen size": [["19", 65, 10], ["23", 120, 10]],
            "Case": [["mini", 40, 10], ["midi", 70, 10]],
            "USB ports": [["2", 10, 10], ["4", 20, 10]]
        }
    def neworder(self):
        Order().new(self.parts)

Menu().neworder()