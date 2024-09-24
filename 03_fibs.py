def fibonacci():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

def main():
	for i, num in enumerate(fibonacci()):
		if i == 10:
			break
		print(num)

if __name__ == '__main__':
	main()
