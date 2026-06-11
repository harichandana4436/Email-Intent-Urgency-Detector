from langchain_core.prompts import PromptTemplate
from email_parser import parser


prompt = PromptTemplate(
    template="""
You are an Email Intent Detector.

Analyze the email and classify:

Intent:
- Request
- Complaint
- Information
- Inquiry
- Appreciation
- Follow-up
- Other

Urgency:
- High
- Medium
- Low

Tone:
- Urgent
- Professional
- Neutral
- Friendly
- Frustrated
- Appreciative

Rules:
- Use only the email content.
- Do not assume missing information.

{format_instructions}

Email:
{email}
""",
    input_variables=["email"],
    partial_variables={
        "format_instructions":
        parser.get_format_instructions()
    }
)