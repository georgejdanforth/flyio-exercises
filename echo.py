#!/usr/bin/env python3

from maelstrom import Node, Request, Body

node = Node()

@node.handler
async def echo(req: Request) -> Body:
  return {
    "type": "echo_ok",
    "echo": req.body["echo"],
    "in_reply_to": req.body["msg_id"],
  }

node.run()