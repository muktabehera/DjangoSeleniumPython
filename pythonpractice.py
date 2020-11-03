def midnum(x):
    l = len(x)
    mid = int((l-1)/2)
    midvalue = x[mid]
    print("value of midnumber is %s" %midvalue)
    return midvalue

def firstnvalue(x,n):
    l = len(x)
    nvalues = x[:n]
    print("the first %s values are %s" %(n,nvalues))
    return nvalues

def listsort(x):
    x.sort()
    print("the sorted list is %r" %x)
    return x

def reverse(x):
    x.reverse()
    print("reversed list is %s" %x)
    return x

def append(x):
    x.append(7)
    print("appneded new list is %s" %x)
    return x

def insert(x,index,value):
    x.insert(index,value)
    print("the list after insert is %s" %x)
    return(x)



if __name__ == '__main__':
    mylist = [3,4,5,6,7,8,9,2,1,0]
    midnum(mylist)
    num = 5
    firstnvalue(mylist,num)
    listsort(mylist)
    reverse(mylist)
    append(mylist)
    myindex = 2
    myvalue = 8
    insert(mylist, myindex, myvalue)

# a = ['a','b','c','v','a','b']
# b = a.copy()
# print(b)

# Find the first non-recurring character in string
# def firstUniqChar(string) -> int:
#     seems = dict()
#     index = len(string)
#     c = ''
#     for i, char in string:
#         if char not in seems:
#             seems.setdefault(char, (i,1))
#         else:
#             seems[char] = (seems[char][0], seems[char][1] + 1)
#
#     for k, value in seems.items():
#         if value[1] == 1 and value[0] < index:
#             index = value[0]
#             c = k
#     return  index if c else -1


# import requests
# import json
# url = "https://hacker-news.firebaseio.com/v0/updates.json"
# response = requests.get(url)
# response.status_code
# response.text
# a = response.text
# res = json.loads(a)
# type(res) *dict
# res['items']

##LIST
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
   # thislist = ["apple", "banana", "cherry"]
   # mylist = list(thislist) *list()
# count()	Returns the number of elements with the specified value
   #thislist.count('s')
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
   # thislist.index('a')
# insert()	Adds an element at the specified position
   # thislist.insert(2, 'test')
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# del

#list to string: ''.join(list)
# string to list with split words: string.split(" ")
# if (string.find(sub_str) == -1): *string.find(sub_str, start, end)
#         print("NO")
#     else:
#         print("YES")
#dictionary: sorted(dict)

