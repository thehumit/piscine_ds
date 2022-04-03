import sys

def ticker_symbols(a):
	COMPANIES = {
	'Apple': 'AAPL',
	'Microsoft': 'MSFT',
	'Netflix': 'NFLX',
	'Tesla': 'TSLA',
	'Nokia': 'NOK'
	}
	STOCKS = {
	'AAPL': 287.73,
	'MSFT': 173.79,
	'NFLX': 416.90,
	'TSLA': 724.88,
	'NOK': 3.37
	}
	try:
		print(list(COMPANIES.keys())[list(COMPANIES.values()).index(a.upper())] + " " +str(STOCKS[a.upper()]))
	except ValueError:
		print("Unknown ticker")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		ticker_symbols(sys.argv[1])
