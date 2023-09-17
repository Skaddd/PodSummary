import pytube
from pytube.exceptions import VideoUnavailable

import logging

log = logging.getLogger(__name__)


def extract_podcast(
    youtube_link: str, saving_path: str = "./data/podcast"
) -> None:
    """Extract Youtube podcast audio only.

    Args:
        youtube_link (str): url linking to a youtube video.
        saving_path (str, optional): saving path.
        Defaults to "./data/podcast".
    """
    pod = pytube.YouTube(youtube_link)
    log.info("Downloading video...")
    try:
        pod.streams.filter(only_audio=True)[0].download(saving_path)

    except VideoUnavailable:
        log.info(f"{youtube_link} is not video, check the link given")
