def settings(request):
    """
    Put selected settings variables into the default template context
    """
    from builder.global_settings import GLOBAL_SETTINGS
    return GLOBAL_SETTINGS