# get TagUI downloads count from GitHub API using requests, updated to TagUI v6.110
import requests

tagui_latest_downloads = 0; tagui_v646_downloads = 0; tagui_v614_downloads = 0; tagui_v6_downloads = 0; tagui_v511_downloads = 0; tagui_v5_rpa_python_downloads = 0;
tagui_latest_linux = 0; tagui_latest_macos = 0; tagui_latest_windows = 0;
tagui_v646_linux = 0; tagui_v646_macos = 0; tagui_v646_windows = 0; tagui_v646_win_exe = 0;
tagui_v614_linux = 0; tagui_v614_macos = 0; tagui_v614_windows = 0;
tagui_v600_linux = 0; tagui_v600_macos = 0; tagui_v600_windows = 0;
tagui_v511_linux = 0; tagui_v511_macos = 0; tagui_v511_windows = 0;
tagui_v5py_linux = 0; tagui_v5py_macos = 0; tagui_v5py_windows = 0;
tagui_excel_addin_v1 = 0; tagui_word_addin_v1 = 0;
tagui_excel_addin_v3 = 0; tagui_word_addin_v3 = 0;
tagui_nodered_docker = 0;

r = requests.get('https://api.github.com/repos/kelaberetiv/TagUI/releases').json()
for n in range(0, len(r)):
    if r[n]['tag_name'] in ['v6.110.0']:
        tagui_latest_downloads = r[n]['assets'][0]['download_count'] + r[n]['assets'][1]['download_count'] + r[n]['assets'][2]['download_count']
        tagui_latest_linux = r[n]['assets'][0]['download_count']
        tagui_latest_macos = r[n]['assets'][1]['download_count']
        tagui_latest_windows = r[n]['assets'][2]['download_count']
    if r[n]['tag_name'] == 'v6.46.0':
        tagui_v646_downloads = r[n]['assets'][1]['download_count'] + r[n]['assets'][2]['download_count'] + r[n]['assets'][3]['download_count'] + r[n]['assets'][4]['download_count']
        tagui_excel_addin_v3 = r[n]['assets'][0]['download_count']
        tagui_v646_linux = r[n]['assets'][1]['download_count']
        tagui_v646_macos = r[n]['assets'][2]['download_count']
        tagui_v646_win_exe = r[n]['assets'][3]['download_count']
        tagui_v646_windows = r[n]['assets'][4]['download_count']
        tagui_word_addin_v3 = r[n]['assets'][5]['download_count']
    if r[n]['tag_name'] == 'v6.14.0':
        tagui_v614_downloads = r[n]['assets'][1]['download_count'] + r[n]['assets'][2]['download_count'] + r[n]['assets'][3]['download_count']
        tagui_excel_addin_v1 = r[n]['assets'][0]['download_count']
        tagui_v614_linux = r[n]['assets'][1]['download_count']
        tagui_v614_macos = r[n]['assets'][2]['download_count']
        tagui_v614_windows = r[n]['assets'][3]['download_count']
        tagui_word_addin_v1 = r[n]['assets'][4]['download_count']
    if r[n]['tag_name'] == 'v6.0.0':
        tagui_v6_downloads = r[n]['assets'][0]['download_count'] + r[n]['assets'][1]['download_count'] + r[n]['assets'][2]['download_count']
        tagui_v600_linux = r[n]['assets'][0]['download_count']
        tagui_v600_macos = r[n]['assets'][1]['download_count']
        tagui_v600_windows = r[n]['assets'][2]['download_count']
    if r[n]['tag_name'] == 'v5.11.0':
        tagui_v511_downloads = r[n]['assets'][0]['download_count'] + r[n]['assets'][1]['download_count'] + r[n]['assets'][2]['download_count']
        tagui_v511_linux = r[n]['assets'][0]['download_count']
        tagui_v511_macos = r[n]['assets'][1]['download_count']
        tagui_v511_windows = r[n]['assets'][2]['download_count']

r = requests.get('https://api.github.com/repos/tebelorg/Tump/releases').json()
for n in range(0, len(r)):
    if r[n]['tag_name'] == 'v1.0.0':
        tagui_v5_rpa_python_downloads = r[n]['assets'][3]['download_count'] + r[n]['assets'][4]['download_count'] + r[n]['assets'][5]['download_count']
        tagui_v5py_linux = r[n]['assets'][3]['download_count']
        tagui_v5py_macos = r[n]['assets'][4]['download_count']
        tagui_v5py_windows = r[n]['assets'][5]['download_count']

try:
    r = requests.get('https://hub.docker.com/v2/repositories/openiap/nodered-tagui')
    tagui_nodered_docker = r.json()['pull_count']
    if type(tagui_nodered_docker) != int:
        tagui_nodered_docker = 0
except:
    tagui_nodered_docker = 0

total_downloads = tagui_latest_downloads + tagui_v646_downloads + tagui_v614_downloads + tagui_v6_downloads + tagui_v511_downloads + tagui_v5_rpa_python_downloads + tagui_nodered_docker
total_linux = tagui_latest_linux + tagui_v646_linux + tagui_v614_linux + tagui_v600_linux + tagui_v511_linux + tagui_v5py_linux
total_macos = tagui_latest_macos + tagui_v646_macos + tagui_v614_macos + tagui_v600_macos + tagui_v511_macos + tagui_v5py_macos
total_windows = tagui_latest_windows + tagui_v646_windows + tagui_v646_win_exe + tagui_v614_windows + tagui_v600_windows + tagui_v511_windows + tagui_v5py_windows

