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

## New Story
* start
    - utter_welcome
* start
    - utter_welcome
* greet
    - utter_greet
* request_pickup_car
    - guest_pickup_form
    - form{"name":"guest_pickup_form"}
    - slot{"requested_slot":"PERSON"}
* inform
    - guest_pickup_form
    - slot{"PERSON":"vansh"}
    - slot{"requested_slot":"guest_phone_number"}
* inform{"phone-number":"9874563211","number":9874563211,"guest_phone_number":"9874563211"}
    - slot{"guest_phone_number":"9874563211"}
    - slot{"guest_phone_number":"9874563211"}
    - guest_pickup_form
    - slot{"guest_phone_number":"9874563211"}
    - slot{"requested_slot":"pickup_location"}
* inform{"pickup_location":"airport"}
    - slot{"pickup_location":"airport"}
    - slot{"pickup_location":"airport"}
    - guest_pickup_form
    - slot{"pickup_location":"airport"}
    - slot{"requested_slot":"pickup_time"}
* inform{"time":"2020-10-01T13:00:00.000-07:00","PERSON":"tomorrow","pickup_time":"1 pm"}
    - slot{"PERSON":"tomorrow"}
    - slot{"pickup_time":"1 pm"}
    - slot{"PERSON":"tomorrow"}
    - slot{"pickup_time":"1 pm"}
    - guest_pickup_form
    - slot{"pickup_time":"tomorrow 1 pm"}
    - slot{"requested_slot":"car_type"}
