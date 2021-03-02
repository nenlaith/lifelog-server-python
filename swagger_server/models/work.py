from swagger_server.models import Period


class Work(Period):
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'column_prefix': __tablename__ + '_'
    }
