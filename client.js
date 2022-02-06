/*
Author : LA
Title : WebSocket Client
Description : Javascript Websocket client, send message to server and receive message from server
Version : 0.1 - Public - Alpha Version
Date : 2022-02-05

NOTE : This is an example to send user actions to control GPIO via webpage using Javascript. - DO NOT REPRESENT FINAL VERSION
*/

const STATUS_ONLINE = "Connection Established"

// NOTE : THIS SOCKET IS SET TO WORK WITH SSL USING WSS - IF NOT USING SSL THEN REPLACE WSS (WebSocket Secure) FOR WS (WebSocket)
const SOCKET = new WebSocket('wss://192.168.2.20:60004');

// Get open event when client is connecting to server
SOCKET.addEventListener('open', function (event) {
        document.getElementById("status").innerHTML = "Status: " + "CONNECTING";
        SOCKET.send(STATUS_ONLINE);

});

// Get close event when client is disconnected of the server
SOCKET.addEventListener('close', function (event) {
        document.getElementById("status").innerHTML = "Status: " + "DISCONNECTED";
        console.log('Connection Closed.');

});

// Get message event when server send back message from client as an echo - When the server send back "Connection Established" then status is set as connected
SOCKET.addEventListener('message', function (event) {
        if (event.data == STATUS_ONLINE) {
                document.getElementById("status").innerHTML = "Status: " + STATUS_ONLINE;
        }

        console.log(event.data);

});

// Receive action ID to be send via websocket - Example : <button id="motor_forward" onclick="send_command(this.id)">Forward</button>
function send_command(action_id) {
        return SOCKET.send(action_id);
}