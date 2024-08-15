def fetch_oura_scores(self) -> str:
    """
    Fetches the daily Oura Ring scores.

    This function fetches the daily Oura Ring score values for today. Including sleep, activity, etc
    from the Oura API and returns them in the form of a string.

    Args:
        None

    Return:
        str: Today's Oura Ring scores, or an error message if one occured.

    Raises:
        RequestException: If an error occured while fetching any Oura score data.

    Example:
        >>> fetch_oura_scores()
        "Today's scores are: Sleep - 85 (Optimal) Readiness - 61 (Fair) Activity - 50 (Pay Attention)
    """
    from requests import request, RequestException
    import datetime

    # Base request info that we can reuse.
    OURA_ACCESS_TOKEN = "<access token here>"
    yesterday_date = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    today_date = datetime.date.today().isoformat()
    request_headers = {"Authorization":  f"Bearer {OURA_ACCESS_TOKEN}"}
    params = {"start_date": yesterday_date, "end_date": today_date}

    # Fetch activity data
    activity_score = 0
    try:
        activity_res = (request("GET", "https://api.ouraring.com/v2/usercollection/daily_activity", params=params, headers=request_headers)).json()
        activity_score = activity_res["data"][0]["score"]
    except RequestException:
        return "An error occured while trying to fetch Oura activity data"
    
    # Fetch sleep data
    sleep_score = 0
    try:
        sleep_res = (request("GET", "https://api.ouraring.com/v2/usercollection/daily_sleep", params=params, headers=request_headers)).json()
        sleep_score = sleep_res["data"][1]["score"]
    except RequestException:
        return "An error occured while trying to fetch Oura sleep data"

    # Fetch readiness score
    readiness_score = 0
    try:
        readiness_res = (request("GET", "https://api.ouraring.com/v2/usercollection/daily_readiness", params=params, headers=request_headers)).json()
        readiness_score = readiness_res["data"][1]["score"]
    except RequestException:
        return "An error occured while trying to fetch Oura readiness data"

    def rate_score(score: int) -> str:
        if score >= 85:
            return "Optimal"
        elif score >= 70:
            return "Good"
        elif score >= 60:
            return "Fair"
        elif score >= 0:
            return "Pay Attention"

    # Return score data.
    return f"Today's scores are: Sleep - {sleep_score} ({rate_score(sleep_score)}) Activity - {activity_score} ({rate_score(activity_score)}) Readiness - {readiness_score} ({rate_score(readiness_score)})"