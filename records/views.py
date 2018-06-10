from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import generic


from .models import Record


class Index(generic.ListView):
    template_name = 'records/index.html'
    context_object_name = 'record_list'

    def get_queryset(self):
        return Record.record_set.order_by('submit_time')


@login_required
def detail(request, pk):
    user = request.user
    if user.has_perm('record.view_all_records'):
        record = Record.record_set.get(pk=pk)
        return HttpResponse(record)
    return HttpResponse("No Permission.")
