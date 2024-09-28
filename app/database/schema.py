from datetime import datetime, timedelta

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func,
    Enum
)

class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(Datetime, nullable=False, default=func.utc_timestamp())
    modified_at = Column(Datetime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    def all_column(self):
        return [c for c in self.__table__.columns if c.primary_key is False and c.name != "create_at"]

    def __hash__(self):
        return hash(self.id)

    def create(self, session: Session, auto_commit=False, **kwargs):