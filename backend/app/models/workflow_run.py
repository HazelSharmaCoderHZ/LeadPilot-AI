from datetime import datetime

from sqlalchemy import DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class WorkflowRun(Base):
    __tablename__ = "workflow_runs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    company_name: Mapped[str] = mapped_column(String(255))
    website: Mapped[str] = mapped_column(String(500))

    status: Mapped[str] = mapped_column(String(50))
    qualification_score: Mapped[int] = mapped_column(Integer)

    workflow_data: Mapped[dict] = mapped_column(JSON)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )