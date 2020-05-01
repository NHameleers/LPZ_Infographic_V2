import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


import numpy as np
import pandas as pd
from pathlib import Path
import os
import sys

import sqlite3




unit_of_analysis = ''

if len(sys.argv) < 2:
    print("Usage: python create_all_pies.py unit_of_analysis")
    print("Unit of analysis can be one of: team, locatie, organisatie")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Usage: python create_all_pies.py unit_of_analysis")
    print("Unit of analysis can be one of: team, locatie, organisatie")
    sys.exit(1)
else:
    unit_of_analysis = sys.argv[1]

data_path = f'../Data/LPZ_{unit_of_analysis}data.csv'


OUTPUT_DIR = f'../TeamInfographics/posters/static/images/{unit_of_analysis}'
Path(OUTPUT_DIR).mkdir(exist_ok=True)



conn = sqlite3.connect('../TeamInfographics/db.sqlite3')  # pass your db url




orange_colors = ['#F8884A', '#F8B296']
blue_colors = ['#00A2DB', '#ABD1FF']
red_colors = ['#ff0000', '#F8884A']
orange_colors_2 = ['#E84E10', '#F8884A']

# bcolor = '#e2ffbc'

def create_pie(val, teamnr, team='team', size='small', topic='dec',
 fontsize=80, colors=['#00A2DB', '#ABD1FF'], bcolor='bcolor', outputdir = ''):
    '''
    team = team or ward
    size = small or large
    topic = dec or med'''

    # prop = fm.FontProperties(fname='F:/2020_01_06_Selectie_backup_I-schijf/LPZ/Infographic/fonts/aileron.heavy.otf')
    prop = fm.FontProperties(fname='../TeamInfographics/posters/static/fonts/Advent_Pro/AdventPro-SemiBold.ttf')

    pie_base = 100
    if topic == 'dec':
        pie_base = 21


    if val == ' ':
        fig, ax = plt.subplots()
        ax.pie([0, pie_base], colors=colors, startangle=90, counterclock=False)
        ax.annotate('n.v.t.', (0.05, -.2), fontsize=fontsize, ha='center', fontproperties=prop)
        fig.savefig(f'{outputdir}/{teamnr}/pypie_{team}_{topic}.png', transparent=True)

    else:
        fig, ax = plt.subplots()
        val = float(val)
        ax.pie([val, pie_base-val], colors=colors, startangle=90, counterclock=False)
        val_rounded = int(round(val, 0))
        ax.annotate(f'{val_rounded}%'.replace('.', ','), (0.05, -.2), fontsize=fontsize, ha='center', fontproperties=prop)
        fig.savefig(f'{outputdir}/{teamnr}/pypie_{team}_{topic}.png', transparent=True)    

    plt.close()


if __name__ == '__main__':



    df = pd.read_sql(f'SELECT * FROM Lpz2019{unit_of_analysis.title()}s', conn)
    df['team_index'] = range(1, df.shape[0] + 1)
    df = df.set_index('team_index')

    suffix_of_main_value = 'mean_team'
    suffix_of_benchmark = 'mean_type_ward'

    if unit_of_analysis == 'locatie':
        suffix_of_main_value = 'mean_locatie'
        suffix_of_benchmark = 'mean_van_org'
    elif unit_of_analysis == 'organisatie':
        suffix_of_main_value = 'mean_organisatie'
        suffix_of_benchmark = 'mean_van_ALLE_orgs'
    

    # create 4 pie-charts for each team and save them in static/images/teamnr folders
    for team_index in range(1, df.shape[0] + 1):

        print(f'Creating pie charts for {unit_of_analysis} {team_index} out of {df.shape[0]}')

        Path(f'../TeamInfographics/posters/static/images/{unit_of_analysis}/{team_index}').mkdir(exist_ok=True)


        create_pie(df.loc[team_index, f'D_QF_PU_Prev_cat2_{suffix_of_main_value}'],
         team_index,
         team='team',
          colors=orange_colors_2,
           outputdir=OUTPUT_DIR)

        create_pie(df.loc[team_index, f'D_QF_PU_Prev_cat2_{suffix_of_benchmark}'],
         team_index,
         team='ward',
          colors=orange_colors_2,
           outputdir=OUTPUT_DIR)

        create_pie(df.loc[team_index, f'D_QF_Prev_MR2_{suffix_of_main_value}'],
         team_index,
         team='team',
         topic='med',
         colors=blue_colors,
         outputdir=OUTPUT_DIR)

        create_pie(df.loc[team_index, f'D_QF_Prev_MR2_{suffix_of_benchmark}'],
         team_index,
         team='ward',
         topic='med',
         colors=blue_colors,
         outputdir=OUTPUT_DIR)