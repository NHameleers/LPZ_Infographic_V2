import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


import numpy as np
import pandas as pd
from pathlib import Path
import os

orange_colors = ['#F8884A', '#F8B296']
blue_colors = ['#00A2DB', '#ABD1FF']

# bcolor = '#e2ffbc'

def create_pie(val, team='team', size='small', topic='dec',
 fontsize=50, colors=['#00A2DB', '#ABD1FF'], bcolor='bcolor'):
    '''
    team = team or ward
    size = small or large
    topic = dec or med'''

    prop = fm.FontProperties(fname='I:/LPZ/Infographic/fonts/aileron.heavy.otf')

    pie_base = 100
    if topic == 'dec':
        pie_base = 21


    if size == 'nvt':
        fig, ax = plt.subplots()
        ax.pie([0, pie_base], colors=colors, startangle=90, counterclock=False)
        ax.annotate('n.v.t.', (0.05, -.2), fontsize=fontsize, ha='center', fontproperties=prop)
        fig.savefig(f'pypie_{team}_{topic}.png', transparent=True)
    # if size == 'small':
    #     fig, ax = plt.subplots()
    #     ax.pie([2.5, 7.5], colors=colors, startangle=90, counterclock=False)
    #     ax.annotate(f'{val}%'.replace('.', ','), (0.05, -.2), fontsize=fontsize, ha='center', fontproperties=prop)
    #     fig.savefig(f'pypie_{team}_{topic}.png', transparent=True)
    #     
    # elif size == 'large':
    else:
        fig, ax = plt.subplots()
        ax.pie([val, pie_base-val], colors=colors, startangle=90, counterclock=False)
        ax.annotate(f'{val}%'.replace('.', ','), (0.05, -.2), fontsize=fontsize, ha='center', fontproperties=prop)
        fig.savefig(f'pypie_{team}_{topic}.png', transparent=True)    

    plt.close()


if __name__ == '__main__':
    create_pie(7.5, team='team')
    create_pie(5, team='ward')
    create_pie(0, team='team', topic='med')
    create_pie(100, team='ward', topic='med')