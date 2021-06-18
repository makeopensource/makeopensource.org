from django.contrib import admin
from .models import Idea, Author
from projects.models import Project, Contributor
from . import ghfunc

@admin.action(description='Approve an idea(s)')
def approve(modeladmin, request, queryset):
        queryset.update(approved=True)
        return

@admin.action(description='Unapprove an idea(s)')
def unapprove(modeladmin, request, queryset):
        queryset.update(approved=False)
        return

@admin.action(description="Publish Idea to Project")
def publish(modeladmin, request, queryset):
        for obj in queryset:
                if not obj.approved:
                        return

        for obj in queryset:
                ghlink, ghrepo = ghfunc.createRepo(obj.title, obj.description)
                ghfunc.permissionUserToRepo(obj.author.github, ghrepo)
                b = Project(title=obj.title, description=obj.description, github = ghlink, release_date=obj.release_date)  
                b.save()
                obj.delete()
        return


class IdeaAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'release_date', 'approved']
        ordering = ['release_date']
        actions = [approve, unapprove, publish]


admin.site.register(Idea, IdeaAdmin)
admin.site.register(Author)
