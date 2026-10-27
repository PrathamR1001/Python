from main import word,letters,num

def encode():
    code = []

    for i in word:
        for x,letter in enumerate(letters):
            if i == letter:
                # print(letters[x + num], num, x, i)
                # print(type(letters[x + num]))
                code.append(letters[x + num])
                new_code = "".join(code)
    print(f"Your new code:\n{new_code}")