"""
FastMCP Youtube Dlp Server
"""

import os
import subprocess

import httpx
from mcp.server.fastmcp import FastMCP

# Create server
mcp = FastMCP("Youtube Dlp")


@mcp.tool()
def download_youtube_video(url: str) -> str:
    """Download a youtube video from a given URL"""
    yt_dlp_path = os.environ.get("YT_DLP_PATH", "/usr/local/bin/yt-dlp")

    # downloading a video
    result = subprocess.run(
        [yt_dlp_path, f"{url}", "-f mp4"],
        stdout=subprocess.PIPE,
    )
    print(result.stdout)
    if result.returncode == 0:
        return f"Success: Video downloaded from {url}"
    else:
        return f"Error: Failed to download video from {url}"


@mcp.tool()
def download_youtube_audio(url: str) -> str:
    """Download a youtube audio from a given URL"""
    yt_dlp_path = os.environ.get("YT_DLP_PATH", "/usr/local/bin/yt-dlp")

    # downloading a audio
    result = subprocess.run(
        [yt_dlp_path, "--audio-format", "mp3", "-x", f"{url}"],
        stdout=subprocess.PIPE,
    )
    print(result.stdout)
    if result.returncode == 0:
        return f"Success: Audio downloaded from {url}"
    else:
        return f"Error: Failed to download audio from {url}"


if __name__ == "__main__":
    # Start the server
    mcp.run(transport="stdio", debug=True)
