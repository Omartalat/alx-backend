#!/usr/bin/env node
const redis = require("redis");

const client = redis.createClient();

client.on("connect", function () {
  console.log("Redis client connected to the server");
});

client.on("error", function (err) {
  console.log("Redis client not connected to the server:", err.toString());
});

const hashVals = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const [key, val] of Object.entries(hashVals)) {
  client.hset("HolbertonSchools", key, val, redis.print);
}

client.hgetall("HolbertonSchools", (_err, res) => {
  console.log(res);
});
