''' This program is to find minimum and maximum value in dictionary'''
marks={"liya":95,"sakthi":75,"nisha":80}
lis = list(marks.values())
large = lis[0]
small = lis[0]
for i in lis:
    if i > large:
        large = i
    if i < small:
        small = i

print("Largest mark:", large)
print("Smallest mark:", small)