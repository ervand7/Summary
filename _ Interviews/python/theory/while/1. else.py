i = 0
while i < 10:
    print(i)
    i += 1

    if i == 7:
        break
# the else block will only work if the cycle finishes normally, without breaking
else:
    print("while ended normally")
