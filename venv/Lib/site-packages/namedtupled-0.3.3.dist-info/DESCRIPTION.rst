
.. image:: https://travis-ci.org/brennv/namedtupled.svg?branch=master
    :target: https://travis-ci.org/brennv/namedtupled
.. image:: https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5-blue.svg
.. image:: https://img.shields.io/codecov/c/github/brennv/namedtupled.svg
    :target: https://codecov.io/gh/brennv/namedtupled

Source: `https://github.com/brennv/namedtupled`_

Docs: `https://namedtupled.readthedocs.io`_

`namedtuples`_ are immutable, performant and classy. **namedtupled** is
a lightweight wrapper for recursively creating namedtuples from nested
dicts, lists, json and yaml. Inspired by `hangtwenty`_.

Installation
============

.. code:: bash

    pip install namedtupled

Getting started
===============

.. code:: python

    import namedtupled

    data = {'binks': {'says': 'meow'}}
    cat = namedtupled.map(data)

    cat  # NT(binks=NT(says='meow'))

    cat.binks.says  # 'meow'

.. _namedtuples: https://docs.python.org/3/library/collections.html
.. _hangtwenty: https://gist.github.com/hangtwenty/5960435
.. _https://github.com/brennv/namedtupled: https://github.com/brennv/namedtupled
.. _https://namedtupled.readthedocs.io: https://namedtupled.readthedocs.io


