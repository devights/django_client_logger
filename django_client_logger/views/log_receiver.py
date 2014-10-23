from django.shortcuts import render, HttpResponse
from django_client_logger.views.rest_dispatch import RESTDispatch
from django_client_logger.logger import process_log_message
import json


class LogReceiver(RESTDispatch):
    def POST(self, request):
        body = request.POST
        try:
            process_log_message(json.loads(body.get('data')))
        except Exception as e:
            print e
        return HttpResponse("")