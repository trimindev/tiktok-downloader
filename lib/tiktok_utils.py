from tiktok_downloader import snaptik
import asyncio
import uuid
import threading


def extract_video_id(tiktok_url):
    url_parts = tiktok_url.split("/")
    video_index = url_parts.index("video")
    video_id = url_parts[video_index + 1]
    return video_id


def download_video(video_url: str, output_folder: str):
    # Get the video data
    video_data = snaptik(video_url)
    # Check if video data is available
    if video_data:
        if video_data[0].type == "video":

            video_id = extract_video_id(video_url)
            output_filename = f"{output_folder}/{video_id}.mp4"

            # Download the video
            video_data[0].download(output_filename)
            print("Video downloaded successfully.")
            return True
        else:
            print("No video found in the provided URL.")
    else:
        print("Failed to retrieve video data.")

    return False


async def download_videos(file_path: str, output_folder: str) -> None:
    try:
        with open(file_path, "r") as file:
            urls = file.readlines()
            urls = [
                url.strip() for url in urls if url.strip()
            ]  # Remove empty lines and strip whitespace

        tasks = [download_video(url, output_folder) for url in urls]
        await asyncio.gather(*tasks)
        return True

    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("Error occurred:", str(e))

    return False


if __name__ == "__main__":
    pass
