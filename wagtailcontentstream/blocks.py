from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.blocks import (
    StructBlock,
    TextBlock,
    StreamBlock,
    RichTextBlock,
)
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.contrib.table_block.blocks import TableBlock

from wagtailcodeblock.blocks import CodeBlock


class CaptionedImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = 'fa-image'
        template = 'standard/blocks/captioned_image.html'
        help_text = 'Select an image and add a caption (optional).'


class ContentStreamBlock(StreamBlock):
    paragraph = RichTextBlock(icon='fa-paragraph')
    heading = TextBlock(icon='fa-header', template='standard/blocks/heading.html')
    image = CaptionedImageBlock()
    table = TableBlock(icon='fa-table')
    embed = EmbedBlock(icon='fa-youtube-play')
    code = CodeBlock(label='Code snippet')

    class Meta:
        template = 'standard/blocks/streamfield.html'
