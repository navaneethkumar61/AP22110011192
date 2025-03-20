from fastapi import FastAPI, HTTPException
import requests
import time
from collections import deque

app = FastAPI()

# Configuration
WINDOW_SIZE = 10
THIRD_PARTY_API = {
    'p': 'https://prime-numbers-api.com/api/v1/primes?limit={}',
    'f': 'https://fibonacci-api.com/api/v1/fibonacci?limit={}',
    'e': 'https://api.math.tools/numbers/even?limit={}',
    'r': 'https://www.random.org/integers/?num={}&min=1&max=100&col=1&base=10&format=plain&rnd=new'
}
VALID_IDS = {"p", "f", "e", "r"}

# Sliding window to store numbers
stored_numbers = deque(maxlen=WINDOW_SIZE)

def fetch_numbers(number_id: str):
    """Fetch numbers from third-party API with a 500ms timeout."""
    mock_data = {
        "p": [2, 3, 5, 7],
        "f": [1, 1, 2, 3, 5],
        "e": [2, 4, 6, 8],
        "r": [9, 14, 27, 32]
    }
    return mock_data.get(number_id, [])
    # try:
    #     start_time = time.time()
    #     url = THIRD_PARTY_API[number_id].format(WINDOW_SIZE)
    #     response = requests.get(url, timeout=0.5)
    #     elapsed_time = time.time() - start_time

    #     if response.status_code == 200 and elapsed_time <= 0.5:
    #         if number_id == 'r':
    #             # Random.org returns plain text; convert to integers
    #             return list(map(int, response.text.strip().split()))
    #         else:
    #             return response.json().get("numbers", [])
    #     else:
    #         return []
    # except requests.RequestException:
    #     return []

@app.get("/numbers/{number_id}")
def get_numbers(number_id: str):
    """Process API request and maintain a sliding window."""
    if number_id not in VALID_IDS:
        raise HTTPException(status_code=400, detail="Invalid number ID")

    window_prev_state = list(stored_numbers)  # Before fetching new numbers
    new_numbers = fetch_numbers(number_id)

    # Store only unique numbers and respect window size
    for num in new_numbers:
        if num not in stored_numbers:
            stored_numbers.append(num)

    window_curr_state = list(stored_numbers)  # After inserting new numbers
    avg = round(sum(stored_numbers) / len(stored_numbers), 2) if stored_numbers else 0.0

    return {
        "windowPrevState": window_prev_state,
        "windowCurrState": window_curr_state,
        "numbers": new_numbers,
        "avg": avg
    }
