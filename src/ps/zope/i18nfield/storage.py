# -*- coding: utf-8 -*-
"""Storage components."""

# zope imports
from persistent.dict import PersistentDict
from zope.interface import implementer

# local imports
from ps.zope.i18nfield import (
    interfaces,
    utils,
)

_marker = dict()
KEY_DEFAULT = u'__default_value'


@implementer(interfaces.II18NDict)
class I18NDict(PersistentDict):
    """A custom dictionnary handling a default value."""

    @classmethod
    def from_text(cls, value):
        """Create a new I18nDict from a str or unicode value."""
        klass = cls()
        klass[KEY_DEFAULT] = value
        return klass

    def __init__(self, *args, **kw):
        super(I18NDict, self).__init__()
        self.update(*args, **kw)
        self.default_language = None
        self.required = False

    def __unicode__(self):
        """Create a string representation of the dictionary by first trying to
        access the value for the current selected language (i.e. from the
        request). If no value exists for this language and the associated
        schema field is required, try to find the best default fallback value
        available.
        """
        lang_req = utils.get_language()
        result = self.get(lang_req, self.get(KEY_DEFAULT))
        if not result and self.required:
            result = self.get_default_value()
        return unicode(result)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __nonzero__(self):
        lang_req = utils.get_language()
        return self.get(lang_req, self.get(KEY_DEFAULT)) is not None

    def __setitem__(self, key, value):
        if not value:
            return
        if key != KEY_DEFAULT and key not in utils.available_languages():
            return
        super(I18NDict, self).__setitem__(key, value)

    def get_default_value(self):
        """Returns the best available default value based on the following
        order:
        1. self.default_language (closest lookup)
        2. Context/application default (adapter/utility)
        3. First non-empty value
        4. None
        """
        result = self.get(self.default_language)
        if not result:
            result = self.get(utils.get_default_language())
            if not result:
                for value in self.values():
                    if value:
                        return value

        return result

    def copy(self):
        result = I18NDict(**self)
        result.default_language = self.default_language
        result.required = self.required
        return result

    def add(self, language, value):
        self[language] = value

    def remove(self, language):
        if language in self:
            del self[language]

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise TypeError('update expected at most 1 arguments, '
                                'got %d' % len(args))
            other = dict(args[0])
            for key in other:
                self[key] = other[key]
        for key in kwargs:
            self[key] = kwargs[key]

    def to_dict(self):
        return dict(**self)
