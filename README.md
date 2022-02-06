# WebSocket_Python_Server_JS_Client
This is an example to get user actions to control GPIO via webpage using Javascript.

In "client.js" file : 

Line 13 - // NOTE : THIS SOCKET IS SET TO WORK WITH SSL USING WSS - IF NOT USING SSL THEN REPLACE WSS (WebSocket Secure) FOR WS (WebSocket) - IP and Port to match SERVER_INFO in server.py file.

    Using SSL : const SOCKET = new WebSocket('wss://192.168.2.20:60004');
    
    Without SSL : const SOCKET = new WebSocket('ws://192.168.2.20:60004');
    
    
In "server.py" file :

Line 179 - # SSL ACTIVATED BY DEFAULT - CAN BE CHANGED HERE - Also IP & PORT

     ws = WebsocketServer(IP="192.168.2.20", PORT=60004, USE_SSL=True) 

Line 119 - Call you own code to control GPIO or whatever you want.

     # GPIO CORE HERE

To start server.py :

      python3 server.py
