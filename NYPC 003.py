N = int(input())
new_char = []
for _ in range(N):
    new_char.append(input())

K = int(input())
advanced_char = []
for _ in range(K):
    advanced_char.append(input())

enable_char = []
for character in new_char:
    if character not in advanced_char:
        enable_char.append(character)

print(len(enable_char))
for i in range(len(enable_char)):
    print(enable_char[i])