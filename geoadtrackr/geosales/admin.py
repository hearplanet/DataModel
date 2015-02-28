from django.contrib import admin

# Register your models here.
from geosales.models import Publisher
from geosales.models import App
from geosales.models import Agent
from geosales.models import Venue
from geosales.models import App_to_Venue
from geosales.models import Install
from geosales.models import Geofield

admin.site.register(Publisher)
admin.site.register(App)
admin.site.register(Agent)
admin.site.register(Venue)
admin.site.register(App_to_Venue)
admin.site.register(Install)
admin.site.register(Geofield)