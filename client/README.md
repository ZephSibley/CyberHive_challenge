Requires Python 3

client.py is a Python CLI script that every 5 seconds will get a list of the processes running
on the machine and post it to a specified server.

### Development

Run for development with `python client.py -t http://SERVER_IP:PORT`

### Production

Run in production with `nohup python client.py -t http://SERVER_IP:PORT &`
