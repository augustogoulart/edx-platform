from import_shims.warn import warn_deprecated_import

warn_deprecated_import('instructor_task.apps', 'lms.djangoapps.instructor_task.apps')

from lms.djangoapps.instructor_task.apps import *
