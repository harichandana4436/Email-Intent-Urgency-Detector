from pydantic import BaseModel
from langchain_core.output_parsers import JsonOutputParser


class EmailAnalysis(BaseModel):
    intent: str
    urgency: str
    tone: str


parser = JsonOutputParser(
    pydantic_object=EmailAnalysis
)