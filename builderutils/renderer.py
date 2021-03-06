#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jinja2


class Renderer(object):
    def __init__(self):
        pass

    def render_j2_template(self, templateFile, searchPath, renderObj):
        """ The API will render a Jinja2 template

        :type  templateFile:  String
        :param templateFile: Name of the template file

        :type  searchPath: String
        :param searchPath: Path to the templates directory

        :type  renderObj:  dict
        :param renderObj: Dictionary object to substitute the template vars

        :returns:
        """
        template_loader = jinja2.FileSystemLoader(searchpath=searchPath)
        env = jinja2.Environment(
            loader=template_loader, trim_blocks=True, lstrip_blocks=True
        )
        template = env.get_template(templateFile)
        renderedData = template.render(renderObj)

        return renderedData

    def render_j2_template_string(self, templateString, renderObj):
        """ one line description

        :type  argument:  data type
        :param  argument:  description

        :returns:
        """
        env = jinja2.Environment(
            loader=jinja2.BaseLoader, trim_blocks=True, lstrip_blocks=True
        )
        template = env.from_string(templateString)
        renderedData = template.render(renderObj)
        return renderedData
