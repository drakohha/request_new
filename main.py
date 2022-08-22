import requests


website = "http://jsonplaceholder.typicode.com/posts/1"
print(requests.get(website).json())

response = requests.put(website , data={
    "id": 1,
    "userId": 12,
    "title": "my new post",
    "body" : "body for my post",
    "photo" : {"1.jpg", "2.jpg"}
})

print(response.json())











# headers={
#     "User-Agent": "IT_overno",
# }
#
#
# response= requests.post("http://httpbin.org/post",
#                         headers=headers ,
#                         params={'a':'b'},
#                         json={"username":"supersecret"}
#                         )
#

# if response.status_code ==200:
# #     print('ok')
#
#
#
# print(response.text)