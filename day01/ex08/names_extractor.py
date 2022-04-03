import sys

def name_extractor():
	f = open(sys.argv[1])
	f_tsv = open("ds.tsv", "w")
	str_tsv = "Name" + "\t" + "Surename" + "\t" + "Email" + "\n"

	tmp = f.read()
	list_of_emails = tmp.split("\n")
	# print(list_of_emails)
	# list_of_emails.pop("")
	for i in list_of_emails:
		fn = i.split('@')[0]
		username = fn.split(".")[0]
		surename = fn.split(".")[1]
		str_tsv += username + "\t" + surename + "\t" + i + "\n"
	f_tsv.write(str_tsv)

if __name__ == '__main__':
	name_extractor()
