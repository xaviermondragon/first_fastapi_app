from pydantic import BaseModel


class SummaryPyLoadSchema(BaseModel):
    url: str
