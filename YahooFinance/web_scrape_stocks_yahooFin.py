# lets get the basic libraries imported - those we would need for Beautiful Soup
from requests import get
from bs4 import BeautifulSoup
import os
from datetime import datetime

# also, since we would need to read the stock names from an external text file, lets setup 
# the relative path

# setup the default lookup location to CWD
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Now __location__ holds the path of the location where out python code file will reside. Hence
# we need to keep our stock list file here as well


# lets define the generate_url(stock) method
def generate_url(stock):
    # base url - the one that we received from the client
    base_url = "https://finance.yahoo.com/quote/"
    
    # complete url
    url = base_url + stock
    return url


# lets create another function which would actually scrape the data and pass the url to it
def extract_data(url):
    # get the response from the url provide
    # this can be done using the 'get' method from response
    response = get(url)

    # create a beautiful soup object to parse the HTML response
    html_resp = BeautifulSoup(response.text, 'html.parser')

    # also, we will need to add the timestamp when the data was scraped
    # lets do that
    time = datetime.now()

    # finally we extract the price information using the find method
    price = html_resp.find('span', class_ = "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)").text

    # we would need both timestamp and price information
    return time, price




if __name__ == "__main__":
    # read the stock names from the text file we just created
    source = open(os.path.join(__location__, 'stock_list.txt'))
    stock_list = source.readlines()

    # lets check what we got into stock_list
    # print(stock_list)

    # lets cleanup the newline character from each element
    stock_list = [val.replace('\n', '') for val in stock_list]
    # basically we have replaced newline with null character

    # lets print now and check
    # print(stock_list)

    # hold the extracted information in a list
    dataset = []

    # now we need to generate a url for each of these stocks and scrape the price
    # we can do this recursively in a loop
    for stock in stock_list:
        # lets generate the url in a separate method
        url = generate_url(stock)
        time, price = extract_data(url)
        # lets append the timestamp, code of the stock and extracted price as a string in a list
        dataset.append(str(str(time) + ',' + str(stock) + ',' + str(price)))

    # finally write the output back to a text file for now
    # eventually the file wrie option can be replaced with storing the information some other way
    # I am just trying to keep it simple for now
    out_file = open(os.path.join(__location__, 'output.txt'), 'w+')
    for data in dataset:
        out_file.write(data+'\n')
    
    out_file.close()

    # lets run the code and check

    # lets check if what we got are indeed the correct prices for each


    # looks good !!
    