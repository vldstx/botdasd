import requests
from bs4 import BeautifulSoup
import json
import sys
import subprocess
import time
import re

token = 'eyJraWQiOiIxdFJzY2tLbmV1d0NqZEg4R2d3MEN6Wk1iVFdTakR1NDNvQnVWM1dBUFlJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJmOTFmMWFiMC1jYTAwLTRhY2ItODEwYy0wZTQ3YjA3YjgxNWUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LWNlbnRyYWwtMS5hbWF6b25hd3MuY29tXC9ldS1jZW50cmFsLTFfMWZIVFBqc3RHIiwiY29nbml0bzp1c2VybmFtZSI6IjMwZDBkOTM3LWQ3YjMtNDM3Ni04MmY2LWFkMjkzOTBjNGEzMCIsImxvY2FsZSI6InJ1IiwiY3VzdG9tOmxhc3RfdXNlcm5hbWVfdHlwZSI6ImVtYWlsIiwib3JpZ2luX2p0aSI6IjQxNzNhOTNjLTIzY2MtNGYyYy1iOTJhLTJmZDg0MzQ0OTZiMiIsImF1ZCI6IjJzNDJmc2FzMThjMGticzU1ZzRjcGpjY3ZmIiwiZXZlbnRfaWQiOiJiMGE5YWNlNi04N2I1LTQzMGMtOTc3Yi0yOGMzOTY0ZGI3MmUiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY4NDk0MjEzOCwiZXhwIjoxNjg0OTQ3NzAxLCJpYXQiOjE2ODQ5NDY4MDEsImp0aSI6ImQ2Y2E3OTVmLTc3ZjEtNGFlNi04NTZkLTZiYzUyYjUxM2UzMiIsImVtYWlsIjoic2x1dHNreWVybmFscmx5Z0BnbWFpbC5jb20ifQ.TbqtbTjgZLKReKqdNx3FgpzI1rNNacqkqyxiX0mLYHGgN6AtlimBFVUovCATv1LCrLvxNPIJzk2hD2kTx1oVZF696W2yaJaWadWCtnVGjAuvRtAULOAIBDnb4SowpxnLmXP7kqWeIykvFdk8CbqQ9YZMUOKp9CFIf9_BZtU2SS_ZfvKux1bdvknjonDF5NDQ9w8TNXYooeCS2lptSoMqiDAfgiO7f9N_2f4I2CGm_DHOCBapTCK12gZxyb7AgrRoh5WiXcD-HMqNrKDy7y6s0MOn6z4UTiLzFuiCEB8_X5uEj2IpsspTn_U8QCJZjkhX7iDxNKx8D1mEplm0Lrfq9A'
def parse_ad(count_ads, count_views, count_user_ads):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.olx.uz/',
        'Accept-Language': 'en-US',
        'Authorization': f'Bearer {token}',
    }

    ads = []

    # Загружаем HTML-страницу с olx.uz
    url = 'https://www.olx.uz/d/transport/'
    response = requests.get(url)
    html = response.text

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, 'html.parser')
    visited_urls = set()
    elements = soup.select('[data-cy="l-card"] a')

    # Переменная для подсчета количества объявлений
    count = 0

    # Получение атрибута 'href' для каждого элемента
    for element in elements:
        if count >= count_ads:
            break

        hrefa = element.get('href')
        if hrefa in visited_urls:
            continue

        visited_urls.add(hrefa)

        href = 'https://www.olx.uz' + hrefa
        print("Ссылка:", href)

        ad_response = requests.get(href, headers=headers)
        ad_html = ad_response.text

        # Создаем объект BeautifulSoup для парсинга HTML страницы объявления
        ad_soup = BeautifulSoup(ad_html, 'html.parser')


        ad_title = ad_soup.find('h1', attrs={'data-cy': 'ad_title'})
        ad_price = ad_soup.find('div', attrs={'data-testid': 'ad-price-container'})
        ad_id_element = ad_soup.select_one('[data-cy="ad-footer-bar-section"] span')
        ad_data = ad_soup.find('span', attrs={'data-cy': 'ad-posted-at'})
        ad_photo = ad_soup.find('div', class_='swiper-zoom-container')
        img_tag = ad_photo.find('img')
        src = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None
       # src = ad_photo.find('img')['src']
        print("Изображение:", src)
        print("Дата публикации:", ad_data.text)
        if ad_id_element is not None:
            ad_text = ad_id_element.get_text(strip=True)
            id_value = ad_text.split('ID:')[1].strip()

            page_views_url = f"https://www.olx.uz/api/v1/offers/{id_value}/page-views/"
            zapros = requests.post(page_views_url, headers=headers)
            data = zapros.json()



            value = 0

            if "data" in data:
                value = data["data"]
                if value >= count_views:
                    continue
                print(f'Просмотров: {value}')

            #time.sleep(10)
           # nomer_telephona = f'https://www.olx.uz/api/v1/offers/{id_value}/limited-phones/'
           # zaprosnomera = requests.get(nomer_telephona, headers=headers)
           #datanomer = zaprosnomera.json()


        # описание - ad_description = ad_soup.find('div', attrs={'data-cy': 'ad_description'})
        print("Заголовок объявления:", ad_title.text)
        print("Цена:", ad_price.text)
        ad_userhref = ad_soup.select_one('[data-cy="seller_card"] a')
        if ad_userhref:
            hrefauser = ad_userhref.get('href')
            if 'http' in hrefauser:
                continue
            else:
                hrefuser = 'https://www.olx.uz' + hrefauser
                print("Ссылка на пользователя:", hrefuser)

            us_response = requests.get(hrefuser, headers=headers)
            us_html = us_response.text
            us_soup = BeautifulSoup(us_html, 'html.parser')

            marker = 'window.__PRERENDERED_STATE__= "{\\"userListing\\":{\\"userListing\\":{\\"pageNumber\\":'
            index = us_html.find(marker)

            if index != -1:
                index += len(marker)
                content_after_marker = us_html[index:]
                substring = '\\"totalElements\\":'
                index = content_after_marker.find(substring)
                if index != -1:
                    index += len(substring)
                    remaining_text = content_after_marker[index:]
                    end_index = remaining_text.find(',')
                    number = remaining_text[:end_index]
                    number = number.strip()
                    if int(number) > count_user_ads:
                        continue

        visited_urls.add(hrefa)

        ads.append(
            {
                "link": href,
                "image_link": src,
                "title": ad_title.text,
                "price": ad_price.text,
                "seller_link": hrefuser,
                "seller_ads_count": number,
                "pub_date": ad_data.text,
                "views_count": value
            }
        )

        count += 1
    
    return ads

if __name__ == '__main__':
    print(parse_ad(1, 100, 1))