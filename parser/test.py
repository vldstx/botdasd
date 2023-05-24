import requests
from bs4 import BeautifulSoup
import json
import sys
import subprocess

token = 'eyJraWQiOiIxdFJzY2tLbmV1d0NqZEg4R2d3MEN6Wk1iVFdTakR1NDNvQnVWM1dBUFlJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJmOTFmMWFiMC1jYTAwLTRhY2ItODEwYy0wZTQ3YjA3YjgxNWUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LWNlbnRyYWwtMS5hbWF6b25hd3MuY29tXC9ldS1jZW50cmFsLTFfMWZIVFBqc3RHIiwiY29nbml0bzp1c2VybmFtZSI6IjMwZDBkOTM3LWQ3YjMtNDM3Ni04MmY2LWFkMjkzOTBjNGEzMCIsImxvY2FsZSI6InJ1IiwiY3VzdG9tOmxhc3RfdXNlcm5hbWVfdHlwZSI6ImVtYWlsIiwib3JpZ2luX2p0aSI6IjQxNzNhOTNjLTIzY2MtNGYyYy1iOTJhLTJmZDg0MzQ0OTZiMiIsImF1ZCI6IjJzNDJmc2FzMThjMGticzU1ZzRjcGpjY3ZmIiwiZXZlbnRfaWQiOiJiMGE5YWNlNi04N2I1LTQzMGMtOTc3Yi0yOGMzOTY0ZGI3MmUiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY4NDk0MjEzOCwiZXhwIjoxNjg0OTQzMDM4LCJpYXQiOjE2ODQ5NDIxMzgsImp0aSI6IjJmMzEwZDc0LWU1NGQtNGY1ZS04YTMyLWU2NWU2NGQyN2I1NSIsImVtYWlsIjoic2x1dHNreWVybmFscmx5Z0BnbWFpbC5jb20ifQ.aHWww6okNImg3f3o5yP2U2ZDe75wTlcnEx4u4rRFJdV6zZoi2oJifJSxWQOpA8GnsW-BoBI3POAl7yvXg9S2eSCTYqDMCsxe42fKnjmwWtGS9yPwBajcN8mH607swjjqOKC8FVnnvipNCSt-CRkF0VvHXy33nwJkGo61JAVB9jCRSt3r47wJge5poMg4_OvQRzVPW52FYniWVkGr0u2kfm9aY9iddiXYR1ZB9_vDqYO1BLcpUaSKWHq-yp_BmVy_J4So3cL8GDSKujz7EG6m66h4kxTO5iYeqyLyiiL_c4rkIYopZljc6gpS8U3Pnoxc9I01c5V4GXOaMk5hmoCs_g'
def parse_ad():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.olx.uz/',
        'Accept-Language': 'en-US',
        'Authorization': f'Bearer {token}',
    }

    completed = False
    while not completed:
        phoneviewpost = f'https://www.olx.uz/api/v1/offers/48320315/phone-view/'
        viewphone = requests.post(phoneviewpost, headers=headers)
        nomer_telephona = f'https://www.olx.uz/api/v1/offers/48320315/limited-phones/'
        zaprosnomera = requests.get(nomer_telephona, headers=headers)
        datanomer = zaprosnomera.json()
        if isinstance(datanomer, dict) and 'error' in datanomer:
            error_message = datanomer['error']['detail']
            if 'подозрительную активность' in error_message:
                print("Ошибка: Подозрительная активность. Повторное выполнение кода...")

            else:
                completed = True  # Выполнение кода завершено, если это не связано с подозрительной активностью
                print(datanomer)
        else:
            completed = True
            print(datanomer)

if __name__ == '__main__':
    parse_ad()