# Wagtail Content Stream

An abstract Django model with a Wagtail StreamField named `body` with multiple blocks I use on a regular basis. This is geared towards developers who need to write examples with code in them. It's opinionated: very little HTML is allowed in the text block, forcing authors to create structured data. The following blocks are included in `ContentStreamBlock`:

* Heading
* Paragraph
* Captioned Image
* Embed
* Table
* Code Block

A secondary StreamBlock, `ContentStreamBlockWithRawCode`, also provides an additional block for injecting HTML, JS, and CSS code. Use with care, as this can really blow up your markup and is a potential code injection point!

Three pages types are provided out-of-the-box.

## Example Usage

You will need to add `wagtailcodeblock` to your `INSTALLED_APPS` Django setting.

#### Basic Usage: a Title Field and Content Stream

First, create a page type in your `models.py`:

```python
from wagtailcontentstream.models import ContentStreamPage, SectionContentStreamPage, ContentStreamPageWithRawCode

class StandardPage(ContentStreamPage):
    pass

class SectionStandardPage(SectionContentStreamPage):
    pass

class StandardPageWithRawCode(ContentStreamPageWithRawCode):
    pass
```

Then in your template:

```django
{% load wagtailcore_tags %}

<h2>{{ page.title }}</h2>
{% include_block page.body %}
```

#### Extended Usage: Adding More Fields

```python
from django.conf import settings
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtailcontentstream.models import ContentStreamPage


class StandardPage(ContentStreamPage):
    date = models.DateField("Post Date")
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL)

    content_panels = [
        FieldPanel('date'),
        FieldPanel('authors'),
    ] + ContentStreamPage.content_panels
```

# Release Notes & Contributors

* Thank you to our [wonderful contributors](https://github.com/FlipperPA/wagtailcontentstream/graphs/contributors)!
* Release notes are [available on GitHub](https://github.com/FlipperPA/wagtailcontentstream/releases).

# Project Maintainer

* Timothy Allen (https://github.com/FlipperPA)
