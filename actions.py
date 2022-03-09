from typing import Dict, Text, List

from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
import smtplib

class ActionHelloworld(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker, 
        domain: Dict
    ) -> List[EventType]:

        sendmail(
        toaddr=tracker.get_slot("email_id"),
        subject=tracker.get_slot("subject"),
        msg=tracker.get_slot('msg'),
        )
        
        dispatcher.utter_message(text=f"Thank you for your information||||||||... Mail sent successfully")
        return []

def sendmail(toaddr,subject,msg):
    my_email="pythontest9080@gmail.com"
    password="samraj9080"
    connection=smtplib.SMTP('smtp.gmail.com',587)
    connection.starttls()
    connection.login(my_email,password)
    connection.sendmail(from_addr=my_email,to_addrs=toaddr,msg=f"Subject:{subject} \n\n {msg}")
    connection.close()