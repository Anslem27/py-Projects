# yt downloader with python uing [ct] and [pytube] lib

import tkinter
import customtkinter as ct
from pytube import YouTube as yt

# System settings
ct.get_appearance_mode()
ct.set_default_color_theme("blue")

#  setup app frame
app = ct.CTk()
app.geometry("620x400")
app.title("Youtube downloader")

# ui elements
title = ct.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# link entry

fetch_url = tkinter.StringVar()
link_input = ct.CTkEntry(app, width=350, height=40, textvariable=fetch_url)
link_input.pack()

# download btn logic


def downloadVideo():
    try:

        instance = yt(link_input.get(), on_progress_callback=updateStats)
        stream = instance.streams.get_lowest_resolution()
        title.configure(text=instance.title)
        finishTxt.configure(text="")
        stream.download()
        finishTxt.configure(text="Download Complete", text_color="green")

    except:
        finishTxt.configure(text="Download failed", text_color="red")


def updateStats(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    download_progress = total_size-bytes_remaining
    percentage = total_size/download_progress * 100
    value = str(int(percentage))
    txtpercentage.configure(text=value+"%")
    txtpercentage.update()

    # update progress bar
    indicator.set(float(percentage)/100)


download_btn = ct.CTkButton(app, text="Download", command=downloadVideo)
download_btn.pack(padx=10, pady=10)


# progress indicator
txtpercentage = ct.CTkLabel(master=app, text="0%")
txtpercentage.pack(padx=5, pady=5)
indicator = ct.CTkProgressBar(app, width=400)
indicator.set(0)
indicator.pack(padx=10, pady=10)
# wrap
# finish text

finishTxt = ct.CTkLabel(app, text="")
finishTxt.pack()


if __name__ == "__main__":
    app.mainloop()
