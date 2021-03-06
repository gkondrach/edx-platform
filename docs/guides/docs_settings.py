"""
Django settings for use when generating API documentation.
Basically the LMS devstack settings plus a few items needed to successfully
import all the Studio code.
"""
from __future__ import absolute_import, unicode_literals

import os

if os.environ['EDX_PLATFORM_SETTINGS'] == 'devstack_docker':
    from lms.envs.devstack_docker import *
    from cms.envs.devstack_docker import (
        ADVANCED_PROBLEM_TYPES,
        COURSE_IMPORT_EXPORT_STORAGE,
        SCRAPE_YOUTUBE_THUMBNAILS_JOB_QUEUE,
        VIDEO_TRANSCRIPT_MIGRATIONS_JOB_QUEUE,
    )
else:
    from lms.envs.devstack import *
    from cms.envs.devstack import (
        ADVANCED_PROBLEM_TYPES,
        COURSE_IMPORT_EXPORT_STORAGE,
        SCRAPE_YOUTUBE_THUMBNAILS_JOB_QUEUE,
        VIDEO_TRANSCRIPT_MIGRATIONS_JOB_QUEUE,
    )

FEATURES['ENABLE_LTI_PROVIDER'] = True

INSTALLED_APPS.extend([
    'contentstore.apps.ContentstoreConfig',
    'course_creators',
    'xblock_config.apps.XBlockConfig',
    'user_tasks',
    'lti_provider'
])
