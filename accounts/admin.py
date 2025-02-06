from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import ApproverProfile, SalesmanProfile



class ApproverProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only superusers can create ApproverProfile
        return request.user.is_superuser

class ApproverProfileInline(admin.StackedInline):
    model = ApproverProfile
    can_delete = False
    verbose_name = 'Approver Profile'

class SalesmanProfileInline(admin.StackedInline):
    model = SalesmanProfile
    can_delete = False
    verbose_name = 'Salesman Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ApproverProfileInline, SalesmanProfileInline)

    def get_inline_instances(self, request, obj=None):
        # Show ApproverProfile inline for staff users, SalesmanProfile for non-staff
        if obj and obj.is_staff:
            return [ApproverProfileInline(self.model, self.admin_site)]
        elif obj:
            return [SalesmanProfileInline(self.model, self.admin_site)]
        return []

# Unregister default User admin and re-register with customization
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(ApproverProfile, ApproverProfileAdmin)