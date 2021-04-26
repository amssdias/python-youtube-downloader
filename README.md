# Youtube Video Downloader

Python YouTube Video Downloader is an application to download videos from YouTube. This provides users to download videos they need in their devices and watch them offline.


## Youtube Video Downloader Python Project

The Youtube downloader project is a python project. The object of this project is to download any type of video in a fast and easy way from youtube in your device.

In this python project, user has to copy the youtube video URL that they want to download and simply paste that URL in the ‘paste link here’ section and click on the download button, it will start downloading the video. When video downloading finishes, it shows a message ‘downloaded’ popup on the window below the download button.


## Pre requisites

- [Python](https://www.python.org/downloads/) - 3.8.4 or up

### Pipfile and Pipfile.Lock

Inside the Pipfile there's all the modules name needed for the project.
Download Pipenv through the terminal window (make sure you have Python installed), just type `pip install pipenv`.

After installing pipenv all you have to do is to download the files and in the terminal window, got to the folder with these files and run `pipenv install` and automatically will install this modules.

This will create a virtual environment with the module `pytube`.

To run this virtual environment all you must do is run `pipenv shell` and to close the virtual environment `exit`.

If any doubts here's a link to some more explanations:

- [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)

## Run

- Download the project, open terminal window on folder with 'y_download.py' and type:

```
pipenv shell
```
To activate the pipenv and then we can run:

```
python text_speech.py
```

## Functions

### `get_video`

Will make sure the url is correct and ask the user which resolution would he like to download.

### `download_video`

Download the video directly to the folder.
