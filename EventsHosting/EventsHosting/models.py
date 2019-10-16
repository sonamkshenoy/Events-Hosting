from django.db import models

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


#User.objects.order_by('last_name', 'userprofile__title')


    def snippet(self):
        return self.body[:250]+"..."

    def __str__(self):
        return self.title+"   -   "+self.category+"   -   "+str(self.currentnum)
