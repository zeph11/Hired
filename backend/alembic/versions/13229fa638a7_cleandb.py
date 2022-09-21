"""cleandb

Revision ID: 13229fa638a7
Revises: 
Create Date: 2022-09-21 21:44:54.775607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13229fa638a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('target_fields',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('languages', sa.ARRAY(sa.String()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_target_fields_id'), 'target_fields', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_type', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('employers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyName', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('contactNumber', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('requiredRoles', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('targetMarket', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('vision', sa.Text(), nullable=False),
    sa.Column('contactEmail', sa.String(), nullable=True),
    sa.Column('contactPerson', sa.String(), nullable=True),
    sa.Column('logo', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employers_id'), 'employers', ['id'], unique=False)
    op.create_table('mcqs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answers', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('correct_answer', sa.String(), nullable=False),
    sa.Column('target_field_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['target_field_id'], ['target_fields.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mcqs_id'), 'mcqs', ['id'], unique=False)
    op.create_table('seekers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('contactNumber', sa.String(), nullable=False),
    sa.Column('write_about_you', sa.Text(), nullable=True),
    sa.Column('yearsOfExperience', sa.Integer(), nullable=True),
    sa.Column('student', sa.Boolean(), nullable=False),
    sa.Column('skills', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('linkedIn', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('cv', sa.String(), nullable=True),
    sa.Column('githubProfile', sa.String(), nullable=True),
    sa.Column('profilePhoto', sa.String(), nullable=True),
    sa.Column('drivingLicenseNum', sa.String(), nullable=True),
    sa.Column('last_job_applied', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_seekers_id'), 'seekers', ['id'], unique=False)
    op.create_table('educations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('qualification', sa.String(), nullable=True),
    sa.Column('graduating_institution', sa.String(), nullable=True),
    sa.Column('graduating_year', sa.DateTime(), nullable=True),
    sa.Column('major', sa.String(), nullable=True),
    sa.Column('cgpa', sa.Float(), nullable=True),
    sa.Column('seeker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seeker_id'], ['seekers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_educations_id'), 'educations', ['id'], unique=False)
    op.create_table('experience',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workPlace', sa.String(length=50), nullable=True),
    sa.Column('yearsOfExperience', sa.Integer(), nullable=True),
    sa.Column('jobTitle', sa.String(length=50), nullable=True),
    sa.Column('jobStartDate', sa.DateTime(), nullable=True),
    sa.Column('jobEndDate', sa.DateTime(), nullable=True),
    sa.Column('field', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('seeker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seeker_id'], ['seekers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_experience_id'), 'experience', ['id'], unique=False)
    op.create_table('jobposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('job_location', sa.String(), nullable=False),
    sa.Column('job_level', sa.String(), nullable=False),
    sa.Column('job_type', sa.String(), nullable=False),
    sa.Column('job_responsibilities', sa.ARRAY(sa.Text()), nullable=False),
    sa.Column('skills', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('minimum_years_of_experience', sa.Integer(), nullable=False),
    sa.Column('education_required', sa.String(), nullable=False),
    sa.Column('no_of_vacancy', sa.Integer(), nullable=False),
    sa.Column('work_hours', sa.String(), nullable=False),
    sa.Column('min_salary', sa.Integer(), nullable=False),
    sa.Column('max_salary', sa.Integer(), nullable=False),
    sa.Column('job_benefits', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('job_start_date', sa.DateTime(), nullable=True),
    sa.Column('remote_onsite', sa.String(), nullable=False),
    sa.Column('status_of_jobs', sa.String(), nullable=False),
    sa.Column('posted_date', sa.DateTime(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('employer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employer_id'], ['employers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_jobposts_id'), 'jobposts', ['id'], unique=False)
    op.create_table('preferences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('expected_min_salary', sa.Integer(), nullable=False),
    sa.Column('expected_max_salary', sa.Integer(), nullable=False),
    sa.Column('preferred_location', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('interested_jobs', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('preferred_job_skills', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('remote_onsite', sa.String(), nullable=False),
    sa.Column('available_hours', sa.String(), nullable=True),
    sa.Column('seeker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seeker_id'], ['seekers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_preferences_id'), 'preferences', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_preferences_id'), table_name='preferences')
    op.drop_table('preferences')
    op.drop_index(op.f('ix_jobposts_id'), table_name='jobposts')
    op.drop_table('jobposts')
    op.drop_index(op.f('ix_experience_id'), table_name='experience')
    op.drop_table('experience')
    op.drop_index(op.f('ix_educations_id'), table_name='educations')
    op.drop_table('educations')
    op.drop_index(op.f('ix_seekers_id'), table_name='seekers')
    op.drop_table('seekers')
    op.drop_index(op.f('ix_mcqs_id'), table_name='mcqs')
    op.drop_table('mcqs')
    op.drop_index(op.f('ix_employers_id'), table_name='employers')
    op.drop_table('employers')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_target_fields_id'), table_name='target_fields')
    op.drop_table('target_fields')
    # ### end Alembic commands ###
