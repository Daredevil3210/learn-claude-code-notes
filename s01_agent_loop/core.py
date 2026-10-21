def run_agent2(messages:list):
    while True:
        response=client.messages.create(
            model=MODEL,system=SYSTEM,messages=messages,
            tools=TOOLS,max_tokens=8000,
        )
        messages.append({"role":"assistant","content":response.content})
        tool_calls=[block for block in response.content if block.type=="tool_use"]
        if not tool_calls:
            return
        results=[]
        for block in tool_calls:
            output=run_bash(block.input["command"])
            results.append({
                "type":"tool_result",
                "tool_use_id":block.id,
                "content":output
            })

        messages.append({"role":"user","content":results})