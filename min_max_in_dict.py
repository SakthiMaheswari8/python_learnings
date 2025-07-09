''' This program is to find minimum and maximum value in dictionary'''
marks= {
    "raghul":{
        "mark":80,
        "class":"12"
    },
     "shakthi":{
        "mark":90,
        "class":"12"
    }
}
lis = list(marks[list(marks.keys())].values())
large = lis[0]
small = lis[0]
for i in lis:
    if i > large:
        large = i
    if i < small:
        small = i