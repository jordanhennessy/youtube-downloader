import streamlit as st
from pytube import YouTube
from os import listdir, remove, path, rename

file_dir = "/tmp/files"
max_vid_length = 1500


def cleanup():
    for name in listdir(file_dir):
        remove(f"{file_dir}/{name}")
    st.session_state["confirmed"] = False
    st.session_state["file"] = None


def start_download():
    st.session_state["confirmed"] = True
    if st.session_state["output"] == "MP3":
        download_mp3()
    elif st.session_state["output"] == "MP4":
        download_mp4()
    else:
        st.write("An error has occurred, please refresh the page")


def get_resolution(video: YouTube):
    best_resolution = None
    resolutions = ["720p", "480p", "360p"]
    for resolution in resolutions:
        if video.streams.filter(resolution=resolution).first():
            best_resolution = resolution
            break

    if best_resolution:
        return video.streams.filter(resolution=best_resolution).first()


def download_mp4():
    video = YouTube(st.session_state["url"])
    if video.length > max_vid_length:
        st.session_state["error"] = True
        return
    video = get_resolution(video)
    st.session_state["title"] = video.title
    file_path = video.download(output_path=file_dir)
    st.session_state["file"] = file_path
    st.session_state["downloaded"] = True


def download_mp3():
    video = YouTube(st.session_state["url"])
    video = video.streams.filter(only_audio=True).first()
    st.session_state["title"] = video.title
    file_path = video.download(output_path=file_dir)
    base, ext = path.splitext(file_path)
    new_file_path = base + ".mp3"
    rename(file_path, new_file_path)
    st.session_state["file"] = new_file_path
    st.session_state["downloaded"] = True


st.set_page_config(page_title="YouTube Downloader")
st.title("Youtube Downloader")
st.markdown("---")

if "confirmed" not in st.session_state:
    st.session_state["confirmed"] = False
if "downloaded" not in st.session_state:
    st.session_state["downloaded"] = False
if "file" not in st.session_state:
    st.session_state["file"] = None
if "error" not in st.session_state:
    st.session_state["error"] = False


col1, col2 = st.columns(2)

with col1:
    st.session_state["url"] = st.text_input("YouTube URL:", placeholder="Paste YouTube URL here")
    if st.session_state["url"] != "" and not st.session_state["confirmed"]:
        st.write(f"Downloading from: {st.session_state['url']}")
        st.button("Confirm", on_click=start_download)
    if st.session_state["downloaded"] and st.session_state["file"]:
        if st.session_state["output"] == "MP3":
            mime = "audio/mpeg"
        else:
            mime = "video/mp4"
        with open(st.session_state["file"], "rb") as output:
            st.download_button(f"Download {st.session_state['output']}", data=output, mime=mime, on_click=cleanup(),
                               file_name=f"{st.session_state['title']}.{str(st.session_state['output']).lower()}")
    if st.session_state["error"]:
        st.write("Videos longer than 25 minutes are not supported. Refresh the page to try a different video")

with col2:
    st.session_state["output"] = st.radio("File Type:", ("MP3", "MP4"))


