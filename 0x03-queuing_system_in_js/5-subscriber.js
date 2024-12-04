#!/usr/bin/env node
const redis = require("redis");

const client = redis.createClient();

client.on("connect", function () {
  console.log("Redis client connected to the server");
});

client.on("error", function (err) {
  console.log("Redis client not connected to the server:", err.toString());
});

const channel = 'holberton school channel';

client.subscribe(channel)
client.on('message', (_error, message) => {
    console.log(message);
    if (message == 'KILL_SERVER') {
        client.unsubscribe(channel);
        client.quit()
    }
});