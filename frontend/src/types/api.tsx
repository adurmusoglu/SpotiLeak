export type YTResult = {
    title: string; 
    video_id: string;
    duration: number;
    channel?: string;
    // will need to add a way to receive the mp3 file itself
};

export type SearchResponse = {
    success: Boolean;
    results: YTResult[];
    current_index: number;
    total_results: number;
};