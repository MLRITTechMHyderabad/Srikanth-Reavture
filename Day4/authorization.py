import re
import json
import logging

# Set up logging (console output only)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("problems detection")
logging.info("authorization successfull")
logging.warning("errors expected in feature")
logging.error("errors detected")
logging.critical("unable to proceed further")




class LaunchAuthorizationSystem:
    """Handles nuclear launch authorization validation."""
    
    AUTH_PATTERN =r"^[A-Z]+-[A-Z0-9]+-[0-9]{1,4}-[A-Z]+$"# Regex for security code validation

    @staticmethod
    def validate_code(code):
        """Validates the launch authorization code."""
        return bool(re.match(LaunchAuthorizationSystem.AUTH_PATTERN, code))

print(LaunchAuthorizationSystem.validate_code("APSE-XX66-1234-ASSV"))
