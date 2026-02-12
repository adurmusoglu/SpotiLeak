from typing import List
from models import SearchRequest, YTResult 
import yt_dlp

def search_youtube(req: SearchRequest) -> List[YTResult]:
    print()