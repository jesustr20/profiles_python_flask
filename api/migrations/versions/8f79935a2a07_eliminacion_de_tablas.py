"""eliminacion de tablas

Revision ID: 8f79935a2a07
Revises: 5afc5ea6980b
Create Date: 2024-04-19 20:20:39.139869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f79935a2a07'
down_revision = '5afc5ea6980b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('area')
    op.drop_table('pedidos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pedidos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('npedidos', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('category', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('code', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('numorden', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pedidos_pkey'),
    sa.UniqueConstraint('name', name='pedidos_name_key'),
    sa.UniqueConstraint('numorden', name='pedidos_numorden_key')
    )
    op.create_table('area',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombrearea', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tipo', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('seccion', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('numseccion', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('nuevaarea', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='area_pkey'),
    sa.UniqueConstraint('name', name='area_name_key'),
    sa.UniqueConstraint('numseccion', name='area_numseccion_key')
    )
    # ### end Alembic commands ###
