f = open('Hello world.txt', 'w')
f.write('hello world')
f.close()

# file named "hello.txt" in write mode ("w") using the open() function and assigns it to the variable f. The with
# statement ensures that the file is properly closed when we're done with it.

# Then we use the write method of the file object f to write the text "hello world" to the file. Finally,
# the file is closed automatically when the with block is exited.

# You should now have a file named "hello.txt" in the current directory with the text "hello world" inside it.
