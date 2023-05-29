import os
import pytube


def extract_podcast(youtube_link: str, saving_path: str = "./data") -> None:
    pod = pytube.YouTube(youtube_link)
    pod.streams.filter(only_audio=True)[0].download(saving_path)

    return


if __name__ == "__main__":
    pass
