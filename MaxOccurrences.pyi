
######max occurrence solutions:

# mystr = "aabbccsbd"


def moc(mystring):

    """
    1. create a new list with unique char
    2. Now count each char from new list in original list and see which has max count
    :param mystring:
    :return:

    newlist = ['a', 'b', 'c']
    countlist = [1,3,4]
    K (max of countlist) = 4

    option 1:
    -> find idx on K in countlist (i.e. 2)
    -> find value in newlist with same idx (i.e. 'c')

    option 2:

    -> zip newlist (as keys) and countlist (as values)
    -> find the key where value is max_count



    """

    mylist = list(mystring)
    newlist = []
    countlist = []

    l = print(len(mystring))


    # 1. create a new list with unique char

    for x in mylist:
        if x not in newlist:
            newlist.append(x)
    print("newlist = %s" %newlist)


    # 2. Now count each char from new list in original list and see which has max count

    for y in newlist:

        # print('for char %s in string the count sn %s' %(y, mylist.count(y) ))
        countlist.append(mylist.count(y))
    print("countlist = %s"%countlist)

    max_count = max(countlist)
    print("max value K = %s" % max_count )

    ################### option 1

    # get the char from newlist that matches k

    idxofKinCountList  = countlist.index(max_count)
    print("idxofKinCountList = %s" %idxofKinCountList)

    print(newlist[idxofKinCountList])

    #################### option 2

    zipped_dict = dict(zip(newlist, countlist))

    print(zipped_dict)

    for key,val in zipped_dict.items():
        if val == max_count:
            print(key)

if __name__ == '__main__':
    s = 'aaaabbcc'
    moc(s)