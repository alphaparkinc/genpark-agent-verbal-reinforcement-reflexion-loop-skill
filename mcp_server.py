"""
MCP Server for genpark-agent-verbal-reinforcement-reflexion-loop-skill
Standard JSON-RPC 2.0 protocol over stdio.
"""

import sys
import json
from client import AgentReflexionLoopClient

client = AgentReflexionLoopClient()

def handle_request(req):
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "reflect_on_trial",
                        "description": "Analyze trial failure trajectory and generate verbal reflection.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "task_goal": {"type": "string"},
                                "trajectory_steps": {"type": "array"},
                                "error_message": {"type": "string"}
                            },
                            "required": ["task_goal", "trajectory_steps", "error_message"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "reflect_on_trial":
            res = client.reflect_on_trial(args.get("task_goal", ""), args.get("trajectory_steps", []), args.get("error_message", ""))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
