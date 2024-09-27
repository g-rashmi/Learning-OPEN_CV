

import pafy

url = "https://www.youtube.com/watch?v=HnLtNrvfZTU&list=RDHnLtNrvfZTU&start_radio=1"
data = pafy.new(url)

# Print video details
print((data))  # Convert the object to string (or) 


# # Access and print specific details about the video

# print("Duration: " + data.duration)
# print("Author: " + data.author)
# print("Viewcount: " + str(data.viewcount))
#pafy=0.5.4 #youtube-dl=2020.12.2