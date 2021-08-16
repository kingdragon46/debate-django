from django.contrib.auth import get_user_model
from django.contrib import admin
from .forms import SignUpForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import *
# from .forms import UserAdminCreationForm, UserAdminChangeForm


class CustomUserAdmin(BaseUserAdmin):

    add_form = SignUpForm
    # form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'phone', 'is_staff', 'is_active','user_creation_date', 'user_type', 'points')
    list_filter = ('email', 'first_name', 'last_name', 'phone','is_staff', 'is_active','user_creation_date', 'user_type', 'points')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password', 'phone', 'user_type', 'user_creation_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_banned', 'is_deleted')}),
        ('Debates', {'fields': ('debates', 'debates_won', 'debates_lost', 'points')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','phone', 'password1', 'password2', 'is_staff', 'is_active', 'user_creation_date')}
        ),
    )
    search_fields = ('email','phone',)
    ordering = ('email','phone',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)