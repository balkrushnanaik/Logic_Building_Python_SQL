num10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_list = []
for i in range(len(num10)-1, -1, -1):
    reversed_list.append(num10[i])
print(f"Reversed list: {reversed_list}")