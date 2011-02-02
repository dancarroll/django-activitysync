from django.shortcuts import render_to_response
from django.template import RequestContext

from activitysync.models import Activity

def index(request):
    return render_to_response(
        'index.html',
        {'activities': Activity.objects.published()},
        context_instance=RequestContext(request)
    )

