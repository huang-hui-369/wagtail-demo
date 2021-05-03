from django.db import models

from wagtail.core.models import Page

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):

    # 追加image field
    head_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = RichTextField(blank=True)

    # 只能有一个home page
    max_count = 1

    # 在panels追加image
    content_panels = Page.content_panels + [
        ImageChooserPanel('head_image'),
        FieldPanel('body', classname="full"),
    ]

    # s

    
