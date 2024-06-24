
async def get_google_forms_link(form_id):
    creds = Credentials(...)
    forms_service = build('forms', 'v1', credentials=creds)
    form = forms_service.forms().get(formId=form_id).execute()
    return form['responderUri']
