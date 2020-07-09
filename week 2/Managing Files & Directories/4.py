# The file_date function creates a new file in the current working directory, checks the date that the file was modified,
# and returns just the date portion of the timestamp in the format of yyyy-mm-dd.
# Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.
import os
import datetime

def file_date(filename):
    with open(filename,'w') as file:
        file.write('')
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    readable = datetime.datetime.fromtimestamp(timestamp).isoformat()
    readable = str(readable)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return "{}".format(readable[:10])

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd