from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DocumentOut(BaseModel):
    id: int
    original_filename: str
    upload_date: datetime
    status: str
    document_type: Optional[str]

    class Config:
        from_attributes = True  # Pydantic v2
