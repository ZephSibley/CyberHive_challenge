server.py is a simple web server that takes post requests from our client.
It then writes the recieved information to a log file named after the hostname of the request originator.

### Development

Run for development with `uvicorn server:app --reload` or `python server.py`

### Production

IMPORTANT: Before starting you must add the client server(s) to the host whitelist

Run for production with ` uvicorn server:app --host 0.0.0.0 --port 8000`
