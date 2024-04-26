def main():
    filename = input("Enter Filename: ")
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print("Number of line/s in the file: ", len(lines), "\n")
            for line_number, line in enumerate(lines, 1):
                print("Line {}: {}".format(line_number, line.strip()))

        while True:
            line_number = int(input("\nEnter line number (0 to quit): "))
            if line_number == 0:
                break
            elif line_number < 1 or line_number > len(lines):
                print("Invalid number")
            else:
                line = lines[line_number-1].strip()
                print(line)
                
    except FileNotFoundError:
        print("Error! The file was not found")
main()
