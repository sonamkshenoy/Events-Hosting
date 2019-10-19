from django.shortcuts import render
from .models import Event, Booking

# Display all events
def events(request):
    events = Event.objects.all()
    return render(request,'events.html',{'events':events})

# Display details
def details(request,slug):
    event = Event.objects.get(slug=slug)
    bookings = Booking.objects.all().filter(event__title=event)

    # Check if number of bookings are greater than maximum number
    if(len(bookings)>=event.maxnum):
        return render(request, 'eventdetail.html',{'event':event, 'filled':'Filled'})
    return render(request, 'eventdetail.html',{'event':event})

# Confirm booking
def submit(request):
    name=request.POST.get('name')
    emailid=request.POST.get('emailid')
    phonenumber=request.POST.get('phonenumber')
    slug = request.POST.get('slug-to-mark')
    event = Event.objects.get(slug=slug)

    # Check if there is already a booking with that emailid for that event
    present = Booking.objects.all().filter(event__title=event, emailid=emailid)


    if(len(present)==0):
        # Generate a token
        tokenidnum = len(Booking.objects.all().filter(event__title=event))
        token = slug+str(tokenidnum)

        bookPerson = Booking(name= name, emailid = emailid, phonenumber=phonenumber, token=token, event=event)#, category=event.category)
        bookPerson.save()
        return render(request,'submitted.html', {'success':'sucess', 'bookPerson': bookPerson,'event':event})

    else: #If the person has already booked a ticket for this event
        return render(request, 'submitted.html', {'error':'You can book only one ticket for this event!', 'name':name,'event':event})