* inform{"car_type":"4 seater"}
    - slot{"car_type":"4 seater"}
    - slot{"car_type":"4 seater"}
    - guest_pickup_form
    - slot{"car_type":"4 seater"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_car_pick_guide
* faq
    - respond_faq
* faq
    - respond_faq
    - utter_faq_guide
* query_knowledge_base{"object_type":"services"}
    - slot{"object_type":"services"}
    - slot{"object_type":"services"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"mention":null}
    - slot{"attribute":null}
    - slot{"knowledge_base_last_object":null}
    - slot{"knowledge_base_last_object_type":"services"}
    - slot{"knowledge_base_listed_objects":[2,1,0]}
* query_knowledge_base{"attribute":"description","services":"Golf"}
    - slot{"attribute":"description"}
    - slot{"services":"Golf"}
    - slot{"attribute":"description"}
    - slot{"services":"Golf"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"attribute":null}
    - slot{"mention":null}
    - slot{"knowledge_base_last_object":1}
    - slot{"knowledge_base_last_object_type":"services"}
* query_knowledge_base{"attribute":"timings"}
    - slot{"attribute":"timings"}
    - slot{"attribute":"timings"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"attribute":null}
    - slot{"mention":null}
    - slot{"knowledge_base_last_object":1}
    - slot{"knowledge_base_last_object_type":"services"}
* query_knowledge_base{"attribute":"book","mention":"it"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"attribute":null}
    - slot{"mention":null}
    - slot{"knowledge_base_last_object":1}
    - slot{"knowledge_base_last_object_type":"services"}
    - golf_book_form
    - form{"name":"golf_book_form"}
    - slot{"PERSON":"tomorrow"}
    - slot{"requested_slot":"time_slot"}
* inform{"time_slot":"Afternoon"}
    - slot{"time_slot":"Afternoon"}
    - slot{"time_slot":"Afternoon"}
    - golf_book_form
    - slot{"time_slot":"Afternoon"}
    - slot{"requested_slot":"guest_number"}
* inform{"number":1,"guest_number":"1"}
    - slot{"guest_number":"1"}
    - slot{"guest_number":"1"}
    - golf_book_form
    - slot{"guest_phone_number":"9874563211"}
    - slot{"pickup_location":"airport"}
    - slot{"PERSON":"tomorrow"}
    - slot{"pickup_time":"1 pm"}
    - slot{"car_type":"4 seater"}
    - slot{"object_type":"services"}
    - slot{"attribute":"description"}
    - slot{"services":"Golf"}
    - slot{"attribute":"timings"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - slot{"time_slot":"Afternoon"}
    - slot{"guest_number":"1"}
    - feedback_form
    - form{"name":"feedback_form"}
    - slot{"requested_slot":"use_conf"}
* affirm{"use_conf":"Yes"}
    - slot{"use_conf":"Yes"}
    - feedback_form
    - slot{"use_conf":"/affirm{\"use_conf\":\"Yes\"}"}
    - slot{"requested_slot":"user_email"}
* inform{"email":"vansh@gmail.com","user_email":"vansh@gmail.com"}
    - slot{"user_email":"vansh@gmail.com"}
    - feedback_form
    - slot{"user_email":"vansh@gmail.com"}
    - form{"name":null}
    - slot{"requested_slot":null}

## Story from conversation with ce05f2e87fa9473f90db24f1cbe95525 on September 30th 2020
* start
    - utter_welcome
* query_knowledge_base{"object_type":"services"}
    - slot{"object_type":"services"}
    - slot{"object_type":"services"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"mention":null}
    - slot{"attribute":null}
    - slot{"knowledge_base_last_object":null}
    - slot{"knowledge_base_last_object_type":"services"}
    - slot{"knowledge_base_listed_objects":[1,0,2]}
* query_knowledge_base{"attribute":"description","services":"Swimming pool"}
    - slot{"attribute":"description"}
    - slot{"services":"Swimming pool"}
    - slot{"attribute":"description"}
    - slot{"services":"Swimming pool"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"attribute":null}
    - slot{"mention":null}
    - slot{"knowledge_base_last_object":0}
    - slot{"knowledge_base_last_object_type":"services"}
* query_knowledge_base{"attribute":"timings"}
    - slot{"attribute":"timings"}
    - slot{"attribute":"timings"}
    - action_query_knowledge_base
    - slot{"object_type":"services"}
    - slot{"attribute":null}
    - slot{"mention":null}
    - slot{"knowledge_base_last_object":0}
    - slot{"knowledge_base_last_object_type":"services"}
* query_knowledge_base{"attribute":"book","mention":"it"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - action_query_knowledge_base
    - slot{"mention":null}
    - slot{"object_type":"services"}
    - golf_book_form
    - form{"name":"golf_book_form"}
    - slot{"requested_slot":"PERSON"}
* inform
    - golf_book_form
    - slot{"PERSON":"vansh"}
    - slot{"requested_slot":"time_slot"}
* inform{"time_slot":"Late morning"}
    - slot{"time_slot":"Late morning"}
    - slot{"time_slot":"Late morning"}
    - golf_book_form
    - slot{"time_slot":"Late morning"}
    - slot{"requested_slot":"guest_number"}
* inform{"number":1,"guest_number":"1"}
    - slot{"guest_number":"1"}
    - slot{"guest_number":"1"}
    - golf_book_form
    - slot{"guest_number":"1"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - slot{"object_type":"services"}
    - slot{"attribute":"description"}
    - slot{"services":"Swimming pool"}
    - slot{"attribute":"timings"}
    - slot{"attribute":"book"}
    - slot{"mention":"it"}
    - slot{"time_slot":"Late morning"}
    - slot{"guest_number":"1"}
    - feedback_form
    - form{"name":"feedback_form"}
    - slot{"requested_slot":"use_conf"}
* affirm{"use_conf":"Yes"}
    - slot{"use_conf":"Yes"}
    - feedback_form
    - slot{"use_conf":"/affirm{\"use_conf\":\"Yes\"}"}
    - slot{"requested_slot":"user_email"}
* inform{"email":"vansh@gmail.com","user_email":"vansh@gmail.com"}
    - slot{"user_email":"vansh@gmail.com"}
    - feedback_form
    - slot{"user_email":"vansh@gmail.com"}
    - form{"name":null}
    - slot{"requested_slot":null}