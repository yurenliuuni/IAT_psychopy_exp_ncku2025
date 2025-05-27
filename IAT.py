#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Sun Mar 30 15:37:36 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_A1
key_resp_A1_corr_sum = 0.0
key_resp_A1_rt_sum = 0.0

# Run 'Before Experiment' code from code_A2
key_resp_A2_corr_sum = 0.0
key_resp_A2_rt_sum = 0.0

# Run 'Before Experiment' code from code_B1
key_resp_B1_corr_sum = 0.0
key_resp_B1_rt_sum = 0.0
# Run 'Before Experiment' code from code_B2
key_resp_B2_corr_sum = 0.0
key_resp_B2_rt_sum = 0.0
# Run 'Before Experiment' code from code_C1
key_resp_C1_corr_sum = 0.0
key_resp_C1_rt_sum = 0.0
# Run 'Before Experiment' code from code_C2
key_resp_C2_corr_sum = 0.0
key_resp_C2_rt_sum = 0.0
# Run 'Before Experiment' code from code_C3
key_resp_C3_corr_sum = 0.0
key_resp_C3_rt_sum = 0.0
# Run 'Before Experiment' code from code_D1
key_resp_D1_corr_sum = 0.0
key_resp_D1_rt_sum = 0.0
# Run 'Before Experiment' code from code_E1
key_resp_E1_corr_sum = 0.0
key_resp_E1_rt_sum = 0.0
# Run 'Before Experiment' code from code_E2
key_resp_E2_corr_sum = 0.0
key_resp_E2_rt_sum = 0.0
# Run 'Before Experiment' code from code_E3
key_resp_E3_corr_sum = 0.0
key_resp_E3_rt_sum = 0.0
# Run 'Before Experiment' code from code_F1
key_resp_F1_corr_sum = 0.0
key_resp_F1_rt_sum = 0.0

# Run 'Before Experiment' code from code_G1
key_resp_G1_corr_sum = 0.0
key_resp_G1_rt_sum = 0.0
# Run 'Before Experiment' code from code_G2
key_resp_G2_corr_sum = 0.0
key_resp_G2_rt_sum = 0.0
# Run 'Before Experiment' code from code_G3
key_resp_G3_corr_sum = 0.0
key_resp_G3_rt_sum = 0.0

