colors = [] # ()
# print(colors)

colors.append("red")
colors.append("blue")
colors.append("yellow")
colors.append("green")
colors.append("pink")
colors.append("brown poo")
# print(colors)

# print(colors[3])
# print(colors[1], colors[2])

colors.pop() # pop "brown poo"
colors.pop() # pop "pink"
colors.pop()
for color in colors:
    print(color)
