"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

"""

st = "Let's take LeetCode contest"
l = list(st.split())
for i in range(len(l)):
    l[i] = ("".join((reversed(l[i]))))

print(" ".join(l))

