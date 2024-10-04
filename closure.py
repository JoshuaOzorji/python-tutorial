person = "Dave"
coins = 3

# print("\n" + person + " has " + str(coins) + "coins left.")

# message = "\n%s has %s coins left." % (person,
#                                        coins)
# print(message)

# message = "\n{} has {} coins left.".format(person,
#                                            coins)
# print(message)

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 5} coins left"
print(message)

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
