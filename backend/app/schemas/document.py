from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DocumentOut(BaseModel):
    id: int
    file_name: str
    upload_date: datetime
    status: str
    document_type: Optional[str]

    class Config:
        orm_mode = True
