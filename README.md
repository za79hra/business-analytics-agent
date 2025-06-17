# BizInsightAgent

**BizInsightAgent** is a business analytics tool that uses a graph-based architecture to calculate key financial metrics such as **profit**, **Customer Acquisition Cost (CAC)**, and provide **strategic alerts** based on daily performance data.

## Features

- Automatically calculates profit and CAC from provided input data (today vs. yesterday)
- Analyzes percentage changes in revenue, cost, and CAC
- Generates helpful management alerts based on performance
- Built on a graph-based architecture using **LangGraph**
- Includes test coverage and a Jupyter Notebook demo

## How to Use

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Run a basic test**  
   ```bash
   python -m biz_insight_agent.tests.test_agent
   ```

3. **Try the demo (Jupyter Notebook)**  
   Open and run `demo/demo.ipynb` in your Jupyter environment.

4. **Run the main application**  
   ```bash
   python main.py
   ```

## Important Notes

- If the number of customers (`customers`) is **zero**, the CAC will return as `inf` (infinity).  
  This indicates that CAC cannot be calculated due to a division by zero, and it's a valid fallback to prevent application crashes.

- Alerts are generated dynamically based on computed metrics, helping guide business decisions (e.g., cost reduction, budget increases).

## Project Structure

```
biz_insight_agent/
│
├── agent/
│   ├── __init__.py
│   ├── nodes.py
│   ├── graph_builder.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_agent.py
│
├── demo/
│   └── demo.ipynb
│
├── main.py
├── requirements.txt
└── README.md
```

---

Feel free to submit feedback or suggestions!
