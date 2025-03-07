# put your python code here

buf = [int(x) for x in input().split()]
l1 = sorted([x - 1 for x in buf[:len(buf) // 2]], reverse=False)
l2 = sorted(buf[len(buf) // 2:], reverse=False)
for i in range(len(buf) // 2):
    if l1[i] <= l2[i]:
        print("НЕТ")
        break
else:
    print("ДА")