from accounts import accounts
from getMessages import getMessages
import time
from dsHook import hookSend

oldMessages = []

for account in accounts:
    oldMessages.append({'account': account['login'], 'uid': getMessages(account['login'], account['password'])[-1]['uid']})
    
def checkMessages():
    for i in range(len(accounts)):
        login = accounts[i]['login']
        password = accounts[i]['password']
        newMessage = getMessages(login, password)[-1]
        if newMessage['uid'] > oldMessages[i]['uid']:
            oldMessages[i]['uid'] = newMessage['uid']
            hookSend(newMessage['subject'], newMessage['text'], newMessage['from'], str(newMessage['to'][0]), str(newMessage['date']))
            

while True:
    checkMessages()
    time.sleep(30)