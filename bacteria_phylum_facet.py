#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import matplotlib
# Say, 'the default sans-serif font is Helvetica'
matplotlib.rcParams['font.sans-serif'] = 'Helvetica'
# Then, 'ALWAYS use sans-serif fonts'
matplotlib.rcParams['font.family'] = 'sans-serif'

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
params={
    'axes.labelsize': '14',
    'xtick.labelsize':'14',
    'ytick.labelsize':'14',
    'lines.linewidth':1,
    'legend.fontsize': '14'
}
pylab.rcParams.update(params)

## import matplotlib numpy pandas biom skbio plotnine scipy
import matplotlib
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from biom import load_table
from biom import example_table
from biom import parse_table
import skbio
from sklearn import manifold
from sklearn.decomposition import PCA
from scipy.spatial import distance
from plotnine import *

ups_melt = pd.read_csv('phylum_ra_melt.csv',header=0,index_col=0)
print(ups_melt.head())
### order categorical data using 2 methods
phylum_ordering = ["c__Agaricomycetes","c__Agaricostilbomycetes",
"c__Archaeorhizomycetes","c__Arthoniomycetes","c__Ascomycota_Incertae sedis",
"c__Basidiomycota_Incertae sedis","c__Chytridiomycetes",
"c__Cystobasidiomycetes","c__Dacrymycetes","c__Dothideomycetes",
"c__Entomophthoromycotina_Incertae sedis","c__Eurotiomycetes",
"c__Exobasidiomycetes","c__Glomeromycetes","c__Kickxellomycotina_Incertae sedis",
"c__Lecanoromycetes","c__Leotiomycetes","c__Microbotryomycetes",
"c__Monoblepharidomycetes","c__Mucoromycotina_Incertae sedis",
"c__Neocallimastigomycetes","c__Neolectomycetes","c__Orbiliomycetes",
"c__Pezizomycetes","c__Pezizomycotina_Incertae sedis","c__Pucciniomycetes",
"c__Saccharomycetes","c__Sordariomycetes","c__Taphrinomycetes",
"c__Tremellomycetes","c__Ustilaginomycetes",
"c__Ustilaginomycotina_Incertae sedis","c__Wallemiomycetes",
"c__Zoopagomycotina_Incertae sedis","c__Zygomycetes"]
ups_melt['Class'] = pd.Categorical(ups_melt['Class'], categories=phylum_ordering)
group_ordering = ['CX','JR','HF','TC','HS','XT']
# ups_melt['group'] = pd.Categorical(ups_melt['group'], categories=phylum_ordering)
ups_melt['group'] = ups_melt['group'].astype('category', categories=group_ordering, ordered=True)
#bar plot using plotnine and save figure
a=(ggplot(ups_melt,aes(x='variable', y='value', fill='Class'))+
	theme_grey()+facet_wrap('~group', ncol = 3,scales = 'free_x')+
	theme(strip_text = element_text(size=12,family='sans-serif'),
		strip_background = element_rect(colour='NONE', fill="#BFBFBF"))+
  geom_bar(stat='identity',width=0.94)+
  scale_fill_manual(values=['#CBD588', '#5F7FC7', '#F5B369','#DA5724',
   '#508578', '#CD9BCD','#AD6F3B', '#673770','#C84248', '#652926',
   '#D14285','#666666','#9BE42C','#EDEDEB','#BA82BD','#3078B3',
   '#C77A30','#7AAB8F','#7A8C73','#C7BAA6','#E3D62E','#DEA196',
   '#879EA6','black', '#8A7C64', '#599861','#8569D5','#D45E1A',
   "#3D6654",'#9C8A1C','#5E738F','#F07D3D','#F5E369','#999999',
   '#FC4F61','#A6732B','#F29999'])+
  theme(axis_ticks_major_x = element_blank(), 
    axis_ticks_minor_x = element_blank(), 
    panel_grid_major=element_blank(),panel_grid_minor=element_blank())+
  scale_y_continuous(expand=[0,0])+labs(y='Relative Abundance',x='')+
  theme(axis_text_x=element_blank())+
  theme(axis_text_y=element_text(size=9,color='black',family='sans-serif'), 
  	axis_title=element_text(size=9,color='black',family='sans-serif'), 
  	legend_text= element_text(size=9,color='black',family='sans-serif'), 
  	legend_title= element_text(size=10,color='black',family='sans-serif'))+
  theme(legend_key_width=7,legend_key_height=7)
  )
a.save(filename = 'fungi_paddy_class_facet12_sorted45.pdf', 
	height=3.25, width=3.25, units = 'in')
