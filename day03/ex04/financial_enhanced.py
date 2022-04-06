from bs4 import BeautifulSoup
import httpx
import sys
import time


def html_getter(x, y):
	# time.sleep(5)
	page = httpx.get(f"https://finance.yahoo.com/quote/{x}/financials", headers = {"User-Agent":"Custom"})
	# print(page.text)
	if page.status_code != 200:
		raise Exception("page is not found")
	soup = BeautifulSoup(page.text, "html.parser")
	all_rows = soup.find_all('div', attrs = {'data-test': 'fin-row'})
	for row in all_rows:
		if row.find('div', attrs = {"title" : y}) is not None:
			# print(row)
			all_colls = row.find_all('div', attrs = {'data-test': 'fin-col'})
			# for coll in all_colls:
				# if coll.find('div'):
			return([y] + [coll.text for coll in all_colls])
if __name__ == "__main__":
	if len(sys.argv) != 3:
		raise Exception("innvalid number of arguments")
	info = html_getter(sys.argv[1], sys.argv[2])
	if info is None:
		raise Exception("nothing found")
