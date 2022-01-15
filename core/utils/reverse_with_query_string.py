from django.urls import reverse


def reverse_querystring(view, urlconf=None, args=None, kwargs=None, current_app=None, query_kwargs=None):
    """Custom reverse to handle query strings.
    Usage:
        reverse_querystring('app.views.my_view', kwargs={'pk': 123}, query_kwargs={'search': 'Bob'})

        for multivalue query string
        reverse_querystring('app.views.my_view', kwargs={'pk': 123}, query_kwargs={'search': ['Bob', 'Jack']})
    """
    base_url = reverse(view, urlconf=urlconf, args=args, kwargs=kwargs, current_app=current_app)

    if query_kwargs:
        lst = []
        for k, v in query_kwargs.items():
            if isinstance(v, (list, tuple)):
                for ret in v:
                    lst.append("%s=%s" % (k, ret))
            else:
                lst.append("%s=%s" % (k, v))

        query_string = "&".join(lst)
        return "%s?%s" % (base_url, query_string)
    return base_url
