from typing import Any, Text, Dict, List
import json
from rasa_sdk.events import AllSlotsReset
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.forms import FormAction
import csv
import random
import pandas
import re

INTENT_DESCRIPTION_MAPPING_PATH = "actions/intent_mapping.csv"

class GuestPickupForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "guest_pickup_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return [
            "PERSON",
            "guest_phone_number","pickup_location","pickup_time","car_type"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "PERSON": [self.from_text()],
            # "PERSON": self.from_entity(entity="PERSON",intent=["inform"]),
                "guest_phone_number": self.from_entity(entity="guest_phone_number", intent=["inform"]),
                "pickup_location": [self.from_text()],
            "pickup_time": [self.from_text()],
                # "pickup_time": self.from_entity(entity="pickup_time", intent=["inform"]),
                "car_type": self.from_entity(entity="car_type", intent=["inform"]),
                }

    def car_type_db(self) -> List[Text]:
        """Database of supported car_types"""

        return [
            "4 seater",
            "6 seater"
        ]

    def validate_car_type(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate car type value."""

        if value.lower() in self.car_type_db():
            # validation succeeded, set the value of the "car_type" slot to value
            return {"car_type": value}
        else:
            dispatcher.utter_message(template="utter_wrong_car_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"car_type": None}



    def validate_guest_phone_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate phone value."""

        # if re.match(r"^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$",value):
        if re.match(r"^[6-9]\d{9}$", value):
            return {"guest_phone_number": value}
        else:
            dispatcher.utter_message(template="utter_wrong_phone_number")
            return {"guest_phone_number": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        loc = tracker.get_slot('pickup_location')
        time = tracker.get_slot('pickup_time')
        car = tracker.get_slot('car_type')
        txt = "Done! Driver will reach "+loc +" before " + time + ". Your chosen car type is "+car+". Please keep your phone active."
        # utter submit template
        dispatcher.utter_message(text=txt)
        return []

class GolfBookingForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "golf_book_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return [
            "PERSON","time_slot",
            "guest_number"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "PERSON": [self.from_text()],
            # "PERSON": self.from_entity(entity="PERSON",intent=["inform"]),
            "time_slot": self.from_entity(entity="time_slot",intent=["inform"]),
                "guest_number": [self.from_text()]
                }

    def timeslot_db(self) -> List[Text]:
        """Database of supported car_types"""

        return [
            "Early Morning",
            "Late Morning",
            "Afternoon"
        ]

    def validate_car_type(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate car type value."""

        if value.lower() in self.timeslot_db():
            # validation succeeded, set the value of the "car_type" slot to value
            return {"time_slot": value}
        else:
            dispatcher.utter_message(template="utter_wrong_time_slot")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"time_slot": None}



    def validate_guest_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate phone value."""

        # if re.match(r"^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$",value):
        if re.match(r"^[1-9]$", value):
            return {"guest_number": value}
        else:
            dispatcher.utter_message(template="utter_wrong_guest_number")
            return {"guest_number": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        person = tracker.get_slot('PERSON')
        time = tracker.get_slot('time_slot')
        guest_num = tracker.get_slot('guest_number')
        service = tracker.get_slot('services')
        txt = " Your " + time + " session of "+ service+ " is reserved for " + guest_num + " guests, in the name of " + person + ". Please talk to our front desk for any further queries. "
        dispatcher.utter_message(text=txt)
        dispatcher.utter_message(template="utter_finish_guide")
        return []

class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv(INTENT_DESCRIPTION_MAPPING_PATH)
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) :

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]

        # for the intent name used to retrieve the button title, we either use
        # the name of the name of the "main" intent, or if it's an intent that triggers
        # the response selector, we use the full retrieval intent name so that we
        # can distinguish between the different sub intents
        first_intent_names = [
            intent.get("name", "")
            if intent.get("name", "") not in ["out_of_scope", "faq"]
            else tracker.latest_message.get("response_selector")
            .get(intent.get("name", ""))
            .get("full_retrieval_intent")
            for intent in intent_ranking
        ]

        message_title = (
            "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            button_title = self.get_button_title(intent, entities)
            if "/" in intent:
                # here we use the button title as the payload as well, because you
                # can't force a response selector sub intent, so we need NLU to parse
                # that correctly
                buttons.append({"title": button_title, "payload": button_title})
            else:
                buttons.append(
                    {"title": button_title, "payload": f"/{intent}{entities_json}"}
                )

        buttons.append({"title": "Something else", "payload": "/out_of_scope"})

        dispatcher.utter_message(text=message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (self.intent_mappings.entities == entities.keys()) & (
            default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("./actions/data.json")

        knowledge_base.set_representation_function_of_object(
            "services", lambda obj: obj["name"] + " \n\n " + obj["description"]

        )

        super().__init__(knowledge_base)

    def utter_attribute_value(self, dispatcher, object_name, attribute_name, attribute_value):

        # take attribute value and extract image url embedded in {}
        attribute_value_string = attribute_value.split('<{')
        attribute_text = attribute_value_string[0]
        try:
            attribute_image = attribute_value_string[1].split('}>')[0]
        except:
            attribute_image = None

        # this dictionary creates custom responses for different attributes
        ans_repo = { "price": [attribute_text,attribute_image],
                     "timings": [attribute_text,attribute_image],
                     "description": [attribute_text,attribute_image],
                     "book":[attribute_text,attribute_image]
                    }
        if attribute_value:

            img = ans_repo[attribute_name][1]
            msg = ans_repo[attribute_name][0]

            dispatcher.utter_message(text=msg,image=img) #it won't send images if text attribute is not included
        else:
            dispatcher.utter_message(
                "Did not find anything related to it for '{}'.".format(
                    object_name
                )
            )
        return []

    def utter_objects(self, dispatcher, object_type, objects):
        # type: (CollectingDispatcher, Text, List[Dict[Text, Any]]) -> None
        """
        Utters a response to the user that lists all found objects.
        Args:
            dispatcher: the dispatcher
            object_type: the object type
            objects: the list of objects
        """
        if object_type == "services":
            if objects:

                button_list = []
                for obj in objects:
                    d = {'title': obj["name"],
                         'payload': '/query_knowledge_base{"attribute":"description","services":"' + obj["name"] + '"}'}
                    button_list.append(d)
                    txt = "Here is the list of "+ object_type+' we have'
                dispatcher.utter_message(text=txt, buttons=button_list)
            else:
                dispatcher.utter_message(
                    "I could not find any services."
                )

class FeedbackForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "feedback_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["use_conf","user_email"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
                "use_conf": [self.from_text()],
            "user_email": self.from_entity(entity="user_email", intent=["inform"])
                }

    def validate_user_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate email value."""

        if re.match(r"[^@]+@[^@]+\.[^@]+",value):
            return {"user_email": value}
        else:
            dispatcher.utter_message(template="utter_wrong_visitor_email")
            return {"user_email": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        dispatcher.utter_message(template="utter_thanks")
        return []


# class SPAbook(FormAction):
#
#     def name(self) -> Text:
#         """Unique identifier of the form"""
#
#         return "spa_book_form"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#
#         return [
#             "guest_num",
#             "PERSON",
#             "guest_phone_number","spa_date","spa_time","treatment_type","spa_session","pref_therapist"]
#
#     def slot_mappings(self) -> Dict[Text, Any]:
#         return {
#             "guest_num": [self.from_text()],
#             "PERSON": [self.from_text()],
#             # "PERSON": self.from_entity(entity="PERSON",intent=["inform"]),
#                 "guest_phone_number": self.from_entity(entity="guest_phone_number", intent=["inform"]),
#                 "spa_date": [self.from_text()],
#             "spa_time": [self.from_text()],
#                 # "pickup_time": self.from_entity(entity="pickup_time", intent=["inform"]),
#                 "treatment_type": self.from_entity(entity="treatment_type", intent=["inform"]),
#             "spa_session": self.from_entity(entity="spa_session", intent=["inform"]),
#             "pref_therapist": self.from_entity(entity="pref_therapist", intent=["inform"])
#                 }
#
#     def validate_guest_phone_number(
#         self,
#         value: Text,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         """Validate phone value."""
#
#         # if re.match(r"^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$",value):
#         if re.match(r"^[6-9]\d{9}$", value):
#             return {"guest_phone_number": value}
#         else:
#             dispatcher.utter_message(template="utter_wrong_phone_number")
#             return {"guest_phone_number": None}
#
#     def submit(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#             after all required slots are filled"""
#
#         spapricematrix = {
#             " Bamboo Massage - Relaxing 50 minutes":"$165",
#             " Bamboo Massage - Deep Tissue 80 minutes": "$220",
#             " Herbal Compression Massage 80 minutes": "$210",
#             " Maternity/Prenatal Massage 50 minutes": "$135",
#             " Salt Serenity - Relaxing 50 minutes": "$165",
#             " Salt Serenity - Deep Tissue 50 minutes": "$220",
#
#
#
#         }
#
#
#         guestNum = tracker.get_slot('guest_num')
#         date = tracker.get_slot('spa_date')
#         time = tracker.get_slot('spa_time')
#         treatment = tracker.get_slot('treatment_type')
#         spasession = tracker.get_slot('spa_session')
#         spaprice = spapricematrix[treatment+spasession]
#         txt = "Done! I have booked a " + time + " "+treatment+" slot for " + guestNum + " guests on "+date + ". Please visit our spa center on the lower ground floor."
#         # utter submit template
#         dispatcher.utter_message(text=txt)
#         return []

