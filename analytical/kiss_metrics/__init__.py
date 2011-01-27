"""
==============================
KISSmetrics -- funnel analysis
==============================

KISSmetrics_ is an easy to implement analytics solution that provides a
powerful visual representation of your customer lifecycle.  Discover how
many visitors go from your landing page to pricing to sign up, and how
many drop out at each stage.

.. _KISSmetrics: http://www.kissmetrics.com/


.. kiss-metrics-installation:

Installation
============

You only need to do perform these steps if you are not using the
generic :ttag:`analytical.*` tags.  If you are, skip to
:ref:`kiss-metrics-configuration`.

In order to use the template tag, you need to add
:mod:`analytical.kiss_metrics` to the installed applications list in
the project :file:`settings.py` file::

    INSTALLED_APPS = [
        ...
        'analytical.kiss_metrics',
        ...
    ]

The KISSmetrics Javascript code is inserted into templates using a
template tag.  Load the :mod:`kiss_metrics` template tag library and
insert the :ttag:`kiss_metrics` tag.  Because every page that you want
to track must have the tag, it is useful to add it to your base
template.  Insert the tag at the top of the HTML head::

    {% load kiss_metrics %}
    <html>
    <head>
    {% kiss_metrics %}
    ...


.. _kiss-metrics-configuration:

Configuration
=============

Before you can use the KISSmetrics integration, you must first set your
API key.


.. _kiss-metrics-api-key:

Setting the API key
-------------------

Every website you track events for with KISSmetrics gets its own API
key, and the :ttag:`kiss_metrics` tag will include it in the rendered
Javascript code.  You can find the website API key by visiting the
website *Product center* on your KISSmetrics dashboard.  Set
:const:`KISS_METRICS_API_KEY` in the project :file:`settings.py` file::

    KISS_METRICS_API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

If you do not set an API key, the tracking code will not be rendered.


.. _kiss-metrics-internal-ips:

Internal IP addresses
---------------------

Usually you do not want to track clicks from your development or
internal IP addresses.  By default, if the tags detect that the client
comes from any address in the :const:`INTERNAL_IPS` setting, the
tracking code is commented out.  See :const:`ANALYTICAL_INTERNAL_IPS`
for important information about detecting the visitor IP address.


.. _kiss-metrics-identify-user:

Identifying users
-----------------

If your websites identifies visitors, you can pass this information on
to KISSmetrics so that you can tie events to users.  By default, the
username of an authenticated user is passed to KISSmetrics
automatically.  See :data:`ANALYTICAL_AUTO_IDENTIFY` for important
information about detecting authenticated visitors.

You can also send the visitor identity yourself by adding the
``analytical_identity`` variable to the template context::

    context = RequestContext({'analytical_identity': identity})
    return some_template.render(context)

If you can derive the identity from the HTTP request, you can also use
a context processor that you add to the
:data:`TEMPLATE_CONTEXT_PROCESSORS` list in :file:`settings.py`::

    def identify(request):
        try:
            return {'analytical_identity': request.user.email}
        except AttributeError:
            return {}

Just remember that if you set the same context variable in the
:class:`~django.template.context.RequestContext` constructor and in a
context processor, the latter clobbers the former.
"""

kiss_metrics_service = {
    'head_top': 'analytical.kiss_metrics.templatetags.kiss_metrics.KissMetricsNode',
}
