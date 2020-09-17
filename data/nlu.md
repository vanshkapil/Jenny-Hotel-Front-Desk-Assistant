## intent:start
- hey
- hello
- hi
- good morning
- good evening
- hey there
- namaskar
- wassup
- namaste
- whats up
- hey How are you
- hello How are you
- hi there
- Hrllo

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- tata
- ok bye
- acha to hum chalte hain
- thanks, bye
- Stop
- End

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- yeah
- ya
- haan
- sahi

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- na
- naa
- nope

## intent:faq/ask_filler
- ok
- hmm
- acha
- good
- interesting
- wow
- Hehe
- Ok
- nothing

## intent:faq/ask_bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:faq/ask_wifi_password
- whats the wifi password
- hey , what is the password for wifi
- what is internet password
- how do I start hotel internet
- how to access hotel wifi
- I want hotel's internet
- How to use hotel wifi
- tell me wifi password
- tell me internet password

## intent:faq/ask_checkin_time
- what is the checkin time
- whats the latest I can checkin
- tell me checkin time
- temme check in time
- whats check in time

## intent:faq/ask_checkout_time
- what is the checkout time
- whats the checkout time
- what is the latest I can leave me room
- what is the latest checkout time
- what is the last time I can move out
- what is the last time I can check out

## intent:faq/ask_roomservice_there
- do you have room service
- is there room service available
- can i order food in my room
- i want room service
- I want water
- I want soda
- I want to order some food
- I want something to eat
- Can I get beer
- room service
- roomservice

## intent:faq/ask_whatservices
- What services are there in the hotel
- what is there to do in your hotel
- what services do you provide
- tell me about your services
- what facilities are available 
- what other services are there
- What services do you provide at the hotel?
- What are the services we have at hotels?
- What services are you providing to hotel guests?
- What services do you offer in hotel?
- What kind of services does your hotel provide?
- What would be the usual services at a hotel?

## intent:faq/bookpool
- I want to book pool session
- book pool service for me
- I want to go swimming
- book pool for me
- I want to use the pool

## intent:faq/ask_roomservice_lastorder
- whats the last order time
- when is the last order
- whats the lastest I can order room service
- last order

## intent:faq/ask_pool_there
- do you have a swimming pool
- is there a pool

## intent:faq/ask_pool_timings
- what are the pool timings
- is pool accessable now
- what are timings of swimming pool
- what time can i use the pool

## intent:request_pickup_car
- I want a pickup car
- I want you to send a car to pick up me
- can you arrange a car to pick me up from [airport](pickup_location)
- I want a car to receive me at the [Airport](pickup_location) at [5PM](pickup_time)
- pick me up from the [airport](pickup_location) please.
- I need a pickup car
- i need  pickup car
- [5pm](pickup_time)
- I need a pickup car from [Airport](pickup_location)
- send a pick up car please
- need a pickup from [airport](pickup_location) at [11am](pickup_time)
- Send a car to recieve me from [Airport](pickup_location)
- Send a car to pick me up from [airport](pickup_location)
- Send a car to meet me at [airport](pickup_location)
- Can someone send me a car to recieve me from [airport](pickup_location) ?
- Send a car to [Airport](pickup_location) to recieve me.

## intent:inform
- my name is [Rob Smith](PERSON)
- [Robin Hood](PERSON)
- [Tom Bantan](PERSON)
- [Jack Sparrow](PERSON)
- [Bob Woolmer](PERSON)
- [airport](pickup_location)
- pick me from [AIRPORT](pickup_location)
- pick me up from the [25th Avenue street](pickup_location)
- I will be there at [2 am](pickup_time)
- [3:00Pm](pickup_time)
- [4](pickup_time) in the afternoon
- [4 seater](car_type)
- [6 seater](car_type)
- I want a [4 seater](car_type)
- [9560833330](guest_phone_number)
- [8765432112](guest_phone_number)
- my number is [7846112671](guest_phone_number)
- [Robin smith](PERSON)
- [Robin Singh](PERSON)
- [Airport](pickup_location)
- [1451/23 Naiwala, Karol Bagh](pickup_location)
- I am [Bob woolmer](PERSON), my number is [9798765432](guest_phone_number) I need a pickup car from [Airport](pickup_location)
- [1 pm](pickup_time)
- [2 pm](pickup_time)
- [3:30 pm](pickup_time)
- [4.20 pm](pickup_time)
- [5 pm](pickup_time)
- [6pm](pickup_time)
- [7pm](pickup_time)
- [8pm](pickup_time)
- [9 PM](pickup_time)
- [10 PM](pickup_time)
- [11 Pm](pickup_time)
- [12 Pm](pickup_time)
- [1 Am](pickup_time)
- [2 am](pickup_time)
- [3 Am](pickup_time)
- [4 am](pickup_time)
- [5 Am](pickup_time)
- [6AM](pickup_time)
- [7am](pickup_time)
- [8am](pickup_time)
- [9 AM](pickup_time)
- [10 AM](pickup_time)
- [11 Am](pickup_time)
- [12 Am](pickup_time)
- [7660833330](guest_phone_number)
- [8660865330](guest_phone_number)
- [9760832330](guest_phone_number)
- [9560844330](guest_phone_number)
- [9760833530](guest_phone_number)
- [9660367330](guest_phone_number)
- Ben Stokes
- David Hooks

## regex:guest_phone_number
- ^[6-9]\d{9}$
