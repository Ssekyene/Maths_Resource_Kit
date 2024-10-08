from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

ConceptResource = Table('concept_resource', Base.metadata,
                        Column('concept_id', String(60),
                                ForeignKey('concept.id', onupdate='CASCADE', ondelete='CASCADE'),
                                primary_key=True),
                        Column('resource_id', String(60),
                                ForeignKey('resource.id', onupdate='CASCADE', ondelete='CASCADE'),
                                primary_key=True)
                        )

class Concept(BaseModel, Base):
    """Representation of concept """

    __tablename__ = 'concept'
    name = Column(String(1024), unique=True, nullable=False)
    introduction = Column(Text, nullable=False)
    conclusion = Column(Text)
    priority = Column(Integer, nullable=False)
    quizzes = relationship('Quiz', backref='concept', cascade='all, delete-orphan')
    activities = relationship('Activity', backref='concept', cascade='all, delete-orphan')
    resources = relationship('Resource', secondary='concept_resource', backref='concepts', viewonly=False)
    description = ""
