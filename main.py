from bs4 import BeautifulSoup
import requests



URL='https://www.house.kg/snyat?sort_by=upped_at%20desc&page='


def get_html(URL):
    response = requests.get(URL)
    return response.text


# def make_links():
#     page_links=[]
#     for page in range(1, 265):
#         link=URL+str(page)        
#         page_links.append(link)
#     return page_links



def get_all_links(html):
    house_url='https://www.house.kg'
    detail_links=[]
    soup=BeautifulSoup(html, 'html.parser')
    divs=soup.find_all('div', class_='listing')
    for div in divs:
        a = div.find('a').get('href')
        full_url=house_url+a
        detail_links.append(full_url) 
    return detail_links




def get_page_data(html):
    soup=BeautifulSoup(html, 'html.parser')
    name = soup.find('div', class_='left').text.strip()
    dollar = soup.find('div',class_='price-dollar').text.strip()
    som = soup.find('div',class_='price-som').text.strip()

    data={'name':name.strip(), 'dollar':dollar, 'som':som}
    print(data)


def main():
    html=get_html('https://www.house.kg/snyat?sort_by=upped_at%20desc&page=1')
    links=get_all_links(html)
    print(links)
    for link in links:
        get_page_data(get_html(link))
    # make_links()



if __name__ == '__main__':
    main()
