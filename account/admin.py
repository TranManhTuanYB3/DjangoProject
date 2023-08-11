from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account, Customer

@admin.register(Account)
class AccountAdmin(UserAdmin):
	list_display = ('id', 'email','username', 'created', 'updated', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('created', 'updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'name', 'address', 'phone')