from __future__ import unicode_literals
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class StandardPage(Page):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname='full'),
    ]


class HomePage(Page):
    feature = RichTextField(blank=True)
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('feature', classname='full'),
        FieldPanel('content', classname='full'),
    ]
