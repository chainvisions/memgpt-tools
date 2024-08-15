# fetch_oura_scores

This tool is used for fetching Oura Ring (smart wearable) data on sleep, readiness, and activity scores, alongside Oura's official rating for each of the score.

Output usually looks something like:

```
Today's scores are: Sleep - 71 (Good) Activity - 52 (Pay Attention) Readiness - 81 (Good)
```

## Usage

To use this tool you will need to [create an Oura Cloud API personal access token](https://cloud.ouraring.com/personal-access-tokens) and add it here in the tool's code:
```
    OURA_ACCESS_TOKEN = "<access token here>"
```