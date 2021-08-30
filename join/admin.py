from django.contrib import admin
from django.http import HttpResponse
from .models import Member

import csv
import datetime


admin.site.disable_action('delete_selected')

class MemberAdmin(admin.ModelAdmin):
	actions = ['export_csv']
	list_display = ('name', 'email', 'est_join_date', 'notifications', 'verified')
	readonly_fields=('join_date',)

	@admin.action(description='Create mailing list from selected members')
	def export_csv(self, request, queryset):
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = f'attachment; filename=email-list-{datetime.datetime.today()}.csv'
		writer = csv.writer(response)

		# Please use the date to ensure the mailing list is up to date!
		writer.writerow([datetime.datetime.now() - datetime.timedelta(hours=4)])  # converts time to est
		for member in queryset:
			writer.writerow([member.email])
		return response

admin.site.register(Member, MemberAdmin)
