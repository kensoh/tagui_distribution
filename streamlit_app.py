# get TagUI downloads count from GitHub API using requests
import requests

tagui_v646_downloads = 0; tagui_v614_downloads = 0; tagui_v6_downloads = 0; tagui_v511_downloads = 0; tagui_v5_rpa_python_downloads = 0;

r = requests.get('https://api.github.com/repos/kelaberetiv/TagUI/releases').json()
for n in range(0, len(r)):
    if r[n]['tag_name'] == 'v6.46.0':
        tagui_v646_downloads = r[n]['assets'][1]['download_count'] + r[n]['assets'][2]['download_count'] + r[n]['assets'][3]['download_count'] + r[n]['assets'][4]['download_count']
    if r[n]['tag_name'] == 'v6.14.0':
        tagui_v614_downloads = r[n]['assets'][1]['download_count'] + r[n]['assets'][2]['download_count'] + r[n]['assets'][3]['download_count']
    if r[n]['tag_name'] == 'v6.0.0':
        tagui_v6_downloads = r[n]['assets'][0]['download_count'] + r[n]['assets'][1]['download_count'] + r[n]['assets'][2]['download_count']
    if r[n]['tag_name'] == 'v5.11.0':
        tagui_v511_downloads = r[n]['assets'][0]['download_count'] + r[n]['assets'][1]['download_count'] + r[n]['assets'][2]['download_count']

r = requests.get('https://api.github.com/repos/tebelorg/Tump/releases').json()
for n in range(0, len(r)):
    if r[n]['tag_name'] == 'v1.0.0':
        tagui_v5_rpa_python_downloads = r[n]['assets'][3]['download_count'] + r[n]['assets'][4]['download_count'] + r[n]['assets'][5]['download_count']

total_downloads = tagui_v646_downloads + tagui_v614_downloads + tagui_v6_downloads + tagui_v511_downloads + tagui_v5_rpa_python_downloads

# get users distribution for TagUI optional chrome extension
import pandas as pd

df = pd.read_csv('chrome_extension_users_mar_2022.csv', header = 1).tail(1).drop(columns=['Date'])

# expand 2-letter header country codes to country names using pycountry
import pycountry

for n in range(1, len(df.columns)):
    for c in range(0, len(list(pycountry.countries))):
        if df.columns[n] == list(pycountry.countries)[c].alpha_2:
            df = df.rename(columns = {df.columns[n]: list(pycountry.countries)[c].name})

# set download counts for countries according to users distribution
distribution_multiplier = float(total_downloads) / float(sum(df.values[0].tolist()))
downloads_distribution = [int(element * distribution_multiplier) for element in df.values[0].tolist()]

# plot map of TagUI downloads globally using plotly
import plotly.graph_objects as go

fig = go.Figure(data = go.Choropleth(
    locations = df.columns.tolist(),
    z = downloads_distribution,
    locationmode = 'country names',
    colorbar_title = "downloads",
    colorscale = 'Reds'
))
    
fig.update_layout(
    title_text = 'TagUI Downloads (v5 & above)',
    margin = {'r': 0, 't': 50, 'l': 0,'b': 0},
    geo_scope = 'world',
    geo_resolution = 50
)

#fig.show()

# use streamlit sharing to serve plot
import streamlit as st
st.plotly_chart(fig, use_container_width = True)
