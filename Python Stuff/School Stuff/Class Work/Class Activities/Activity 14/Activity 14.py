#Activity 14

#Reference all Open and Read with FileName variable
FileName = "2025_GCSE_Programming_Activity14.txt"

#Read the file as a string and print out the output
with open(FileName, "r") as File:
    FileContents = File.read()
    print(FileContents)

#Read the file as a 1 Dimension array and print out the output