from collections import OrderedDict
key = input().replace('j', 'i')
keys = list(OrderedDict.fromkeys(key))

#用chr(ord('a') + i) for i in range(26)打字母表并跳过j
alphabet = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) != 'j']
for letter in alphabet:
        if letter not in keys:
            keys.append(letter)

matrix = []
for i in range(5):
    matrix.append(keys[i * 5:(i + 1) * 5])

pos = {}  #用字典找位置，用空间换时间
for i in range(5):
    for j in range(5):
        pos[matrix[i][j]] = (i, j)


def encrypt(plaintext):
    text = []
    for ch in plaintext:
        if ch == 'j':
            text.append('i')
        else:
            text.append(ch)

    pairs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            pairs.append([text[i], 'x' if text[i] != 'x' else 'q'])
            i += 1
        elif text[i] == text[i + 1]:
            pairs.append([text[i], 'x' if text[i] != 'x' else 'q'])
            i += 1
        else:
            pairs.append([text[i], text[i + 1]])
            i += 2

    cipher = []
    for a, b in pairs:
        row1, col1 = pos[a]
        row2, col2 = pos[b]
        if row1 == row2:
            cipher.append(matrix[row1][(col1 + 1) % 5])
            cipher.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            cipher.append(matrix[(row1 + 1) % 5][col1])
            cipher.append(matrix[(row2 + 1) % 5][col2])
        else:
            cipher.append(matrix[row1][col2])
            cipher.append(matrix[row2][col1])

    return ''.join(cipher)


n = int(input())
for _ in range(n):
    plaintext = input()
    print(encrypt(plaintext))

