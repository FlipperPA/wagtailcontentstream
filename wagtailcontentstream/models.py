from wagtail import VERSION as WAGTAIL_VERSION


if WAGTAIL_VERSION >= (3, 0):
    from wagtail.admin.panels import FieldPanel
    from wagtail.fields import StreamField
    from wagtail.models import Page
else:
    from wagtail.admin.edit_handlers import StreamFieldPanel as FieldPanel
    from wagtail.core.fields import StreamField
    from wagtail.core.models import Page

from .blocks import ContentStreamBlock, ContentStreamBlockWithRawCode, SectionBlock


class ContentStreamPage(Page):
    body = StreamField(
        ContentStreamBlock(),
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        abstract = True


class ContentStreamPageWithRawCode(Page):
    body = StreamField(
        ContentStreamBlockWithRawCode(),
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        abstract = True


class SectionContentStreamPage(Page):
    body = StreamField(
        SectionBlock(),
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        abstract = True
