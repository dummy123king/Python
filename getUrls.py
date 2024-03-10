import requests
from bs4 import BeautifulSoup
import webbrowser

# Example usage
base_url = "http://textfiles.com/"
target_url = "http://textfiles.com/directory.html"


def print_extracted_Urls(extracted_urls):
    if extracted_urls:
        print("Extracted URLs:")
        for url in extracted_urls:
            print(url)
    else:
        print("No URLs found on the webpage.")

def extract_urls(url):
  """Extracts URLs from a webpage using requests and BeautifulSoup.

  Args:
      url: The URL of the webpage to scrape.

  Returns:
      A list of extracted URLs from the webpage.
  """
  # Send an HTTP GET request to the URL
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all anchor tags (<a>) containing URLs
    links = soup.find_all('a', href=True)

    # Extract URLs from the anchor tags
    urls = [link['href'] for link in links]

    # Remove duplicates (optional)
    urls = list(set(urls))

    return urls
  else:
    print(f"Error getting webpage: {response.status_code}")
    return []

def downLoadFile(url, fileName = "ExampleFile"):
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Open the file in binary write mode
        with open(fileName, "wb") as f:  # Use "wb" for binary write mode
            # Decode the bytes to a string and write to the file
            f.write(response.content)  # Decode bytes to string
        print(f"{fileName} downloaded successfully.")
    else:
        print("Failed to download file. Status code:", response.status_code)


def getThefileFromUrl(baseUrls = None, subModuleName  = None, fileToDownload  = None):
    absoluteUrl1 = None
    extracted_urls = extract_urls(target_url)
    if extracted_urls:
        print("Extracted URLs:")
        for url in extracted_urls:
            if subModuleName == url:
                absoluteUrl1 = base_url + subModuleName
                break
            else:
                continue
        if absoluteUrl1 != None:
            print(absoluteUrl1)
            extracted_urls = extract_urls(absoluteUrl1)
            if extracted_urls:
                for item in fileToDownload:
                    absoluteUrl2 = absoluteUrl1 + "/" + item
                    downLoadFile(absoluteUrl2, item)
            else:
                print("No URLs found on .")
        else:
            print("No URLs found inside the WebPage")
    else:
        print("No URLs found on the webpage.")

if __name__ == "__main__":
    data = [
    "blood.txt",
    "books.txt",
    "br-hatlb.sng",
    "brap.txt",
    "broken.alb",
    "broken.txt",
    "brosinga.txt",
    "brothel.txt",
    "bulfugaz.txt",
    "bullshit.txt",
    ]
    getThefileFromUrl(base_url, "music", data)
