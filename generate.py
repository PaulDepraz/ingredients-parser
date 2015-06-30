#! /usr/bin/python
# -*- coding: utf-8 -*-
from graph_tool.all import *

# Ingredients Graph
ig =  Graph()
v_name = ig.new_vertex_property("string")
v_is_basis = ig.new_vertex_property("bool")
e_is_substitute = ig.new_edge_property("bool")
# Use gi.set_edge_filter(e_is_substitute) to filter

# root node
root = ig.add_vertex()
v_name[root] = 'ingrediente'


def add_in_node(target, son_meta):
    v = ig.add_vertex()
    ig.add_edge(v, target)
    v_name[v] = son_meta
    return v


def add_out_node(source, par_meta):
    v = ig.add_vertex()
    ig.add_edge(source, v)
    v_name[v] = par_meta
    return v

def add_ingredient(out_node, par_meta):
    v = ig.add_vertex()
    ig.add_edge(out_node, v)
    v_name[v] = par_meta
    v_is_basis[v] = 1
    return v


def add_substitute(v1, v2):
    e1 = ig.add_edge(v1, v2)
    e2 = ig.add_edge(v2, v1)
    e_is_substitute[e1] = 1
    e_is_substitute[e2] = 1


#----------------------------------------------------------------------------
# -== CATEGORIAS ==--
# ingredient < - verdura
verdura = add_out_node(root, 'verdura')
legume = add_out_node(root, 'legume')
fruta = add_out_node(root, 'fruta')
tempero = add_out_node(root, 'tempero')
laticinio = add_out_node(root, 'laticínio')
grao = add_out_node(root, 'grão')
farinha = add_out_node(root, 'farinha')
semente = add_out_node(root, 'semente')
oleo = add_out_node(root, 'óleo')
industrializado = add_out_node(root, 'industrializado')

#------------------------------------------------
# -== INGREDIENTES ==--
# ALFACE
alface = add_ingredient(verdura, 'alface')
add_out_node(alface, 'crespa')
add_out_node(alface, 'lisa')
add_out_node(alface, 'roxa')
# AGRIAO
add_out_node(verdura, 'agrião')
# BATATA
batata = add_ingredient(legume, 'batata')
add_out_node(batata, 'asterix')
add_out_node(batata, 'baroa')
add_out_node(batata, 'bolinha')
add_out_node(batata, 'doce')
add_out_node(batata, 'inglesa')
add_out_node(batata, 'yacon')
# CACAU
cacau = add_ingredient(fruta, 'cacau')
add_out_node(cacau, 'pó')
add_out_node(cacau, 'poupa')
add_out_node(cacau, 'semente')
# COCO
coco = add_ingredient(fruta, 'coco')
add_out_node(coco, 'seco')
add_out_node(coco, 'verde')
add_out_node(coco, 'ralado')
# OLEO
oleo_ = add_ingredient(oleo, 'óleo')
add_out_node(oleo_, 'girassol')
add_out_node(oleo_, 'canola')
add_out_node(oleo_, 'soja')
add_out_node(oleo_, 'coco')
# SEMENTE
semente_ = add_ingredient(semente, 'semente')
add_out_node(semente_, 'girassol')
add_out_node(semente_, 'mostarda')
add_out_node(semente_, 'cacau')
add_out_node(semente_, 'coentro')
# GERGELIM
gergelim = add_ingredient(semente, 'gergelim')
gp = add_out_node(gergelim, 'pasta')
add_out_node(gergelim, 'torrado')
# TAHINE
tahine = add_ingredient(industrializado, 'tahine')
add_substitute(tahine, gp)
# ACUCAR
acucar = add_ingredient(industrializado, 'açúcar')
add_out_node(acucar, 'demerara')
add_out_node(acucar, 'mascavo')
# AVEIA
aveia = add_out_node(industrializado, 'aveia')
add_out_node(aveia, 'flocos')
# FARINHA
farinha_ = add_ingredient(industrializado, 'farinha')
av = add_out_node(farinha_, 'aveia')
add_out_node(av, 'integral')
mi = add_out_node(farinha_, 'milho')
add_out_node(mi, 'fina')
add_out_node(farinha_, 'trigo')
add_out_node(farinha_, 'mandioca')
add_out_node(farinha_, 'quinua')
add_out_node(farinha_, 'rosca')
# FERMENTO
fermento = add_ingredient(industrializado, 'fermento')
add_out_node(fermento, 'fresco')
add_out_node(fermento, 'pó')
# BETERRABA
add_ingredient(legume, 'beterraba')
# ALHO
alho = add_ingredient(tempero, 'alho')
add_out_node(alho, 'descascado')
add_out_node(alho, 'pasta')
add_out_node(alho, 'poró')
# AZEITE
azeite = add_ingredient(oleo, 'azeite')
ol = add_out_node(azeite, 'oliva')
add_out_node(ol, 'virgem')
ex = add_out_node(ol, 'extra')
add_out_node(ex, 'virgem')
add_out_node(azeite, 'dendê')
# SALSA
salsa = add_ingredient(tempero, 'salsa')
salsinha = add_out_node(tempero, 'salsinha')
add_substitute(salsa, salsinha)
# COENTRO
add_ingredient(tempero, 'coentro')
# LIMAO
limao = add_ingredient(fruta, 'limão')
add_out_node(limao, 'siciliano')
ga = add_out_node(limao, 'galego')
ta = add_out_node(limao, 'taiti')
add_substitute(ga, ta)
ro = add_out_node(limao, 'rosa')
cr = add_out_node(limao, 'cravo')
add_substitute(ro, cr)
# LIMA
lima = add_ingredient(fruta, 'lima')
add_out_node(lima, 'persia')
# SAL
sal = add_ingredient(industrializado, 'sal')
add_out_node(sal, 'temperado')
io = add_out_node(sal, 'iodado')
ro = add_out_node(sal, 'rosa')
add_substitute(io, ro)
# PIMENTA
pimenta = add_ingredient(tempero, 'pimenta')
add_out_node(pimenta, 'biquinho')
add_out_node(pimenta, 'bode')
re = add_out_node(pimenta, 'reino')
add_out_node(re, 'pó')
# PIMENTAO
pimentao = add_ingredient(tempero, 'pimentão')
add_out_node(pimentao, 'amarelo')
add_out_node(pimentao, 'verde')
add_out_node(pimentao, 'vermelho')

# -----------------------------------------------------------------
# Save properties
ig.vertex_properties['name'] = v_name
ig.vertex_properties['is_basis'] = v_is_basis
ig.edge_properties['is_substitute'] = e_is_substitute
# Draw image
graph_draw(ig, vertex_text=ig.vertex_properties['name'], 
            vertex_font_size=11,
            edge_pen_width=5,
            vertex_size=2,
            output_size=(3000, 1400), 
            edge_color=e_is_substitute,
            output="ingredients.png")
# Export to compressed xml
ig.save("ingredients.xml.gz")
ig.save('ingredients.graphml', fmt='graphml')