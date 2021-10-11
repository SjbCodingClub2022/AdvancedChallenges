# Requests and Json Usage
This task assess your knowledge of the requests library and parsing through json responses

## Info
Your solution should be housed in a file named 'solution.py'

The 'requests' library is required for this project

installaion:

    pip install requests

## Function
The function will have no parameters

Make a get request to this api endpoint

    https://api2.binance.com/api/v3/ticker/24hr

Load the requests response as json

Create a dictionary with the following keys and values parsed from the json response

    "Symbol": "Current Price"

Here is an example

    "ETHUSDT": 3528.15,
    "BTCUSDT": 57219.99

Do this for every symbol in the response

Return the dictionary with all the tickers and prices

## Final Program
Use the following statement

    print(Function_Name()["ETHUSDT"])
