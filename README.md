# Wagtail Content Stream

Markdown blocks for Wagtail Streamfields.

## Example Usage

    from wagtail.wagtailcore.fields import StreamField
    from wagtail.wagtailcore.models import Page
    from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
    from wagtailcontentstream import ContentStream

    class MyPage(Page):
        body = StreamField(ContentBlock())

        content_panels = Page.content_panels + [
            StreamFieldPanel('body'),
        ]

## Contributors

* Timothy Allen (https://github.com/FlipperPA)
