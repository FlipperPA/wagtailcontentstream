# Wagtail Content Stream

An abstract Django model with a Wagtail StreamField named `body` with multiple blocks I use on a regular basis. It's opinioned: very little HTML is allowed in the text block, forcing authors to create structured data. The following blocks are included in the StreamBlock, `ContentStreamBlock`:

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
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtailcontentstream.models import ContentStreamPage


class StandardPage(ContentStreamPage):
    date = models.DateField("Post Date")
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL)

    content_panels = [
        FieldPanel('date'),
        FieldPanel('authors'),
    ] + ContentStreamPage.content_panels
```

# Change Log

## 0.4

* Added ContentStreamPageWithRawCode and ContentStreamBlockWithRawCode for injecting raw code into pages.

## 0.3

* Wagtail 2.0 compatibility.

## 0.3.1

* Add support for alignment and credit of CaptionedImageBlock.

## 0.2

* Add a StreamBlock with sections.

## 0.2.1

* Help text and a bug fix for Section StreamBlocks.

## 0.2.2

* Improve block templates.

## 0.2.3

* Add Documents as a block type.

# 0.1

* Initial release.

# Contributors

* Timothy Allen (https://github.com/FlipperPA)
