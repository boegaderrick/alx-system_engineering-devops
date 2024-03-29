#!/usr/bin/python3
"""
    This module contains a function that makes an API call
"""
from requests import get


def number_of_subscribers(subreddit):
    """
        This function sends a request to the reddit api requesting
        information about a subreddit then returns the said subreddit's
        total number of subscribers to the caller.

        @subreddit: Name of subreddit to request
        @Return: Total number of subscribers on success
               : 0 on failure
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/114.0.0.0 Safari/537.36 Edg/114.0.0.0'
    }
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code > 299:
        return 0

    response = response.json()
    return (response.get('data').get('subscribers'))
