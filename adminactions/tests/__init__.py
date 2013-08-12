from django.conf import settings
from .mass_update import *  # NOQA
from .exports import *  # NOQA
from .merge import MergeTest, MergeTestApi  # NOQA

if getattr(settings, 'ENABLE_SELENIUM', True):
    try:
        import selenium  # NOQA
        from .selenium_tests import *  # NOQA
    except ImportError:
        import warnings

        warnings.warn('Unable load Selenium. Selenium tests will be disabled')


from adminactions.utils import get_field_value, get_field_by_path, get_verbose_name, flatten

__test__ = {
    'get_field_value': get_field_value,
    'get_field_by_path': get_field_by_path,
    'get_verbose_name': get_verbose_name,
    'flatten': flatten,


}
