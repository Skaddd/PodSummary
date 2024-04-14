import pytube
from pytube.exceptions import VideoUnavailable
from tqdm import tqdm
from joblib import Parallel, delayed
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


def find_videos(playlist_url: str, channel_url: str = None) -> list[str]:
    """Extract multiple video urls from youtube.

    Args:
        playlist_url (str): youtube playlist url.
        channel_url (str, optional): youtube channel url.
        Defaults to None.

    Returns:
        list[str]: list of youtube urls.
    """
    try:
        if channel_url is not None:
            yt_object = pytube.Channel(channel_url)
        else:
            yt_object = pytube.Playlist(playlist_url)
        final_urls = [
            video_url for video_url in tqdm(yt_object.url_generator())
        ]
    except KeyError:
        log.warning("The given playlist/channel is not working, check it")
        return []

    return final_urls


def batch_extract_podcast(podcast_urls: list[str]) -> None:
    """Extract multiple videos.

    Args:
        podcast_urls (list[str]): list of youtube urls.
    """
    for video_url in tqdm(podcast_urls):
        extract_podcast(video_url)


def global_extract_podcast(
    playlist_url: list[str],
    channel_url: str = None,
    batch_size: int = 10,
    n_jobs: int = -1,
) -> None:
    log.info(
        "Multiprocessing is launched |"
        + f"batch_size : {batch_size} | jobs : {n_jobs}"
    )
    all_urls = find_videos(playlist_url, channel_url)

    log.info(f"From the selectioned source : {len(all_urls)}" + " were found")

    executor = Parallel(n_jobs=n_jobs, verbose=1)
    do = delayed(batch_extract_podcast)
    tasks = (
        do(all_urls[i: i + batch_size])
        for i in range(0, len(all_urls), batch_size)
    )
    _ = executor(tasks)
