const CONFIG = {
    // For local development and network testing, this dynamically uses the same 
    // hostname (e.g., localhost or your local IP) but points to port 8000.
    // When pushing live, change this to your production API URL 
    // (e.g., "https://api.yourdomain.com")
    API_BASE_URL: `${window.location.protocol}//${window.location.hostname}:8000`
};
