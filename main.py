"""
FastMCP Youtube Dlp Server
"""

import logging
import os
import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Youtube Dlp")

# Default download directory from environment variable or fallback to user's home directory
DEFAULT_DOWNLOAD_DIR = os.environ.get(
    "DEFAULT_DOWNLOAD_DIR",
    os.path.join(os.path.expanduser("~"), "Downloads", "youtube_downloads"),
)
# Expand user path if using tilde notation
DEFAULT_DOWNLOAD_DIR = os.path.expanduser(DEFAULT_DOWNLOAD_DIR)
# Current download directory (can be changed via set_download_path)
current_download_dir = DEFAULT_DOWNLOAD_DIR

# Create the default directory if it doesn't exist
os.makedirs(DEFAULT_DOWNLOAD_DIR, exist_ok=True)


@mcp.tool()
def get_current_download_path() -> str:
    """Get the current folder path where downloads are being saved

    Returns:
        The current download path
    """
    return f"Current download path: {current_download_dir}"


@mcp.tool()
def download_youtube_video(url: str) -> str:
    """Download a youtube video from a given URL"""
    yt_dlp_path = os.environ.get("YT_DLP_PATH", "/usr/local/bin/yt-dlp")

    # Ensure the download directory exists
    os.makedirs(current_download_dir, exist_ok=True)

    # downloading a video
    result = subprocess.run(
        [
            yt_dlp_path,
            f"{url}",
            "-f",
            "mp4",
            "-o",
            os.path.join(current_download_dir, "%(title)s.%(ext)s"),
            "--print",
            "after_move:filepath",
        ],
        stdout=subprocess.PIPE,
        text=True,
    )

    output = result.stdout.strip()
    logging.info(output)

    if result.returncode == 0:
        return f"Success: Video downloaded from {url} to path: {output}"
    else:
        return f"Error: Failed to download video from {url}"


@mcp.tool()
def download_youtube_audio(url: str) -> str:
    """Download a youtube audio from a given URL"""
    yt_dlp_path = os.environ.get("YT_DLP_PATH", "/usr/local/bin/yt-dlp")

    # Ensure the download directory exists
    os.makedirs(current_download_dir, exist_ok=True)

    # downloading a audio
    result = subprocess.run(
        [
            yt_dlp_path,
            "--audio-format",
            "mp3",
            "-x",
            f"{url}",
            "-o",
            os.path.join(current_download_dir, "%(title)s.%(ext)s"),
            "--print",
            "after_move:filepath",
        ],
        stdout=subprocess.PIPE,
        text=True,
    )

    output = result.stdout.strip()
    logging.info(output)

    if result.returncode == 0:
        return f"Success: Audio downloaded from {url} to path: {output}"
    else:
        return f"Error: Failed to download audio from {url}"


if __name__ == "__main__":
    # Start the server
    mcp.run(transport="stdio")
