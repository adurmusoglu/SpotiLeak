from typing import List
from fastapi import HTTPException
from models import SearchRequest, YTResult 
from yt_dlp import YoutubeDL

def search_youtube(req: SearchRequest) -> List[YTResult]:
    parts = [req.song, req.artist]
    query = " ".join(p.strip() for p in parts if p and p.strip())
    search_url = f"ytsearch{req.total_results}:{query}"

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": True,   # key: do NOT resolve formats/streams
        "noplaylist": True,
        "socket_timeout": 10,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            data = ydl.extract_info(search_url, download=False)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"yt-dlp search failed: {e}")

    entries = data.get("entries") or []
    results: List[YTResult] = []

    for e in entries:
        if not e:
            continue

        video_id = e.get("id") or ""
        title = e.get("title") or ""
        duration = float(e.get("duration") or 0)
        # Optional -- includes the channel that uploaded the YT video
        channel = e.get("artist") or e.get("uploader") or e.get("channel")

        if not video_id:
            continue

        results.append(
            YTResult(
                title=title,
                video_id=video_id,
                duration=duration,
                channel=channel
            )
        )

    return results