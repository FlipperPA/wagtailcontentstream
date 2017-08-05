from wagtail.wagtailcore.blocks import TextBlock, StructBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class CaptionedImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = 'fa-image'
        template = 'wagtailcontentstream/blocks/captioned_image.html'
        help_text = 'Select an image and add a caption (optional).'
