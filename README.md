# Wagtail Content Stream

An abstract Django model with a Wagtail StreamField named `body` with multiple blocks I use on a regular basis. It's opinioned: very little HTML is allowed in the text block, forcing authors to create structured data. The following blocks are included in the StreamField:

* Heading
* Paragraph
* Captioned Image
* Embed
* Table
* Code Block

A secondary page type, `SectionContentStreamPage`, provides sections headers for a bit more structure.

## Example Usage

You will need to add `wagtailcodeblock` to your `INSTALLED_APPS` Django setting.

#### Basic Usage: a Title Field and Content Stream

First, create a page type in your `models.py`:

```python
from wagtailcontentstream.models import ContentStreamPage

class StandardPage(ContentStreamPage):
    pass

class SectionStandardPage(SectionContentStreamPage):
    pass
```

Then in your template:

```html
<h2>{{ page.title }}</h2>
{{ page.body }}
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

## Contributors

* Timothy Allen (https://github.com/FlipperPA)
