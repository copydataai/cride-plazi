from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# models
from cride.users.models import User, Profile

class UserAdmin(UserAdmin):
    # fieldsets = (
    #     (None, {"fields": ("username", "password")}),
    #     (_("Personal info"), {"fields": ("first_name", "email")}),
    #     (
    #         _("Permissions"),
    #         {
    #             "fields": (
    #                 "is_active",
    #                 "is_staff",
    #                 "is_superuser",
    #                 "groups",
    #                 "user_permissions",
    #             ),
    #         },
    #     ),
    #     (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    # )
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_client",)
    list_filter = ("is_client", "is_staff", "created", "modified",)
    search_fields = ("first_name", "last_name",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin"""
    list_display = ('user', 'reputation', "rides_taken", "rides_offered",)
    search_fields = ('user__username', 'user__email', "user__first_name", "user__last_name",)
    list_filter = ('reputation',)


admin.site.register(User, UserAdmin)
