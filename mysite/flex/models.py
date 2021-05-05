""" flexabel page """

from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks

from streams import blocks as myblocks

class FlexPage(Page):

    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("title_and_text", myblocks.TitleAndTextBlock()),
            ("prograph", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=50, null=True,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

class Meta: 

    verbose_name = "flex_page"
    verbose_name_plural = "flex_pages"
