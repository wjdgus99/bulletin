from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=100)
    content = models.TextField('CONTENT', default='')
    pub_date = models.DateTimeField('PUBLISH DATE', default=timezone.now)
    mod_date = models.DateTimeField('MODIFY DATE', auto_now=True)


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-mod_date',)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])


    def get_previous(self):
        return self.get_previous_by_mod_date()


    def get_next(self):
        return self.get_next_by_mod_date()


    def get_content(self):
        return self.content


    # def get_next_by_mod_date(self):
    #     return reverse('blog:post_detail', args=[self.id+1])
