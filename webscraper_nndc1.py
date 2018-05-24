#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:37:16 2018

@author: tyler
"""
#https://realpython.com/python-web-scraping-practical-introduction/
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv   

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
for n in range(178):
    for z in range(117):
        raw_html = simple_get('https://www.nndc.bnl.gov/chart/reCenter.jsp?z='+str(z)+'&n='+str(n))
        html = BeautifulSoup(raw_html, 'html.parser')
        data_rows = html.findAll('tr')  # skip the first 2 header rows        
        player_data = [[td.getText() for td in data_rows[i].findAll('td')]
            for i in range(len(data_rows))]
        player_data[12:14]
        nums = len(player_data)
        fields=[n,z,player_data[13][:]]#,player_data[13][1],player_data[13][2],player_data[13][3],player_data[13][4]]
        with open(r'n_z12.csv', 'a+') as file:
            writer = csv.writer(file)
            writer.writerow(fields)

# =============================================================================
# player_data[12:14]
# for i, li in enumerate(html.select('li')):
#         print(i, li.text)
# data_rows = html.findAll('tr')  # skip the first 2 header rows        
# player_data = [[td.getText() for td in data_rows[i].findAll('td')]
#             for i in range(len(data_rows))]
# player_data[12:14]
# #https://www.nndc.bnl.gov/chart/reCenter.jsp?z=70&n=98
# =============================================================================
