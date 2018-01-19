tot = 0

price_cpu = [100, 120, 200]
type_cpu = ["p3", "p5", "p7"]
input_cpu = input("What CPU? 1) p3  2) p5  3)p7")
tot += price_cpu[(int(input_cpu) - 1)]
input_cpu = type_cpu[(int(input_cpu) - 1)]

print("Choices: {}".format(input_cpu))
print(tot)


