from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100 )
    pub_date = models.DateTimeField('pub_date')
    body = models.TextField()

    def __str__(self): # 게시글의 제목이 blog라는 어드민페이지 뜨게한다
        return self.title