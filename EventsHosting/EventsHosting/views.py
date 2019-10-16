from django.shortcuts import render
from .models import Event


def events(request):
    events = Event.objects.all()
    return render(request,'events.html',{'events':events})

def details(request,slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'eventdetail.html',{'event':event})

def submit(request):
    name=request.POST.get('name')
    emailid=request.POST.get('emailid')
    phonenumber=request.POST.get('phonenumber')
    slug=request.POST.get('slug-to-mark')
    event=Event.objects.get(slug=slug)

    if(emailid not in event.emaillist):
        event.emaillist=event.emaillist+"Token ID:"+slug+str(event.currentnum)+ "\nEmail Id: "+emailid+ "\nName: "+name+ "\nPhone number:" + phonenumber+ "\n\n\n"
        event.currentnum+=1
        event.save()
        return render(request,'submitted.html', {'success':'sucess', 'name':name, 'uid':slug+str(event.currentnum) ,'emailid':emailid, 'phonenumber':phonenumber,'event':event})
    else:
        return render(request, 'submitted.html', {'error':'You can book only one ticket for this event!', 'name':name, 'emailid':emailid, 'phonenumber':phonenumber,'event':event})
