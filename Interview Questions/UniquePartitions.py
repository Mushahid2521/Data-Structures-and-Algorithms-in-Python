from collections import deque

"""
Split S into S1 and S2 where two part has same characters
"""

S = "ababa"

count = 0
S= list(S)
a = set()
b = deque(S)
c = set(S)

for i in range(len(S)):
    pop = b.popleft()
    a.add(pop)
    if pop not in b:
      c.discard(pop)
    if len(a) == len(c):
        print(a,  c)
        count = count+1

print(count)