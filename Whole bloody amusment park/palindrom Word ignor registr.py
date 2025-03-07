# put your python code here
l = [ch.lower() for ch in input()]
for i in range(len(l) // 2):
    if l[i] != l[-(i+1)]:
        print("НЕТ")
        break
else:
    print("ДА")


