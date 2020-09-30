## say goodbye
* start
  - utter_welcome
* goodbye
  - utter_goodbye

## say hi
* start
  - utter_welcome
* greet
  - utter_greet 


## happychitchat
* start
  - utter_welcome
* greet
  - utter_greet  
* faq
  - respond_faq
* faq  
  - respond_faq
  - utter_faq_guide
* goodbye
  - utter_goodbye


## happychitchat
* start
  - utter_welcome
* faq
  - respond_faq
* faq  
  - respond_faq
  - utter_faq_guide  
* goodbye
  - utter_goodbye

## happy_pickup_guest_form
* start
  - utter_welcome
* request_pickup_car
    - guest_pickup_form
    - form{"name": "guest_pickup_form"}
    - form{"name": null}
    - utter_car_pick_guide
* faq
    - respond_faq
* faq  
    - respond_faq
    - utter_faq_guide


## interactive_story_2
* start
    - utter_welcome
* request_pickup_car
    - guest_pickup_form
    - form{"name": "guest_pickup_form"}
    - slot{"requested_slot": "PERSON"}
* form: inform{"PERSON": "Vansh Kapil"}
    - slot{"PERSON": "Vansh Kapil"}
    - slot{"requested_slot": "guest_phone_number"}
* form: inform{"guest_phone_number": "9876543211"}
    - slot{"guest_phone_number": "9876543211"}
    - form: guest_pickup_form
    - slot{"guest_phone_number": "9876543211"}
    - slot{"requested_slot": "pickup_location"}
* form: inform{"pickup_location": "airport"}
    - slot{"pickup_location": "airport"}
    - form: guest_pickup_form
    - slot{"pickup_location": "airport"}
    - slot{"requested_slot": "pickup_time"}
* form: inform{"pickup_time": "2PM"}
    - slot{"pickup_time": "2PM"}
    - form: guest_pickup_form
    - slot{"pickup_time": "2PM"}
    - slot{"requested_slot": "car_type"}
* form: inform{"car_type": "4 seater"}
    - slot{"car_type": "4 seater"}
    - form: guest_pickup_form
    - slot{"car_type": "4 seater"}    
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_car_pick_guide
* faq
    - respond_faq
* faq  
    - respond_faq
    - utter_faq_guide

## interactive_story_2
* start
    - utter_welcome
* request_pickup_car
    - guest_pickup_form
    - form{"name": "guest_pickup_form"}
    - slot{"requested_slot": "PERSON"}
* form: inform{"PERSON": "Robin Singh"}
    - slot{"PERSON": "Robin Singh"}
    - slot{"requested_slot": "guest_phone_number"}
* form: inform{"guest_phone_number": "9876543211"}
    - slot{"guest_phone_number": "9876543211"}
    - form: guest_pickup_form
    - slot{"guest_phone_number": "9876543211"}
    - slot{"requested_slot": "pickup_location"}
* form: inform{"pickup_location": "airport"}
    - slot{"pickup_location": "airport"}
    - form: guest_pickup_form
    - slot{"pickup_location": "airport"}
    - slot{"requested_slot": "pickup_time"}
* form: inform{"pickup_time": "5 AM"}
    - slot{"pickup_time": "5 AM"}
    - form: guest_pickup_form
    - slot{"pickup_time": "5 AM"}
    - slot{"requested_slot": "car_type"}
* form: inform{"car_type": "6 seater"}
    - slot{"car_type": "6 seater"}
    - form: guest_pickup_form
    - slot{"car_type": "6 seater"}    
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_car_pick_guide
* faq
    - respond_faq
* faq  
    - respond_faq
    - utter_faq_guide


## New Story
* start
    - utter_welcome
* request_pickup_car
    - guest_pickup_form
    - form{"name":"guest_pickup_form"}
    - slot{"requested_slot":"PERSON"}
    - slot{"PERSON":"robin smith"}
