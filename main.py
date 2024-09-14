import yt_dlp as youtube_dl
import instaloader
import tkinter as tk
from tkinter import filedialog, simpledialog

# YouTube video downloader
def download_youtube_video(url, save_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s'
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("YouTube video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Instagram video downloader
def download_instagram_video(url, save_path):
    try:
        ig_loader = instaloader.Instaloader(dirname_pattern=save_path)
        ig_loader.download_post(instaloader.Post.from_shortcode(ig_loader.context, url.split("/")[-2]), target=save_path)
        print("Instagram video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Function to open file dialog
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    # Ask user which platform they want to download from
    platform = simpledialog.askstring("Platform", "Which platform? Enter 'YouTube' or 'Instagram':").lower()
    
    video_url = input("Please enter the video URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        if platform == "youtube":
            download_youtube_video(video_url, save_dir)
        elif platform == "instagram":
            download_instagram_video(video_url, save_dir)
        else:
            print("Invalid platform selected.")
    else:
        print("Invalid save location.")
