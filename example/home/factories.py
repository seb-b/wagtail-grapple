import datetime

import factory
import wagtail_factories
from factory import fuzzy
from home.blocks import (
    ImageGalleryBlock,
    ImageGalleryImage,
    ImageGalleryImages,
    TextWithCallableBlock,
)
from home.models import (
    Advert,
    Author,
    AuthorPage,
    BlogPage,
    BlogPageRelatedLink,
    MiddlewareModel,
    Person,
    SimpleModel,
)
from wagtail.core import blocks


# START: Block Factories
class DateBlockFactory(wagtail_factories.blocks.BlockFactory):
    class Meta:
        model = blocks.DateBlock


class DateTimeBlockFactory(wagtail_factories.blocks.BlockFactory):
    class Meta:
        model = blocks.DateTimeBlock


class DecimalBlockFactory(wagtail_factories.blocks.BlockFactory):
    class Meta:
        model = blocks.DecimalBlock


class RichTextBlockFactory(wagtail_factories.blocks.BlockFactory):
    class Meta:
        model = blocks.RichTextBlock


class StreamBlockFactory(wagtail_factories.blocks.BlockFactory):
    class Meta:
        model = blocks.StreamBlock


class PageChooserBlockFactory(wagtail_factories.blocks.BlockFactory):
    class Meta:
        model = blocks.PageChooserBlock


class ImageGalleryImageFactory(wagtail_factories.StructBlockFactory):
    image = factory.SubFactory(wagtail_factories.ImageChooserBlockFactory)

    class Meta:
        model = ImageGalleryImage


class ImageGalleryImagesFactory(StreamBlockFactory):
    class Meta:
        model = ImageGalleryImages


class ImageGalleryBlockFactory(wagtail_factories.StructBlockFactory):
    title = factory.Sequence(lambda n: f"Image gallery {n}")
    images = factory.SubFactory(ImageGalleryImagesFactory)

    class Meta:
        model = ImageGalleryBlock


class TextWithCallableBlockFactory(wagtail_factories.StructBlockFactory):
    text = factory.Sequence(lambda n: f"Text with callable {n}")
    integer = factory.fuzzy.FuzzyInteger(low=1, high=10)
    decimal = factory.fuzzy.FuzzyFloat(low=0.1, high=0.9)

    class Meta:
        model = TextWithCallableBlock


class BlogPageRelatedLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPageRelatedLink

    page = factory.SubFactory("home.factories.BlogPageFactory")
    name = factory.Sequence(lambda n: f"Person {n}")
    url = factory.Sequence(lambda n: f"Url {n}")


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    page = factory.SubFactory("home.factories.BlogPageFactory")
    role = factory.Sequence(lambda n: f"Role {n}")
    person = factory.SubFactory("home.factories.PersonFactory")


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    name = factory.Sequence(lambda n: f"Name {n}")
    job = factory.Sequence(lambda n: f"Job {n}")


class BlogPageFactory(wagtail_factories.PageFactory):
    title = factory.Sequence(lambda n: f"Blog post {n}")
    date = datetime.date.today()
    author = factory.SubFactory("home.factories.AuthorPageFactory")
    body = wagtail_factories.StreamFieldFactory(
        {
            "heading": wagtail_factories.CharBlockFactory,
            "paragraph": RichTextBlockFactory,
            "image": wagtail_factories.ImageChooserBlockFactory,
            "decimal": DecimalBlockFactory,
            "date": DateBlockFactory,
            "datetime": DateTimeBlockFactory,
            "gallery": ImageGalleryBlockFactory,
            "page": PageChooserBlockFactory,
            "text_with_callable": TextWithCallableBlockFactory,
            "objectives": wagtail_factories.ListBlockFactory(
                wagtail_factories.CharBlockFactory
            ),
        }
    )

    class Meta:
        model = BlogPage

    @factory.post_generation
    def create_links(self, create, extracted, **kwargs):
        if create:
            # Create Blog Links
            BlogPageRelatedLinkFactory.create_batch(5, page=self)
            # Create a Person
            person = PersonFactory.create()
            # Create Blog Authors
            AuthorFactory.create_batch(8, page=self, person=person)
            # Create Blog tags
            for tag in ["Tag 1", "Tag 2", "Tag 3"]:
                self.tags.add(tag)


class AuthorPageFactory(wagtail_factories.PageFactory):
    name = factory.Sequence(lambda n: f"Person {n}")

    class Meta:
        model = AuthorPage


class AdvertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advert

    url = factory.Sequence(lambda n: f"Person {n}")
    text = fuzzy.FuzzyText()


class SimpleModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SimpleModel


class MiddlewareModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MiddlewareModel
