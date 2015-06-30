#! /usr/bin/python
# -*- coding: utf-8 -*-
from graph_tool.all import *  # @UnusedWildImport
from fuzzywuzzy import process
from itertools import tee
import re

# Ingredients Graph
ig = load_graph('ingredients.xml.gz')

v_name = ig.vertex_properties['name']
v_is_basis = ig.vertex_properties['is_basis']

plural = {u'eis':u'l',
          u'les':u'l',
          #'is':'l',
          u'res':u'r',
          u'ns':u'm',
          u'ães':u'ão',
          u'ões':u'ão',
          u'aes':u'ão',
          u'oes':u'ão',
          u'zes':u'z',
          u'éis':u'el'
          }


def get_choices(vertex_list):
    names = []
    for v in vertex_list:
        names.append(v_name[v].decode('utf-8'))
    return names


def to_singular(string):
    for key in plural.iterkeys():
        pattern = key + '$'
        match = re.search(pattern, string)
        if match:
            string = re.sub(pattern, plural[key], string)
            break
    return string


def find_vertex(query, v_method, singularize=False, graphfilter=None):
    if not query: return
    ig.set_vertex_filter(graphfilter)
    if singularize:
        query = to_singular(query)
    match = None;
    for v in v_method():
        if v_name[v].decode('utf-8')==query:
            match = v
            break
    if not match:
        choices = get_choices(v_method())
        match = process.extractOne(query, choices, score_cutoff=70)
        if match:
            match = find_vertex(match[0], v_method)
    ig.set_vertex_filter(None)
    return match


def find_ingredients(words):
    # words is string list
    # Get 1st word ingredient
    base_v = find_vertex(words[0], ig.vertices, True, v_is_basis)
    if not base_v: return []
    ingredients = [v_name[base_v]]
    # Get last words in graph
    lwords = words[1:]
    for w in lwords:
        v = find_vertex(w, base_v.out_neighbours)
        if v:
            ingredients.append(v_name[v])
            base_v = v
        else:
            break
    return ingredients


ings = find_ingredients([u'batata', u'doce'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'cacau', u'pó'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'óleo', u'coco'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'tahine'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'açúcar', u'demerara'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'farinha', u'aveia'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'beterraba'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'alho'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'azeite'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'salsa'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'limões', u'tahiti'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'semente', u'coentro'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'sal'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'pimenta', u'reino', u'moída', u'hora'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'mexericas']) # ADD
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'maçãs']) # ADD
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'açúcar', u'demerara'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'água'])
for i in ings:
    print i
print '---------'
ings = find_ingredients([u'azetes', u'olivia', u'estra', u'virgens'])
for i in ings:
    print i

