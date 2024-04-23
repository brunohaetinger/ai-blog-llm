import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin

# Create the data directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

url = "https://diego-pacheco.blogspot.com/"
driver = webdriver.Chrome()  # Use Chrome or any other browser you prefer
driver.get(url)

while True:
    # Get all article links on the current page
    soup = BeautifulSoup(driver.page_source, "html.parser")
    more_posts_url = soup.find("a", class_="blog-pager-older-link")["href"]
    print("next URL: " + more_posts_url)
    
    post_links = [link["href"] for link in soup.select("article.post-outer-container > div > div > h3 > a")]

    # Download and save each post as .md file
    for post_link in post_links:
        post_url = urljoin(url, post_link)
        driver.get(post_url)
        post_soup = BeautifulSoup(driver.page_source, "html.parser")
        
        # Extract post title and content
        post_title = post_soup.title.text
        post_content = post_soup.find("div", class_="post-body").get_text()

        # Replace "/" with "-" in the file name
        file_name = os.path.join("data", post_title.replace("/", "-").replace(" ", "_") + ".md")
        with open(file_name, "w") as file:
            file.write(f"# {post_title}\n\n")
            file.write(post_content)

        print(f"Saved {file_name}")

    # Click the "More posts" button
    try:
        # more_posts_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, "load-more"))
        # )
        # more_posts_button.click()
        driver.get(more_posts_url)
        time.sleep(2)  # Wait for the page to load
    except Exception as e:
        print("No more posts to load.")
        break

driver.quit()
print("All posts saved.")
