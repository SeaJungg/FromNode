from django.contrib import admin
from .models import Members
from .models import Projects
from .models import Posts

admin.site.register(Members)
admin.site.register(Projects)
admin.site.register(Posts)