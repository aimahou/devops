from django.shortcuts import render
from server.models import RemoteUserBindHost
from .models import TerminalLog
from util.tool import login_required, post_required, admin_required
from django.http import JsonResponse
from .forms import HostForm
# Create your views here.


@login_required
def lists(request):
    hosts = RemoteUserBindHost.objects.all()
    return render(request, 'webssh/host_lists.html', locals())


@login_required
@post_required
def terminal(request):
    host_form = HostForm(request.POST)
    error_message = '请检查填写的内容!'
    if host_form.is_valid():
        host_id = host_form.cleaned_data.get('hostid')
        host = RemoteUserBindHost.objects.get(id=host_id)
        return render(request, 'webssh/terminal.html', locals())

    return JsonResponse({"code": 406, "err": error_message})


@login_required
@admin_required
def logs(request):
    logs = TerminalLog.objects.all()
    return render(request, 'webssh/terminal_logs.html', locals())
