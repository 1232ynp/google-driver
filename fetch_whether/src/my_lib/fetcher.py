import requests
import pandas as pd


def fetch_max_temperature(target_date: str) -> pd.DataFrame:
    """Fetch max temperature to Open-Meteo.

    Args:
        target_date (str): Date for which to retrieve data.

    Returns:
        pd.DataFrame: df of the acquired data.

    Raises:
        RequestException: HTTP status code other than 200.
    """
    endpoint = "https://api.open-meteo.com/v1/forecast?" \
               "latitude=35.69&longitude=139.69&" \
               "daily=temperature_2m_max&" \
               "timezone=Asia%2FTokyo&" \
               "start_date=" + target_date + "&end_date=" + target_date

    try:
        res = requests.get(endpoint)
        res.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise err

    result = res.json()
    daily_max_temperature = float(result['daily']['temperature_2m_max'][0])

    df = pd.DataFrame(
        [
            {
                "date": target_date,
                "place": "Tokyo",
                "daily_max_temperature": daily_max_temperature
            }
        ]
    )

    return df


def fetch_max_wind_speed(target_date: str) -> pd.DataFrame:
    """Fetch max wind speed to Open-Meteo.

    Args:
        target_date (str): Date for which to retrieve data.

    Returns:
        pd.DataFrame: df of the acquired data.

    Raises:
        RequestException: HTTP status code other than 200.
    """
    endpoint = "https://api.open-meteo.com/v1/forecast?" \
               "latitude=35.69&longitude=139.69&" \
               "daily=windspeed_10m_max&" \
               "timezone=Asia%2FTokyo&" \
               "start_date=" + target_date + "&end_date=" + target_date

    try:
        res = requests.get(endpoint)
        res.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise err

    result = res.json()
    daily_max_wind_speed = (result['daily']['windspeed_10m_max'][0])

    df = pd.DataFrame(
        [
            {
                "date": target_date,
                "place": "tokyo",
                "daily_max_wind_speed": daily_max_wind_speed
            }
        ]
    )

    return df
