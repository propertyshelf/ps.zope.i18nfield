# -*- coding: utf-8 -*-
"""Helper methods for the I18N field."""

# python imports
import codecs


def uninvl(value, default=u''):
    """Get specified value converted to unicode, or an empty unicode string if
    value is empty

    :param value: [required] text to be checked
    :type value: str or unicode
    :param default: default value
    :return: value, or default if value is empty
    :rtype: unicode
    """
    try:
        if isinstance(value, unicode):
            return value
        return codecs.decode(value or default)
    except:
        return codecs.decode(value or default, 'latin1')


def get_language():
    return u'en'


def get_default_language():
    return u'en'


def available_languages():
    return [u'en', ]
