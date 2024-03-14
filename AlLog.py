import random
import time

def list_creator(x, blank_chance=0.19):
    return [[""] * (x + 2)] + [
        [""]+
        [chr(random.randint(65, 90)) if random.random() > blank_chance else ""
            for _ in range(x)]
        + [""]
        for _ in range(x)]+[[""] * (x + 2)]


def selected_n(x):
    valid = [chr(x) for x in range(65, 91)]
    print("Type a sentence that only uses characters from the UK alphabet:")
    inp = list(input(">>>: ").upper())
    listy = []
    listy.append([""]*(x+2))
    for _ in range(x):
        _listy = [""]
        for _ in range(x):
            try:
                if inp[0] == ' ' or inp[0] not in valid:
                    _listy.append("")
                else:
                    _listy.append(inp[0])
                inp.pop(0)
            except:
                _listy.append("")
        _listy.append("")
        listy.append(_listy)
    listy.append([""]*(x+2))
    
    return listy


def logic_1(arr):
    cnst = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    vowl = ['A', 'E', 'I', 'O', 'U']
    freq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            ajc = "".join(looper(arr, i, j)).strip("").strip('')

            if len(ajc) == 0:
                arr[i+1][j+1] == arr[i][j]
            
            elif len(ajc) == 1:
                arr[i][j] = freq[freq.index(ajc[0]) - (len(freq) - 1)]

            elif len(ajc) in [2, 4]:
                val = 0
                for item in ajc:
                    if item in cnst:
                        val += cnst.index(item)
                    else:
                        val += vowl.index(item)
                val //= len(ajc)
                if val < len(vowl):
                    arr[i][j] = vowl[val]
                else:
                    arr[i][j] = cnst[val]

            if len(ajc) == 3:
                com = float("inf")
                for item in ajc:
                    if freq.index(item) < com:
                        com = freq.index(item)
                arr[i][j] = freq[com]

            elif len(ajc) == 5:
                letters = [0, 0]
                for item in ajc:
                    if item in vowl:
                        letters[0] += 1
                    else:
                        letters[1] += 1
                if letters[0] == 2:
                    vowls = []
                    for item in ajc:
                        if item in vowl:
                            vowls.append(item)
                            if len(vowls) == 2:
                                arr[i][j] = vowl[((vowl.index(vowls[0])) + (vowl.index(vowls[1]))) // 2]
                if letters[1] == 2:
                    cnsts = []
                    for item in ajc:
                        if item in cnst:
                            cnsts.append(item)
                            if len(cnsts) == 2:
                                arr[i][j] = cnst[((cnst.index(cnsts[0])) + (cnst.index(cnsts[1]))) // 2]

            elif len(ajc) == 6:
                com = float("-inf")
                for item in ajc:
                    if freq.index(item) > com:
                        com = freq.index(item)
                arr[i][j] = freq[com]

            elif len(ajc) == 7:
                letters = [0, 0]
                for item in ajc:
                    if item in vowl:
                        letters[0] += 1
                    else:
                        letters[1] += 1
                idx = float("inf")
                if letters[0] > letters[1]:
                    for item in ajc:
                        if item in vowl and freq.index(item) < idx:
                            idx = freq.index(item)
                    arr[i][j] = freq[idx]
                else:
                    for item in ajc:
                        if item in cnst and freq.index(item) < idx:
                            idx = freq.index(item)
                    arr[i][j] = freq[idx]

            elif len(ajc) > 8:
                arr[i][j] = ""

    return arr


def looper(arr, i, j):
    pos = []
    for l in range(-1, 2):
        for n in range(-1, 2):
            y, x = i + l, j + n
            if 0 <= y < len(arr) and 0 <= x < len(arr[0]):
                pos.append(arr[y][x])
    return pos