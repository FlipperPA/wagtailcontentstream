from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore.blocks import (
    RichTextBlock,
    TextBlock,
    StructBlock,
)

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock


class CaptionedImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = 'image'
        template = 'wagtailcontentstream/blocks/captioned_image.html'
        help_text = 'Select an image and add a caption (optional).'


class ContentStreamPage(Page):
    body = StreamField([
        (
            'heading',
            TextBlock(
                icon='title',
                template='wagtailcontentstream/blocks/heading.html',
            ),
        ),
        (
            'paragraph',
            RichTextBlock(
                icon='pilcrow',
                features=['bold', 'italic', 'link', 'ol', 'ul'],
            ),
        ),
        ('image', CaptionedImageBlock()),
        ('embed', EmbedBlock(icon='media')),
        ('table', TableBlock(icon='table')),
        ('code', CodeBlock(icon='code')),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        abstract = True
