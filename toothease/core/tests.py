import pytest
import datetime
from freezegun import freeze_time
from django.utils import timezone
from django.core.exceptions import ValidationError
from .mixins import AgeMixin
from .validators import future_date_validator, past_date_validator


def test_future_date_validator():
    future_date = datetime.date.today() + datetime.timedelta(days=1)

    with pytest.raises(ValidationError):
        future_date_validator(future_date)

    assert future_date_validator(datetime.date.today()) is None


def test_past_date_validator():
    past_date = timezone.now() - datetime.timedelta(minutes=1)

    with pytest.raises(ValidationError):
        past_date_validator(past_date)

    assert past_date_validator(timezone.now() + datetime.timedelta(minutes=1)) is None


@freeze_time("2020-01-01")
def test_mixin_age():
    class Test(AgeMixin):
        birth_date = datetime.date(1990, 1, 1)

    assert Test().age == 30
