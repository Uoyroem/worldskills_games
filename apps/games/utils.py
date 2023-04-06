
def upload_to(instance, filename: str):
    return f'{instance.get_absolute_url()}/{filename}'
