#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpRigToolkit-libs-spaceswitcher
"""

from __future__ import print_function, division, absolute_import

import os
import logging.config

from tpDcc.core import library

from tpRigToolkit.libs.spaceswitcher.core import consts


class SpaceSwitcherLib(library.DccLibrary, object):

    ID = consts.LIB_ID

    def __init__(self, *args, **kwargs):
        super(SpaceSwitcherLib, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls):
        base_tool_config = library.DccLibrary.config_dict()
        tool_config = {
            'name': 'Space Switcher Library',
            'id': cls.ID,
            'supported_dccs': {'maya': ['2017', '2018', '2019', '2020']},
            'tooltip': 'Library that contains library to create space switch setups'
        }
        base_tool_config.update(tool_config)

        return base_tool_config


def create_logger(dev=False):
    """
    Creates logger for current tpRigToolkit-libs-spaceswitcher package
    """

    logger_directory = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpRigToolkit', 'logs', 'libs'))
    if not os.path.isdir(logger_directory):
        os.makedirs(logger_directory)

    logging_config = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '__logging__.ini'))

    logging.config.fileConfig(logging_config, disable_existing_loggers=False)
    logger = logging.getLogger('tpRigToolkit-libs-spaceswitcher')
    dev = os.getenv('TPRIGTOOLKIT_DEV', dev)
    if dev:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger


create_logger()