* inform{"PERSON":"robin smith"}
    - guest_pickup_form
    - slot{"PERSON":"robin smith"}
    - slot{"guest_phone_number":"9876543211"}
* inform{"guest_phone_number":"9876543211"}
    - guest_pickup_form
    - slot{"guest_phone_number":"9876543211"}
    - slot{"pickup_location":"airport"}
* inform{"pickup_location":"airport"}
    - guest_pickup_form
    - slot{"pickup_location":"airport"}
    - slot{"pickup_time":"2pm"}
* inform{"pickup_time":"2pm"}
    - guest_pickup_form
    - slot{"pickup_time":"2pm"}
    - slot{"car_type":"4 seater"}
* inform{"car_type":"4 seater"}
    - guest_pickup_form
    - form{"name":null}
    - slot{"car_type":"4 seater"}
    - utter_car_pick_guide
* faq
    - respond_faq
* faq  
    - respond_faq
    - utter_faq_guide  


## New Story
* start
    - utter_welcome
* request_pickup_car
    - guest_pickup_form
    - form{"name":"guest_pickup_form"}
    - slot{"requested_slot":"PERSON"}
    - slot{"PERSON":"Bob willis"}
* inform{"PERSON":"Bob willis"}
    - guest_pickup_form
    - slot{"PERSON":["Bob","Bob willis"]}
    - slot{"guest_phone_number":"9876543211"}
* inform{"guest_phone_number":"9876543211"}
    - guest_pickup_form
    - slot{"guest_phone_number":"9876543211"}
    - slot{"pickup_location":"25th avenue"}
* inform{"pickup_location":"25th avenue"}
    - guest_pickup_form
    - slot{"pickup_location":"25th avenue park"}
    - slot{"pickup_time":"1 pm"}
* inform{"pickup_time":"1 pm"}
    - guest_pickup_form
    - slot{"pickup_time":"1 pm"}
    - slot{"car_type":"4 seater"}
* inform{"car_type":"4 seater"}
    - guest_pickup_form
    - form{"name":null}
    - slot{"car_type":"4 seater"}
    - utter_car_pick_guide
* faq
    - respond_faq
* faq  
    - respond_faq
    - utter_faq_guide

## New Story
* start
    - utter_welcome
    - slot{"pickup_location":"airport"}
* request_pickup_car{"pickup_location":"airport","pickup_time":"12 pm"}
    - slot{"pickup_location":"airport"}
    - slot{"pickup_time":"12 pm"}
    - guest_pickup_form
    - form{"name":"guest_pickup_form"}
    - slot{"pickup_location":"airport"}
    - slot{"PERSON":"Ben Stokes"}
* inform{"PERSON":"Ben Stokes"}
    - guest_pickup_form
    - slot{"guest_phone_number":"8765432112"}
* inform{"guest_phone_number":"8765432112"}
    - guest_pickup_form
    - slot{"guest_phone_number":"8765432112"}
    - slot{"car_type":"6 seater"}
* inform{"car_type":"6 seater"}
    - guest_pickup_form
    - form{"name":null}
    - slot{"car_type":"6 seater"}
    - utter_car_pick_guide
* faq
    - respond_faq
* faq  
    - respond_faq
    - utter_faq_guide

## New Story
* start
    - utter_welcome
    - slot{"pickup_location":"airport"}
* request_pickup_car{"pickup_location":"airport"}
    - guest_pickup_form
    - form{"name":"guest_pickup_form"}
    - slot{"pickup_location":"airport"}
    - slot{"PERSON":"Gabbar"}
* inform{"PERSON":"Gabbar"}
    - guest_pickup_form
    - slot{"PERSON":["singh","Gabbar"]}
    - slot{"guest_phone_number":"9560822220"}
* inform{"guest_phone_number":"9560822220"}
    - guest_pickup_form
    - slot{"guest_phone_number":"9560822220"}
* inform
    - guest_pickup_form
    - slot{"pickup_time":"11am"}
    - slot{"car_type":"6 seater"}
