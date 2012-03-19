.. dotSkapes documentation master file, created by
   sphinx-quickstart on Tue Oct 11 13:23:01 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


:mod:`wiki` -- Wiki Documentation
=================================

:Version: |release|
:Source: github.org_
:Bug tracker: 'github.org/issues <`https://github.com/dotSkapes/dotSkapes/issues?sort=created&direction=desc&state=open>'_

Consider wikiSkapes_ an adaptation of Massimo DiPierro's plugin_wiki_.
Basically it adds a RESTful interface and MongoDB backend to plugin_wiki:

* **MongoDB**: Document database
* **RESTful**: Architecture for delivering resources

For complete list of additional parameters reffer to : YXZ.

.. note:: This requires and instance of Web2Py to work

.. note:: This is integrated into the dotSkapes stack (including authentication). It can be found as a stand-alone on github wikiSkapes


Details about implementation
----------------------------

wikiSkapes_ is useful for delivering scientific content

Here is a demo of RESTful call

.. code-block:: python

	beaker_kwargs = dict(key='sources', expire='never', type='memory')

And another of the LaTeX syntax

.. code-block:: python

	beaker_kwargs = dict(key='sources', expire='never', type='memory')





Installation
-----------



API
---

.. autoclass:: modules.savage.graph.base.BaseGraph
    :members: 

.. autofunction:: modules.savage.graph.base.BaseGraph.attachCanvas


Changelog
---------

.. toctree::
   :maxdepth: 2

   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
