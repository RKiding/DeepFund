from graph.constants import AgentKey
from llm.prompt import INSIDER_PROMPT
from graph.schema import FundState, AnalystSignal
from llm.inference import agent_call
from apis.router import Router, APISource
from util.db_helper import get_db
from util.logger import logger

# Insider trading thresholds
thresholds = {
    "num_trades": 15,
}

def insider_agent(state: FundState):
    """Insider trading specialist analyzing insider activity patterns."""
    agent_name = AgentKey.INSIDER
    llm_config = state["llm_config"]
    ticker = state["ticker"]
    portfolio_id = state["portfolio"].id

    # Get db instance
    db = get_db()

    logger.log_agent_status(agent_name, ticker, "Fetching insider trades")
    
    # Get the insider trades
    router = Router(APISource.ALPHA_VANTAGE)
    insider_trades = router.get_us_stock_insider_trades(
        ticker=ticker,
        limit=thresholds["num_trades"],
    )
    if not insider_trades:
        return state

    # Analyze insider trading signal via LLM
    trades_dict = [m.model_dump() for m in insider_trades]
    prompt = INSIDER_PROMPT.format(num_trades=thresholds["num_trades"],trades=trades_dict)

    signal = agent_call(
        prompt=prompt,
        llm_config=llm_config,
        pydantic_model=AnalystSignal
    )

    # save signal
    logger.log_signal(agent_name, ticker, signal)
    db.save_signal(portfolio_id, agent_name, ticker, prompt, signal)
    
    return {"analyst_signals": [signal]}


