from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class AutomationLog(Base):
    __tablename__ = "automation_logs"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    action_type = Column(String, nullable=False)
    action_time = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="success")

    document = relationship("Document", backref="automation_logs")
