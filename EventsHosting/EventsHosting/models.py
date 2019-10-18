from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Event(models.Model):
    title = models.CharField(max_length=101)
    body = models.TextField()
    price = models.IntegerField()
    datetime = models.DateTimeField()
    endtime = models.TimeField()
    image = models.FileField(upload_to='static/')
    currentnum = models.IntegerField(default=0)
    maxnum = models.IntegerField(default=10)
    category = models.TextField()
    emaillist = models.TextField(blank=True)
    slug = models.SlugField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)



    def snippet(self):
        return self.body[:250]+"..."

    def __str__(self):
        return self.title #+"   -   "+self.category+"   -   "+str(self.currentnum)


class Booking(models.Model):
    name = models.CharField(max_length=200)
    emailid = models.CharField(max_length=200)
    token = models.CharField(max_length=100)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.event.title


    # manufacturer = models.ForeignKey('Event', on_delete=models.CASCADE)

#User.objects.order_by('last_name', 'userprofile__title')
