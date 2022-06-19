from imap_tools import MailBox
from pprint import pprint


def getMessages(login, password):
    with MailBox('imap.MAIL_SERVICE.ru').login(login, password, 'INBOX') as mailbox:
        messages = []
        for msg in mailbox.fetch():
            messages.append({'uid': msg.uid, 'subject': msg.subject, 'text': msg.text, 'from': msg.from_, 'to': msg.to, 'date': msg.date})
        
        return messages

