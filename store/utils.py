import random
import string

from django.utils.text import slugify

def list_changer(l):
    # """ if a list have tuple items and in those tuples there is only one item then this
    # function will return the list of only those items in the list the tuples will be gone."""
    # if len(l) > 0:
    #     return "sorry"
    #
    # else:
    z = []
    for i in l:
        z.append(i[0])

    return z


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug

    else:
        slug = slugify(instance.__class__)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug = slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
