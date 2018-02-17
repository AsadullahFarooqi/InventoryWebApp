import random
import string

from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.http import HttpResponseRedirect
from django.utils.text import slugify


from .utils import code_generator

User = settings.AUTH_USER_MODEL
# Create your models here.
class Profile(models.Model):
    user              = models.OneToOneField(User, related_name='profile') # user.profile
    activation_key    = models.CharField(max_length=120, blank=True, null=True)
    activated         = models.BooleanField(default=False)
    timestamp         = models.DateTimeField(auto_now_add=True)
    updated           = models.DateTimeField(auto_now=True)
    slug              = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator()# 'somekey' #gen key
            self.save()
            #path_ = reverse()
            user_email = self.user.email
            path_ = reverse_lazy("user_activation", kwargs={"code": self.activation_key})
            full_path = HttpResponseRedirect(path_)
            print(full_path)
            subject = "{0} User Account Activation".format(user_email,)
            from_email = settings.DEFAULT_FROM_EMAIL
            message = "user email and path {0}: {1}".format(user_email, full_path)
            
            recipient_list = ["asadullah.itcgcs@gmail.com"]
            html_message = "<p>user email and path {0}: {1}</p>".format(user_email, full_path)
            print(html_message)
            # sent_mail = send_mail(
            #                 subject, 
            #                 message, 
            #                 from_email, 
            #                 recipient_list, 
            #                 fail_silently=False, 
            #                 html_message=html_message)
            sent_mail = False
            return sent_mail

#f'Activate your account here: {full_path}' 



def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.user.username)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_slug, sender=Profile)