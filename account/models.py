import random
import string

# from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
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
            user_email = self.user.email
            path_ = reverse("user_activation", kwargs={"code": self.activation_key})
            # full_path = settings.ALLOWED_HOSTS[0] + path_
            full_path = "http://127.0.0.1:8000" + path_
            # subject = "User Account Activation"   #"http://asadliam.pythonanywhere.com"
            # from_email = settings.DEFAULT_FROM_EMAIL
            # message = "user email and path {0}: {1}".format(user_email, full_path)
            # recipient_list = ["asadullah.itcgcs@gmail.com"]
            # html_message = "<p>user email and path {0}: {1}</p>".format(user_email, full_path)

            # with open("/home/AsadLiam/forgithub/inventory/AppliedUsers.csv", 'a') as csvfile:
            with open(settings.BASE_DIR + "/AppliedUsers.csv", 'a') as csvfile:
                csvfile.write(str(str(self.user.username) + " , " + str(user_email) + " , " + str("Activation Key :: " + full_path) + " , " + self.user.first_name) + " , " + str(self.user.last_name)  + "\n")

            # print(html_message)
            # sent_mail = send_mail(
            #                 subject,
            #                 message,
            #                 from_email,
            #                 recipient_list,
            #                 fail_silently=False,
            #                 html_message=html_message)
            sent_mail = False
            return sent_mail


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
