x = [0,1,2,3,4,5]
y = ["a","b","c","d","e","f"]

"""lst = []
lst.append(x)
lst.append(y)
print(len(lst))

print(len(lst[0]))
"""

for liste1, liste2 in zip(x,y):
    #print(f"liste1 = {liste1}, liste2 = {liste2}")
    print(f"({liste1},{liste2})")
