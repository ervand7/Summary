from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from apps.chat.forms import ConversationForm, MessageForm
from apps.chat.models import Conversation, Message, Section


def index_view(request):
    context = {
        'sections': Section.objects.all(),
    }
    return render(request, 'chat/index.html', context=context)


class SectionView(TemplateView):
    template_name = 'chat/section.html'

    @property
    def section_id(self):
        return self.kwargs.get('section_id')

    @property
    def conversation_id(self):
        return self.request.GET.get('conversation')

    @property
    def conversation(self):
        if not self.conversation_id:
            return None
        return get_object_or_404(Conversation, id=self.conversation_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        conversations = Conversation.objects.filter(section_id=self.section_id)

        if self.conversation_id:
            messages = Message.objects.filter(conversation_id=self.conversation_id)
        else:
            messages = []

        conversation_form = kwargs.get('conversation_form', ConversationForm())
        message_form = kwargs.get('message_form', MessageForm())

        context.update({
            'section': get_object_or_404(Section, id=self.section_id),
            'conversations': conversations,
            'conversation': self.conversation,
            'messages': messages,
            'conversation_form': conversation_form,
            'message_form': message_form,
        })
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form_type = request.POST.get('form')

        if form_type == 'conversation':
            form = self._process_form(ConversationForm, self._conversation_form_valid)
            if not form.is_valid():
                kwargs['conversation_form'] = form

        elif form_type == 'message' and self.conversation_id:
            form = self._process_form(MessageForm, self._message_form_valid)
            if not form.is_valid():
                kwargs['message_form'] = form

        return self.get(request, *args, **kwargs)

    def _process_form(self, form_class, on_valid):
        form = form_class(self.request.POST)
        if form.is_valid():
            on_valid(form)
        return form

    def _conversation_form_valid(self, form):
        conversation = form.save(commit=False)
        conversation.section_id = self.section_id
        conversation.user = self.request.user
        conversation.save()
        return conversation

    def _message_form_valid(self, form):
        message = form.save(commit=False)
        message.conversation_id = self.conversation_id
        message.user = self.request.user
        message.save()
        return message
