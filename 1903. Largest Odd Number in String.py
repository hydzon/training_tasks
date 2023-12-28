"""
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

"""

num = "80230416803720094"
i_num = []

for i in range(len(num)):
    if int(num[i]) % 2 != 0:
        i_num.append(int(num[i]))

i_num.sort(reverse=True)
s = 0
for i in range(len(i_num), 1):
    s += 10**5 * i_num[i]


print()
