# 'ControlUp' EdgeDX Automation Engineer Role:
### API Technical Exercise Solution

This code checks the Binance API for all Cryptocurrency stats, then sorts them by 
'priceChangePercent' and prints out the top 3 most-changed results along with the 
Current Average Price from the /avgPrice endpoint.

- The very limited dependencies are in the `requirements.txt` file
- You will need to sign up to RapidAPI (Free tier gives 100 queries per month) 
- Under the ControlUp directory create an .env file
- Once signed up, you need to add your API key to the `.env` file
- To run the tool, ADD ***GITHUB ACTIONS*** type or click `python crypto_checker.py`

Notes on using your API Key:
- create a file called .env in the secrets directory
- Add your API key as the variable API_KEY
- Use the format `API_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxx'`
- More ENV vars can be added to this file and will be added to the secrets dictionary in `apilib.py`

If you get SSL version warnings:
`pip uninstall urllib3`
`pip install 'urllib3<2.0`


TO MAKE SURE YOU USE THE REAL API:

**Beware** The current default uses the real API but this will speed up your use of your credits.
