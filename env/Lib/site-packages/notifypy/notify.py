from .mailer import Mailer
from .app.SmsProvider import SmsProvider

class Notify:
    def __init__(self, email, passwd, provider):
        # mailer
        self.mailer = Mailer(email, passwd, provider = provider)

    def sendNotification(self, to, title, message, notification_type = 'mail', twilio_keys = {}):
        # send notification now
        if notification_type == 'mail':
            chk = self.mailer.sendMsg(to, title, message)
            if chk:
                return True
        elif notification_type == 'sms':
            smsService = SmsProvider(twilio_keys['sid'], twilio_keys['auth'])
            smsService.send(to, title, message, twilio_keys['phone_number'])

