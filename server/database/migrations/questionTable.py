from alembic import op
import sqlalchemy as sa

# Migration identifiers
revision = "<timestamp>_create_questions_table"  # Replace with actual timestamp
down_revision = "<previous_migration_id>"  # Replace with the user table migration ID

def upgrade():
    """Create questions table"""
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("question", sa.Text(), nullable=False),
        sa.Column("option_a", sa.Text(), nullable=False),
        sa.Column("option_b", sa.Text(), nullable=False),
        sa.Column("option_c", sa.Text(), nullable=False),
        sa.Column("option_d", sa.Text(), nullable=False),
        sa.Column("correct_answer", sa.Integer(), nullable=False),
    )

def downgrade():
    """Drop questions table"""
    op.drop_table("questions")
