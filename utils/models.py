from django.db import models
from django_extensions.db.models import (CreationDateTimeField,
                                         ModificationDateTimeField)


class DatedReadonlyModelMixin(models.Model):
    """
    Base class for a model with a creation datetime field.
  """

    class Meta:
        abstract = True

    # Date/time when created.
    when_created = CreationDateTimeField(
        db_index=True,
        editable=False,
    )


class DatedReadWriteModelMixin(DatedReadonlyModelMixin):
    """
    Base class for a model object with a creation and a modification datetime field.
  """

    class Meta:
        abstract = True

    # Date/time when modified.
    when_modified = ModificationDateTimeField(
        db_index=True,
        editable=False,
    )
