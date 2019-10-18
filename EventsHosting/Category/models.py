from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=101)
    body = models.TextField()
    price = models.IntegerField()
    datetime = models.DateTimeField()
    endtime = models.TimeField()
    image = models.FileField(upload_to='static/')
    ordering = ('category',)
    currentnum = models.IntegerField(default=0)
    maxnum = models.IntegerField(default=10)
    category = models.TextField()
    emaillist = models.TextField(blank=True)
    slug = models.SlugField()


    def snippet(self):
        return self.body[:250]+"..."

    def __str__(self):
        return self.title #+"   -   "+self.category+"   -   "+str(self.currentnum)


class ArtCraft(models.Model):

    event = models.ForeignKey('EventsHosting.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title+"("+str(self.event.currentnum)+")"


class Education(models.Model):
    #
    event = models.ForeignKey('EventsHosting.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title+"("+str(self.event.currentnum)+")"


class Fun(models.Model):

    event = models.ForeignKey('EventsHosting.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title+"("+str(self.event.currentnum)+")"


class Kids(models.Model):

    event = models.ForeignKey('EventsHosting.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title+"("+str(self.event.currentnum)+")"


class Meetup(models.Model):

    event = models.ForeignKey('EventsHosting.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title+"("+str(self.event.currentnum)+")"



class SelfDevelopment(models.Model):

    event = models.ForeignKey('EventsHosting.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title+"("+str(self.event.currentnum)+")"
