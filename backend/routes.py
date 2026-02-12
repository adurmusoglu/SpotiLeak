from fastapi import APIRouter
from models import SearchRequest, SearchResponse
from services.search_service import search_youtube

router = APIRouter()

@router.get("/")
def health_check():
    return {"status" : "SpotiLeak Backend API Connected..."}

@router.post("/api/search", response_model=SearchResponse)
def search(req: SearchRequest) -> SearchResponse:
    # Cleans up the query object
    song = req.song.strip()
    artist = req.artist.strip() if req.artist else None
    artist = artist or None
    cleaned_req = SearchRequest(song=song, 
                            artist=artist, 
                            total_results=req.total_results,
                            query_id=req.query_id)

    results = search_youtube(cleaned_req)
    return SearchResponse(success=True, 
                          results=results,
                          current_index=0,
                          total_results=len(results))
    


