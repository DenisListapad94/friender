from celery import shared_task
# from friender.celery import app
from .models import UserRating
import requests
import base64
from django.core.files.base import ContentFile


@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def generate_photo(user_id,rating,description):
    response = requests.post(
        'https://bf.dallemini.ai/generate',
        json={'prompt': description}
    )
    data = base64.b64decode(response.json()['images'][0])
    photo = ContentFile(data, name='hello.png')
    UserRating.objects.create(user_id=int(user_id),rating=int(rating),description=description,photo=photo)