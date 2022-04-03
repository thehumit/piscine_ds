import sys

def all_stocks(a):
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
	words = a.split(",")
	for word in words:
		if (word == ""):
			return

	for word in words:
		word = word.strip()
		if (word == ""):
			return
		if (word.title() in COMPANIES):
			print(word.title() + " stock price is " + str(STOCKS[COMPANIES[word.title()]]))
		elif (word.upper() in STOCKS):
			try:
				print(word.upper() + " is a ticker symbol for " + list(COMPANIES.keys())[list(COMPANIES.values()).index(word.upper())])
			except ValueError:
				pass
		else:
			print(word + " is an unknown company or an unknown ticker symbol")



if __name__ == '__main__':
	if len(sys.argv) == 2:
		all_stocks(sys.argv[1])
