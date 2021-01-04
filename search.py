# unordered list
items = [2,20,8,19,56,23,87,41,49,53]

def find_item(item, itemList):
    for i in range(0, len(items)):
        if item == itemList[i]:
            return i
        
    return None

# print(find_item(87, items))
# print(find_item(250, items))

# ordered list
items2 = [6,8,19,20,23,41,49,53,56,87]

def binarysearch(item, itemList):
    listsize = len(itemList) - 1

    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        midPt = (lowerIdx + upperIdx) // 2
        if itemList[midPt] == item:
            return midPt

        if item > itemList[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if listsize > upperIdx:
        return None

# print(binarysearch(23, items2))
# print(binarysearch(87, items2))
# print(binarysearch(250, items2))

# check sorted list

items3 = [6,8,19,20,23,41,49,53,56,87]
items4 = [6,20,8,19,56,23,87,41,49,53]

def is_sorted(itemlist):
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))
    
print(is_sorted(items3))
print(is_sorted(items4))