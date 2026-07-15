# names = ["Bob", "Alice", "Eve", "Charlie", "David", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Mallory", "Niaj", "Olivia", "Peggy", "Sybil", "Trent", "Victor", "Walter"]

# for name in names:
#     if len(name) > 4:
#         name = name.upper()
#         print(name)


    
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,50]
# for n in data:


# finding outlier in a list of integers

q1 = 25/100 * len(data)
print(f"Q1: {q1}")
q3 = 75/100 * len(data)
print(f"Q3: {q3}")

iqr = q3 - q1
print(f"IQR: {iqr}")

lower_fence = q1 - 1.5 * iqr
print(f"Lower fence: {lower_fence}")

higher_fence = q3 + 1.5 * iqr
print(f"Higher fence: {higher_fence}")

