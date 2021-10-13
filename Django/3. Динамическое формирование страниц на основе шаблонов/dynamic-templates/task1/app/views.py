from django.shortcuts import render
from app.work_with_csv import get_csv_file_content


def inflation_view(request):
    template_name = 'inflation.html'
    all_table, columns_names = get_csv_file_content()
    context = {'columns_names': columns_names, 'all_table': all_table}
    return render(
        request=request, template_name=template_name, context=context
    )
