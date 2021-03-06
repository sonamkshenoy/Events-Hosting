from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator


# Display all events
def events(request):
    events_list = Event.objects.all()
    paginator = Paginator(events_list,2)
    page=request.GET.get('page')
    events = paginator.get_page(page)
    return render(request,'events.html',{'events':events})

# Display details
def details(request,slug):
    event = Event.objects.get(slug=slug)
    bookings = Booking.objects.all().filter(event__title=event)
    eventTickets = EventTickets.objects.all()
    for eventdet in eventTickets:
        print(eventdet.eventName)
        print(eventdet.tickets.all())

    # Check if number of bookings are greater than maximum number
    if(len(bookings)>=event.maxnum):
        return render(request, 'eventdetail.html',{'event':event, 'filled':'Filled'})
    return render(request, 'eventdetail.html',{'event':event,'tickets':{'paid':True, 'paidCost':500, 'free':True, 'donation':False}})

# Confirm booking
def submit(request):
    name=request.POST.get('name')
    emailid=request.POST.get('emailid').lower()
    phonenumber=request.POST.get('phonenumber')
    slug = request.POST.get('slug-to-mark')
    event = Event.objects.get(slug=slug)

    # # Check if there is already a booking with that emailid for that event
    # present = Booking.objects.all().filter(event__title=event, emailid=emailid)
    #
    #
    # if(len(present)==0):
    # Generate a token
    tokenidnum = len(Booking.objects.all().filter(event__title=event))+1
    token = slug+str(tokenidnum)

    bookPerson = Booking(name= name, emailid = emailid, phonenumber=phonenumber, token=token, event=event)#, category=event.category)
    bookPerson.save()
    return render(request,'submitted.html', {'success':'sucess', 'bookPerson': bookPerson,'event':event})

    # else: #If the person has already booked a ticket for this event
    #     return render(request, 'submitted.html', {'error':'You can book only one ticket for this event!', 'name':name,'event':event})



def viewBookings(request):
    if(request.method=="POST"):
        emailid = request.POST['emailid'].lower()
        print(emailid)
        bookings = Booking.objects.all().filter(emailid=emailid)
        print(bookings)
        # return HttpResponse(bookings)
        return render(request,'viewBookings.html', {'check':'check', 'bookings':bookings})

    return render(request,'viewBookings.html')
