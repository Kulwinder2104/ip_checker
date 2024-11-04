from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ip_address = ""  # Initialize an empty string to store the IP address
        self.in_ip_section = False  # Flag to check if we are in the section containing the IP

    def handle_starttag(self, tag, attrs):
        pass  # We don't need to do anything for start tags in this case

    def handle_endtag(self, tag):
        if tag == "body":
            self.in_ip_section = False  # Reset the flag when we exit the body

    def handle_data(self, data):
        if "Current IP Address: " in data:
            self.ip_address = data.split(":")[1].strip()  # Extract IP address

def fetch_ip():
    myparser = MyHTMLParser()

    try:
        with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
            html = response.read().decode('utf-8')
        myparser.feed(html)
        return myparser.ip_address
    except urllib.error.URLError as e:
        return f"Error fetching URL: {e}"

if __name__ == "__main__":
    print(fetch_ip())
  