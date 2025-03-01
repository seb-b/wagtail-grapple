# Generated by Django 3.2.15 on 2022-08-12 14:55

from django.db import migrations

try:
    from wagtail import blocks
    from wagtail import fields
except ImportError:
    # Wagtail < 3.0
    from wagtail.core import blocks
    from wagtail.core import fields

from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=fields.StreamField(
                [
                    ("heading", blocks.CharBlock(form_classname="full title")),
                    ("paragraph", blocks.RichTextBlock()),
                    ("image", ImageChooserBlock()),
                    ("decimal", blocks.DecimalBlock()),
                    ("date", blocks.DateBlock()),
                    ("datetime", blocks.DateTimeBlock()),
                    (
                        "gallery",
                        blocks.StructBlock(
                            [
                                (
                                    "title",
                                    blocks.CharBlock(form_classname="full title"),
                                ),
                                (
                                    "images",
                                    blocks.StreamBlock(
                                        [
                                            (
                                                "image",
                                                blocks.StructBlock(
                                                    [
                                                        (
                                                            "caption",
                                                            blocks.CharBlock(
                                                                form_classname="full title"
                                                            ),
                                                        ),
                                                        (
                                                            "image",
                                                            ImageChooserBlock(),
                                                        ),
                                                    ]
                                                ),
                                            )
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "video",
                        blocks.StructBlock(
                            [
                                (
                                    "youtube_link",
                                    EmbedBlock(required=False),
                                )
                            ]
                        ),
                    ),
                    (
                        "objectives",
                        blocks.ListBlock(blocks.CharBlock()),
                    ),
                    (
                        "carousel",
                        blocks.StreamBlock(
                            [
                                (
                                    "text",
                                    blocks.CharBlock(form_classname="full title"),
                                ),
                                ("image", ImageChooserBlock()),
                                ("markup", blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    (
                        "callout",
                        blocks.StructBlock(
                            [
                                ("text", blocks.RichTextBlock()),
                                ("image", ImageChooserBlock()),
                            ]
                        ),
                    ),
                    (
                        "text_and_buttons",
                        blocks.StructBlock(
                            [
                                ("text", blocks.TextBlock()),
                                (
                                    "buttons",
                                    blocks.ListBlock(
                                        blocks.StructBlock(
                                            [
                                                (
                                                    "button_text",
                                                    blocks.CharBlock(
                                                        label="Text",
                                                        max_length=50,
                                                        required=True,
                                                    ),
                                                ),
                                                (
                                                    "button_link",
                                                    blocks.CharBlock(
                                                        label="Link",
                                                        max_length=255,
                                                        required=True,
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "mainbutton",
                                    blocks.StructBlock(
                                        [
                                            (
                                                "button_text",
                                                blocks.CharBlock(
                                                    label="Text",
                                                    max_length=50,
                                                    required=True,
                                                ),
                                            ),
                                            (
                                                "button_link",
                                                blocks.CharBlock(
                                                    label="Link",
                                                    max_length=255,
                                                    required=True,
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("page", blocks.PageChooserBlock()),
                    (
                        "text_with_callable",
                        blocks.StructBlock(
                            [
                                ("text", blocks.CharBlock()),
                                ("integer", blocks.IntegerBlock()),
                                ("decimal", blocks.FloatBlock()),
                            ]
                        ),
                    ),
                    (
                        "block_with_name",
                        blocks.StructBlock([("name", blocks.TextBlock())]),
                    ),
                    (
                        "advert",
                        SnippetChooserBlock("home.Advert"),
                    ),
                    (
                        "person",
                        SnippetChooserBlock("home.Person"),
                    ),
                ],
            ),
        ),
    ]
