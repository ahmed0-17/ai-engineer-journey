"""merge A and B

Revision ID: 8943978544e2
Revises: e89f7f5442fa, 6e105f1b4e85
Create Date: 2026-11-04 03:49:22.911449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8943978544e2'
down_revision: Union[str, Sequence[str], None] = ('e89f7f5442fa', '6e105f1b4e85')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
