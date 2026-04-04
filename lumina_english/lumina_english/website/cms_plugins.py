from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import SimpleText, CourseCard

from .models import (
    Navigation,
    HeroSection,
    AISection,
    CoursesSection,
    DashboardSection,
    Footer,
    EnrollmentModal,
)


@plugin_pool.register_plugin
class SimpleTextPlugin(CMSPluginBase):
    model = SimpleText
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
    model = CourseCard
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
    model = Navigation
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
    model = HeroSection
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
    model = AISection
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
    model = CoursesSection
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
    model = DashboardSection
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
    model = Footer
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
    model = EnrollmentModal
    module = _('Lumina')
    name = _('Enrollment Modal')
    render_template = 'website/plugins/enrollment_modal.html'
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context