* inform{"car_type":"6 seater"}
    - guest_pickup_form
    - form{"name":null}
    - slot{"car_type":"6 seater"}
    - utter_car_pick_guide
* faq
    - respond_faq
* faq  
    - respond_faq
    - utter_faq_guide

## New Story
* start
    - utter_welcome
    - slot{"pickup_location":"airport"}
* request_pickup_car{"pickup_location":"airport"}
    - slot{"pickup_location":"airport"}
    - guest_pickup_form
    - form{"name":"guest_pickup_form"}
    - slot{"pickup_location":"airport"}
    - slot{"PERSON":"David Saker"}
* affirm{"PERSON":"David Saker"}
    - slot{"PERSON":"David Saker"}
    - guest_pickup_form
    - slot{"PERSON":"David Saker"}
    - slot{"guest_phone_number":"9876543211"}
* inform{"guest_phone_number":"9876543211"}
    - slot{"guest_phone_number":"9876543211"}
    - guest_pickup_form
    - slot{"guest_phone_number":"9876543211"}
* faq
    - respond_faq
    - guest_pickup_form
    - slot{"requested_slot":"pickup_time"}
* inform
    - guest_pickup_form
    - slot{"pickup_time":"11am"}
    - slot{"car_type":"4 seater"}
* inform{"car_type":"4 seater"}
    - guest_pickup_form
    - form{"name":null}
    - slot{"car_type":"4 seater"}
    - utter_car_pick_guide

## New Story
* start
    - utter_welcome
    - slot{"pickup_location":"Bus Station"}
* request_pickup_car{"pickup_location":"Bus Station"}
    - slot{"pickup_location":"Bus Station"}
    - guest_pickup_form
    - form{"name":"guest_pickup_form"}
    - slot{"pickup_location":"Bus Station"}
    - slot{"PERSON":"David Saker"}
* affirm{"PERSON":"David Saker"}
    - slot{"PERSON":"David Saker"}
    - guest_pickup_form
    - slot{"PERSON":"David Saker"}
    - slot{"guest_phone_number":"9876543211"}
* inform{"guest_phone_number":"9876543211"}
    - slot{"guest_phone_number":"9876543211"}
    - guest_pickup_form
    - slot{"guest_phone_number":"9876543211"}
* faq
    - respond_faq
    - guest_pickup_form
    - slot{"requested_slot":"pickup_time"}
* inform
    - guest_pickup_form
    - slot{"pickup_time":"11am"}
    - slot{"car_type":"4 seater"}
* inform{"car_type":"4 seater"}
    - guest_pickup_form
    - form{"name":null}
    - slot{"car_type":"4 seater"}
    - utter_car_pick_guide

## New Story
* start
    - utter_welcome
    - slot{"pickup_location":"Airport"}
* request_pickup_car{"pickup_location":"Airport"}
    - slot{"pickup_location":"Airport"}
    - guest_pickup_form
    - form{"name":"guest_pickup_form"}
    - slot{"pickup_location":"Airport"}
* faq
    - guest_pickup_form
    - slot{"PERSON":"vansh"}
    - slot{"guest_phone_number":"9876543211"}
* inform{"guest_phone_number":"9876543211"}
    - slot{"guest_phone_number":"9876543211"}
    - guest_pickup_form
    - slot{"guest_phone_number":"9876543211"}
* faq
    - respond_faq
    - guest_pickup_form
    - slot{"requested_slot":"pickup_time"}
* inform{"pickup_time":"11am"}
    - guest_pickup_form
    - slot{"car_type":"4 seater"}
* inform{"car_type":"4 seater"}
    - guest_pickup_form
    - form{"name":null}
    - slot{"car_type":"4 seater"}
    - utter_car_pick_guide
* faq
    - respond_faq


## interactive_story_1
* query_knowledge_base
  - action_query_knowledge_base

