from biz_insight_agent.graph_builder import build_agent_graph


def test_biz_insight_agent_flow():
    test_cases = [
        {
            "input_data": {
                "today": {"revenue": 1200, "cost": 800, "customers": 10},
                "yesterday": {"revenue": 1000, "cost": 700, "customers": 10}
            }
        },
        {
            "input_data": {
                "today": {"revenue": 1000, "cost": 700, "customers": 10},
                "yesterday": {"revenue": 800, "cost": 600, "customers": 8}
            }
        },
        {
            "input_data": {
                "today": {"revenue": 600, "cost": 800, "customers": 10},
                "yesterday": {"revenue": 1000, "cost": 700, "customers": 10}
            }
        },
        {
            "input_data": {
                "today": {"revenue": 1000, "cost": 600, "customers": 10},
                "yesterday": {"revenue": 1000, "cost": 700, "customers": 10}
            }
        },
        {
            "input_data": {
                "today": {"revenue": 1500, "cost": 700, "customers": 15},
                "yesterday": {"revenue": 1000, "cost": 700, "customers": 10}
            }
        },
        {
            "input_data": {
                "today": {"revenue": 1000, "cost": 700, "customers": 0},
                "yesterday": {"revenue": 800, "cost": 600, "customers": 0}
            }
        },
        {
            "input_data": {
                "today": {"revenue": 1500, "cost": 1000, "customers": 10},
                "yesterday": {"revenue": 1400, "cost": 500, "customers": 10}
            }
        }

    ]

    agent = build_agent_graph()

    for idx, input_data in enumerate(test_cases, 1):
        print(f"Test case {idx}")
        result = agent.invoke(input_data)

        assert isinstance(result, dict), "Result must be a dict"
        assert "recommendations" in result, "Missing 'recommendations' in output"

        rec = result["recommendations"]

        assert "profit" in rec, "Missing 'profit' in recommendations"
        assert "cac" in rec, "Missing 'cac' in recommendations"
        assert "alerts" in rec, "Missing 'alerts' in recommendations"
        assert isinstance(rec["alerts"], list), "'alerts' must be a list"

        print("✅ Output:")
        print(rec)
        print("-" * 40)


if __name__ == "__main__":
    test_biz_insight_agent_flow()
