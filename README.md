# Events-Hosting
A Django app that aids users to browse and book events, with easy management of events by the admin.


To run the application, run the following commands:
```
python manage.py makemigrations Events-Hosting
python manage.py migrate
python manage.py runserver
```

At the moment, there are 5 events. By default, the maximum number of seats for an event is 10, but this can be changed through the admin panel. 


### Admin credentials
Username:username
Password:password

The admin can add an event through the admin panel.
Also, the admin can see info of the users who have booked a ticket for the event.

**Note that the slug field should be small (5-8 characters) and **unique** since it will be used to generate a unique ID for each user who has booked a ticket.
The format for the token ID is <slug><current_num> where current_num is a mark for the number of users who have booked the ticket till now.
Moreover, it is highly recommended that the slug be closely related to the event**

A user cannot book more than one ticket for an event, but can book multiple events. This is taken care of, through the email-id of the user.


