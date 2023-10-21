text = input("Input: ")
shift = int(input("Shift: "))

if shift >= 26:
    shift = shift - (26*(shift // 26))

if shift == 0:
    print(text)
else:
    for letter in text:
        if letter == " ":
            output = 32
        else:
            output = ord(letter) + shift

        if 65 <= ord(letter) <= 90:
            if output > 90:
                new_shift = output - 90
                output = 64 + new_shift
        elif 97 <= ord(letter) <= 122:
            if output > 122:
                new_shift = output - 122
                output = 96 + new_shift
        print(chr(output), end="")
