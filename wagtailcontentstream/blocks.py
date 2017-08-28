from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore.blocks import (
    RichTextBlock,
    TextBlock,
    StructBlock,
)
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock


class CaptionedImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = 'fa-image'
        template = 'wagtailcontentstream/blocks/captioned_image.html'
        help_text = 'Select an image and add a caption (optional).'


class ContentStream(StreamBlock):
    paragraph = RichTextBlock(
        icon='fa-paragraph',
        features=['bold', 'italic', 'link', 'ol', 'ul'],
    )
    heading = TextBlock(icon='fa-header', template='wagtailcontentstream/blocks/heading.html')
    image = CaptionedImageBlock()
    table = TableBlock(icon='fa-table')
    embed = EmbedBlock(icon='fa-youtube-play')
    code = CodeBlock(label='Code snippet')

    class Meta:
        template = 'standard/blocks/streamfield.html'
