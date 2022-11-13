from django.contrib import admin
from polls.models import Question

admin.site.register(Question)  # сообщение админке, что у объекта Question есть интерфейс администратора
