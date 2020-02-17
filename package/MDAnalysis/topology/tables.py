# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# MDAnalysis --- https://www.mdanalysis.org
# Copyright (c) 2006-2017 The MDAnalysis Development Team and contributors
# (see the file AUTHORS for the full list of names)
#
# Released under the GNU Public Licence, v2 or any higher version
#
# Please cite your use of MDAnalysis in published work:
#
# R. J. Gowers, M. Linke, J. Barnoud, T. J. E. Reddy, M. N. Melo, S. L. Seyler,
# D. L. Dotson, J. Domanski, S. Buchoux, I. M. Kenney, and O. Beckstein.
# MDAnalysis: A Python package for the rapid analysis of molecular dynamics
# simulations. In S. Benthall and S. Rostrup editors, Proceedings of the 15th
# Python in Science Conference, pages 102-109, Austin, TX, 2016. SciPy.
# doi: 10.25080/majora-629e541a-00e
#
# N. Michaud-Agrawal, E. J. Denning, T. B. Woolf, and O. Beckstein.
# MDAnalysis: A Toolkit for the Analysis of Molecular Dynamics Simulations.
# J. Comput. Chem. 32 (2011), 2319--2327, doi:10.1002/jcc.21787
#

"""
MDAnalysis topology tables
==========================

The module contains static lookup tables for atom typing etc. The
tables are dictionaries that are indexed by the element.
Following dictionaries are available: `atomelements`, `masses`, `vdwradii` and `names`.

Additional element numbers (Z) can be converted to the symbols (SYMB) and vice versa
using the two dictionaries `Z2SYMB` and `SYMB2Z`.

The content of the raw .json files can be accessed under `raw_atom_base`, `raw_atomnames_elements` and
`raw_vdw_radii`. These directories contain besides the `data` field selected meta-data
(`_source`, `_source_url`, `_comment`, `_last_update`).

"""

from __future__ import absolute_import
import json
import os

elements = ['H',
            'LI', 'BE', 'B', 'C', 'N', 'O', 'F',
            'NA', 'MG', 'AL', 'P', 'SI', 'S', 'CL',
            'K']

table_folder = __file__.replace('tables.py', '')

with open(os.path.join(table_folder, 'tables', 'atom_base.json'), 'r') as table_file:
    raw_atom_base = json.load(table_file)

with open(os.path.join(table_folder, 'tables', 'atomnames_elements.json'), 'r') as table_file:
    raw_atomnames_elements = json.load(table_file)

with open(os.path.join(table_folder, 'tables', 'vdw_radii.json'), 'r') as table_file:
    raw_vdw_radii = json.load(table_file)

atomelements = raw_atomnames_elements['data']

masses = {key: element['atomic_mass'] for key, element in raw_atom_base['data'].items()}
masses['DUMMY'] = 0.0

names = {key: element['name'] for key, element in raw_atom_base['data'].items()}

vdwradii = {key: element['vdw_radius'] for key, element in raw_atom_base['data'].items() if 'vdw_radius' in element}
vdwradii.update(raw_vdw_radii['data'])  # add additional vdw_radii

SYMB2Z = {key: element['Z'] for key, element in raw_atom_base['data'].items()}
Z2SYMB = {element['Z']: key for key, element in raw_atom_base['data'].items()}
