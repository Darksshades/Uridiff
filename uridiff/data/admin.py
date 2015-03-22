from django.contrib import admin
from uridiff.data.models import Question, UriUser

class QuestionAdmin(admin.ModelAdmin):
    pass

class UriUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(UriUser, UriUserAdmin)