##Authors who havesubmissions > = threshold

# https://jsonmock.hackerrank.com/api/article_users?page=1


# threshold (int) parameter
# return list of usernames where submission_count >= threshold


import requests
import json


# url = "https://jsonmock.hackerrank.com/api/article_users"
# response = requests.get(url)
# #response.status_code
# #response.text
# res = response.text
# #print(type(res))
# a = json.loads(res)
# print(type(a))
# #print(a['data'])
# l = a['data']
# print(len(l))
# a1 = l[0]
# print(a1)
# print('author = %s' %a1['username'])
# print('submission count is %s' %a1['submission_count'])

def resfun(t):
    userlist = []

    for q in range(1, 3):

        url = "https://jsonmock.hackerrank.com/api/article_users?page=%s"%q

        response = requests.get(url)

        if response.status_code == 200:

            res = response.text

            jres = json.loads(res)

            p = jres['total_pages']

            jresdata = jres['data']

            for x in range(0, len(jresdata)):
                if jresdata[x]['submission_count'] >= t:
                    userlist.append(jresdata[x]['username'])

    return userlist

    # print(jresdata[0])
    # print(jresdata[0]['username'])


t1 = 10
print(resfun(t1))