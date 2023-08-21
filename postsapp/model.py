from django.db  import models


class Post(models.Model):

    username= models.CharField(max_length=1000)

    caption = models.TextField()
    likes= models.PositiveIntegerField(default=0)

    def __str__(self) :
        return self.caption
    
    class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        text = models.TextField()

        def __str__(self):
            return self.text