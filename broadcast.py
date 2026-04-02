#!/usr/bin/env python3


from maelstrom import Node, Request, Body

node = Node()
topology = {}
values = []

@node.handler
async def broadcast(req: Request) -> Body:
  values.append(req.body["message"])
  return {
    "type": "broadcast_ok"
  }

@node.handler
async def read(req: Request) -> Body:
  return {
    "type": "read_ok",
    "messages": values,
  }

@node.handler
async def topology(req: Request) -> Body:
  global topology
  topology = req.body["topology"]
  return {
    "type": "topology_ok",
  }

node.run()