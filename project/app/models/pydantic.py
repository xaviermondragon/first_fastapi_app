from pydantic import BaseModel


class SummaryPayLoadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummaryPayLoadSchema):
    id: int


class SummaryUpdatePayloadSchema(SummaryPayLoadSchema):
    summary: str
