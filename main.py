# importing the requests library
import requests
import sys
import os

class GetMacAddressDetails:
    def __init__(self, search):
        ''' Constructor '''
        self.search = search
        self.URL = "https://api.macaddress.io/v1"
        self.fName = "config.json"
        self.apikey = os.environ['apikeys']


    def getVendorDetails(self):
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'apiKey': self.apikey, 'output': 'json', 'search': self.search}
        # sending get request and saving the response as response object
        try:
            response = requests.get(url=self.URL, params=PARAMS)
            # extracting data in json format
            data = response.json()
            return data['vendorDetails']['companyName']
        except requests.exceptions.HTTPError as e:
            # Whoops it wasn't a 200
            return "Error: " + str(e)


if __name__ == '__main__':
    try:
        search = sys.argv[1]
        details = GetMacAddressDetails(search)
        companyName = details.getVendorDetails()
        print("Company Name ==", companyName)
    except OSError as err:
        print("OS error: {0}".format(err))
