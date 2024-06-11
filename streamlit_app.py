import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon_reviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    reviews = []
    review_elements = soup.find_all('div', {'data-hook': 'review'})
    
    for review in review_elements:
        review_text = review.find('span', {'data-hook': 'review-body'}).text.strip()
        reviews.append(review_text)
    
    return reviews

def main():
    st.title("Amazon Product Review Extractor")
    
    product_url = st.text_input("Enter Amazon Product URL:")
    if st.button("Extract Reviews"):
        if product_url:
            try:
                reviews = scrape_amazon_reviews(product_url)
                df = pd.DataFrame({"Reviews": reviews})
                st.write(df)
            except:
                st.error("Failed to extract reviews. Please check the URL and try again.")

if __name__ == "__main__":
    main()
