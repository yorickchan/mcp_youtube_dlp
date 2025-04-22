# MCP YouTube-DLP

A Model Context Protocol (MCP) server that provides tools for downloading YouTube videos and audio using yt-dlp.

## Features

- Download YouTube videos in MP4 format
- Download YouTube audio in MP3 format
- Integration with MCP for AI assistant integration

## Prerequisites

- Python 3.13 or higher
- yt-dlp installed on your system

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -e .
```

Or using uv:

```bash
uv pip install -e .
```

## Usage

### Running the Server

Start the MCP server:

```bash
python main.py
```

The server will start in stdio mode with debug enabled.

### Environment Variables

- `YT_DLP_PATH`: Path to the yt-dlp executable (default: `/usr/local/bin/yt-dlp`)

### Available Tools

#### download_youtube_video

Downloads a YouTube video in MP4 format.

**Parameters:**
- `url`: The YouTube video URL

**Returns:**
- A success or error message

#### download_youtube_audio

Downloads a YouTube video's audio in MP3 format.

**Parameters:**
- `url`: The YouTube video URL

**Returns:**
- A success or error message

## MCP Integration

This server implements the Model Context Protocol, allowing AI assistants to access tools for downloading YouTube content. The server can be connected to any MCP-compatible client.

## License

This project is licensed under the GNU General Public License, version 2 (GPL-2.0) - see the [GNU website](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) for details.