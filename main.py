from biz_insight_agent.graph_builder import build_agent_graph

agent = build_agent_graph()


input_data = {
    "input_data": {
        "today": {
            "revenue": 1200,
            "cost": 700,
            "customers": 35
        },
        "yesterday": {
            "revenue": 1000,
            "cost": 500,
            "customers": 40
        }
    }
}

result = agent.invoke(input_data)
print(result)
