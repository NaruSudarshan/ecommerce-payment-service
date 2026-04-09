import os

# SCENARIO 1: The True Positive (ASTra MUST catch this)
aws_secret_key = "AKIA_REAL_SECRET_123"

# SCENARIO 2: The False Positive Comment (ASTra MUST ignore this)
# Do not hardcode the password="AKIA_FAKE_SECRET_456"

# SCENARIO 3: The False Positive Docstring (ASTra MUST ignore this)
"""
Example database configuration:
db_password = "SUPER_SECRET_789"
"""

# SCENARIO 4: The Safe Dynamic Variable (ASTra MUST ignore this)
safe_api_key = os.getenv("API_KEY")
