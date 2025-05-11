from Module5_mod import Processor

def main():
    processor = Processor()
    number = int(input("Please enter how many integer you want to input: "))
    for i in range(number):
        value = int(input("Please enter the number one by one: "))
        processor.insertNumber(value)

    target = int(input("Please enter the target value you want to look at: "))
    processor.searchNumber(target)

if __name__ == "__main__":
    main()