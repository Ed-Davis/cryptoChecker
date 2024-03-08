# 'ControlUp' EdgeDX Automation Engineer Role:
### API Technical Exercise Solution

This code checks the Binance API for all Cryptocurrency stats, then sorts them by 
'priceChangePercent' and prints out the top 3 most-changed results along with the 
Current Average Price from the /avgPrice endpoint.

- The very limited dependencies are in the `requirements.txt` file
- You will need to sign up to RapidAPI (Free tier gives 100 queries per month) 
- Under the ControlUp directory create your own `secrets` folder and create a .env file
- Once signed up, you need to add your API key to the `.env` file
- To run the tool, ADD ***GITHUB ACTIONS*** type or click `python cryptoChecks.py`

Notes on using your API Key:
- create a file called .env in the secrets directory
- Add your API key as the variable API_KEY
- Use the format `API_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxx'`
- More ENV vars can be added to this file and will be added to the secrets dictionary in `apilib.py`


TO MAKE SURE YOU USE THE REAL API:

Uncomment line 6 and comment out line 7 to use the real API (the default is mocked).
This is the default behaviour due to the need for an API key
