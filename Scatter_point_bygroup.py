"""
@author: Jianshu Zhao (zhaojs16@mails.tsinghua.edu.cn)
"""
# pca analysis of fungal community
import matplotlib
# Say, "the default sans-serif font is Helvetica"
matplotlib.rcParams['font.sans-serif'] = "Helvetica"
# Then, "ALWAYS use sans-serif fonts"
matplotlib.rcParams['font.family'] = "sans-serif"

import numpy as np
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
params={
    'axes.labelsize': '14',
    'xtick.labelsize':'14',
    'ytick.labelsize':'14',
    'lines.linewidth':1,
    'legend.fontsize': '14',
    'figure.figsize'   : '6, 5.5'
}

pylab.rcParams.update(params)



import math
import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *

# read dataframe and check
bacteria_ddr_group = pd.read_csv('fungal_bary_all_data_scale_group_181.csv',header=0,index_col=0)
category_ordering = ['Regional','Meso','Local']
bacteria_ddr_group['category'] = pd.Categorical(bacteria_ddr_group['category'], categories=category_ordering)
plot_fungi_ddr=(ggplot(bacteria_ddr_group,aes(x='np.log10(geodis)',y='np.log10(1-bray_all)'))+
	geom_point(aes(color='category'),size=0.45)+
	stat_smooth(aes(group='category'),method='lm',color='black',size=1.35)+
	scale_color_manual(values=['#557DAD','#B4CBDD','#92BFA0'])+
    theme_matplotlib()+
    theme(panel_border=element_rect(size=1,color='black'))+theme(axis_ticks_minor=element_blank())+
    theme(legend_position=(0.24,0.25),legend_entry_spacing=0.01)+
    theme(legend_background=element_rect(alpha=0))+
	theme(axis_text=element_text(size=12,color='black',family='sans-serif'),axis_title=element_text(size=13,color='black',family='sans-serif'),
		legend_text= element_text(size=11,color='black',family='sans-serif'),legend_title= element_text(size=11,color='black',family='sans-serif'))
  )+labs(x="ln(geographic distance (m))",y="ln(community similarity)")+theme(legend_title=element_blank())

plot_fungi_ddr.save('paddy_fungi_ddr_scale_matplotlib111.pdf',width=4.75, height=3.9)






## theme_bw style
plot_fungi_ddr=(ggplot(bacteria_ddr_group,aes(x='np.log10(geodis)',y='np.log10(1-bray_all)'))+
    geom_point(aes(color='category'),size=0.45)+
    stat_smooth(aes(group='category'),method='lm',color='black',size=1.5)+
    scale_color_manual(values=['#557DAD','#B4CBDD','#92BFA0'])+#stat_smooth(method='lm',color='#D9D9D9',se=False)+
    #theme(axis_line=element_line(size=1.5))+
    theme_linedraw()+theme(panel_grid=element_blank())+theme(panel_border=element_rect(size=1))+
    theme(legend_position=(0.24,0.25),legend_entry_spacing=0.01)+theme(legend_background=element_rect(alpha=0))+
    theme(axis_text=element_text(size=12,color='black',family='sans-serif'),axis_title=element_text(size=13,color='black',family='sans-serif'),
        legend_text= element_text(size=11,color='black',family='sans-serif'),legend_title= element_text(size=11,color='black',family='sans-serif'))
  )+labs(x="ln(geographic distance (m))",y="ln(community similarity)")+theme(legend_title=element_blank())

plot_fungi_ddr.save('paddy_fungi_ddr_scale112_small_bw.pdf',width=4.74, height=3.9)




plot_fungi_ddr=(ggplot(bacteria_ddr_group,aes(x='np.log10(geodis)',y='np.log10(1-bray_all)'))+
    geom_point(aes(color='category'),size=0.45)+
    stat_smooth(aes(group='category'),method='lm',color='black',size=1.5)+
    scale_color_manual(values=['#557DAD','#B4CBDD','#92BFA0'])+#stat_smooth(method='lm',color='#D9D9D9',se=False)+
    #theme(axis_line=element_line(size=1.5))+
    theme_minimal()+theme(panel_border=element_rect(color='#EDEDED'))+
    theme(legend_position=(0.24,0.25),legend_entry_spacing=0.01)+theme(legend_background=element_rect(alpha=0))+
    theme(axis_text=element_text(size=12,color='black',family='sans-serif'),axis_title=element_text(size=13,color='black',family='sans-serif'),
        legend_text= element_text(size=11,color='black',family='sans-serif'),legend_title= element_text(size=11,color='black',family='sans-serif'))
  )+labs(x="ln(geographic distance (m))",y="ln(community similarity)")+theme(legend_title=element_blank())

plot_fungi_ddr.save('paddy_fungi_ddr_scale112_small_minimal.pdf',width=4.75, height=3.9)
