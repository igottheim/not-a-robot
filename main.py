import requests
import json
import sys
from groupy.client import Client
from datetime import datetime, timezone
from creds import token, refgroup

client = Client.from_token(token)
groups = client.groups.list()
myuser = client.user.get_me()
chats = client.chats.list_all()
grouplist = list(groups.autopage())



print(grouplist[1].messages)


for x in grouplist:
    if x.name == refgroup:
        # for key, value in x.data.items():
        #     print(f"{key} {value}")
        messageData = x.data['messages']
        memberData = x.data['members']
        break

print(messageData)
print(messageData['preview'])

totalMessages = messageData['count']

for x in memberData:
    print(x['nickname'])

# print(memberData)
# for key, value in group.data.items():
#         print(f"{key} {value}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    headers = {'content-type': 'application/json'}
    # weatherUrl = 'wttr.in/London'
    groupMeURL = 'https://api.groupme.com/v3/bots/post'
    botId = 'c86b261852b074abedfd262d02'


    #
    #
    # weatherAPIResponse = requests.get(weatherUrl)
    # weatherJson = json.loads(weatherAPIResponse)
    # print(weatherJson)

    string = "WOW there have been " + str(totalMessages) + " messages in this group"

    string1 = "I LUV STEAK"
    print(string)

    data = {
        "text": string1, "bot_id": botId
    }



    # comment out below line to run without posting to GroupMe
    # requests.post(groupMeURL, data=json.dumps(data), headers=headers)
