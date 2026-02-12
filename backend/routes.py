from fastapi import APIRouter
from models import SearchRequest, YTResult, SearchResponse
from services.search_service import search_youtube

router = APIRouter()

@router.get("/")
def health_check():
    return {"status" : "SpotiLeak Backend API Connected..."}

@router.post("/api/search", response_model=SearchResponse)
def search(req: SearchRequest) -> SearchResponse:
    # Cleans up the query object
    req.song = req.song.strip()
    req.artist = req.artist.strip() if req.artist else None
    if req.artist == "":
        req.artist=None

    results = search_youtube(req)
    return SearchResponse(success=True if len(results) > 0 else False, 
                          results=results,
                          current_index=0,
                          total_results=len(results))
    


