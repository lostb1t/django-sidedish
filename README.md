Django SideDish
==========================

Dishes are content boxes visible in various "side's" of your website

Whether, and where, a given dish will appear on a page depends on both the theme enabled and on administrative block settings. Dish settings are controlled from the SideDish administration. It is possible to control whether each dish is enabled where it will be placed on the page, and control the visibility of blocks on each page.


Features
----------

- Control visibilty of dishes on each page from admin
- CKeditor support for body field
- Schedule options for publishing
- Template tags to render individual dishes or side's
- Templates for dishes and side's


Installation
----------

Add ``sidedish`` to your ``INSTALLED_APPS`` setting.


Usage
----------



Available settings
----------

	SIDEDISH_SIDES = (('left', _('Left')),('right', _('Right')),)

List with side definitions.

	SIDEDISH_STATUS_DRAFT = 1
	SIDEDISH_STATUS_PUBLISHED = 2
	SIDEDISH_STATUS_CHOICES = (
	    (SIDEDISH_STATUS_DRAFT, _("Draft")),
	    (SIDEDISH_STATUS_PUBLISHED, _("Published")),
	)

Defines the various dish status choices.

Templates
----------

#### Template Tags

The following template tag libraries are available:

- `sidedish`: tags for dealing with dishes in general

    #### sidedishes

    Renders a side full of dishes

        {% sidedishes 'side_name' %}

    #### sidedish

    Renders a dish

        {% sidedish 'dish_slug' %}