import datetime
query_date = datetime.datetime.now()
print('')
print('total ' + query_date.strftime('%d/%m/%y') + '  - ' + str(total_downloads).ljust(6) + ' (' + str(total_windows) + '/' + str(total_macos) + '/' + str(total_linux) + ')')
print('===========================================')
print('latest downloads - ' + str(tagui_latest_downloads).ljust(6) + ' (' + str(tagui_latest_windows) + '/' + str(tagui_latest_macos) + '/' + str(tagui_latest_linux) + ')')
print('v6.46 downloads - ' + str(tagui_v646_downloads).ljust(6) + ' (' + str(tagui_v646_windows + tagui_v646_win_exe) + '/' + str(tagui_v646_macos) + '/' + str(tagui_v646_linux) + ')')
print('v6.14 downloads - ' + str(tagui_v614_downloads).ljust(6) + ' (' + str(tagui_v614_windows) + '/' + str(tagui_v614_macos) + '/' + str(tagui_v614_linux) + ')')
print('v6.00 downloads - ' + str(tagui_v6_downloads).ljust(6) + ' (' + str(tagui_v600_windows) + '/' + str(tagui_v600_macos) + '/' + str(tagui_v600_linux) + ')')
print('v5.11 downloads - ' + str(tagui_v511_downloads).ljust(6) + ' (' + str(tagui_v511_windows) + '/' + str(tagui_v511_macos) + '/' + str(tagui_v511_linux) + ')')
print('v5_py downloads - ' + str(tagui_v5_rpa_python_downloads).ljust(6) + ' (' + str(tagui_v5py_windows) + '/' + str(tagui_v5py_macos) + '/' + str(tagui_v5py_linux) + ')')
print('docker downloads - ' + str(tagui_nodered_docker))
print('')
print('* windows/macos/linux breakdown in brackets')
print('')

csv_line = ''
csv_line = query_date.strftime('%d/%m/%y')
csv_line = csv_line + ',' + str(total_downloads)
csv_line = csv_line + ',' + str(total_windows)
csv_line = csv_line + ',' + str(total_macos)
csv_line = csv_line + ',' + str(total_linux)
csv_line = csv_line + ',' + str(tagui_v5_rpa_python_downloads)
csv_line = csv_line + ',' + str(tagui_v5py_windows)
csv_line = csv_line + ',' + str(tagui_v5py_macos)
csv_line = csv_line + ',' + str(tagui_v5py_linux)
csv_line = csv_line + ',' + str(tagui_v511_downloads)
csv_line = csv_line + ',' + str(tagui_v511_windows)
csv_line = csv_line + ',' + str(tagui_v511_macos)
csv_line = csv_line + ',' + str(tagui_v511_linux)
csv_line = csv_line + ',' + str(tagui_v6_downloads)
csv_line = csv_line + ',' + str(tagui_v600_windows)
csv_line = csv_line + ',' + str(tagui_v600_macos)
csv_line = csv_line + ',' + str(tagui_v600_linux)
csv_line = csv_line + ',' + str(tagui_v614_downloads)
csv_line = csv_line + ',' + str(tagui_v614_windows)
csv_line = csv_line + ',' + str(tagui_v614_macos)
csv_line = csv_line + ',' + str(tagui_v614_linux)
csv_line = csv_line + ',' + str(tagui_v646_downloads)
csv_line = csv_line + ',' + str(tagui_v646_windows)
csv_line = csv_line + ',' + str(tagui_v646_win_exe)
csv_line = csv_line + ',' + str(tagui_v646_macos)
csv_line = csv_line + ',' + str(tagui_v646_linux)
csv_line = csv_line + ',' + str(tagui_nodered_docker)
csv_line = csv_line + ',' + str(tagui_latest_downloads)
csv_line = csv_line + ',' + str(tagui_latest_windows)
csv_line = csv_line + ',' + str(tagui_latest_macos)
csv_line = csv_line + ',' + str(tagui_latest_linux)
csv_line = csv_line + ',,' + ',,,,' + ',,,,' + ',,,,' + ',,,,' + ',,,,' + ',,,,' + ',,,,' + ',,,,'

import os
if not os.path.isfile('tagui_downloads.csv'):
    f = open('tagui_downloads.csv', 'w')
    f.write('date,total_downloads,total_windows,total_macos,total_linux,tagui_v5_rpa_python_downloads,tagui_v5py_windows,tagui_v5py_macos,tagui_v5py_linux,tagui_v511_downloads,tagui_v511_windows,tagui_v511_macos,tagui_v511_linux,tagui_v6_downloads,tagui_v600_windows,tagui_v600_macos,tagui_v600_linux,tagui_v614_downloads,tagui_v614_windows,tagui_v614_macos,tagui_v614_linux,tagui_v646_downloads,tagui_v646_windows,tagui_v646_win_exe,tagui_v646_macos,tagui_v646_linux,tagui_nodered_docker,tagui_latest_downloads,tagui_latest_windows,tagui_latest_macos,tagui_latest_linux,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,' + '\n')
    f.close()

f = open('tagui_downloads.csv', 'a')
f.write(csv_line + '\n')
f.close()
