def context_dict(request):
    ctx = {}
    current_user = request.user
    if current_user.id is not None:
        if not current_user.is_staff:
            empresa = current_user.office.customer
            ctx['empresa'] = empresa
    return ctx
