""" flexabel page """

from django.db import models

from wagtail.admin.edit_handlers import FieldPanel 
from wagtail.core.models import Page

class FlexPage(Page):

    template = "flex/flex_page.html"

    # @todo add stream field

    # content = StreamField()

    subtitle = models.CharField(max_length=50, null=True,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

class Meta: 

    verbose_name = "flex_page"
    verbose_name_plural = "flex_pages"
