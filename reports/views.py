from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404, FileResponse
import os


@login_required
def reports(request):
    reports = request.user.office.report_set.all()
    context = {'reports': reports}
    return render(request, "reports/reports.html", context)


@login_required
def report_download(request, pk):
    report = list(request.user.office.report_set.filter(id=pk))
    if len(report):
        report = report[0]
        # file_path = "media/documents/reports/Empresa 1/Oficina 1/reporte.txt" # report.get_document_filename()
        file_path = report.get_document_filename()
        try:
            response = FileResponse(open(file_path, 'rb'))
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        except Exception:
            raise Http404
    else:
        raise Http404
