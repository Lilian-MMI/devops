'use strict';

const express = require('express');

// Constants
const PORT = 6060;
const HOST = '127.0.0.1';

// App
const app = express();
const server = require("http").createServer(app);
const io = require("socket.io").listen(server);
server.listen(PORT);
console.log("Server is running");
var path = require('path')
  
app.use(express.static(path.join(__dirname, 'app')));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

const connections = [];

io.sockets.on("connection", socket => {
  connections.push(socket);
  console.log(" %s sockets is connected", connections.length);

  socket.on("disconnect", () => {
    connections.splice(connections.indexOf(socket), 1);
  });
});