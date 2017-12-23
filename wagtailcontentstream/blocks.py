# Wagtail 2.0 compatibility - new package paths
from wagtail.contrib.table_block.blocks import TableBlock
try:
    from wagtail.core.blocks import (
        ChoiceBlock,
        RichTextBlock,
        TextBlock,
        StructBlock,
        StreamBlock,
    )
    from wagtail.documents.blocks import DocumentChooserBlock
    from wagtail.embeds.blocks import EmbedBlock
    from wagtail.images.blocks import ImageChooserBlock
except ImportError:
    from wagtail.wagtailcore.blocks import (
        ChoiceBlock,
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
    """
    An image block with a caption, credit, and alignment.
    """
    CENTER = 1
    FULL = 2
    LEFT = 3
    RIGHT = 4
    ALIGN_CHOICES = (
        (LEFT, 'left'),
        (RIGHT, 'right'),
        (CENTER, 'center'),
        (FULL, 'full width'),
    )

    image = ImageChooserBlock(
        help_text='The image to display.',
    )
    caption = TextBlock(
        required=False,
        help_text='The caption will appear under the image, if entered.'
    )
    credit = TextBlock(
        required=False,
        help_text='The credit will appear under the image, if entered.'
    )
    align = ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('right', 'Right'),
            ('center', 'Center'),
            ('full', 'Full Width'),
        ],
        default='left',
        help_text='How to align the image in the body of the page.'
    )

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
