class Notification:

  def send(self):
    print("Sending notification")

class EmailNotification(Notification):

  def send(self):
    print("Sending notification via email")    


class SMSNotification(Notification):

  def send(self):
    print("Sending notification via SMS")    


class PushNotification(Notification):

  def send(self):
    print("Sending notification via  Push Notification")            



notifications=[Notification(),EmailNotification(),SMSNotification(),PushNotification()]

for notification in notifications:
  notification.send()