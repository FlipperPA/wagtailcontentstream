from wagtail.wagtailcore.blocks import (
    RichTextBlock,
    TextBlock,
)
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtailcodeblock.blocks import CodeBlock

from .blocks import CaptionedImageBlock


class ContentStream(StreamField):
    paragraph = RichTextBlock(icon='fa-paragraph')
    heading = TextBlock(icon='fa-header', template='wagtailcontentstream/blocks/heading.html')
    image = CaptionedImageBlock()
    table = TableBlock(icon='fa-table')
    embed = EmbedBlock(icon='fa-youtube-play')
    code = CodeBlock(label='Code snippet')

    class Meta:
        template = 'wagtailcontentstream/blocks/streamfield.html'
