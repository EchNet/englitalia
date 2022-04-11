from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class UserAdmin(BaseUserAdmin):
  list_display = [ele for ele in BaseUserAdmin.list_display] + ["hijack_button"]

  def hijack_button(self, obj):
    if not obj.is_active:
      return "Not active"
    return format_html(
        mark_safe("""
        <input type="submit" formaction="/hijack/{}/" value="Hijack" />
        """), obj.id)

  hijack_button.short_description = "Hijack"
  hijack_button.allow_tags = True


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
