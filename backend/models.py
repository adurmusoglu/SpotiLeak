from pydantic import BaseModel
from typing import Optional, List

class SearchRequest(BaseModel):
    song: str
    artist: Optional[str] = ""
    total_results: int
    query_id: int

class YTResult(BaseModel):
    title: str
    url: str 
    video_id: str
    duration: float
    download_url: str
    artist: Optional[str] = None
    # will need to add a way to send the mp3 file itself

class SearchResponse(BaseModel):
    success: bool
    results: List[YTResult] = []
    current_index: int = 0
    total_results: int = 0