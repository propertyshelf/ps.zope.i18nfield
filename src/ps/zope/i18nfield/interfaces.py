# -*- coding: utf-8 -*-
"""Schema interfaces."""

# zope imports
from zope.i18n.interfaces import ILanguageAvailability as \
    IBaseLanguageAvailability
from zope.interface import Interface
from zope.schema import interfaces


class ILanguageAvailability(IBaseLanguageAvailability):
    """A list of available languages."""

    def getDefaultLanguage(combined=False):
        """Return the system default language."""

    def getLanguages(combined=False):
        """Return a sequence of Language objects for available languages."""

    def getLanguageListing(combined=False):
        """Return a sequence of language code and language name tuples."""


class II18NField(interfaces.IDict):
    """Marker interface used to identify I18N properties."""


class II18NTextLineField(II18NField):
    """Marker interface used to identify I18N textline properties."""


class II18NTextField(II18NField):
    """Marker interface used to identify I18N text properties."""


class II18NDictReader(Interface):
    """Default value dict reading methods"""

    def __unicode__():
        """Create a unicode representation of the dictionary."""

    def __str__():
        """Create a string representation of the dictionary."""

    def get(key, default=None):
        """Get given key from dict, or default if key is missing"""

    def keys():
        """Get dict keys"""

    def values():
        """Get dict values"""

    def items():
        """Get dict items"""

    def copy():
        """Return an exact copy of the given dict, including default value"""


class II18NDictWriter(Interface):
    """Default value dict writing methods"""

    def __delitem__(key):
        """Delete specified key from dict"""

    def __setitem__(key, value):
        """Set specified key with specified value"""

    def clear():
        """Remove all dict values"""

    def update(b):
        """Update dict with values from specified dict"""

    def setdefault(key, failobj=None):
        """Get given key from dict or set it with specified value"""

    def pop(key, *args):
        """Remove given key from dict and return its value"""

    def popitem():
        """Pop last item from dict"""


class II18NDict(II18NDictReader, II18NDictWriter):
    """Default value dict marker interface"""
