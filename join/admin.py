from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
	readonly_fields=('join_date',)

admin.site.register(Member, MemberAdmin)
