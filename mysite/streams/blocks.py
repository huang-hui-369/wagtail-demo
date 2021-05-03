
from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="add a title")
    text = blocks.TextBlock(required=True, help_text="add a text")

    class Meta: 
        template="streams/title_and_text.html"
        icon = "edit"
        label = "Title & Text"


   