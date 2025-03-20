# AP22110011192
# FastAPI Sliding Window API

## Overview
This is a FastAPI-based microservice that fetches numbers from third-party APIs and maintains a sliding window of recent numbers. The service processes API requests, ensures uniqueness within the window, and calculates the average of the stored numbers.

## Features
- Fetch numbers from different categories: Prime, Fibonacci, Even, and Random.
- Maintain a sliding window of recent numbers (default size: 10).
- Avoid duplicates in the stored numbers.
- Compute the average of the numbers in the sliding window.
- Uses mock data instead of actual third-party API calls for quick testing.

## Endpoints
### GET /numbers/{number_id}
Fetches numbers from the specified category and updates the sliding window.

#### Parameters:
- number_id (string): The category of numbers to fetch. Accepted values:
  - p → Prime numbers
  - f → Fibonacci numbers
  - e → Even numbers
  - r → Random numbers

#### Response:
json
{
  "windowPrevState": [2, 3, 5],
  "windowCurrState": [2, 3, 5, 7],
  "numbers": [7],
  "avg": 4.25
}


## Installation & Running
### Prerequisites:
- Python 3.8+
- FastAPI
- Uvicorn
- Requests (if using real API calls)

### Install dependencies:
sh
pip install fastapi uvicorn requests


### Run the API server:
sh
uvicorn main:app --reload


### Test the API:
Open your browser or use a tool like curl or Postman to test:
sh
curl -X GET "http://127.0.0.1:8000/numbers/p"
