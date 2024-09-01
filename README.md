# Proxy-Based Request Handling

This project demonstrates how to use a pool of proxies to make HTTP requests in a controlled manner. The script rotates through a list of proxy servers, ensuring that no single proxy is used too frequently.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tinmaungzin/proxy-ip.git
    cd proxy-ip
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Configure Proxy List:**

    Edit the `proxy_list` variable in the script to include your desired proxy servers.

2. **Adjust Request Settings:**

    - `MAX_REQUESTS_PER_PROXY`: The maximum number of requests allowed per proxy before switching to another.
    - `total_requests`: The total number of requests to be made.

3. **Run the Script:**

    Execute the script to start making requests:

    ```bash
    python app.py
    ```


## Script Behavior

- **Proxy Pool:** Uses a cycle of proxies to make HTTP requests.
- **Request Limiting:** Limits the number of requests per proxy to avoid overuse.
- **Error Handling:** Catches and reports errors encountered during requests.
- **Success Reporting:** Prints a success message if the request is successful and provides the proxy used.

## Code Overview

- **Proxy Pooling:** Rotates through a list of proxies using `itertools.cycle`.
- **Request Limiting:** Keeps track of requests made with each proxy to enforce limits.
- **HTTP Requests:** Makes requests to `https://jsonplaceholder.typicode.com/posts` using the selected proxy.
- **Error Handling:** Handles and reports errors with the current proxy.

## Troubleshooting

- **Proxy Issues:** Ensure that the proxies are valid and functional. Update the `proxy_list` with working proxies.
- **Request Failures:** If requests fail frequently, check the proxy server status or increase the timeout setting.
- **Rate Limiting:** Adjust `MAX_REQUESTS_PER_PROXY` and `total_requests` to better suit your use case.

