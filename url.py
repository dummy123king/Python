import requests

# url = "http://textfiles.com/messages/p80-1.txt"  # Replace this with your URL
url = "http://textfiles.com/messages/103dbug4.txt"
fileName = "example4.txt"

def downLoadFile(url, fileName):
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Open the file in binary write mode
        with open(fileName, "wb") as f:  # Use "wb" for binary write mode
            # Decode the bytes to a string and write to the file
            f.write(response.content)  # Decode bytes to string
        print("File downloaded successfully.")
    else:
        print("Failed to download file. Status code:", response.status_code)


downLoadFile(url, fileName)