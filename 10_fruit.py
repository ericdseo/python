print("> What fruit? (apple, banana, orange, mango)")
fruit = input()
print("> How many?")
count = int(input())
print("> Here you're are!")

# 사전
emojis = {
    "apple": "🍎",
    "banana": "🍌",
    "orange": "🍊",
    "mango": "🥭"
}

emoji = emojis.get(fruit, "💩")

# 함수
def print_emojis(emoji, count):
    # 리스트
    results = []
    for i in range(count):
        results.append(emoji)
    print(results)

print_emojis(emoji, count)

