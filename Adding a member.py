import requests
import json

bearerToken = input("Enter your API access token: ")
bearerToken = "Bearer " + bearerToken
roomID = input("Enter Room ID: ")
add_counter = int(input("How many members do you want to add? "))

while add_counter !=0:               
    member_email = input("Enter member's email: ")
    headers = {"Authorization": bearerToken,
               "Content-Type":"application/json"}

    member_parameter = {"roomId":roomID, "personEmail":member_email}
    message_parameter = {"roomId":roomID, "markdown":"I LOVE API"}
                  
    member = requests.post("https://webexapis.com/v1/memberships", headers=headers, json = member_parameter)
    message = requests.post("https://webexapis.com/v1/messages", headers=headers, json = message_parameter)
    print(member.json())
    print(message.json())
    add_counter -= 1
