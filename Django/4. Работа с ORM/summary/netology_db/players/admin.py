from django.contrib import admin

from .models import Player, Team


class PlayerAdmin(admin.ModelAdmin):
    pass


class TeamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)