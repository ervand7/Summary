from django import forms
from django_svg_image_form_field import SvgAndImageFormField

from apps.chat.models import Conversation, Message, Section


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ('text',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
