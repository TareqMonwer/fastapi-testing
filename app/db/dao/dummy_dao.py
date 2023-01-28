from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db_session
from app.db.models.dummy_model import DummyModel


class DummyDAO:
    """Class for accessing dummy table."""

    def __init__(self, session = Depends(get_db_session)):
        self.session = session

    def create_dummy_model(self, name: str) -> None:
        """
        Add single dummy to session.

        :param name: name of a dummy.
        """
        self.session.add(DummyModel(name=name))

    def get_all_dummies(self, limit: int, offset: int) -> List[DummyModel]:
        """
        Get all dummy models with limit/offset pagination.

        :param limit: limit of dummies.
        :param offset: offset of dummies.
        :return: stream of dummies.
        """
        # raw_dummies = self.session.execute(
        #     select(DummyModel).limit(limit).offset(offset),
        # )
        raw_dummies = self.session.execute(
            select(DummyModel),
        )

        return raw_dummies.scalars().fetchall()

    def filter(
        self,
        name: Optional[str] = None,
    ) -> List[DummyModel]:
        """
        Get specific dummy model.

        :param name: name of dummy instance.
        :return: dummy models.
        """
        query = select(DummyModel)
        if name:
            query = query.where(DummyModel.name == name)
        rows = self.session.execute(query)
        return rows.scalars().fetchall()
