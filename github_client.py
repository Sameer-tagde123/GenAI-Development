import requests
from fastapi import HTTPException, status

GITHUB_TIMEOUT = (3, 10)  # connect, read


def get_github_user(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=GITHUB_TIMEOUT)
    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="GitHub took too long to respond",
        )
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Could not reach GitHub",
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"GitHub user '{username}' not found",
        )

    if response.status_code == 403:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="GitHub rate limit reached. Try later.",
        )

    if not response.ok:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"GitHub error: {response.status_code}",
        )

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="GitHub returned invalid JSON",
        )

    return data