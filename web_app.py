import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    description = soup.find('meta', attrs={'name': 'description'})['content']
    return title, description
import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    description = soup.find('meta', attrs={'name': 'description'})['content']
    return title, description

def main():
    st.title('Web Scraping App')
    url = st.text_input('Enter URL')
    
    if st.button('Scrape'):
        if url:
            title, description = scrape_website(url)
            st.write(f'Title: {title}')
            st.write(f'Description: {description}')
        else:
            st.write('Please enter a URL')

if __name__ == '__main__':
    main()
