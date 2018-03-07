from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.admin.rich_text.editors.draftail.features import InlineStyleFeature
from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def register_monospace_feature(features):
    """
    Registering the `monospace` feature, which uses the `CODE` Draft.js inline style type,
    and is stored as HTML with a `<code>` tag.
    """
    feature_name = 'monospace'
    draftail_type = 'CODE'
    html_tag = 'code'

    # Configure how Draftail handles the feature in its toolbar.
    control = {
        'type': draftail_type,
        'label': '{ }',
        'description': 'Monospace',
    }

    # Call register_editor_plugin to register the configuration for Draftail.
    features.register_editor_plugin(
        'draftail', feature_name, InlineStyleFeature(control)
    )

    # Configure the content transform from the DB to the editor and back.
    db_conversion = {
        'from_database_format': {html_tag: InlineStyleElementHandler(draftail_type)},
        'to_database_format': {'style_map': {draftail_type: html_tag}},
    }

    # Call register_converter_rule to register the content transformation conversion.
    features.register_converter_rule('contentstate', feature_name, db_conversion)