## interactive_story_1
* query_knowledge_base
  - slot{"object_type":"services"} 
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"description","services": "Golf"}  
  - slot{"services": "Golf"}
  - slot{"attribute": "description"}
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"price","services": "Golf"}  
  - action_query_knowledge_base

## interactive_story_1
* query_knowledge_base
  - slot{"object_type":"services"} 
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"description","services": "Golf"}  
  - slot{"services": "Golf"}
  - slot{"attribute": "description"}
  - action_query_knowledge_base
* faq
  - respond_faq  
* query_knowledge_base{"attribute":"price","services": "Golf"}  
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"book","services": "Golf"}  
  - action_query_knowledge_base  
  - golf_book_form
  - form{"name": "golf_book_form"}
  - form{"name": null} 
  - feedback_form
  - form{"name":"feedback_form"}
  - form{"name": null}

## interactive_story_1
* query_knowledge_base
  - slot{"object_type":"services"} 
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"description","services": "Golf"}  
  - slot{"services": "Golf"}
  - slot{"attribute": "description"}
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"price","services": "Golf"}  
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"book","mention":"it"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"object_type":"services"}
    - golf_book_form
    - form{"name":"golf_book_form"}
    - form{"name": null} 
    - feedback_form
    - form{"name":"feedback_form"}
    - form{"name": null}


## New Story
* start
    - utter_welcome
    - slot{"object_type":"services"}
* query_knowledge_base{"object_type":"services"}
    - slot{"object_type":"services"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"attribute":"description"}
* query_knowledge_base{"attribute":"description","services":"Golf"}
    - slot{"attribute":"description"}
    - slot{"services":"Golf"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"attribute":"book"}
* query_knowledge_base{"attribute":"book","mention":"it"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - golf_book_form
    - form{"name":"golf_book_form"}
    - form{"name": null} 
    - feedback_form
    - form{"name":"feedback_form"}
    - form{"name": null}


## interactive_story_1
* query_knowledge_base
  - slot{"object_type":"services"} 
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"description","services": "Spa Station"}  
  - slot{"services": "Spa Station"}
  - slot{"attribute": "description"}
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"price","services": "Spa Station"}  
  - action_query_knowledge_base

## interactive_story_1
* query_knowledge_base
  - slot{"object_type":"services"} 
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"description","services": "Spa Station"}  
  - slot{"services": "Spa Station"}
  - slot{"attribute": "description"}
  - action_query_knowledge_base
* faq
  - respond_faq  
* query_knowledge_base{"attribute":"price","services": "Spa Station"}  
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"book","mention":"it"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"object_type":"services"}
    - golf_book_form
    - form{"name":"golf_book_form"}
    - form{"name": null} 
    - feedback_form
    - form{"name":"feedback_form"}
    - form{"name": null}

## interactive_story_1
* query_knowledge_base
  - slot{"object_type":"services"} 
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"description","services": "Swimming pool"}  
  - slot{"services": "Swimming pool"}
  - slot{"attribute": "description"}
  - action_query_knowledge_base
* faq
  - respond_faq  
* query_knowledge_base{"attribute":"price","services": "Swimming pool"}  
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"book","mention":"it"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"object_type":"services"}
    - golf_book_form
    - form{"name":"golf_book_form"}
    - form{"name": null} 
    - feedback_form
    - form{"name":"feedback_form"}
    - form{"name": null}

## interactive_story_1
* query_knowledge_base
  - slot{"object_type":"services"} 
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"description","services": "Swimming pool"}  
  - slot{"services": "Swimming pool"}
  - slot{"attribute": "description"}
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"price","services": "Swimming pool"}  
  - action_query_knowledge_base
* query_knowledge_base{"attribute":"book","mention":"it"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"object_type":"services"}
    - golf_book_form
    - form{"name":"golf_book_form"}
    - form{"name": null} 
    - feedback_form
    - form{"name":"feedback_form"}
    - form{"name": null}