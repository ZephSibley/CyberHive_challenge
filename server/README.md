server.py is a simple web server that takes post requests from our client.
It then writes the recieved information to a log file named after the hostname of the request originator.

Run with `uvicorn server:app --reload` or `python server.py`
