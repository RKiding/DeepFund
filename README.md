# DeepFund

[![arXiv](https://img.shields.io/badge/arXiv-2503.18313-<COLOR>.svg)](https://arxiv.org/abs/2503.18313)

This project serves as an ideal solution to the below key question:

**Will LLM Be Professional At Fund Investment? A Live Arena perspective**

We evaluate the trading capability of LLM across various financial markets given a unified environment. The LLM shall ingest external information, drive a multi-agent system, and make trading decisions. The LLM performance will be presented in a trading arena view across various dimensions. 


> Disclaimer: This project is for educational and research purposes only, **it does not trade actually.**

## Framework
![Framework](./image/framework.png)



## Setup Environment
Pre-requisite: Install Conda (if not already installed): Go to [anaconda.com/download](https://www.anaconda.com/download/).

1. Clone the repository:
```bash
git clone https://github.com/tigerlcl/deepfund.git
cd deepfund
```

2. Create a virtual env from the env configuration file:
```bash
conda env create -f environment.yml
```

3. Set up environment variables:
```bash
# Create .env file for your API keys (OpenAI, DeepSeek, etc.)
cp .env.example .env
```

## Setup Database
We apply **SQLite** as the database to store the agent activities and portfolio status when running the system.

```bash
cd src
python database/setup.py
# This will create a sqlite database in the path `src/assets/deepfund.db`
```
 You may install VSCode Extension [SQLite Viewer](https://marketplace.cursorapi.com/items?itemName=qwtel.sqlite-viewer) to view the database.

### Relation Diagram
ERD is generated by [drawdb](https://drawdb.app/)

<p align="center">
  <img src="./image/DeepFund_ERD.png" alt="DeepFund ERD" width="400"/>
  <br>
  <em>DeepFundDB covers four tables: Config, Portfolio, Decision, and Signal</em>
</p>


## Running the System
Enter the `src` directory and run the `main.py` file with configuration:
```bash
cd src
python main.py --config xxx.yaml
```
Configs are saved in `src/config`. Below is a sample config file:
```yaml
# Deep Fund Configuration
exp_name: "my_unique_exp_name"

# Trading settings
tickers:
  - MSFT
  - NVDA

# Analysts to run, refer to graph.constants.py
workflow_analysts:
  - fundamental
  - technical
  - news


# LLM model settings, refer to llm/inference.py
llm:
  provider: "DeepSeek" 
  model: "deepseek-chat"
```

Comment out `workflow_analysts` configs to run planner. Planner agent coordinates which analysts to run and cook signals for portfolio manager.

## Expected Output
Please refer to `src/example` for the expected output.
> Running fact: time 36 sec, LLM cost: 0.01 CNY

## Project Structure 
```
deepfund/
├── src/
│   ├── main.py                   # Main entry point
│   ├── agents/                   # Agent build and registry
│   ├── apis/                     # APIs for external financial data
│   ├── config/                   # Configuration files
│   ├── database/                 # Database setup and helper
│   ├── example/                  # Example log and db
│   ├── graph/                    # Workflow, prompt, and schema
│   ├── llm/                      # LLM providers
│   ├── util/                     # Utility functions and helpers
├── environment.yml               # For Conda
├── README.md                     # Project documentation
├── ...
```


## Data Source Dependency
- Alpha Vantage API, [Claim Free API Key](https://www.alphavantage.co/support/#support)
  - Fundamental Analyst
  - Insider Trades Analyst
  - Technical Analyst
- YFinance API (No API Key Required)
  - News Analysts
  - Portfolio Manager


## Acknowledgements
The project gets inspiration from the following projects:
- [Cursor AI](https://www.cursor.com/), The AI Code Editor
- [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund), An AI Hedge Fund Team
- [LangGraph](https://langchain-ai.github.io/langgraph/tutorials/workflows), Tutorial on Workflows and Agents
- [OpenManus](https://github.com/mannaandpoem/OpenManus), An open-source framework for building general AI agents

## Roadmap
> We are working on the following features. Collaborate with us!
- MCPify Deepfund
  - Turn APIs as LLM tools
  - Renovate the database query style
- Extend Financial Markets
- More ...

## License
This project is licensed under the MIT License - see the LICENSE file for details.
