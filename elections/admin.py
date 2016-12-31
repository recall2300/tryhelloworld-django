from django.contrib import admin
from .models import *

admin.site.register(Candidate)
admin.site.register(Poll)
admin.site.register(Choice)