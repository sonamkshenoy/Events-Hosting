# Events-Hosting
A Django app that aids users to browse and book events, with easy management of events by the admin.


To run the application, run the following commands:
```
cd EventsHosting
pip install -r requirements.txt
python manage.py runserver
```

At the moment, there are 5 events. By default, the limit on the number of seats for an event is 10, which can however be changed through the admin panel. 


### Admin credentials
Username:username  
Password:password

The admin can add an event through the admin panel.
Also, the admin can see info of all the users who have booked a ticket for the event.

**Note that the slug field should be small (5-8 characters) and **unique** since it will be used to generate a unique ID for each user who has booked a ticket.
The format for the token ID is <slug_name><current_num> where slug_name is the slug and current_num is an indicator of the number of users who have booked the ticket till now.
Moreover, it is highly recommended that the slug be closely related to the event.**

A user cannot book more than one ticket for an event, but can book multiple events. This is taken care of, through the email-id of the user.


To add any extra field to the model, make the changes in models.py and then run,
```
python manage.py makemigrations EventsHosting
python manage.py migrate
```
