"""
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Example_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'example_theme')
"""

# encoding: utf-8

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import config
from ckanext.pages.interfaces import IPagesSchema
import ckan.logic.action.get as tk


ORGANIZATION_FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLScw8OGeR6ZbUGcxjJ-nl9JQpXmHuUu0e52P0cqlKQKy9Ty_vg/viewform'

def organization_form():
    return ORGANIZATION_FORM_LINK

def organization_views(org_packages):
    org_views = 0
    for pkg in org_packages:
        pkg_views = toolkit.get_action('package_show')(
            data_dict={'id':pkg.name,'tracking_data':'true'})
        pkg_views = pkg_views['tracking_summary']['total']   
        org_views = org_views + pkg_views
    return org_views

def all_categories():
    all_categories_list = []
    
    category = {}
    category['text'] = "Agriculture, Food & Forests"
    category['img_src'] = "/example_theme_categories/agriculture.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Cities & Regions"
    category['img_src'] = "/example_theme_categories/cities.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Connectivity"
    category['img_src'] = "/example_theme_categories/connectivity.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Culture"
    category['img_src'] = "/example_theme_categories/culture.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Demography"
    category['img_src'] = "/example_theme_categories/demography.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Economy & Finance"
    category['img_src'] = "/example_theme_categories/economy.png"    
    all_categories_list.append(category)

    category = {}
    category['text'] = "Education"
    category['img_src'] = "/example_theme_categories/education.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Environment & Energy"
    category['img_src'] = "/example_theme_categories/environment.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Government & Public Sector"
    category['img_src'] = "/example_theme_categories/government.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Health"
    category['img_src'] = "/example_theme_categories/health.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Housing & Public Services"
    category['img_src'] = "/example_theme_categories/housing.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Manufactoring & Public Services"
    category['img_src'] = "/example_theme_categories/manufecturing.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Public Safety"
    category['img_src'] = "/example_theme_categories/publicsafety.png"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Science & Technology"
    category['img_src'] = "/example_theme_categories/science.png"
    all_categories_list.append(category)

    return all_categories_list

def popular_datasets(limit=4):
    datasets = toolkit.get_action('package_search')(
        data_dict={ 'sort':'views_total desc','rows':limit})
    return datasets['results']

def most_recent_datasets(limit=4):
    datasets = toolkit.get_action('package_search')(
        data_dict={ 'sort':'metadata_created desc','rows':limit}) 
    return datasets['results']


class ExampleThemePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    plugins.implements(plugins.IConfigurer)

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'example_theme')

    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'example_theme_all_categories_list': all_categories,
                'example_theme_recent_datasets' : most_recent_datasets,
                'example_theme_popular_datasets' : popular_datasets,
                'example_theme_organization_form' : organization_form,
                'example_theme_organization_views' : organization_views,
                }

