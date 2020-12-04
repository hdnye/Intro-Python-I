"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# using the with keyword for file objects will properly close the file after 
# the suite finishes
# with open('src/foo.txt', 'r') as f:
#     read_data = f.read()
#     # print(read_data)
#     text = read_data.split()
#     print(text)
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# with open('src/bar.txt', 'w') as bar_file:
#     bar_file.writelines('Python is great\nI love it more than JS\nMight pass my sprint\n')
#     print(bar_file)

with open('src/bar.txt', 'r') as f:
    read_data = f.read()
    # print(read_data)
    text = read_data.split()
    start = '"'
    sentence = []
    for i in text:
        if start[0].isupper():
            sentence[i]
    print(sentence)
        

# if not using with, close the file with print(f.closed) or w/e var was used    



# start = text[0].isupper() or '"'
# print(start)
