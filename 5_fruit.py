print("> What fruit?")
fruit = input()
print('> How many?')
count = int(input())

# 1.5 실수
# 15  정수 (integer)
# "15" -> 15

if fruit == "apple":
    for i in range(count):
        print(i, "🍎", end="")
elif fruit == "banana":
    for i in range(count):
        print(i, '🍌', end="")
elif fruit == "orange":
    for i in range(count):
        print(i, '🍊', end="")
elif fruit == "mango":
    for i in range(count):
        print(i, '🥭', end="")
else:
    for i in range(count):
        print(i, '💩', end="")

print()
print("> Bye~!")