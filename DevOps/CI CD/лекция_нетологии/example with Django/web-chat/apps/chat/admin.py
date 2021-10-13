from django.contrib import admin

from apps.chat.forms import SectionForm
from apps.chat.models import Conversation, Message, Section


class ConversationInline(admin.TabularInline):
    model = Conversation
    extra = 0
    readonly_fields = ('text', 'user')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    inlines = (ConversationInline,)
    form = SectionForm


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('text', 'user')


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'user', 'created_at', 'modified_at')
    list_filter = ('section', 'user')
    search_fields = ('text', 'section__title')
    readonly_fields = ('user',)
    inlines = (MessageInline,)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'modified_at')
    list_filter = ('conversation', 'conversation__section', 'user')
    search_fields = ('text', 'conversation__text', 'conversation__section__title')
    readonly_fields = ('user',)
