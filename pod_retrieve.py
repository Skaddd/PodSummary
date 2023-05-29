import os
import pytube
from pytube.exceptions import VideoUnavailable

import logging

log = logging.getLogger(__name__)


def extract_podcast(youtube_link: str, saving_path: str = "./data") -> None:
    pod = pytube.YouTube(youtube_link)
    try:
        pod.streams.filter(only_audio=True)[0].download(saving_path)

    except VideoUnavailable:
        log.info(f"{youtube_link} is not video, check the link given")


if __name__ == "__main__":
    pass
