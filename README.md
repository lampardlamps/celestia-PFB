# Celestia PFB Submission UI

This project provides a simple user interface for submitting PFBs to the Celestia blockchain network. The project consists of two main parts: a Python server using flask and an HTML/CSS frontend.

## Requirements

- Python 3.x
- Flask 2.x
- requests 2.x

## How to Run

1. Install the required packages.
2. Start the server by running `python app.py`.
3. Open a web browser and go to `http://localhost:8000` (the port is set to 8000 but you can change it to any port by modifying line 65 in the `app.py` code).
4. The Celestia nodes need to be configured to be able to receive external PFB submissions. This can be done by adding `--gateway --gateway.addr {IP address or localhost} --gateway.port 26659` when starting the node.
5. Once started, the UI looks like this (tested on a Macbook):<img width="1404" alt="UI screenshot" src="https://github.com/lampardlamps/celestia-PFB/assets/1702296/01bb5f0c-58fd-44ed-97ca-582d58a7bbe2"> The following values should be input by the user: namespace ID, data and URL (which should be the IP address of the Celestia server, including the correct port number), and after that, hit `Submit` button, and the reponse will be displayed by the box below the button.
6. To get the namespaced share, input the block height returned by the previous step, and hit the `Get namespaced share` button, and the received results will be displayed in the text box below. 


## Flask Server (app.py)

The `app.py` file contains the Flask server implementation. It provides two endpoints:

- `/submit`: This endpoint accepts POST requests with the PFB data, namespace ID, and URL. The server uses the `requests` library to submit the PFB to the Celestia network.
- `/get_namespaced_share`: This endpoint accepts POST requests with block height while retrivign the namespace ID URL from the previous `/submit` step. The server uses the `requests` library to retrieve the namespaced share at the given block height.

## Frontend (index.html)

The frontend provides a simple user interface for submitting PFBs and retrieving namespaced shares. It consists of three files:

- `index.html`: This file contains the HTML markup for the user interface, with the CSS styling integrated.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
