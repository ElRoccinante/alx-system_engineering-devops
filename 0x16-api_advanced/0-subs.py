#!/usr/bin/python3
"""
Contains number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    
    # Reddit API endpoint for subreddit information
    url = f'http://www.reddit.com/r/{subreddit}/about.json'
    
    # Set a custom User-Agent to avoid issues with the Reddit API
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
    
    try:
        # Send GET request to Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            subreddit_info = response.json()
            
            # Extract and return the number of subscribers
            subscribers_count = subreddit_info.get("data", {}).get("subscribers", 0)
            return subscribers_count
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        # Handle exceptions (e.g., invalid subreddit or network issues)
        print(f"Exception: {e}")
        return 0

