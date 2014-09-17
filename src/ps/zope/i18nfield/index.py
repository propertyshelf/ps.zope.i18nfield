# -*- coding: utf-8 -*-
"""I18N index."""

# zope imports
from ps.zope.i18nfield.storage import I18NDict
from ps.zope.i18nfield.utils import get_language, available_languages
from z3c.indexer.index import FieldIndex


class I18NIndex(FieldIndex):

    def clear(self):
        """Initialize forward and reverse mappings."""
        super(I18NIndex, self).clear()
        self._indices = self.family.OO.BTree()

    def documentCount(self):
        """See interface IStatistics"""
        index = self._indices.get(get_language())
        if index:
            return index.documentCount()
        return self._num_docs()

    def wordCount(self):
        """See interface IStatistics"""
        index = self._indices.get(get_language())
        if index:
            return len(index._fwd_index)
        return len(self._fwd_index)

    def sort(self, docids, reverse=False, limit=None):
        index = self._indices.get(get_language())
        if index:
            return index.sort(docids, reverse, limit)

    def applyEq(self, value):
        index = self._indices.get(get_language())
        if index:
            return index.applyEq(value)

    def applyNotEq(self, not_value):
        index = self._indices.get(get_language())
        if index:
            return index.applyNotEq(not_value)

    def applyBetween(self, min_value, max_value, exclude_min=False,
                     exclude_max=False):
        index = self._indices.get(get_language())
        if index:
            return index.applyBetween(
                min_value,
                max_value,
                exclude_min,
                exclude_max,
            )

    def applyGe(self, min_value, exclude_min=False):
        index = self._indices.get(get_language())
        if index:
            return index.applyGe(min_value, exclude_min)

    def applyLe(self, max_value, exclude_max=False):
        index = self._indices.get(get_language())
        if index:
            return index.applyLe(max_value, exclude_max)

    def applyIn(self, values):
        index = self._indices.get(get_language())
        if index:
            return index.applyIn(values)

    def doIndex(self, oid, value):
        """Index a value by its object id."""
        if isinstance(value, I18NDict):
            for lang in available_languages():
                index = self._indices.get(lang)
                if index is None:
                    index = self._indices[lang] = FieldIndex()
                index.index_doc(oid, value.get_for_language(lang))
            return

    def doUnIndex(self, oid):
        """Unindex a value by its object id."""
        index = self._indices.get(get_language())
        if index:
            return index.unindex_doc(oid)
