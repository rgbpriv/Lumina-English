from django.db import models
from cms.models.pluginmodel import CMSPlugin


# Generic rich HTML content plugin. Use this to store textual/HTML
# fragments editable in the CMS frontend. Tailwind classes can be
# included in the stored HTML so styling remains on the frontend.
class SimpleText(CMSPlugin):
	title = models.CharField(max_length=255, blank=True, null=True)
	content = models.TextField(blank=True, help_text='HTML content, can include Tailwind classes')

	def __str__(self):
		return self.title or f"SimpleText #{self.pk}"


# Course card plugin for the repeated course boxes on the page.
class CourseCard(CMSPlugin):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	price = models.CharField(max_length=64, blank=True)
	highlight = models.BooleanField(default=False)

	def __str__(self):
		return self.title


# Navigation bar plugin (stores HTML or small structured text)
class Navigation(CMSPlugin):
	content = models.TextField(blank=True, help_text='Navigation HTML (use Tailwind classes)')

	def __str__(self):
		return f"Navigation #{self.pk}"


# Hero section plugin
class HeroSection(CMSPlugin):
	eyebrow = models.CharField(max_length=255, blank=True)
	heading = models.TextField(blank=True)
	subheading = models.TextField(blank=True)
	cta_text = models.CharField(max_length=128, blank=True)
	cta_link = models.CharField(max_length=255, blank=True)
	image_url = models.CharField(max_length=1024, blank=True)

	def __str__(self):
		return self.eyebrow or f"Hero #{self.pk}"


# AI Era section plugin
class AISection(CMSPlugin):
	pretitle = models.CharField(max_length=255, blank=True)
	title = models.CharField(max_length=255, blank=True)
	body = models.TextField(blank=True)

	def __str__(self):
		return self.title or f"AISection #{self.pk}"


# Courses section wrapper (can contain CourseCard children)
class CoursesSection(CMSPlugin):
	title = models.CharField(max_length=255, blank=True)
	intro = models.TextField(blank=True)

	def __str__(self):
		return self.title or f"Courses #{self.pk}"


# Dashboard mockup plugin
class DashboardSection(CMSPlugin):
	greeting = models.CharField(max_length=255, blank=True)
	next_class = models.CharField(max_length=255, blank=True)
	stat_1_title = models.CharField(max_length=64, blank=True)
	stat_1_value = models.CharField(max_length=64, blank=True)
	stat_2_title = models.CharField(max_length=64, blank=True)
	stat_2_value = models.CharField(max_length=64, blank=True)
	stat_3_title = models.CharField(max_length=64, blank=True)
	stat_3_value = models.CharField(max_length=64, blank=True)

	def __str__(self):
		return self.greeting or f"Dashboard #{self.pk}"


# Footer plugin
class Footer(CMSPlugin):
	content = models.TextField(blank=True, help_text='Footer HTML (Tailwind allowed)')

	def __str__(self):
		return f"Footer #{self.pk}"


# Enrollment modal plugin
class EnrollmentModal(CMSPlugin):
	heading = models.CharField(max_length=255, blank=True)
	subtext = models.TextField(blank=True)

	def __str__(self):
		return self.heading or f"Modal #{self.pk}"
