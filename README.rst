==========================
Django SideDish
==========================

Dishes are the boxes visible in various area of your Drupal website's screens.

Whether, and where, a given dish will appear on a page depends on both the theme enabled and on administrative block settings. Dish settings are controlled from the SideDish administration. It is possible to control whether each dish is enabled where it will be placed on the page, and control the visibility of blocks on each page.


Installation
============

Add ``sidedish`` to your ``INSTALLED_APPS`` setting.


Usage
============

Templates
=========

Template Tags
-------------

The following template tag libraries are available:

- `sidedish`: tags for dealing with dishes in general

    side
    -----------

    Renders a side

        {% dish 'side_name' %}

    dish
    -----------

    Renders a dish

        {% dish 'dish_slug' %}
