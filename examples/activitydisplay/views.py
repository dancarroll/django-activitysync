from django.http import HttpResponse
from activitysync.models import Activity

def index(request):
    return HttpResponse("Nice", status=200, mimetype='text/plain')

