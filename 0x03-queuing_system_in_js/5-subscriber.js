#!/usr/bin/node
import { createClient } from "redis";

const client = createClient();
const Exit_MSG = "KILL_SERVER";

client.on_connect("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

client.on_connect("connect", () => {
  console.log("Redis client connected to the server");
});

client.subscribe("holberton school channel");

client.on_connect("message", (_err, msg) => {
  console.log(msg);
  if (msg === Exit_MSG) {
    client.unsubscribe();
    client.quit();
  }
});
