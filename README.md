FetchNovels
===========

[![Dependency Status](https://dependencyci.com/github/wangjiezhe/FetchNovels/badge)](https://dependencyci.com/github/wangjiezhe/FetchNovels)
[![Requirements Status](https://requires.io/github/wangjiezhe/FetchNovels/requirements.svg?branch=master)](https://requires.io/github/wangjiezhe/FetchNovels/requirements/?branch=master)
[![Documentation Status](https://readthedocs.org/projects/docs/badge/?version=latest)](http://fetchnovels.readthedocs.io/en/latest/?badge=latest)
[![Code Health](https://landscape.io/github/wangjiezhe/FetchNovels/master/landscape.svg?style=flat)](https://landscape.io/github/wangjiezhe/FetchNovels/master)

[![PyPI](https://img.shields.io/pypi/v/FetchNovels.svg)](https://pypi.python.org/pypi/FetchNovels)
[![GPL Licence](https://img.shields.io/pypi/l/FetchNovels.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Status](https://img.shields.io/pypi/status/FetchNovels.svg)](https://pypi.python.org/pypi/FetchNovels)
[![Pyversions](https://img.shields.io/pypi/pyversions/FetchNovels.svg)](https://pypi.python.org/pypi/FetchNovels)
[![Downloads](https://img.shields.io/pypi/dm/FetchNovels.svg)](https://pypi.python.org/pypi/FetchNovels)

[![BADGINATOR](https://badginator.herokuapp.com/wangjiezhe/FetchNovels.svg)](https://github.com/defunctzombie/badginator)

Fetch novels from internet.

A renewed version.


Usage
-----

    $ fetchnovels -h
    usage: fetchnovels [-h] [-V] [-u | -d | -l | -ls | -la | -D | -m] [-v] [-r]
                       [-t SECONDS] [-p HOST:PORT | -n]
                       [source] [tid [tid ...]]

    Fetch novels from Internet, and write into file.

    Available sources:
      bgif2, biquge, dzxsw, feizw, haxtxt, jjwxc, klxsw, lou19,
      lwxs, lwxs520, lwxsw, piaotian, piaotiancc, ranwen, shu69,
      shushu8, sto, ttshuba, ttzw, ttzw5, uks5, wdxs, xs365, yfzww,
      yq33, zhaishu8, doubangroup, ...

    positional arguments:
      source                download source
      tid                   id for novels to download

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -u, --update          update novels in the database
      -d, --dump-only       dump only without update
      -l, --list            list novels in the database
      -ls, --list-serial    list serials in the database
      -la, --list-article   list articles in the database
      -D, --delete          delete novels in the database
      -m, --mark-finish     mark novels as finished
      -v, --verbose         show in more detail
      -r, --refresh         refresh novel in the database
      -t SECONDS, --sleep SECONDS
                            sleep several seconds after updating a novel
      -p HOST:PORT, --proxy HOST:PORT
                            use specific proxy
      -n, --no-proxy        do not use any proxies


Todo
----

* [ ] Get novel in forum
* [ ] Login to get token
* [x] Add option to dump directly from database (for no network connection case)
* [x] Fix text width for id and intro


Disclaimer
----------

This software does not produce any actual content.
All data are grabbed from the internet.
