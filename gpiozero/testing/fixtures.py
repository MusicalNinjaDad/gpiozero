import pytest
from ..devices import Device
from ..pins.mock import MockFactory, MockPWMPin

@pytest.fixture()
def no_default_factory(request):
    save_pin_factory = Device.pin_factory
    Device.pin_factory = None
    try:
        yield None
    finally:
        Device.pin_factory = save_pin_factory

@pytest.fixture(scope='function')
def mock_factory(request):
    save_factory = Device.pin_factory
    Device.pin_factory = MockFactory()
    try:
        yield Device.pin_factory
        # This reset() may seem redundant given we're re-constructing the
        # factory for each function that requires it but MockFactory (via
        # LocalFactory) stores some info at the class level which reset()
        # clears.
    finally:
        if Device.pin_factory is not None:
            Device.pin_factory.reset()
        Device.pin_factory = save_factory

@pytest.fixture()
def pwm(request, mock_factory):
    mock_factory.pin_class = MockPWMPin