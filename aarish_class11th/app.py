import urllib.request
url = 'https://wtlyt-my.sharepoint.com/:x:/g/personal/helal_anwar_wtlyt_onmicrosoft_com/Ebrl6JII8QhKtEiYlOc0XwsBRRZnpADfRXNbsY4SMTsq0Q?rtime=-vVR3CnX3Eg&download=1'


file_Path = 'time_table_leader.xlsx'
urllib.request.urlretrieve(url, file_Path)
