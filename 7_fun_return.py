# number = int("90909090")
# print(type(number), number + 1)

# string = str(123)
# print(type(string), string)

def plus(x, y):
    return x + y

result = plus(2, 3)
print(result)

def times(x, y):
    return x * y

result = times(9, 119)
print(result)

def emoji(fruit):
    if fruit == "apple":
        return "🍎"
    elif fruit == "grape":
        return "🍇"
    elif fruit == "pineapple":
        return "🍍"
    elif fruit == "kiwi":
        return "🥝"
    elif fruit == "peach":
        return "🍑"
    else:
        return " 👩 go home "

print(emoji("kiwi"))
print(emoji('mom'))
print(emoji('peach'))
