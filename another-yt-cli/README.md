# Yet Another yt-cli

- **What can it do as of now ?**
> It can query the input entered by user on youtube and get the first matching result, and play it in the video player.

- **Things to improve:**
> - Let the user choose the video by giving them the first 10 or so search results.
> - Allow users to set the resolution as per their preference.

---
## Demo:
<img src="./assets/demo.gif" width=100%>

### **Requirements**:
The following packages need to be installed:
```
beautifulsoup4
certifi
charset-normalizer
idna
lxml
requests
soupsieve
urllib3
youtube-dl
```
To install the above packages, change directory to the project folder
```shell
cd another-yt-cli
```
Now install the packages by running,
```shell
pip install -r requirements.txt
```
And. now to run the program, type
```shell
python main.py
```
> **Note: You will also require the mpv player to play the videos