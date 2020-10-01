## intent:start
- start
- START
- Start

## intent:greet
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
- and checkin time
- whats check in time

## intent:faq/ask_checkout_time
- what is the checkout time
- whats the checkout time
- what is the latest I can leave me room
- what is the latest checkout time
- what is the last time I can move out
- what is the last time I can check out
- and check out time

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

## intent:faq/ask_roomservice_lastorder
- whats the last order time
- when is the last order
- whats the lastest I can order room service
- last order

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
- hi, pick me up from [airport](pickup_location)
- I need a [4 seater](car_type) car to pick me up from [Airport](pickup_location)

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
- [Ben Stokes](PERSON)
- [David Hooks](PERSON)
- [4](guest_number)
- [2](guest_number)
- [5](guest_number)
- [1](guest_number)
- [Early morning](time_slot)
- [Late morning](time_slot)
- [Afternoon](time_slot)
- [vanshkapil@gmail.com](user_email)
- [vansh@getsoothr.com](user_email)
- [david@seapines.com](user_email)
- [d.saker@marriot.com](user_email)

## intent:query_knowledge_base
- what [services](object_type) do you have ?
- Tell me about the [services](object_type) hotel provide
- What [services](object_type) are there in the hotel
- what is there [to do]{"entity": "object_type", "value": "services"} in your hotel
- what [services](object_type) do you provide
- tell me about your [services](object_type)
- what [facilities]{"entity": "object_type", "value": "services"} are available
- what other [services](object_type) are there
- What [services](object_type) do you provide at the hotel?
- What are the [services](object_type) we have at hotels?
- What [services](object_type) are you providing to hotel guests?
- What [services](object_type) do you offer in hotel?
- What kind of [services](object_type) does your hotel provide?
- What would be the usual [services](object_type) at a hotel?
- what is the [price](attribute) of a [SPA]{"entity": "services", "value": "Spa Station"} session?
- how much does a session of [spa]{"entity": "services", "value": "Spa Station"} [cost]{"entity": "attribute", "value": "price"} ?
- what's the [price](attribute)
- What are the [pool]{"entity": "services", "value": "Swimming pool"} [timings](attribute)?
- whats the opening [time]{"entity": "attribute", "value": "timings"} of [Golf](services)?
- what are the [charges]{"entity": "attribute", "value": "price"}?
- how much do you [charge]{"entity": "attribute", "value": "price"} for a session of [golf]{"entity": "services", "value": "Golf"}?
- show me [pictures]{"entity": "attribute", "value": "image"} of your [pool]{"entity": "services", "value": "Swimming pool"}
- ok, [book](attribute) [it](mention)
- [reserve]{"entity": "attribute", "value": "book"} a [golf]{"entity": "services", "value": "Golf"} session
- how to [reserve]{"entity": "attribute", "value": "book"} a session of [Golf](services)
- I want to [book](attribute) [it](mention) for [4](guest_number) people
- What are the [spa]{"entity": "services", "value": "Spa Station"} [timings](attribute)?
- whats the opening [time]{"entity": "attribute", "value": "timings"} of [spa]{"entity": "services", "value": "Spa Station"}?
- show me [pictures]{"entity": "attribute", "value": "image"} of your [spa]{"entity": "services", "value": "Spa Station"}
- [tell me]{"entity": "attribute", "value": "description"} about your [spa]{"entity": "services", "value": "Spa Station"}
- how do I [reserve]{"entity": "attribute", "value": "book"} [it](mention)
- [reserve]{"entity": "attribute", "value": "book"} a [pool]{"entity": "services", "value": "Swimming pool"} session for me please

## synonym:Golf
- golf

## synonym:Spa Station
- SPA
- spa

## synonym:Swimming pool
- pool

## synonym:book
- reserve

## synonym:description
- tell me

## synonym:image
- pictures

## synonym:price
- cost
- charges
- charge

## synonym:services
- to do
- facilities

## synonym:timings
- time

## regex:car_type
- 4 seater
- 6 seater

## regex:guest_number
- ^[1-9]$

## regex:guest_phone_number
- ^[6-9]\d{9}$

## regex:user_email
- [^@]+@[^@]+\.[^@]+
