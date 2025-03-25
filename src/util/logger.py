import os
import logging
from datetime import datetime
from graph.schema import Decision, AnalystSignal

class DeepFundLogger:
    """Logger for the Deep Fund application."""

    def __init__(self, log_level: str = 'INFO'):
        """Initialize the logger.
        
        Args:
            log_dict: Dictionary containing log configuration.
        """
        self.log_dir = os.path.join(os.getcwd(), 'logs')
        self.log_level = log_level
        
        # Create log directory if it doesn't exist
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Create logger
        self.logger = logging.getLogger("deep_fund")
        self.logger.setLevel(self.log_level)
        
        
        # Create file handler
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.log_dir, f"deepfund_{timestamp}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(self.log_level)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message: str):
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message: str):
        """Log an info message."""
        self.logger.info(message)

    def warning(self, message: str):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message: str):
        """Log an error message."""
        self.logger.error(message)

    def log_agent_status(self, agent_name: str, ticker: str, status: str):
        """Log the status of an agent."""
        if ticker:
            msg = f"Agent: {agent_name} | Ticker: {ticker} | Status: {status}"
        else:
            msg = f"Agent: {agent_name} | Status: {status}"

        self.info(msg)

    def log_decision(self, ticker: str, d: Decision):
        """Log the decision of a ticker."""
        msg = f"Decision for {ticker}: {d.action} | Reason: {d.justification}"
        self.info(msg)

    def log_signal(self, agent_name: str, ticker: str, s: AnalystSignal):
        """Log the signal of a ticker."""
        msg = f"Agent: {agent_name} | Ticker: {ticker} | Signal: {s.signal} | Justification: {s.justification}"
        self.info(msg)
        
# Create a global logger instance
logger = DeepFundLogger()
