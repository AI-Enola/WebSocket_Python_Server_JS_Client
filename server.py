"""
Author : LA
Title : WebSocket Server
Description : Python Websocket server serve Javascript Websocket client, receive message from client and send message to client
Version : 1.0 - Public
Requirements : Python and Javascript
Date : 2022-02-05

NOTE : This is an example to get user actions to control GPIO via webpage using Javascript.

"""


# Python Library
import asyncio
import websockets
import ssl

# Custom library
from log import Log



class WebsocketServer:
    """
        Init logger, IP, PORT, SSL ( USE_SSL is set to true by default )
        Serve websocket server
        Start session for each websocket client
        Receive or send message via websocket
        
    """
    
    def __init__(self, IP=str, PORT=int, USE_SSL=bool) -> None:
        """
        Init logger ,WebSocket and SSL if using it
        WebSocket Parameters : INET - IP: 127.0.0.1 - PORT:60004 (CAN BE CHANGED)
        Return None
        """
        
        # Init logger
        log = Log(log_in_file=True, log_in_console=True, encoding='utf-8', filename='./log.txt', filemode='a', logger_name='WEBSOCKET PYTHON', format='%(name)s - %(asctime)s - %(levelname)s: %(message)s')
        self.logger = log.get_logger() # Get logger object
        
        self.logger.info(f"[SERVER WEBSOCKET] - Starting WEBSOCKET Server using IP/DOMAIN: {IP} and listening on Port: {PORT}")
        self.SERVER_INFO = [IP, PORT]
        
        self.USE_SSL = USE_SSL
        
        # Init SSL if USE_SSL is True
        if  self.USE_SSL :
            
            self.logger.info("[SERVER WEBSOCKET] - Init SSL...")
            
            """ GENERATED SSL CERTIFICATE AND KEY USING THIS COMMAND :
                openssl req -newkey rsa:4096 \
                -x509 \
                -sha256 \
                -days 3650 \
                -nodes \
                -out example.crt \
                -keyout example.key
            """
            
            SSL_CERTIFICATE = 'SSL_2022_01.crt'
            SSL_KEY = 'SSL_2022_01.key'
            
            self.SSL_CONTEXT = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            self.SSL_CONTEXT.load_cert_chain(SSL_CERTIFICATE, SSL_KEY, password=None) # We generated a non password SSL certificates and key for lab purpose
        
        
    async def serve_websocket(self) -> None:
        """
        Serve websocket
        Socket Parameters : INET - IP: 127.0.0.1 - PORT:60004 - SSL CONTEXT (CAN BE CHANGED)
        Exception raised when serving websocket failed
        Return None
        """
        
        self.logger.info("[SERVER WEBSOCKET] - Init websocket server...")
        
        try :
            
            if self.USE_SSL :
                
                self.logger.info("[SERVER WEBSOCKET] - Serving with SSL.")
                async with websockets.serve(self.session, self.SERVER_INFO[0], self.SERVER_INFO[1], ssl=self.SSL_CONTEXT):
                    await asyncio.Future()  # RUN PROGRAM FOREVER
                    
            else: 
                
                self.logger.info("[SERVER WEBSOCKET] - Serving without SSL.")
                async with websockets.serve(self.session, self.SERVER_INFO[0], self.SERVER_INFO[1]):
                    await asyncio.Future()  # RUN PROGRAM FOREVER
        except :
            self.logger.error("[SERVER WEBSOCKET] - Serving FAILED !")
            raise
            
            
    async def session(self, websocket) -> None:
        """
        Serve websocket
        Socket Parameters : INET - IP: 127.0.0.1 - PORT:60004 - SSL CONTEXT (CAN BE CHANGED)
        Exception raised when serving websocket failed
        Return None
        """
        
        self.logger.info("[SERVER WEBSOCKET] - Starting session...")
        self.websocket = websocket
        
        while True: # KEEP IT ALIVE
            
            message = str("")
            
            message = await self.receive_from_client()
            self.logger.info(f"[SERVER WEBSOCKET] - Message from client : {message}")
            
            if message : # Check if message is not empty
                
                # GPIO CORE HERE
                
                await self.send_to_client(data_out=message)
            
            
    async def receive_from_client(self) -> str:
        """
        Message variable is empty before receiving message from client
        Parameters : self
        Exception raised when receiving from websocket failed
        Return : message as str
        """
        
        self.logger.info("[SERVER WEBSOCKET] - Receiving from client...")
        
        message = str("") # Empty
        
        try : 
            message = await self.websocket.recv()
            
        except:
            
            self.logger.error(f"[SERVER WEBSOCKET] - Receiving from client FAILED!")
            raise
            
            
        if message :
            self.logger.info("[SERVER WEBSOCKET] - Message Received from client.\n")
        
        else :
            self.logger.info("[SERVER WEBSOCKET] - Message Received from client is empty !\n")
            
        return message
        
    
    
    async def send_to_client(self, data_out=str) -> None:
        """
        Send data to client via websocket
        Parameters : self, data_out as str for client
        Exception raised when sending to websocket failed
        Return : None
        """

        self.logger.info("[SERVER WEBSOCKET] - Sending to client...")
        
        try :
            await self.websocket.send(data_out)
            
        except:
            
            self.logger.error(f"[SERVER WEBSOCKET] - Sending to client FAILED!")
            raise
        
        self.logger.info("[SERVER WEBSOCKET] - Data Sended to client...\n")
        
     
   
if __name__ == "__main__":
    
    ws = WebsocketServer(IP="192.168.2.20", PORT=60004, USE_SSL=True) # SSL ACTIVATED BY DEFAULT - CAN BE CHANGED HERE - Also IP & PORT
    asyncio.run(ws.serve_websocket()) # Run program
