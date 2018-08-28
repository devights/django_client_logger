from django.http import HttpResponse
from django.views import View
from django_client_logger.logger import process_log_message
from userservice.user import UserService
import logging
import json

logger = logging.getLogger(__name__)


class LogReceiver(View):
    def post(self, request, *args, **kwargs):
        original_user = UserService().get_original_user()
        override_user = UserService().get_override_user()
        session_key = request.session.session_key
        body = request.POST
        try:
            data = body.get('data')
            process_log_message(json.loads(data), session_key,
                                original_user, override_user)
        except Exception as ex:
            logger.error('Failed to process log messages: %s, "%s"' % (
                ex, data))
        return HttpResponse('')
