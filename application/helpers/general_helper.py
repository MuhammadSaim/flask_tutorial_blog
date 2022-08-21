
def form_errors(form):
    errors = {}
    for error in form.errors:
        errors[error] = form.errors.get(error)[0]
    return errors


def is_ajax(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'
