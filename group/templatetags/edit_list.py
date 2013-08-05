from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.inclusion_tag("tags/edit_list.html")
def edit_list(tag_object):
    content_type = ContentType.objects.get_for_model(tag_object.__class__)
    url_admin = reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(tag_object.pk,))
    return dict(url_admin=url_admin)

