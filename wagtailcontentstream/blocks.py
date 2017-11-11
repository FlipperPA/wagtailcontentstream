from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore.blocks import (
    RichTextBlock,
    TextBlock,
    StructBlock,
    StreamBlock,
)

from wagtail.wagtaildocs.blocks import DocumentChooserBlock
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


class ContentStreamBlock(StreamBlock):
    heading = TextBlock(
        icon='title',
        template='wagtailcontentstream/blocks/heading.html',
    )
    paragraph = RichTextBlock(
        icon='pilcrow',
        features=['bold', 'italic', 'link', 'ol', 'ul'],
    )
    image = CaptionedImageBlock()
    document = DocumentChooserBlock()
    embed = EmbedBlock(icon='media')
    table = TableBlock(icon='table')
    code = CodeBlock(icon='code')

    class Meta:
        help_text = 'The main page body.'


class SectionStructBlock(StructBlock):
    section_heading = TextBlock(
        icon='title',
        help_text='Heading for this section.',
    )
    body = ContentStreamBlock(
        help_text='The body content goes here.',
    )

    class Meta:
        template = 'wagtailcontentstream/blocks/section_struct_block.html'
        icon = 'doc-full-inverse'


class SectionBlock(StreamBlock):
    section = SectionStructBlock()

    class Meta:
        help_text = 'The main page body.'
