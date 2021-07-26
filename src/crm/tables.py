import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Staff(Base):
    __tablename__ = 'staff'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True, nullable=False)
    phone = sa.Column(sa.Numeric(30))
    password = sa.Column(sa.String)


class Client(Base):
    __tablename__ = 'client'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, unique=True, nullable=False)
    phone = sa.Column(sa.Numeric(30))
    password = sa.Column(sa.String)


class ClientRequests(Base):
    __tablename__ = 'client_requests'

    id = sa.Column(sa.Integer, primary_key=True)
    date_request = sa.Column(sa.Date)
    subject = sa.Column(sa.Text)
    type_request_id = sa.Column(sa.Integer, sa.ForeignKey("requests_type.id"))
    status_id = sa.Column(sa.Integer, sa.ForeignKey("status.id"))
    client_id = sa.Column(sa.Integer, sa.ForeignKey("client.id"))


class Status(Base):
    __tablename__ = 'status'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)


class RequestsType(Base):
    __tablename__ = 'requests_type'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)