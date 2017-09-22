# Wagtail Content Stream

An abstract Django abstract model with a Wagtail StreamField named `body` with multiple blocks I use on a regular basis. It's opinioned: very little HTML is allowed in the text block, forcing authors to create structured data. The following blocks are included in the StreamField:

* Heading
* Paragraph
* Captioned Image
* Embed
* Table
* Code Block

## Example Usage

You will need to add `wagtailcodeblock` to your `INSTALLED_APPS` Django setting.

#### Basic Usage: a Title Field and Content Stream

First, create a page type in your `models.py`:

    from wagtailcontentstream.models import ContentStreamPage

    class StandardPage(ContentStreamPage):
        pass

Then in your template:

    <h1>{{ page.title }}</h2>
    {{ page.body }}

#### Extended Usage: Adding More Fields

    from django.db import models
    from wagtail.wagtailadmin.edit_handlers import FieldPanel
    from wagtailcontentstream.models import ContentStreamPage


    class StandardPage(ContentStreamPage):
        date = models.DateField("Post Date")

        content_panels = [
            FieldPanel('date'),
        ] + ContentStreamPage.content_panels


## Contributors

* Timothy Allen (https://github.com/FlipperPA)
