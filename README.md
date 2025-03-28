# Youtube Stream Capture - YTStreamCap
## Description
This is python script that currently allows to track youtube channels and capture livestreams from them. Script uses Youtube data v3 api that checks if specified channel is streaming and then if so it downloads it to previously specified out path. The download itself uses yt_dlp that will later merge audio and video files.
## Instalation
**Step 1:**
```
apt update -y && apt upgrade -y
```
**Step 2:**
```
apt install python3 python3-venv python3-pip -y
```
**Step 3:**
```
python3 -m venv PATH_TO_DESIRED_FOLDER
```
**Step 4:**
```
source PATH_TO_DESIRED_FOLDER/bin/activate
```
**Step 5:**
```
pip install yt_dlp google-api-python-client
```
**Step 6:**<br />
<br />[Download main.py](https://github.com/HomicideFreak/YTStreamCap/releases/download/Releases/main.py)<br />
<br />**Step 7:**<br />
<br />Put main.py in your virtual environment folder<br />
<br /> **_!!! IMPORTANT !!!_**<br />
<br />**_PUT YOUR API KEY IN THE main.py SCRIPT_**<br />

## Usage
* Make sure virutal environment is activated: 
```
source PATH_TO_DESIRED_FOLDER/bin/activate
```
* Run the script: 
```
python3 PATH_TO_DESIRED_FOLDER/main.py
```
* Follow the instructions of the program, once you specify the channel to track and output path, script will automatically track the channel and download any livestream to output folder.
* To exit from virtual environment: 
```
deactivate
```


