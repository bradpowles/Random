COACHCOST = 550
TICKETCOST = 30

def calculate(ticket, coach):
    n = int(input("No. of students? "))
    tot = (((n-(n//11))*ticket)+coach)
    print("Total cost: {}".format(tot))
    per = tot//n
    print("Per Student cost: {}".format(per))

calculate(TICKETCOST, COACHCOST)