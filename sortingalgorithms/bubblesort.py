

def main():
    unsorted_list = [29, 54, 13, 23, 41, 20, 12,37, 38, 5, 7, 72, 39, 43, 64, 30, 71, 50, 45]
    sorted = False
    print("###BUBBLESORT###")
    print('Unsorted list:')
    print(unsorted_list)
    while sorted == False:
        for i in range(0, len(unsorted_list) - 1):
            current_number = unsorted_list[i]
            next_number = unsorted_list[i + 1]


if __name__ == "__main__":
	main()
