# Wagtail 2.0 compatibility - new package paths
try:
    from wagtail.admin.edit_handlers import StreamFieldPanel
    from wagtail.core.fields import StreamField
    from wagtail.core.models import Page
except ImportError:
    from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
    from wagtail.wagtailcore.fields import StreamField
    from wagtail.wagtailcore.models import Page

from .blocks import ContentStreamBlock, SectionBlock


class ContentStreamPage(Page):
    body = StreamField(
        ContentStreamBlock(),
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        abstract = True


class SectionContentStreamPage(Page):
    body = StreamField(
        SectionBlock(),
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        abstract = True
