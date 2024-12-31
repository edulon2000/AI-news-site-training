
---

# **News Scraper**

## **Overview**

The **News Scraper** project aims to create a Python script that collects news from a specific website, processes, and organizes the information by categories. The scraper will use the `BeautifulSoup` library for parsing and extracting HTML data and the `Requests` library to make HTTP requests to the website. This project will help in learning and applying techniques related to web scraping, text processing, and data categorization.

## **Requirements**

### **Technologies and Tools**
- **Python** (version 3.x or higher)
- **Python Libraries**:
  - `BeautifulSoup` (for parsing HTML)
  - `Requests` (for making HTTP requests)
  - **(Optional)** `Pandas` (for handling and storing news in tabular format)
  - **(Optional)** `nltk` or `spacy` (for text processing and categorizing news)
- **Code Editor**: VS Code, PyCharm, or any other editor of your choice
- **Virtual Environment** (recommended for managing dependencies)

### **Installing the Libraries**
The required libraries can be installed using `pip`:
```bash
pip install beautifulsoup4 requests pandas nltk
```

## **Environment Setup**

### **Step 1: Install Python**
Ensure that Python is installed on your system. If not, download the latest version from the [official Python website](https://www.python.org/downloads/).

### **Step 2: Create a Virtual Environment**
Create a virtual environment to isolate the project's dependencies:
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows**: `venv\Scripts\activate`
- **Linux/Mac**: `source venv/bin/activate`

### **Step 3: Install Dependencies**
Install the necessary libraries:
```bash
pip install beautifulsoup4 requests pandas nltk
```

### **Step 4: Directory Structure**
Create the following directory structure for your project:
```
news-scraper/
│
├── venv/             # Virtual environment
├── scraper.py        # Main scraper script
├── requirements.txt  # List of dependencies
└── README.md         # Project documentation
```

In the `requirements.txt` file, list the dependencies for easy installation in other environments:
```
beautifulsoup4
requests
pandas
nltk
```

## **Features**

### **1. Collecting News**
The script will make HTTP requests to the chosen website and use `BeautifulSoup` to parse the page and extract news content.

**Example of collection**:
- Access the news website URL.
- Extract the news titles, links, publication date, and summary.

### **2. Text Processing**
Text processing will be used to analyze the content of the news articles and categorize them based on their topics.

**Example of categorization**:
- Identify categories such as "Technology", "Politics", "Economy", etc., using keywords or classification models.

### **3. Storing Data**
The collected and categorized news will be saved in a CSV file or a database, depending on the user's preference.

**Example CSV format**:
```csv
Title, URL, Category, Summary
"News 1", "http://example.com/news1", "Technology", "Summary of news 1"
"News 2", "http://example.com/news2", "Politics", "Summary of news 2"
```

### **4. Scheduled Execution (Optional)**
An optional feature would be to allow the scraper to run on a schedule, collecting news at regular intervals.

## **Code Structure**

### **1. scraper.py**
This will be the main script for the project. It will be responsible for:
- Making HTTP requests to the websites.
- Parsing the HTML using BeautifulSoup.
- Extracting news data.
- Processing and categorizing the news.
- Storing the results.

**Example code structure**:
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def collect_news(soup):
    news_list = []
    for item in soup.find_all('div', class_='news-item'):
        title = item.find('h2').text
        link = item.find('a')['href']
        summary = item.find('p').text
        news_list.append([title, link, summary])
    return news_list

def categorize_news(news_list):
    # Simple categorization example
    for news in news_list:
        if 'technology' in news[0].lower():
            news.append('Technology')
        else:
            news.append('Other')
    return news_list

def save_news(news_list):
    df = pd.DataFrame(news_list, columns=['Title', 'URL', 'Summary', 'Category'])
    df.to_csv('news.csv', index=False)

def main():
    url = 'https://www.example.com'
    soup = get_content(url)
    news_list = collect_news(soup)
    news_list = categorize_news(news_list)
    save_news(news_list)

if __name__ == '__main__':
    main()
```

---
