#! /usr/bin/env python3

# Variables

firstName = "Bryan"
lastName = "Duncanson"
openSlice = open("slicing-file.txt")
sliceLines = openSlice.readlines()
sliceList = []
# for num, line in enumerate(sliceLines):
    # sliceList.append(line.strip("\n"))
    # using enumerate allows you to check with print(sliceList[num])
for line in sliceLines:
    sliceList.append(line.strip("\n"))
# Driver code
print(f"Name: {firstName:<>6}>{lastName:<>10}>") # probably didnt want a formatted name but i wanted to try

ql_1 = sliceList[-3:-4:-1]
ql_2 = sliceList[2:5]
ql_3 = sliceList[-10:-16:-2]
ql_4 = sliceList[10:13]
ql_5 = sliceList[-19:-22:-1]

quoteList = ql_1 + ql_2 + ql_3 + ql_4 + ql_5
quote = " " .join(quoteList)
print(quote)

# to check if it matches change the ' in cant then use this code
# if quote == "Whether you think you can or you think you can't, you are right.":
#    print("you did it")