from django import forms
from django.utils.translation import gettext_lazy as _
from entangled.forms import EntangledModelForm
from djangocms_text.fields import HTMLFormField
from .models import LuminaFrontendBaseModel


class HeroSectionForm(EntangledModelForm):
    eyebrow = forms.CharField(label=_("Eyebrow"), required=False)
    heading = HTMLFormField(label=_("Heading"), required=False)
    subheading = HTMLFormField(label=_("Subheading"), required=False)
    cta_text = forms.CharField(label=_("CTA Text"), required=False)
    cta_link = forms.CharField(label=_("CTA Link"), required=False)
    image_url = forms.CharField(label=_("Image URL"), required=False)

    frontend_editable_fields = ['eyebrow', 'heading', 'subheading', 'cta_text', 'cta_link', 'image_url']

    class Meta:
        model = LuminaFrontendBaseModel
        entangled_fields = {'config': ['eyebrow', 'heading', 'subheading', 'cta_text', 'cta_link', 'image_url']}


class SimpleTextForm(EntangledModelForm):
    content = HTMLFormField(
        label=_("Content"),
        required=False,
    )

    frontend_editable_fields = ['content']

    class Meta:
        model = LuminaFrontendBaseModel
        entangled_fields = {'config': ['content']}


class CourseCardForm(EntangledModelForm):
    title = forms.CharField(label=_("Title"), required=False)
    description = HTMLFormField(label=_("Description"), required=False)
    price = forms.CharField(label=_("Price"), required=False)
    highlight = forms.BooleanField(label=_("Highlight"), required=False)

    frontend_editable_fields = ['title', 'description']

    class Meta:
        model = LuminaFrontendBaseModel
        entangled_fields = {'config': ['title', 'description']}


class LuminaNavigationForm(EntangledModelForm):
    content = HTMLFormField(label=_("Content"), required=False)

    frontend_editable_fields = ['content']

    class Meta:
        model = LuminaFrontendBaseModel
        entangled_fields = {'config': ['content']}


class AISectionForm(EntangledModelForm):
    pretitle = forms.CharField(label=_("Pretitle"), required=False)
    title = forms.CharField(label=_("Title"), required=False)
    body = HTMLFormField(label=_("Body"), required=False)

    frontend_editable_fields = ['pretitle', 'title', 'body']

    class Meta:
        model = LuminaFrontendBaseModel
        entangled_fields = {'config': ['pretitle', 'title', 'body']}


class CoursesSectionForm(EntangledModelForm):
    title = forms.CharField(label=_("Title"), required=False)
    intro = HTMLFormField(label=_("Intro"), required=False)

    frontend_editable_fields = ['title', 'intro']

    class Meta:
        model = LuminaFrontendBaseModel
        entangled_fields = {'config': ['title', 'intro']}


class DashboardForm(EntangledModelForm):
    greeting = forms.CharField(label=_("Greeting"), required=False)
    next_class = forms.CharField(label=_("Next class"), required=False)
    stat_1_title = forms.CharField(label=_("Stat 1 Title"), required=False)
    stat_1_value = forms.CharField(label=_("Stat 1 Value"), required=False)
    stat_2_title = forms.CharField(label=_("Stat 2 Title"), required=False)
    stat_2_value = forms.CharField(label=_("Stat 2 Value"), required=False)
    stat_3_title = forms.CharField(label=_("Stat 3 Title"), required=False)
    stat_3_value = forms.CharField(label=_("Stat 3 Value"), required=False)

    frontend_editable_fields = [
        'greeting', 'next_class',
        'stat_1_title', 'stat_1_value',
        'stat_2_title', 'stat_2_value',
        'stat_3_title', 'stat_3_value',
    ]

    class Meta:
        model = LuminaFrontendBaseModel
        entangled_fields = {'config': [
            'greeting', 'next_class',
            'stat_1_title', 'stat_1_value',
            'stat_2_title', 'stat_2_value',
            'stat_3_title', 'stat_3_value',
        ]}


class FooterForm(EntangledModelForm):
    content = HTMLFormField(label=_("Content"), required=False)

    frontend_editable_fields = ['content']

    class Meta:
        model = LuminaFrontendBaseModel
        entangled_fields = {'config': ['content']}


class EnrollmentModalForm(EntangledModelForm):
    heading = forms.CharField(label=_("Heading"), required=False)
    subtext = HTMLFormField(label=_("Subtext"), required=False)

    frontend_editable_fields = ['heading', 'subtext']

    class Meta:
        model = LuminaFrontendBaseModel
        entangled_fields = {'config': ['heading', 'subtext']}