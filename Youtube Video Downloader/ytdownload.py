from pytube import YouTube  

link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"  #add your video link here

try:  
    youtube_video = YouTube(link)  
except:  
    print("Connection Timed Out")  

print(youtube_video .title)
stream = youtube_video .streams.first()
try:  
    stream.download()
except:  
    print("Please try again!!")  
print('Download Successful')  