n = int(input())
Map = {'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9'}
numlist = {}
for _ in range(n):
    phone=input().strip().replace('-', '')
    nphone=[]
    for char in phone:
        if char.isdigit():
            nphone.append(char)
        else:
            nphone.append(Map[char])
    newphone = ''.join(nphone[:3]) + '-' + ''.join(nphone[3:])
    numlist[newphone]=numlist.get(newphone,0)+1
numlistnew=sorted(numlist.items(),key=lambda item:item[0])
output=False
for num in numlistnew:
    if num[1] > 1:
        print(f'{num[0]} {num[1]}')
        output=True
if not output:
    print('No duplicates.')










