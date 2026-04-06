from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import LuminaFrontendBaseModel
from .cms_forms import (
    HeroSectionForm,
    SimpleTextForm,
    CourseCardForm,
    LuminaNavigationForm,
    AISectionForm,
    CoursesSectionForm,
    DashboardForm,
    FooterForm,
    EnrollmentModalForm,
)


@plugin_pool.register_plugin
class SimpleTextPlugin(CMSPluginBase):
    model = LuminaFrontendBaseModel
    form = SimpleTextForm
    module = _('Lumina')
    name = _('Simple Text (HTML)')
    render_template = 'website/plugins/simple_text.html'
    allow_children = False
    text_enabled = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class CourseCardPlugin(CMSPluginBase):
    model = LuminaFrontendBaseModel
    form = CourseCardForm
    module = _('Lumina')
    name = _('Course Card')
    render_template = 'website/plugins/course_card.html'
    allow_children = False
    text_enabled = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class LuminaNavigationPlugin(CMSPluginBase):
    model = LuminaFrontendBaseModel
    form = LuminaNavigationForm
    module = _('Lumina')
    name = _('Navigation')
    render_template = 'website/plugins/navigation.html'
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class HeroPlugin(CMSPluginBase):
    model = LuminaFrontendBaseModel
    form = HeroSectionForm
    module = _('Lumina')
    name = _('Hero Section')
    render_template = 'website/plugins/hero.html'
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class AISectionPlugin(CMSPluginBase):
    model = LuminaFrontendBaseModel
    form = AISectionForm
    module = _('Lumina')
    name = _('AI Era Section')
    render_template = 'website/plugins/ai_section.html'
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class CoursesSectionPlugin(CMSPluginBase):
    model = LuminaFrontendBaseModel
    form = CoursesSectionForm
    module = _('Lumina')
    name = _('Courses Section')
    render_template = 'website/plugins/courses_section.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class DashboardPlugin(CMSPluginBase):
    model = LuminaFrontendBaseModel
    form = DashboardForm
    module = _('Lumina')
    name = _('Dashboard Section')
    render_template = 'website/plugins/dashboard.html'
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class FooterPlugin(CMSPluginBase):
    model = LuminaFrontendBaseModel
    form = FooterForm
    module = _('Lumina')
    name = _('Footer')
    render_template = 'website/plugins/footer.html'
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class EnrollmentModalPlugin(CMSPluginBase):
    model = LuminaFrontendBaseModel
    form = EnrollmentModalForm
    module = _('Lumina')
    name = _('Enrollment Modal')
    render_template = 'website/plugins/enrollment_modal.html'
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context
