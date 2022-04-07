import sys
import resource

def reader():
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        tmp_line = 'hey'
        while tmp_line:
            tmp_line = file.readline()
            yield tmp_line


def main():
	for i in reader():
		pass
	usage = resource.getrusage(resource.RUSAGE_SELF)
	print(f'Peak Memory Usage = {(usage.ru_maxrss / (1024**3)):.3f} GB')
	print(f'User Mode Time + System Mode Time = {(usage.ru_utime + usage.ru_stime):.2f}s')

if __name__=="__main__":
	if (len(sys.argv) == 2):
		main()
