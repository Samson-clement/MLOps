import pandas as pd
from typing import Dict, Any
import json
from datetime import datetime

class ModelMonitor:
    def __init__(self, reference_data_path: str):
        self.reference_data = pd.read_csv(reference_data_path)
        self.predictions_log = []
        
    def log_prediction(self, input_data: Dict[str, Any], prediction: str):
        """Log each prediction with timestamp for monitoring"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "input": input_data,
            "prediction": prediction
        }
        self.predictions_log.append(log_entry)
        
        # Save logs periodically (every 100 predictions)
        if len(self.predictions_log) >= 100:
            self._save_logs()
    
    def _save_logs(self):
        """Save prediction logs to file"""
        with open(f"logs/predictions_{datetime.now().strftime('%Y%m%d')}.json", 'a') as f:
            for log in self.predictions_log:
                f.write(json.dumps(log) + '\n')
        self.predictions_log = []