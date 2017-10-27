from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.models import Page

from .blocks import ContentStreamBlock, SectionBlock


class ContentStreamPage(Page):
    body = ContentStreamBlock(
        blank=True,
        help='',
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        abstract = True


class SectionContentStreamPage(Page):
    body = SectionBlock(
        blank=True,
        help='',
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        abstract = True
