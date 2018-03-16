import random
import string

from django.utils.text import slugify
from django.db import models
from django.db.models.signals import pre_save

from store.utils import unique_slug_generator
from account.models import Profile

class OnlyActiveItems(models.Manager):
    def all(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(OnlyActiveItems, self).filter(active=True)

# Create your models here.
class Company(models.Model):
	owner = models.ForeignKey(Profile, related_name="companies")
	name = models.CharField(max_length=25)
	email = models.EmailField(blank=True, null=True)
	phone = models.BigIntegerField(blank=True, null=True)
	location = models.CharField(max_length = 50, help_text="state/city, country")
	timestamp = models.DateTimeField(auto_now_add= True)
	slug = models.SlugField(unique=True, blank=True)

	active = models.BooleanField(default=True)
	objects = OnlyActiveItems()


	class Meta(object):
		verbose_name_plural = "Companies"
		ordering = ["-timestamp"]

	def __str__(self):
		return self.name


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
        slug = slugify(instance.name)

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


pre_save.connect(pre_save_slug, sender=Company)