# Run 'Before Experiment' code from code_H1
key_resp_H1_corr_sum = 0.0
key_resp_H1_rt_sum = 0.0
# Run 'Before Experiment' code from code_I1
key_resp_I1_corr_sum = 0.0
key_resp_I1_rt_sum = 0.0
# Run 'Before Experiment' code from code_I2
key_resp_I2_corr_sum = 0.0
key_resp_I2_rt_sum = 0.0
# Run 'Before Experiment' code from code_I3
key_resp_I3_corr_sum = 0.0
key_resp_I3_rt_sum = 0.0
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'IAT'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1280, 800]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/xiaodantong/Desktop/MyPsyPyExpt/Subfolder/IAT/IAT.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0.6549, 0.6549, 0.6549], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.6549, 0.6549, 0.6549]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_22') is None:
        # initialise key_resp_22
        key_resp_22 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_22',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp_A1') is None:
        # initialise key_resp_A1
        key_resp_A1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_A1',
        )
    if deviceManager.getDevice('key_resp_score') is None:
        # initialise key_resp_score
        key_resp_score = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_score',
        )
    if deviceManager.getDevice('key_resp_23') is None:
        # initialise key_resp_23
        key_resp_23 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_23',
        )
    if deviceManager.getDevice('key_resp_A2') is None:
        # initialise key_resp_A2
        key_resp_A2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_A2',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp_24') is None:
        # initialise key_resp_24
        key_resp_24 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_24',
        )
    if deviceManager.getDevice('key_resp_B1') is None:
        # initialise key_resp_B1
        key_resp_B1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_B1',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    if deviceManager.getDevice('key_resp_25') is None:
        # initialise key_resp_25
        key_resp_25 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_25',
        )
    if deviceManager.getDevice('key_resp_B2') is None:
        # initialise key_resp_B2
        key_resp_B2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_B2',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('key_resp_26') is None:
        # initialise key_resp_26
        key_resp_26 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_26',
        )
    if deviceManager.getDevice('key_resp_C1') is None:
        # initialise key_resp_C1
        key_resp_C1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_C1',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_resp_27') is None:
        # initialise key_resp_27
        key_resp_27 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_27',
        )
    if deviceManager.getDevice('key_resp_C2') is None:
        # initialise key_resp_C2
        key_resp_C2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_C2',
        )
    if deviceManager.getDevice('key_resp_7') is None:
        # initialise key_resp_7
        key_resp_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_7',
        )
    if deviceManager.getDevice('key_resp_28') is None:
        # initialise key_resp_28
        key_resp_28 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_28',
        )
    if deviceManager.getDevice('key_resp_C3') is None:
        # initialise key_resp_C3
        key_resp_C3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_C3',
        )
    if deviceManager.getDevice('key_resp_8') is None:
        # initialise key_resp_8
        key_resp_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_8',
        )
    if deviceManager.getDevice('key_resp_29') is None:
        # initialise key_resp_29
        key_resp_29 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_29',
        )
    if deviceManager.getDevice('key_resp_D1') is None:
        # initialise key_resp_D1
        key_resp_D1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_D1',
        )
    if deviceManager.getDevice('key_resp_9') is None:
        # initialise key_resp_9
        key_resp_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_9',
        )
    if deviceManager.getDevice('key_resp_30') is None:
        # initialise key_resp_30
        key_resp_30 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_30',
        )
    if deviceManager.getDevice('key_resp_E1') is None:
        # initialise key_resp_E1
        key_resp_E1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_E1',
        )
    if deviceManager.getDevice('key_resp_10') is None:
        # initialise key_resp_10
        key_resp_10 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_10',
        )
    if deviceManager.getDevice('key_resp_31') is None:
        # initialise key_resp_31
        key_resp_31 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_31',
        )
    if deviceManager.getDevice('key_resp_E2') is None:
        # initialise key_resp_E2
        key_resp_E2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_E2',
        )
    if deviceManager.getDevice('key_resp_11') is None:
        # initialise key_resp_11
        key_resp_11 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_11',
        )
    if deviceManager.getDevice('key_resp_40') is None:
        # initialise key_resp_40
        key_resp_40 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_40',
        )
    if deviceManager.getDevice('key_resp_E3') is None:
        # initialise key_resp_E3
        key_resp_E3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_E3',
        )
    if deviceManager.getDevice('key_resp_12') is None:
        # initialise key_resp_12
        key_resp_12 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_12',
        )
    if deviceManager.getDevice('key_resp_32') is None:
        # initialise key_resp_32
        key_resp_32 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_32',
        )
    if deviceManager.getDevice('key_resp_F1') is None:
        # initialise key_resp_F1
        key_resp_F1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_F1',
        )
    if deviceManager.getDevice('key_resp_13') is None:
        # initialise key_resp_13
        key_resp_13 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_13',
        )
    if deviceManager.getDevice('key_resp_33') is None:
        # initialise key_resp_33
        key_resp_33 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_33',
        )
    if deviceManager.getDevice('key_resp_G1') is None:
        # initialise key_resp_G1
        key_resp_G1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_G1',
        )
    if deviceManager.getDevice('key_resp_14') is None:
        # initialise key_resp_14
        key_resp_14 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_14',
        )
    if deviceManager.getDevice('key_resp_35') is None:
        # initialise key_resp_35
        key_resp_35 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_35',
        )
    if deviceManager.getDevice('key_resp_G2') is None:
        # initialise key_resp_G2
        key_resp_G2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_G2',
        )
    if deviceManager.getDevice('key_resp_15') is None:
        # initialise key_resp_15
        key_resp_15 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_15',
        )
    if deviceManager.getDevice('key_resp_34') is None:
        # initialise key_resp_34
        key_resp_34 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_34',
        )
    if deviceManager.getDevice('key_resp_G3') is None:
        # initialise key_resp_G3
        key_resp_G3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_G3',
        )
    if deviceManager.getDevice('key_resp_16') is None:
        # initialise key_resp_16
        key_resp_16 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_16',
        )
    if deviceManager.getDevice('key_resp_H1') is None:
        # initialise key_resp_H1
        key_resp_H1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_H1',
        )
    if deviceManager.getDevice('key_resp_19') is None:
        # initialise key_resp_19
        key_resp_19 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_19',
        )
    if deviceManager.getDevice('key_resp_17') is None:
        # initialise key_resp_17
        key_resp_17 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_17',
        )
    if deviceManager.getDevice('key_resp_37') is None:
        # initialise key_resp_37
        key_resp_37 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_37',
        )
    if deviceManager.getDevice('key_resp_I1') is None:
        # initialise key_resp_I1
        key_resp_I1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_I1',
        )
    if deviceManager.getDevice('key_resp_18') is None:
        # initialise key_resp_18
        key_resp_18 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_18',
        )
    if deviceManager.getDevice('key_resp_38') is None:
        # initialise key_resp_38
        key_resp_38 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_38',
        )
    if deviceManager.getDevice('key_resp_I2') is None:
        # initialise key_resp_I2
        key_resp_I2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_I2',
        )
    if deviceManager.getDevice('key_resp_20') is None:
        # initialise key_resp_20
        key_resp_20 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_20',
        )
    if deviceManager.getDevice('key_resp_39') is None:
        # initialise key_resp_39
        key_resp_39 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_39',
        )
    if deviceManager.getDevice('key_resp_I3') is None:
        # initialise key_resp_I3
        key_resp_I3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_I3',
        )
    if deviceManager.getDevice('key_resp_21') is None:
        # initialise key_resp_21
        key_resp_21 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_21',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # enter 'rush' mode (raise CPU priority)
    if not PILOTING:
        core.rush(enable=True)
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    welcome = visual.ImageStim(
        win=win,
        name='welcome', 
        image='picture/welcome_工作區域 1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.6, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_22 = keyboard.Keyboard(deviceName='key_resp_22')
    
    # --- Initialize components for Routine "Introduction" ---
    text = visual.TextStim(win=win, name='text',
        text='Put the left forefinger on the "A" key for the items belong to the category "unplesant".\n\nPut the right forefinger on the "L" key for the items belong to the category "plesant".\n\nPress the "space bar" to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "reminder_A1" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Part 1\n\nIf you make a mistake, a "error" will appear.\nGo as fast as you can while being accurate.\n\nThe trial will begin.\n\nPress the "space bar" to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practice_Task_A1" ---
    text_A1 = visual.TextStim(win=win, name='text_A1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_A1 = keyboard.Keyboard(deviceName='key_resp_A1')
    
    # --- Initialize components for Routine "feedback_A1" ---
    # Run 'Begin Experiment' code from code_A1
    msg = ""
    key_resp_A1_corr_sum_temp = 0.0
    key_resp_A1_rt_sum_temp = 0.0
    
    feedback_text_A1 = visual.TextStim(win=win, name='feedback_text_A1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_A1" ---
    score_A1_text = visual.TextStim(win=win, name='score_A1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_score = keyboard.Keyboard(deviceName='key_resp_score')
    # Run 'Begin Experiment' code from score_A1_code
    feedback_msg =""
    
    # --- Initialize components for Routine "reminder_A2" ---
    text_45 = visual.TextStim(win=win, name='text_45',
        text='Part 2\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_23 = keyboard.Keyboard(deviceName='key_resp_23')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_A2" ---
    text_A2 = visual.TextStim(win=win, name='text_A2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_A2 = keyboard.Keyboard(deviceName='key_resp_A2')
    
    # --- Initialize components for Routine "feedback_A2" ---
    # Run 'Begin Experiment' code from code_A2
    msg = ""
    key_resp_A2_corr_sum_temp = 0.0
    key_resp_A2_rt_sum_temp = 0.0
    
    feedback_text_A2 = visual.TextStim(win=win, name='feedback_text_A2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_A2" ---
    score_A2_text = visual.TextStim(win=win, name='score_A2_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    # Run 'Begin Experiment' code from score_A2_code
    feedback_msg =""
    
    # --- Initialize components for Routine "reminder_B1" ---
    text_46 = visual.TextStim(win=win, name='text_46',
        text='Part 3\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_24 = keyboard.Keyboard(deviceName='key_resp_24')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practice_Task_B1" ---
    text_B1 = visual.TextStim(win=win, name='text_B1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_B1 = keyboard.Keyboard(deviceName='key_resp_B1')
    
    # --- Initialize components for Routine "feedback_B1" ---
    # Run 'Begin Experiment' code from code_B1
    msg = ""
    key_resp_B1_corr_sum_temp = 0.0
    key_resp_B1_rt_sum_temp = 0.0
    
    feedback_text_B1 = visual.TextStim(win=win, name='feedback_text_B1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_B1" ---
    score_B1_text = visual.TextStim(win=win, name='score_B1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    # Run 'Begin Experiment' code from score_B1_code
    feedback_msg =""
    
    # --- Initialize components for Routine "reminder_B2" ---
    text_47 = visual.TextStim(win=win, name='text_47',
        text='Part 4\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_25 = keyboard.Keyboard(deviceName='key_resp_25')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_B2" ---
    text_B2 = visual.TextStim(win=win, name='text_B2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_B2 = keyboard.Keyboard(deviceName='key_resp_B2')
    
    # --- Initialize components for Routine "feedback_B2" ---
    # Run 'Begin Experiment' code from code_B2
    msg = ""
    key_resp_B2_corr_sum_temp = 0.0
    key_resp_B2_rt_sum_temp = 0.0
    
    feedback_text_B2 = visual.TextStim(win=win, name='feedback_text_B2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_B2" ---
    score_B2_text = visual.TextStim(win=win, name='score_B2_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    # Run 'Begin Experiment' code from score_B2_code
    feedback_msg =""
    
    # --- Initialize components for Routine "reminder_C1" ---
    text_20 = visual.TextStim(win=win, name='text_20',
        text='Part 5\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_26 = keyboard.Keyboard(deviceName='key_resp_26')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_C1" ---
    text_C1 = visual.TextStim(win=win, name='text_C1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_C1 = keyboard.Keyboard(deviceName='key_resp_C1')
    
    # --- Initialize components for Routine "feedback_C1" ---
    # Run 'Begin Experiment' code from code_C1
    msg = ""
    key_resp_C1_corr_sum_temp = 0.0
    key_resp_C1_rt_sum_temp = 0.0
    feedback_text_C1 = visual.TextStim(win=win, name='feedback_text_C1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_C1" ---
    # Run 'Begin Experiment' code from score_C1_code
    feedback_msg =""
    score_C1_text = visual.TextStim(win=win, name='score_C1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    
    # --- Initialize components for Routine "reminder_C2" ---
    text_21 = visual.TextStim(win=win, name='text_21',
        text='Part 6\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_27 = keyboard.Keyboard(deviceName='key_resp_27')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_C2" ---
    text_C2 = visual.TextStim(win=win, name='text_C2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_C2 = keyboard.Keyboard(deviceName='key_resp_C2')
    
    # --- Initialize components for Routine "feedback_C2" ---
    # Run 'Begin Experiment' code from code_C2
    msg = ""
    key_resp_C2_corr_sum_temp = 0.0
    key_resp_C2_rt_sum_temp = 0.0
    
    feedback_text_C2 = visual.TextStim(win=win, name='feedback_text_C2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_C2" ---
    # Run 'Begin Experiment' code from score_C2_code
    feedback_msg =""
    score_C2_text = visual.TextStim(win=win, name='score_C2_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    
    # --- Initialize components for Routine "reminder_C3" ---
    text_48 = visual.TextStim(win=win, name='text_48',
        text='Part 7\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_28 = keyboard.Keyboard(deviceName='key_resp_28')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_C3" ---
    text_C3 = visual.TextStim(win=win, name='text_C3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_C3 = keyboard.Keyboard(deviceName='key_resp_C3')
    
    # --- Initialize components for Routine "feedback_C3" ---
    # Run 'Begin Experiment' code from code_C3
    msg = ""
    key_resp_C3_corr_sum_temp = 0.0
    key_resp_C3_rt_sum_temp = 0.0
    feedback_text_C3 = visual.TextStim(win=win, name='feedback_text_C3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_C3" ---
    # Run 'Begin Experiment' code from score_C3_code
    feedback_msg =""
    score_C3_text = visual.TextStim(win=win, name='score_C3_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_8 = keyboard.Keyboard(deviceName='key_resp_8')
    
    # --- Initialize components for Routine "reminder_D1" ---
    text_49 = visual.TextStim(win=win, name='text_49',
        text='Part 8\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_29 = keyboard.Keyboard(deviceName='key_resp_29')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_D1" ---
    text_D1 = visual.TextStim(win=win, name='text_D1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_D1 = keyboard.Keyboard(deviceName='key_resp_D1')
    
    # --- Initialize components for Routine "feedback_D1" ---
    # Run 'Begin Experiment' code from code_D1
    msg = ""
    key_resp_D1_corr_sum_temp = 0.0
    key_resp_D1_rt_sum_temp = 0.0
    feedback_text_D1 = visual.TextStim(win=win, name='feedback_text_D1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_D1" ---
    # Run 'Begin Experiment' code from score_D1_code
    feedback_msg =""
    score_D1_text = visual.TextStim(win=win, name='score_D1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_9 = keyboard.Keyboard(deviceName='key_resp_9')
    
    # --- Initialize components for Routine "reminder_E1" ---
    text_50 = visual.TextStim(win=win, name='text_50',
        text='Part 9\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_30 = keyboard.Keyboard(deviceName='key_resp_30')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practice_Task_E1" ---
    text_E1 = visual.TextStim(win=win, name='text_E1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_E1 = keyboard.Keyboard(deviceName='key_resp_E1')
    
    # --- Initialize components for Routine "feedback_E1" ---
    # Run 'Begin Experiment' code from code_E1
    msg = ""
    key_resp_E1_corr_sum_temp = 0.0
    key_resp_E1_rt_sum_temp = 0.0
    feedback_text_E1 = visual.TextStim(win=win, name='feedback_text_E1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_E1" ---
    # Run 'Begin Experiment' code from score_E1_code
    feedback_msg =""
    score_E1_text = visual.TextStim(win=win, name='score_E1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_10 = keyboard.Keyboard(deviceName='key_resp_10')
    
    # --- Initialize components for Routine "reminder_E2" ---
    text_51 = visual.TextStim(win=win, name='text_51',
        text='Part 10\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_31 = keyboard.Keyboard(deviceName='key_resp_31')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_E2" ---
    text_E2 = visual.TextStim(win=win, name='text_E2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_E2 = keyboard.Keyboard(deviceName='key_resp_E2')
    
    # --- Initialize components for Routine "feedback_E2" ---
    # Run 'Begin Experiment' code from code_E2
    msg = ""
    key_resp_E2_corr_sum_temp = 0.0
    key_resp_E2_rt_sum_temp = 0.0
    
    feedback_text_E2 = visual.TextStim(win=win, name='feedback_text_E2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_E2" ---
    # Run 'Begin Experiment' code from score_E2_code
    feedback_msg =""
    score_E2_text = visual.TextStim(win=win, name='score_E2_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_11 = keyboard.Keyboard(deviceName='key_resp_11')
    
    # --- Initialize components for Routine "reminder_E3" ---
    text_52 = visual.TextStim(win=win, name='text_52',
        text='Part 11\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_40 = keyboard.Keyboard(deviceName='key_resp_40')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_E3" ---
    text_E3 = visual.TextStim(win=win, name='text_E3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_E3 = keyboard.Keyboard(deviceName='key_resp_E3')
    
    # --- Initialize components for Routine "feedback_E3" ---
    # Run 'Begin Experiment' code from code_E3
    msg = ""
    key_resp_E3_corr_sum_temp = 0.0
    key_resp_E3_rt_sum_temp = 0.0
    feedback_text_E3 = visual.TextStim(win=win, name='feedback_text_E3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_E3" ---
    # Run 'Begin Experiment' code from score_E3_code
    feedback_msg =""
    score_E3_text = visual.TextStim(win=win, name='score_E3_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_12 = keyboard.Keyboard(deviceName='key_resp_12')
    
    # --- Initialize components for Routine "reminder_F1" ---
    text_53 = visual.TextStim(win=win, name='text_53',
        text='Part 12\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_32 = keyboard.Keyboard(deviceName='key_resp_32')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_F1" ---
    text_F1 = visual.TextStim(win=win, name='text_F1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_F1 = keyboard.Keyboard(deviceName='key_resp_F1')
    
    # --- Initialize components for Routine "feedback_F1" ---
    # Run 'Begin Experiment' code from code_F1
    msg = ""
    key_resp_F1_corr_sum_temp = 0.0
    key_resp_F1_rt_sum_temp = 0.0
    feedback_text_F1 = visual.TextStim(win=win, name='feedback_text_F1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_F1" ---
    # Run 'Begin Experiment' code from score_F1_code
    feedback_msg =""
    score_F1_text = visual.TextStim(win=win, name='score_F1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_13 = keyboard.Keyboard(deviceName='key_resp_13')
    
    # --- Initialize components for Routine "reminder_G1" ---
    text_54 = visual.TextStim(win=win, name='text_54',
        text='Part 13\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_33 = keyboard.Keyboard(deviceName='key_resp_33')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practice_Task_G1" ---
    text_G1 = visual.TextStim(win=win, name='text_G1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_G1 = keyboard.Keyboard(deviceName='key_resp_G1')
    
    # --- Initialize components for Routine "feedback_G1" ---
    # Run 'Begin Experiment' code from code_G1
    msg = ""
    key_resp_G1_corr_sum_temp = 0.0
    key_resp_G1_rt_sum_temp = 0.0
    feedback_text_G1 = visual.TextStim(win=win, name='feedback_text_G1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_G1" ---
    # Run 'Begin Experiment' code from score_G1_code
    feedback_msg =""
    
    score_G1_text = visual.TextStim(win=win, name='score_G1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_14 = keyboard.Keyboard(deviceName='key_resp_14')
    
    # --- Initialize components for Routine "reminder_G2" ---
    text_55 = visual.TextStim(win=win, name='text_55',
        text='Part 14\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_35 = keyboard.Keyboard(deviceName='key_resp_35')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_G2" ---
    text_G2 = visual.TextStim(win=win, name='text_G2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_G2 = keyboard.Keyboard(deviceName='key_resp_G2')
    
    # --- Initialize components for Routine "feedback_G2" ---
    # Run 'Begin Experiment' code from code_G2
    msg = ""
    key_resp_G2_corr_sum_temp = 0.0
    key_resp_G2_rt_sum_temp = 0.0
    feedback_text_G2 = visual.TextStim(win=win, name='feedback_text_G2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_G2" ---
    # Run 'Begin Experiment' code from score_G2_code
    feedback_msg =""
    score_G2_text = visual.TextStim(win=win, name='score_G2_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_15 = keyboard.Keyboard(deviceName='key_resp_15')
    
    # --- Initialize components for Routine "reminder_G3" ---
    text_56 = visual.TextStim(win=win, name='text_56',
        text='Part 15\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_34 = keyboard.Keyboard(deviceName='key_resp_34')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_G3" ---
    text_G3 = visual.TextStim(win=win, name='text_G3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_G3 = keyboard.Keyboard(deviceName='key_resp_G3')
    
    # --- Initialize components for Routine "feedback_G3" ---
    # Run 'Begin Experiment' code from code_G3
    msg = ""
    key_resp_G3_corr_sum_temp = 0.0
    key_resp_G3_rt_sum_temp = 0.0
    
    feedback_text_G3 = visual.TextStim(win=win, name='feedback_text_G3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_G3" ---
    # Run 'Begin Experiment' code from score_G3_code
    feedback_msg =""
    score_G3_text = visual.TextStim(win=win, name='score_G3_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_16 = keyboard.Keyboard(deviceName='key_resp_16')
    
    # --- Initialize components for Routine "reminder_H1" ---
    text_H1 = visual.TextStim(win=win, name='text_H1',
        text='Part 16\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_H1 = keyboard.Keyboard(deviceName='key_resp_H1')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_H1" ---
    text_37 = visual.TextStim(win=win, name='text_37',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_19 = keyboard.Keyboard(deviceName='key_resp_19')
    
    # --- Initialize components for Routine "feedback_H1" ---
    # Run 'Begin Experiment' code from code_H1
    msg = ""
    key_resp_H1_corr_sum_temp = 0.0
    key_resp_H1_rt_sum_temp = 0.0
    feedback_text_H1 = visual.TextStim(win=win, name='feedback_text_H1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_H1" ---
    # Run 'Begin Experiment' code from score_H1_code
    feedback_msg =""
    score_H1_text = visual.TextStim(win=win, name='score_H1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_17 = keyboard.Keyboard(deviceName='key_resp_17')
    
    # --- Initialize components for Routine "reminder_I1" ---
    text_58 = visual.TextStim(win=win, name='text_58',
        text='Part 17\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_37 = keyboard.Keyboard(deviceName='key_resp_37')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practice_Task_I1" ---
    text_I1 = visual.TextStim(win=win, name='text_I1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_I1 = keyboard.Keyboard(deviceName='key_resp_I1')
    
    # --- Initialize components for Routine "feedback_I1" ---
    # Run 'Begin Experiment' code from code_I1
    msg = ""
    key_resp_I1_corr_sum_temp = 0.0
    key_resp_I1_rt_sum_temp = 0.0
    feedback_text_I1 = visual.TextStim(win=win, name='feedback_text_I1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_I1" ---
    # Run 'Begin Experiment' code from score_I1_code
    feedback_msg =""
    score_I1_text = visual.TextStim(win=win, name='score_I1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_18 = keyboard.Keyboard(deviceName='key_resp_18')
    
    # --- Initialize components for Routine "reminder_I2" ---
    text_59 = visual.TextStim(win=win, name='text_59',
        text='Part 18\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_38 = keyboard.Keyboard(deviceName='key_resp_38')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_I2" ---
    text_I2 = visual.TextStim(win=win, name='text_I2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_I2 = keyboard.Keyboard(deviceName='key_resp_I2')
    
    # --- Initialize components for Routine "feedback_I2" ---
    # Run 'Begin Experiment' code from code_I2
    msg = ""
    key_resp_I2_corr_sum_temp = 0.0
    key_resp_I2_rt_sum_temp = 0.0
    
    feedback_text_I2 = visual.TextStim(win=win, name='feedback_text_I2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_I2" ---
    # Run 'Begin Experiment' code from score_I2_code
    feedback_msg =""
    score_I2_text = visual.TextStim(win=win, name='score_I2_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_20 = keyboard.Keyboard(deviceName='key_resp_20')
    
    # --- Initialize components for Routine "reminder_I3" ---
    text_60 = visual.TextStim(win=win, name='text_60',
        text='Part 19\n\nThe trial will begin.\n\nPress space bar to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_39 = keyboard.Keyboard(deviceName='key_resp_39')
    
    # --- Initialize components for Routine "ISI1500" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "record_Task_I3" ---
    text_I3 = visual.TextStim(win=win, name='text_I3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_I3 = keyboard.Keyboard(deviceName='key_resp_I3')
    
    # --- Initialize components for Routine "feedback_I3" ---
    # Run 'Begin Experiment' code from code_I3
    msg = ""
    key_resp_I3_corr_sum_temp = 0.0
    key_resp_I3_rt_sum_temp = 0.0
    
    feedback_text_I3 = visual.TextStim(win=win, name='feedback_text_I3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISI250" ---
    
    # --- Initialize components for Routine "score_I3" ---
    # Run 'Begin Experiment' code from score_I3_code
    feedback_msg =""
    score_I3_text = visual.TextStim(win=win, name='score_I3_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_21 = keyboard.Keyboard(deviceName='key_resp_21')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    # create an object to store info about Routine Welcome
    Welcome = data.Routine(
        name='Welcome',
        components=[welcome, key_resp_22],
    )
    Welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_22
    key_resp_22.keys = []
    key_resp_22.rt = []
    _key_resp_22_allKeys = []
    # store start times for Welcome
    Welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome.tStart = globalClock.getTime(format='float')
    Welcome.status = STARTED
    thisExp.addData('Welcome.started', Welcome.tStart)
    Welcome.maxDuration = None
    # keep track of which components have finished
    WelcomeComponents = Welcome.components
    for thisComponent in Welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome" ---
    Welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome* updates
        
        # if welcome is starting this frame...
        if welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome.frameNStart = frameN  # exact frame index
            welcome.tStart = t  # local t and not account for scr refresh
            welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome.started')
            # update status
            welcome.status = STARTED
            welcome.setAutoDraw(True)
        
        # if welcome is active this frame...
        if welcome.status == STARTED:
            # update params
            pass
        
        # *key_resp_22* updates
        waitOnFlip = False
        
        # if key_resp_22 is starting this frame...
        if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_22.frameNStart = frameN  # exact frame index
            key_resp_22.tStart = t  # local t and not account for scr refresh
            key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_22.started')
            # update status
            key_resp_22.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_22.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_22.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_22_allKeys.extend(theseKeys)
            if len(_key_resp_22_allKeys):
                key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
                key_resp_22.rt = _key_resp_22_allKeys[-1].rt
                key_resp_22.duration = _key_resp_22_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in Welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome
    Welcome.tStop = globalClock.getTime(format='float')
    Welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Welcome.stopped', Welcome.tStop)
    # check responses
    if key_resp_22.keys in ['', [], None]:  # No response was made
        key_resp_22.keys = None
    thisExp.addData('key_resp_22.keys',key_resp_22.keys)
    if key_resp_22.keys != None:  # we had a response
        thisExp.addData('key_resp_22.rt', key_resp_22.rt)
        thisExp.addData('key_resp_22.duration', key_resp_22.duration)
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Introduction" ---
    # create an object to store info about Routine Introduction
    Introduction = data.Routine(
        name='Introduction',
        components=[text, key_resp],
    )
    Introduction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for Introduction
    Introduction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Introduction.tStart = globalClock.getTime(format='float')
    Introduction.status = STARTED
    thisExp.addData('Introduction.started', Introduction.tStart)
    Introduction.maxDuration = None
    # keep track of which components have finished
    IntroductionComponents = Introduction.components
    for thisComponent in Introduction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Introduction" ---
    Introduction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Introduction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Introduction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Introduction" ---
    for thisComponent in Introduction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Introduction
    Introduction.tStop = globalClock.getTime(format='float')
    Introduction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Introduction.stopped', Introduction.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_20 = data.TrialHandler2(
        name='trials_20',
        nReps=0.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(trials_20)  # add the loop to the experiment
    thisTrial_20 = trials_20.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
    if thisTrial_20 != None:
        for paramName in thisTrial_20:
            globals()[paramName] = thisTrial_20[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_20 in trials_20:
        currentLoop = trials_20
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
        if thisTrial_20 != None:
            for paramName in thisTrial_20:
                globals()[paramName] = thisTrial_20[paramName]
        
        # --- Prepare to start Routine "reminder_A1" ---
        # create an object to store info about Routine reminder_A1
        reminder_A1 = data.Routine(
            name='reminder_A1',
            components=[text_2, key_resp_2],
        )
        reminder_A1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_2
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # store start times for reminder_A1
        reminder_A1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reminder_A1.tStart = globalClock.getTime(format='float')
        reminder_A1.status = STARTED
        thisExp.addData('reminder_A1.started', reminder_A1.tStart)
        reminder_A1.maxDuration = None
        # keep track of which components have finished
        reminder_A1Components = reminder_A1.components
        for thisComponent in reminder_A1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reminder_A1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        reminder_A1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                reminder_A1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reminder_A1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reminder_A1" ---
        for thisComponent in reminder_A1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reminder_A1
        reminder_A1.tStop = globalClock.getTime(format='float')
        reminder_A1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reminder_A1.stopped', reminder_A1.tStop)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials_20.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials_20.addData('key_resp_2.rt', key_resp_2.rt)
            trials_20.addData('key_resp_2.duration', key_resp_2.duration)
        # the Routine "reminder_A1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ISI1500" ---
        # create an object to store info about Routine ISI1500
        ISI1500 = data.Routine(
            name='ISI1500',
            components=[text_3],
        )
        ISI1500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI1500
        ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI1500.tStart = globalClock.getTime(format='float')
        ISI1500.status = STARTED
        thisExp.addData('ISI1500.started', ISI1500.tStart)
        ISI1500.maxDuration = 1.5
        # keep track of which components have finished
        ISI1500Components = ISI1500.components
        for thisComponent in ISI1500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI1500" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        ISI1500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI1500.maxDuration-frameTolerance:
                ISI1500.maxDurationReached = True
                continueRoutine = False
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # if text_3 is stopping this frame...
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    # update status
                    text_3.status = FINISHED
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI1500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI1500" ---
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI1500
        ISI1500.tStop = globalClock.getTime(format='float')
        ISI1500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI1500.stopped', ISI1500.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI1500.maxDurationReached:
            routineTimer.addTime(-ISI1500.maxDuration)
        elif ISI1500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler2(
            name='trials',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('excel/TestA1_D2_right_japan.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "practice_Task_A1" ---
            # create an object to store info about Routine practice_Task_A1
            practice_Task_A1 = data.Routine(
                name='practice_Task_A1',
                components=[text_A1, key_resp_A1],
            )
            practice_Task_A1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            text_A1.setText(name)
            # create starting attributes for key_resp_A1
            key_resp_A1.keys = []
            key_resp_A1.rt = []
            _key_resp_A1_allKeys = []
            # store start times for practice_Task_A1
            practice_Task_A1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            practice_Task_A1.tStart = globalClock.getTime(format='float')
            practice_Task_A1.status = STARTED
            thisExp.addData('practice_Task_A1.started', practice_Task_A1.tStart)
            practice_Task_A1.maxDuration = None
            # keep track of which components have finished
            practice_Task_A1Components = practice_Task_A1.components
            for thisComponent in practice_Task_A1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "practice_Task_A1" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            practice_Task_A1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_A1* updates
                
                # if text_A1 is starting this frame...
                if text_A1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_A1.frameNStart = frameN  # exact frame index
                    text_A1.tStart = t  # local t and not account for scr refresh
                    text_A1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_A1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_A1.started')
                    # update status
                    text_A1.status = STARTED
                    text_A1.setAutoDraw(True)
                
                # if text_A1 is active this frame...
                if text_A1.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_A1* updates
                waitOnFlip = False
                
                # if key_resp_A1 is starting this frame...
                if key_resp_A1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_A1.frameNStart = frameN  # exact frame index
                    key_resp_A1.tStart = t  # local t and not account for scr refresh
                    key_resp_A1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_A1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_A1.started')
                    # update status
                    key_resp_A1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_A1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_A1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_A1.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_A1.getKeys(keyList=['a', 'l'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_A1_allKeys.extend(theseKeys)
                    if len(_key_resp_A1_allKeys):
                        key_resp_A1.keys = _key_resp_A1_allKeys[-1].name  # just the last key pressed
                        key_resp_A1.rt = _key_resp_A1_allKeys[-1].rt
                        key_resp_A1.duration = _key_resp_A1_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_A1.keys == str(keypad)) or (key_resp_A1.keys == keypad):
                            key_resp_A1.corr = 1
                        else:
                            key_resp_A1.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    practice_Task_A1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practice_Task_A1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practice_Task_A1" ---
            for thisComponent in practice_Task_A1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for practice_Task_A1
            practice_Task_A1.tStop = globalClock.getTime(format='float')
            practice_Task_A1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('practice_Task_A1.stopped', practice_Task_A1.tStop)
            # check responses
            if key_resp_A1.keys in ['', [], None]:  # No response was made
                key_resp_A1.keys = None
                # was no response the correct answer?!
                if str(keypad).lower() == 'none':
                   key_resp_A1.corr = 1;  # correct non-response
                else:
                   key_resp_A1.corr = 0;  # failed to respond (incorrectly)
            # store data for trials (TrialHandler)
            trials.addData('key_resp_A1.keys',key_resp_A1.keys)
            trials.addData('key_resp_A1.corr', key_resp_A1.corr)
            if key_resp_A1.keys != None:  # we had a response
                trials.addData('key_resp_A1.rt', key_resp_A1.rt)
                trials.addData('key_resp_A1.duration', key_resp_A1.duration)
            # the Routine "practice_Task_A1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback_A1" ---
            # create an object to store info about Routine feedback_A1
            feedback_A1 = data.Routine(
                name='feedback_A1',
                components=[feedback_text_A1],
            )
            feedback_A1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_A1
            key_resp_A1_rt_sum_temp = key_resp_A1_rt_sum_temp + float(str(key_resp_A1.rt))
            
            if key_resp_A1.corr:
                key_resp_A1_corr_sum_temp =key_resp_A1_corr_sum_temp +1
                continueRoutine = False
            else:
                msg = 'error'
            feedback_text_A1.setText(msg)
            # store start times for feedback_A1
            feedback_A1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback_A1.tStart = globalClock.getTime(format='float')
            feedback_A1.status = STARTED
            thisExp.addData('feedback_A1.started', feedback_A1.tStart)
            feedback_A1.maxDuration = None
            # keep track of which components have finished
            feedback_A1Components = feedback_A1.components
            for thisComponent in feedback_A1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback_A1" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            feedback_A1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text_A1* updates
                
                # if feedback_text_A1 is starting this frame...
                if feedback_text_A1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_A1.frameNStart = frameN  # exact frame index
                    feedback_text_A1.tStart = t  # local t and not account for scr refresh
                    feedback_text_A1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_A1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_A1.started')
                    # update status
                    feedback_text_A1.status = STARTED
                    feedback_text_A1.setAutoDraw(True)
                
                # if feedback_text_A1 is active this frame...
                if feedback_text_A1.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text_A1 is stopping this frame...
                if feedback_text_A1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text_A1.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text_A1.tStop = t  # not accounting for scr refresh
                        feedback_text_A1.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_text_A1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text_A1.stopped')
                        # update status
                        feedback_text_A1.status = FINISHED
                        feedback_text_A1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback_A1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_A1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback_A1" ---
            for thisComponent in feedback_A1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback_A1
            feedback_A1.tStop = globalClock.getTime(format='float')
            feedback_A1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback_A1.stopped', feedback_A1.tStop)
            # Run 'End Routine' code from code_A1
            key_resp_A1_corr_sum = key_resp_A1_corr_sum_temp
            key_resp_A1_rt_sum = key_resp_A1_rt_sum_temp
            
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback_A1.maxDurationReached:
                routineTimer.addTime(-feedback_A1.maxDuration)
            elif feedback_A1.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "ISI250" ---
            # create an object to store info about Routine ISI250
            ISI250 = data.Routine(
                name='ISI250',
                components=[],
            )
            ISI250.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for ISI250
            ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI250.tStart = globalClock.getTime(format='float')
            ISI250.status = STARTED
            thisExp.addData('ISI250.started', ISI250.tStart)
            ISI250.maxDuration = 0.25
            # keep track of which components have finished
            ISI250Components = ISI250.components
            for thisComponent in ISI250.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI250" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            ISI250.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > ISI250.maxDuration-frameTolerance:
                    ISI250.maxDurationReached = True
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI250.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI250.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI250" ---
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI250
            ISI250.tStop = globalClock.getTime(format='float')
            ISI250.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI250.stopped', ISI250.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if ISI250.maxDurationReached:
                routineTimer.addTime(-ISI250.maxDuration)
            elif ISI250.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "score_A1" ---
        # create an object to store info about Routine score_A1
        score_A1 = data.Routine(
            name='score_A1',
            components=[score_A1_text, key_resp_score],
        )
        score_A1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_score
        key_resp_score.keys = []
        key_resp_score.rt = []
        _key_resp_score_allKeys = []
        # Run 'Begin Routine' code from score_A1_code
        feedback_msg ="" 
        
        accuracy = round((key_resp_A1_corr_sum / 50) * 100, 2)  
        rt_average = round((key_resp_A1_rt_sum / 50) * 1000, 2)  
        
        feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
        feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
        feedback_msg += "Press space bar to continue."
        # store start times for score_A1
        score_A1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        score_A1.tStart = globalClock.getTime(format='float')
        score_A1.status = STARTED
        thisExp.addData('score_A1.started', score_A1.tStart)
        score_A1.maxDuration = None
        # keep track of which components have finished
        score_A1Components = score_A1.components
        for thisComponent in score_A1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "score_A1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        score_A1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *score_A1_text* updates
            
            # if score_A1_text is starting this frame...
            if score_A1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_A1_text.frameNStart = frameN  # exact frame index
                score_A1_text.tStart = t  # local t and not account for scr refresh
                score_A1_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_A1_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'score_A1_text.started')
                # update status
                score_A1_text.status = STARTED
                score_A1_text.setAutoDraw(True)
            
            # if score_A1_text is active this frame...
            if score_A1_text.status == STARTED:
                # update params
                score_A1_text.setText(feedback_msg, log=False)
            
            # *key_resp_score* updates
            waitOnFlip = False
            
            # if key_resp_score is starting this frame...
            if key_resp_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_score.frameNStart = frameN  # exact frame index
                key_resp_score.tStart = t  # local t and not account for scr refresh
                key_resp_score.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_score, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_score.started')
                # update status
                key_resp_score.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_score.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_score.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_score.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_score.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_score_allKeys.extend(theseKeys)
                if len(_key_resp_score_allKeys):
                    key_resp_score.keys = _key_resp_score_allKeys[-1].name  # just the last key pressed
                    key_resp_score.rt = _key_resp_score_allKeys[-1].rt
                    key_resp_score.duration = _key_resp_score_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                score_A1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in score_A1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "score_A1" ---
        for thisComponent in score_A1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for score_A1
        score_A1.tStop = globalClock.getTime(format='float')
        score_A1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('score_A1.stopped', score_A1.tStop)
        # check responses
        if key_resp_score.keys in ['', [], None]:  # No response was made
            key_resp_score.keys = None
        trials_20.addData('key_resp_score.keys',key_resp_score.keys)
        if key_resp_score.keys != None:  # we had a response
            trials_20.addData('key_resp_score.rt', key_resp_score.rt)
            trials_20.addData('key_resp_score.duration', key_resp_score.duration)
        # the Routine "score_A1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "reminder_A2" ---
        # create an object to store info about Routine reminder_A2
        reminder_A2 = data.Routine(
            name='reminder_A2',
            components=[text_45, key_resp_23],
        )
        reminder_A2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_23
        key_resp_23.keys = []
        key_resp_23.rt = []
        _key_resp_23_allKeys = []
        # store start times for reminder_A2
        reminder_A2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reminder_A2.tStart = globalClock.getTime(format='float')
        reminder_A2.status = STARTED
        thisExp.addData('reminder_A2.started', reminder_A2.tStart)
        reminder_A2.maxDuration = None
        # keep track of which components have finished
        reminder_A2Components = reminder_A2.components
        for thisComponent in reminder_A2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reminder_A2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        reminder_A2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_45* updates
            
            # if text_45 is starting this frame...
            if text_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_45.frameNStart = frameN  # exact frame index
                text_45.tStart = t  # local t and not account for scr refresh
                text_45.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_45, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_45.started')
                # update status
                text_45.status = STARTED
                text_45.setAutoDraw(True)
            
            # if text_45 is active this frame...
            if text_45.status == STARTED:
                # update params
                pass
            
            # *key_resp_23* updates
            waitOnFlip = False
            
            # if key_resp_23 is starting this frame...
            if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_23.frameNStart = frameN  # exact frame index
                key_resp_23.tStart = t  # local t and not account for scr refresh
                key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_23.started')
                # update status
                key_resp_23.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_23.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_23.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_23_allKeys.extend(theseKeys)
                if len(_key_resp_23_allKeys):
                    key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
                    key_resp_23.rt = _key_resp_23_allKeys[-1].rt
                    key_resp_23.duration = _key_resp_23_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                reminder_A2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reminder_A2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reminder_A2" ---
        for thisComponent in reminder_A2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reminder_A2
        reminder_A2.tStop = globalClock.getTime(format='float')
        reminder_A2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reminder_A2.stopped', reminder_A2.tStop)
        # check responses
        if key_resp_23.keys in ['', [], None]:  # No response was made
            key_resp_23.keys = None
        trials_20.addData('key_resp_23.keys',key_resp_23.keys)
        if key_resp_23.keys != None:  # we had a response
            trials_20.addData('key_resp_23.rt', key_resp_23.rt)
            trials_20.addData('key_resp_23.duration', key_resp_23.duration)
        # the Routine "reminder_A2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ISI1500" ---
        # create an object to store info about Routine ISI1500
        ISI1500 = data.Routine(
            name='ISI1500',
            components=[text_3],
        )
        ISI1500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI1500
        ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI1500.tStart = globalClock.getTime(format='float')
        ISI1500.status = STARTED
        thisExp.addData('ISI1500.started', ISI1500.tStart)
        ISI1500.maxDuration = 1.5
        # keep track of which components have finished
        ISI1500Components = ISI1500.components
        for thisComponent in ISI1500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI1500" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        ISI1500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI1500.maxDuration-frameTolerance:
                ISI1500.maxDurationReached = True
                continueRoutine = False
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # if text_3 is stopping this frame...
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    # update status
                    text_3.status = FINISHED
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI1500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI1500" ---
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI1500
        ISI1500.tStop = globalClock.getTime(format='float')
        ISI1500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI1500.stopped', ISI1500.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI1500.maxDurationReached:
            routineTimer.addTime(-ISI1500.maxDuration)
        elif ISI1500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # set up handler to look after randomisation of conditions etc
        trials_4 = data.TrialHandler2(
            name='trials_4',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('excel/TestA1_D2_right_japan.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials_4)  # add the loop to the experiment
        thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                globals()[paramName] = thisTrial_4[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_4 in trials_4:
            currentLoop = trials_4
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    globals()[paramName] = thisTrial_4[paramName]
            
            # --- Prepare to start Routine "record_Task_A2" ---
            # create an object to store info about Routine record_Task_A2
            record_Task_A2 = data.Routine(
                name='record_Task_A2',
                components=[text_A2, key_resp_A2],
            )
            record_Task_A2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            text_A2.setText(name)
            # create starting attributes for key_resp_A2
            key_resp_A2.keys = []
            key_resp_A2.rt = []
            _key_resp_A2_allKeys = []
            # store start times for record_Task_A2
            record_Task_A2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            record_Task_A2.tStart = globalClock.getTime(format='float')
            record_Task_A2.status = STARTED
            thisExp.addData('record_Task_A2.started', record_Task_A2.tStart)
            record_Task_A2.maxDuration = None
            # keep track of which components have finished
            record_Task_A2Components = record_Task_A2.components
            for thisComponent in record_Task_A2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "record_Task_A2" ---
            # if trial has changed, end Routine now
            if isinstance(trials_4, data.TrialHandler2) and thisTrial_4.thisN != trials_4.thisTrial.thisN:
                continueRoutine = False
            record_Task_A2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_A2* updates
                
                # if text_A2 is starting this frame...
                if text_A2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_A2.frameNStart = frameN  # exact frame index
                    text_A2.tStart = t  # local t and not account for scr refresh
                    text_A2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_A2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_A2.started')
                    # update status
                    text_A2.status = STARTED
                    text_A2.setAutoDraw(True)
                
                # if text_A2 is active this frame...
                if text_A2.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_A2* updates
                waitOnFlip = False
                
                # if key_resp_A2 is starting this frame...
                if key_resp_A2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_A2.frameNStart = frameN  # exact frame index
                    key_resp_A2.tStart = t  # local t and not account for scr refresh
                    key_resp_A2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_A2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_A2.started')
                    # update status
                    key_resp_A2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_A2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_A2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_A2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_A2.getKeys(keyList=['a', 'l'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_A2_allKeys.extend(theseKeys)
                    if len(_key_resp_A2_allKeys):
                        key_resp_A2.keys = _key_resp_A2_allKeys[-1].name  # just the last key pressed
                        key_resp_A2.rt = _key_resp_A2_allKeys[-1].rt
                        key_resp_A2.duration = _key_resp_A2_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_A2.keys == str(keypad)) or (key_resp_A2.keys == keypad):
                            key_resp_A2.corr = 1
                        else:
                            key_resp_A2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    record_Task_A2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in record_Task_A2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "record_Task_A2" ---
            for thisComponent in record_Task_A2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for record_Task_A2
            record_Task_A2.tStop = globalClock.getTime(format='float')
            record_Task_A2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('record_Task_A2.stopped', record_Task_A2.tStop)
            # check responses
            if key_resp_A2.keys in ['', [], None]:  # No response was made
                key_resp_A2.keys = None
                # was no response the correct answer?!
                if str(keypad).lower() == 'none':
                   key_resp_A2.corr = 1;  # correct non-response
                else:
                   key_resp_A2.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_4 (TrialHandler)
            trials_4.addData('key_resp_A2.keys',key_resp_A2.keys)
            trials_4.addData('key_resp_A2.corr', key_resp_A2.corr)
            if key_resp_A2.keys != None:  # we had a response
                trials_4.addData('key_resp_A2.rt', key_resp_A2.rt)
                trials_4.addData('key_resp_A2.duration', key_resp_A2.duration)
            # the Routine "record_Task_A2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback_A2" ---
            # create an object to store info about Routine feedback_A2
            feedback_A2 = data.Routine(
                name='feedback_A2',
                components=[feedback_text_A2],
            )
            feedback_A2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_A2
            key_resp_A2_rt_sum_temp = key_resp_A2_rt_sum_temp + float(str(key_resp_A2.rt))
            
            if key_resp_A2.corr:
                key_resp_A2_corr_sum_temp =key_resp_A2_corr_sum_temp +1
                continueRoutine = False
            else:
                msg = 'error'
            feedback_text_A2.setText(msg)
            # store start times for feedback_A2
            feedback_A2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback_A2.tStart = globalClock.getTime(format='float')
            feedback_A2.status = STARTED
            thisExp.addData('feedback_A2.started', feedback_A2.tStart)
            feedback_A2.maxDuration = None
            # keep track of which components have finished
            feedback_A2Components = feedback_A2.components
            for thisComponent in feedback_A2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback_A2" ---
            # if trial has changed, end Routine now
            if isinstance(trials_4, data.TrialHandler2) and thisTrial_4.thisN != trials_4.thisTrial.thisN:
                continueRoutine = False
            feedback_A2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text_A2* updates
                
                # if feedback_text_A2 is starting this frame...
                if feedback_text_A2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_A2.frameNStart = frameN  # exact frame index
                    feedback_text_A2.tStart = t  # local t and not account for scr refresh
                    feedback_text_A2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_A2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_A2.started')
                    # update status
                    feedback_text_A2.status = STARTED
                    feedback_text_A2.setAutoDraw(True)
                
                # if feedback_text_A2 is active this frame...
                if feedback_text_A2.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text_A2 is stopping this frame...
                if feedback_text_A2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text_A2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text_A2.tStop = t  # not accounting for scr refresh
                        feedback_text_A2.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_text_A2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text_A2.stopped')
                        # update status
                        feedback_text_A2.status = FINISHED
                        feedback_text_A2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback_A2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_A2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback_A2" ---
            for thisComponent in feedback_A2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback_A2
            feedback_A2.tStop = globalClock.getTime(format='float')
            feedback_A2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback_A2.stopped', feedback_A2.tStop)
            # Run 'End Routine' code from code_A2
            key_resp_A2_corr_sum = key_resp_A2_corr_sum_temp
            key_resp_A2_rt_sum = key_resp_A2_rt_sum_temp
            
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback_A2.maxDurationReached:
                routineTimer.addTime(-feedback_A2.maxDuration)
            elif feedback_A2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "ISI250" ---
            # create an object to store info about Routine ISI250
            ISI250 = data.Routine(
                name='ISI250',
                components=[],
            )
            ISI250.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for ISI250
            ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI250.tStart = globalClock.getTime(format='float')
            ISI250.status = STARTED
            thisExp.addData('ISI250.started', ISI250.tStart)
            ISI250.maxDuration = 0.25
            # keep track of which components have finished
            ISI250Components = ISI250.components
            for thisComponent in ISI250.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI250" ---
            # if trial has changed, end Routine now
            if isinstance(trials_4, data.TrialHandler2) and thisTrial_4.thisN != trials_4.thisTrial.thisN:
                continueRoutine = False
            ISI250.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > ISI250.maxDuration-frameTolerance:
                    ISI250.maxDurationReached = True
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI250.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI250.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI250" ---
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI250
            ISI250.tStop = globalClock.getTime(format='float')
            ISI250.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI250.stopped', ISI250.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if ISI250.maxDurationReached:
                routineTimer.addTime(-ISI250.maxDuration)
            elif ISI250.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_4'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "score_A2" ---
        # create an object to store info about Routine score_A2
        score_A2 = data.Routine(
            name='score_A2',
            components=[score_A2_text, key_resp_3],
        )
        score_A2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_3
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # Run 'Begin Routine' code from score_A2_code
        feedback_msg ="" 
        
        accuracy = round((key_resp_A2_corr_sum / 50) * 100, 2)  
        rt_average = round((key_resp_A2_rt_sum / 50) * 1000, 2)  
        
        feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
        feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
        feedback_msg += "Press space bar to continue."
        # store start times for score_A2
        score_A2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        score_A2.tStart = globalClock.getTime(format='float')
        score_A2.status = STARTED
        thisExp.addData('score_A2.started', score_A2.tStart)
        score_A2.maxDuration = None
        # keep track of which components have finished
        score_A2Components = score_A2.components
        for thisComponent in score_A2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "score_A2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        score_A2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *score_A2_text* updates
            
            # if score_A2_text is starting this frame...
            if score_A2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_A2_text.frameNStart = frameN  # exact frame index
                score_A2_text.tStart = t  # local t and not account for scr refresh
                score_A2_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_A2_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'score_A2_text.started')
                # update status
                score_A2_text.status = STARTED
                score_A2_text.setAutoDraw(True)
            
            # if score_A2_text is active this frame...
            if score_A2_text.status == STARTED:
                # update params
                score_A2_text.setText(feedback_msg, log=False)
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                score_A2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in score_A2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "score_A2" ---
        for thisComponent in score_A2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for score_A2
        score_A2.tStop = globalClock.getTime(format='float')
        score_A2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('score_A2.stopped', score_A2.tStop)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials_20.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials_20.addData('key_resp_3.rt', key_resp_3.rt)
            trials_20.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "score_A2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "reminder_B1" ---
        # create an object to store info about Routine reminder_B1
        reminder_B1 = data.Routine(
            name='reminder_B1',
            components=[text_46, key_resp_24],
        )
        reminder_B1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_24
        key_resp_24.keys = []
        key_resp_24.rt = []
        _key_resp_24_allKeys = []
        # store start times for reminder_B1
        reminder_B1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reminder_B1.tStart = globalClock.getTime(format='float')
        reminder_B1.status = STARTED
        thisExp.addData('reminder_B1.started', reminder_B1.tStart)
        reminder_B1.maxDuration = None
        # keep track of which components have finished
        reminder_B1Components = reminder_B1.components
        for thisComponent in reminder_B1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reminder_B1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        reminder_B1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_46* updates
            
            # if text_46 is starting this frame...
            if text_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_46.frameNStart = frameN  # exact frame index
                text_46.tStart = t  # local t and not account for scr refresh
                text_46.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_46, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_46.started')
                # update status
                text_46.status = STARTED
                text_46.setAutoDraw(True)
            
            # if text_46 is active this frame...
            if text_46.status == STARTED:
                # update params
                pass
            
            # *key_resp_24* updates
            waitOnFlip = False
            
            # if key_resp_24 is starting this frame...
            if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_24.frameNStart = frameN  # exact frame index
                key_resp_24.tStart = t  # local t and not account for scr refresh
                key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_24.started')
                # update status
                key_resp_24.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_24.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_24.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_24_allKeys.extend(theseKeys)
                if len(_key_resp_24_allKeys):
                    key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
                    key_resp_24.rt = _key_resp_24_allKeys[-1].rt
                    key_resp_24.duration = _key_resp_24_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                reminder_B1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reminder_B1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reminder_B1" ---
        for thisComponent in reminder_B1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reminder_B1
        reminder_B1.tStop = globalClock.getTime(format='float')
        reminder_B1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reminder_B1.stopped', reminder_B1.tStop)
        # check responses
        if key_resp_24.keys in ['', [], None]:  # No response was made
            key_resp_24.keys = None
        trials_20.addData('key_resp_24.keys',key_resp_24.keys)
        if key_resp_24.keys != None:  # we had a response
            trials_20.addData('key_resp_24.rt', key_resp_24.rt)
            trials_20.addData('key_resp_24.duration', key_resp_24.duration)
        # the Routine "reminder_B1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ISI1500" ---
        # create an object to store info about Routine ISI1500
        ISI1500 = data.Routine(
            name='ISI1500',
            components=[text_3],
        )
        ISI1500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI1500
        ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI1500.tStart = globalClock.getTime(format='float')
        ISI1500.status = STARTED
        thisExp.addData('ISI1500.started', ISI1500.tStart)
        ISI1500.maxDuration = 1.5
        # keep track of which components have finished
        ISI1500Components = ISI1500.components
        for thisComponent in ISI1500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI1500" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        ISI1500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI1500.maxDuration-frameTolerance:
                ISI1500.maxDurationReached = True
                continueRoutine = False
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # if text_3 is stopping this frame...
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    # update status
                    text_3.status = FINISHED
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI1500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI1500" ---
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI1500
        ISI1500.tStop = globalClock.getTime(format='float')
        ISI1500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI1500.stopped', ISI1500.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI1500.maxDurationReached:
            routineTimer.addTime(-ISI1500.maxDuration)
        elif ISI1500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # set up handler to look after randomisation of conditions etc
        trials_7 = data.TrialHandler2(
            name='trials_7',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('excel/TaskB_Positive_ornot.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials_7)  # add the loop to the experiment
        thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
        if thisTrial_7 != None:
            for paramName in thisTrial_7:
                globals()[paramName] = thisTrial_7[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_7 in trials_7:
            currentLoop = trials_7
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
            if thisTrial_7 != None:
                for paramName in thisTrial_7:
                    globals()[paramName] = thisTrial_7[paramName]
            
            # --- Prepare to start Routine "practice_Task_B1" ---
            # create an object to store info about Routine practice_Task_B1
            practice_Task_B1 = data.Routine(
                name='practice_Task_B1',
                components=[text_B1, key_resp_B1],
            )
            practice_Task_B1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            text_B1.setText(words)
            # create starting attributes for key_resp_B1
            key_resp_B1.keys = []
            key_resp_B1.rt = []
            _key_resp_B1_allKeys = []
            # store start times for practice_Task_B1
            practice_Task_B1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            practice_Task_B1.tStart = globalClock.getTime(format='float')
            practice_Task_B1.status = STARTED
            thisExp.addData('practice_Task_B1.started', practice_Task_B1.tStart)
            practice_Task_B1.maxDuration = None
            # keep track of which components have finished
            practice_Task_B1Components = practice_Task_B1.components
            for thisComponent in practice_Task_B1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "practice_Task_B1" ---
            # if trial has changed, end Routine now
            if isinstance(trials_7, data.TrialHandler2) and thisTrial_7.thisN != trials_7.thisTrial.thisN:
                continueRoutine = False
            practice_Task_B1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_B1* updates
                
                # if text_B1 is starting this frame...
                if text_B1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_B1.frameNStart = frameN  # exact frame index
                    text_B1.tStart = t  # local t and not account for scr refresh
                    text_B1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_B1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_B1.started')
                    # update status
                    text_B1.status = STARTED
                    text_B1.setAutoDraw(True)
                
                # if text_B1 is active this frame...
                if text_B1.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_B1* updates
                waitOnFlip = False
                
                # if key_resp_B1 is starting this frame...
                if key_resp_B1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_B1.frameNStart = frameN  # exact frame index
                    key_resp_B1.tStart = t  # local t and not account for scr refresh
                    key_resp_B1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_B1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_B1.started')
                    # update status
                    key_resp_B1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_B1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_B1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_B1.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_B1.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_B1_allKeys.extend(theseKeys)
                    if len(_key_resp_B1_allKeys):
                        key_resp_B1.keys = _key_resp_B1_allKeys[-1].name  # just the last key pressed
                        key_resp_B1.rt = _key_resp_B1_allKeys[-1].rt
                        key_resp_B1.duration = _key_resp_B1_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_B1.keys == str(keypad)) or (key_resp_B1.keys == keypad):
                            key_resp_B1.corr = 1
                        else:
                            key_resp_B1.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    practice_Task_B1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practice_Task_B1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practice_Task_B1" ---
            for thisComponent in practice_Task_B1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for practice_Task_B1
            practice_Task_B1.tStop = globalClock.getTime(format='float')
            practice_Task_B1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('practice_Task_B1.stopped', practice_Task_B1.tStop)
            # check responses
            if key_resp_B1.keys in ['', [], None]:  # No response was made
                key_resp_B1.keys = None
                # was no response the correct answer?!
                if str(keypad).lower() == 'none':
                   key_resp_B1.corr = 1;  # correct non-response
                else:
                   key_resp_B1.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_7 (TrialHandler)
            trials_7.addData('key_resp_B1.keys',key_resp_B1.keys)
            trials_7.addData('key_resp_B1.corr', key_resp_B1.corr)
            if key_resp_B1.keys != None:  # we had a response
                trials_7.addData('key_resp_B1.rt', key_resp_B1.rt)
                trials_7.addData('key_resp_B1.duration', key_resp_B1.duration)
            # the Routine "practice_Task_B1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback_B1" ---
            # create an object to store info about Routine feedback_B1
            feedback_B1 = data.Routine(
                name='feedback_B1',
                components=[feedback_text_B1],
            )
            feedback_B1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_B1
            key_resp_B1_rt_sum_temp = key_resp_B1_rt_sum_temp + float(str(key_resp_B1.rt))
            
            if key_resp_B1.corr:
                key_resp_B1_corr_sum_temp =key_resp_B1_corr_sum_temp +1
                continueRoutine = False
            else:
                msg = 'error'
            feedback_text_B1.setText(msg)
            # store start times for feedback_B1
            feedback_B1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback_B1.tStart = globalClock.getTime(format='float')
            feedback_B1.status = STARTED
            thisExp.addData('feedback_B1.started', feedback_B1.tStart)
            feedback_B1.maxDuration = None
            # keep track of which components have finished
            feedback_B1Components = feedback_B1.components
            for thisComponent in feedback_B1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback_B1" ---
            # if trial has changed, end Routine now
            if isinstance(trials_7, data.TrialHandler2) and thisTrial_7.thisN != trials_7.thisTrial.thisN:
                continueRoutine = False
            feedback_B1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text_B1* updates
                
                # if feedback_text_B1 is starting this frame...
                if feedback_text_B1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_B1.frameNStart = frameN  # exact frame index
                    feedback_text_B1.tStart = t  # local t and not account for scr refresh
                    feedback_text_B1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_B1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_B1.started')
                    # update status
                    feedback_text_B1.status = STARTED
                    feedback_text_B1.setAutoDraw(True)
                
                # if feedback_text_B1 is active this frame...
                if feedback_text_B1.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text_B1 is stopping this frame...
                if feedback_text_B1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text_B1.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text_B1.tStop = t  # not accounting for scr refresh
                        feedback_text_B1.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_text_B1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text_B1.stopped')
                        # update status
                        feedback_text_B1.status = FINISHED
                        feedback_text_B1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback_B1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_B1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback_B1" ---
            for thisComponent in feedback_B1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback_B1
            feedback_B1.tStop = globalClock.getTime(format='float')
            feedback_B1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback_B1.stopped', feedback_B1.tStop)
            # Run 'End Routine' code from code_B1
            key_resp_B1_corr_sum = key_resp_B1_corr_sum_temp
            key_resp_B1_rt_sum = key_resp_B1_rt_sum_temp
            
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback_B1.maxDurationReached:
                routineTimer.addTime(-feedback_B1.maxDuration)
            elif feedback_B1.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "ISI250" ---
            # create an object to store info about Routine ISI250
            ISI250 = data.Routine(
                name='ISI250',
                components=[],
            )
            ISI250.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for ISI250
            ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI250.tStart = globalClock.getTime(format='float')
            ISI250.status = STARTED
            thisExp.addData('ISI250.started', ISI250.tStart)
            ISI250.maxDuration = 0.25
            # keep track of which components have finished
            ISI250Components = ISI250.components
            for thisComponent in ISI250.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI250" ---
            # if trial has changed, end Routine now
            if isinstance(trials_7, data.TrialHandler2) and thisTrial_7.thisN != trials_7.thisTrial.thisN:
                continueRoutine = False
            ISI250.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > ISI250.maxDuration-frameTolerance:
                    ISI250.maxDurationReached = True
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI250.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI250.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI250" ---
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI250
            ISI250.tStop = globalClock.getTime(format='float')
            ISI250.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI250.stopped', ISI250.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if ISI250.maxDurationReached:
                routineTimer.addTime(-ISI250.maxDuration)
            elif ISI250.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_7'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "score_B1" ---
        # create an object to store info about Routine score_B1
        score_B1 = data.Routine(
            name='score_B1',
            components=[score_B1_text, key_resp_6],
        )
        score_B1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_6
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # Run 'Begin Routine' code from score_B1_code
        feedback_msg ="" 
        
        accuracy = round((key_resp_B1_corr_sum / 50) * 100, 2)  
        rt_average = round((key_resp_B1_rt_sum / 50) * 1000, 2)  
        
        feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
        feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
        feedback_msg += "Press space bar to continue."
        # store start times for score_B1
        score_B1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        score_B1.tStart = globalClock.getTime(format='float')
        score_B1.status = STARTED
        thisExp.addData('score_B1.started', score_B1.tStart)
        score_B1.maxDuration = None
        # keep track of which components have finished
        score_B1Components = score_B1.components
        for thisComponent in score_B1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "score_B1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        score_B1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *score_B1_text* updates
            
            # if score_B1_text is starting this frame...
            if score_B1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_B1_text.frameNStart = frameN  # exact frame index
                score_B1_text.tStart = t  # local t and not account for scr refresh
                score_B1_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_B1_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'score_B1_text.started')
                # update status
                score_B1_text.status = STARTED
                score_B1_text.setAutoDraw(True)
            
            # if score_B1_text is active this frame...
            if score_B1_text.status == STARTED:
                # update params
                score_B1_text.setText(feedback_msg, log=False)
            
            # *key_resp_6* updates
            waitOnFlip = False
            
            # if key_resp_6 is starting this frame...
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_6.started')
                # update status
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                score_B1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in score_B1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "score_B1" ---
        for thisComponent in score_B1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for score_B1
        score_B1.tStop = globalClock.getTime(format='float')
        score_B1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('score_B1.stopped', score_B1.tStop)
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        trials_20.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            trials_20.addData('key_resp_6.rt', key_resp_6.rt)
            trials_20.addData('key_resp_6.duration', key_resp_6.duration)
        # the Routine "score_B1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "reminder_B2" ---
        # create an object to store info about Routine reminder_B2
        reminder_B2 = data.Routine(
            name='reminder_B2',
            components=[text_47, key_resp_25],
        )
        reminder_B2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_25
        key_resp_25.keys = []
        key_resp_25.rt = []
        _key_resp_25_allKeys = []
        # store start times for reminder_B2
        reminder_B2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reminder_B2.tStart = globalClock.getTime(format='float')
        reminder_B2.status = STARTED
        thisExp.addData('reminder_B2.started', reminder_B2.tStart)
        reminder_B2.maxDuration = None
        # keep track of which components have finished
        reminder_B2Components = reminder_B2.components
        for thisComponent in reminder_B2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reminder_B2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        reminder_B2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_47* updates
            
            # if text_47 is starting this frame...
            if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_47.frameNStart = frameN  # exact frame index
                text_47.tStart = t  # local t and not account for scr refresh
                text_47.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_47.started')
                # update status
                text_47.status = STARTED
                text_47.setAutoDraw(True)
            
            # if text_47 is active this frame...
            if text_47.status == STARTED:
                # update params
                pass
            
            # *key_resp_25* updates
            waitOnFlip = False
            
            # if key_resp_25 is starting this frame...
            if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_25.frameNStart = frameN  # exact frame index
                key_resp_25.tStart = t  # local t and not account for scr refresh
                key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_25.started')
                # update status
                key_resp_25.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_25.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_25.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_25_allKeys.extend(theseKeys)
                if len(_key_resp_25_allKeys):
                    key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
                    key_resp_25.rt = _key_resp_25_allKeys[-1].rt
                    key_resp_25.duration = _key_resp_25_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                reminder_B2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reminder_B2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reminder_B2" ---
        for thisComponent in reminder_B2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reminder_B2
        reminder_B2.tStop = globalClock.getTime(format='float')
        reminder_B2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reminder_B2.stopped', reminder_B2.tStop)
        # check responses
        if key_resp_25.keys in ['', [], None]:  # No response was made
            key_resp_25.keys = None
        trials_20.addData('key_resp_25.keys',key_resp_25.keys)
        if key_resp_25.keys != None:  # we had a response
            trials_20.addData('key_resp_25.rt', key_resp_25.rt)
            trials_20.addData('key_resp_25.duration', key_resp_25.duration)
        # the Routine "reminder_B2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ISI1500" ---
        # create an object to store info about Routine ISI1500
        ISI1500 = data.Routine(
            name='ISI1500',
            components=[text_3],
        )
        ISI1500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI1500
        ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI1500.tStart = globalClock.getTime(format='float')
        ISI1500.status = STARTED
        thisExp.addData('ISI1500.started', ISI1500.tStart)
        ISI1500.maxDuration = 1.5
        # keep track of which components have finished
        ISI1500Components = ISI1500.components
        for thisComponent in ISI1500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI1500" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        ISI1500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI1500.maxDuration-frameTolerance:
                ISI1500.maxDurationReached = True
                continueRoutine = False
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # if text_3 is stopping this frame...
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    # update status
                    text_3.status = FINISHED
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI1500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI1500" ---
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI1500
        ISI1500.tStop = globalClock.getTime(format='float')
        ISI1500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI1500.stopped', ISI1500.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI1500.maxDurationReached:
            routineTimer.addTime(-ISI1500.maxDuration)
        elif ISI1500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler2(
            name='trials_2',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('excel/TaskB_Positive_ornot.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            
            # --- Prepare to start Routine "record_Task_B2" ---
            # create an object to store info about Routine record_Task_B2
            record_Task_B2 = data.Routine(
                name='record_Task_B2',
                components=[text_B2, key_resp_B2],
            )
            record_Task_B2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            text_B2.setText(words)
            # create starting attributes for key_resp_B2
            key_resp_B2.keys = []
            key_resp_B2.rt = []
            _key_resp_B2_allKeys = []
            # store start times for record_Task_B2
            record_Task_B2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            record_Task_B2.tStart = globalClock.getTime(format='float')
            record_Task_B2.status = STARTED
            thisExp.addData('record_Task_B2.started', record_Task_B2.tStart)
            record_Task_B2.maxDuration = None
            # keep track of which components have finished
            record_Task_B2Components = record_Task_B2.components
            for thisComponent in record_Task_B2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "record_Task_B2" ---
            # if trial has changed, end Routine now
            if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
                continueRoutine = False
            record_Task_B2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_B2* updates
                
                # if text_B2 is starting this frame...
                if text_B2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_B2.frameNStart = frameN  # exact frame index
                    text_B2.tStart = t  # local t and not account for scr refresh
                    text_B2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_B2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_B2.started')
                    # update status
                    text_B2.status = STARTED
                    text_B2.setAutoDraw(True)
                
                # if text_B2 is active this frame...
                if text_B2.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_B2* updates
                waitOnFlip = False
                
                # if key_resp_B2 is starting this frame...
                if key_resp_B2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_B2.frameNStart = frameN  # exact frame index
                    key_resp_B2.tStart = t  # local t and not account for scr refresh
                    key_resp_B2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_B2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_B2.started')
                    # update status
                    key_resp_B2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_B2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_B2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_B2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_B2.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_B2_allKeys.extend(theseKeys)
                    if len(_key_resp_B2_allKeys):
                        key_resp_B2.keys = _key_resp_B2_allKeys[-1].name  # just the last key pressed
                        key_resp_B2.rt = _key_resp_B2_allKeys[-1].rt
                        key_resp_B2.duration = _key_resp_B2_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_B2.keys == str(keypad)) or (key_resp_B2.keys == keypad):
                            key_resp_B2.corr = 1
                        else:
                            key_resp_B2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    record_Task_B2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in record_Task_B2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "record_Task_B2" ---
            for thisComponent in record_Task_B2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for record_Task_B2
            record_Task_B2.tStop = globalClock.getTime(format='float')
            record_Task_B2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('record_Task_B2.stopped', record_Task_B2.tStop)
            # check responses
            if key_resp_B2.keys in ['', [], None]:  # No response was made
                key_resp_B2.keys = None
                # was no response the correct answer?!
                if str(keypad).lower() == 'none':
                   key_resp_B2.corr = 1;  # correct non-response
                else:
                   key_resp_B2.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_2 (TrialHandler)
            trials_2.addData('key_resp_B2.keys',key_resp_B2.keys)
            trials_2.addData('key_resp_B2.corr', key_resp_B2.corr)
            if key_resp_B2.keys != None:  # we had a response
                trials_2.addData('key_resp_B2.rt', key_resp_B2.rt)
                trials_2.addData('key_resp_B2.duration', key_resp_B2.duration)
            # the Routine "record_Task_B2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback_B2" ---
            # create an object to store info about Routine feedback_B2
            feedback_B2 = data.Routine(
                name='feedback_B2',
                components=[feedback_text_B2],
            )
            feedback_B2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_B2
            key_resp_B2_rt_sum_temp = key_resp_B2_rt_sum_temp + float(str(key_resp_B2.rt))
            
            if key_resp_B2.corr:
                key_resp_B2_corr_sum_temp =key_resp_B2_corr_sum_temp +1
                continueRoutine = False
            else:
                msg = 'error'
            feedback_text_B2.setText(msg)
            # store start times for feedback_B2
            feedback_B2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback_B2.tStart = globalClock.getTime(format='float')
            feedback_B2.status = STARTED
            thisExp.addData('feedback_B2.started', feedback_B2.tStart)
            feedback_B2.maxDuration = None
            # keep track of which components have finished
            feedback_B2Components = feedback_B2.components
            for thisComponent in feedback_B2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback_B2" ---
            # if trial has changed, end Routine now
            if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
                continueRoutine = False
            feedback_B2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text_B2* updates
                
                # if feedback_text_B2 is starting this frame...
                if feedback_text_B2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_B2.frameNStart = frameN  # exact frame index
                    feedback_text_B2.tStart = t  # local t and not account for scr refresh
                    feedback_text_B2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_B2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_B2.started')
                    # update status
                    feedback_text_B2.status = STARTED
                    feedback_text_B2.setAutoDraw(True)
                
                # if feedback_text_B2 is active this frame...
                if feedback_text_B2.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text_B2 is stopping this frame...
                if feedback_text_B2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text_B2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text_B2.tStop = t  # not accounting for scr refresh
                        feedback_text_B2.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_text_B2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text_B2.stopped')
                        # update status
                        feedback_text_B2.status = FINISHED
                        feedback_text_B2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback_B2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_B2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback_B2" ---
            for thisComponent in feedback_B2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback_B2
            feedback_B2.tStop = globalClock.getTime(format='float')
            feedback_B2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback_B2.stopped', feedback_B2.tStop)
            # Run 'End Routine' code from code_B2
            key_resp_B2_corr_sum = key_resp_B2_corr_sum_temp
            key_resp_B2_rt_sum = key_resp_B2_rt_sum_temp
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback_B2.maxDurationReached:
                routineTimer.addTime(-feedback_B2.maxDuration)
            elif feedback_B2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "ISI250" ---
            # create an object to store info about Routine ISI250
            ISI250 = data.Routine(
                name='ISI250',
                components=[],
            )
            ISI250.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for ISI250
            ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI250.tStart = globalClock.getTime(format='float')
            ISI250.status = STARTED
            thisExp.addData('ISI250.started', ISI250.tStart)
            ISI250.maxDuration = 0.25
            # keep track of which components have finished
            ISI250Components = ISI250.components
            for thisComponent in ISI250.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI250" ---
            # if trial has changed, end Routine now
            if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
                continueRoutine = False
            ISI250.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > ISI250.maxDuration-frameTolerance:
                    ISI250.maxDurationReached = True
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI250.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI250.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI250" ---
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI250
            ISI250.tStop = globalClock.getTime(format='float')
            ISI250.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI250.stopped', ISI250.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if ISI250.maxDurationReached:
                routineTimer.addTime(-ISI250.maxDuration)
            elif ISI250.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "score_B2" ---
        # create an object to store info about Routine score_B2
        score_B2 = data.Routine(
            name='score_B2',
            components=[score_B2_text, key_resp_4],
        )
        score_B2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_4
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # Run 'Begin Routine' code from score_B2_code
        feedback_msg ="" 
        
        accuracy = round((key_resp_B2_corr_sum / 50) * 100, 2)  
        rt_average = round((key_resp_B2_rt_sum / 50) * 1000, 2)  
        
        feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
        feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
        feedback_msg += "Press space bar to continue."
        # store start times for score_B2
        score_B2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        score_B2.tStart = globalClock.getTime(format='float')
        score_B2.status = STARTED
        thisExp.addData('score_B2.started', score_B2.tStart)
        score_B2.maxDuration = None
        # keep track of which components have finished
        score_B2Components = score_B2.components
        for thisComponent in score_B2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "score_B2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        score_B2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *score_B2_text* updates
            
            # if score_B2_text is starting this frame...
            if score_B2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_B2_text.frameNStart = frameN  # exact frame index
                score_B2_text.tStart = t  # local t and not account for scr refresh
                score_B2_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_B2_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'score_B2_text.started')
                # update status
                score_B2_text.status = STARTED
                score_B2_text.setAutoDraw(True)
            
            # if score_B2_text is active this frame...
            if score_B2_text.status == STARTED:
                # update params
                score_B2_text.setText(feedback_msg, log=False)
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                score_B2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in score_B2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "score_B2" ---
        for thisComponent in score_B2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for score_B2
        score_B2.tStop = globalClock.getTime(format='float')
        score_B2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('score_B2.stopped', score_B2.tStop)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials_20.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials_20.addData('key_resp_4.rt', key_resp_4.rt)
            trials_20.addData('key_resp_4.duration', key_resp_4.duration)
        # the Routine "score_B2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "reminder_C1" ---
        # create an object to store info about Routine reminder_C1
        reminder_C1 = data.Routine(
            name='reminder_C1',
            components=[text_20, key_resp_26],
        )
        reminder_C1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_26
        key_resp_26.keys = []
        key_resp_26.rt = []
        _key_resp_26_allKeys = []
        # store start times for reminder_C1
        reminder_C1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reminder_C1.tStart = globalClock.getTime(format='float')
        reminder_C1.status = STARTED
        thisExp.addData('reminder_C1.started', reminder_C1.tStart)
        reminder_C1.maxDuration = None
        # keep track of which components have finished
        reminder_C1Components = reminder_C1.components
        for thisComponent in reminder_C1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reminder_C1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        reminder_C1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_20* updates
            
            # if text_20 is starting this frame...
            if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_20.frameNStart = frameN  # exact frame index
                text_20.tStart = t  # local t and not account for scr refresh
                text_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_20.started')
                # update status
                text_20.status = STARTED
                text_20.setAutoDraw(True)
            
            # if text_20 is active this frame...
            if text_20.status == STARTED:
                # update params
                pass
            
            # *key_resp_26* updates
            waitOnFlip = False
            
            # if key_resp_26 is starting this frame...
            if key_resp_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_26.frameNStart = frameN  # exact frame index
                key_resp_26.tStart = t  # local t and not account for scr refresh
                key_resp_26.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_26, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_26.started')
                # update status
                key_resp_26.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_26.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_26.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_26_allKeys.extend(theseKeys)
                if len(_key_resp_26_allKeys):
                    key_resp_26.keys = _key_resp_26_allKeys[-1].name  # just the last key pressed
                    key_resp_26.rt = _key_resp_26_allKeys[-1].rt
                    key_resp_26.duration = _key_resp_26_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                reminder_C1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reminder_C1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reminder_C1" ---
        for thisComponent in reminder_C1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reminder_C1
        reminder_C1.tStop = globalClock.getTime(format='float')
        reminder_C1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reminder_C1.stopped', reminder_C1.tStop)
        # check responses
        if key_resp_26.keys in ['', [], None]:  # No response was made
            key_resp_26.keys = None
        trials_20.addData('key_resp_26.keys',key_resp_26.keys)
        if key_resp_26.keys != None:  # we had a response
            trials_20.addData('key_resp_26.rt', key_resp_26.rt)
            trials_20.addData('key_resp_26.duration', key_resp_26.duration)
        # the Routine "reminder_C1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ISI1500" ---
        # create an object to store info about Routine ISI1500
        ISI1500 = data.Routine(
            name='ISI1500',
            components=[text_3],
        )
        ISI1500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI1500
        ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI1500.tStart = globalClock.getTime(format='float')
        ISI1500.status = STARTED
        thisExp.addData('ISI1500.started', ISI1500.tStart)
        ISI1500.maxDuration = 1.5
        # keep track of which components have finished
        ISI1500Components = ISI1500.components
        for thisComponent in ISI1500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI1500" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        ISI1500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI1500.maxDuration-frameTolerance:
                ISI1500.maxDurationReached = True
                continueRoutine = False
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # if text_3 is stopping this frame...
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    # update status
                    text_3.status = FINISHED
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI1500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI1500" ---
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI1500
        ISI1500.tStop = globalClock.getTime(format='float')
        ISI1500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI1500.stopped', ISI1500.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI1500.maxDurationReached:
            routineTimer.addTime(-ISI1500.maxDuration)
        elif ISI1500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # set up handler to look after randomisation of conditions etc
        trials_3 = data.TrialHandler2(
            name='trials_3',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('excel/TaskC1_E2_block1st3rd_congruent_japan_prefer.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials_3)  # add the loop to the experiment
        thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_3 in trials_3:
            currentLoop = trials_3
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    globals()[paramName] = thisTrial_3[paramName]
            
            # --- Prepare to start Routine "record_Task_C1" ---
            # create an object to store info about Routine record_Task_C1
            record_Task_C1 = data.Routine(
                name='record_Task_C1',
                components=[text_C1, key_resp_C1],
            )
            record_Task_C1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            text_C1.setText(words)
            # create starting attributes for key_resp_C1
            key_resp_C1.keys = []
            key_resp_C1.rt = []
            _key_resp_C1_allKeys = []
            # store start times for record_Task_C1
            record_Task_C1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            record_Task_C1.tStart = globalClock.getTime(format='float')
            record_Task_C1.status = STARTED
            thisExp.addData('record_Task_C1.started', record_Task_C1.tStart)
            record_Task_C1.maxDuration = None
            # keep track of which components have finished
            record_Task_C1Components = record_Task_C1.components
            for thisComponent in record_Task_C1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "record_Task_C1" ---
            # if trial has changed, end Routine now
            if isinstance(trials_3, data.TrialHandler2) and thisTrial_3.thisN != trials_3.thisTrial.thisN:
                continueRoutine = False
            record_Task_C1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_C1* updates
                
                # if text_C1 is starting this frame...
                if text_C1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_C1.frameNStart = frameN  # exact frame index
                    text_C1.tStart = t  # local t and not account for scr refresh
                    text_C1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_C1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_C1.started')
                    # update status
                    text_C1.status = STARTED
                    text_C1.setAutoDraw(True)
                
                # if text_C1 is active this frame...
                if text_C1.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_C1* updates
                waitOnFlip = False
                
                # if key_resp_C1 is starting this frame...
                if key_resp_C1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_C1.frameNStart = frameN  # exact frame index
                    key_resp_C1.tStart = t  # local t and not account for scr refresh
                    key_resp_C1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_C1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_C1.started')
                    # update status
                    key_resp_C1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_C1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_C1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_C1.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_C1.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_C1_allKeys.extend(theseKeys)
                    if len(_key_resp_C1_allKeys):
                        key_resp_C1.keys = _key_resp_C1_allKeys[-1].name  # just the last key pressed
                        key_resp_C1.rt = _key_resp_C1_allKeys[-1].rt
                        key_resp_C1.duration = _key_resp_C1_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_C1.keys == str(keypad)) or (key_resp_C1.keys == keypad):
                            key_resp_C1.corr = 1
                        else:
                            key_resp_C1.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    record_Task_C1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in record_Task_C1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "record_Task_C1" ---
            for thisComponent in record_Task_C1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for record_Task_C1
            record_Task_C1.tStop = globalClock.getTime(format='float')
            record_Task_C1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('record_Task_C1.stopped', record_Task_C1.tStop)
            # check responses
            if key_resp_C1.keys in ['', [], None]:  # No response was made
                key_resp_C1.keys = None
                # was no response the correct answer?!
                if str(keypad).lower() == 'none':
                   key_resp_C1.corr = 1;  # correct non-response
                else:
                   key_resp_C1.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_3 (TrialHandler)
            trials_3.addData('key_resp_C1.keys',key_resp_C1.keys)
            trials_3.addData('key_resp_C1.corr', key_resp_C1.corr)
            if key_resp_C1.keys != None:  # we had a response
                trials_3.addData('key_resp_C1.rt', key_resp_C1.rt)
                trials_3.addData('key_resp_C1.duration', key_resp_C1.duration)
            # the Routine "record_Task_C1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback_C1" ---
            # create an object to store info about Routine feedback_C1
            feedback_C1 = data.Routine(
                name='feedback_C1',
                components=[feedback_text_C1],
            )
            feedback_C1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_C1
            key_resp_C1_rt_sum_temp = key_resp_C1_rt_sum_temp + float(str(key_resp_C1.rt))
            
            if key_resp_C1.corr:
                key_resp_C1_corr_sum_temp =key_resp_C1_corr_sum_temp +1
                continueRoutine = False
            else:
                msg = 'error'
            feedback_text_C1.setText(msg)
            # store start times for feedback_C1
            feedback_C1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback_C1.tStart = globalClock.getTime(format='float')
            feedback_C1.status = STARTED
            thisExp.addData('feedback_C1.started', feedback_C1.tStart)
            feedback_C1.maxDuration = None
            # keep track of which components have finished
            feedback_C1Components = feedback_C1.components
            for thisComponent in feedback_C1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback_C1" ---
            # if trial has changed, end Routine now
            if isinstance(trials_3, data.TrialHandler2) and thisTrial_3.thisN != trials_3.thisTrial.thisN:
                continueRoutine = False
            feedback_C1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text_C1* updates
                
                # if feedback_text_C1 is starting this frame...
                if feedback_text_C1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_C1.frameNStart = frameN  # exact frame index
                    feedback_text_C1.tStart = t  # local t and not account for scr refresh
                    feedback_text_C1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_C1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_C1.started')
                    # update status
                    feedback_text_C1.status = STARTED
                    feedback_text_C1.setAutoDraw(True)
                
                # if feedback_text_C1 is active this frame...
                if feedback_text_C1.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text_C1 is stopping this frame...
                if feedback_text_C1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text_C1.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text_C1.tStop = t  # not accounting for scr refresh
                        feedback_text_C1.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_text_C1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text_C1.stopped')
                        # update status
                        feedback_text_C1.status = FINISHED
                        feedback_text_C1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback_C1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_C1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback_C1" ---
            for thisComponent in feedback_C1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback_C1
            feedback_C1.tStop = globalClock.getTime(format='float')
            feedback_C1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback_C1.stopped', feedback_C1.tStop)
            # Run 'End Routine' code from code_C1
            key_resp_C1_corr_sum = key_resp_C1_corr_sum_temp
            key_resp_C1_rt_sum = key_resp_C1_rt_sum_temp
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback_C1.maxDurationReached:
                routineTimer.addTime(-feedback_C1.maxDuration)
            elif feedback_C1.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "ISI250" ---
            # create an object to store info about Routine ISI250
            ISI250 = data.Routine(
                name='ISI250',
                components=[],
            )
            ISI250.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for ISI250
            ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI250.tStart = globalClock.getTime(format='float')
            ISI250.status = STARTED
            thisExp.addData('ISI250.started', ISI250.tStart)
            ISI250.maxDuration = 0.25
            # keep track of which components have finished
            ISI250Components = ISI250.components
            for thisComponent in ISI250.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI250" ---
            # if trial has changed, end Routine now
            if isinstance(trials_3, data.TrialHandler2) and thisTrial_3.thisN != trials_3.thisTrial.thisN:
                continueRoutine = False
            ISI250.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > ISI250.maxDuration-frameTolerance:
                    ISI250.maxDurationReached = True
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI250.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI250.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI250" ---
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI250
            ISI250.tStop = globalClock.getTime(format='float')
            ISI250.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI250.stopped', ISI250.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if ISI250.maxDurationReached:
                routineTimer.addTime(-ISI250.maxDuration)
            elif ISI250.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_3'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "score_C1" ---
        # create an object to store info about Routine score_C1
        score_C1 = data.Routine(
            name='score_C1',
            components=[score_C1_text, key_resp_5],
        )
        score_C1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from score_C1_code
        feedback_msg ="" 
        
        accuracy = round((key_resp_C1_corr_sum / 50) * 100, 2)  
        rt_average = round((key_resp_C1_rt_sum / 50) * 1000, 2)  
        
        feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
        feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
        feedback_msg += "Press space bar to continue."
        # create starting attributes for key_resp_5
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # store start times for score_C1
        score_C1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        score_C1.tStart = globalClock.getTime(format='float')
        score_C1.status = STARTED
        thisExp.addData('score_C1.started', score_C1.tStart)
        score_C1.maxDuration = None
        # keep track of which components have finished
        score_C1Components = score_C1.components
        for thisComponent in score_C1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "score_C1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        score_C1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *score_C1_text* updates
            
            # if score_C1_text is starting this frame...
            if score_C1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_C1_text.frameNStart = frameN  # exact frame index
                score_C1_text.tStart = t  # local t and not account for scr refresh
                score_C1_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_C1_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'score_C1_text.started')
                # update status
                score_C1_text.status = STARTED
                score_C1_text.setAutoDraw(True)
            
            # if score_C1_text is active this frame...
            if score_C1_text.status == STARTED:
                # update params
                score_C1_text.setText(feedback_msg, log=False)
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                score_C1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in score_C1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "score_C1" ---
        for thisComponent in score_C1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for score_C1
        score_C1.tStop = globalClock.getTime(format='float')
        score_C1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('score_C1.stopped', score_C1.tStop)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials_20.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials_20.addData('key_resp_5.rt', key_resp_5.rt)
            trials_20.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "score_C1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "reminder_C2" ---
        # create an object to store info about Routine reminder_C2
        reminder_C2 = data.Routine(
            name='reminder_C2',
            components=[text_21, key_resp_27],
        )
        reminder_C2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_27
        key_resp_27.keys = []
        key_resp_27.rt = []
        _key_resp_27_allKeys = []
        # store start times for reminder_C2
        reminder_C2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reminder_C2.tStart = globalClock.getTime(format='float')
        reminder_C2.status = STARTED
        thisExp.addData('reminder_C2.started', reminder_C2.tStart)
        reminder_C2.maxDuration = None
        # keep track of which components have finished
        reminder_C2Components = reminder_C2.components
        for thisComponent in reminder_C2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reminder_C2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        reminder_C2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_21* updates
            
            # if text_21 is starting this frame...
            if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_21.frameNStart = frameN  # exact frame index
                text_21.tStart = t  # local t and not account for scr refresh
                text_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_21.started')
                # update status
                text_21.status = STARTED
                text_21.setAutoDraw(True)
            
            # if text_21 is active this frame...
            if text_21.status == STARTED:
                # update params
                pass
            
            # *key_resp_27* updates
            waitOnFlip = False
            
            # if key_resp_27 is starting this frame...
            if key_resp_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_27.frameNStart = frameN  # exact frame index
                key_resp_27.tStart = t  # local t and not account for scr refresh
                key_resp_27.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_27, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_27.started')
                # update status
                key_resp_27.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_27.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_27.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_27.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_27.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_27_allKeys.extend(theseKeys)
                if len(_key_resp_27_allKeys):
                    key_resp_27.keys = _key_resp_27_allKeys[-1].name  # just the last key pressed
                    key_resp_27.rt = _key_resp_27_allKeys[-1].rt
                    key_resp_27.duration = _key_resp_27_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                reminder_C2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reminder_C2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reminder_C2" ---
        for thisComponent in reminder_C2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reminder_C2
        reminder_C2.tStop = globalClock.getTime(format='float')
        reminder_C2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reminder_C2.stopped', reminder_C2.tStop)
        # check responses
        if key_resp_27.keys in ['', [], None]:  # No response was made
            key_resp_27.keys = None
        trials_20.addData('key_resp_27.keys',key_resp_27.keys)
        if key_resp_27.keys != None:  # we had a response
            trials_20.addData('key_resp_27.rt', key_resp_27.rt)
            trials_20.addData('key_resp_27.duration', key_resp_27.duration)
        # the Routine "reminder_C2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ISI1500" ---
        # create an object to store info about Routine ISI1500
        ISI1500 = data.Routine(
            name='ISI1500',
            components=[text_3],
        )
        ISI1500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI1500
        ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI1500.tStart = globalClock.getTime(format='float')
        ISI1500.status = STARTED
        thisExp.addData('ISI1500.started', ISI1500.tStart)
        ISI1500.maxDuration = 1.5
        # keep track of which components have finished
        ISI1500Components = ISI1500.components
        for thisComponent in ISI1500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI1500" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        ISI1500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI1500.maxDuration-frameTolerance:
                ISI1500.maxDurationReached = True
                continueRoutine = False
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # if text_3 is stopping this frame...
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    # update status
                    text_3.status = FINISHED
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI1500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI1500" ---
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI1500
        ISI1500.tStop = globalClock.getTime(format='float')
        ISI1500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI1500.stopped', ISI1500.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI1500.maxDurationReached:
            routineTimer.addTime(-ISI1500.maxDuration)
        elif ISI1500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # set up handler to look after randomisation of conditions etc
        trials_5 = data.TrialHandler2(
            name='trials_5',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('excel/TaskC1_E2_block2nd_congruent_japan_prefer.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials_5)  # add the loop to the experiment
        thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                globals()[paramName] = thisTrial_5[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_5 in trials_5:
            currentLoop = trials_5
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
            if thisTrial_5 != None:
                for paramName in thisTrial_5:
                    globals()[paramName] = thisTrial_5[paramName]
            
            # --- Prepare to start Routine "record_Task_C2" ---
            # create an object to store info about Routine record_Task_C2
            record_Task_C2 = data.Routine(
                name='record_Task_C2',
                components=[text_C2, key_resp_C2],
            )
            record_Task_C2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            text_C2.setText(words)
            # create starting attributes for key_resp_C2
            key_resp_C2.keys = []
            key_resp_C2.rt = []
            _key_resp_C2_allKeys = []
            # store start times for record_Task_C2
            record_Task_C2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            record_Task_C2.tStart = globalClock.getTime(format='float')
            record_Task_C2.status = STARTED
            thisExp.addData('record_Task_C2.started', record_Task_C2.tStart)
            record_Task_C2.maxDuration = None
            # keep track of which components have finished
            record_Task_C2Components = record_Task_C2.components
            for thisComponent in record_Task_C2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "record_Task_C2" ---
            # if trial has changed, end Routine now
            if isinstance(trials_5, data.TrialHandler2) and thisTrial_5.thisN != trials_5.thisTrial.thisN:
                continueRoutine = False
            record_Task_C2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_C2* updates
                
                # if text_C2 is starting this frame...
                if text_C2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_C2.frameNStart = frameN  # exact frame index
                    text_C2.tStart = t  # local t and not account for scr refresh
                    text_C2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_C2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_C2.started')
                    # update status
                    text_C2.status = STARTED
                    text_C2.setAutoDraw(True)
                
                # if text_C2 is active this frame...
                if text_C2.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_C2* updates
                waitOnFlip = False
                
                # if key_resp_C2 is starting this frame...
                if key_resp_C2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_C2.frameNStart = frameN  # exact frame index
                    key_resp_C2.tStart = t  # local t and not account for scr refresh
                    key_resp_C2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_C2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_C2.started')
                    # update status
                    key_resp_C2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_C2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_C2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_C2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_C2.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_C2_allKeys.extend(theseKeys)
                    if len(_key_resp_C2_allKeys):
                        key_resp_C2.keys = _key_resp_C2_allKeys[-1].name  # just the last key pressed
                        key_resp_C2.rt = _key_resp_C2_allKeys[-1].rt
                        key_resp_C2.duration = _key_resp_C2_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_C2.keys == str(keypad)) or (key_resp_C2.keys == keypad):
                            key_resp_C2.corr = 1
                        else:
                            key_resp_C2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    record_Task_C2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in record_Task_C2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "record_Task_C2" ---
            for thisComponent in record_Task_C2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for record_Task_C2
            record_Task_C2.tStop = globalClock.getTime(format='float')
            record_Task_C2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('record_Task_C2.stopped', record_Task_C2.tStop)
            # check responses
            if key_resp_C2.keys in ['', [], None]:  # No response was made
                key_resp_C2.keys = None
                # was no response the correct answer?!
                if str(keypad).lower() == 'none':
                   key_resp_C2.corr = 1;  # correct non-response
                else:
                   key_resp_C2.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_5 (TrialHandler)
            trials_5.addData('key_resp_C2.keys',key_resp_C2.keys)
            trials_5.addData('key_resp_C2.corr', key_resp_C2.corr)
            if key_resp_C2.keys != None:  # we had a response
                trials_5.addData('key_resp_C2.rt', key_resp_C2.rt)
                trials_5.addData('key_resp_C2.duration', key_resp_C2.duration)
            # the Routine "record_Task_C2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback_C2" ---
            # create an object to store info about Routine feedback_C2
            feedback_C2 = data.Routine(
                name='feedback_C2',
                components=[feedback_text_C2],
            )
            feedback_C2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_C2
            key_resp_C2_rt_sum_temp = key_resp_C2_rt_sum_temp + float(str(key_resp_C2.rt))
            
            if key_resp_C2.corr:
                key_resp_C2_corr_sum_temp =key_resp_C2_corr_sum_temp +1
                continueRoutine = False
            else:
                msg = 'error'
            
            feedback_text_C2.setText(msg)
            # store start times for feedback_C2
            feedback_C2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback_C2.tStart = globalClock.getTime(format='float')
            feedback_C2.status = STARTED
            thisExp.addData('feedback_C2.started', feedback_C2.tStart)
            feedback_C2.maxDuration = None
            # keep track of which components have finished
            feedback_C2Components = feedback_C2.components
            for thisComponent in feedback_C2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback_C2" ---
            # if trial has changed, end Routine now
            if isinstance(trials_5, data.TrialHandler2) and thisTrial_5.thisN != trials_5.thisTrial.thisN:
                continueRoutine = False
            feedback_C2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text_C2* updates
                
                # if feedback_text_C2 is starting this frame...
                if feedback_text_C2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_C2.frameNStart = frameN  # exact frame index
                    feedback_text_C2.tStart = t  # local t and not account for scr refresh
                    feedback_text_C2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_C2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_C2.started')
                    # update status
                    feedback_text_C2.status = STARTED
                    feedback_text_C2.setAutoDraw(True)
                
                # if feedback_text_C2 is active this frame...
                if feedback_text_C2.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text_C2 is stopping this frame...
                if feedback_text_C2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text_C2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text_C2.tStop = t  # not accounting for scr refresh
                        feedback_text_C2.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_text_C2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text_C2.stopped')
                        # update status
                        feedback_text_C2.status = FINISHED
                        feedback_text_C2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback_C2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_C2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback_C2" ---
            for thisComponent in feedback_C2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback_C2
            feedback_C2.tStop = globalClock.getTime(format='float')
            feedback_C2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback_C2.stopped', feedback_C2.tStop)
            # Run 'End Routine' code from code_C2
            key_resp_C2_corr_sum = key_resp_C2_corr_sum_temp
            key_resp_C2_rt_sum = key_resp_C2_rt_sum_temp
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback_C2.maxDurationReached:
                routineTimer.addTime(-feedback_C2.maxDuration)
            elif feedback_C2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "ISI250" ---
            # create an object to store info about Routine ISI250
            ISI250 = data.Routine(
                name='ISI250',
                components=[],
            )
            ISI250.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for ISI250
            ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI250.tStart = globalClock.getTime(format='float')
            ISI250.status = STARTED
            thisExp.addData('ISI250.started', ISI250.tStart)
            ISI250.maxDuration = 0.25
            # keep track of which components have finished
            ISI250Components = ISI250.components
            for thisComponent in ISI250.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI250" ---
            # if trial has changed, end Routine now
            if isinstance(trials_5, data.TrialHandler2) and thisTrial_5.thisN != trials_5.thisTrial.thisN:
                continueRoutine = False
            ISI250.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > ISI250.maxDuration-frameTolerance:
                    ISI250.maxDurationReached = True
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI250.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI250.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI250" ---
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI250
            ISI250.tStop = globalClock.getTime(format='float')
            ISI250.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI250.stopped', ISI250.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if ISI250.maxDurationReached:
                routineTimer.addTime(-ISI250.maxDuration)
            elif ISI250.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_5'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "score_C2" ---
        # create an object to store info about Routine score_C2
        score_C2 = data.Routine(
            name='score_C2',
            components=[score_C2_text, key_resp_7],
        )
        score_C2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from score_C2_code
        feedback_msg ="" 
        
        accuracy = round((key_resp_C2_corr_sum / 50) * 100, 2)  
        rt_average = round((key_resp_C2_rt_sum / 50) * 1000, 2)  
        
        feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
        feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
        feedback_msg += "Press space bar to continue."
        # create starting attributes for key_resp_7
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        # store start times for score_C2
        score_C2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        score_C2.tStart = globalClock.getTime(format='float')
        score_C2.status = STARTED
        thisExp.addData('score_C2.started', score_C2.tStart)
        score_C2.maxDuration = None
        # keep track of which components have finished
        score_C2Components = score_C2.components
        for thisComponent in score_C2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "score_C2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        score_C2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *score_C2_text* updates
            
            # if score_C2_text is starting this frame...
            if score_C2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_C2_text.frameNStart = frameN  # exact frame index
                score_C2_text.tStart = t  # local t and not account for scr refresh
                score_C2_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_C2_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'score_C2_text.started')
                # update status
                score_C2_text.status = STARTED
                score_C2_text.setAutoDraw(True)
            
            # if score_C2_text is active this frame...
            if score_C2_text.status == STARTED:
                # update params
                score_C2_text.setText(feedback_msg, log=False)
            
            # *key_resp_7* updates
            waitOnFlip = False
            
            # if key_resp_7 is starting this frame...
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.started')
                # update status
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                score_C2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in score_C2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "score_C2" ---
        for thisComponent in score_C2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for score_C2
        score_C2.tStop = globalClock.getTime(format='float')
        score_C2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('score_C2.stopped', score_C2.tStop)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        trials_20.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials_20.addData('key_resp_7.rt', key_resp_7.rt)
            trials_20.addData('key_resp_7.duration', key_resp_7.duration)
        # the Routine "score_C2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "reminder_C3" ---
        # create an object to store info about Routine reminder_C3
        reminder_C3 = data.Routine(
            name='reminder_C3',
            components=[text_48, key_resp_28],
        )
        reminder_C3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_28
        key_resp_28.keys = []
        key_resp_28.rt = []
        _key_resp_28_allKeys = []
        # store start times for reminder_C3
        reminder_C3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reminder_C3.tStart = globalClock.getTime(format='float')
        reminder_C3.status = STARTED
        thisExp.addData('reminder_C3.started', reminder_C3.tStart)
        reminder_C3.maxDuration = None
        # keep track of which components have finished
        reminder_C3Components = reminder_C3.components
        for thisComponent in reminder_C3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reminder_C3" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        reminder_C3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_48* updates
            
            # if text_48 is starting this frame...
            if text_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_48.frameNStart = frameN  # exact frame index
                text_48.tStart = t  # local t and not account for scr refresh
                text_48.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_48, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_48.started')
                # update status
                text_48.status = STARTED
                text_48.setAutoDraw(True)
            
            # if text_48 is active this frame...
            if text_48.status == STARTED:
                # update params
                pass
            
            # *key_resp_28* updates
            waitOnFlip = False
            
            # if key_resp_28 is starting this frame...
            if key_resp_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_28.frameNStart = frameN  # exact frame index
                key_resp_28.tStart = t  # local t and not account for scr refresh
                key_resp_28.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_28, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_28.started')
                # update status
                key_resp_28.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_28.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_28.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_28.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_28.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_28_allKeys.extend(theseKeys)
                if len(_key_resp_28_allKeys):
                    key_resp_28.keys = _key_resp_28_allKeys[-1].name  # just the last key pressed
                    key_resp_28.rt = _key_resp_28_allKeys[-1].rt
                    key_resp_28.duration = _key_resp_28_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                reminder_C3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reminder_C3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reminder_C3" ---
        for thisComponent in reminder_C3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reminder_C3
        reminder_C3.tStop = globalClock.getTime(format='float')
        reminder_C3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reminder_C3.stopped', reminder_C3.tStop)
        # check responses
        if key_resp_28.keys in ['', [], None]:  # No response was made
            key_resp_28.keys = None
        trials_20.addData('key_resp_28.keys',key_resp_28.keys)
        if key_resp_28.keys != None:  # we had a response
            trials_20.addData('key_resp_28.rt', key_resp_28.rt)
            trials_20.addData('key_resp_28.duration', key_resp_28.duration)
        # the Routine "reminder_C3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ISI1500" ---
        # create an object to store info about Routine ISI1500
        ISI1500 = data.Routine(
            name='ISI1500',
            components=[text_3],
        )
        ISI1500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI1500
        ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI1500.tStart = globalClock.getTime(format='float')
        ISI1500.status = STARTED
        thisExp.addData('ISI1500.started', ISI1500.tStart)
        ISI1500.maxDuration = 1.5
        # keep track of which components have finished
        ISI1500Components = ISI1500.components
        for thisComponent in ISI1500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI1500" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        ISI1500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI1500.maxDuration-frameTolerance:
                ISI1500.maxDurationReached = True
                continueRoutine = False
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # if text_3 is stopping this frame...
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    # update status
                    text_3.status = FINISHED
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI1500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI1500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI1500" ---
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI1500
        ISI1500.tStop = globalClock.getTime(format='float')
        ISI1500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI1500.stopped', ISI1500.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI1500.maxDurationReached:
            routineTimer.addTime(-ISI1500.maxDuration)
        elif ISI1500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # set up handler to look after randomisation of conditions etc
        trials_6 = data.TrialHandler2(
            name='trials_6',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('excel/TaskC1_E2_block1st3rd_congruent_japan_prefer.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials_6)  # add the loop to the experiment
        thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
        if thisTrial_6 != None:
            for paramName in thisTrial_6:
                globals()[paramName] = thisTrial_6[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_6 in trials_6:
            currentLoop = trials_6
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
            if thisTrial_6 != None:
                for paramName in thisTrial_6:
                    globals()[paramName] = thisTrial_6[paramName]
            
            # --- Prepare to start Routine "record_Task_C3" ---
            # create an object to store info about Routine record_Task_C3
            record_Task_C3 = data.Routine(
                name='record_Task_C3',
                components=[text_C3, key_resp_C3],
            )
            record_Task_C3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            text_C3.setText(words)
            # create starting attributes for key_resp_C3
            key_resp_C3.keys = []
            key_resp_C3.rt = []
            _key_resp_C3_allKeys = []
            # store start times for record_Task_C3
            record_Task_C3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            record_Task_C3.tStart = globalClock.getTime(format='float')
            record_Task_C3.status = STARTED
            thisExp.addData('record_Task_C3.started', record_Task_C3.tStart)
            record_Task_C3.maxDuration = None
            # keep track of which components have finished
            record_Task_C3Components = record_Task_C3.components
            for thisComponent in record_Task_C3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "record_Task_C3" ---
            # if trial has changed, end Routine now
            if isinstance(trials_6, data.TrialHandler2) and thisTrial_6.thisN != trials_6.thisTrial.thisN:
                continueRoutine = False
            record_Task_C3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_C3* updates
                
                # if text_C3 is starting this frame...
                if text_C3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_C3.frameNStart = frameN  # exact frame index
                    text_C3.tStart = t  # local t and not account for scr refresh
                    text_C3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_C3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_C3.started')
                    # update status
                    text_C3.status = STARTED
                    text_C3.setAutoDraw(True)
                
                # if text_C3 is active this frame...
                if text_C3.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_C3* updates
                waitOnFlip = False
                
                # if key_resp_C3 is starting this frame...
                if key_resp_C3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_C3.frameNStart = frameN  # exact frame index
                    key_resp_C3.tStart = t  # local t and not account for scr refresh
                    key_resp_C3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_C3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_C3.started')
                    # update status
                    key_resp_C3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_C3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_C3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_C3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_C3.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_C3_allKeys.extend(theseKeys)
                    if len(_key_resp_C3_allKeys):
                        key_resp_C3.keys = _key_resp_C3_allKeys[-1].name  # just the last key pressed
                        key_resp_C3.rt = _key_resp_C3_allKeys[-1].rt
                        key_resp_C3.duration = _key_resp_C3_allKeys[-1].duration
                        # was this correct?
                        if (key_resp_C3.keys == str(keypad)) or (key_resp_C3.keys == keypad):
                            key_resp_C3.corr = 1
                        else:
                            key_resp_C3.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    record_Task_C3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in record_Task_C3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "record_Task_C3" ---
            for thisComponent in record_Task_C3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for record_Task_C3
            record_Task_C3.tStop = globalClock.getTime(format='float')
            record_Task_C3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('record_Task_C3.stopped', record_Task_C3.tStop)
            # check responses
            if key_resp_C3.keys in ['', [], None]:  # No response was made
                key_resp_C3.keys = None
                # was no response the correct answer?!
                if str(keypad).lower() == 'none':
                   key_resp_C3.corr = 1;  # correct non-response
                else:
                   key_resp_C3.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_6 (TrialHandler)
            trials_6.addData('key_resp_C3.keys',key_resp_C3.keys)
            trials_6.addData('key_resp_C3.corr', key_resp_C3.corr)
            if key_resp_C3.keys != None:  # we had a response
                trials_6.addData('key_resp_C3.rt', key_resp_C3.rt)
                trials_6.addData('key_resp_C3.duration', key_resp_C3.duration)
            # the Routine "record_Task_C3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback_C3" ---
            # create an object to store info about Routine feedback_C3
            feedback_C3 = data.Routine(
                name='feedback_C3',
                components=[feedback_text_C3],
            )
            feedback_C3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_C3
            key_resp_C3_rt_sum_temp = key_resp_C3_rt_sum_temp + float(str(key_resp_C3.rt))
            
            if key_resp_C3.corr:
                key_resp_C3_corr_sum_temp =key_resp_C3_corr_sum_temp +1
                continueRoutine = False
            else:
                msg = 'error'
            feedback_text_C3.setText(msg)
            # store start times for feedback_C3
            feedback_C3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback_C3.tStart = globalClock.getTime(format='float')
            feedback_C3.status = STARTED
            thisExp.addData('feedback_C3.started', feedback_C3.tStart)
            feedback_C3.maxDuration = None
            # keep track of which components have finished
            feedback_C3Components = feedback_C3.components
            for thisComponent in feedback_C3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback_C3" ---
            # if trial has changed, end Routine now
            if isinstance(trials_6, data.TrialHandler2) and thisTrial_6.thisN != trials_6.thisTrial.thisN:
                continueRoutine = False
            feedback_C3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text_C3* updates
                
                # if feedback_text_C3 is starting this frame...
                if feedback_text_C3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_C3.frameNStart = frameN  # exact frame index
                    feedback_text_C3.tStart = t  # local t and not account for scr refresh
                    feedback_text_C3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_C3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_C3.started')
                    # update status
                    feedback_text_C3.status = STARTED
                    feedback_text_C3.setAutoDraw(True)
                
                # if feedback_text_C3 is active this frame...
                if feedback_text_C3.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text_C3 is stopping this frame...
                if feedback_text_C3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text_C3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text_C3.tStop = t  # not accounting for scr refresh
                        feedback_text_C3.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_text_C3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text_C3.stopped')
                        # update status
                        feedback_text_C3.status = FINISHED
                        feedback_text_C3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback_C3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_C3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback_C3" ---
            for thisComponent in feedback_C3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback_C3
            feedback_C3.tStop = globalClock.getTime(format='float')
            feedback_C3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback_C3.stopped', feedback_C3.tStop)
            # Run 'End Routine' code from code_C3
            key_resp_C3_corr_sum = key_resp_C3_corr_sum_temp
            key_resp_C3_rt_sum = key_resp_C3_rt_sum_temp
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback_C3.maxDurationReached:
                routineTimer.addTime(-feedback_C3.maxDuration)
            elif feedback_C3.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "ISI250" ---
            # create an object to store info about Routine ISI250
            ISI250 = data.Routine(
                name='ISI250',
                components=[],
            )
            ISI250.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for ISI250
            ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI250.tStart = globalClock.getTime(format='float')
            ISI250.status = STARTED
            thisExp.addData('ISI250.started', ISI250.tStart)
            ISI250.maxDuration = 0.25
            # keep track of which components have finished
            ISI250Components = ISI250.components
            for thisComponent in ISI250.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI250" ---
            # if trial has changed, end Routine now
            if isinstance(trials_6, data.TrialHandler2) and thisTrial_6.thisN != trials_6.thisTrial.thisN:
                continueRoutine = False
            ISI250.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > ISI250.maxDuration-frameTolerance:
                    ISI250.maxDurationReached = True
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI250.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI250.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI250" ---
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI250
            ISI250.tStop = globalClock.getTime(format='float')
            ISI250.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI250.stopped', ISI250.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if ISI250.maxDurationReached:
                routineTimer.addTime(-ISI250.maxDuration)
            elif ISI250.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_6'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "score_C3" ---
        # create an object to store info about Routine score_C3
        score_C3 = data.Routine(
            name='score_C3',
            components=[score_C3_text, key_resp_8],
        )
        score_C3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from score_C3_code
        feedback_msg ="" 
        
        accuracy = round((key_resp_C3_corr_sum / 50) * 100, 2)  
        rt_average = round((key_resp_C3_rt_sum / 50) * 1000, 2)  
        
        feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
        feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
        feedback_msg += "Press space bar to continue."
        # create starting attributes for key_resp_8
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        # store start times for score_C3
        score_C3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        score_C3.tStart = globalClock.getTime(format='float')
        score_C3.status = STARTED
        thisExp.addData('score_C3.started', score_C3.tStart)
        score_C3.maxDuration = None
        # keep track of which components have finished
        score_C3Components = score_C3.components
        for thisComponent in score_C3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "score_C3" ---
        # if trial has changed, end Routine now
        if isinstance(trials_20, data.TrialHandler2) and thisTrial_20.thisN != trials_20.thisTrial.thisN:
            continueRoutine = False
        score_C3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *score_C3_text* updates
            
            # if score_C3_text is starting this frame...
            if score_C3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_C3_text.frameNStart = frameN  # exact frame index
                score_C3_text.tStart = t  # local t and not account for scr refresh
                score_C3_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_C3_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'score_C3_text.started')
                # update status
                score_C3_text.status = STARTED
                score_C3_text.setAutoDraw(True)
            
            # if score_C3_text is active this frame...
            if score_C3_text.status == STARTED:
                # update params
                score_C3_text.setText(feedback_msg, log=False)
            
            # if score_C3_text is stopping this frame...
            if score_C3_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > score_C3_text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    score_C3_text.tStop = t  # not accounting for scr refresh
                    score_C3_text.tStopRefresh = tThisFlipGlobal  # on global time
                    score_C3_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'score_C3_text.stopped')
                    # update status
                    score_C3_text.status = FINISHED
                    score_C3_text.setAutoDraw(False)
            
            # *key_resp_8* updates
            waitOnFlip = False
            
            # if key_resp_8 is starting this frame...
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_8.started')
                # update status
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                score_C3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in score_C3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "score_C3" ---
        for thisComponent in score_C3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for score_C3
        score_C3.tStop = globalClock.getTime(format='float')
        score_C3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('score_C3.stopped', score_C3.tStop)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
        trials_20.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            trials_20.addData('key_resp_8.rt', key_resp_8.rt)
            trials_20.addData('key_resp_8.duration', key_resp_8.duration)
        # the Routine "score_C3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 0.0 repeats of 'trials_20'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "reminder_D1" ---
    # create an object to store info about Routine reminder_D1
    reminder_D1 = data.Routine(
        name='reminder_D1',
        components=[text_49, key_resp_29],
    )
    reminder_D1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_29
    key_resp_29.keys = []
    key_resp_29.rt = []
    _key_resp_29_allKeys = []
    # store start times for reminder_D1
    reminder_D1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_D1.tStart = globalClock.getTime(format='float')
    reminder_D1.status = STARTED
    thisExp.addData('reminder_D1.started', reminder_D1.tStart)
    reminder_D1.maxDuration = None
    # keep track of which components have finished
    reminder_D1Components = reminder_D1.components
    for thisComponent in reminder_D1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_D1" ---
    reminder_D1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_49* updates
        
        # if text_49 is starting this frame...
        if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_49.frameNStart = frameN  # exact frame index
            text_49.tStart = t  # local t and not account for scr refresh
            text_49.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_49.started')
            # update status
            text_49.status = STARTED
            text_49.setAutoDraw(True)
        
        # if text_49 is active this frame...
        if text_49.status == STARTED:
            # update params
            pass
        
        # *key_resp_29* updates
        waitOnFlip = False
        
        # if key_resp_29 is starting this frame...
        if key_resp_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_29.frameNStart = frameN  # exact frame index
            key_resp_29.tStart = t  # local t and not account for scr refresh
            key_resp_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_29.started')
            # update status
            key_resp_29.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_29.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_29.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_29.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_29.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_29_allKeys.extend(theseKeys)
            if len(_key_resp_29_allKeys):
                key_resp_29.keys = _key_resp_29_allKeys[-1].name  # just the last key pressed
                key_resp_29.rt = _key_resp_29_allKeys[-1].rt
                key_resp_29.duration = _key_resp_29_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_D1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_D1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_D1" ---
    for thisComponent in reminder_D1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_D1
    reminder_D1.tStop = globalClock.getTime(format='float')
    reminder_D1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_D1.stopped', reminder_D1.tStop)
    # check responses
    if key_resp_29.keys in ['', [], None]:  # No response was made
        key_resp_29.keys = None
    thisExp.addData('key_resp_29.keys',key_resp_29.keys)
    if key_resp_29.keys != None:  # we had a response
        thisExp.addData('key_resp_29.rt', key_resp_29.rt)
        thisExp.addData('key_resp_29.duration', key_resp_29.duration)
    thisExp.nextEntry()
    # the Routine "reminder_D1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_8 = data.TrialHandler2(
        name='trials_8',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskA2_D1_right_korean.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_8)  # add the loop to the experiment
    thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            globals()[paramName] = thisTrial_8[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_8 in trials_8:
        currentLoop = trials_8
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
        if thisTrial_8 != None:
            for paramName in thisTrial_8:
                globals()[paramName] = thisTrial_8[paramName]
        
        # --- Prepare to start Routine "record_Task_D1" ---
        # create an object to store info about Routine record_Task_D1
        record_Task_D1 = data.Routine(
            name='record_Task_D1',
            components=[text_D1, key_resp_D1],
        )
        record_Task_D1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_D1.setText(name)
        # create starting attributes for key_resp_D1
        key_resp_D1.keys = []
        key_resp_D1.rt = []
        _key_resp_D1_allKeys = []
        # store start times for record_Task_D1
        record_Task_D1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        record_Task_D1.tStart = globalClock.getTime(format='float')
        record_Task_D1.status = STARTED
        thisExp.addData('record_Task_D1.started', record_Task_D1.tStart)
        record_Task_D1.maxDuration = None
        # keep track of which components have finished
        record_Task_D1Components = record_Task_D1.components
        for thisComponent in record_Task_D1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "record_Task_D1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_8, data.TrialHandler2) and thisTrial_8.thisN != trials_8.thisTrial.thisN:
            continueRoutine = False
        record_Task_D1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_D1* updates
            
            # if text_D1 is starting this frame...
            if text_D1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_D1.frameNStart = frameN  # exact frame index
                text_D1.tStart = t  # local t and not account for scr refresh
                text_D1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_D1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_D1.started')
                # update status
                text_D1.status = STARTED
                text_D1.setAutoDraw(True)
            
            # if text_D1 is active this frame...
            if text_D1.status == STARTED:
                # update params
                pass
            
            # *key_resp_D1* updates
            waitOnFlip = False
            
            # if key_resp_D1 is starting this frame...
            if key_resp_D1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_D1.frameNStart = frameN  # exact frame index
                key_resp_D1.tStart = t  # local t and not account for scr refresh
                key_resp_D1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_D1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_D1.started')
                # update status
                key_resp_D1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_D1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_D1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_D1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_D1.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_D1_allKeys.extend(theseKeys)
                if len(_key_resp_D1_allKeys):
                    key_resp_D1.keys = _key_resp_D1_allKeys[-1].name  # just the last key pressed
                    key_resp_D1.rt = _key_resp_D1_allKeys[-1].rt
                    key_resp_D1.duration = _key_resp_D1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_D1.keys == str(keypad)) or (key_resp_D1.keys == keypad):
                        key_resp_D1.corr = 1
                    else:
                        key_resp_D1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                record_Task_D1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_Task_D1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "record_Task_D1" ---
        for thisComponent in record_Task_D1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for record_Task_D1
        record_Task_D1.tStop = globalClock.getTime(format='float')
        record_Task_D1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('record_Task_D1.stopped', record_Task_D1.tStop)
        # check responses
        if key_resp_D1.keys in ['', [], None]:  # No response was made
            key_resp_D1.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_D1.corr = 1;  # correct non-response
            else:
               key_resp_D1.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_8 (TrialHandler)
        trials_8.addData('key_resp_D1.keys',key_resp_D1.keys)
        trials_8.addData('key_resp_D1.corr', key_resp_D1.corr)
        if key_resp_D1.keys != None:  # we had a response
            trials_8.addData('key_resp_D1.rt', key_resp_D1.rt)
            trials_8.addData('key_resp_D1.duration', key_resp_D1.duration)
        # the Routine "record_Task_D1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_D1" ---
        # create an object to store info about Routine feedback_D1
        feedback_D1 = data.Routine(
            name='feedback_D1',
            components=[feedback_text_D1],
        )
        feedback_D1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_D1
        key_resp_D1_rt_sum_temp = key_resp_D1_rt_sum_temp + float(str(key_resp_D1.rt))
        
        if key_resp_D1.corr:
            key_resp_D1_corr_sum_temp =key_resp_D1_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_D1.setText(msg)
        # store start times for feedback_D1
        feedback_D1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_D1.tStart = globalClock.getTime(format='float')
        feedback_D1.status = STARTED
        thisExp.addData('feedback_D1.started', feedback_D1.tStart)
        feedback_D1.maxDuration = None
        # keep track of which components have finished
        feedback_D1Components = feedback_D1.components
        for thisComponent in feedback_D1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_D1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_8, data.TrialHandler2) and thisTrial_8.thisN != trials_8.thisTrial.thisN:
            continueRoutine = False
        feedback_D1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_D1* updates
            
            # if feedback_text_D1 is starting this frame...
            if feedback_text_D1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_D1.frameNStart = frameN  # exact frame index
                feedback_text_D1.tStart = t  # local t and not account for scr refresh
                feedback_text_D1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_D1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_D1.started')
                # update status
                feedback_text_D1.status = STARTED
                feedback_text_D1.setAutoDraw(True)
            
            # if feedback_text_D1 is active this frame...
            if feedback_text_D1.status == STARTED:
                # update params
                pass
            
            # if feedback_text_D1 is stopping this frame...
            if feedback_text_D1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_D1.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_D1.tStop = t  # not accounting for scr refresh
                    feedback_text_D1.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_D1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_D1.stopped')
                    # update status
                    feedback_text_D1.status = FINISHED
                    feedback_text_D1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_D1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_D1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_D1" ---
        for thisComponent in feedback_D1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_D1
        feedback_D1.tStop = globalClock.getTime(format='float')
        feedback_D1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_D1.stopped', feedback_D1.tStop)
        # Run 'End Routine' code from code_D1
        key_resp_D1_corr_sum = key_resp_D1_corr_sum_temp
        key_resp_D1_rt_sum = key_resp_D1_rt_sum_temp
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_D1.maxDurationReached:
            routineTimer.addTime(-feedback_D1.maxDuration)
        elif feedback_D1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_8, data.TrialHandler2) and thisTrial_8.thisN != trials_8.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_8'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_D1" ---
    # create an object to store info about Routine score_D1
    score_D1 = data.Routine(
        name='score_D1',
        components=[score_D1_text, key_resp_9],
    )
    score_D1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_D1_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_D1_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_D1_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_9
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # store start times for score_D1
    score_D1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_D1.tStart = globalClock.getTime(format='float')
    score_D1.status = STARTED
    thisExp.addData('score_D1.started', score_D1.tStart)
    score_D1.maxDuration = None
    # keep track of which components have finished
    score_D1Components = score_D1.components
    for thisComponent in score_D1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_D1" ---
    score_D1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_D1_text* updates
        
        # if score_D1_text is starting this frame...
        if score_D1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_D1_text.frameNStart = frameN  # exact frame index
            score_D1_text.tStart = t  # local t and not account for scr refresh
            score_D1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_D1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_D1_text.started')
            # update status
            score_D1_text.status = STARTED
            score_D1_text.setAutoDraw(True)
        
        # if score_D1_text is active this frame...
        if score_D1_text.status == STARTED:
            # update params
            score_D1_text.setText(feedback_msg, log=False)
        
        # *key_resp_9* updates
        waitOnFlip = False
        
        # if key_resp_9 is starting this frame...
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            # update status
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_D1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_D1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_D1" ---
    for thisComponent in score_D1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_D1
    score_D1.tStop = globalClock.getTime(format='float')
    score_D1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_D1.stopped', score_D1.tStop)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    thisExp.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        thisExp.addData('key_resp_9.rt', key_resp_9.rt)
        thisExp.addData('key_resp_9.duration', key_resp_9.duration)
    thisExp.nextEntry()
    # the Routine "score_D1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_E1" ---
    # create an object to store info about Routine reminder_E1
    reminder_E1 = data.Routine(
        name='reminder_E1',
        components=[text_50, key_resp_30],
    )
    reminder_E1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_30
    key_resp_30.keys = []
    key_resp_30.rt = []
    _key_resp_30_allKeys = []
    # store start times for reminder_E1
    reminder_E1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_E1.tStart = globalClock.getTime(format='float')
    reminder_E1.status = STARTED
    thisExp.addData('reminder_E1.started', reminder_E1.tStart)
    reminder_E1.maxDuration = None
    # keep track of which components have finished
    reminder_E1Components = reminder_E1.components
    for thisComponent in reminder_E1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_E1" ---
    reminder_E1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_50* updates
        
        # if text_50 is starting this frame...
        if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_50.frameNStart = frameN  # exact frame index
            text_50.tStart = t  # local t and not account for scr refresh
            text_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_50.started')
            # update status
            text_50.status = STARTED
            text_50.setAutoDraw(True)
        
        # if text_50 is active this frame...
        if text_50.status == STARTED:
            # update params
            pass
        
        # *key_resp_30* updates
        waitOnFlip = False
        
        # if key_resp_30 is starting this frame...
        if key_resp_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_30.frameNStart = frameN  # exact frame index
            key_resp_30.tStart = t  # local t and not account for scr refresh
            key_resp_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_30.started')
            # update status
            key_resp_30.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_30.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_30.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_30.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_30.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_30_allKeys.extend(theseKeys)
            if len(_key_resp_30_allKeys):
                key_resp_30.keys = _key_resp_30_allKeys[-1].name  # just the last key pressed
                key_resp_30.rt = _key_resp_30_allKeys[-1].rt
                key_resp_30.duration = _key_resp_30_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_E1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_E1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_E1" ---
    for thisComponent in reminder_E1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_E1
    reminder_E1.tStop = globalClock.getTime(format='float')
    reminder_E1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_E1.stopped', reminder_E1.tStop)
    # check responses
    if key_resp_30.keys in ['', [], None]:  # No response was made
        key_resp_30.keys = None
    thisExp.addData('key_resp_30.keys',key_resp_30.keys)
    if key_resp_30.keys != None:  # we had a response
        thisExp.addData('key_resp_30.rt', key_resp_30.rt)
        thisExp.addData('key_resp_30.duration', key_resp_30.duration)
    thisExp.nextEntry()
    # the Routine "reminder_E1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_9 = data.TrialHandler2(
        name='trials_9',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskC2_E1_block1st3rd_congruent_korean_prefer.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_9)  # add the loop to the experiment
    thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            globals()[paramName] = thisTrial_9[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_9 in trials_9:
        currentLoop = trials_9
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
        if thisTrial_9 != None:
            for paramName in thisTrial_9:
                globals()[paramName] = thisTrial_9[paramName]
        
        # --- Prepare to start Routine "practice_Task_E1" ---
        # create an object to store info about Routine practice_Task_E1
        practice_Task_E1 = data.Routine(
            name='practice_Task_E1',
            components=[text_E1, key_resp_E1],
        )
        practice_Task_E1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_E1.setText(words)
        # create starting attributes for key_resp_E1
        key_resp_E1.keys = []
        key_resp_E1.rt = []
        _key_resp_E1_allKeys = []
        # store start times for practice_Task_E1
        practice_Task_E1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_Task_E1.tStart = globalClock.getTime(format='float')
        practice_Task_E1.status = STARTED
        thisExp.addData('practice_Task_E1.started', practice_Task_E1.tStart)
        practice_Task_E1.maxDuration = None
        # keep track of which components have finished
        practice_Task_E1Components = practice_Task_E1.components
        for thisComponent in practice_Task_E1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_Task_E1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_9, data.TrialHandler2) and thisTrial_9.thisN != trials_9.thisTrial.thisN:
            continueRoutine = False
        practice_Task_E1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_E1* updates
            
            # if text_E1 is starting this frame...
            if text_E1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_E1.frameNStart = frameN  # exact frame index
                text_E1.tStart = t  # local t and not account for scr refresh
                text_E1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_E1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_E1.started')
                # update status
                text_E1.status = STARTED
                text_E1.setAutoDraw(True)
            
            # if text_E1 is active this frame...
            if text_E1.status == STARTED:
                # update params
                pass
            
            # *key_resp_E1* updates
            waitOnFlip = False
            
            # if key_resp_E1 is starting this frame...
            if key_resp_E1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_E1.frameNStart = frameN  # exact frame index
                key_resp_E1.tStart = t  # local t and not account for scr refresh
                key_resp_E1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_E1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_E1.started')
                # update status
                key_resp_E1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_E1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_E1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_E1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_E1.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_E1_allKeys.extend(theseKeys)
                if len(_key_resp_E1_allKeys):
                    key_resp_E1.keys = _key_resp_E1_allKeys[-1].name  # just the last key pressed
                    key_resp_E1.rt = _key_resp_E1_allKeys[-1].rt
                    key_resp_E1.duration = _key_resp_E1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_E1.keys == str(keypad)) or (key_resp_E1.keys == keypad):
                        key_resp_E1.corr = 1
                    else:
                        key_resp_E1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practice_Task_E1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_Task_E1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_Task_E1" ---
        for thisComponent in practice_Task_E1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_Task_E1
        practice_Task_E1.tStop = globalClock.getTime(format='float')
        practice_Task_E1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_Task_E1.stopped', practice_Task_E1.tStop)
        # check responses
        if key_resp_E1.keys in ['', [], None]:  # No response was made
            key_resp_E1.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_E1.corr = 1;  # correct non-response
            else:
               key_resp_E1.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_9 (TrialHandler)
        trials_9.addData('key_resp_E1.keys',key_resp_E1.keys)
        trials_9.addData('key_resp_E1.corr', key_resp_E1.corr)
        if key_resp_E1.keys != None:  # we had a response
            trials_9.addData('key_resp_E1.rt', key_resp_E1.rt)
            trials_9.addData('key_resp_E1.duration', key_resp_E1.duration)
        # the Routine "practice_Task_E1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_E1" ---
        # create an object to store info about Routine feedback_E1
        feedback_E1 = data.Routine(
            name='feedback_E1',
            components=[feedback_text_E1],
        )
        feedback_E1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_E1
        key_resp_E1_rt_sum_temp = key_resp_E1_rt_sum_temp + float(str(key_resp_E1.rt))
        
        if key_resp_E1.corr:
            key_resp_E1_corr_sum_temp =key_resp_E1_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        
        feedback_text_E1.setText(msg)
        # store start times for feedback_E1
        feedback_E1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_E1.tStart = globalClock.getTime(format='float')
        feedback_E1.status = STARTED
        thisExp.addData('feedback_E1.started', feedback_E1.tStart)
        feedback_E1.maxDuration = None
        # keep track of which components have finished
        feedback_E1Components = feedback_E1.components
        for thisComponent in feedback_E1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_E1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_9, data.TrialHandler2) and thisTrial_9.thisN != trials_9.thisTrial.thisN:
            continueRoutine = False
        feedback_E1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_E1* updates
            
            # if feedback_text_E1 is starting this frame...
            if feedback_text_E1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_E1.frameNStart = frameN  # exact frame index
                feedback_text_E1.tStart = t  # local t and not account for scr refresh
                feedback_text_E1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_E1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_E1.started')
                # update status
                feedback_text_E1.status = STARTED
                feedback_text_E1.setAutoDraw(True)
            
            # if feedback_text_E1 is active this frame...
            if feedback_text_E1.status == STARTED:
                # update params
                pass
            
            # if feedback_text_E1 is stopping this frame...
            if feedback_text_E1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_E1.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_E1.tStop = t  # not accounting for scr refresh
                    feedback_text_E1.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_E1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_E1.stopped')
                    # update status
                    feedback_text_E1.status = FINISHED
                    feedback_text_E1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_E1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_E1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_E1" ---
        for thisComponent in feedback_E1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_E1
        feedback_E1.tStop = globalClock.getTime(format='float')
        feedback_E1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_E1.stopped', feedback_E1.tStop)
        # Run 'End Routine' code from code_E1
        key_resp_E1_corr_sum = key_resp_E1_corr_sum_temp
        key_resp_E1_rt_sum = key_resp_E1_rt_sum_temp
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_E1.maxDurationReached:
            routineTimer.addTime(-feedback_E1.maxDuration)
        elif feedback_E1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_9, data.TrialHandler2) and thisTrial_9.thisN != trials_9.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_9'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_E1" ---
    # create an object to store info about Routine score_E1
    score_E1 = data.Routine(
        name='score_E1',
        components=[score_E1_text, key_resp_10],
    )
    score_E1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_E1_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_E1_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_E1_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_10
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # store start times for score_E1
    score_E1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_E1.tStart = globalClock.getTime(format='float')
    score_E1.status = STARTED
    thisExp.addData('score_E1.started', score_E1.tStart)
    score_E1.maxDuration = None
    # keep track of which components have finished
    score_E1Components = score_E1.components
    for thisComponent in score_E1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_E1" ---
    score_E1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_E1_text* updates
        
        # if score_E1_text is starting this frame...
        if score_E1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_E1_text.frameNStart = frameN  # exact frame index
            score_E1_text.tStart = t  # local t and not account for scr refresh
            score_E1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_E1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_E1_text.started')
            # update status
            score_E1_text.status = STARTED
            score_E1_text.setAutoDraw(True)
        
        # if score_E1_text is active this frame...
        if score_E1_text.status == STARTED:
            # update params
            score_E1_text.setText(feedback_msg, log=False)
        
        # *key_resp_10* updates
        waitOnFlip = False
        
        # if key_resp_10 is starting this frame...
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_10.started')
            # update status
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                key_resp_10.duration = _key_resp_10_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_E1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_E1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_E1" ---
    for thisComponent in score_E1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_E1
    score_E1.tStop = globalClock.getTime(format='float')
    score_E1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_E1.stopped', score_E1.tStop)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    thisExp.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        thisExp.addData('key_resp_10.rt', key_resp_10.rt)
        thisExp.addData('key_resp_10.duration', key_resp_10.duration)
    thisExp.nextEntry()
    # the Routine "score_E1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_E2" ---
    # create an object to store info about Routine reminder_E2
    reminder_E2 = data.Routine(
        name='reminder_E2',
        components=[text_51, key_resp_31],
    )
    reminder_E2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_31
    key_resp_31.keys = []
    key_resp_31.rt = []
    _key_resp_31_allKeys = []
    # store start times for reminder_E2
    reminder_E2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_E2.tStart = globalClock.getTime(format='float')
    reminder_E2.status = STARTED
    thisExp.addData('reminder_E2.started', reminder_E2.tStart)
    reminder_E2.maxDuration = None
    # keep track of which components have finished
    reminder_E2Components = reminder_E2.components
    for thisComponent in reminder_E2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_E2" ---
    reminder_E2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_51* updates
        
        # if text_51 is starting this frame...
        if text_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_51.frameNStart = frameN  # exact frame index
            text_51.tStart = t  # local t and not account for scr refresh
            text_51.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_51, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_51.started')
            # update status
            text_51.status = STARTED
            text_51.setAutoDraw(True)
        
        # if text_51 is active this frame...
        if text_51.status == STARTED:
            # update params
            pass
        
        # *key_resp_31* updates
        waitOnFlip = False
        
        # if key_resp_31 is starting this frame...
        if key_resp_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_31.frameNStart = frameN  # exact frame index
            key_resp_31.tStart = t  # local t and not account for scr refresh
            key_resp_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_31, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_31.started')
            # update status
            key_resp_31.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_31.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_31.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_31.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_31.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_31_allKeys.extend(theseKeys)
            if len(_key_resp_31_allKeys):
                key_resp_31.keys = _key_resp_31_allKeys[-1].name  # just the last key pressed
                key_resp_31.rt = _key_resp_31_allKeys[-1].rt
                key_resp_31.duration = _key_resp_31_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_E2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_E2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_E2" ---
    for thisComponent in reminder_E2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_E2
    reminder_E2.tStop = globalClock.getTime(format='float')
    reminder_E2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_E2.stopped', reminder_E2.tStop)
    # check responses
    if key_resp_31.keys in ['', [], None]:  # No response was made
        key_resp_31.keys = None
    thisExp.addData('key_resp_31.keys',key_resp_31.keys)
    if key_resp_31.keys != None:  # we had a response
        thisExp.addData('key_resp_31.rt', key_resp_31.rt)
        thisExp.addData('key_resp_31.duration', key_resp_31.duration)
    thisExp.nextEntry()
    # the Routine "reminder_E2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_10 = data.TrialHandler2(
        name='trials_10',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskC2_E1_block2nd_congruent_korean_prefer.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_10)  # add the loop to the experiment
    thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
    if thisTrial_10 != None:
        for paramName in thisTrial_10:
            globals()[paramName] = thisTrial_10[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_10 in trials_10:
        currentLoop = trials_10
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
        if thisTrial_10 != None:
            for paramName in thisTrial_10:
                globals()[paramName] = thisTrial_10[paramName]
        
        # --- Prepare to start Routine "record_Task_E2" ---
        # create an object to store info about Routine record_Task_E2
        record_Task_E2 = data.Routine(
            name='record_Task_E2',
            components=[text_E2, key_resp_E2],
        )
        record_Task_E2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_E2.setText(words)
        # create starting attributes for key_resp_E2
        key_resp_E2.keys = []
        key_resp_E2.rt = []
        _key_resp_E2_allKeys = []
        # store start times for record_Task_E2
        record_Task_E2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        record_Task_E2.tStart = globalClock.getTime(format='float')
        record_Task_E2.status = STARTED
        thisExp.addData('record_Task_E2.started', record_Task_E2.tStart)
        record_Task_E2.maxDuration = None
        # keep track of which components have finished
        record_Task_E2Components = record_Task_E2.components
        for thisComponent in record_Task_E2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "record_Task_E2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_10, data.TrialHandler2) and thisTrial_10.thisN != trials_10.thisTrial.thisN:
            continueRoutine = False
        record_Task_E2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_E2* updates
            
            # if text_E2 is starting this frame...
            if text_E2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_E2.frameNStart = frameN  # exact frame index
                text_E2.tStart = t  # local t and not account for scr refresh
                text_E2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_E2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_E2.started')
                # update status
                text_E2.status = STARTED
                text_E2.setAutoDraw(True)
            
            # if text_E2 is active this frame...
            if text_E2.status == STARTED:
                # update params
                pass
            
            # *key_resp_E2* updates
            waitOnFlip = False
            
            # if key_resp_E2 is starting this frame...
            if key_resp_E2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_E2.frameNStart = frameN  # exact frame index
                key_resp_E2.tStart = t  # local t and not account for scr refresh
                key_resp_E2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_E2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_E2.started')
                # update status
                key_resp_E2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_E2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_E2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_E2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_E2.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_E2_allKeys.extend(theseKeys)
                if len(_key_resp_E2_allKeys):
                    key_resp_E2.keys = _key_resp_E2_allKeys[-1].name  # just the last key pressed
                    key_resp_E2.rt = _key_resp_E2_allKeys[-1].rt
                    key_resp_E2.duration = _key_resp_E2_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_E2.keys == str(keypad)) or (key_resp_E2.keys == keypad):
                        key_resp_E2.corr = 1
                    else:
                        key_resp_E2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                record_Task_E2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_Task_E2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "record_Task_E2" ---
        for thisComponent in record_Task_E2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for record_Task_E2
        record_Task_E2.tStop = globalClock.getTime(format='float')
        record_Task_E2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('record_Task_E2.stopped', record_Task_E2.tStop)
        # check responses
        if key_resp_E2.keys in ['', [], None]:  # No response was made
            key_resp_E2.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_E2.corr = 1;  # correct non-response
            else:
               key_resp_E2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_10 (TrialHandler)
        trials_10.addData('key_resp_E2.keys',key_resp_E2.keys)
        trials_10.addData('key_resp_E2.corr', key_resp_E2.corr)
        if key_resp_E2.keys != None:  # we had a response
            trials_10.addData('key_resp_E2.rt', key_resp_E2.rt)
            trials_10.addData('key_resp_E2.duration', key_resp_E2.duration)
        # the Routine "record_Task_E2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_E2" ---
        # create an object to store info about Routine feedback_E2
        feedback_E2 = data.Routine(
            name='feedback_E2',
            components=[feedback_text_E2],
        )
        feedback_E2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_E2
        key_resp_E2_rt_sum_temp = key_resp_E2_rt_sum_temp + float(str(key_resp_E2.rt))
        
        if key_resp_E2.corr:
            key_resp_E2_corr_sum_temp =key_resp_E2_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_E2.setText(msg)
        # store start times for feedback_E2
        feedback_E2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_E2.tStart = globalClock.getTime(format='float')
        feedback_E2.status = STARTED
        thisExp.addData('feedback_E2.started', feedback_E2.tStart)
        feedback_E2.maxDuration = None
        # keep track of which components have finished
        feedback_E2Components = feedback_E2.components
        for thisComponent in feedback_E2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_E2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_10, data.TrialHandler2) and thisTrial_10.thisN != trials_10.thisTrial.thisN:
            continueRoutine = False
        feedback_E2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_E2* updates
            
            # if feedback_text_E2 is starting this frame...
            if feedback_text_E2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_E2.frameNStart = frameN  # exact frame index
                feedback_text_E2.tStart = t  # local t and not account for scr refresh
                feedback_text_E2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_E2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_E2.started')
                # update status
                feedback_text_E2.status = STARTED
                feedback_text_E2.setAutoDraw(True)
            
            # if feedback_text_E2 is active this frame...
            if feedback_text_E2.status == STARTED:
                # update params
                pass
            
            # if feedback_text_E2 is stopping this frame...
            if feedback_text_E2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_E2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_E2.tStop = t  # not accounting for scr refresh
                    feedback_text_E2.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_E2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_E2.stopped')
                    # update status
                    feedback_text_E2.status = FINISHED
                    feedback_text_E2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_E2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_E2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_E2" ---
        for thisComponent in feedback_E2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_E2
        feedback_E2.tStop = globalClock.getTime(format='float')
        feedback_E2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_E2.stopped', feedback_E2.tStop)
        # Run 'End Routine' code from code_E2
        key_resp_E2_corr_sum = key_resp_E2_corr_sum_temp
        key_resp_E2_rt_sum = key_resp_E2_rt_sum_temp
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_E2.maxDurationReached:
            routineTimer.addTime(-feedback_E2.maxDuration)
        elif feedback_E2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_10, data.TrialHandler2) and thisTrial_10.thisN != trials_10.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_10'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_E2" ---
    # create an object to store info about Routine score_E2
    score_E2 = data.Routine(
        name='score_E2',
        components=[score_E2_text, key_resp_11],
    )
    score_E2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_E2_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_E2_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_E2_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_11
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # store start times for score_E2
    score_E2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_E2.tStart = globalClock.getTime(format='float')
    score_E2.status = STARTED
    thisExp.addData('score_E2.started', score_E2.tStart)
    score_E2.maxDuration = None
    # keep track of which components have finished
    score_E2Components = score_E2.components
    for thisComponent in score_E2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_E2" ---
    score_E2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_E2_text* updates
        
        # if score_E2_text is starting this frame...
        if score_E2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_E2_text.frameNStart = frameN  # exact frame index
            score_E2_text.tStart = t  # local t and not account for scr refresh
            score_E2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_E2_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_E2_text.started')
            # update status
            score_E2_text.status = STARTED
            score_E2_text.setAutoDraw(True)
        
        # if score_E2_text is active this frame...
        if score_E2_text.status == STARTED:
            # update params
            score_E2_text.setText(feedback_msg, log=False)
        
        # *key_resp_11* updates
        waitOnFlip = False
        
        # if key_resp_11 is starting this frame...
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_11.started')
            # update status
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_E2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_E2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_E2" ---
    for thisComponent in score_E2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_E2
    score_E2.tStop = globalClock.getTime(format='float')
    score_E2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_E2.stopped', score_E2.tStop)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    thisExp.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        thisExp.addData('key_resp_11.rt', key_resp_11.rt)
        thisExp.addData('key_resp_11.duration', key_resp_11.duration)
    thisExp.nextEntry()
    # the Routine "score_E2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_E3" ---
    # create an object to store info about Routine reminder_E3
    reminder_E3 = data.Routine(
        name='reminder_E3',
        components=[text_52, key_resp_40],
    )
    reminder_E3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_40
    key_resp_40.keys = []
    key_resp_40.rt = []
    _key_resp_40_allKeys = []
    # store start times for reminder_E3
    reminder_E3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_E3.tStart = globalClock.getTime(format='float')
    reminder_E3.status = STARTED
    thisExp.addData('reminder_E3.started', reminder_E3.tStart)
    reminder_E3.maxDuration = None
    # keep track of which components have finished
    reminder_E3Components = reminder_E3.components
    for thisComponent in reminder_E3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_E3" ---
    reminder_E3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_52* updates
        
        # if text_52 is starting this frame...
        if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_52.frameNStart = frameN  # exact frame index
            text_52.tStart = t  # local t and not account for scr refresh
            text_52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_52.started')
            # update status
            text_52.status = STARTED
            text_52.setAutoDraw(True)
        
        # if text_52 is active this frame...
        if text_52.status == STARTED:
            # update params
            pass
        
        # *key_resp_40* updates
        waitOnFlip = False
        
        # if key_resp_40 is starting this frame...
        if key_resp_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_40.frameNStart = frameN  # exact frame index
            key_resp_40.tStart = t  # local t and not account for scr refresh
            key_resp_40.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_40, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_40.started')
            # update status
            key_resp_40.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_40.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_40.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_40.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_40.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_40_allKeys.extend(theseKeys)
            if len(_key_resp_40_allKeys):
                key_resp_40.keys = _key_resp_40_allKeys[-1].name  # just the last key pressed
                key_resp_40.rt = _key_resp_40_allKeys[-1].rt
                key_resp_40.duration = _key_resp_40_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_E3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_E3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_E3" ---
    for thisComponent in reminder_E3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_E3
    reminder_E3.tStop = globalClock.getTime(format='float')
    reminder_E3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_E3.stopped', reminder_E3.tStop)
    # check responses
    if key_resp_40.keys in ['', [], None]:  # No response was made
        key_resp_40.keys = None
    thisExp.addData('key_resp_40.keys',key_resp_40.keys)
    if key_resp_40.keys != None:  # we had a response
        thisExp.addData('key_resp_40.rt', key_resp_40.rt)
        thisExp.addData('key_resp_40.duration', key_resp_40.duration)
    thisExp.nextEntry()
    # the Routine "reminder_E3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_11 = data.TrialHandler2(
        name='trials_11',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskC2_E1_block1st3rd_congruent_korean_prefer.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_11)  # add the loop to the experiment
    thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
    if thisTrial_11 != None:
        for paramName in thisTrial_11:
            globals()[paramName] = thisTrial_11[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_11 in trials_11:
        currentLoop = trials_11
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
        if thisTrial_11 != None:
            for paramName in thisTrial_11:
                globals()[paramName] = thisTrial_11[paramName]
        
        # --- Prepare to start Routine "record_Task_E3" ---
        # create an object to store info about Routine record_Task_E3
        record_Task_E3 = data.Routine(
            name='record_Task_E3',
            components=[text_E3, key_resp_E3],
        )
        record_Task_E3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_E3.setText(words)
        # create starting attributes for key_resp_E3
        key_resp_E3.keys = []
        key_resp_E3.rt = []
        _key_resp_E3_allKeys = []
        # store start times for record_Task_E3
        record_Task_E3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        record_Task_E3.tStart = globalClock.getTime(format='float')
        record_Task_E3.status = STARTED
        thisExp.addData('record_Task_E3.started', record_Task_E3.tStart)
        record_Task_E3.maxDuration = None
        # keep track of which components have finished
        record_Task_E3Components = record_Task_E3.components
        for thisComponent in record_Task_E3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "record_Task_E3" ---
        # if trial has changed, end Routine now
        if isinstance(trials_11, data.TrialHandler2) and thisTrial_11.thisN != trials_11.thisTrial.thisN:
            continueRoutine = False
        record_Task_E3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_E3* updates
            
            # if text_E3 is starting this frame...
            if text_E3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_E3.frameNStart = frameN  # exact frame index
                text_E3.tStart = t  # local t and not account for scr refresh
                text_E3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_E3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_E3.started')
                # update status
                text_E3.status = STARTED
                text_E3.setAutoDraw(True)
            
            # if text_E3 is active this frame...
            if text_E3.status == STARTED:
                # update params
                pass
            
            # *key_resp_E3* updates
            waitOnFlip = False
            
            # if key_resp_E3 is starting this frame...
            if key_resp_E3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_E3.frameNStart = frameN  # exact frame index
                key_resp_E3.tStart = t  # local t and not account for scr refresh
                key_resp_E3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_E3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_E3.started')
                # update status
                key_resp_E3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_E3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_E3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_E3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_E3.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_E3_allKeys.extend(theseKeys)
                if len(_key_resp_E3_allKeys):
                    key_resp_E3.keys = _key_resp_E3_allKeys[-1].name  # just the last key pressed
                    key_resp_E3.rt = _key_resp_E3_allKeys[-1].rt
                    key_resp_E3.duration = _key_resp_E3_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_E3.keys == str(keypad)) or (key_resp_E3.keys == keypad):
                        key_resp_E3.corr = 1
                    else:
                        key_resp_E3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                record_Task_E3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_Task_E3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "record_Task_E3" ---
        for thisComponent in record_Task_E3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for record_Task_E3
        record_Task_E3.tStop = globalClock.getTime(format='float')
        record_Task_E3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('record_Task_E3.stopped', record_Task_E3.tStop)
        # check responses
        if key_resp_E3.keys in ['', [], None]:  # No response was made
            key_resp_E3.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_E3.corr = 1;  # correct non-response
            else:
               key_resp_E3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_11 (TrialHandler)
        trials_11.addData('key_resp_E3.keys',key_resp_E3.keys)
        trials_11.addData('key_resp_E3.corr', key_resp_E3.corr)
        if key_resp_E3.keys != None:  # we had a response
            trials_11.addData('key_resp_E3.rt', key_resp_E3.rt)
            trials_11.addData('key_resp_E3.duration', key_resp_E3.duration)
        # the Routine "record_Task_E3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_E3" ---
        # create an object to store info about Routine feedback_E3
        feedback_E3 = data.Routine(
            name='feedback_E3',
            components=[feedback_text_E3],
        )
        feedback_E3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_E3
        key_resp_E3_rt_sum_temp = key_resp_E3_rt_sum_temp + float(str(key_resp_E3.rt))
        
        if key_resp_E3.corr:
            key_resp_E3_corr_sum_temp =key_resp_E3_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_E3.setText(msg)
        # store start times for feedback_E3
        feedback_E3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_E3.tStart = globalClock.getTime(format='float')
        feedback_E3.status = STARTED
        thisExp.addData('feedback_E3.started', feedback_E3.tStart)
        feedback_E3.maxDuration = None
        # keep track of which components have finished
        feedback_E3Components = feedback_E3.components
        for thisComponent in feedback_E3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_E3" ---
        # if trial has changed, end Routine now
        if isinstance(trials_11, data.TrialHandler2) and thisTrial_11.thisN != trials_11.thisTrial.thisN:
            continueRoutine = False
        feedback_E3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_E3* updates
            
            # if feedback_text_E3 is starting this frame...
            if feedback_text_E3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_E3.frameNStart = frameN  # exact frame index
                feedback_text_E3.tStart = t  # local t and not account for scr refresh
                feedback_text_E3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_E3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_E3.started')
                # update status
                feedback_text_E3.status = STARTED
                feedback_text_E3.setAutoDraw(True)
            
            # if feedback_text_E3 is active this frame...
            if feedback_text_E3.status == STARTED:
                # update params
                pass
            
            # if feedback_text_E3 is stopping this frame...
            if feedback_text_E3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_E3.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_E3.tStop = t  # not accounting for scr refresh
                    feedback_text_E3.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_E3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_E3.stopped')
                    # update status
                    feedback_text_E3.status = FINISHED
                    feedback_text_E3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_E3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_E3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_E3" ---
        for thisComponent in feedback_E3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_E3
        feedback_E3.tStop = globalClock.getTime(format='float')
        feedback_E3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_E3.stopped', feedback_E3.tStop)
        # Run 'End Routine' code from code_E3
        key_resp_E3_corr_sum = key_resp_E3_corr_sum_temp
        key_resp_E3_rt_sum = key_resp_E3_rt_sum_temp
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_E3.maxDurationReached:
            routineTimer.addTime(-feedback_E3.maxDuration)
        elif feedback_E3.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_11, data.TrialHandler2) and thisTrial_11.thisN != trials_11.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_11'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_E3" ---
    # create an object to store info about Routine score_E3
    score_E3 = data.Routine(
        name='score_E3',
        components=[score_E3_text, key_resp_12],
    )
    score_E3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_E3_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_E3_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_E3_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_12
    key_resp_12.keys = []
    key_resp_12.rt = []
    _key_resp_12_allKeys = []
    # store start times for score_E3
    score_E3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_E3.tStart = globalClock.getTime(format='float')
    score_E3.status = STARTED
    thisExp.addData('score_E3.started', score_E3.tStart)
    score_E3.maxDuration = None
    # keep track of which components have finished
    score_E3Components = score_E3.components
    for thisComponent in score_E3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_E3" ---
    score_E3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_E3_text* updates
        
        # if score_E3_text is starting this frame...
        if score_E3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_E3_text.frameNStart = frameN  # exact frame index
            score_E3_text.tStart = t  # local t and not account for scr refresh
            score_E3_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_E3_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_E3_text.started')
            # update status
            score_E3_text.status = STARTED
            score_E3_text.setAutoDraw(True)
        
        # if score_E3_text is active this frame...
        if score_E3_text.status == STARTED:
            # update params
            score_E3_text.setText(feedback_msg, log=False)
        
        # *key_resp_12* updates
        waitOnFlip = False
        
        # if key_resp_12 is starting this frame...
        if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.tStart = t  # local t and not account for scr refresh
            key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_12.started')
            # update status
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_12.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_12.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_12_allKeys.extend(theseKeys)
            if len(_key_resp_12_allKeys):
                key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                key_resp_12.duration = _key_resp_12_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_E3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_E3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_E3" ---
    for thisComponent in score_E3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_E3
    score_E3.tStop = globalClock.getTime(format='float')
    score_E3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_E3.stopped', score_E3.tStop)
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
        key_resp_12.keys = None
    thisExp.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        thisExp.addData('key_resp_12.rt', key_resp_12.rt)
        thisExp.addData('key_resp_12.duration', key_resp_12.duration)
    thisExp.nextEntry()
    # the Routine "score_E3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_F1" ---
    # create an object to store info about Routine reminder_F1
    reminder_F1 = data.Routine(
        name='reminder_F1',
        components=[text_53, key_resp_32],
    )
    reminder_F1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_32
    key_resp_32.keys = []
    key_resp_32.rt = []
    _key_resp_32_allKeys = []
    # store start times for reminder_F1
    reminder_F1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_F1.tStart = globalClock.getTime(format='float')
    reminder_F1.status = STARTED
    thisExp.addData('reminder_F1.started', reminder_F1.tStart)
    reminder_F1.maxDuration = None
    # keep track of which components have finished
    reminder_F1Components = reminder_F1.components
    for thisComponent in reminder_F1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_F1" ---
    reminder_F1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_53* updates
        
        # if text_53 is starting this frame...
        if text_53.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_53.frameNStart = frameN  # exact frame index
            text_53.tStart = t  # local t and not account for scr refresh
            text_53.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_53, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_53.started')
            # update status
            text_53.status = STARTED
            text_53.setAutoDraw(True)
        
        # if text_53 is active this frame...
        if text_53.status == STARTED:
            # update params
            pass
        
        # *key_resp_32* updates
        waitOnFlip = False
        
        # if key_resp_32 is starting this frame...
        if key_resp_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_32.frameNStart = frameN  # exact frame index
            key_resp_32.tStart = t  # local t and not account for scr refresh
            key_resp_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_32, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_32.started')
            # update status
            key_resp_32.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_32.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_32.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_32.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_32.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_32_allKeys.extend(theseKeys)
            if len(_key_resp_32_allKeys):
                key_resp_32.keys = _key_resp_32_allKeys[-1].name  # just the last key pressed
                key_resp_32.rt = _key_resp_32_allKeys[-1].rt
                key_resp_32.duration = _key_resp_32_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_F1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_F1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_F1" ---
    for thisComponent in reminder_F1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_F1
    reminder_F1.tStop = globalClock.getTime(format='float')
    reminder_F1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_F1.stopped', reminder_F1.tStop)
    # check responses
    if key_resp_32.keys in ['', [], None]:  # No response was made
        key_resp_32.keys = None
    thisExp.addData('key_resp_32.keys',key_resp_32.keys)
    if key_resp_32.keys != None:  # we had a response
        thisExp.addData('key_resp_32.rt', key_resp_32.rt)
        thisExp.addData('key_resp_32.duration', key_resp_32.duration)
    thisExp.nextEntry()
    # the Routine "reminder_F1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_12 = data.TrialHandler2(
        name='trials_12',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskF1_H2_korean_right_truncate.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_12)  # add the loop to the experiment
    thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
    if thisTrial_12 != None:
        for paramName in thisTrial_12:
            globals()[paramName] = thisTrial_12[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_12 in trials_12:
        currentLoop = trials_12
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
        if thisTrial_12 != None:
            for paramName in thisTrial_12:
                globals()[paramName] = thisTrial_12[paramName]
        
        # --- Prepare to start Routine "record_Task_F1" ---
        # create an object to store info about Routine record_Task_F1
        record_Task_F1 = data.Routine(
            name='record_Task_F1',
            components=[text_F1, key_resp_F1],
        )
        record_Task_F1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_F1.setText(name)
        # create starting attributes for key_resp_F1
        key_resp_F1.keys = []
        key_resp_F1.rt = []
        _key_resp_F1_allKeys = []
        # store start times for record_Task_F1
        record_Task_F1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        record_Task_F1.tStart = globalClock.getTime(format='float')
        record_Task_F1.status = STARTED
        thisExp.addData('record_Task_F1.started', record_Task_F1.tStart)
        record_Task_F1.maxDuration = None
        # keep track of which components have finished
        record_Task_F1Components = record_Task_F1.components
        for thisComponent in record_Task_F1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "record_Task_F1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_12, data.TrialHandler2) and thisTrial_12.thisN != trials_12.thisTrial.thisN:
            continueRoutine = False
        record_Task_F1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_F1* updates
            
            # if text_F1 is starting this frame...
            if text_F1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_F1.frameNStart = frameN  # exact frame index
                text_F1.tStart = t  # local t and not account for scr refresh
                text_F1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_F1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_F1.started')
                # update status
                text_F1.status = STARTED
                text_F1.setAutoDraw(True)
            
            # if text_F1 is active this frame...
            if text_F1.status == STARTED:
                # update params
                pass
            
            # *key_resp_F1* updates
            waitOnFlip = False
            
            # if key_resp_F1 is starting this frame...
            if key_resp_F1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_F1.frameNStart = frameN  # exact frame index
                key_resp_F1.tStart = t  # local t and not account for scr refresh
                key_resp_F1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_F1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_F1.started')
                # update status
                key_resp_F1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_F1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_F1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_F1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_F1.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_F1_allKeys.extend(theseKeys)
                if len(_key_resp_F1_allKeys):
                    key_resp_F1.keys = _key_resp_F1_allKeys[-1].name  # just the last key pressed
                    key_resp_F1.rt = _key_resp_F1_allKeys[-1].rt
                    key_resp_F1.duration = _key_resp_F1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_F1.keys == str(keypad)) or (key_resp_F1.keys == keypad):
                        key_resp_F1.corr = 1
                    else:
                        key_resp_F1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                record_Task_F1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_Task_F1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "record_Task_F1" ---
        for thisComponent in record_Task_F1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for record_Task_F1
        record_Task_F1.tStop = globalClock.getTime(format='float')
        record_Task_F1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('record_Task_F1.stopped', record_Task_F1.tStop)
        # check responses
        if key_resp_F1.keys in ['', [], None]:  # No response was made
            key_resp_F1.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_F1.corr = 1;  # correct non-response
            else:
               key_resp_F1.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_12 (TrialHandler)
        trials_12.addData('key_resp_F1.keys',key_resp_F1.keys)
        trials_12.addData('key_resp_F1.corr', key_resp_F1.corr)
        if key_resp_F1.keys != None:  # we had a response
            trials_12.addData('key_resp_F1.rt', key_resp_F1.rt)
            trials_12.addData('key_resp_F1.duration', key_resp_F1.duration)
        # the Routine "record_Task_F1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_F1" ---
        # create an object to store info about Routine feedback_F1
        feedback_F1 = data.Routine(
            name='feedback_F1',
            components=[feedback_text_F1],
        )
        feedback_F1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_F1
        key_resp_F1_rt_sum_temp = key_resp_F1_rt_sum_temp + float(str(key_resp_F1.rt))
        
        if key_resp_F1.corr:
            key_resp_F1_corr_sum_temp =key_resp_F1_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_F1.setText(msg)
        # store start times for feedback_F1
        feedback_F1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_F1.tStart = globalClock.getTime(format='float')
        feedback_F1.status = STARTED
        thisExp.addData('feedback_F1.started', feedback_F1.tStart)
        feedback_F1.maxDuration = None
        # keep track of which components have finished
        feedback_F1Components = feedback_F1.components
        for thisComponent in feedback_F1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_F1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_12, data.TrialHandler2) and thisTrial_12.thisN != trials_12.thisTrial.thisN:
            continueRoutine = False
        feedback_F1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_F1* updates
            
            # if feedback_text_F1 is starting this frame...
            if feedback_text_F1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_F1.frameNStart = frameN  # exact frame index
                feedback_text_F1.tStart = t  # local t and not account for scr refresh
                feedback_text_F1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_F1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_F1.started')
                # update status
                feedback_text_F1.status = STARTED
                feedback_text_F1.setAutoDraw(True)
            
            # if feedback_text_F1 is active this frame...
            if feedback_text_F1.status == STARTED:
                # update params
                pass
            
            # if feedback_text_F1 is stopping this frame...
            if feedback_text_F1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_F1.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_F1.tStop = t  # not accounting for scr refresh
                    feedback_text_F1.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_F1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_F1.stopped')
                    # update status
                    feedback_text_F1.status = FINISHED
                    feedback_text_F1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_F1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_F1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_F1" ---
        for thisComponent in feedback_F1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_F1
        feedback_F1.tStop = globalClock.getTime(format='float')
        feedback_F1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_F1.stopped', feedback_F1.tStop)
        # Run 'End Routine' code from code_F1
        key_resp_F1_corr_sum = key_resp_F1_corr_sum_temp
        key_resp_F1_rt_sum = key_resp_F1_rt_sum_temp
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_F1.maxDurationReached:
            routineTimer.addTime(-feedback_F1.maxDuration)
        elif feedback_F1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_12, data.TrialHandler2) and thisTrial_12.thisN != trials_12.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_12'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_F1" ---
    # create an object to store info about Routine score_F1
    score_F1 = data.Routine(
        name='score_F1',
        components=[score_F1_text, key_resp_13],
    )
    score_F1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_F1_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_F1_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_F1_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_13
    key_resp_13.keys = []
    key_resp_13.rt = []
    _key_resp_13_allKeys = []
    # store start times for score_F1
    score_F1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_F1.tStart = globalClock.getTime(format='float')
    score_F1.status = STARTED
    thisExp.addData('score_F1.started', score_F1.tStart)
    score_F1.maxDuration = None
    # keep track of which components have finished
    score_F1Components = score_F1.components
    for thisComponent in score_F1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_F1" ---
    score_F1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_F1_text* updates
        
        # if score_F1_text is starting this frame...
        if score_F1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_F1_text.frameNStart = frameN  # exact frame index
            score_F1_text.tStart = t  # local t and not account for scr refresh
            score_F1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_F1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_F1_text.started')
            # update status
            score_F1_text.status = STARTED
            score_F1_text.setAutoDraw(True)
        
        # if score_F1_text is active this frame...
        if score_F1_text.status == STARTED:
            # update params
            score_F1_text.setText(feedback_msg, log=False)
        
        # *key_resp_13* updates
        waitOnFlip = False
        
        # if key_resp_13 is starting this frame...
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_13.started')
            # update status
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_13_allKeys.extend(theseKeys)
            if len(_key_resp_13_allKeys):
                key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                key_resp_13.duration = _key_resp_13_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_F1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_F1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_F1" ---
    for thisComponent in score_F1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_F1
    score_F1.tStop = globalClock.getTime(format='float')
    score_F1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_F1.stopped', score_F1.tStop)
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys = None
    thisExp.addData('key_resp_13.keys',key_resp_13.keys)
    if key_resp_13.keys != None:  # we had a response
        thisExp.addData('key_resp_13.rt', key_resp_13.rt)
        thisExp.addData('key_resp_13.duration', key_resp_13.duration)
    thisExp.nextEntry()
    # the Routine "score_F1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_G1" ---
    # create an object to store info about Routine reminder_G1
    reminder_G1 = data.Routine(
        name='reminder_G1',
        components=[text_54, key_resp_33],
    )
    reminder_G1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_33
    key_resp_33.keys = []
    key_resp_33.rt = []
    _key_resp_33_allKeys = []
    # store start times for reminder_G1
    reminder_G1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_G1.tStart = globalClock.getTime(format='float')
    reminder_G1.status = STARTED
    thisExp.addData('reminder_G1.started', reminder_G1.tStart)
    reminder_G1.maxDuration = None
    # keep track of which components have finished
    reminder_G1Components = reminder_G1.components
    for thisComponent in reminder_G1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_G1" ---
    reminder_G1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_54* updates
        
        # if text_54 is starting this frame...
        if text_54.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_54.frameNStart = frameN  # exact frame index
            text_54.tStart = t  # local t and not account for scr refresh
            text_54.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_54, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_54.started')
            # update status
            text_54.status = STARTED
            text_54.setAutoDraw(True)
        
        # if text_54 is active this frame...
        if text_54.status == STARTED:
            # update params
            pass
        
        # *key_resp_33* updates
        waitOnFlip = False
        
        # if key_resp_33 is starting this frame...
        if key_resp_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_33.frameNStart = frameN  # exact frame index
            key_resp_33.tStart = t  # local t and not account for scr refresh
            key_resp_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_33, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_33.started')
            # update status
            key_resp_33.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_33.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_33.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_33.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_33.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_33_allKeys.extend(theseKeys)
            if len(_key_resp_33_allKeys):
                key_resp_33.keys = _key_resp_33_allKeys[-1].name  # just the last key pressed
                key_resp_33.rt = _key_resp_33_allKeys[-1].rt
                key_resp_33.duration = _key_resp_33_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_G1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_G1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_G1" ---
    for thisComponent in reminder_G1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_G1
    reminder_G1.tStop = globalClock.getTime(format='float')
    reminder_G1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_G1.stopped', reminder_G1.tStop)
    # check responses
    if key_resp_33.keys in ['', [], None]:  # No response was made
        key_resp_33.keys = None
    thisExp.addData('key_resp_33.keys',key_resp_33.keys)
    if key_resp_33.keys != None:  # we had a response
        thisExp.addData('key_resp_33.rt', key_resp_33.rt)
        thisExp.addData('key_resp_33.duration', key_resp_33.duration)
    thisExp.nextEntry()
    # the Routine "reminder_G1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_13 = data.TrialHandler2(
        name='trials_13',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskG1_I2_block1st3rd_congruent_korean_prefer.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_13)  # add the loop to the experiment
    thisTrial_13 = trials_13.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
    if thisTrial_13 != None:
        for paramName in thisTrial_13:
            globals()[paramName] = thisTrial_13[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_13 in trials_13:
        currentLoop = trials_13
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
        if thisTrial_13 != None:
            for paramName in thisTrial_13:
                globals()[paramName] = thisTrial_13[paramName]
        
        # --- Prepare to start Routine "practice_Task_G1" ---
        # create an object to store info about Routine practice_Task_G1
        practice_Task_G1 = data.Routine(
            name='practice_Task_G1',
            components=[text_G1, key_resp_G1],
        )
        practice_Task_G1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_G1.setText(words)
        # create starting attributes for key_resp_G1
        key_resp_G1.keys = []
        key_resp_G1.rt = []
        _key_resp_G1_allKeys = []
        # store start times for practice_Task_G1
        practice_Task_G1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_Task_G1.tStart = globalClock.getTime(format='float')
        practice_Task_G1.status = STARTED
        thisExp.addData('practice_Task_G1.started', practice_Task_G1.tStart)
        practice_Task_G1.maxDuration = None
        # keep track of which components have finished
        practice_Task_G1Components = practice_Task_G1.components
        for thisComponent in practice_Task_G1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_Task_G1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_13, data.TrialHandler2) and thisTrial_13.thisN != trials_13.thisTrial.thisN:
            continueRoutine = False
        practice_Task_G1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_G1* updates
            
            # if text_G1 is starting this frame...
            if text_G1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_G1.frameNStart = frameN  # exact frame index
                text_G1.tStart = t  # local t and not account for scr refresh
                text_G1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_G1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_G1.started')
                # update status
                text_G1.status = STARTED
                text_G1.setAutoDraw(True)
            
            # if text_G1 is active this frame...
            if text_G1.status == STARTED:
                # update params
                pass
            
            # *key_resp_G1* updates
            waitOnFlip = False
            
            # if key_resp_G1 is starting this frame...
            if key_resp_G1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_G1.frameNStart = frameN  # exact frame index
                key_resp_G1.tStart = t  # local t and not account for scr refresh
                key_resp_G1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_G1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_G1.started')
                # update status
                key_resp_G1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_G1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_G1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_G1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_G1.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_G1_allKeys.extend(theseKeys)
                if len(_key_resp_G1_allKeys):
                    key_resp_G1.keys = _key_resp_G1_allKeys[-1].name  # just the last key pressed
                    key_resp_G1.rt = _key_resp_G1_allKeys[-1].rt
                    key_resp_G1.duration = _key_resp_G1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_G1.keys == str(keypad)) or (key_resp_G1.keys == keypad):
                        key_resp_G1.corr = 1
                    else:
                        key_resp_G1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practice_Task_G1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_Task_G1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_Task_G1" ---
        for thisComponent in practice_Task_G1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_Task_G1
        practice_Task_G1.tStop = globalClock.getTime(format='float')
        practice_Task_G1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_Task_G1.stopped', practice_Task_G1.tStop)
        # check responses
        if key_resp_G1.keys in ['', [], None]:  # No response was made
            key_resp_G1.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_G1.corr = 1;  # correct non-response
            else:
               key_resp_G1.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_13 (TrialHandler)
        trials_13.addData('key_resp_G1.keys',key_resp_G1.keys)
        trials_13.addData('key_resp_G1.corr', key_resp_G1.corr)
        if key_resp_G1.keys != None:  # we had a response
            trials_13.addData('key_resp_G1.rt', key_resp_G1.rt)
            trials_13.addData('key_resp_G1.duration', key_resp_G1.duration)
        # the Routine "practice_Task_G1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_G1" ---
        # create an object to store info about Routine feedback_G1
        feedback_G1 = data.Routine(
            name='feedback_G1',
            components=[feedback_text_G1],
        )
        feedback_G1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_G1
        key_resp_G1_rt_sum_temp = key_resp_G1_rt_sum_temp + float(str(key_resp_G1.rt))
        
        if key_resp_G1.corr:
            key_resp_G1_corr_sum_temp =key_resp_G1_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_G1.setText(msg)
        # store start times for feedback_G1
        feedback_G1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_G1.tStart = globalClock.getTime(format='float')
        feedback_G1.status = STARTED
        thisExp.addData('feedback_G1.started', feedback_G1.tStart)
        feedback_G1.maxDuration = None
        # keep track of which components have finished
        feedback_G1Components = feedback_G1.components
        for thisComponent in feedback_G1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_G1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_13, data.TrialHandler2) and thisTrial_13.thisN != trials_13.thisTrial.thisN:
            continueRoutine = False
        feedback_G1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_G1* updates
            
            # if feedback_text_G1 is starting this frame...
            if feedback_text_G1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_G1.frameNStart = frameN  # exact frame index
                feedback_text_G1.tStart = t  # local t and not account for scr refresh
                feedback_text_G1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_G1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_G1.started')
                # update status
                feedback_text_G1.status = STARTED
                feedback_text_G1.setAutoDraw(True)
            
            # if feedback_text_G1 is active this frame...
            if feedback_text_G1.status == STARTED:
                # update params
                pass
            
            # if feedback_text_G1 is stopping this frame...
            if feedback_text_G1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_G1.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_G1.tStop = t  # not accounting for scr refresh
                    feedback_text_G1.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_G1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_G1.stopped')
                    # update status
                    feedback_text_G1.status = FINISHED
                    feedback_text_G1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_G1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_G1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_G1" ---
        for thisComponent in feedback_G1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_G1
        feedback_G1.tStop = globalClock.getTime(format='float')
        feedback_G1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_G1.stopped', feedback_G1.tStop)
        # Run 'End Routine' code from code_G1
        key_resp_G1_corr_sum = key_resp_G1_corr_sum_temp
        key_resp_G1_rt_sum = key_resp_G1_rt_sum_temp
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_G1.maxDurationReached:
            routineTimer.addTime(-feedback_G1.maxDuration)
        elif feedback_G1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_13, data.TrialHandler2) and thisTrial_13.thisN != trials_13.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_13'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_G1" ---
    # create an object to store info about Routine score_G1
    score_G1 = data.Routine(
        name='score_G1',
        components=[score_G1_text, key_resp_14],
    )
    score_G1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_G1_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_G1_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_G1_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_14
    key_resp_14.keys = []
    key_resp_14.rt = []
    _key_resp_14_allKeys = []
    # store start times for score_G1
    score_G1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_G1.tStart = globalClock.getTime(format='float')
    score_G1.status = STARTED
    thisExp.addData('score_G1.started', score_G1.tStart)
    score_G1.maxDuration = None
    # keep track of which components have finished
    score_G1Components = score_G1.components
    for thisComponent in score_G1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_G1" ---
    score_G1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_G1_text* updates
        
        # if score_G1_text is starting this frame...
        if score_G1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_G1_text.frameNStart = frameN  # exact frame index
            score_G1_text.tStart = t  # local t and not account for scr refresh
            score_G1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_G1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_G1_text.started')
            # update status
            score_G1_text.status = STARTED
            score_G1_text.setAutoDraw(True)
        
        # if score_G1_text is active this frame...
        if score_G1_text.status == STARTED:
            # update params
            score_G1_text.setText(feedback_msg, log=False)
        
        # *key_resp_14* updates
        waitOnFlip = False
        
        # if key_resp_14 is starting this frame...
        if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.tStart = t  # local t and not account for scr refresh
            key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_14.started')
            # update status
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_14.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_14.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_14_allKeys.extend(theseKeys)
            if len(_key_resp_14_allKeys):
                key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                key_resp_14.duration = _key_resp_14_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_G1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_G1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_G1" ---
    for thisComponent in score_G1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_G1
    score_G1.tStop = globalClock.getTime(format='float')
    score_G1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_G1.stopped', score_G1.tStop)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
    thisExp.addData('key_resp_14.keys',key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        thisExp.addData('key_resp_14.rt', key_resp_14.rt)
        thisExp.addData('key_resp_14.duration', key_resp_14.duration)
    thisExp.nextEntry()
    # the Routine "score_G1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_G2" ---
    # create an object to store info about Routine reminder_G2
    reminder_G2 = data.Routine(
        name='reminder_G2',
        components=[text_55, key_resp_35],
    )
    reminder_G2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_35
    key_resp_35.keys = []
    key_resp_35.rt = []
    _key_resp_35_allKeys = []
    # store start times for reminder_G2
    reminder_G2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_G2.tStart = globalClock.getTime(format='float')
    reminder_G2.status = STARTED
    thisExp.addData('reminder_G2.started', reminder_G2.tStart)
    reminder_G2.maxDuration = None
    # keep track of which components have finished
    reminder_G2Components = reminder_G2.components
    for thisComponent in reminder_G2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_G2" ---
    reminder_G2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_55* updates
        
        # if text_55 is starting this frame...
        if text_55.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_55.frameNStart = frameN  # exact frame index
            text_55.tStart = t  # local t and not account for scr refresh
            text_55.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_55, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_55.started')
            # update status
            text_55.status = STARTED
            text_55.setAutoDraw(True)
        
        # if text_55 is active this frame...
        if text_55.status == STARTED:
            # update params
            pass
        
        # *key_resp_35* updates
        waitOnFlip = False
        
        # if key_resp_35 is starting this frame...
        if key_resp_35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_35.frameNStart = frameN  # exact frame index
            key_resp_35.tStart = t  # local t and not account for scr refresh
            key_resp_35.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_35, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_35.started')
            # update status
            key_resp_35.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_35.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_35.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_35.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_35.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_35_allKeys.extend(theseKeys)
            if len(_key_resp_35_allKeys):
                key_resp_35.keys = _key_resp_35_allKeys[-1].name  # just the last key pressed
                key_resp_35.rt = _key_resp_35_allKeys[-1].rt
                key_resp_35.duration = _key_resp_35_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_G2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_G2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_G2" ---
    for thisComponent in reminder_G2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_G2
    reminder_G2.tStop = globalClock.getTime(format='float')
    reminder_G2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_G2.stopped', reminder_G2.tStop)
    # check responses
    if key_resp_35.keys in ['', [], None]:  # No response was made
        key_resp_35.keys = None
    thisExp.addData('key_resp_35.keys',key_resp_35.keys)
    if key_resp_35.keys != None:  # we had a response
        thisExp.addData('key_resp_35.rt', key_resp_35.rt)
        thisExp.addData('key_resp_35.duration', key_resp_35.duration)
    thisExp.nextEntry()
    # the Routine "reminder_G2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_14 = data.TrialHandler2(
        name='trials_14',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskG1_I2_block2nd_congruent_korean_prefer.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_14)  # add the loop to the experiment
    thisTrial_14 = trials_14.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
    if thisTrial_14 != None:
        for paramName in thisTrial_14:
            globals()[paramName] = thisTrial_14[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_14 in trials_14:
        currentLoop = trials_14
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
        if thisTrial_14 != None:
            for paramName in thisTrial_14:
                globals()[paramName] = thisTrial_14[paramName]
        
        # --- Prepare to start Routine "record_Task_G2" ---
        # create an object to store info about Routine record_Task_G2
        record_Task_G2 = data.Routine(
            name='record_Task_G2',
            components=[text_G2, key_resp_G2],
        )
        record_Task_G2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_G2.setText(words)
        # create starting attributes for key_resp_G2
        key_resp_G2.keys = []
        key_resp_G2.rt = []
        _key_resp_G2_allKeys = []
        # store start times for record_Task_G2
        record_Task_G2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        record_Task_G2.tStart = globalClock.getTime(format='float')
        record_Task_G2.status = STARTED
        thisExp.addData('record_Task_G2.started', record_Task_G2.tStart)
        record_Task_G2.maxDuration = None
        # keep track of which components have finished
        record_Task_G2Components = record_Task_G2.components
        for thisComponent in record_Task_G2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "record_Task_G2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_14, data.TrialHandler2) and thisTrial_14.thisN != trials_14.thisTrial.thisN:
            continueRoutine = False
        record_Task_G2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_G2* updates
            
            # if text_G2 is starting this frame...
            if text_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_G2.frameNStart = frameN  # exact frame index
                text_G2.tStart = t  # local t and not account for scr refresh
                text_G2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_G2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_G2.started')
                # update status
                text_G2.status = STARTED
                text_G2.setAutoDraw(True)
            
            # if text_G2 is active this frame...
            if text_G2.status == STARTED:
                # update params
                pass
            
            # *key_resp_G2* updates
            waitOnFlip = False
            
            # if key_resp_G2 is starting this frame...
            if key_resp_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_G2.frameNStart = frameN  # exact frame index
                key_resp_G2.tStart = t  # local t and not account for scr refresh
                key_resp_G2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_G2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_G2.started')
                # update status
                key_resp_G2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_G2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_G2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_G2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_G2.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_G2_allKeys.extend(theseKeys)
                if len(_key_resp_G2_allKeys):
                    key_resp_G2.keys = _key_resp_G2_allKeys[-1].name  # just the last key pressed
                    key_resp_G2.rt = _key_resp_G2_allKeys[-1].rt
                    key_resp_G2.duration = _key_resp_G2_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_G2.keys == str(kaypad)) or (key_resp_G2.keys == kaypad):
                        key_resp_G2.corr = 1
                    else:
                        key_resp_G2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                record_Task_G2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_Task_G2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "record_Task_G2" ---
        for thisComponent in record_Task_G2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for record_Task_G2
        record_Task_G2.tStop = globalClock.getTime(format='float')
        record_Task_G2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('record_Task_G2.stopped', record_Task_G2.tStop)
        # check responses
        if key_resp_G2.keys in ['', [], None]:  # No response was made
            key_resp_G2.keys = None
            # was no response the correct answer?!
            if str(kaypad).lower() == 'none':
               key_resp_G2.corr = 1;  # correct non-response
            else:
               key_resp_G2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_14 (TrialHandler)
        trials_14.addData('key_resp_G2.keys',key_resp_G2.keys)
        trials_14.addData('key_resp_G2.corr', key_resp_G2.corr)
        if key_resp_G2.keys != None:  # we had a response
            trials_14.addData('key_resp_G2.rt', key_resp_G2.rt)
            trials_14.addData('key_resp_G2.duration', key_resp_G2.duration)
        # the Routine "record_Task_G2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_G2" ---
        # create an object to store info about Routine feedback_G2
        feedback_G2 = data.Routine(
            name='feedback_G2',
            components=[feedback_text_G2],
        )
        feedback_G2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_G2
        key_resp_G2_rt_sum_temp = key_resp_G2_rt_sum_temp + float(str(key_resp_G2.rt))
        
        if key_resp_G2.corr:
            key_resp_G2_corr_sum_temp =key_resp_G2_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_G2.setText(msg)
        # store start times for feedback_G2
        feedback_G2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_G2.tStart = globalClock.getTime(format='float')
        feedback_G2.status = STARTED
        thisExp.addData('feedback_G2.started', feedback_G2.tStart)
        feedback_G2.maxDuration = None
        # keep track of which components have finished
        feedback_G2Components = feedback_G2.components
        for thisComponent in feedback_G2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_G2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_14, data.TrialHandler2) and thisTrial_14.thisN != trials_14.thisTrial.thisN:
            continueRoutine = False
        feedback_G2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_G2* updates
            
            # if feedback_text_G2 is starting this frame...
            if feedback_text_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_G2.frameNStart = frameN  # exact frame index
                feedback_text_G2.tStart = t  # local t and not account for scr refresh
                feedback_text_G2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_G2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_G2.started')
                # update status
                feedback_text_G2.status = STARTED
                feedback_text_G2.setAutoDraw(True)
            
            # if feedback_text_G2 is active this frame...
            if feedback_text_G2.status == STARTED:
                # update params
                pass
            
            # if feedback_text_G2 is stopping this frame...
            if feedback_text_G2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_G2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_G2.tStop = t  # not accounting for scr refresh
                    feedback_text_G2.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_G2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_G2.stopped')
                    # update status
                    feedback_text_G2.status = FINISHED
                    feedback_text_G2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_G2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_G2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_G2" ---
        for thisComponent in feedback_G2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_G2
        feedback_G2.tStop = globalClock.getTime(format='float')
        feedback_G2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_G2.stopped', feedback_G2.tStop)
        # Run 'End Routine' code from code_G2
        key_resp_G2_corr_sum = key_resp_G2_corr_sum_temp
        key_resp_G2_rt_sum = key_resp_G2_rt_sum_temp
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_G2.maxDurationReached:
            routineTimer.addTime(-feedback_G2.maxDuration)
        elif feedback_G2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_14, data.TrialHandler2) and thisTrial_14.thisN != trials_14.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_14'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_G2" ---
    # create an object to store info about Routine score_G2
    score_G2 = data.Routine(
        name='score_G2',
        components=[score_G2_text, key_resp_15],
    )
    score_G2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_G2_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_G2_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_G2_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_15
    key_resp_15.keys = []
    key_resp_15.rt = []
    _key_resp_15_allKeys = []
    # store start times for score_G2
    score_G2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_G2.tStart = globalClock.getTime(format='float')
    score_G2.status = STARTED
    thisExp.addData('score_G2.started', score_G2.tStart)
    score_G2.maxDuration = None
    # keep track of which components have finished
    score_G2Components = score_G2.components
    for thisComponent in score_G2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_G2" ---
    score_G2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_G2_text* updates
        
        # if score_G2_text is starting this frame...
        if score_G2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_G2_text.frameNStart = frameN  # exact frame index
            score_G2_text.tStart = t  # local t and not account for scr refresh
            score_G2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_G2_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_G2_text.started')
            # update status
            score_G2_text.status = STARTED
            score_G2_text.setAutoDraw(True)
        
        # if score_G2_text is active this frame...
        if score_G2_text.status == STARTED:
            # update params
            score_G2_text.setText(feedback_msg, log=False)
        
        # *key_resp_15* updates
        waitOnFlip = False
        
        # if key_resp_15 is starting this frame...
        if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_15.frameNStart = frameN  # exact frame index
            key_resp_15.tStart = t  # local t and not account for scr refresh
            key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_15.started')
            # update status
            key_resp_15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_15.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_15.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_15_allKeys.extend(theseKeys)
            if len(_key_resp_15_allKeys):
                key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
                key_resp_15.rt = _key_resp_15_allKeys[-1].rt
                key_resp_15.duration = _key_resp_15_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_G2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_G2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_G2" ---
    for thisComponent in score_G2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_G2
    score_G2.tStop = globalClock.getTime(format='float')
    score_G2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_G2.stopped', score_G2.tStop)
    # check responses
    if key_resp_15.keys in ['', [], None]:  # No response was made
        key_resp_15.keys = None
    thisExp.addData('key_resp_15.keys',key_resp_15.keys)
    if key_resp_15.keys != None:  # we had a response
        thisExp.addData('key_resp_15.rt', key_resp_15.rt)
        thisExp.addData('key_resp_15.duration', key_resp_15.duration)
    thisExp.nextEntry()
    # the Routine "score_G2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_G3" ---
    # create an object to store info about Routine reminder_G3
    reminder_G3 = data.Routine(
        name='reminder_G3',
        components=[text_56, key_resp_34],
    )
    reminder_G3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_34
    key_resp_34.keys = []
    key_resp_34.rt = []
    _key_resp_34_allKeys = []
    # store start times for reminder_G3
    reminder_G3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_G3.tStart = globalClock.getTime(format='float')
    reminder_G3.status = STARTED
    thisExp.addData('reminder_G3.started', reminder_G3.tStart)
    reminder_G3.maxDuration = None
    # keep track of which components have finished
    reminder_G3Components = reminder_G3.components
    for thisComponent in reminder_G3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_G3" ---
    reminder_G3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_56* updates
        
        # if text_56 is starting this frame...
        if text_56.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_56.frameNStart = frameN  # exact frame index
            text_56.tStart = t  # local t and not account for scr refresh
            text_56.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_56, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_56.started')
            # update status
            text_56.status = STARTED
            text_56.setAutoDraw(True)
        
        # if text_56 is active this frame...
        if text_56.status == STARTED:
            # update params
            pass
        
        # *key_resp_34* updates
        waitOnFlip = False
        
        # if key_resp_34 is starting this frame...
        if key_resp_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_34.frameNStart = frameN  # exact frame index
            key_resp_34.tStart = t  # local t and not account for scr refresh
            key_resp_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_34, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_34.started')
            # update status
            key_resp_34.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_34.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_34.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_34.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_34.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_34_allKeys.extend(theseKeys)
            if len(_key_resp_34_allKeys):
                key_resp_34.keys = _key_resp_34_allKeys[-1].name  # just the last key pressed
                key_resp_34.rt = _key_resp_34_allKeys[-1].rt
                key_resp_34.duration = _key_resp_34_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_G3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_G3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_G3" ---
    for thisComponent in reminder_G3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_G3
    reminder_G3.tStop = globalClock.getTime(format='float')
    reminder_G3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_G3.stopped', reminder_G3.tStop)
    # check responses
    if key_resp_34.keys in ['', [], None]:  # No response was made
        key_resp_34.keys = None
    thisExp.addData('key_resp_34.keys',key_resp_34.keys)
    if key_resp_34.keys != None:  # we had a response
        thisExp.addData('key_resp_34.rt', key_resp_34.rt)
        thisExp.addData('key_resp_34.duration', key_resp_34.duration)
    thisExp.nextEntry()
    # the Routine "reminder_G3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_15 = data.TrialHandler2(
        name='trials_15',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskG1_I2_block1st3rd_congruent_korean_prefer.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_15)  # add the loop to the experiment
    thisTrial_15 = trials_15.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
    if thisTrial_15 != None:
        for paramName in thisTrial_15:
            globals()[paramName] = thisTrial_15[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_15 in trials_15:
        currentLoop = trials_15
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
        if thisTrial_15 != None:
            for paramName in thisTrial_15:
                globals()[paramName] = thisTrial_15[paramName]
        
        # --- Prepare to start Routine "record_Task_G3" ---
        # create an object to store info about Routine record_Task_G3
        record_Task_G3 = data.Routine(
            name='record_Task_G3',
            components=[text_G3, key_resp_G3],
        )
        record_Task_G3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_G3.setText(words)
        # create starting attributes for key_resp_G3
        key_resp_G3.keys = []
        key_resp_G3.rt = []
        _key_resp_G3_allKeys = []
        # store start times for record_Task_G3
        record_Task_G3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        record_Task_G3.tStart = globalClock.getTime(format='float')
        record_Task_G3.status = STARTED
        thisExp.addData('record_Task_G3.started', record_Task_G3.tStart)
        record_Task_G3.maxDuration = None
        # keep track of which components have finished
        record_Task_G3Components = record_Task_G3.components
        for thisComponent in record_Task_G3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "record_Task_G3" ---
        # if trial has changed, end Routine now
        if isinstance(trials_15, data.TrialHandler2) and thisTrial_15.thisN != trials_15.thisTrial.thisN:
            continueRoutine = False
        record_Task_G3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_G3* updates
            
            # if text_G3 is starting this frame...
            if text_G3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_G3.frameNStart = frameN  # exact frame index
                text_G3.tStart = t  # local t and not account for scr refresh
                text_G3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_G3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_G3.started')
                # update status
                text_G3.status = STARTED
                text_G3.setAutoDraw(True)
            
            # if text_G3 is active this frame...
            if text_G3.status == STARTED:
                # update params
                pass
            
            # *key_resp_G3* updates
            waitOnFlip = False
            
            # if key_resp_G3 is starting this frame...
            if key_resp_G3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_G3.frameNStart = frameN  # exact frame index
                key_resp_G3.tStart = t  # local t and not account for scr refresh
                key_resp_G3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_G3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_G3.started')
                # update status
                key_resp_G3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_G3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_G3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_G3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_G3.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_G3_allKeys.extend(theseKeys)
                if len(_key_resp_G3_allKeys):
                    key_resp_G3.keys = _key_resp_G3_allKeys[-1].name  # just the last key pressed
                    key_resp_G3.rt = _key_resp_G3_allKeys[-1].rt
                    key_resp_G3.duration = _key_resp_G3_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_G3.keys == str(keypad)) or (key_resp_G3.keys == keypad):
                        key_resp_G3.corr = 1
                    else:
                        key_resp_G3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                record_Task_G3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_Task_G3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "record_Task_G3" ---
        for thisComponent in record_Task_G3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for record_Task_G3
        record_Task_G3.tStop = globalClock.getTime(format='float')
        record_Task_G3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('record_Task_G3.stopped', record_Task_G3.tStop)
        # check responses
        if key_resp_G3.keys in ['', [], None]:  # No response was made
            key_resp_G3.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_G3.corr = 1;  # correct non-response
            else:
               key_resp_G3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_15 (TrialHandler)
        trials_15.addData('key_resp_G3.keys',key_resp_G3.keys)
        trials_15.addData('key_resp_G3.corr', key_resp_G3.corr)
        if key_resp_G3.keys != None:  # we had a response
            trials_15.addData('key_resp_G3.rt', key_resp_G3.rt)
            trials_15.addData('key_resp_G3.duration', key_resp_G3.duration)
        # the Routine "record_Task_G3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_G3" ---
        # create an object to store info about Routine feedback_G3
        feedback_G3 = data.Routine(
            name='feedback_G3',
            components=[feedback_text_G3],
        )
        feedback_G3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_G3
        key_resp_G3_rt_sum_temp = key_resp_G3_rt_sum_temp + float(str(key_resp_G3.rt))
        
        if key_resp_G3.corr:
            key_resp_G3_corr_sum_temp =key_resp_G3_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_G3.setText(msg)
        # store start times for feedback_G3
        feedback_G3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_G3.tStart = globalClock.getTime(format='float')
        feedback_G3.status = STARTED
        thisExp.addData('feedback_G3.started', feedback_G3.tStart)
        feedback_G3.maxDuration = None
        # keep track of which components have finished
        feedback_G3Components = feedback_G3.components
        for thisComponent in feedback_G3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_G3" ---
        # if trial has changed, end Routine now
        if isinstance(trials_15, data.TrialHandler2) and thisTrial_15.thisN != trials_15.thisTrial.thisN:
            continueRoutine = False
        feedback_G3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_G3* updates
            
            # if feedback_text_G3 is starting this frame...
            if feedback_text_G3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_G3.frameNStart = frameN  # exact frame index
                feedback_text_G3.tStart = t  # local t and not account for scr refresh
                feedback_text_G3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_G3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_G3.started')
                # update status
                feedback_text_G3.status = STARTED
                feedback_text_G3.setAutoDraw(True)
            
            # if feedback_text_G3 is active this frame...
            if feedback_text_G3.status == STARTED:
                # update params
                pass
            
            # if feedback_text_G3 is stopping this frame...
            if feedback_text_G3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_G3.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_G3.tStop = t  # not accounting for scr refresh
                    feedback_text_G3.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_G3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_G3.stopped')
                    # update status
                    feedback_text_G3.status = FINISHED
                    feedback_text_G3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_G3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_G3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_G3" ---
        for thisComponent in feedback_G3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_G3
        feedback_G3.tStop = globalClock.getTime(format='float')
        feedback_G3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_G3.stopped', feedback_G3.tStop)
        # Run 'End Routine' code from code_G3
        key_resp_G3_corr_sum = key_resp_G3_corr_sum_temp
        key_resp_G3_rt_sum = key_resp_G3_rt_sum_temp
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_G3.maxDurationReached:
            routineTimer.addTime(-feedback_G3.maxDuration)
        elif feedback_G3.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_15, data.TrialHandler2) and thisTrial_15.thisN != trials_15.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_15'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_G3" ---
    # create an object to store info about Routine score_G3
    score_G3 = data.Routine(
        name='score_G3',
        components=[score_G3_text, key_resp_16],
    )
    score_G3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_G3_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_G3_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_G3_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_16
    key_resp_16.keys = []
    key_resp_16.rt = []
    _key_resp_16_allKeys = []
    # store start times for score_G3
    score_G3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_G3.tStart = globalClock.getTime(format='float')
    score_G3.status = STARTED
    thisExp.addData('score_G3.started', score_G3.tStart)
    score_G3.maxDuration = None
    # keep track of which components have finished
    score_G3Components = score_G3.components
    for thisComponent in score_G3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_G3" ---
    score_G3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_G3_text* updates
        
        # if score_G3_text is starting this frame...
        if score_G3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_G3_text.frameNStart = frameN  # exact frame index
            score_G3_text.tStart = t  # local t and not account for scr refresh
            score_G3_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_G3_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_G3_text.started')
            # update status
            score_G3_text.status = STARTED
            score_G3_text.setAutoDraw(True)
        
        # if score_G3_text is active this frame...
        if score_G3_text.status == STARTED:
            # update params
            score_G3_text.setText(feedback_msg, log=False)
        
        # *key_resp_16* updates
        waitOnFlip = False
        
        # if key_resp_16 is starting this frame...
        if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_16.frameNStart = frameN  # exact frame index
            key_resp_16.tStart = t  # local t and not account for scr refresh
            key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_16.started')
            # update status
            key_resp_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_16.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_16.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_16_allKeys.extend(theseKeys)
            if len(_key_resp_16_allKeys):
                key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
                key_resp_16.rt = _key_resp_16_allKeys[-1].rt
                key_resp_16.duration = _key_resp_16_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_G3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_G3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_G3" ---
    for thisComponent in score_G3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_G3
    score_G3.tStop = globalClock.getTime(format='float')
    score_G3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_G3.stopped', score_G3.tStop)
    # check responses
    if key_resp_16.keys in ['', [], None]:  # No response was made
        key_resp_16.keys = None
    thisExp.addData('key_resp_16.keys',key_resp_16.keys)
    if key_resp_16.keys != None:  # we had a response
        thisExp.addData('key_resp_16.rt', key_resp_16.rt)
        thisExp.addData('key_resp_16.duration', key_resp_16.duration)
    thisExp.nextEntry()
    # the Routine "score_G3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_H1" ---
    # create an object to store info about Routine reminder_H1
    reminder_H1 = data.Routine(
        name='reminder_H1',
        components=[text_H1, key_resp_H1],
    )
    reminder_H1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_H1
    key_resp_H1.keys = []
    key_resp_H1.rt = []
    _key_resp_H1_allKeys = []
    # store start times for reminder_H1
    reminder_H1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_H1.tStart = globalClock.getTime(format='float')
    reminder_H1.status = STARTED
    thisExp.addData('reminder_H1.started', reminder_H1.tStart)
    reminder_H1.maxDuration = None
    # keep track of which components have finished
    reminder_H1Components = reminder_H1.components
    for thisComponent in reminder_H1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_H1" ---
    reminder_H1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_H1* updates
        
        # if text_H1 is starting this frame...
        if text_H1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_H1.frameNStart = frameN  # exact frame index
            text_H1.tStart = t  # local t and not account for scr refresh
            text_H1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_H1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_H1.started')
            # update status
            text_H1.status = STARTED
            text_H1.setAutoDraw(True)
        
        # if text_H1 is active this frame...
        if text_H1.status == STARTED:
            # update params
            pass
        
        # *key_resp_H1* updates
        waitOnFlip = False
        
        # if key_resp_H1 is starting this frame...
        if key_resp_H1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_H1.frameNStart = frameN  # exact frame index
            key_resp_H1.tStart = t  # local t and not account for scr refresh
            key_resp_H1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_H1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_H1.started')
            # update status
            key_resp_H1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_H1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_H1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_H1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_H1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_H1_allKeys.extend(theseKeys)
            if len(_key_resp_H1_allKeys):
                key_resp_H1.keys = _key_resp_H1_allKeys[-1].name  # just the last key pressed
                key_resp_H1.rt = _key_resp_H1_allKeys[-1].rt
                key_resp_H1.duration = _key_resp_H1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_H1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_H1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_H1" ---
    for thisComponent in reminder_H1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_H1
    reminder_H1.tStop = globalClock.getTime(format='float')
    reminder_H1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_H1.stopped', reminder_H1.tStop)
    # check responses
    if key_resp_H1.keys in ['', [], None]:  # No response was made
        key_resp_H1.keys = None
    thisExp.addData('key_resp_H1.keys',key_resp_H1.keys)
    if key_resp_H1.keys != None:  # we had a response
        thisExp.addData('key_resp_H1.rt', key_resp_H1.rt)
        thisExp.addData('key_resp_H1.duration', key_resp_H1.duration)
    thisExp.nextEntry()
    # the Routine "reminder_H1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_16 = data.TrialHandler2(
        name='trials_16',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskF2_H1_japan_right_truncate.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_16)  # add the loop to the experiment
    thisTrial_16 = trials_16.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
    if thisTrial_16 != None:
        for paramName in thisTrial_16:
            globals()[paramName] = thisTrial_16[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_16 in trials_16:
        currentLoop = trials_16
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
        if thisTrial_16 != None:
            for paramName in thisTrial_16:
                globals()[paramName] = thisTrial_16[paramName]
        
        # --- Prepare to start Routine "record_Task_H1" ---
        # create an object to store info about Routine record_Task_H1
        record_Task_H1 = data.Routine(
            name='record_Task_H1',
            components=[text_37, key_resp_19],
        )
        record_Task_H1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_37.setText(name)
        # create starting attributes for key_resp_19
        key_resp_19.keys = []
        key_resp_19.rt = []
        _key_resp_19_allKeys = []
        # store start times for record_Task_H1
        record_Task_H1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        record_Task_H1.tStart = globalClock.getTime(format='float')
        record_Task_H1.status = STARTED
        thisExp.addData('record_Task_H1.started', record_Task_H1.tStart)
        record_Task_H1.maxDuration = None
        # keep track of which components have finished
        record_Task_H1Components = record_Task_H1.components
        for thisComponent in record_Task_H1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "record_Task_H1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_16, data.TrialHandler2) and thisTrial_16.thisN != trials_16.thisTrial.thisN:
            continueRoutine = False
        record_Task_H1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_37* updates
            
            # if text_37 is starting this frame...
            if text_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_37.frameNStart = frameN  # exact frame index
                text_37.tStart = t  # local t and not account for scr refresh
                text_37.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_37, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_37.started')
                # update status
                text_37.status = STARTED
                text_37.setAutoDraw(True)
            
            # if text_37 is active this frame...
            if text_37.status == STARTED:
                # update params
                pass
            
            # *key_resp_19* updates
            waitOnFlip = False
            
            # if key_resp_19 is starting this frame...
            if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_19.frameNStart = frameN  # exact frame index
                key_resp_19.tStart = t  # local t and not account for scr refresh
                key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_19.started')
                # update status
                key_resp_19.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_19.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_19.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_19_allKeys.extend(theseKeys)
                if len(_key_resp_19_allKeys):
                    key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                    key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                    key_resp_19.duration = _key_resp_19_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_19.keys == str(keypad)) or (key_resp_19.keys == keypad):
                        key_resp_19.corr = 1
                    else:
                        key_resp_19.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                record_Task_H1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_Task_H1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "record_Task_H1" ---
        for thisComponent in record_Task_H1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for record_Task_H1
        record_Task_H1.tStop = globalClock.getTime(format='float')
        record_Task_H1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('record_Task_H1.stopped', record_Task_H1.tStop)
        # check responses
        if key_resp_19.keys in ['', [], None]:  # No response was made
            key_resp_19.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_19.corr = 1;  # correct non-response
            else:
               key_resp_19.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_16 (TrialHandler)
        trials_16.addData('key_resp_19.keys',key_resp_19.keys)
        trials_16.addData('key_resp_19.corr', key_resp_19.corr)
        if key_resp_19.keys != None:  # we had a response
            trials_16.addData('key_resp_19.rt', key_resp_19.rt)
            trials_16.addData('key_resp_19.duration', key_resp_19.duration)
        # the Routine "record_Task_H1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_H1" ---
        # create an object to store info about Routine feedback_H1
        feedback_H1 = data.Routine(
            name='feedback_H1',
            components=[feedback_text_H1],
        )
        feedback_H1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_H1
        key_resp_H1_rt_sum_temp = key_resp_H1_rt_sum_temp + float(str(key_resp_H1.rt))
        
        if key_resp_H1.corr:
            key_resp_H1_corr_sum_temp =key_resp_H1_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_H1.setText(msg)
        # store start times for feedback_H1
        feedback_H1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_H1.tStart = globalClock.getTime(format='float')
        feedback_H1.status = STARTED
        thisExp.addData('feedback_H1.started', feedback_H1.tStart)
        feedback_H1.maxDuration = None
        # keep track of which components have finished
        feedback_H1Components = feedback_H1.components
        for thisComponent in feedback_H1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_H1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_16, data.TrialHandler2) and thisTrial_16.thisN != trials_16.thisTrial.thisN:
            continueRoutine = False
        feedback_H1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_H1* updates
            
            # if feedback_text_H1 is starting this frame...
            if feedback_text_H1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_H1.frameNStart = frameN  # exact frame index
                feedback_text_H1.tStart = t  # local t and not account for scr refresh
                feedback_text_H1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_H1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_H1.started')
                # update status
                feedback_text_H1.status = STARTED
                feedback_text_H1.setAutoDraw(True)
            
            # if feedback_text_H1 is active this frame...
            if feedback_text_H1.status == STARTED:
                # update params
                pass
            
            # if feedback_text_H1 is stopping this frame...
            if feedback_text_H1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_H1.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_H1.tStop = t  # not accounting for scr refresh
                    feedback_text_H1.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_H1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_H1.stopped')
                    # update status
                    feedback_text_H1.status = FINISHED
                    feedback_text_H1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_H1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_H1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_H1" ---
        for thisComponent in feedback_H1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_H1
        feedback_H1.tStop = globalClock.getTime(format='float')
        feedback_H1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_H1.stopped', feedback_H1.tStop)
        # Run 'End Routine' code from code_H1
        key_resp_H1_corr_sum = key_resp_H1_corr_sum_temp
        key_resp_H1_rt_sum = key_resp_H1_rt_sum_temp
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_H1.maxDurationReached:
            routineTimer.addTime(-feedback_H1.maxDuration)
        elif feedback_H1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_16, data.TrialHandler2) and thisTrial_16.thisN != trials_16.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_16'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_H1" ---
    # create an object to store info about Routine score_H1
    score_H1 = data.Routine(
        name='score_H1',
        components=[score_H1_text, key_resp_17],
    )
    score_H1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_H1_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_H1_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_H1_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_17
    key_resp_17.keys = []
    key_resp_17.rt = []
    _key_resp_17_allKeys = []
    # store start times for score_H1
    score_H1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_H1.tStart = globalClock.getTime(format='float')
    score_H1.status = STARTED
    thisExp.addData('score_H1.started', score_H1.tStart)
    score_H1.maxDuration = None
    # keep track of which components have finished
    score_H1Components = score_H1.components
    for thisComponent in score_H1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_H1" ---
    score_H1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_H1_text* updates
        
        # if score_H1_text is starting this frame...
        if score_H1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_H1_text.frameNStart = frameN  # exact frame index
            score_H1_text.tStart = t  # local t and not account for scr refresh
            score_H1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_H1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_H1_text.started')
            # update status
            score_H1_text.status = STARTED
            score_H1_text.setAutoDraw(True)
        
        # if score_H1_text is active this frame...
        if score_H1_text.status == STARTED:
            # update params
            score_H1_text.setText(feedback_msg, log=False)
        
        # *key_resp_17* updates
        waitOnFlip = False
        
        # if key_resp_17 is starting this frame...
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_17.started')
            # update status
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_17_allKeys.extend(theseKeys)
            if len(_key_resp_17_allKeys):
                key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                key_resp_17.duration = _key_resp_17_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_H1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_H1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_H1" ---
    for thisComponent in score_H1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_H1
    score_H1.tStop = globalClock.getTime(format='float')
    score_H1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_H1.stopped', score_H1.tStop)
    # check responses
    if key_resp_17.keys in ['', [], None]:  # No response was made
        key_resp_17.keys = None
    thisExp.addData('key_resp_17.keys',key_resp_17.keys)
    if key_resp_17.keys != None:  # we had a response
        thisExp.addData('key_resp_17.rt', key_resp_17.rt)
        thisExp.addData('key_resp_17.duration', key_resp_17.duration)
    thisExp.nextEntry()
    # the Routine "score_H1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_I1" ---
    # create an object to store info about Routine reminder_I1
    reminder_I1 = data.Routine(
        name='reminder_I1',
        components=[text_58, key_resp_37],
    )
    reminder_I1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_37
    key_resp_37.keys = []
    key_resp_37.rt = []
    _key_resp_37_allKeys = []
    # store start times for reminder_I1
    reminder_I1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_I1.tStart = globalClock.getTime(format='float')
    reminder_I1.status = STARTED
    thisExp.addData('reminder_I1.started', reminder_I1.tStart)
    reminder_I1.maxDuration = None
    # keep track of which components have finished
    reminder_I1Components = reminder_I1.components
    for thisComponent in reminder_I1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_I1" ---
    reminder_I1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_58* updates
        
        # if text_58 is starting this frame...
        if text_58.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_58.frameNStart = frameN  # exact frame index
            text_58.tStart = t  # local t and not account for scr refresh
            text_58.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_58, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_58.started')
            # update status
            text_58.status = STARTED
            text_58.setAutoDraw(True)
        
        # if text_58 is active this frame...
        if text_58.status == STARTED:
            # update params
            pass
        
        # *key_resp_37* updates
        waitOnFlip = False
        
        # if key_resp_37 is starting this frame...
        if key_resp_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_37.frameNStart = frameN  # exact frame index
            key_resp_37.tStart = t  # local t and not account for scr refresh
            key_resp_37.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_37, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_37.started')
            # update status
            key_resp_37.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_37.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_37.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_37.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_37.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_37_allKeys.extend(theseKeys)
            if len(_key_resp_37_allKeys):
                key_resp_37.keys = _key_resp_37_allKeys[-1].name  # just the last key pressed
                key_resp_37.rt = _key_resp_37_allKeys[-1].rt
                key_resp_37.duration = _key_resp_37_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_I1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_I1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_I1" ---
    for thisComponent in reminder_I1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_I1
    reminder_I1.tStop = globalClock.getTime(format='float')
    reminder_I1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_I1.stopped', reminder_I1.tStop)
    # check responses
    if key_resp_37.keys in ['', [], None]:  # No response was made
        key_resp_37.keys = None
    thisExp.addData('key_resp_37.keys',key_resp_37.keys)
    if key_resp_37.keys != None:  # we had a response
        thisExp.addData('key_resp_37.rt', key_resp_37.rt)
        thisExp.addData('key_resp_37.duration', key_resp_37.duration)
    thisExp.nextEntry()
    # the Routine "reminder_I1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_17 = data.TrialHandler2(
        name='trials_17',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskG2_I1_block1st3rd_congruent_japan_prefer.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_17)  # add the loop to the experiment
    thisTrial_17 = trials_17.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
    if thisTrial_17 != None:
        for paramName in thisTrial_17:
            globals()[paramName] = thisTrial_17[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_17 in trials_17:
        currentLoop = trials_17
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
        if thisTrial_17 != None:
            for paramName in thisTrial_17:
                globals()[paramName] = thisTrial_17[paramName]
        
        # --- Prepare to start Routine "practice_Task_I1" ---
        # create an object to store info about Routine practice_Task_I1
        practice_Task_I1 = data.Routine(
            name='practice_Task_I1',
            components=[text_I1, key_resp_I1],
        )
        practice_Task_I1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_I1.setText(words)
        # create starting attributes for key_resp_I1
        key_resp_I1.keys = []
        key_resp_I1.rt = []
        _key_resp_I1_allKeys = []
        # store start times for practice_Task_I1
        practice_Task_I1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_Task_I1.tStart = globalClock.getTime(format='float')
        practice_Task_I1.status = STARTED
        thisExp.addData('practice_Task_I1.started', practice_Task_I1.tStart)
        practice_Task_I1.maxDuration = None
        # keep track of which components have finished
        practice_Task_I1Components = practice_Task_I1.components
        for thisComponent in practice_Task_I1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_Task_I1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_17, data.TrialHandler2) and thisTrial_17.thisN != trials_17.thisTrial.thisN:
            continueRoutine = False
        practice_Task_I1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_I1* updates
            
            # if text_I1 is starting this frame...
            if text_I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_I1.frameNStart = frameN  # exact frame index
                text_I1.tStart = t  # local t and not account for scr refresh
                text_I1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_I1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_I1.started')
                # update status
                text_I1.status = STARTED
                text_I1.setAutoDraw(True)
            
            # if text_I1 is active this frame...
            if text_I1.status == STARTED:
                # update params
                pass
            
            # *key_resp_I1* updates
            waitOnFlip = False
            
            # if key_resp_I1 is starting this frame...
            if key_resp_I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_I1.frameNStart = frameN  # exact frame index
                key_resp_I1.tStart = t  # local t and not account for scr refresh
                key_resp_I1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_I1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_I1.started')
                # update status
                key_resp_I1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_I1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_I1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_I1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_I1.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_I1_allKeys.extend(theseKeys)
                if len(_key_resp_I1_allKeys):
                    key_resp_I1.keys = _key_resp_I1_allKeys[-1].name  # just the last key pressed
                    key_resp_I1.rt = _key_resp_I1_allKeys[-1].rt
                    key_resp_I1.duration = _key_resp_I1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_I1.keys == str(keypad)) or (key_resp_I1.keys == keypad):
                        key_resp_I1.corr = 1
                    else:
                        key_resp_I1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practice_Task_I1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_Task_I1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_Task_I1" ---
        for thisComponent in practice_Task_I1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_Task_I1
        practice_Task_I1.tStop = globalClock.getTime(format='float')
        practice_Task_I1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_Task_I1.stopped', practice_Task_I1.tStop)
        # check responses
        if key_resp_I1.keys in ['', [], None]:  # No response was made
            key_resp_I1.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_I1.corr = 1;  # correct non-response
            else:
               key_resp_I1.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_17 (TrialHandler)
        trials_17.addData('key_resp_I1.keys',key_resp_I1.keys)
        trials_17.addData('key_resp_I1.corr', key_resp_I1.corr)
        if key_resp_I1.keys != None:  # we had a response
            trials_17.addData('key_resp_I1.rt', key_resp_I1.rt)
            trials_17.addData('key_resp_I1.duration', key_resp_I1.duration)
        # the Routine "practice_Task_I1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_I1" ---
        # create an object to store info about Routine feedback_I1
        feedback_I1 = data.Routine(
            name='feedback_I1',
            components=[feedback_text_I1],
        )
        feedback_I1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_I1
        key_resp_I1_rt_sum_temp = key_resp_I1_rt_sum_temp + float(str(key_resp_I1.rt))
        
        if key_resp_I1.corr:
            key_resp_I1_corr_sum_temp =key_resp_I1_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_I1.setText(msg)
        # store start times for feedback_I1
        feedback_I1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_I1.tStart = globalClock.getTime(format='float')
        feedback_I1.status = STARTED
        thisExp.addData('feedback_I1.started', feedback_I1.tStart)
        feedback_I1.maxDuration = None
        # keep track of which components have finished
        feedback_I1Components = feedback_I1.components
        for thisComponent in feedback_I1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_I1" ---
        # if trial has changed, end Routine now
        if isinstance(trials_17, data.TrialHandler2) and thisTrial_17.thisN != trials_17.thisTrial.thisN:
            continueRoutine = False
        feedback_I1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_I1* updates
            
            # if feedback_text_I1 is starting this frame...
            if feedback_text_I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_I1.frameNStart = frameN  # exact frame index
                feedback_text_I1.tStart = t  # local t and not account for scr refresh
                feedback_text_I1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_I1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_I1.started')
                # update status
                feedback_text_I1.status = STARTED
                feedback_text_I1.setAutoDraw(True)
            
            # if feedback_text_I1 is active this frame...
            if feedback_text_I1.status == STARTED:
                # update params
                pass
            
            # if feedback_text_I1 is stopping this frame...
            if feedback_text_I1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_I1.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_I1.tStop = t  # not accounting for scr refresh
                    feedback_text_I1.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_I1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_I1.stopped')
                    # update status
                    feedback_text_I1.status = FINISHED
                    feedback_text_I1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_I1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_I1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_I1" ---
        for thisComponent in feedback_I1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_I1
        feedback_I1.tStop = globalClock.getTime(format='float')
        feedback_I1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_I1.stopped', feedback_I1.tStop)
        # Run 'End Routine' code from code_I1
        key_resp_I1_corr_sum = key_resp_I1_corr_sum_temp
        key_resp_I1_rt_sum = key_resp_I1_rt_sum_temp
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_I1.maxDurationReached:
            routineTimer.addTime(-feedback_I1.maxDuration)
        elif feedback_I1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_17, data.TrialHandler2) and thisTrial_17.thisN != trials_17.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_17'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_I1" ---
    # create an object to store info about Routine score_I1
    score_I1 = data.Routine(
        name='score_I1',
        components=[score_I1_text, key_resp_18],
    )
    score_I1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_I1_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_I1_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_I1_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_18
    key_resp_18.keys = []
    key_resp_18.rt = []
    _key_resp_18_allKeys = []
    # store start times for score_I1
    score_I1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_I1.tStart = globalClock.getTime(format='float')
    score_I1.status = STARTED
    thisExp.addData('score_I1.started', score_I1.tStart)
    score_I1.maxDuration = None
    # keep track of which components have finished
    score_I1Components = score_I1.components
    for thisComponent in score_I1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_I1" ---
    score_I1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_I1_text* updates
        
        # if score_I1_text is starting this frame...
        if score_I1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_I1_text.frameNStart = frameN  # exact frame index
            score_I1_text.tStart = t  # local t and not account for scr refresh
            score_I1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_I1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_I1_text.started')
            # update status
            score_I1_text.status = STARTED
            score_I1_text.setAutoDraw(True)
        
        # if score_I1_text is active this frame...
        if score_I1_text.status == STARTED:
            # update params
            score_I1_text.setText(feedback_msg, log=False)
        
        # *key_resp_18* updates
        waitOnFlip = False
        
        # if key_resp_18 is starting this frame...
        if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_18.frameNStart = frameN  # exact frame index
            key_resp_18.tStart = t  # local t and not account for scr refresh
            key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_18.started')
            # update status
            key_resp_18.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_18.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_18.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_18_allKeys.extend(theseKeys)
            if len(_key_resp_18_allKeys):
                key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                key_resp_18.rt = _key_resp_18_allKeys[-1].rt
                key_resp_18.duration = _key_resp_18_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_I1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_I1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_I1" ---
    for thisComponent in score_I1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_I1
    score_I1.tStop = globalClock.getTime(format='float')
    score_I1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_I1.stopped', score_I1.tStop)
    # check responses
    if key_resp_18.keys in ['', [], None]:  # No response was made
        key_resp_18.keys = None
    thisExp.addData('key_resp_18.keys',key_resp_18.keys)
    if key_resp_18.keys != None:  # we had a response
        thisExp.addData('key_resp_18.rt', key_resp_18.rt)
        thisExp.addData('key_resp_18.duration', key_resp_18.duration)
    thisExp.nextEntry()
    # the Routine "score_I1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_I2" ---
    # create an object to store info about Routine reminder_I2
    reminder_I2 = data.Routine(
        name='reminder_I2',
        components=[text_59, key_resp_38],
    )
    reminder_I2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_38
    key_resp_38.keys = []
    key_resp_38.rt = []
    _key_resp_38_allKeys = []
    # store start times for reminder_I2
    reminder_I2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_I2.tStart = globalClock.getTime(format='float')
    reminder_I2.status = STARTED
    thisExp.addData('reminder_I2.started', reminder_I2.tStart)
    reminder_I2.maxDuration = None
    # keep track of which components have finished
    reminder_I2Components = reminder_I2.components
    for thisComponent in reminder_I2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_I2" ---
    reminder_I2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_59* updates
        
        # if text_59 is starting this frame...
        if text_59.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_59.frameNStart = frameN  # exact frame index
            text_59.tStart = t  # local t and not account for scr refresh
            text_59.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_59, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_59.started')
            # update status
            text_59.status = STARTED
            text_59.setAutoDraw(True)
        
        # if text_59 is active this frame...
        if text_59.status == STARTED:
            # update params
            pass
        
        # *key_resp_38* updates
        waitOnFlip = False
        
        # if key_resp_38 is starting this frame...
        if key_resp_38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_38.frameNStart = frameN  # exact frame index
            key_resp_38.tStart = t  # local t and not account for scr refresh
            key_resp_38.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_38, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_38.started')
            # update status
            key_resp_38.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_38.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_38.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_38.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_38.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_38_allKeys.extend(theseKeys)
            if len(_key_resp_38_allKeys):
                key_resp_38.keys = _key_resp_38_allKeys[-1].name  # just the last key pressed
                key_resp_38.rt = _key_resp_38_allKeys[-1].rt
                key_resp_38.duration = _key_resp_38_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_I2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_I2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_I2" ---
    for thisComponent in reminder_I2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_I2
    reminder_I2.tStop = globalClock.getTime(format='float')
    reminder_I2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_I2.stopped', reminder_I2.tStop)
    # check responses
    if key_resp_38.keys in ['', [], None]:  # No response was made
        key_resp_38.keys = None
    thisExp.addData('key_resp_38.keys',key_resp_38.keys)
    if key_resp_38.keys != None:  # we had a response
        thisExp.addData('key_resp_38.rt', key_resp_38.rt)
        thisExp.addData('key_resp_38.duration', key_resp_38.duration)
    thisExp.nextEntry()
    # the Routine "reminder_I2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_18 = data.TrialHandler2(
        name='trials_18',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskG2_I1_block2nd_congruent_japan_prefer.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_18)  # add the loop to the experiment
    thisTrial_18 = trials_18.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
    if thisTrial_18 != None:
        for paramName in thisTrial_18:
            globals()[paramName] = thisTrial_18[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_18 in trials_18:
        currentLoop = trials_18
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
        if thisTrial_18 != None:
            for paramName in thisTrial_18:
                globals()[paramName] = thisTrial_18[paramName]
        
        # --- Prepare to start Routine "record_Task_I2" ---
        # create an object to store info about Routine record_Task_I2
        record_Task_I2 = data.Routine(
            name='record_Task_I2',
            components=[text_I2, key_resp_I2],
        )
        record_Task_I2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_I2.setText(words)
        # create starting attributes for key_resp_I2
        key_resp_I2.keys = []
        key_resp_I2.rt = []
        _key_resp_I2_allKeys = []
        # store start times for record_Task_I2
        record_Task_I2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        record_Task_I2.tStart = globalClock.getTime(format='float')
        record_Task_I2.status = STARTED
        thisExp.addData('record_Task_I2.started', record_Task_I2.tStart)
        record_Task_I2.maxDuration = None
        # keep track of which components have finished
        record_Task_I2Components = record_Task_I2.components
        for thisComponent in record_Task_I2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "record_Task_I2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_18, data.TrialHandler2) and thisTrial_18.thisN != trials_18.thisTrial.thisN:
            continueRoutine = False
        record_Task_I2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_I2* updates
            
            # if text_I2 is starting this frame...
            if text_I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_I2.frameNStart = frameN  # exact frame index
                text_I2.tStart = t  # local t and not account for scr refresh
                text_I2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_I2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_I2.started')
                # update status
                text_I2.status = STARTED
                text_I2.setAutoDraw(True)
            
            # if text_I2 is active this frame...
            if text_I2.status == STARTED:
                # update params
                pass
            
            # *key_resp_I2* updates
            waitOnFlip = False
            
            # if key_resp_I2 is starting this frame...
            if key_resp_I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_I2.frameNStart = frameN  # exact frame index
                key_resp_I2.tStart = t  # local t and not account for scr refresh
                key_resp_I2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_I2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_I2.started')
                # update status
                key_resp_I2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_I2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_I2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_I2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_I2.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_I2_allKeys.extend(theseKeys)
                if len(_key_resp_I2_allKeys):
                    key_resp_I2.keys = _key_resp_I2_allKeys[-1].name  # just the last key pressed
                    key_resp_I2.rt = _key_resp_I2_allKeys[-1].rt
                    key_resp_I2.duration = _key_resp_I2_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_I2.keys == str(keypad)) or (key_resp_I2.keys == keypad):
                        key_resp_I2.corr = 1
                    else:
                        key_resp_I2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                record_Task_I2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_Task_I2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "record_Task_I2" ---
        for thisComponent in record_Task_I2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for record_Task_I2
        record_Task_I2.tStop = globalClock.getTime(format='float')
        record_Task_I2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('record_Task_I2.stopped', record_Task_I2.tStop)
        # check responses
        if key_resp_I2.keys in ['', [], None]:  # No response was made
            key_resp_I2.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_I2.corr = 1;  # correct non-response
            else:
               key_resp_I2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_18 (TrialHandler)
        trials_18.addData('key_resp_I2.keys',key_resp_I2.keys)
        trials_18.addData('key_resp_I2.corr', key_resp_I2.corr)
        if key_resp_I2.keys != None:  # we had a response
            trials_18.addData('key_resp_I2.rt', key_resp_I2.rt)
            trials_18.addData('key_resp_I2.duration', key_resp_I2.duration)
        # the Routine "record_Task_I2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_I2" ---
        # create an object to store info about Routine feedback_I2
        feedback_I2 = data.Routine(
            name='feedback_I2',
            components=[feedback_text_I2],
        )
        feedback_I2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_I2
        key_resp_I2_rt_sum_temp = key_resp_I2_rt_sum_temp + float(str(key_resp_I2.rt))
        
        if key_resp_I2.corr:
            key_resp_I2_corr_sum_temp =key_resp_I2_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_I2.setText(msg)
        # store start times for feedback_I2
        feedback_I2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_I2.tStart = globalClock.getTime(format='float')
        feedback_I2.status = STARTED
        thisExp.addData('feedback_I2.started', feedback_I2.tStart)
        feedback_I2.maxDuration = None
        # keep track of which components have finished
        feedback_I2Components = feedback_I2.components
        for thisComponent in feedback_I2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_I2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_18, data.TrialHandler2) and thisTrial_18.thisN != trials_18.thisTrial.thisN:
            continueRoutine = False
        feedback_I2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_I2* updates
            
            # if feedback_text_I2 is starting this frame...
            if feedback_text_I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_I2.frameNStart = frameN  # exact frame index
                feedback_text_I2.tStart = t  # local t and not account for scr refresh
                feedback_text_I2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_I2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_I2.started')
                # update status
                feedback_text_I2.status = STARTED
                feedback_text_I2.setAutoDraw(True)
            
            # if feedback_text_I2 is active this frame...
            if feedback_text_I2.status == STARTED:
                # update params
                pass
            
            # if feedback_text_I2 is stopping this frame...
            if feedback_text_I2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_I2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_I2.tStop = t  # not accounting for scr refresh
                    feedback_text_I2.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_I2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_I2.stopped')
                    # update status
                    feedback_text_I2.status = FINISHED
                    feedback_text_I2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_I2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_I2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_I2" ---
        for thisComponent in feedback_I2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_I2
        feedback_I2.tStop = globalClock.getTime(format='float')
        feedback_I2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_I2.stopped', feedback_I2.tStop)
        # Run 'End Routine' code from code_I2
        key_resp_I2_corr_sum = key_resp_I2_corr_sum_temp
        key_resp_I2_rt_sum = key_resp_I2_rt_sum_temp
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_I2.maxDurationReached:
            routineTimer.addTime(-feedback_I2.maxDuration)
        elif feedback_I2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_18, data.TrialHandler2) and thisTrial_18.thisN != trials_18.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_18'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_I2" ---
    # create an object to store info about Routine score_I2
    score_I2 = data.Routine(
        name='score_I2',
        components=[score_I2_text, key_resp_20],
    )
    score_I2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_I2_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_I2_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_I2_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_20
    key_resp_20.keys = []
    key_resp_20.rt = []
    _key_resp_20_allKeys = []
    # store start times for score_I2
    score_I2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_I2.tStart = globalClock.getTime(format='float')
    score_I2.status = STARTED
    thisExp.addData('score_I2.started', score_I2.tStart)
    score_I2.maxDuration = None
    # keep track of which components have finished
    score_I2Components = score_I2.components
    for thisComponent in score_I2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_I2" ---
    score_I2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_I2_text* updates
        
        # if score_I2_text is starting this frame...
        if score_I2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_I2_text.frameNStart = frameN  # exact frame index
            score_I2_text.tStart = t  # local t and not account for scr refresh
            score_I2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_I2_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_I2_text.started')
            # update status
            score_I2_text.status = STARTED
            score_I2_text.setAutoDraw(True)
        
        # if score_I2_text is active this frame...
        if score_I2_text.status == STARTED:
            # update params
            score_I2_text.setText(feedback_msg, log=False)
        
        # *key_resp_20* updates
        waitOnFlip = False
        
        # if key_resp_20 is starting this frame...
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_20.started')
            # update status
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_20_allKeys.extend(theseKeys)
            if len(_key_resp_20_allKeys):
                key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
                key_resp_20.rt = _key_resp_20_allKeys[-1].rt
                key_resp_20.duration = _key_resp_20_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_I2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_I2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_I2" ---
    for thisComponent in score_I2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_I2
    score_I2.tStop = globalClock.getTime(format='float')
    score_I2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_I2.stopped', score_I2.tStop)
    # check responses
    if key_resp_20.keys in ['', [], None]:  # No response was made
        key_resp_20.keys = None
    thisExp.addData('key_resp_20.keys',key_resp_20.keys)
    if key_resp_20.keys != None:  # we had a response
        thisExp.addData('key_resp_20.rt', key_resp_20.rt)
        thisExp.addData('key_resp_20.duration', key_resp_20.duration)
    thisExp.nextEntry()
    # the Routine "score_I2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_I3" ---
    # create an object to store info about Routine reminder_I3
    reminder_I3 = data.Routine(
        name='reminder_I3',
        components=[text_60, key_resp_39],
    )
    reminder_I3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_39
    key_resp_39.keys = []
    key_resp_39.rt = []
    _key_resp_39_allKeys = []
    # store start times for reminder_I3
    reminder_I3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reminder_I3.tStart = globalClock.getTime(format='float')
    reminder_I3.status = STARTED
    thisExp.addData('reminder_I3.started', reminder_I3.tStart)
    reminder_I3.maxDuration = None
    # keep track of which components have finished
    reminder_I3Components = reminder_I3.components
    for thisComponent in reminder_I3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reminder_I3" ---
    reminder_I3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_60* updates
        
        # if text_60 is starting this frame...
        if text_60.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_60.frameNStart = frameN  # exact frame index
            text_60.tStart = t  # local t and not account for scr refresh
            text_60.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_60, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_60.started')
            # update status
            text_60.status = STARTED
            text_60.setAutoDraw(True)
        
        # if text_60 is active this frame...
        if text_60.status == STARTED:
            # update params
            pass
        
        # *key_resp_39* updates
        waitOnFlip = False
        
        # if key_resp_39 is starting this frame...
        if key_resp_39.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_39.frameNStart = frameN  # exact frame index
            key_resp_39.tStart = t  # local t and not account for scr refresh
            key_resp_39.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_39, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_39.started')
            # update status
            key_resp_39.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_39.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_39.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_39.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_39.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_39_allKeys.extend(theseKeys)
            if len(_key_resp_39_allKeys):
                key_resp_39.keys = _key_resp_39_allKeys[-1].name  # just the last key pressed
                key_resp_39.rt = _key_resp_39_allKeys[-1].rt
                key_resp_39.duration = _key_resp_39_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            reminder_I3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_I3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_I3" ---
    for thisComponent in reminder_I3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reminder_I3
    reminder_I3.tStop = globalClock.getTime(format='float')
    reminder_I3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reminder_I3.stopped', reminder_I3.tStop)
    # check responses
    if key_resp_39.keys in ['', [], None]:  # No response was made
        key_resp_39.keys = None
    thisExp.addData('key_resp_39.keys',key_resp_39.keys)
    if key_resp_39.keys != None:  # we had a response
        thisExp.addData('key_resp_39.rt', key_resp_39.rt)
        thisExp.addData('key_resp_39.duration', key_resp_39.duration)
    thisExp.nextEntry()
    # the Routine "reminder_I3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI1500" ---
    # create an object to store info about Routine ISI1500
    ISI1500 = data.Routine(
        name='ISI1500',
        components=[text_3],
    )
    ISI1500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ISI1500
    ISI1500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI1500.tStart = globalClock.getTime(format='float')
    ISI1500.status = STARTED
    thisExp.addData('ISI1500.started', ISI1500.tStart)
    ISI1500.maxDuration = 1.5
    # keep track of which components have finished
    ISI1500Components = ISI1500.components
    for thisComponent in ISI1500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI1500" ---
    ISI1500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ISI1500.maxDuration-frameTolerance:
            ISI1500.maxDurationReached = True
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI1500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI1500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI1500" ---
    for thisComponent in ISI1500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI1500
    ISI1500.tStop = globalClock.getTime(format='float')
    ISI1500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI1500.stopped', ISI1500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI1500.maxDurationReached:
        routineTimer.addTime(-ISI1500.maxDuration)
    elif ISI1500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_19 = data.TrialHandler2(
        name='trials_19',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('excel/TaskG2_I1_block1st3rd_congruent_japan_prefer.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_19)  # add the loop to the experiment
    thisTrial_19 = trials_19.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
    if thisTrial_19 != None:
        for paramName in thisTrial_19:
            globals()[paramName] = thisTrial_19[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_19 in trials_19:
        currentLoop = trials_19
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
        if thisTrial_19 != None:
            for paramName in thisTrial_19:
                globals()[paramName] = thisTrial_19[paramName]
        
        # --- Prepare to start Routine "record_Task_I3" ---
        # create an object to store info about Routine record_Task_I3
        record_Task_I3 = data.Routine(
            name='record_Task_I3',
            components=[text_I3, key_resp_I3],
        )
        record_Task_I3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_I3.setText(words)
        # create starting attributes for key_resp_I3
        key_resp_I3.keys = []
        key_resp_I3.rt = []
        _key_resp_I3_allKeys = []
        # store start times for record_Task_I3
        record_Task_I3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        record_Task_I3.tStart = globalClock.getTime(format='float')
        record_Task_I3.status = STARTED
        thisExp.addData('record_Task_I3.started', record_Task_I3.tStart)
        record_Task_I3.maxDuration = None
        # keep track of which components have finished
        record_Task_I3Components = record_Task_I3.components
        for thisComponent in record_Task_I3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "record_Task_I3" ---
        # if trial has changed, end Routine now
        if isinstance(trials_19, data.TrialHandler2) and thisTrial_19.thisN != trials_19.thisTrial.thisN:
            continueRoutine = False
        record_Task_I3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_I3* updates
            
            # if text_I3 is starting this frame...
            if text_I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_I3.frameNStart = frameN  # exact frame index
                text_I3.tStart = t  # local t and not account for scr refresh
                text_I3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_I3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_I3.started')
                # update status
                text_I3.status = STARTED
                text_I3.setAutoDraw(True)
            
            # if text_I3 is active this frame...
            if text_I3.status == STARTED:
                # update params
                pass
            
            # *key_resp_I3* updates
            waitOnFlip = False
            
            # if key_resp_I3 is starting this frame...
            if key_resp_I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_I3.frameNStart = frameN  # exact frame index
                key_resp_I3.tStart = t  # local t and not account for scr refresh
                key_resp_I3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_I3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_I3.started')
                # update status
                key_resp_I3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_I3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_I3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_I3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_I3.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_I3_allKeys.extend(theseKeys)
                if len(_key_resp_I3_allKeys):
                    key_resp_I3.keys = _key_resp_I3_allKeys[-1].name  # just the last key pressed
                    key_resp_I3.rt = _key_resp_I3_allKeys[-1].rt
                    key_resp_I3.duration = _key_resp_I3_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_I3.keys == str(keypad)) or (key_resp_I3.keys == keypad):
                        key_resp_I3.corr = 1
                    else:
                        key_resp_I3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                record_Task_I3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_Task_I3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "record_Task_I3" ---
        for thisComponent in record_Task_I3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for record_Task_I3
        record_Task_I3.tStop = globalClock.getTime(format='float')
        record_Task_I3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('record_Task_I3.stopped', record_Task_I3.tStop)
        # check responses
        if key_resp_I3.keys in ['', [], None]:  # No response was made
            key_resp_I3.keys = None
            # was no response the correct answer?!
            if str(keypad).lower() == 'none':
               key_resp_I3.corr = 1;  # correct non-response
            else:
               key_resp_I3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_19 (TrialHandler)
        trials_19.addData('key_resp_I3.keys',key_resp_I3.keys)
        trials_19.addData('key_resp_I3.corr', key_resp_I3.corr)
        if key_resp_I3.keys != None:  # we had a response
            trials_19.addData('key_resp_I3.rt', key_resp_I3.rt)
            trials_19.addData('key_resp_I3.duration', key_resp_I3.duration)
        # the Routine "record_Task_I3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback_I3" ---
        # create an object to store info about Routine feedback_I3
        feedback_I3 = data.Routine(
            name='feedback_I3',
            components=[feedback_text_I3],
        )
        feedback_I3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_I3
        key_resp_I3_rt_sum_temp = key_resp_I3_rt_sum_temp + float(str(key_resp_I3.rt))
        
        if key_resp_I3.corr:
            key_resp_I3_corr_sum_temp =key_resp_I3_corr_sum_temp +1
            continueRoutine = False
        else:
            msg = 'error'
        feedback_text_I3.setText(msg)
        # store start times for feedback_I3
        feedback_I3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_I3.tStart = globalClock.getTime(format='float')
        feedback_I3.status = STARTED
        thisExp.addData('feedback_I3.started', feedback_I3.tStart)
        feedback_I3.maxDuration = None
        # keep track of which components have finished
        feedback_I3Components = feedback_I3.components
        for thisComponent in feedback_I3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_I3" ---
        # if trial has changed, end Routine now
        if isinstance(trials_19, data.TrialHandler2) and thisTrial_19.thisN != trials_19.thisTrial.thisN:
            continueRoutine = False
        feedback_I3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_I3* updates
            
            # if feedback_text_I3 is starting this frame...
            if feedback_text_I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_I3.frameNStart = frameN  # exact frame index
                feedback_text_I3.tStart = t  # local t and not account for scr refresh
                feedback_text_I3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_I3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_I3.started')
                # update status
                feedback_text_I3.status = STARTED
                feedback_text_I3.setAutoDraw(True)
            
            # if feedback_text_I3 is active this frame...
            if feedback_text_I3.status == STARTED:
                # update params
                pass
            
            # if feedback_text_I3 is stopping this frame...
            if feedback_text_I3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_I3.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_I3.tStop = t  # not accounting for scr refresh
                    feedback_text_I3.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text_I3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_I3.stopped')
                    # update status
                    feedback_text_I3.status = FINISHED
                    feedback_text_I3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_I3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_I3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_I3" ---
        for thisComponent in feedback_I3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_I3
        feedback_I3.tStop = globalClock.getTime(format='float')
        feedback_I3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_I3.stopped', feedback_I3.tStop)
        # Run 'End Routine' code from code_I3
        key_resp_I3_corr_sum = key_resp_I3_corr_sum_temp
        key_resp_I3_rt_sum = key_resp_I3_rt_sum_temp
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_I3.maxDurationReached:
            routineTimer.addTime(-feedback_I3.maxDuration)
        elif feedback_I3.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "ISI250" ---
        # create an object to store info about Routine ISI250
        ISI250 = data.Routine(
            name='ISI250',
            components=[],
        )
        ISI250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ISI250
        ISI250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ISI250.tStart = globalClock.getTime(format='float')
        ISI250.status = STARTED
        thisExp.addData('ISI250.started', ISI250.tStart)
        ISI250.maxDuration = 0.25
        # keep track of which components have finished
        ISI250Components = ISI250.components
        for thisComponent in ISI250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI250" ---
        # if trial has changed, end Routine now
        if isinstance(trials_19, data.TrialHandler2) and thisTrial_19.thisN != trials_19.thisTrial.thisN:
            continueRoutine = False
        ISI250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ISI250.maxDuration-frameTolerance:
                ISI250.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ISI250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI250" ---
        for thisComponent in ISI250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ISI250
        ISI250.tStop = globalClock.getTime(format='float')
        ISI250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ISI250.stopped', ISI250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ISI250.maxDurationReached:
            routineTimer.addTime(-ISI250.maxDuration)
        elif ISI250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_19'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "score_I3" ---
    # create an object to store info about Routine score_I3
    score_I3 = data.Routine(
        name='score_I3',
        components=[score_I3_text, key_resp_21],
    )
    score_I3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from score_I3_code
    feedback_msg ="" 
    
    accuracy = round((key_resp_I3_corr_sum / 50) * 100, 2)  
    rt_average = round((key_resp_I3_rt_sum / 50) * 1000, 2)  
    
    feedback_msg += "Accuracy: " + str(accuracy) + "%\n"  
    feedback_msg += "RT Average: " + str(rt_average) + " ms\n"  
    feedback_msg += "Press space bar to continue."
    # create starting attributes for key_resp_21
    key_resp_21.keys = []
    key_resp_21.rt = []
    _key_resp_21_allKeys = []
    # store start times for score_I3
    score_I3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    score_I3.tStart = globalClock.getTime(format='float')
    score_I3.status = STARTED
    thisExp.addData('score_I3.started', score_I3.tStart)
    score_I3.maxDuration = None
    # keep track of which components have finished
    score_I3Components = score_I3.components
    for thisComponent in score_I3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "score_I3" ---
    score_I3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_I3_text* updates
        
        # if score_I3_text is starting this frame...
        if score_I3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            score_I3_text.frameNStart = frameN  # exact frame index
            score_I3_text.tStart = t  # local t and not account for scr refresh
            score_I3_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(score_I3_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'score_I3_text.started')
            # update status
            score_I3_text.status = STARTED
            score_I3_text.setAutoDraw(True)
        
        # if score_I3_text is active this frame...
        if score_I3_text.status == STARTED:
            # update params
            score_I3_text.setText(feedback_msg, log=False)
        
        # *key_resp_21* updates
        waitOnFlip = False
        
        # if key_resp_21 is starting this frame...
        if key_resp_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_21.frameNStart = frameN  # exact frame index
            key_resp_21.tStart = t  # local t and not account for scr refresh
            key_resp_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_21.started')
            # update status
            key_resp_21.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_21.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_21.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_21_allKeys.extend(theseKeys)
            if len(_key_resp_21_allKeys):
                key_resp_21.keys = _key_resp_21_allKeys[-1].name  # just the last key pressed
                key_resp_21.rt = _key_resp_21_allKeys[-1].rt
                key_resp_21.duration = _key_resp_21_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            score_I3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in score_I3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score_I3" ---
    for thisComponent in score_I3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for score_I3
    score_I3.tStop = globalClock.getTime(format='float')
    score_I3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('score_I3.stopped', score_I3.tStop)
    # check responses
    if key_resp_21.keys in ['', [], None]:  # No response was made
        key_resp_21.keys = None
    thisExp.addData('key_resp_21.keys',key_resp_21.keys)
    if key_resp_21.keys != None:  # we had a response
        thisExp.addData('key_resp_21.rt', key_resp_21.rt)
        thisExp.addData('key_resp_21.duration', key_resp_21.duration)
    thisExp.nextEntry()
    # the Routine "score_I3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)
    # end 'rush' mode
    core.rush(enable=False)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
