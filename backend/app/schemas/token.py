from pydantic import BaseModel

class Token(BaseModel):
    """
    This is the Pydantic schema for our JWT response.
    It defines what the JSON will look like when we send a token.
    """
    access_token: str
    token_type: str # This will always be 'bearer'
