from django.contrib import admin
from .models import Planet, Recruit, Sith, Test, Question, ResultTest

class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class RecruitAdmin(admin.ModelAdmin):
    list_display = ('name','planet','email','age',)
    list_display_links = ('name',)
    search_fields = ('name','email',)

class SithAdmin(admin.ModelAdmin):
    list_display = ('name','planet')
    list_display_links = ('name',)
    search_fields = ('name','planet')

class QuestionInline(admin.TabularInline):
    model = Question

class TestAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]
    list_display = ('uidorden',)
    list_display_links = ('uidorden',)
    search_fields = ('uidorden',)


class ResultTestAdmin(admin.ModelAdmin):
    list_display = ('recruit','question')


admin.site.register(Planet, PlanetAdmin)
admin.site.register(Recruit, RecruitAdmin)
admin.site.register(Sith, SithAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(ResultTest, ResultTestAdmin)