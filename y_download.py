from pytube import YouTube
import tkinter as tk


# Append all resolutions to list
resolutions = []


def get_video(url: str):
    """
    Get the video and tell user if the url was valid
    """
    global frm_text_video
    global lbl_text_video
    global resolutions

    try:

        # If we not downloading first time
        if resolutions:
            for i in resolutions:
                i.pack_forget()

        # Display to user that it's getting video
        frm_text_video.pack()

        # Class to download video
        yt = YouTube(url)

        lbl_text_video['text'] = "Choose resolution"

        # Only choose videos that have audio and video in 1 file (progressive)
        progressive_streams = yt.streams.filter(progressive=True)

        for counter, stream in enumerate(progressive_streams):
            # print(f"{counter}: {stream.resolution}")

            frm_res = tk.Frame(master=window, padx=15, pady=10)
            res_video = tk.Button(
                master=frm_res,
                padx=8,
                pady=4,
                text=stream.resolution,
                command=lambda: download_video(stream)
            )

            resolutions.append(frm_res)
            frm_res.pack()
            res_video.pack()

        print("Done")

    except:
        lbl_text_video['text'] = "URL not valid, try other one"


def download_video(stream):
    lbl_text_video['text'] = "Downloading..."
    stream.download()
    lbl_text_video['text'] = "Download Complete"


# Layout
window = tk.Tk()
window.geometry("450x450")

frm_title = tk.Frame(master=window, pady=15)
frm_text = tk.Frame(master=window, pady=10)
frm_button = tk.Frame(master=window, pady=15)

lbl_title = tk.Label(
    master=frm_title,
    text="Youtube Video Downloader",
    font=("Courier", 20, "bold"),
    fg="blue"
)
ent_text = tk.Entry(
    master=frm_text,
    font=("Courier", 12)
)
btn_button = tk.Button(
    master=frm_button,
    text="Download",
    font=("Courier", 15),
    pady=8,
    padx=15,
    command=lambda: get_video(ent_text.get())
)

frm_title.pack()
frm_text.pack()
frm_button.pack()

lbl_title.pack()
ent_text.pack()
btn_button.pack()

# When getting the video
frm_text_video = tk.Frame(master=window, pady=10)
lbl_text_video = tk.Label(
    master=frm_text_video,
    text="Getting video...",
    font=("Courier", 12)
)

lbl_text_video.pack()


window.mainloop()
