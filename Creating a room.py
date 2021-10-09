import requests
import json

bearerToken = input("Enter your API access token: ")
bearerToken = "Bearer " + bearerToken
room_title = input("Enter Room name: ")

headers = {"Authorization": bearerToken,
           "Content-Type":"application/json"}

room_parameter = {"title":room_title}
room = requests.post("https://webexapis.com/v1/rooms", headers=headers, json = room_parameter)
print(room.json())
