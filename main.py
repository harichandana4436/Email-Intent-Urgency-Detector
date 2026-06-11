from prompt import prompt
from model import llm
from email_parser import parser

chain = prompt | llm | parser

email = input("Enter Email:\n\n")

result = chain.invoke(
    {
        "email": email
    }
)

print("\nResult:")
print(result)