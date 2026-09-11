"""Retarget edit actions on generated reference pages to the YAML source."""


def on_page_context(context, page, config, nav):
    source = page.meta.get("source_yaml")
    if source:
        page.edit_url = f"{config['repo_url']}/edit/master/{source}"
    return context
