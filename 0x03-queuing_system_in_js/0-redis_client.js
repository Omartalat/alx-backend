#!/usr/bin/env node
const redis = require("redis");

const client = redis.createClient();

client.on("connect", function () {
  console.log("Redis client connected to the server");
});

client.on("error", function (err) {
  console.log("Redis client not connected to the server:", err.toString());
});
