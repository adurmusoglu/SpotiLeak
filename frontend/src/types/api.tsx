export type YTResult = {
    title: string; 
    url: string;
    video_id: string;
    duration: number;
    download_url: string;
    artist?: string;
    // will need to add a way to send the mp3 file itself
};

export type SearchResponse = {
    success: Boolean;
    results: YTResult[];
    current_index: number;
    total_results: number;
};