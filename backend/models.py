from pydantic import BaseModel
from typing import Optional, List

# Models for initial search that users can scroll through to pick the video they like
class SearchRequest(BaseModel):
    song: str
    artist: Optional[str] = None
    total_results: int = 1
    query_id: int

class YTResult(BaseModel):
    title: str
    video_id: str
    duration: float
    channel: Optional[str] = None

class SearchResponse(BaseModel):
    success: bool = False
    results: List[YTResult] = []
    current_index: int = 0
    total_results: int = 0

# Models for the actual download and configuring process for the MP3 file