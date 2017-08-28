# Wagtail Content Stream

Markdown blocks for Wagtail Streamfields.

## Example Usage

You will need to add `wagtailcodeblock` and `wagtailcontentstream` both to your `INSTALLED_APPS` Django setting.

    from wagtail.wagtailcore.fields import StreamField
    from wagtail.wagtailcore.models import Page
    from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
    from wagtailcontentstream.blocks import ContentStream

    class MyPage(Page):
        body = StreamField(ContentStream())

        content_panels = Page.content_panels + [
            StreamFieldPanel('body'),
        ]

## Contributors

* Timothy Allen (https://github.com/FlipperPA)
