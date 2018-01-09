from django.contrib import admin
from .models import Person,Scholarship,IndiaState,Education,Religion,Category,Worker,Gender

# Register your models here.
admin.site.register(Person)
admin.site.register(Scholarship)
admin.site.register(IndiaState)
admin.site.register(Education)
admin.site.register(Religion)
admin.site.register(Category)
admin.site.register(Worker)
admin.site.register(Gender)