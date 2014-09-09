# -*- coding: utf-8 -*-
"""Widget interface definitions."""

# zope imports
from z3c.form.interfaces import (
    ITextAreaWidget,
    ITextWidget,
    IWidget,
)
from zope import schema


class II18NWidget(IWidget):
    """I18N base widget."""

    langs = schema.List(
        title=u'Languages',
        description=u'List of languages supported by the given widget.',
        required=True,
    )


class II18NTextWidget(II18NWidget, ITextWidget):
    """I18N text widget."""


class II18NTextAreaWidget(II18NWidget, ITextAreaWidget):
    """I18N textarea widget."""
