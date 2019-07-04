interests = ["Working", "Hussling", "Sleeping", "Fucking", "Eating"]

ln = len(interests)

for x in interests:
	print(x)

interests.pop(2)
interests.remove("Eating")
interests.append("Reading")
print("\n")
print("Now my about my interests..\n")

for y in interests:
	print(y)


