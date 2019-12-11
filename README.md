# Events-Hosting
A Django app that aids users to browse and book events, with easy management of events by the admin.


To run the application, run the following commands:
```
cd EventsHosting
pip install -r requirements.txt
python manage.py runserver
```

At the moment, there are a few events. By default, the limit on the number of seats for an event is 10, which can however be changed through the admin panel.


### Admin features  

The admin can add an event through the admin panel **through the section for "Events"**.

Any changes made to a particular category will be reflected in the Events, Bookings that belong to that Category.  
Similarly any changes made to an event will be seen in the booking under that event too.

The admin can see info of all the users who have booked a ticket for the event and filter them based on a category.

The category filters have been dynamically added; thus if any category is deleted or added, the admin **need not** manually add the category to the filter. It will automatically be updated. All they have to do is add a new category to the "Category" section.  

Event booking form isn't made available (in Master branch) or the events aren't displayed (in ModificationNoDisplay branch) if all tickets for that particular event are sold.

**Note that the slug field should be small (5-8 characters) and **unique** since it will be used to generate a unique ID for each user who has booked a ticket.**
The format for the token ID is <slug_name><current_num> where slug_name is the slug and current_num is an indicator of the number of users who have booked the ticket till now.
Moreover, it is highly recommended that the slug be closely related to the event.

A user can book more than one ticket for an event and check their bookings too with their Email ID.


To add any extra field to the model, make the changes in models.py and then run,
```
python manage.py makemigrations EventsHosting
python manage.py migrate
```
