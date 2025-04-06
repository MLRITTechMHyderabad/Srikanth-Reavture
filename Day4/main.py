# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 12:23:28 2025

@author: 91766
"""
import json
import logging
from authorization import LaunchAuthorizationSystem

# Set up logging (console output only)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("problems detection")
logging.info("authorization successfull")
logging.warning("errors expected in feature")
logging.error("errors detected")
logging.critical("unable to proceed further")

class Warhead:
    """Represents a nuclear warhead with specific payload information."""
    
    def __init__(self, warhead_id, type, yield_kt):
        self.warhead_id = warhead_id
        self.type = type
        self.yield_kt = yield_kt  # Yield in kilotons

    def get_info(self):
        print(self.warhead_id)
        print(self.type)
        print(self.yield_kt)
        

class Submarine:
    """Controls the nuclear missile launch sequence."""
    
    def __init__(self, name, warhead_data):
        self.name = name
        self.warheads = [Warhead(**w) for w in warhead_data]

    def authorize_launch(self, auth_code):
        """Attempts to authorize and launch a missile."""
        
        """Simulates launching a missile."""
        logging.info(f"Attempting to launch missile from {self.name}...")   
        auth_system = LaunchAuthorizationSystem()
        if auth_system.validate_code(auth_code):
            logging.info("Authorization successful. Launching missile...")
            self.launch_missile()
        else:
            logging.error("Authorization failed. Launch aborted.")
            logging.critical("Critical failure in authorization system. Immediate action required!")
            print("Authorization failed. Launch aborted.")
            return False
        return True
    
        

# JSON Data (Simulating a warhead payload inventory)
warhead_json = '''
[
    {"warhead_id": "W001", "type": "Thermonuclear", "yield_kt": 1000},
    {"warhead_id": "W002", "type": "Tactical", "yield_kt": 300}
]
'''

# Load warhead data
warhead_data = json.loads(warhead_json)

# Initialize submarine
submarine = Submarine("USS Trident", warhead_data)

# 🚀 Try launching with an incorrect code
submarine.authorize_launch("INVALID-123")

# 🚀 Try launching with a valid code
submarine.authorize_launch("AUTH-XYZ123-4567-SECURE")
