/************ 
 * Iat *
 ************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'IAT';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from code_A1
key_resp_A1_corr_sum = 0.0;
key_resp_A1_rt_sum = 0.0;

// Run 'Before Experiment' code from code_A2
key_resp_A2_corr_sum = 0.0;
key_resp_A2_rt_sum = 0.0;

// Run 'Before Experiment' code from code_B1
key_resp_B1_corr_sum = 0.0;
key_resp_B1_rt_sum = 0.0;

// Run 'Before Experiment' code from code_B2
key_resp_B2_corr_sum = 0.0;
key_resp_B2_rt_sum = 0.0;

// Run 'Before Experiment' code from code_C1
key_resp_C1_corr_sum = 0.0;
key_resp_C1_rt_sum = 0.0;

// Run 'Before Experiment' code from code_C2
key_resp_C2_corr_sum = 0.0;
key_resp_C2_rt_sum = 0.0;

// Run 'Before Experiment' code from code_C3
key_resp_C3_corr_sum = 0.0;
key_resp_C3_rt_sum = 0.0;

// Run 'Before Experiment' code from code_D1
key_resp_D1_corr_sum = 0.0;
key_resp_D1_rt_sum = 0.0;

// Run 'Before Experiment' code from code_E1
key_resp_E1_corr_sum = 0.0;
key_resp_E1_rt_sum = 0.0;

// Run 'Before Experiment' code from code_E2
key_resp_E2_corr_sum = 0.0;
key_resp_E2_rt_sum = 0.0;

// Run 'Before Experiment' code from code_E3
key_resp_E3_corr_sum = 0.0;
key_resp_E3_rt_sum = 0.0;

// Run 'Before Experiment' code from code_F1
key_resp_F1_corr_sum = 0.0;
key_resp_F1_rt_sum = 0.0;

// Run 'Before Experiment' code from code_G1
key_resp_G1_corr_sum = 0.0;
key_resp_G1_rt_sum = 0.0;

// Run 'Before Experiment' code from code_G2
key_resp_G2_corr_sum = 0.0;
key_resp_G2_rt_sum = 0.0;

// Run 'Before Experiment' code from code_G3
key_resp_G3_corr_sum = 0.0;
key_resp_G3_rt_sum = 0.0;

// Run 'Before Experiment' code from code_H1
key_resp_H1_corr_sum = 0.0;
key_resp_H1_rt_sum = 0.0;

// Run 'Before Experiment' code from code_I1
key_resp_I1_corr_sum = 0.0;
key_resp_I1_rt_sum = 0.0;

// Run 'Before Experiment' code from code_I2
key_resp_I2_corr_sum = 0.0;
key_resp_I2_rt_sum = 0.0;

// Run 'Before Experiment' code from code_I3
key_resp_I3_corr_sum = 0.0;
key_resp_I3_rt_sum = 0.0;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.6549, 0.6549, 0.6549]),
  units: 'pix',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(IntroductionRoutineBegin());
flowScheduler.add(IntroductionRoutineEachFrame());
flowScheduler.add(IntroductionRoutineEnd());
const trials_20LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_20LoopBegin(trials_20LoopScheduler));
flowScheduler.add(trials_20LoopScheduler);
flowScheduler.add(trials_20LoopEnd);

























































flowScheduler.add(reminder_D1RoutineBegin());
flowScheduler.add(reminder_D1RoutineEachFrame());
flowScheduler.add(reminder_D1RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_8LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_8LoopBegin(trials_8LoopScheduler));
flowScheduler.add(trials_8LoopScheduler);
flowScheduler.add(trials_8LoopEnd);




flowScheduler.add(score_D1RoutineBegin());
flowScheduler.add(score_D1RoutineEachFrame());
flowScheduler.add(score_D1RoutineEnd());
flowScheduler.add(reminder_E1RoutineBegin());
flowScheduler.add(reminder_E1RoutineEachFrame());
flowScheduler.add(reminder_E1RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_9LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_9LoopBegin(trials_9LoopScheduler));
flowScheduler.add(trials_9LoopScheduler);
flowScheduler.add(trials_9LoopEnd);




flowScheduler.add(score_E1RoutineBegin());
flowScheduler.add(score_E1RoutineEachFrame());
flowScheduler.add(score_E1RoutineEnd());
flowScheduler.add(reminder_E2RoutineBegin());
flowScheduler.add(reminder_E2RoutineEachFrame());
flowScheduler.add(reminder_E2RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_10LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_10LoopBegin(trials_10LoopScheduler));
flowScheduler.add(trials_10LoopScheduler);
flowScheduler.add(trials_10LoopEnd);




flowScheduler.add(score_E2RoutineBegin());
flowScheduler.add(score_E2RoutineEachFrame());
flowScheduler.add(score_E2RoutineEnd());
flowScheduler.add(reminder_E3RoutineBegin());
flowScheduler.add(reminder_E3RoutineEachFrame());
flowScheduler.add(reminder_E3RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_11LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_11LoopBegin(trials_11LoopScheduler));
flowScheduler.add(trials_11LoopScheduler);
flowScheduler.add(trials_11LoopEnd);




flowScheduler.add(score_E3RoutineBegin());
flowScheduler.add(score_E3RoutineEachFrame());
flowScheduler.add(score_E3RoutineEnd());
flowScheduler.add(reminder_F1RoutineBegin());
flowScheduler.add(reminder_F1RoutineEachFrame());
flowScheduler.add(reminder_F1RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_12LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_12LoopBegin(trials_12LoopScheduler));
flowScheduler.add(trials_12LoopScheduler);
flowScheduler.add(trials_12LoopEnd);




flowScheduler.add(score_F1RoutineBegin());
flowScheduler.add(score_F1RoutineEachFrame());
flowScheduler.add(score_F1RoutineEnd());
flowScheduler.add(reminder_G1RoutineBegin());
flowScheduler.add(reminder_G1RoutineEachFrame());
flowScheduler.add(reminder_G1RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_13LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_13LoopBegin(trials_13LoopScheduler));
flowScheduler.add(trials_13LoopScheduler);
flowScheduler.add(trials_13LoopEnd);




flowScheduler.add(score_G1RoutineBegin());
flowScheduler.add(score_G1RoutineEachFrame());
flowScheduler.add(score_G1RoutineEnd());
flowScheduler.add(reminder_G2RoutineBegin());
flowScheduler.add(reminder_G2RoutineEachFrame());
flowScheduler.add(reminder_G2RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_14LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_14LoopBegin(trials_14LoopScheduler));
flowScheduler.add(trials_14LoopScheduler);
flowScheduler.add(trials_14LoopEnd);




flowScheduler.add(score_G2RoutineBegin());
flowScheduler.add(score_G2RoutineEachFrame());
flowScheduler.add(score_G2RoutineEnd());
flowScheduler.add(reminder_G3RoutineBegin());
flowScheduler.add(reminder_G3RoutineEachFrame());
flowScheduler.add(reminder_G3RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_15LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_15LoopBegin(trials_15LoopScheduler));
flowScheduler.add(trials_15LoopScheduler);
flowScheduler.add(trials_15LoopEnd);




flowScheduler.add(score_G3RoutineBegin());
flowScheduler.add(score_G3RoutineEachFrame());
flowScheduler.add(score_G3RoutineEnd());
flowScheduler.add(reminder_H1RoutineBegin());
flowScheduler.add(reminder_H1RoutineEachFrame());
flowScheduler.add(reminder_H1RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_16LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_16LoopBegin(trials_16LoopScheduler));
flowScheduler.add(trials_16LoopScheduler);
flowScheduler.add(trials_16LoopEnd);




flowScheduler.add(score_H1RoutineBegin());
flowScheduler.add(score_H1RoutineEachFrame());
flowScheduler.add(score_H1RoutineEnd());
flowScheduler.add(reminder_I1RoutineBegin());
flowScheduler.add(reminder_I1RoutineEachFrame());
flowScheduler.add(reminder_I1RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_17LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_17LoopBegin(trials_17LoopScheduler));
flowScheduler.add(trials_17LoopScheduler);
flowScheduler.add(trials_17LoopEnd);




flowScheduler.add(score_I1RoutineBegin());
flowScheduler.add(score_I1RoutineEachFrame());
flowScheduler.add(score_I1RoutineEnd());
flowScheduler.add(reminder_I2RoutineBegin());
flowScheduler.add(reminder_I2RoutineEachFrame());
flowScheduler.add(reminder_I2RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_18LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_18LoopBegin(trials_18LoopScheduler));
flowScheduler.add(trials_18LoopScheduler);
flowScheduler.add(trials_18LoopEnd);




flowScheduler.add(score_I2RoutineBegin());
flowScheduler.add(score_I2RoutineEachFrame());
flowScheduler.add(score_I2RoutineEnd());
flowScheduler.add(reminder_I3RoutineBegin());
flowScheduler.add(reminder_I3RoutineEachFrame());
flowScheduler.add(reminder_I3RoutineEnd());
flowScheduler.add(ISI1500RoutineBegin());
flowScheduler.add(ISI1500RoutineEachFrame());
flowScheduler.add(ISI1500RoutineEnd());
const trials_19LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_19LoopBegin(trials_19LoopScheduler));
flowScheduler.add(trials_19LoopScheduler);
flowScheduler.add(trials_19LoopEnd);




flowScheduler.add(score_I3RoutineBegin());
flowScheduler.add(score_I3RoutineEachFrame());
flowScheduler.add(score_I3RoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'excel/TestA1_D2_right_japan.xlsx', 'path': 'excel/TestA1_D2_right_japan.xlsx'},
    {'name': 'excel/TestA1_D2_right_japan.xlsx', 'path': 'excel/TestA1_D2_right_japan.xlsx'},
    {'name': 'excel/TaskB_Positive_ornot.xlsx', 'path': 'excel/TaskB_Positive_ornot.xlsx'},
    {'name': 'excel/TaskB_Positive_ornot.xlsx', 'path': 'excel/TaskB_Positive_ornot.xlsx'},
    {'name': 'excel/TaskC1_E2_block1st3rd_congruent_japan_prefer.xlsx', 'path': 'excel/TaskC1_E2_block1st3rd_congruent_japan_prefer.xlsx'},
    {'name': 'excel/TaskC1_E2_block2nd_congruent_japan_prefer.xlsx', 'path': 'excel/TaskC1_E2_block2nd_congruent_japan_prefer.xlsx'},
    {'name': 'excel/TaskC1_E2_block1st3rd_congruent_japan_prefer.xlsx', 'path': 'excel/TaskC1_E2_block1st3rd_congruent_japan_prefer.xlsx'},
    {'name': 'excel/TaskA2_D1_right_korean.xlsx', 'path': 'excel/TaskA2_D1_right_korean.xlsx'},
    {'name': 'excel/TaskC2_E1_block1st3rd_congruent_korean_prefer.xlsx', 'path': 'excel/TaskC2_E1_block1st3rd_congruent_korean_prefer.xlsx'},
    {'name': 'excel/TaskC2_E1_block2nd_congruent_korean_prefer.xlsx', 'path': 'excel/TaskC2_E1_block2nd_congruent_korean_prefer.xlsx'},
    {'name': 'excel/TaskC2_E1_block1st3rd_congruent_korean_prefer.xlsx', 'path': 'excel/TaskC2_E1_block1st3rd_congruent_korean_prefer.xlsx'},
    {'name': 'excel/TaskF1_H2_korean_right_truncate.xlsx', 'path': 'excel/TaskF1_H2_korean_right_truncate.xlsx'},
    {'name': 'excel/TaskG1_I2_block1st3rd_congruent_korean_prefer.xlsx', 'path': 'excel/TaskG1_I2_block1st3rd_congruent_korean_prefer.xlsx'},
    {'name': 'excel/TaskG1_I2_block2nd_congruent_korean_prefer.xlsx', 'path': 'excel/TaskG1_I2_block2nd_congruent_korean_prefer.xlsx'},
    {'name': 'excel/TaskG1_I2_block1st3rd_congruent_korean_prefer.xlsx', 'path': 'excel/TaskG1_I2_block1st3rd_congruent_korean_prefer.xlsx'},
    {'name': 'excel/TaskF2_H1_japan_right_truncate.xlsx', 'path': 'excel/TaskF2_H1_japan_right_truncate.xlsx'},
    {'name': 'excel/TaskG2_I1_block1st3rd_congruent_japan_prefer.xlsx', 'path': 'excel/TaskG2_I1_block1st3rd_congruent_japan_prefer.xlsx'},
    {'name': 'excel/TaskG2_I1_block2nd_congruent_japan_prefer.xlsx', 'path': 'excel/TaskG2_I1_block2nd_congruent_japan_prefer.xlsx'},
    {'name': 'excel/TaskG2_I1_block1st3rd_congruent_japan_prefer.xlsx', 'path': 'excel/TaskG2_I1_block1st3rd_congruent_japan_prefer.xlsx'},
    {'name': 'picture/welcome_工作區域 1.png', 'path': 'picture/welcome_工作區域 1.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var WelcomeClock;
var welcome;
var key_resp_22;
var IntroductionClock;
var text;
var key_resp;
var reminder_A1Clock;
var text_2;
var key_resp_2;
var ISI1500Clock;
var text_3;
var practice_Task_A1Clock;
var text_A1;
var key_resp_A1;
var feedback_A1Clock;
var msg;
var key_resp_A1_corr_sum_temp;
var key_resp_A1_rt_sum_temp;
var feedback_text_A1;
var ISI250Clock;
var score_A1Clock;
var score_A1_text;
var key_resp_score;
var feedback_msg;
var reminder_A2Clock;
var text_45;
var key_resp_23;
var record_Task_A2Clock;
var text_A2;
var key_resp_A2;
var feedback_A2Clock;
var key_resp_A2_corr_sum_temp;
var key_resp_A2_rt_sum_temp;
var feedback_text_A2;
var score_A2Clock;
var score_A2_text;
var key_resp_3;
var reminder_B1Clock;
var text_46;
var key_resp_24;
var practice_Task_B1Clock;
var text_B1;
var key_resp_B1;
var feedback_B1Clock;
var key_resp_B1_corr_sum_temp;
var key_resp_B1_rt_sum_temp;
var feedback_text_B1;
var score_B1Clock;
var score_B1_text;
var key_resp_6;
var reminder_B2Clock;
var text_47;
var key_resp_25;
var record_Task_B2Clock;
var text_B2;
var key_resp_B2;
var feedback_B2Clock;
var key_resp_B2_corr_sum_temp;
var key_resp_B2_rt_sum_temp;
var feedback_text_B2;
var score_B2Clock;
var score_B2_text;
var key_resp_4;
var reminder_C1Clock;
var text_20;
var key_resp_26;
var record_Task_C1Clock;
var text_C1;
var key_resp_C1;
var feedback_C1Clock;
var key_resp_C1_corr_sum_temp;
var key_resp_C1_rt_sum_temp;
var feedback_text_C1;
var score_C1Clock;
var score_C1_text;
var key_resp_5;
var reminder_C2Clock;
var text_21;
var key_resp_27;
var record_Task_C2Clock;
var text_C2;
var key_resp_C2;
var feedback_C2Clock;
var key_resp_C2_corr_sum_temp;
var key_resp_C2_rt_sum_temp;
var feedback_text_C2;
var score_C2Clock;
var score_C2_text;
var key_resp_7;
var reminder_C3Clock;
var text_48;
var key_resp_28;
var record_Task_C3Clock;
var text_C3;
var key_resp_C3;
var feedback_C3Clock;
var key_resp_C3_corr_sum_temp;
var key_resp_C3_rt_sum_temp;
var feedback_text_C3;
var score_C3Clock;
var score_C3_text;
var key_resp_8;
var reminder_D1Clock;
var text_49;
var key_resp_29;
var record_Task_D1Clock;
var text_D1;
var key_resp_D1;
var feedback_D1Clock;
var key_resp_D1_corr_sum_temp;
var key_resp_D1_rt_sum_temp;
var feedback_text_D1;
var score_D1Clock;
var score_D1_text;
var key_resp_9;
var reminder_E1Clock;
var text_50;
var key_resp_30;
var practice_Task_E1Clock;
var text_E1;
var key_resp_E1;
var feedback_E1Clock;
var key_resp_E1_corr_sum_temp;
var key_resp_E1_rt_sum_temp;
var feedback_text_E1;
var score_E1Clock;
var score_E1_text;
var key_resp_10;
var reminder_E2Clock;
var text_51;
var key_resp_31;
var record_Task_E2Clock;
var text_E2;
var key_resp_E2;
var feedback_E2Clock;
var key_resp_E2_corr_sum_temp;
var key_resp_E2_rt_sum_temp;
var feedback_text_E2;
var score_E2Clock;
var score_E2_text;
var key_resp_11;
var reminder_E3Clock;
var text_52;
var key_resp_40;
var record_Task_E3Clock;
var text_E3;
var key_resp_E3;
var feedback_E3Clock;
var key_resp_E3_corr_sum_temp;
var key_resp_E3_rt_sum_temp;
var feedback_text_E3;
var score_E3Clock;
var score_E3_text;
var key_resp_12;
var reminder_F1Clock;
var text_53;
var key_resp_32;
var record_Task_F1Clock;
var text_F1;
var key_resp_F1;
var feedback_F1Clock;
var key_resp_F1_corr_sum_temp;
var key_resp_F1_rt_sum_temp;
var feedback_text_F1;
var score_F1Clock;
var score_F1_text;
var key_resp_13;
var reminder_G1Clock;
var text_54;
var key_resp_33;
var practice_Task_G1Clock;
var text_G1;
var key_resp_G1;
var feedback_G1Clock;
var key_resp_G1_corr_sum_temp;
var key_resp_G1_rt_sum_temp;
var feedback_text_G1;
var score_G1Clock;
var score_G1_text;
var key_resp_14;
var reminder_G2Clock;
var text_55;
var key_resp_35;
var record_Task_G2Clock;
var text_G2;
var key_resp_G2;
var feedback_G2Clock;
var key_resp_G2_corr_sum_temp;
var key_resp_G2_rt_sum_temp;
var feedback_text_G2;
var score_G2Clock;
var score_G2_text;
var key_resp_15;
var reminder_G3Clock;
var text_56;
var key_resp_34;
var record_Task_G3Clock;
var text_G3;
var key_resp_G3;
var feedback_G3Clock;
var key_resp_G3_corr_sum_temp;
var key_resp_G3_rt_sum_temp;
var feedback_text_G3;
var score_G3Clock;
var score_G3_text;
var key_resp_16;
var reminder_H1Clock;
var text_H1;
var key_resp_H1;
var record_Task_H1Clock;
var text_37;
var key_resp_19;
var feedback_H1Clock;
var key_resp_H1_corr_sum_temp;
var key_resp_H1_rt_sum_temp;
var feedback_text_H1;
var score_H1Clock;
var score_H1_text;
var key_resp_17;
var reminder_I1Clock;
var text_58;
var key_resp_37;
var practice_Task_I1Clock;
var text_I1;
var key_resp_I1;
var feedback_I1Clock;
var key_resp_I1_corr_sum_temp;
var key_resp_I1_rt_sum_temp;
var feedback_text_I1;
var score_I1Clock;
var score_I1_text;
var key_resp_18;
var reminder_I2Clock;
var text_59;
var key_resp_38;
var record_Task_I2Clock;
var text_I2;
var key_resp_I2;
var feedback_I2Clock;
var key_resp_I2_corr_sum_temp;
var key_resp_I2_rt_sum_temp;
var feedback_text_I2;
var score_I2Clock;
var score_I2_text;
var key_resp_20;
var reminder_I3Clock;
var text_60;
var key_resp_39;
var record_Task_I3Clock;
var text_I3;
var key_resp_I3;
var feedback_I3Clock;
var key_resp_I3_corr_sum_temp;
var key_resp_I3_rt_sum_temp;
var feedback_text_I3;
var score_I3Clock;
var score_I3_text;
var key_resp_21;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  welcome = new visual.ImageStim({
    win : psychoJS.window,
    name : 'welcome', units : undefined, 
    image : 'picture/welcome_工作區域 1.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1.6, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_22 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Introduction"
  IntroductionClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Put the left forefinger on the "A" key for the items belong to the category "unplesant".\n\nPut the right forefinger on the "L" key for the items belong to the category "plesant".\n\nPress the "space bar" to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_A1"
  reminder_A1Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Part 1\n\nIf you make a mistake, a "error" will appear.\nGo as fast as you can while being accurate.\n\nThe trial will begin.\n\nPress the "space bar" to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ISI1500"
  ISI1500Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "practice_Task_A1"
  practice_Task_A1Clock = new util.Clock();
  text_A1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_A1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_A1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_A1"
  feedback_A1Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_A1
  msg = "";
  key_resp_A1_corr_sum_temp = 0.0;
  key_resp_A1_rt_sum_temp = 0.0;
  
  feedback_text_A1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_A1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "ISI250"
  ISI250Clock = new util.Clock();
  // Initialize components for Routine "score_A1"
  score_A1Clock = new util.Clock();
  score_A1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_A1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_score = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from score_A1_code
  feedback_msg = "";
  
  // Initialize components for Routine "reminder_A2"
  reminder_A2Clock = new util.Clock();
  text_45 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_45',
    text: 'Part 2\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_23 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_A2"
  record_Task_A2Clock = new util.Clock();
  text_A2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_A2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_A2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_A2"
  feedback_A2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_A2
  msg = "";
  key_resp_A2_corr_sum_temp = 0.0;
  key_resp_A2_rt_sum_temp = 0.0;
  
  feedback_text_A2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_A2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_A2"
  score_A2Clock = new util.Clock();
  score_A2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_A2_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from score_A2_code
  feedback_msg = "";
  
  // Initialize components for Routine "reminder_B1"
  reminder_B1Clock = new util.Clock();
  text_46 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_46',
    text: 'Part 3\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_24 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_Task_B1"
  practice_Task_B1Clock = new util.Clock();
  text_B1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_B1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_B1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_B1"
  feedback_B1Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_B1
  msg = "";
  key_resp_B1_corr_sum_temp = 0.0;
  key_resp_B1_rt_sum_temp = 0.0;
  
  feedback_text_B1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_B1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_B1"
  score_B1Clock = new util.Clock();
  score_B1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_B1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from score_B1_code
  feedback_msg = "";
  
  // Initialize components for Routine "reminder_B2"
  reminder_B2Clock = new util.Clock();
  text_47 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_47',
    text: 'Part 4\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_25 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_B2"
  record_Task_B2Clock = new util.Clock();
  text_B2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_B2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_B2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_B2"
  feedback_B2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_B2
  msg = "";
  key_resp_B2_corr_sum_temp = 0.0;
  key_resp_B2_rt_sum_temp = 0.0;
  
  feedback_text_B2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_B2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_B2"
  score_B2Clock = new util.Clock();
  score_B2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_B2_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from score_B2_code
  feedback_msg = "";
  
  // Initialize components for Routine "reminder_C1"
  reminder_C1Clock = new util.Clock();
  text_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_20',
    text: 'Part 5\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_26 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_C1"
  record_Task_C1Clock = new util.Clock();
  text_C1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_C1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_C1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_C1"
  feedback_C1Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_C1
  msg = "";
  key_resp_C1_corr_sum_temp = 0.0;
  key_resp_C1_rt_sum_temp = 0.0;
  
  feedback_text_C1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_C1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_C1"
  score_C1Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_C1_code
  feedback_msg = "";
  
  score_C1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_C1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_C2"
  reminder_C2Clock = new util.Clock();
  text_21 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_21',
    text: 'Part 6\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_27 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_C2"
  record_Task_C2Clock = new util.Clock();
  text_C2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_C2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_C2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_C2"
  feedback_C2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_C2
  msg = "";
  key_resp_C2_corr_sum_temp = 0.0;
  key_resp_C2_rt_sum_temp = 0.0;
  
  feedback_text_C2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_C2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_C2"
  score_C2Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_C2_code
  feedback_msg = "";
  
  score_C2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_C2_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_C3"
  reminder_C3Clock = new util.Clock();
  text_48 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_48',
    text: 'Part 7\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_28 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_C3"
  record_Task_C3Clock = new util.Clock();
  text_C3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_C3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_C3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_C3"
  feedback_C3Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_C3
  msg = "";
  key_resp_C3_corr_sum_temp = 0.0;
  key_resp_C3_rt_sum_temp = 0.0;
  
  feedback_text_C3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_C3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_C3"
  score_C3Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_C3_code
  feedback_msg = "";
  
  score_C3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_C3_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_D1"
  reminder_D1Clock = new util.Clock();
  text_49 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_49',
    text: 'Part 8\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_29 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_D1"
  record_Task_D1Clock = new util.Clock();
  text_D1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_D1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_D1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_D1"
  feedback_D1Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_D1
  msg = "";
  key_resp_D1_corr_sum_temp = 0.0;
  key_resp_D1_rt_sum_temp = 0.0;
  
  feedback_text_D1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_D1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_D1"
  score_D1Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_D1_code
  feedback_msg = "";
  
  score_D1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_D1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_E1"
  reminder_E1Clock = new util.Clock();
  text_50 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_50',
    text: 'Part 9\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_30 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_Task_E1"
  practice_Task_E1Clock = new util.Clock();
  text_E1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_E1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_E1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_E1"
  feedback_E1Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_E1
  msg = "";
  key_resp_E1_corr_sum_temp = 0.0;
  key_resp_E1_rt_sum_temp = 0.0;
  
  feedback_text_E1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_E1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_E1"
  score_E1Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_E1_code
  feedback_msg = "";
  
  score_E1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_E1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_E2"
  reminder_E2Clock = new util.Clock();
  text_51 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_51',
    text: 'Part 10\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_31 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_E2"
  record_Task_E2Clock = new util.Clock();
  text_E2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_E2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_E2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_E2"
  feedback_E2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_E2
  msg = "";
  key_resp_E2_corr_sum_temp = 0.0;
  key_resp_E2_rt_sum_temp = 0.0;
  
  feedback_text_E2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_E2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_E2"
  score_E2Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_E2_code
  feedback_msg = "";
  
  score_E2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_E2_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_E3"
  reminder_E3Clock = new util.Clock();
  text_52 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_52',
    text: 'Part 11\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_40 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_E3"
  record_Task_E3Clock = new util.Clock();
  text_E3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_E3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_E3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_E3"
  feedback_E3Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_E3
  msg = "";
  key_resp_E3_corr_sum_temp = 0.0;
  key_resp_E3_rt_sum_temp = 0.0;
  
  feedback_text_E3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_E3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_E3"
  score_E3Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_E3_code
  feedback_msg = "";
  
  score_E3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_E3_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_F1"
  reminder_F1Clock = new util.Clock();
  text_53 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_53',
    text: 'Part 12\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_32 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_F1"
  record_Task_F1Clock = new util.Clock();
  text_F1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_F1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_F1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_F1"
  feedback_F1Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_F1
  msg = "";
  key_resp_F1_corr_sum_temp = 0.0;
  key_resp_F1_rt_sum_temp = 0.0;
  
  feedback_text_F1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_F1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_F1"
  score_F1Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_F1_code
  feedback_msg = "";
  
  score_F1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_F1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_G1"
  reminder_G1Clock = new util.Clock();
  text_54 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_54',
    text: 'Part 13\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_33 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_Task_G1"
  practice_Task_G1Clock = new util.Clock();
  text_G1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_G1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_G1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_G1"
  feedback_G1Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_G1
  msg = "";
  key_resp_G1_corr_sum_temp = 0.0;
  key_resp_G1_rt_sum_temp = 0.0;
  
  feedback_text_G1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_G1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_G1"
  score_G1Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_G1_code
  feedback_msg = "";
  
  score_G1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_G1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_G2"
  reminder_G2Clock = new util.Clock();
  text_55 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_55',
    text: 'Part 14\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_35 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_G2"
  record_Task_G2Clock = new util.Clock();
  text_G2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_G2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_G2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_G2"
  feedback_G2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_G2
  msg = "";
  key_resp_G2_corr_sum_temp = 0.0;
  key_resp_G2_rt_sum_temp = 0.0;
  
  feedback_text_G2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_G2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_G2"
  score_G2Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_G2_code
  feedback_msg = "";
  
  score_G2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_G2_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_G3"
  reminder_G3Clock = new util.Clock();
  text_56 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_56',
    text: 'Part 15\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_34 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_G3"
  record_Task_G3Clock = new util.Clock();
  text_G3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_G3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_G3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_G3"
  feedback_G3Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_G3
  msg = "";
  key_resp_G3_corr_sum_temp = 0.0;
  key_resp_G3_rt_sum_temp = 0.0;
  
  feedback_text_G3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_G3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_G3"
  score_G3Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_G3_code
  feedback_msg = "";
  
  score_G3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_G3_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_H1"
  reminder_H1Clock = new util.Clock();
  text_H1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_H1',
    text: 'Part 16\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_H1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_H1"
  record_Task_H1Clock = new util.Clock();
  text_37 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_37',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_19 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_H1"
  feedback_H1Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_H1
  msg = "";
  key_resp_H1_corr_sum_temp = 0.0;
  key_resp_H1_rt_sum_temp = 0.0;
  
  feedback_text_H1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_H1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_H1"
  score_H1Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_H1_code
  feedback_msg = "";
  
  score_H1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_H1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_17 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_I1"
  reminder_I1Clock = new util.Clock();
  text_58 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_58',
    text: 'Part 17\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_37 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_Task_I1"
  practice_Task_I1Clock = new util.Clock();
  text_I1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_I1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_I1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_I1"
  feedback_I1Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_I1
  msg = "";
  key_resp_I1_corr_sum_temp = 0.0;
  key_resp_I1_rt_sum_temp = 0.0;
  
  feedback_text_I1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_I1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_I1"
  score_I1Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_I1_code
  feedback_msg = "";
  
  score_I1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_I1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_I2"
  reminder_I2Clock = new util.Clock();
  text_59 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_59',
    text: 'Part 18\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_38 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_I2"
  record_Task_I2Clock = new util.Clock();
  text_I2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_I2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_I2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_I2"
  feedback_I2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_I2
  msg = "";
  key_resp_I2_corr_sum_temp = 0.0;
  key_resp_I2_rt_sum_temp = 0.0;
  
  feedback_text_I2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_I2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_I2"
  score_I2Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_I2_code
  feedback_msg = "";
  
  score_I2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_I2_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_20 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_I3"
  reminder_I3Clock = new util.Clock();
  text_60 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_60',
    text: 'Part 19\n\nThe trial will begin.\n\nPress space bar to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_39 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "record_Task_I3"
  record_Task_I3Clock = new util.Clock();
  text_I3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_I3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_I3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_I3"
  feedback_I3Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_I3
  msg = "";
  key_resp_I3_corr_sum_temp = 0.0;
  key_resp_I3_rt_sum_temp = 0.0;
  
  feedback_text_I3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text_I3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "score_I3"
  score_I3Clock = new util.Clock();
  // Run 'Begin Experiment' code from score_I3_code
  feedback_msg = "";
  
  score_I3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'score_I3_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_21 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var WelcomeMaxDurationReached;
var _key_resp_22_allKeys;
var WelcomeMaxDuration;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    WelcomeClock.reset();
    routineTimer.reset();
    WelcomeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_22.keys = undefined;
    key_resp_22.rt = undefined;
    _key_resp_22_allKeys = [];
    psychoJS.experiment.addData('Welcome.started', globalClock.getTime());
    WelcomeMaxDuration = null
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(welcome);
    WelcomeComponents.push(key_resp_22);
    
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function WelcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome' ---
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome* updates
    if (t >= 0.0 && welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome.tStart = t;  // (not accounting for frame time here)
      welcome.frameNStart = frameN;  // exact frame index
      
      welcome.setAutoDraw(true);
    }
    
    
    // *key_resp_22* updates
    if (t >= 0.0 && key_resp_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_22.tStart = t;  // (not accounting for frame time here)
      key_resp_22.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_22.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.clearEvents(); });
    }
    
    if (key_resp_22.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_22.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_22_allKeys = _key_resp_22_allKeys.concat(theseKeys);
      if (_key_resp_22_allKeys.length > 0) {
        key_resp_22.keys = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].name;  // just the last key pressed
        key_resp_22.rt = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].rt;
        key_resp_22.duration = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome' ---
    for (const thisComponent of WelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_22.corr, level);
    }
    psychoJS.experiment.addData('key_resp_22.keys', key_resp_22.keys);
    if (typeof key_resp_22.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_22.rt', key_resp_22.rt);
        psychoJS.experiment.addData('key_resp_22.duration', key_resp_22.duration);
        routineTimer.reset();
        }
    
    key_resp_22.stop();
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var IntroductionMaxDurationReached;
var _key_resp_allKeys;
var IntroductionMaxDuration;
var IntroductionComponents;
function IntroductionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Introduction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    IntroductionClock.reset();
    routineTimer.reset();
    IntroductionMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('Introduction.started', globalClock.getTime());
    IntroductionMaxDuration = null
    // keep track of which components have finished
    IntroductionComponents = [];
    IntroductionComponents.push(text);
    IntroductionComponents.push(key_resp);
    
    for (const thisComponent of IntroductionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function IntroductionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Introduction' ---
    // get current time
    t = IntroductionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of IntroductionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function IntroductionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Introduction' ---
    for (const thisComponent of IntroductionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Introduction.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_20;
function trials_20LoopBegin(trials_20LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_20 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 0, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_20'
    });
    psychoJS.experiment.addLoop(trials_20); // add the loop to the experiment
    currentLoop = trials_20;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_20 of trials_20) {
      snapshot = trials_20.getSnapshot();
      trials_20LoopScheduler.add(importConditions(snapshot));
      trials_20LoopScheduler.add(reminder_A1RoutineBegin(snapshot));
      trials_20LoopScheduler.add(reminder_A1RoutineEachFrame());
      trials_20LoopScheduler.add(reminder_A1RoutineEnd(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineBegin(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineEachFrame());
      trials_20LoopScheduler.add(ISI1500RoutineEnd(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      trials_20LoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      trials_20LoopScheduler.add(trialsLoopScheduler);
      trials_20LoopScheduler.add(trialsLoopEnd);
      trials_20LoopScheduler.add(score_A1RoutineBegin(snapshot));
      trials_20LoopScheduler.add(score_A1RoutineEachFrame());
      trials_20LoopScheduler.add(score_A1RoutineEnd(snapshot));
      trials_20LoopScheduler.add(reminder_A2RoutineBegin(snapshot));
      trials_20LoopScheduler.add(reminder_A2RoutineEachFrame());
      trials_20LoopScheduler.add(reminder_A2RoutineEnd(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineBegin(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineEachFrame());
      trials_20LoopScheduler.add(ISI1500RoutineEnd(snapshot));
      const trials_4LoopScheduler = new Scheduler(psychoJS);
      trials_20LoopScheduler.add(trials_4LoopBegin(trials_4LoopScheduler, snapshot));
      trials_20LoopScheduler.add(trials_4LoopScheduler);
      trials_20LoopScheduler.add(trials_4LoopEnd);
      trials_20LoopScheduler.add(score_A2RoutineBegin(snapshot));
      trials_20LoopScheduler.add(score_A2RoutineEachFrame());
      trials_20LoopScheduler.add(score_A2RoutineEnd(snapshot));
      trials_20LoopScheduler.add(reminder_B1RoutineBegin(snapshot));
      trials_20LoopScheduler.add(reminder_B1RoutineEachFrame());
      trials_20LoopScheduler.add(reminder_B1RoutineEnd(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineBegin(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineEachFrame());
      trials_20LoopScheduler.add(ISI1500RoutineEnd(snapshot));
      const trials_7LoopScheduler = new Scheduler(psychoJS);
      trials_20LoopScheduler.add(trials_7LoopBegin(trials_7LoopScheduler, snapshot));
      trials_20LoopScheduler.add(trials_7LoopScheduler);
      trials_20LoopScheduler.add(trials_7LoopEnd);
      trials_20LoopScheduler.add(score_B1RoutineBegin(snapshot));
      trials_20LoopScheduler.add(score_B1RoutineEachFrame());
      trials_20LoopScheduler.add(score_B1RoutineEnd(snapshot));
      trials_20LoopScheduler.add(reminder_B2RoutineBegin(snapshot));
      trials_20LoopScheduler.add(reminder_B2RoutineEachFrame());
      trials_20LoopScheduler.add(reminder_B2RoutineEnd(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineBegin(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineEachFrame());
      trials_20LoopScheduler.add(ISI1500RoutineEnd(snapshot));
      const trials_2LoopScheduler = new Scheduler(psychoJS);
      trials_20LoopScheduler.add(trials_2LoopBegin(trials_2LoopScheduler, snapshot));
      trials_20LoopScheduler.add(trials_2LoopScheduler);
      trials_20LoopScheduler.add(trials_2LoopEnd);
      trials_20LoopScheduler.add(score_B2RoutineBegin(snapshot));
      trials_20LoopScheduler.add(score_B2RoutineEachFrame());
      trials_20LoopScheduler.add(score_B2RoutineEnd(snapshot));
      trials_20LoopScheduler.add(reminder_C1RoutineBegin(snapshot));
      trials_20LoopScheduler.add(reminder_C1RoutineEachFrame());
      trials_20LoopScheduler.add(reminder_C1RoutineEnd(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineBegin(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineEachFrame());
      trials_20LoopScheduler.add(ISI1500RoutineEnd(snapshot));
      const trials_3LoopScheduler = new Scheduler(psychoJS);
      trials_20LoopScheduler.add(trials_3LoopBegin(trials_3LoopScheduler, snapshot));
      trials_20LoopScheduler.add(trials_3LoopScheduler);
      trials_20LoopScheduler.add(trials_3LoopEnd);
      trials_20LoopScheduler.add(score_C1RoutineBegin(snapshot));
      trials_20LoopScheduler.add(score_C1RoutineEachFrame());
      trials_20LoopScheduler.add(score_C1RoutineEnd(snapshot));
      trials_20LoopScheduler.add(reminder_C2RoutineBegin(snapshot));
      trials_20LoopScheduler.add(reminder_C2RoutineEachFrame());
      trials_20LoopScheduler.add(reminder_C2RoutineEnd(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineBegin(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineEachFrame());
      trials_20LoopScheduler.add(ISI1500RoutineEnd(snapshot));
      const trials_5LoopScheduler = new Scheduler(psychoJS);
      trials_20LoopScheduler.add(trials_5LoopBegin(trials_5LoopScheduler, snapshot));
      trials_20LoopScheduler.add(trials_5LoopScheduler);
      trials_20LoopScheduler.add(trials_5LoopEnd);
      trials_20LoopScheduler.add(score_C2RoutineBegin(snapshot));
      trials_20LoopScheduler.add(score_C2RoutineEachFrame());
      trials_20LoopScheduler.add(score_C2RoutineEnd(snapshot));
      trials_20LoopScheduler.add(reminder_C3RoutineBegin(snapshot));
      trials_20LoopScheduler.add(reminder_C3RoutineEachFrame());
      trials_20LoopScheduler.add(reminder_C3RoutineEnd(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineBegin(snapshot));
      trials_20LoopScheduler.add(ISI1500RoutineEachFrame());
      trials_20LoopScheduler.add(ISI1500RoutineEnd(snapshot));
      const trials_6LoopScheduler = new Scheduler(psychoJS);
      trials_20LoopScheduler.add(trials_6LoopBegin(trials_6LoopScheduler, snapshot));
      trials_20LoopScheduler.add(trials_6LoopScheduler);
      trials_20LoopScheduler.add(trials_6LoopEnd);
      trials_20LoopScheduler.add(score_C3RoutineBegin(snapshot));
      trials_20LoopScheduler.add(score_C3RoutineEachFrame());
      trials_20LoopScheduler.add(score_C3RoutineEnd(snapshot));
      trials_20LoopScheduler.add(trials_20LoopEndIteration(trials_20LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TestA1_D2_right_japan.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(practice_Task_A1RoutineBegin(snapshot));
      trialsLoopScheduler.add(practice_Task_A1RoutineEachFrame());
      trialsLoopScheduler.add(practice_Task_A1RoutineEnd(snapshot));
      trialsLoopScheduler.add(feedback_A1RoutineBegin(snapshot));
      trialsLoopScheduler.add(feedback_A1RoutineEachFrame());
      trialsLoopScheduler.add(feedback_A1RoutineEnd(snapshot));
      trialsLoopScheduler.add(ISI250RoutineBegin(snapshot));
      trialsLoopScheduler.add(ISI250RoutineEachFrame());
      trialsLoopScheduler.add(ISI250RoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_4;
function trials_4LoopBegin(trials_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TestA1_D2_right_japan.xlsx',
      seed: undefined, name: 'trials_4'
    });
    psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
    currentLoop = trials_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_4 of trials_4) {
      snapshot = trials_4.getSnapshot();
      trials_4LoopScheduler.add(importConditions(snapshot));
      trials_4LoopScheduler.add(record_Task_A2RoutineBegin(snapshot));
      trials_4LoopScheduler.add(record_Task_A2RoutineEachFrame());
      trials_4LoopScheduler.add(record_Task_A2RoutineEnd(snapshot));
      trials_4LoopScheduler.add(feedback_A2RoutineBegin(snapshot));
      trials_4LoopScheduler.add(feedback_A2RoutineEachFrame());
      trials_4LoopScheduler.add(feedback_A2RoutineEnd(snapshot));
      trials_4LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_4LoopScheduler.add(ISI250RoutineEachFrame());
      trials_4LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_4LoopScheduler.add(trials_4LoopEndIteration(trials_4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_7;
function trials_7LoopBegin(trials_7LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_7 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskB_Positive_ornot.xlsx',
      seed: undefined, name: 'trials_7'
    });
    psychoJS.experiment.addLoop(trials_7); // add the loop to the experiment
    currentLoop = trials_7;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_7 of trials_7) {
      snapshot = trials_7.getSnapshot();
      trials_7LoopScheduler.add(importConditions(snapshot));
      trials_7LoopScheduler.add(practice_Task_B1RoutineBegin(snapshot));
      trials_7LoopScheduler.add(practice_Task_B1RoutineEachFrame());
      trials_7LoopScheduler.add(practice_Task_B1RoutineEnd(snapshot));
      trials_7LoopScheduler.add(feedback_B1RoutineBegin(snapshot));
      trials_7LoopScheduler.add(feedback_B1RoutineEachFrame());
      trials_7LoopScheduler.add(feedback_B1RoutineEnd(snapshot));
      trials_7LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_7LoopScheduler.add(ISI250RoutineEachFrame());
      trials_7LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_7LoopScheduler.add(trials_7LoopEndIteration(trials_7LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_7LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_7);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_7LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskB_Positive_ornot.xlsx',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(record_Task_B2RoutineBegin(snapshot));
      trials_2LoopScheduler.add(record_Task_B2RoutineEachFrame());
      trials_2LoopScheduler.add(record_Task_B2RoutineEnd(snapshot));
      trials_2LoopScheduler.add(feedback_B2RoutineBegin(snapshot));
      trials_2LoopScheduler.add(feedback_B2RoutineEachFrame());
      trials_2LoopScheduler.add(feedback_B2RoutineEnd(snapshot));
      trials_2LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_2LoopScheduler.add(ISI250RoutineEachFrame());
      trials_2LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskC1_E2_block1st3rd_congruent_japan_prefer.xlsx',
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(record_Task_C1RoutineBegin(snapshot));
      trials_3LoopScheduler.add(record_Task_C1RoutineEachFrame());
      trials_3LoopScheduler.add(record_Task_C1RoutineEnd(snapshot));
      trials_3LoopScheduler.add(feedback_C1RoutineBegin(snapshot));
      trials_3LoopScheduler.add(feedback_C1RoutineEachFrame());
      trials_3LoopScheduler.add(feedback_C1RoutineEnd(snapshot));
      trials_3LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_3LoopScheduler.add(ISI250RoutineEachFrame());
      trials_3LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_5;
function trials_5LoopBegin(trials_5LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_5 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskC1_E2_block2nd_congruent_japan_prefer.xlsx',
      seed: undefined, name: 'trials_5'
    });
    psychoJS.experiment.addLoop(trials_5); // add the loop to the experiment
    currentLoop = trials_5;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_5 of trials_5) {
      snapshot = trials_5.getSnapshot();
      trials_5LoopScheduler.add(importConditions(snapshot));
      trials_5LoopScheduler.add(record_Task_C2RoutineBegin(snapshot));
      trials_5LoopScheduler.add(record_Task_C2RoutineEachFrame());
      trials_5LoopScheduler.add(record_Task_C2RoutineEnd(snapshot));
      trials_5LoopScheduler.add(feedback_C2RoutineBegin(snapshot));
      trials_5LoopScheduler.add(feedback_C2RoutineEachFrame());
      trials_5LoopScheduler.add(feedback_C2RoutineEnd(snapshot));
      trials_5LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_5LoopScheduler.add(ISI250RoutineEachFrame());
      trials_5LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_5LoopScheduler.add(trials_5LoopEndIteration(trials_5LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_5LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_5);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_5LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_6;
function trials_6LoopBegin(trials_6LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_6 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskC1_E2_block1st3rd_congruent_japan_prefer.xlsx',
      seed: undefined, name: 'trials_6'
    });
    psychoJS.experiment.addLoop(trials_6); // add the loop to the experiment
    currentLoop = trials_6;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_6 of trials_6) {
      snapshot = trials_6.getSnapshot();
      trials_6LoopScheduler.add(importConditions(snapshot));
      trials_6LoopScheduler.add(record_Task_C3RoutineBegin(snapshot));
      trials_6LoopScheduler.add(record_Task_C3RoutineEachFrame());
      trials_6LoopScheduler.add(record_Task_C3RoutineEnd(snapshot));
      trials_6LoopScheduler.add(feedback_C3RoutineBegin(snapshot));
      trials_6LoopScheduler.add(feedback_C3RoutineEachFrame());
      trials_6LoopScheduler.add(feedback_C3RoutineEnd(snapshot));
      trials_6LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_6LoopScheduler.add(ISI250RoutineEachFrame());
      trials_6LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_6LoopScheduler.add(trials_6LoopEndIteration(trials_6LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_6LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_6);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_6LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_20LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_20);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_20LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_8;
function trials_8LoopBegin(trials_8LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_8 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskA2_D1_right_korean.xlsx',
      seed: undefined, name: 'trials_8'
    });
    psychoJS.experiment.addLoop(trials_8); // add the loop to the experiment
    currentLoop = trials_8;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_8 of trials_8) {
      snapshot = trials_8.getSnapshot();
      trials_8LoopScheduler.add(importConditions(snapshot));
      trials_8LoopScheduler.add(record_Task_D1RoutineBegin(snapshot));
      trials_8LoopScheduler.add(record_Task_D1RoutineEachFrame());
      trials_8LoopScheduler.add(record_Task_D1RoutineEnd(snapshot));
      trials_8LoopScheduler.add(feedback_D1RoutineBegin(snapshot));
      trials_8LoopScheduler.add(feedback_D1RoutineEachFrame());
      trials_8LoopScheduler.add(feedback_D1RoutineEnd(snapshot));
      trials_8LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_8LoopScheduler.add(ISI250RoutineEachFrame());
      trials_8LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_8LoopScheduler.add(trials_8LoopEndIteration(trials_8LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_8LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_8);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_8LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_9;
function trials_9LoopBegin(trials_9LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_9 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskC2_E1_block1st3rd_congruent_korean_prefer.xlsx',
      seed: undefined, name: 'trials_9'
    });
    psychoJS.experiment.addLoop(trials_9); // add the loop to the experiment
    currentLoop = trials_9;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_9 of trials_9) {
      snapshot = trials_9.getSnapshot();
      trials_9LoopScheduler.add(importConditions(snapshot));
      trials_9LoopScheduler.add(practice_Task_E1RoutineBegin(snapshot));
      trials_9LoopScheduler.add(practice_Task_E1RoutineEachFrame());
      trials_9LoopScheduler.add(practice_Task_E1RoutineEnd(snapshot));
      trials_9LoopScheduler.add(feedback_E1RoutineBegin(snapshot));
      trials_9LoopScheduler.add(feedback_E1RoutineEachFrame());
      trials_9LoopScheduler.add(feedback_E1RoutineEnd(snapshot));
      trials_9LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_9LoopScheduler.add(ISI250RoutineEachFrame());
      trials_9LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_9LoopScheduler.add(trials_9LoopEndIteration(trials_9LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_9LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_9);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_9LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_10;
function trials_10LoopBegin(trials_10LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_10 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskC2_E1_block2nd_congruent_korean_prefer.xlsx',
      seed: undefined, name: 'trials_10'
    });
    psychoJS.experiment.addLoop(trials_10); // add the loop to the experiment
    currentLoop = trials_10;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_10 of trials_10) {
      snapshot = trials_10.getSnapshot();
      trials_10LoopScheduler.add(importConditions(snapshot));
      trials_10LoopScheduler.add(record_Task_E2RoutineBegin(snapshot));
      trials_10LoopScheduler.add(record_Task_E2RoutineEachFrame());
      trials_10LoopScheduler.add(record_Task_E2RoutineEnd(snapshot));
      trials_10LoopScheduler.add(feedback_E2RoutineBegin(snapshot));
      trials_10LoopScheduler.add(feedback_E2RoutineEachFrame());
      trials_10LoopScheduler.add(feedback_E2RoutineEnd(snapshot));
      trials_10LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_10LoopScheduler.add(ISI250RoutineEachFrame());
      trials_10LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_10LoopScheduler.add(trials_10LoopEndIteration(trials_10LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_10LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_10);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_10LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_11;
function trials_11LoopBegin(trials_11LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_11 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskC2_E1_block1st3rd_congruent_korean_prefer.xlsx',
      seed: undefined, name: 'trials_11'
    });
    psychoJS.experiment.addLoop(trials_11); // add the loop to the experiment
    currentLoop = trials_11;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_11 of trials_11) {
      snapshot = trials_11.getSnapshot();
      trials_11LoopScheduler.add(importConditions(snapshot));
      trials_11LoopScheduler.add(record_Task_E3RoutineBegin(snapshot));
      trials_11LoopScheduler.add(record_Task_E3RoutineEachFrame());
      trials_11LoopScheduler.add(record_Task_E3RoutineEnd(snapshot));
      trials_11LoopScheduler.add(feedback_E3RoutineBegin(snapshot));
      trials_11LoopScheduler.add(feedback_E3RoutineEachFrame());
      trials_11LoopScheduler.add(feedback_E3RoutineEnd(snapshot));
      trials_11LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_11LoopScheduler.add(ISI250RoutineEachFrame());
      trials_11LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_11LoopScheduler.add(trials_11LoopEndIteration(trials_11LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_11LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_11);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_11LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_12;
function trials_12LoopBegin(trials_12LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_12 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskF1_H2_korean_right_truncate.xlsx',
      seed: undefined, name: 'trials_12'
    });
    psychoJS.experiment.addLoop(trials_12); // add the loop to the experiment
    currentLoop = trials_12;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_12 of trials_12) {
      snapshot = trials_12.getSnapshot();
      trials_12LoopScheduler.add(importConditions(snapshot));
      trials_12LoopScheduler.add(record_Task_F1RoutineBegin(snapshot));
      trials_12LoopScheduler.add(record_Task_F1RoutineEachFrame());
      trials_12LoopScheduler.add(record_Task_F1RoutineEnd(snapshot));
      trials_12LoopScheduler.add(feedback_F1RoutineBegin(snapshot));
      trials_12LoopScheduler.add(feedback_F1RoutineEachFrame());
      trials_12LoopScheduler.add(feedback_F1RoutineEnd(snapshot));
      trials_12LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_12LoopScheduler.add(ISI250RoutineEachFrame());
      trials_12LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_12LoopScheduler.add(trials_12LoopEndIteration(trials_12LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_12LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_12);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_12LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_13;
function trials_13LoopBegin(trials_13LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_13 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskG1_I2_block1st3rd_congruent_korean_prefer.xlsx',
      seed: undefined, name: 'trials_13'
    });
    psychoJS.experiment.addLoop(trials_13); // add the loop to the experiment
    currentLoop = trials_13;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_13 of trials_13) {
      snapshot = trials_13.getSnapshot();
      trials_13LoopScheduler.add(importConditions(snapshot));
      trials_13LoopScheduler.add(practice_Task_G1RoutineBegin(snapshot));
      trials_13LoopScheduler.add(practice_Task_G1RoutineEachFrame());
      trials_13LoopScheduler.add(practice_Task_G1RoutineEnd(snapshot));
      trials_13LoopScheduler.add(feedback_G1RoutineBegin(snapshot));
      trials_13LoopScheduler.add(feedback_G1RoutineEachFrame());
      trials_13LoopScheduler.add(feedback_G1RoutineEnd(snapshot));
      trials_13LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_13LoopScheduler.add(ISI250RoutineEachFrame());
      trials_13LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_13LoopScheduler.add(trials_13LoopEndIteration(trials_13LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_13LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_13);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_13LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_14;
function trials_14LoopBegin(trials_14LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_14 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskG1_I2_block2nd_congruent_korean_prefer.xlsx',
      seed: undefined, name: 'trials_14'
    });
    psychoJS.experiment.addLoop(trials_14); // add the loop to the experiment
    currentLoop = trials_14;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_14 of trials_14) {
      snapshot = trials_14.getSnapshot();
      trials_14LoopScheduler.add(importConditions(snapshot));
      trials_14LoopScheduler.add(record_Task_G2RoutineBegin(snapshot));
      trials_14LoopScheduler.add(record_Task_G2RoutineEachFrame());
      trials_14LoopScheduler.add(record_Task_G2RoutineEnd(snapshot));
      trials_14LoopScheduler.add(feedback_G2RoutineBegin(snapshot));
      trials_14LoopScheduler.add(feedback_G2RoutineEachFrame());
      trials_14LoopScheduler.add(feedback_G2RoutineEnd(snapshot));
      trials_14LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_14LoopScheduler.add(ISI250RoutineEachFrame());
      trials_14LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_14LoopScheduler.add(trials_14LoopEndIteration(trials_14LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_14LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_14);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_14LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_15;
function trials_15LoopBegin(trials_15LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_15 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskG1_I2_block1st3rd_congruent_korean_prefer.xlsx',
      seed: undefined, name: 'trials_15'
    });
    psychoJS.experiment.addLoop(trials_15); // add the loop to the experiment
    currentLoop = trials_15;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_15 of trials_15) {
      snapshot = trials_15.getSnapshot();
      trials_15LoopScheduler.add(importConditions(snapshot));
      trials_15LoopScheduler.add(record_Task_G3RoutineBegin(snapshot));
      trials_15LoopScheduler.add(record_Task_G3RoutineEachFrame());
      trials_15LoopScheduler.add(record_Task_G3RoutineEnd(snapshot));
      trials_15LoopScheduler.add(feedback_G3RoutineBegin(snapshot));
      trials_15LoopScheduler.add(feedback_G3RoutineEachFrame());
      trials_15LoopScheduler.add(feedback_G3RoutineEnd(snapshot));
      trials_15LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_15LoopScheduler.add(ISI250RoutineEachFrame());
      trials_15LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_15LoopScheduler.add(trials_15LoopEndIteration(trials_15LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_15LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_15);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_15LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_16;
function trials_16LoopBegin(trials_16LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_16 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskF2_H1_japan_right_truncate.xlsx',
      seed: undefined, name: 'trials_16'
    });
    psychoJS.experiment.addLoop(trials_16); // add the loop to the experiment
    currentLoop = trials_16;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_16 of trials_16) {
      snapshot = trials_16.getSnapshot();
      trials_16LoopScheduler.add(importConditions(snapshot));
      trials_16LoopScheduler.add(record_Task_H1RoutineBegin(snapshot));
      trials_16LoopScheduler.add(record_Task_H1RoutineEachFrame());
      trials_16LoopScheduler.add(record_Task_H1RoutineEnd(snapshot));
      trials_16LoopScheduler.add(feedback_H1RoutineBegin(snapshot));
      trials_16LoopScheduler.add(feedback_H1RoutineEachFrame());
      trials_16LoopScheduler.add(feedback_H1RoutineEnd(snapshot));
      trials_16LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_16LoopScheduler.add(ISI250RoutineEachFrame());
      trials_16LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_16LoopScheduler.add(trials_16LoopEndIteration(trials_16LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_16LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_16);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_16LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_17;
function trials_17LoopBegin(trials_17LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_17 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskG2_I1_block1st3rd_congruent_japan_prefer.xlsx',
      seed: undefined, name: 'trials_17'
    });
    psychoJS.experiment.addLoop(trials_17); // add the loop to the experiment
    currentLoop = trials_17;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_17 of trials_17) {
      snapshot = trials_17.getSnapshot();
      trials_17LoopScheduler.add(importConditions(snapshot));
      trials_17LoopScheduler.add(practice_Task_I1RoutineBegin(snapshot));
      trials_17LoopScheduler.add(practice_Task_I1RoutineEachFrame());
      trials_17LoopScheduler.add(practice_Task_I1RoutineEnd(snapshot));
      trials_17LoopScheduler.add(feedback_I1RoutineBegin(snapshot));
      trials_17LoopScheduler.add(feedback_I1RoutineEachFrame());
      trials_17LoopScheduler.add(feedback_I1RoutineEnd(snapshot));
      trials_17LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_17LoopScheduler.add(ISI250RoutineEachFrame());
      trials_17LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_17LoopScheduler.add(trials_17LoopEndIteration(trials_17LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_17LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_17);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_17LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_18;
function trials_18LoopBegin(trials_18LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_18 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskG2_I1_block2nd_congruent_japan_prefer.xlsx',
      seed: undefined, name: 'trials_18'
    });
    psychoJS.experiment.addLoop(trials_18); // add the loop to the experiment
    currentLoop = trials_18;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_18 of trials_18) {
      snapshot = trials_18.getSnapshot();
      trials_18LoopScheduler.add(importConditions(snapshot));
      trials_18LoopScheduler.add(record_Task_I2RoutineBegin(snapshot));
      trials_18LoopScheduler.add(record_Task_I2RoutineEachFrame());
      trials_18LoopScheduler.add(record_Task_I2RoutineEnd(snapshot));
      trials_18LoopScheduler.add(feedback_I2RoutineBegin(snapshot));
      trials_18LoopScheduler.add(feedback_I2RoutineEachFrame());
      trials_18LoopScheduler.add(feedback_I2RoutineEnd(snapshot));
      trials_18LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_18LoopScheduler.add(ISI250RoutineEachFrame());
      trials_18LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_18LoopScheduler.add(trials_18LoopEndIteration(trials_18LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_18LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_18);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_18LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_19;
function trials_19LoopBegin(trials_19LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_19 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'excel/TaskG2_I1_block1st3rd_congruent_japan_prefer.xlsx',
      seed: undefined, name: 'trials_19'
    });
    psychoJS.experiment.addLoop(trials_19); // add the loop to the experiment
    currentLoop = trials_19;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_19 of trials_19) {
      snapshot = trials_19.getSnapshot();
      trials_19LoopScheduler.add(importConditions(snapshot));
      trials_19LoopScheduler.add(record_Task_I3RoutineBegin(snapshot));
      trials_19LoopScheduler.add(record_Task_I3RoutineEachFrame());
      trials_19LoopScheduler.add(record_Task_I3RoutineEnd(snapshot));
      trials_19LoopScheduler.add(feedback_I3RoutineBegin(snapshot));
      trials_19LoopScheduler.add(feedback_I3RoutineEachFrame());
      trials_19LoopScheduler.add(feedback_I3RoutineEnd(snapshot));
      trials_19LoopScheduler.add(ISI250RoutineBegin(snapshot));
      trials_19LoopScheduler.add(ISI250RoutineEachFrame());
      trials_19LoopScheduler.add(ISI250RoutineEnd(snapshot));
      trials_19LoopScheduler.add(trials_19LoopEndIteration(trials_19LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_19LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_19);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_19LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var reminder_A1MaxDurationReached;
var _key_resp_2_allKeys;
var reminder_A1MaxDuration;
var reminder_A1Components;
function reminder_A1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_A1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_A1Clock.reset();
    routineTimer.reset();
    reminder_A1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('reminder_A1.started', globalClock.getTime());
    reminder_A1MaxDuration = null
    // keep track of which components have finished
    reminder_A1Components = [];
    reminder_A1Components.push(text_2);
    reminder_A1Components.push(key_resp_2);
    
    for (const thisComponent of reminder_A1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_A1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_A1' ---
    // get current time
    t = reminder_A1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_A1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_A1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_A1' ---
    for (const thisComponent of reminder_A1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_A1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "reminder_A1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ISI1500MaxDurationReached;
var ISI1500MaxDuration;
var ISI1500Components;
function ISI1500RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ISI1500' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ISI1500Clock.reset(routineTimer.getTime());
    routineTimer.add(1.500000);
    ISI1500MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('ISI1500.started', globalClock.getTime());
    ISI1500MaxDuration = 1.5
    // keep track of which components have finished
    ISI1500Components = [];
    ISI1500Components.push(text_3);
    
    for (const thisComponent of ISI1500Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ISI1500RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ISI1500' ---
    // get current time
    t = ISI1500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > ISI1500MaxDuration) {
        ISI1500MaxDurationReached = true
        continueRoutine = false
    }
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ISI1500Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISI1500RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ISI1500' ---
    for (const thisComponent of ISI1500Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ISI1500.stopped', globalClock.getTime());
    if (ISI1500MaxDurationReached) {
        ISI1500Clock.add(ISI1500MaxDuration);
    } else {
        ISI1500Clock.add(1.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_Task_A1MaxDurationReached;
var _key_resp_A1_allKeys;
var practice_Task_A1MaxDuration;
var practice_Task_A1Components;
function practice_Task_A1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_Task_A1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_Task_A1Clock.reset();
    routineTimer.reset();
    practice_Task_A1MaxDurationReached = false;
    // update component parameters for each repeat
    text_A1.setText(name);
    key_resp_A1.keys = undefined;
    key_resp_A1.rt = undefined;
    _key_resp_A1_allKeys = [];
    psychoJS.experiment.addData('practice_Task_A1.started', globalClock.getTime());
    practice_Task_A1MaxDuration = null
    // keep track of which components have finished
    practice_Task_A1Components = [];
    practice_Task_A1Components.push(text_A1);
    practice_Task_A1Components.push(key_resp_A1);
    
    for (const thisComponent of practice_Task_A1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_Task_A1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_Task_A1' ---
    // get current time
    t = practice_Task_A1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_A1* updates
    if (t >= 0.0 && text_A1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_A1.tStart = t;  // (not accounting for frame time here)
      text_A1.frameNStart = frameN;  // exact frame index
      
      text_A1.setAutoDraw(true);
    }
    
    
    // *key_resp_A1* updates
    if (t >= 0.0 && key_resp_A1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_A1.tStart = t;  // (not accounting for frame time here)
      key_resp_A1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_A1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_A1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_A1.clearEvents(); });
    }
    
    if (key_resp_A1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_A1.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_A1_allKeys = _key_resp_A1_allKeys.concat(theseKeys);
      if (_key_resp_A1_allKeys.length > 0) {
        key_resp_A1.keys = _key_resp_A1_allKeys[_key_resp_A1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_A1.rt = _key_resp_A1_allKeys[_key_resp_A1_allKeys.length - 1].rt;
        key_resp_A1.duration = _key_resp_A1_allKeys[_key_resp_A1_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_A1.keys == keypad) {
            key_resp_A1.corr = 1;
        } else {
            key_resp_A1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_Task_A1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_Task_A1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_Task_A1' ---
    for (const thisComponent of practice_Task_A1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_Task_A1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_A1.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_A1.corr = 1;  // correct non-response
      } else {
         key_resp_A1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_A1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_A1.keys', key_resp_A1.keys);
    psychoJS.experiment.addData('key_resp_A1.corr', key_resp_A1.corr);
    if (typeof key_resp_A1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_A1.rt', key_resp_A1.rt);
        psychoJS.experiment.addData('key_resp_A1.duration', key_resp_A1.duration);
        routineTimer.reset();
        }
    
    key_resp_A1.stop();
    // the Routine "practice_Task_A1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_A1MaxDurationReached;
var feedback_A1MaxDuration;
var feedback_A1Components;
function feedback_A1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_A1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_A1Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_A1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_A1
    key_resp_A1_rt_sum_temp = (key_resp_A1_rt_sum_temp + Number.parseFloat(key_resp_A1.rt.toString()));
    if (key_resp_A1.corr) {
        key_resp_A1_corr_sum_temp = (key_resp_A1_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_A1.setText(msg);
    psychoJS.experiment.addData('feedback_A1.started', globalClock.getTime());
    feedback_A1MaxDuration = null
    // keep track of which components have finished
    feedback_A1Components = [];
    feedback_A1Components.push(feedback_text_A1);
    
    for (const thisComponent of feedback_A1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_A1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_A1' ---
    // get current time
    t = feedback_A1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_A1* updates
    if (t >= 0.0 && feedback_text_A1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_A1.tStart = t;  // (not accounting for frame time here)
      feedback_text_A1.frameNStart = frameN;  // exact frame index
      
      feedback_text_A1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_A1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_A1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_A1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_A1_corr_sum;
var key_resp_A1_rt_sum;
function feedback_A1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_A1' ---
    for (const thisComponent of feedback_A1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_A1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_A1
    key_resp_A1_corr_sum = key_resp_A1_corr_sum_temp;
    key_resp_A1_rt_sum = key_resp_A1_rt_sum_temp;
    
    if (feedback_A1MaxDurationReached) {
        feedback_A1Clock.add(feedback_A1MaxDuration);
    } else {
        feedback_A1Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ISI250MaxDurationReached;
var ISI250MaxDuration;
var ISI250Components;
function ISI250RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ISI250' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ISI250Clock.reset(routineTimer.getTime());
    routineTimer.add(0.250000);
    ISI250MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('ISI250.started', globalClock.getTime());
    ISI250MaxDuration = 0.25
    // keep track of which components have finished
    ISI250Components = [];
    
    for (const thisComponent of ISI250Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ISI250RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ISI250' ---
    // get current time
    t = ISI250Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > ISI250MaxDuration) {
        ISI250MaxDurationReached = true
        continueRoutine = false
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ISI250Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISI250RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ISI250' ---
    for (const thisComponent of ISI250Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ISI250.stopped', globalClock.getTime());
    if (ISI250MaxDurationReached) {
        ISI250Clock.add(ISI250MaxDuration);
    } else {
        ISI250Clock.add(0.250000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_A1MaxDurationReached;
var _key_resp_score_allKeys;
var accuracy;
var rt_average;
var score_A1MaxDuration;
var score_A1Components;
function score_A1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_A1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_A1Clock.reset();
    routineTimer.reset();
    score_A1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_score.keys = undefined;
    key_resp_score.rt = undefined;
    _key_resp_score_allKeys = [];
    // Run 'Begin Routine' code from score_A1_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_A1_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_A1_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    psychoJS.experiment.addData('score_A1.started', globalClock.getTime());
    score_A1MaxDuration = null
    // keep track of which components have finished
    score_A1Components = [];
    score_A1Components.push(score_A1_text);
    score_A1Components.push(key_resp_score);
    
    for (const thisComponent of score_A1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_A1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_A1' ---
    // get current time
    t = score_A1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_A1_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_A1_text.setText(feedback_msg, false);
    }
    
    // *score_A1_text* updates
    if (t >= 0.0 && score_A1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_A1_text.tStart = t;  // (not accounting for frame time here)
      score_A1_text.frameNStart = frameN;  // exact frame index
      
      score_A1_text.setAutoDraw(true);
    }
    
    
    // *key_resp_score* updates
    if (t >= 0.0 && key_resp_score.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_score.tStart = t;  // (not accounting for frame time here)
      key_resp_score.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_score.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_score.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_score.clearEvents(); });
    }
    
    if (key_resp_score.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_score.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_score_allKeys = _key_resp_score_allKeys.concat(theseKeys);
      if (_key_resp_score_allKeys.length > 0) {
        key_resp_score.keys = _key_resp_score_allKeys[_key_resp_score_allKeys.length - 1].name;  // just the last key pressed
        key_resp_score.rt = _key_resp_score_allKeys[_key_resp_score_allKeys.length - 1].rt;
        key_resp_score.duration = _key_resp_score_allKeys[_key_resp_score_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_A1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_A1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_A1' ---
    for (const thisComponent of score_A1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_A1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_score.corr, level);
    }
    psychoJS.experiment.addData('key_resp_score.keys', key_resp_score.keys);
    if (typeof key_resp_score.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_score.rt', key_resp_score.rt);
        psychoJS.experiment.addData('key_resp_score.duration', key_resp_score.duration);
        routineTimer.reset();
        }
    
    key_resp_score.stop();
    // the Routine "score_A1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_A2MaxDurationReached;
var _key_resp_23_allKeys;
var reminder_A2MaxDuration;
var reminder_A2Components;
function reminder_A2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_A2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_A2Clock.reset();
    routineTimer.reset();
    reminder_A2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_23.keys = undefined;
    key_resp_23.rt = undefined;
    _key_resp_23_allKeys = [];
    psychoJS.experiment.addData('reminder_A2.started', globalClock.getTime());
    reminder_A2MaxDuration = null
    // keep track of which components have finished
    reminder_A2Components = [];
    reminder_A2Components.push(text_45);
    reminder_A2Components.push(key_resp_23);
    
    for (const thisComponent of reminder_A2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_A2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_A2' ---
    // get current time
    t = reminder_A2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_45* updates
    if (t >= 0.0 && text_45.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_45.tStart = t;  // (not accounting for frame time here)
      text_45.frameNStart = frameN;  // exact frame index
      
      text_45.setAutoDraw(true);
    }
    
    
    // *key_resp_23* updates
    if (t >= 0.0 && key_resp_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_23.tStart = t;  // (not accounting for frame time here)
      key_resp_23.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_23.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_23.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_23.clearEvents(); });
    }
    
    if (key_resp_23.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_23.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_23_allKeys = _key_resp_23_allKeys.concat(theseKeys);
      if (_key_resp_23_allKeys.length > 0) {
        key_resp_23.keys = _key_resp_23_allKeys[_key_resp_23_allKeys.length - 1].name;  // just the last key pressed
        key_resp_23.rt = _key_resp_23_allKeys[_key_resp_23_allKeys.length - 1].rt;
        key_resp_23.duration = _key_resp_23_allKeys[_key_resp_23_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_A2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_A2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_A2' ---
    for (const thisComponent of reminder_A2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_A2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_23.corr, level);
    }
    psychoJS.experiment.addData('key_resp_23.keys', key_resp_23.keys);
    if (typeof key_resp_23.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_23.rt', key_resp_23.rt);
        psychoJS.experiment.addData('key_resp_23.duration', key_resp_23.duration);
        routineTimer.reset();
        }
    
    key_resp_23.stop();
    // the Routine "reminder_A2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_A2MaxDurationReached;
var _key_resp_A2_allKeys;
var record_Task_A2MaxDuration;
var record_Task_A2Components;
function record_Task_A2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_A2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_A2Clock.reset();
    routineTimer.reset();
    record_Task_A2MaxDurationReached = false;
    // update component parameters for each repeat
    text_A2.setText(name);
    key_resp_A2.keys = undefined;
    key_resp_A2.rt = undefined;
    _key_resp_A2_allKeys = [];
    psychoJS.experiment.addData('record_Task_A2.started', globalClock.getTime());
    record_Task_A2MaxDuration = null
    // keep track of which components have finished
    record_Task_A2Components = [];
    record_Task_A2Components.push(text_A2);
    record_Task_A2Components.push(key_resp_A2);
    
    for (const thisComponent of record_Task_A2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_A2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_A2' ---
    // get current time
    t = record_Task_A2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_A2* updates
    if (t >= 0.0 && text_A2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_A2.tStart = t;  // (not accounting for frame time here)
      text_A2.frameNStart = frameN;  // exact frame index
      
      text_A2.setAutoDraw(true);
    }
    
    
    // *key_resp_A2* updates
    if (t >= 0.0 && key_resp_A2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_A2.tStart = t;  // (not accounting for frame time here)
      key_resp_A2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_A2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_A2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_A2.clearEvents(); });
    }
    
    if (key_resp_A2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_A2.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_A2_allKeys = _key_resp_A2_allKeys.concat(theseKeys);
      if (_key_resp_A2_allKeys.length > 0) {
        key_resp_A2.keys = _key_resp_A2_allKeys[_key_resp_A2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_A2.rt = _key_resp_A2_allKeys[_key_resp_A2_allKeys.length - 1].rt;
        key_resp_A2.duration = _key_resp_A2_allKeys[_key_resp_A2_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_A2.keys == keypad) {
            key_resp_A2.corr = 1;
        } else {
            key_resp_A2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_A2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_A2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_A2' ---
    for (const thisComponent of record_Task_A2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_A2.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_A2.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_A2.corr = 1;  // correct non-response
      } else {
         key_resp_A2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_A2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_A2.keys', key_resp_A2.keys);
    psychoJS.experiment.addData('key_resp_A2.corr', key_resp_A2.corr);
    if (typeof key_resp_A2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_A2.rt', key_resp_A2.rt);
        psychoJS.experiment.addData('key_resp_A2.duration', key_resp_A2.duration);
        routineTimer.reset();
        }
    
    key_resp_A2.stop();
    // the Routine "record_Task_A2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_A2MaxDurationReached;
var feedback_A2MaxDuration;
var feedback_A2Components;
function feedback_A2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_A2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_A2Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_A2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_A2
    key_resp_A2_rt_sum_temp = (key_resp_A2_rt_sum_temp + Number.parseFloat(key_resp_A2.rt.toString()));
    if (key_resp_A2.corr) {
        key_resp_A2_corr_sum_temp = (key_resp_A2_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_A2.setText(msg);
    psychoJS.experiment.addData('feedback_A2.started', globalClock.getTime());
    feedback_A2MaxDuration = null
    // keep track of which components have finished
    feedback_A2Components = [];
    feedback_A2Components.push(feedback_text_A2);
    
    for (const thisComponent of feedback_A2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_A2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_A2' ---
    // get current time
    t = feedback_A2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_A2* updates
    if (t >= 0.0 && feedback_text_A2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_A2.tStart = t;  // (not accounting for frame time here)
      feedback_text_A2.frameNStart = frameN;  // exact frame index
      
      feedback_text_A2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_A2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_A2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_A2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_A2_corr_sum;
var key_resp_A2_rt_sum;
function feedback_A2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_A2' ---
    for (const thisComponent of feedback_A2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_A2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_A2
    key_resp_A2_corr_sum = key_resp_A2_corr_sum_temp;
    key_resp_A2_rt_sum = key_resp_A2_rt_sum_temp;
    
    if (feedback_A2MaxDurationReached) {
        feedback_A2Clock.add(feedback_A2MaxDuration);
    } else {
        feedback_A2Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_A2MaxDurationReached;
var _key_resp_3_allKeys;
var score_A2MaxDuration;
var score_A2Components;
function score_A2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_A2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_A2Clock.reset();
    routineTimer.reset();
    score_A2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // Run 'Begin Routine' code from score_A2_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_A2_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_A2_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    psychoJS.experiment.addData('score_A2.started', globalClock.getTime());
    score_A2MaxDuration = null
    // keep track of which components have finished
    score_A2Components = [];
    score_A2Components.push(score_A2_text);
    score_A2Components.push(key_resp_3);
    
    for (const thisComponent of score_A2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_A2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_A2' ---
    // get current time
    t = score_A2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_A2_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_A2_text.setText(feedback_msg, false);
    }
    
    // *score_A2_text* updates
    if (t >= 0.0 && score_A2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_A2_text.tStart = t;  // (not accounting for frame time here)
      score_A2_text.frameNStart = frameN;  // exact frame index
      
      score_A2_text.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_A2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_A2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_A2' ---
    for (const thisComponent of score_A2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_A2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "score_A2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_B1MaxDurationReached;
var _key_resp_24_allKeys;
var reminder_B1MaxDuration;
var reminder_B1Components;
function reminder_B1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_B1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_B1Clock.reset();
    routineTimer.reset();
    reminder_B1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_24.keys = undefined;
    key_resp_24.rt = undefined;
    _key_resp_24_allKeys = [];
    psychoJS.experiment.addData('reminder_B1.started', globalClock.getTime());
    reminder_B1MaxDuration = null
    // keep track of which components have finished
    reminder_B1Components = [];
    reminder_B1Components.push(text_46);
    reminder_B1Components.push(key_resp_24);
    
    for (const thisComponent of reminder_B1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_B1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_B1' ---
    // get current time
    t = reminder_B1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_46* updates
    if (t >= 0.0 && text_46.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_46.tStart = t;  // (not accounting for frame time here)
      text_46.frameNStart = frameN;  // exact frame index
      
      text_46.setAutoDraw(true);
    }
    
    
    // *key_resp_24* updates
    if (t >= 0.0 && key_resp_24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_24.tStart = t;  // (not accounting for frame time here)
      key_resp_24.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_24.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_24.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_24.clearEvents(); });
    }
    
    if (key_resp_24.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_24.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_24_allKeys = _key_resp_24_allKeys.concat(theseKeys);
      if (_key_resp_24_allKeys.length > 0) {
        key_resp_24.keys = _key_resp_24_allKeys[_key_resp_24_allKeys.length - 1].name;  // just the last key pressed
        key_resp_24.rt = _key_resp_24_allKeys[_key_resp_24_allKeys.length - 1].rt;
        key_resp_24.duration = _key_resp_24_allKeys[_key_resp_24_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_B1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_B1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_B1' ---
    for (const thisComponent of reminder_B1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_B1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_24.corr, level);
    }
    psychoJS.experiment.addData('key_resp_24.keys', key_resp_24.keys);
    if (typeof key_resp_24.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_24.rt', key_resp_24.rt);
        psychoJS.experiment.addData('key_resp_24.duration', key_resp_24.duration);
        routineTimer.reset();
        }
    
    key_resp_24.stop();
    // the Routine "reminder_B1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_Task_B1MaxDurationReached;
var _key_resp_B1_allKeys;
var practice_Task_B1MaxDuration;
var practice_Task_B1Components;
function practice_Task_B1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_Task_B1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_Task_B1Clock.reset();
    routineTimer.reset();
    practice_Task_B1MaxDurationReached = false;
    // update component parameters for each repeat
    text_B1.setText(words);
    key_resp_B1.keys = undefined;
    key_resp_B1.rt = undefined;
    _key_resp_B1_allKeys = [];
    psychoJS.experiment.addData('practice_Task_B1.started', globalClock.getTime());
    practice_Task_B1MaxDuration = null
    // keep track of which components have finished
    practice_Task_B1Components = [];
    practice_Task_B1Components.push(text_B1);
    practice_Task_B1Components.push(key_resp_B1);
    
    for (const thisComponent of practice_Task_B1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_Task_B1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_Task_B1' ---
    // get current time
    t = practice_Task_B1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_B1* updates
    if (t >= 0.0 && text_B1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_B1.tStart = t;  // (not accounting for frame time here)
      text_B1.frameNStart = frameN;  // exact frame index
      
      text_B1.setAutoDraw(true);
    }
    
    
    // *key_resp_B1* updates
    if (t >= 0.0 && key_resp_B1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_B1.tStart = t;  // (not accounting for frame time here)
      key_resp_B1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_B1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_B1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_B1.clearEvents(); });
    }
    
    if (key_resp_B1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_B1.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_B1_allKeys = _key_resp_B1_allKeys.concat(theseKeys);
      if (_key_resp_B1_allKeys.length > 0) {
        key_resp_B1.keys = _key_resp_B1_allKeys[_key_resp_B1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_B1.rt = _key_resp_B1_allKeys[_key_resp_B1_allKeys.length - 1].rt;
        key_resp_B1.duration = _key_resp_B1_allKeys[_key_resp_B1_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_B1.keys == keypad) {
            key_resp_B1.corr = 1;
        } else {
            key_resp_B1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_Task_B1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_Task_B1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_Task_B1' ---
    for (const thisComponent of practice_Task_B1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_Task_B1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_B1.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_B1.corr = 1;  // correct non-response
      } else {
         key_resp_B1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_B1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_B1.keys', key_resp_B1.keys);
    psychoJS.experiment.addData('key_resp_B1.corr', key_resp_B1.corr);
    if (typeof key_resp_B1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_B1.rt', key_resp_B1.rt);
        psychoJS.experiment.addData('key_resp_B1.duration', key_resp_B1.duration);
        routineTimer.reset();
        }
    
    key_resp_B1.stop();
    // the Routine "practice_Task_B1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_B1MaxDurationReached;
var feedback_B1MaxDuration;
var feedback_B1Components;
function feedback_B1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_B1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_B1Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_B1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_B1
    key_resp_B1_rt_sum_temp = (key_resp_B1_rt_sum_temp + Number.parseFloat(key_resp_B1.rt.toString()));
    if (key_resp_B1.corr) {
        key_resp_B1_corr_sum_temp = (key_resp_B1_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_B1.setText(msg);
    psychoJS.experiment.addData('feedback_B1.started', globalClock.getTime());
    feedback_B1MaxDuration = null
    // keep track of which components have finished
    feedback_B1Components = [];
    feedback_B1Components.push(feedback_text_B1);
    
    for (const thisComponent of feedback_B1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_B1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_B1' ---
    // get current time
    t = feedback_B1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_B1* updates
    if (t >= 0.0 && feedback_text_B1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_B1.tStart = t;  // (not accounting for frame time here)
      feedback_text_B1.frameNStart = frameN;  // exact frame index
      
      feedback_text_B1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_B1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_B1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_B1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_B1_corr_sum;
var key_resp_B1_rt_sum;
function feedback_B1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_B1' ---
    for (const thisComponent of feedback_B1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_B1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_B1
    key_resp_B1_corr_sum = key_resp_B1_corr_sum_temp;
    key_resp_B1_rt_sum = key_resp_B1_rt_sum_temp;
    
    if (feedback_B1MaxDurationReached) {
        feedback_B1Clock.add(feedback_B1MaxDuration);
    } else {
        feedback_B1Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_B1MaxDurationReached;
var _key_resp_6_allKeys;
var score_B1MaxDuration;
var score_B1Components;
function score_B1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_B1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_B1Clock.reset();
    routineTimer.reset();
    score_B1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // Run 'Begin Routine' code from score_B1_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_B1_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_B1_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    psychoJS.experiment.addData('score_B1.started', globalClock.getTime());
    score_B1MaxDuration = null
    // keep track of which components have finished
    score_B1Components = [];
    score_B1Components.push(score_B1_text);
    score_B1Components.push(key_resp_6);
    
    for (const thisComponent of score_B1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_B1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_B1' ---
    // get current time
    t = score_B1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_B1_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_B1_text.setText(feedback_msg, false);
    }
    
    // *score_B1_text* updates
    if (t >= 0.0 && score_B1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_B1_text.tStart = t;  // (not accounting for frame time here)
      score_B1_text.frameNStart = frameN;  // exact frame index
      
      score_B1_text.setAutoDraw(true);
    }
    
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }
    
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        key_resp_6.duration = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_B1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_B1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_B1' ---
    for (const thisComponent of score_B1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_B1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "score_B1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_B2MaxDurationReached;
var _key_resp_25_allKeys;
var reminder_B2MaxDuration;
var reminder_B2Components;
function reminder_B2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_B2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_B2Clock.reset();
    routineTimer.reset();
    reminder_B2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_25.keys = undefined;
    key_resp_25.rt = undefined;
    _key_resp_25_allKeys = [];
    psychoJS.experiment.addData('reminder_B2.started', globalClock.getTime());
    reminder_B2MaxDuration = null
    // keep track of which components have finished
    reminder_B2Components = [];
    reminder_B2Components.push(text_47);
    reminder_B2Components.push(key_resp_25);
    
    for (const thisComponent of reminder_B2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_B2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_B2' ---
    // get current time
    t = reminder_B2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_47* updates
    if (t >= 0.0 && text_47.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_47.tStart = t;  // (not accounting for frame time here)
      text_47.frameNStart = frameN;  // exact frame index
      
      text_47.setAutoDraw(true);
    }
    
    
    // *key_resp_25* updates
    if (t >= 0.0 && key_resp_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_25.tStart = t;  // (not accounting for frame time here)
      key_resp_25.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_25.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_25.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_25.clearEvents(); });
    }
    
    if (key_resp_25.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_25.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_25_allKeys = _key_resp_25_allKeys.concat(theseKeys);
      if (_key_resp_25_allKeys.length > 0) {
        key_resp_25.keys = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].name;  // just the last key pressed
        key_resp_25.rt = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].rt;
        key_resp_25.duration = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_B2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_B2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_B2' ---
    for (const thisComponent of reminder_B2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_B2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_25.corr, level);
    }
    psychoJS.experiment.addData('key_resp_25.keys', key_resp_25.keys);
    if (typeof key_resp_25.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_25.rt', key_resp_25.rt);
        psychoJS.experiment.addData('key_resp_25.duration', key_resp_25.duration);
        routineTimer.reset();
        }
    
    key_resp_25.stop();
    // the Routine "reminder_B2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_B2MaxDurationReached;
var _key_resp_B2_allKeys;
var record_Task_B2MaxDuration;
var record_Task_B2Components;
function record_Task_B2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_B2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_B2Clock.reset();
    routineTimer.reset();
    record_Task_B2MaxDurationReached = false;
    // update component parameters for each repeat
    text_B2.setText(words);
    key_resp_B2.keys = undefined;
    key_resp_B2.rt = undefined;
    _key_resp_B2_allKeys = [];
    psychoJS.experiment.addData('record_Task_B2.started', globalClock.getTime());
    record_Task_B2MaxDuration = null
    // keep track of which components have finished
    record_Task_B2Components = [];
    record_Task_B2Components.push(text_B2);
    record_Task_B2Components.push(key_resp_B2);
    
    for (const thisComponent of record_Task_B2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_B2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_B2' ---
    // get current time
    t = record_Task_B2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_B2* updates
    if (t >= 0.0 && text_B2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_B2.tStart = t;  // (not accounting for frame time here)
      text_B2.frameNStart = frameN;  // exact frame index
      
      text_B2.setAutoDraw(true);
    }
    
    
    // *key_resp_B2* updates
    if (t >= 0.0 && key_resp_B2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_B2.tStart = t;  // (not accounting for frame time here)
      key_resp_B2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_B2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_B2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_B2.clearEvents(); });
    }
    
    if (key_resp_B2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_B2.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_B2_allKeys = _key_resp_B2_allKeys.concat(theseKeys);
      if (_key_resp_B2_allKeys.length > 0) {
        key_resp_B2.keys = _key_resp_B2_allKeys[_key_resp_B2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_B2.rt = _key_resp_B2_allKeys[_key_resp_B2_allKeys.length - 1].rt;
        key_resp_B2.duration = _key_resp_B2_allKeys[_key_resp_B2_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_B2.keys == keypad) {
            key_resp_B2.corr = 1;
        } else {
            key_resp_B2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_B2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_B2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_B2' ---
    for (const thisComponent of record_Task_B2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_B2.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_B2.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_B2.corr = 1;  // correct non-response
      } else {
         key_resp_B2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_B2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_B2.keys', key_resp_B2.keys);
    psychoJS.experiment.addData('key_resp_B2.corr', key_resp_B2.corr);
    if (typeof key_resp_B2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_B2.rt', key_resp_B2.rt);
        psychoJS.experiment.addData('key_resp_B2.duration', key_resp_B2.duration);
        routineTimer.reset();
        }
    
    key_resp_B2.stop();
    // the Routine "record_Task_B2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_B2MaxDurationReached;
var feedback_B2MaxDuration;
var feedback_B2Components;
function feedback_B2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_B2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_B2Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_B2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_B2
    key_resp_B2_rt_sum_temp = (key_resp_B2_rt_sum_temp + Number.parseFloat(key_resp_B2.rt.toString()));
    if (key_resp_B2.corr) {
        key_resp_B2_corr_sum_temp = (key_resp_B2_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_B2.setText(msg);
    psychoJS.experiment.addData('feedback_B2.started', globalClock.getTime());
    feedback_B2MaxDuration = null
    // keep track of which components have finished
    feedback_B2Components = [];
    feedback_B2Components.push(feedback_text_B2);
    
    for (const thisComponent of feedback_B2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_B2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_B2' ---
    // get current time
    t = feedback_B2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_B2* updates
    if (t >= 0.0 && feedback_text_B2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_B2.tStart = t;  // (not accounting for frame time here)
      feedback_text_B2.frameNStart = frameN;  // exact frame index
      
      feedback_text_B2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_B2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_B2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_B2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_B2_corr_sum;
var key_resp_B2_rt_sum;
function feedback_B2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_B2' ---
    for (const thisComponent of feedback_B2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_B2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_B2
    key_resp_B2_corr_sum = key_resp_B2_corr_sum_temp;
    key_resp_B2_rt_sum = key_resp_B2_rt_sum_temp;
    
    if (feedback_B2MaxDurationReached) {
        feedback_B2Clock.add(feedback_B2MaxDuration);
    } else {
        feedback_B2Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_B2MaxDurationReached;
var _key_resp_4_allKeys;
var score_B2MaxDuration;
var score_B2Components;
function score_B2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_B2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_B2Clock.reset();
    routineTimer.reset();
    score_B2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // Run 'Begin Routine' code from score_B2_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_B2_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_B2_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    psychoJS.experiment.addData('score_B2.started', globalClock.getTime());
    score_B2MaxDuration = null
    // keep track of which components have finished
    score_B2Components = [];
    score_B2Components.push(score_B2_text);
    score_B2Components.push(key_resp_4);
    
    for (const thisComponent of score_B2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_B2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_B2' ---
    // get current time
    t = score_B2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_B2_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_B2_text.setText(feedback_msg, false);
    }
    
    // *score_B2_text* updates
    if (t >= 0.0 && score_B2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_B2_text.tStart = t;  // (not accounting for frame time here)
      score_B2_text.frameNStart = frameN;  // exact frame index
      
      score_B2_text.setAutoDraw(true);
    }
    
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_B2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_B2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_B2' ---
    for (const thisComponent of score_B2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_B2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "score_B2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_C1MaxDurationReached;
var _key_resp_26_allKeys;
var reminder_C1MaxDuration;
var reminder_C1Components;
function reminder_C1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_C1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_C1Clock.reset();
    routineTimer.reset();
    reminder_C1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_26.keys = undefined;
    key_resp_26.rt = undefined;
    _key_resp_26_allKeys = [];
    psychoJS.experiment.addData('reminder_C1.started', globalClock.getTime());
    reminder_C1MaxDuration = null
    // keep track of which components have finished
    reminder_C1Components = [];
    reminder_C1Components.push(text_20);
    reminder_C1Components.push(key_resp_26);
    
    for (const thisComponent of reminder_C1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_C1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_C1' ---
    // get current time
    t = reminder_C1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_20* updates
    if (t >= 0.0 && text_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_20.tStart = t;  // (not accounting for frame time here)
      text_20.frameNStart = frameN;  // exact frame index
      
      text_20.setAutoDraw(true);
    }
    
    
    // *key_resp_26* updates
    if (t >= 0.0 && key_resp_26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_26.tStart = t;  // (not accounting for frame time here)
      key_resp_26.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_26.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_26.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_26.clearEvents(); });
    }
    
    if (key_resp_26.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_26.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_26_allKeys = _key_resp_26_allKeys.concat(theseKeys);
      if (_key_resp_26_allKeys.length > 0) {
        key_resp_26.keys = _key_resp_26_allKeys[_key_resp_26_allKeys.length - 1].name;  // just the last key pressed
        key_resp_26.rt = _key_resp_26_allKeys[_key_resp_26_allKeys.length - 1].rt;
        key_resp_26.duration = _key_resp_26_allKeys[_key_resp_26_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_C1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_C1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_C1' ---
    for (const thisComponent of reminder_C1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_C1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_26.corr, level);
    }
    psychoJS.experiment.addData('key_resp_26.keys', key_resp_26.keys);
    if (typeof key_resp_26.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_26.rt', key_resp_26.rt);
        psychoJS.experiment.addData('key_resp_26.duration', key_resp_26.duration);
        routineTimer.reset();
        }
    
    key_resp_26.stop();
    // the Routine "reminder_C1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_C1MaxDurationReached;
var _key_resp_C1_allKeys;
var record_Task_C1MaxDuration;
var record_Task_C1Components;
function record_Task_C1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_C1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_C1Clock.reset();
    routineTimer.reset();
    record_Task_C1MaxDurationReached = false;
    // update component parameters for each repeat
    text_C1.setText(words);
    key_resp_C1.keys = undefined;
    key_resp_C1.rt = undefined;
    _key_resp_C1_allKeys = [];
    psychoJS.experiment.addData('record_Task_C1.started', globalClock.getTime());
    record_Task_C1MaxDuration = null
    // keep track of which components have finished
    record_Task_C1Components = [];
    record_Task_C1Components.push(text_C1);
    record_Task_C1Components.push(key_resp_C1);
    
    for (const thisComponent of record_Task_C1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_C1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_C1' ---
    // get current time
    t = record_Task_C1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_C1* updates
    if (t >= 0.0 && text_C1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_C1.tStart = t;  // (not accounting for frame time here)
      text_C1.frameNStart = frameN;  // exact frame index
      
      text_C1.setAutoDraw(true);
    }
    
    
    // *key_resp_C1* updates
    if (t >= 0.0 && key_resp_C1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_C1.tStart = t;  // (not accounting for frame time here)
      key_resp_C1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_C1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_C1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_C1.clearEvents(); });
    }
    
    if (key_resp_C1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_C1.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_C1_allKeys = _key_resp_C1_allKeys.concat(theseKeys);
      if (_key_resp_C1_allKeys.length > 0) {
        key_resp_C1.keys = _key_resp_C1_allKeys[_key_resp_C1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_C1.rt = _key_resp_C1_allKeys[_key_resp_C1_allKeys.length - 1].rt;
        key_resp_C1.duration = _key_resp_C1_allKeys[_key_resp_C1_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_C1.keys == keypad) {
            key_resp_C1.corr = 1;
        } else {
            key_resp_C1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_C1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_C1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_C1' ---
    for (const thisComponent of record_Task_C1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_C1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_C1.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_C1.corr = 1;  // correct non-response
      } else {
         key_resp_C1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_C1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_C1.keys', key_resp_C1.keys);
    psychoJS.experiment.addData('key_resp_C1.corr', key_resp_C1.corr);
    if (typeof key_resp_C1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_C1.rt', key_resp_C1.rt);
        psychoJS.experiment.addData('key_resp_C1.duration', key_resp_C1.duration);
        routineTimer.reset();
        }
    
    key_resp_C1.stop();
    // the Routine "record_Task_C1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_C1MaxDurationReached;
var feedback_C1MaxDuration;
var feedback_C1Components;
function feedback_C1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_C1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_C1Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_C1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_C1
    key_resp_C1_rt_sum_temp = (key_resp_C1_rt_sum_temp + Number.parseFloat(key_resp_C1.rt.toString()));
    if (key_resp_C1.corr) {
        key_resp_C1_corr_sum_temp = (key_resp_C1_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_C1.setText(msg);
    psychoJS.experiment.addData('feedback_C1.started', globalClock.getTime());
    feedback_C1MaxDuration = null
    // keep track of which components have finished
    feedback_C1Components = [];
    feedback_C1Components.push(feedback_text_C1);
    
    for (const thisComponent of feedback_C1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_C1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_C1' ---
    // get current time
    t = feedback_C1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_C1* updates
    if (t >= 0.0 && feedback_text_C1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_C1.tStart = t;  // (not accounting for frame time here)
      feedback_text_C1.frameNStart = frameN;  // exact frame index
      
      feedback_text_C1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_C1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_C1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_C1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_C1_corr_sum;
var key_resp_C1_rt_sum;
function feedback_C1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_C1' ---
    for (const thisComponent of feedback_C1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_C1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_C1
    key_resp_C1_corr_sum = key_resp_C1_corr_sum_temp;
    key_resp_C1_rt_sum = key_resp_C1_rt_sum_temp;
    
    if (feedback_C1MaxDurationReached) {
        feedback_C1Clock.add(feedback_C1MaxDuration);
    } else {
        feedback_C1Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_C1MaxDurationReached;
var _key_resp_5_allKeys;
var score_C1MaxDuration;
var score_C1Components;
function score_C1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_C1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_C1Clock.reset();
    routineTimer.reset();
    score_C1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_C1_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_C1_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_C1_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('score_C1.started', globalClock.getTime());
    score_C1MaxDuration = null
    // keep track of which components have finished
    score_C1Components = [];
    score_C1Components.push(score_C1_text);
    score_C1Components.push(key_resp_5);
    
    for (const thisComponent of score_C1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_C1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_C1' ---
    // get current time
    t = score_C1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_C1_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_C1_text.setText(feedback_msg, false);
    }
    
    // *score_C1_text* updates
    if (t >= 0.0 && score_C1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_C1_text.tStart = t;  // (not accounting for frame time here)
      score_C1_text.frameNStart = frameN;  // exact frame index
      
      score_C1_text.setAutoDraw(true);
    }
    
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_C1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_C1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_C1' ---
    for (const thisComponent of score_C1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_C1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "score_C1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_C2MaxDurationReached;
var _key_resp_27_allKeys;
var reminder_C2MaxDuration;
var reminder_C2Components;
function reminder_C2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_C2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_C2Clock.reset();
    routineTimer.reset();
    reminder_C2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_27.keys = undefined;
    key_resp_27.rt = undefined;
    _key_resp_27_allKeys = [];
    psychoJS.experiment.addData('reminder_C2.started', globalClock.getTime());
    reminder_C2MaxDuration = null
    // keep track of which components have finished
    reminder_C2Components = [];
    reminder_C2Components.push(text_21);
    reminder_C2Components.push(key_resp_27);
    
    for (const thisComponent of reminder_C2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_C2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_C2' ---
    // get current time
    t = reminder_C2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_21* updates
    if (t >= 0.0 && text_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_21.tStart = t;  // (not accounting for frame time here)
      text_21.frameNStart = frameN;  // exact frame index
      
      text_21.setAutoDraw(true);
    }
    
    
    // *key_resp_27* updates
    if (t >= 0.0 && key_resp_27.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_27.tStart = t;  // (not accounting for frame time here)
      key_resp_27.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_27.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_27.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_27.clearEvents(); });
    }
    
    if (key_resp_27.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_27.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_27_allKeys = _key_resp_27_allKeys.concat(theseKeys);
      if (_key_resp_27_allKeys.length > 0) {
        key_resp_27.keys = _key_resp_27_allKeys[_key_resp_27_allKeys.length - 1].name;  // just the last key pressed
        key_resp_27.rt = _key_resp_27_allKeys[_key_resp_27_allKeys.length - 1].rt;
        key_resp_27.duration = _key_resp_27_allKeys[_key_resp_27_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_C2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_C2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_C2' ---
    for (const thisComponent of reminder_C2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_C2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_27.corr, level);
    }
    psychoJS.experiment.addData('key_resp_27.keys', key_resp_27.keys);
    if (typeof key_resp_27.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_27.rt', key_resp_27.rt);
        psychoJS.experiment.addData('key_resp_27.duration', key_resp_27.duration);
        routineTimer.reset();
        }
    
    key_resp_27.stop();
    // the Routine "reminder_C2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_C2MaxDurationReached;
var _key_resp_C2_allKeys;
var record_Task_C2MaxDuration;
var record_Task_C2Components;
function record_Task_C2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_C2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_C2Clock.reset();
    routineTimer.reset();
    record_Task_C2MaxDurationReached = false;
    // update component parameters for each repeat
    text_C2.setText(words);
    key_resp_C2.keys = undefined;
    key_resp_C2.rt = undefined;
    _key_resp_C2_allKeys = [];
    psychoJS.experiment.addData('record_Task_C2.started', globalClock.getTime());
    record_Task_C2MaxDuration = null
    // keep track of which components have finished
    record_Task_C2Components = [];
    record_Task_C2Components.push(text_C2);
    record_Task_C2Components.push(key_resp_C2);
    
    for (const thisComponent of record_Task_C2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_C2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_C2' ---
    // get current time
    t = record_Task_C2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_C2* updates
    if (t >= 0.0 && text_C2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_C2.tStart = t;  // (not accounting for frame time here)
      text_C2.frameNStart = frameN;  // exact frame index
      
      text_C2.setAutoDraw(true);
    }
    
    
    // *key_resp_C2* updates
    if (t >= 0.0 && key_resp_C2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_C2.tStart = t;  // (not accounting for frame time here)
      key_resp_C2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_C2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_C2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_C2.clearEvents(); });
    }
    
    if (key_resp_C2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_C2.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_C2_allKeys = _key_resp_C2_allKeys.concat(theseKeys);
      if (_key_resp_C2_allKeys.length > 0) {
        key_resp_C2.keys = _key_resp_C2_allKeys[_key_resp_C2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_C2.rt = _key_resp_C2_allKeys[_key_resp_C2_allKeys.length - 1].rt;
        key_resp_C2.duration = _key_resp_C2_allKeys[_key_resp_C2_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_C2.keys == keypad) {
            key_resp_C2.corr = 1;
        } else {
            key_resp_C2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_C2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_C2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_C2' ---
    for (const thisComponent of record_Task_C2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_C2.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_C2.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_C2.corr = 1;  // correct non-response
      } else {
         key_resp_C2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_C2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_C2.keys', key_resp_C2.keys);
    psychoJS.experiment.addData('key_resp_C2.corr', key_resp_C2.corr);
    if (typeof key_resp_C2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_C2.rt', key_resp_C2.rt);
        psychoJS.experiment.addData('key_resp_C2.duration', key_resp_C2.duration);
        routineTimer.reset();
        }
    
    key_resp_C2.stop();
    // the Routine "record_Task_C2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_C2MaxDurationReached;
var feedback_C2MaxDuration;
var feedback_C2Components;
function feedback_C2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_C2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_C2Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_C2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_C2
    key_resp_C2_rt_sum_temp = (key_resp_C2_rt_sum_temp + Number.parseFloat(key_resp_C2.rt.toString()));
    if (key_resp_C2.corr) {
        key_resp_C2_corr_sum_temp = (key_resp_C2_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_C2.setText(msg);
    psychoJS.experiment.addData('feedback_C2.started', globalClock.getTime());
    feedback_C2MaxDuration = null
    // keep track of which components have finished
    feedback_C2Components = [];
    feedback_C2Components.push(feedback_text_C2);
    
    for (const thisComponent of feedback_C2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_C2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_C2' ---
    // get current time
    t = feedback_C2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_C2* updates
    if (t >= 0.0 && feedback_text_C2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_C2.tStart = t;  // (not accounting for frame time here)
      feedback_text_C2.frameNStart = frameN;  // exact frame index
      
      feedback_text_C2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_C2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_C2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_C2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_C2_corr_sum;
var key_resp_C2_rt_sum;
function feedback_C2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_C2' ---
    for (const thisComponent of feedback_C2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_C2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_C2
    key_resp_C2_corr_sum = key_resp_C2_corr_sum_temp;
    key_resp_C2_rt_sum = key_resp_C2_rt_sum_temp;
    
    if (feedback_C2MaxDurationReached) {
        feedback_C2Clock.add(feedback_C2MaxDuration);
    } else {
        feedback_C2Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_C2MaxDurationReached;
var _key_resp_7_allKeys;
var score_C2MaxDuration;
var score_C2Components;
function score_C2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_C2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_C2Clock.reset();
    routineTimer.reset();
    score_C2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_C2_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_C2_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_C2_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    psychoJS.experiment.addData('score_C2.started', globalClock.getTime());
    score_C2MaxDuration = null
    // keep track of which components have finished
    score_C2Components = [];
    score_C2Components.push(score_C2_text);
    score_C2Components.push(key_resp_7);
    
    for (const thisComponent of score_C2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_C2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_C2' ---
    // get current time
    t = score_C2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_C2_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_C2_text.setText(feedback_msg, false);
    }
    
    // *score_C2_text* updates
    if (t >= 0.0 && score_C2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_C2_text.tStart = t;  // (not accounting for frame time here)
      score_C2_text.frameNStart = frameN;  // exact frame index
      
      score_C2_text.setAutoDraw(true);
    }
    
    
    // *key_resp_7* updates
    if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }
    
    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        key_resp_7.duration = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_C2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_C2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_C2' ---
    for (const thisComponent of score_C2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_C2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_7.corr, level);
    }
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        psychoJS.experiment.addData('key_resp_7.duration', key_resp_7.duration);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // the Routine "score_C2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_C3MaxDurationReached;
var _key_resp_28_allKeys;
var reminder_C3MaxDuration;
var reminder_C3Components;
function reminder_C3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_C3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_C3Clock.reset();
    routineTimer.reset();
    reminder_C3MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_28.keys = undefined;
    key_resp_28.rt = undefined;
    _key_resp_28_allKeys = [];
    psychoJS.experiment.addData('reminder_C3.started', globalClock.getTime());
    reminder_C3MaxDuration = null
    // keep track of which components have finished
    reminder_C3Components = [];
    reminder_C3Components.push(text_48);
    reminder_C3Components.push(key_resp_28);
    
    for (const thisComponent of reminder_C3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_C3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_C3' ---
    // get current time
    t = reminder_C3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_48* updates
    if (t >= 0.0 && text_48.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_48.tStart = t;  // (not accounting for frame time here)
      text_48.frameNStart = frameN;  // exact frame index
      
      text_48.setAutoDraw(true);
    }
    
    
    // *key_resp_28* updates
    if (t >= 0.0 && key_resp_28.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_28.tStart = t;  // (not accounting for frame time here)
      key_resp_28.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_28.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_28.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_28.clearEvents(); });
    }
    
    if (key_resp_28.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_28.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_28_allKeys = _key_resp_28_allKeys.concat(theseKeys);
      if (_key_resp_28_allKeys.length > 0) {
        key_resp_28.keys = _key_resp_28_allKeys[_key_resp_28_allKeys.length - 1].name;  // just the last key pressed
        key_resp_28.rt = _key_resp_28_allKeys[_key_resp_28_allKeys.length - 1].rt;
        key_resp_28.duration = _key_resp_28_allKeys[_key_resp_28_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_C3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_C3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_C3' ---
    for (const thisComponent of reminder_C3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_C3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_28.corr, level);
    }
    psychoJS.experiment.addData('key_resp_28.keys', key_resp_28.keys);
    if (typeof key_resp_28.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_28.rt', key_resp_28.rt);
        psychoJS.experiment.addData('key_resp_28.duration', key_resp_28.duration);
        routineTimer.reset();
        }
    
    key_resp_28.stop();
    // the Routine "reminder_C3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_C3MaxDurationReached;
var _key_resp_C3_allKeys;
var record_Task_C3MaxDuration;
var record_Task_C3Components;
function record_Task_C3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_C3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_C3Clock.reset();
    routineTimer.reset();
    record_Task_C3MaxDurationReached = false;
    // update component parameters for each repeat
    text_C3.setText(words);
    key_resp_C3.keys = undefined;
    key_resp_C3.rt = undefined;
    _key_resp_C3_allKeys = [];
    psychoJS.experiment.addData('record_Task_C3.started', globalClock.getTime());
    record_Task_C3MaxDuration = null
    // keep track of which components have finished
    record_Task_C3Components = [];
    record_Task_C3Components.push(text_C3);
    record_Task_C3Components.push(key_resp_C3);
    
    for (const thisComponent of record_Task_C3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_C3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_C3' ---
    // get current time
    t = record_Task_C3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_C3* updates
    if (t >= 0.0 && text_C3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_C3.tStart = t;  // (not accounting for frame time here)
      text_C3.frameNStart = frameN;  // exact frame index
      
      text_C3.setAutoDraw(true);
    }
    
    
    // *key_resp_C3* updates
    if (t >= 0.0 && key_resp_C3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_C3.tStart = t;  // (not accounting for frame time here)
      key_resp_C3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_C3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_C3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_C3.clearEvents(); });
    }
    
    if (key_resp_C3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_C3.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_C3_allKeys = _key_resp_C3_allKeys.concat(theseKeys);
      if (_key_resp_C3_allKeys.length > 0) {
        key_resp_C3.keys = _key_resp_C3_allKeys[_key_resp_C3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_C3.rt = _key_resp_C3_allKeys[_key_resp_C3_allKeys.length - 1].rt;
        key_resp_C3.duration = _key_resp_C3_allKeys[_key_resp_C3_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_C3.keys == keypad) {
            key_resp_C3.corr = 1;
        } else {
            key_resp_C3.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_C3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_C3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_C3' ---
    for (const thisComponent of record_Task_C3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_C3.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_C3.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_C3.corr = 1;  // correct non-response
      } else {
         key_resp_C3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_C3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_C3.keys', key_resp_C3.keys);
    psychoJS.experiment.addData('key_resp_C3.corr', key_resp_C3.corr);
    if (typeof key_resp_C3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_C3.rt', key_resp_C3.rt);
        psychoJS.experiment.addData('key_resp_C3.duration', key_resp_C3.duration);
        routineTimer.reset();
        }
    
    key_resp_C3.stop();
    // the Routine "record_Task_C3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_C3MaxDurationReached;
var feedback_C3MaxDuration;
var feedback_C3Components;
function feedback_C3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_C3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_C3Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_C3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_C3
    key_resp_C3_rt_sum_temp = (key_resp_C3_rt_sum_temp + Number.parseFloat(key_resp_C3.rt.toString()));
    if (key_resp_C3.corr) {
        key_resp_C3_corr_sum_temp = (key_resp_C3_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_C3.setText(msg);
    psychoJS.experiment.addData('feedback_C3.started', globalClock.getTime());
    feedback_C3MaxDuration = null
    // keep track of which components have finished
    feedback_C3Components = [];
    feedback_C3Components.push(feedback_text_C3);
    
    for (const thisComponent of feedback_C3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_C3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_C3' ---
    // get current time
    t = feedback_C3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_C3* updates
    if (t >= 0.0 && feedback_text_C3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_C3.tStart = t;  // (not accounting for frame time here)
      feedback_text_C3.frameNStart = frameN;  // exact frame index
      
      feedback_text_C3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_C3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_C3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_C3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_C3_corr_sum;
var key_resp_C3_rt_sum;
function feedback_C3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_C3' ---
    for (const thisComponent of feedback_C3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_C3.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_C3
    key_resp_C3_corr_sum = key_resp_C3_corr_sum_temp;
    key_resp_C3_rt_sum = key_resp_C3_rt_sum_temp;
    
    if (feedback_C3MaxDurationReached) {
        feedback_C3Clock.add(feedback_C3MaxDuration);
    } else {
        feedback_C3Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_C3MaxDurationReached;
var _key_resp_8_allKeys;
var score_C3MaxDuration;
var score_C3Components;
function score_C3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_C3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_C3Clock.reset();
    routineTimer.reset();
    score_C3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_C3_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_C3_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_C3_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    psychoJS.experiment.addData('score_C3.started', globalClock.getTime());
    score_C3MaxDuration = null
    // keep track of which components have finished
    score_C3Components = [];
    score_C3Components.push(score_C3_text);
    score_C3Components.push(key_resp_8);
    
    for (const thisComponent of score_C3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_C3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_C3' ---
    // get current time
    t = score_C3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_C3_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_C3_text.setText(feedback_msg, false);
    }
    
    // *score_C3_text* updates
    if (t >= 0.0 && score_C3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_C3_text.tStart = t;  // (not accounting for frame time here)
      score_C3_text.frameNStart = frameN;  // exact frame index
      
      score_C3_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (score_C3_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      score_C3_text.setAutoDraw(false);
    }
    
    
    // *key_resp_8* updates
    if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }
    
    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        key_resp_8.duration = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_C3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_C3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_C3' ---
    for (const thisComponent of score_C3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_C3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_8.corr, level);
    }
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        psychoJS.experiment.addData('key_resp_8.duration', key_resp_8.duration);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "score_C3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_D1MaxDurationReached;
var _key_resp_29_allKeys;
var reminder_D1MaxDuration;
var reminder_D1Components;
function reminder_D1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_D1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_D1Clock.reset();
    routineTimer.reset();
    reminder_D1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_29.keys = undefined;
    key_resp_29.rt = undefined;
    _key_resp_29_allKeys = [];
    psychoJS.experiment.addData('reminder_D1.started', globalClock.getTime());
    reminder_D1MaxDuration = null
    // keep track of which components have finished
    reminder_D1Components = [];
    reminder_D1Components.push(text_49);
    reminder_D1Components.push(key_resp_29);
    
    for (const thisComponent of reminder_D1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_D1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_D1' ---
    // get current time
    t = reminder_D1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_49* updates
    if (t >= 0.0 && text_49.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_49.tStart = t;  // (not accounting for frame time here)
      text_49.frameNStart = frameN;  // exact frame index
      
      text_49.setAutoDraw(true);
    }
    
    
    // *key_resp_29* updates
    if (t >= 0.0 && key_resp_29.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_29.tStart = t;  // (not accounting for frame time here)
      key_resp_29.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_29.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_29.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_29.clearEvents(); });
    }
    
    if (key_resp_29.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_29.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_29_allKeys = _key_resp_29_allKeys.concat(theseKeys);
      if (_key_resp_29_allKeys.length > 0) {
        key_resp_29.keys = _key_resp_29_allKeys[_key_resp_29_allKeys.length - 1].name;  // just the last key pressed
        key_resp_29.rt = _key_resp_29_allKeys[_key_resp_29_allKeys.length - 1].rt;
        key_resp_29.duration = _key_resp_29_allKeys[_key_resp_29_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_D1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_D1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_D1' ---
    for (const thisComponent of reminder_D1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_D1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_29.corr, level);
    }
    psychoJS.experiment.addData('key_resp_29.keys', key_resp_29.keys);
    if (typeof key_resp_29.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_29.rt', key_resp_29.rt);
        psychoJS.experiment.addData('key_resp_29.duration', key_resp_29.duration);
        routineTimer.reset();
        }
    
    key_resp_29.stop();
    // the Routine "reminder_D1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_D1MaxDurationReached;
var _key_resp_D1_allKeys;
var record_Task_D1MaxDuration;
var record_Task_D1Components;
function record_Task_D1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_D1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_D1Clock.reset();
    routineTimer.reset();
    record_Task_D1MaxDurationReached = false;
    // update component parameters for each repeat
    text_D1.setText(name);
    key_resp_D1.keys = undefined;
    key_resp_D1.rt = undefined;
    _key_resp_D1_allKeys = [];
    psychoJS.experiment.addData('record_Task_D1.started', globalClock.getTime());
    record_Task_D1MaxDuration = null
    // keep track of which components have finished
    record_Task_D1Components = [];
    record_Task_D1Components.push(text_D1);
    record_Task_D1Components.push(key_resp_D1);
    
    for (const thisComponent of record_Task_D1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_D1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_D1' ---
    // get current time
    t = record_Task_D1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_D1* updates
    if (t >= 0.0 && text_D1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_D1.tStart = t;  // (not accounting for frame time here)
      text_D1.frameNStart = frameN;  // exact frame index
      
      text_D1.setAutoDraw(true);
    }
    
    
    // *key_resp_D1* updates
    if (t >= 0.0 && key_resp_D1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_D1.tStart = t;  // (not accounting for frame time here)
      key_resp_D1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_D1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_D1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_D1.clearEvents(); });
    }
    
    if (key_resp_D1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_D1.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_D1_allKeys = _key_resp_D1_allKeys.concat(theseKeys);
      if (_key_resp_D1_allKeys.length > 0) {
        key_resp_D1.keys = _key_resp_D1_allKeys[_key_resp_D1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_D1.rt = _key_resp_D1_allKeys[_key_resp_D1_allKeys.length - 1].rt;
        key_resp_D1.duration = _key_resp_D1_allKeys[_key_resp_D1_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_D1.keys == keypad) {
            key_resp_D1.corr = 1;
        } else {
            key_resp_D1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_D1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_D1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_D1' ---
    for (const thisComponent of record_Task_D1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_D1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_D1.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_D1.corr = 1;  // correct non-response
      } else {
         key_resp_D1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_D1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_D1.keys', key_resp_D1.keys);
    psychoJS.experiment.addData('key_resp_D1.corr', key_resp_D1.corr);
    if (typeof key_resp_D1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_D1.rt', key_resp_D1.rt);
        psychoJS.experiment.addData('key_resp_D1.duration', key_resp_D1.duration);
        routineTimer.reset();
        }
    
    key_resp_D1.stop();
    // the Routine "record_Task_D1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_D1MaxDurationReached;
var feedback_D1MaxDuration;
var feedback_D1Components;
function feedback_D1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_D1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_D1Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_D1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_D1
    key_resp_D1_rt_sum_temp = (key_resp_D1_rt_sum_temp + Number.parseFloat(key_resp_D1.rt.toString()));
    if (key_resp_D1.corr) {
        key_resp_D1_corr_sum_temp = (key_resp_D1_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_D1.setText(msg);
    psychoJS.experiment.addData('feedback_D1.started', globalClock.getTime());
    feedback_D1MaxDuration = null
    // keep track of which components have finished
    feedback_D1Components = [];
    feedback_D1Components.push(feedback_text_D1);
    
    for (const thisComponent of feedback_D1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_D1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_D1' ---
    // get current time
    t = feedback_D1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_D1* updates
    if (t >= 0.0 && feedback_text_D1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_D1.tStart = t;  // (not accounting for frame time here)
      feedback_text_D1.frameNStart = frameN;  // exact frame index
      
      feedback_text_D1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_D1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_D1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_D1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_D1_corr_sum;
var key_resp_D1_rt_sum;
function feedback_D1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_D1' ---
    for (const thisComponent of feedback_D1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_D1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_D1
    key_resp_D1_corr_sum = key_resp_D1_corr_sum_temp;
    key_resp_D1_rt_sum = key_resp_D1_rt_sum_temp;
    
    if (feedback_D1MaxDurationReached) {
        feedback_D1Clock.add(feedback_D1MaxDuration);
    } else {
        feedback_D1Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_D1MaxDurationReached;
var _key_resp_9_allKeys;
var score_D1MaxDuration;
var score_D1Components;
function score_D1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_D1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_D1Clock.reset();
    routineTimer.reset();
    score_D1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_D1_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_D1_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_D1_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    psychoJS.experiment.addData('score_D1.started', globalClock.getTime());
    score_D1MaxDuration = null
    // keep track of which components have finished
    score_D1Components = [];
    score_D1Components.push(score_D1_text);
    score_D1Components.push(key_resp_9);
    
    for (const thisComponent of score_D1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_D1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_D1' ---
    // get current time
    t = score_D1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_D1_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_D1_text.setText(feedback_msg, false);
    }
    
    // *score_D1_text* updates
    if (t >= 0.0 && score_D1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_D1_text.tStart = t;  // (not accounting for frame time here)
      score_D1_text.frameNStart = frameN;  // exact frame index
      
      score_D1_text.setAutoDraw(true);
    }
    
    
    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }
    
    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        key_resp_9.duration = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_D1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_D1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_D1' ---
    for (const thisComponent of score_D1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_D1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_9.corr, level);
    }
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        psychoJS.experiment.addData('key_resp_9.duration', key_resp_9.duration);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "score_D1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_E1MaxDurationReached;
var _key_resp_30_allKeys;
var reminder_E1MaxDuration;
var reminder_E1Components;
function reminder_E1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_E1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_E1Clock.reset();
    routineTimer.reset();
    reminder_E1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_30.keys = undefined;
    key_resp_30.rt = undefined;
    _key_resp_30_allKeys = [];
    psychoJS.experiment.addData('reminder_E1.started', globalClock.getTime());
    reminder_E1MaxDuration = null
    // keep track of which components have finished
    reminder_E1Components = [];
    reminder_E1Components.push(text_50);
    reminder_E1Components.push(key_resp_30);
    
    for (const thisComponent of reminder_E1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_E1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_E1' ---
    // get current time
    t = reminder_E1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_50* updates
    if (t >= 0.0 && text_50.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_50.tStart = t;  // (not accounting for frame time here)
      text_50.frameNStart = frameN;  // exact frame index
      
      text_50.setAutoDraw(true);
    }
    
    
    // *key_resp_30* updates
    if (t >= 0.0 && key_resp_30.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_30.tStart = t;  // (not accounting for frame time here)
      key_resp_30.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_30.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_30.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_30.clearEvents(); });
    }
    
    if (key_resp_30.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_30.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_30_allKeys = _key_resp_30_allKeys.concat(theseKeys);
      if (_key_resp_30_allKeys.length > 0) {
        key_resp_30.keys = _key_resp_30_allKeys[_key_resp_30_allKeys.length - 1].name;  // just the last key pressed
        key_resp_30.rt = _key_resp_30_allKeys[_key_resp_30_allKeys.length - 1].rt;
        key_resp_30.duration = _key_resp_30_allKeys[_key_resp_30_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_E1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_E1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_E1' ---
    for (const thisComponent of reminder_E1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_E1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_30.corr, level);
    }
    psychoJS.experiment.addData('key_resp_30.keys', key_resp_30.keys);
    if (typeof key_resp_30.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_30.rt', key_resp_30.rt);
        psychoJS.experiment.addData('key_resp_30.duration', key_resp_30.duration);
        routineTimer.reset();
        }
    
    key_resp_30.stop();
    // the Routine "reminder_E1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_Task_E1MaxDurationReached;
var _key_resp_E1_allKeys;
var practice_Task_E1MaxDuration;
var practice_Task_E1Components;
function practice_Task_E1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_Task_E1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_Task_E1Clock.reset();
    routineTimer.reset();
    practice_Task_E1MaxDurationReached = false;
    // update component parameters for each repeat
    text_E1.setText(words);
    key_resp_E1.keys = undefined;
    key_resp_E1.rt = undefined;
    _key_resp_E1_allKeys = [];
    psychoJS.experiment.addData('practice_Task_E1.started', globalClock.getTime());
    practice_Task_E1MaxDuration = null
    // keep track of which components have finished
    practice_Task_E1Components = [];
    practice_Task_E1Components.push(text_E1);
    practice_Task_E1Components.push(key_resp_E1);
    
    for (const thisComponent of practice_Task_E1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_Task_E1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_Task_E1' ---
    // get current time
    t = practice_Task_E1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_E1* updates
    if (t >= 0.0 && text_E1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_E1.tStart = t;  // (not accounting for frame time here)
      text_E1.frameNStart = frameN;  // exact frame index
      
      text_E1.setAutoDraw(true);
    }
    
    
    // *key_resp_E1* updates
    if (t >= 0.0 && key_resp_E1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_E1.tStart = t;  // (not accounting for frame time here)
      key_resp_E1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_E1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_E1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_E1.clearEvents(); });
    }
    
    if (key_resp_E1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_E1.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_E1_allKeys = _key_resp_E1_allKeys.concat(theseKeys);
      if (_key_resp_E1_allKeys.length > 0) {
        key_resp_E1.keys = _key_resp_E1_allKeys[_key_resp_E1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_E1.rt = _key_resp_E1_allKeys[_key_resp_E1_allKeys.length - 1].rt;
        key_resp_E1.duration = _key_resp_E1_allKeys[_key_resp_E1_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_E1.keys == keypad) {
            key_resp_E1.corr = 1;
        } else {
            key_resp_E1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_Task_E1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_Task_E1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_Task_E1' ---
    for (const thisComponent of practice_Task_E1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_Task_E1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_E1.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_E1.corr = 1;  // correct non-response
      } else {
         key_resp_E1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_E1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_E1.keys', key_resp_E1.keys);
    psychoJS.experiment.addData('key_resp_E1.corr', key_resp_E1.corr);
    if (typeof key_resp_E1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_E1.rt', key_resp_E1.rt);
        psychoJS.experiment.addData('key_resp_E1.duration', key_resp_E1.duration);
        routineTimer.reset();
        }
    
    key_resp_E1.stop();
    // the Routine "practice_Task_E1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_E1MaxDurationReached;
var feedback_E1MaxDuration;
var feedback_E1Components;
function feedback_E1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_E1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_E1Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_E1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_E1
    key_resp_E1_rt_sum_temp = (key_resp_E1_rt_sum_temp + Number.parseFloat(key_resp_E1.rt.toString()));
    if (key_resp_E1.corr) {
        key_resp_E1_corr_sum_temp = (key_resp_E1_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_E1.setText(msg);
    psychoJS.experiment.addData('feedback_E1.started', globalClock.getTime());
    feedback_E1MaxDuration = null
    // keep track of which components have finished
    feedback_E1Components = [];
    feedback_E1Components.push(feedback_text_E1);
    
    for (const thisComponent of feedback_E1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_E1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_E1' ---
    // get current time
    t = feedback_E1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_E1* updates
    if (t >= 0.0 && feedback_text_E1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_E1.tStart = t;  // (not accounting for frame time here)
      feedback_text_E1.frameNStart = frameN;  // exact frame index
      
      feedback_text_E1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_E1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_E1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_E1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_E1_corr_sum;
var key_resp_E1_rt_sum;
function feedback_E1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_E1' ---
    for (const thisComponent of feedback_E1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_E1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_E1
    key_resp_E1_corr_sum = key_resp_E1_corr_sum_temp;
    key_resp_E1_rt_sum = key_resp_E1_rt_sum_temp;
    
    if (feedback_E1MaxDurationReached) {
        feedback_E1Clock.add(feedback_E1MaxDuration);
    } else {
        feedback_E1Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_E1MaxDurationReached;
var _key_resp_10_allKeys;
var score_E1MaxDuration;
var score_E1Components;
function score_E1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_E1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_E1Clock.reset();
    routineTimer.reset();
    score_E1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_E1_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_E1_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_E1_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    psychoJS.experiment.addData('score_E1.started', globalClock.getTime());
    score_E1MaxDuration = null
    // keep track of which components have finished
    score_E1Components = [];
    score_E1Components.push(score_E1_text);
    score_E1Components.push(key_resp_10);
    
    for (const thisComponent of score_E1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_E1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_E1' ---
    // get current time
    t = score_E1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_E1_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_E1_text.setText(feedback_msg, false);
    }
    
    // *score_E1_text* updates
    if (t >= 0.0 && score_E1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_E1_text.tStart = t;  // (not accounting for frame time here)
      score_E1_text.frameNStart = frameN;  // exact frame index
      
      score_E1_text.setAutoDraw(true);
    }
    
    
    // *key_resp_10* updates
    if (t >= 0.0 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }
    
    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
        key_resp_10.duration = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_E1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_E1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_E1' ---
    for (const thisComponent of score_E1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_E1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_10.corr, level);
    }
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        psychoJS.experiment.addData('key_resp_10.duration', key_resp_10.duration);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "score_E1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_E2MaxDurationReached;
var _key_resp_31_allKeys;
var reminder_E2MaxDuration;
var reminder_E2Components;
function reminder_E2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_E2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_E2Clock.reset();
    routineTimer.reset();
    reminder_E2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_31.keys = undefined;
    key_resp_31.rt = undefined;
    _key_resp_31_allKeys = [];
    psychoJS.experiment.addData('reminder_E2.started', globalClock.getTime());
    reminder_E2MaxDuration = null
    // keep track of which components have finished
    reminder_E2Components = [];
    reminder_E2Components.push(text_51);
    reminder_E2Components.push(key_resp_31);
    
    for (const thisComponent of reminder_E2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_E2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_E2' ---
    // get current time
    t = reminder_E2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_51* updates
    if (t >= 0.0 && text_51.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_51.tStart = t;  // (not accounting for frame time here)
      text_51.frameNStart = frameN;  // exact frame index
      
      text_51.setAutoDraw(true);
    }
    
    
    // *key_resp_31* updates
    if (t >= 0.0 && key_resp_31.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_31.tStart = t;  // (not accounting for frame time here)
      key_resp_31.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_31.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_31.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_31.clearEvents(); });
    }
    
    if (key_resp_31.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_31.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_31_allKeys = _key_resp_31_allKeys.concat(theseKeys);
      if (_key_resp_31_allKeys.length > 0) {
        key_resp_31.keys = _key_resp_31_allKeys[_key_resp_31_allKeys.length - 1].name;  // just the last key pressed
        key_resp_31.rt = _key_resp_31_allKeys[_key_resp_31_allKeys.length - 1].rt;
        key_resp_31.duration = _key_resp_31_allKeys[_key_resp_31_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_E2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_E2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_E2' ---
    for (const thisComponent of reminder_E2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_E2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_31.corr, level);
    }
    psychoJS.experiment.addData('key_resp_31.keys', key_resp_31.keys);
    if (typeof key_resp_31.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_31.rt', key_resp_31.rt);
        psychoJS.experiment.addData('key_resp_31.duration', key_resp_31.duration);
        routineTimer.reset();
        }
    
    key_resp_31.stop();
    // the Routine "reminder_E2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_E2MaxDurationReached;
var _key_resp_E2_allKeys;
var record_Task_E2MaxDuration;
var record_Task_E2Components;
function record_Task_E2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_E2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_E2Clock.reset();
    routineTimer.reset();
    record_Task_E2MaxDurationReached = false;
    // update component parameters for each repeat
    text_E2.setText(words);
    key_resp_E2.keys = undefined;
    key_resp_E2.rt = undefined;
    _key_resp_E2_allKeys = [];
    psychoJS.experiment.addData('record_Task_E2.started', globalClock.getTime());
    record_Task_E2MaxDuration = null
    // keep track of which components have finished
    record_Task_E2Components = [];
    record_Task_E2Components.push(text_E2);
    record_Task_E2Components.push(key_resp_E2);
    
    for (const thisComponent of record_Task_E2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_E2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_E2' ---
    // get current time
    t = record_Task_E2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_E2* updates
    if (t >= 0.0 && text_E2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_E2.tStart = t;  // (not accounting for frame time here)
      text_E2.frameNStart = frameN;  // exact frame index
      
      text_E2.setAutoDraw(true);
    }
    
    
    // *key_resp_E2* updates
    if (t >= 0.0 && key_resp_E2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_E2.tStart = t;  // (not accounting for frame time here)
      key_resp_E2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_E2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_E2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_E2.clearEvents(); });
    }
    
    if (key_resp_E2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_E2.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_E2_allKeys = _key_resp_E2_allKeys.concat(theseKeys);
      if (_key_resp_E2_allKeys.length > 0) {
        key_resp_E2.keys = _key_resp_E2_allKeys[_key_resp_E2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_E2.rt = _key_resp_E2_allKeys[_key_resp_E2_allKeys.length - 1].rt;
        key_resp_E2.duration = _key_resp_E2_allKeys[_key_resp_E2_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_E2.keys == keypad) {
            key_resp_E2.corr = 1;
        } else {
            key_resp_E2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_E2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_E2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_E2' ---
    for (const thisComponent of record_Task_E2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_E2.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_E2.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_E2.corr = 1;  // correct non-response
      } else {
         key_resp_E2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_E2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_E2.keys', key_resp_E2.keys);
    psychoJS.experiment.addData('key_resp_E2.corr', key_resp_E2.corr);
    if (typeof key_resp_E2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_E2.rt', key_resp_E2.rt);
        psychoJS.experiment.addData('key_resp_E2.duration', key_resp_E2.duration);
        routineTimer.reset();
        }
    
    key_resp_E2.stop();
    // the Routine "record_Task_E2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_E2MaxDurationReached;
var feedback_E2MaxDuration;
var feedback_E2Components;
function feedback_E2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_E2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_E2Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_E2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_E2
    key_resp_E2_rt_sum_temp = (key_resp_E2_rt_sum_temp + Number.parseFloat(key_resp_E2.rt.toString()));
    if (key_resp_E2.corr) {
        key_resp_E2_corr_sum_temp = (key_resp_E2_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_E2.setText(msg);
    psychoJS.experiment.addData('feedback_E2.started', globalClock.getTime());
    feedback_E2MaxDuration = null
    // keep track of which components have finished
    feedback_E2Components = [];
    feedback_E2Components.push(feedback_text_E2);
    
    for (const thisComponent of feedback_E2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_E2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_E2' ---
    // get current time
    t = feedback_E2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_E2* updates
    if (t >= 0.0 && feedback_text_E2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_E2.tStart = t;  // (not accounting for frame time here)
      feedback_text_E2.frameNStart = frameN;  // exact frame index
      
      feedback_text_E2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_E2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_E2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_E2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_E2_corr_sum;
var key_resp_E2_rt_sum;
function feedback_E2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_E2' ---
    for (const thisComponent of feedback_E2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_E2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_E2
    key_resp_E2_corr_sum = key_resp_E2_corr_sum_temp;
    key_resp_E2_rt_sum = key_resp_E2_rt_sum_temp;
    
    if (feedback_E2MaxDurationReached) {
        feedback_E2Clock.add(feedback_E2MaxDuration);
    } else {
        feedback_E2Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_E2MaxDurationReached;
var _key_resp_11_allKeys;
var score_E2MaxDuration;
var score_E2Components;
function score_E2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_E2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_E2Clock.reset();
    routineTimer.reset();
    score_E2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_E2_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_E2_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_E2_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    psychoJS.experiment.addData('score_E2.started', globalClock.getTime());
    score_E2MaxDuration = null
    // keep track of which components have finished
    score_E2Components = [];
    score_E2Components.push(score_E2_text);
    score_E2Components.push(key_resp_11);
    
    for (const thisComponent of score_E2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_E2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_E2' ---
    // get current time
    t = score_E2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_E2_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_E2_text.setText(feedback_msg, false);
    }
    
    // *score_E2_text* updates
    if (t >= 0.0 && score_E2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_E2_text.tStart = t;  // (not accounting for frame time here)
      score_E2_text.frameNStart = frameN;  // exact frame index
      
      score_E2_text.setAutoDraw(true);
    }
    
    
    // *key_resp_11* updates
    if (t >= 0.0 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }
    
    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        key_resp_11.duration = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_E2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_E2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_E2' ---
    for (const thisComponent of score_E2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_E2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_11.corr, level);
    }
    psychoJS.experiment.addData('key_resp_11.keys', key_resp_11.keys);
    if (typeof key_resp_11.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_11.rt', key_resp_11.rt);
        psychoJS.experiment.addData('key_resp_11.duration', key_resp_11.duration);
        routineTimer.reset();
        }
    
    key_resp_11.stop();
    // the Routine "score_E2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_E3MaxDurationReached;
var _key_resp_40_allKeys;
var reminder_E3MaxDuration;
var reminder_E3Components;
function reminder_E3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_E3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_E3Clock.reset();
    routineTimer.reset();
    reminder_E3MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_40.keys = undefined;
    key_resp_40.rt = undefined;
    _key_resp_40_allKeys = [];
    psychoJS.experiment.addData('reminder_E3.started', globalClock.getTime());
    reminder_E3MaxDuration = null
    // keep track of which components have finished
    reminder_E3Components = [];
    reminder_E3Components.push(text_52);
    reminder_E3Components.push(key_resp_40);
    
    for (const thisComponent of reminder_E3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_E3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_E3' ---
    // get current time
    t = reminder_E3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_52* updates
    if (t >= 0.0 && text_52.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_52.tStart = t;  // (not accounting for frame time here)
      text_52.frameNStart = frameN;  // exact frame index
      
      text_52.setAutoDraw(true);
    }
    
    
    // *key_resp_40* updates
    if (t >= 0.0 && key_resp_40.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_40.tStart = t;  // (not accounting for frame time here)
      key_resp_40.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_40.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_40.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_40.clearEvents(); });
    }
    
    if (key_resp_40.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_40.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_40_allKeys = _key_resp_40_allKeys.concat(theseKeys);
      if (_key_resp_40_allKeys.length > 0) {
        key_resp_40.keys = _key_resp_40_allKeys[_key_resp_40_allKeys.length - 1].name;  // just the last key pressed
        key_resp_40.rt = _key_resp_40_allKeys[_key_resp_40_allKeys.length - 1].rt;
        key_resp_40.duration = _key_resp_40_allKeys[_key_resp_40_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_E3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_E3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_E3' ---
    for (const thisComponent of reminder_E3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_E3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_40.corr, level);
    }
    psychoJS.experiment.addData('key_resp_40.keys', key_resp_40.keys);
    if (typeof key_resp_40.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_40.rt', key_resp_40.rt);
        psychoJS.experiment.addData('key_resp_40.duration', key_resp_40.duration);
        routineTimer.reset();
        }
    
    key_resp_40.stop();
    // the Routine "reminder_E3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_E3MaxDurationReached;
var _key_resp_E3_allKeys;
var record_Task_E3MaxDuration;
var record_Task_E3Components;
function record_Task_E3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_E3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_E3Clock.reset();
    routineTimer.reset();
    record_Task_E3MaxDurationReached = false;
    // update component parameters for each repeat
    text_E3.setText(words);
    key_resp_E3.keys = undefined;
    key_resp_E3.rt = undefined;
    _key_resp_E3_allKeys = [];
    psychoJS.experiment.addData('record_Task_E3.started', globalClock.getTime());
    record_Task_E3MaxDuration = null
    // keep track of which components have finished
    record_Task_E3Components = [];
    record_Task_E3Components.push(text_E3);
    record_Task_E3Components.push(key_resp_E3);
    
    for (const thisComponent of record_Task_E3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_E3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_E3' ---
    // get current time
    t = record_Task_E3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_E3* updates
    if (t >= 0.0 && text_E3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_E3.tStart = t;  // (not accounting for frame time here)
      text_E3.frameNStart = frameN;  // exact frame index
      
      text_E3.setAutoDraw(true);
    }
    
    
    // *key_resp_E3* updates
    if (t >= 0.0 && key_resp_E3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_E3.tStart = t;  // (not accounting for frame time here)
      key_resp_E3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_E3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_E3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_E3.clearEvents(); });
    }
    
    if (key_resp_E3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_E3.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_E3_allKeys = _key_resp_E3_allKeys.concat(theseKeys);
      if (_key_resp_E3_allKeys.length > 0) {
        key_resp_E3.keys = _key_resp_E3_allKeys[_key_resp_E3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_E3.rt = _key_resp_E3_allKeys[_key_resp_E3_allKeys.length - 1].rt;
        key_resp_E3.duration = _key_resp_E3_allKeys[_key_resp_E3_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_E3.keys == keypad) {
            key_resp_E3.corr = 1;
        } else {
            key_resp_E3.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_E3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_E3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_E3' ---
    for (const thisComponent of record_Task_E3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_E3.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_E3.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_E3.corr = 1;  // correct non-response
      } else {
         key_resp_E3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_E3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_E3.keys', key_resp_E3.keys);
    psychoJS.experiment.addData('key_resp_E3.corr', key_resp_E3.corr);
    if (typeof key_resp_E3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_E3.rt', key_resp_E3.rt);
        psychoJS.experiment.addData('key_resp_E3.duration', key_resp_E3.duration);
        routineTimer.reset();
        }
    
    key_resp_E3.stop();
    // the Routine "record_Task_E3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_E3MaxDurationReached;
var feedback_E3MaxDuration;
var feedback_E3Components;
function feedback_E3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_E3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_E3Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_E3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_E3
    key_resp_E3_rt_sum_temp = (key_resp_E3_rt_sum_temp + Number.parseFloat(key_resp_E3.rt.toString()));
    if (key_resp_E3.corr) {
        key_resp_E3_corr_sum_temp = (key_resp_E3_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_E3.setText(msg);
    psychoJS.experiment.addData('feedback_E3.started', globalClock.getTime());
    feedback_E3MaxDuration = null
    // keep track of which components have finished
    feedback_E3Components = [];
    feedback_E3Components.push(feedback_text_E3);
    
    for (const thisComponent of feedback_E3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_E3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_E3' ---
    // get current time
    t = feedback_E3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_E3* updates
    if (t >= 0.0 && feedback_text_E3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_E3.tStart = t;  // (not accounting for frame time here)
      feedback_text_E3.frameNStart = frameN;  // exact frame index
      
      feedback_text_E3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_E3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_E3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_E3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_E3_corr_sum;
var key_resp_E3_rt_sum;
function feedback_E3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_E3' ---
    for (const thisComponent of feedback_E3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_E3.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_E3
    key_resp_E3_corr_sum = key_resp_E3_corr_sum_temp;
    key_resp_E3_rt_sum = key_resp_E3_rt_sum_temp;
    
    if (feedback_E3MaxDurationReached) {
        feedback_E3Clock.add(feedback_E3MaxDuration);
    } else {
        feedback_E3Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_E3MaxDurationReached;
var _key_resp_12_allKeys;
var score_E3MaxDuration;
var score_E3Components;
function score_E3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_E3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_E3Clock.reset();
    routineTimer.reset();
    score_E3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_E3_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_E3_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_E3_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    psychoJS.experiment.addData('score_E3.started', globalClock.getTime());
    score_E3MaxDuration = null
    // keep track of which components have finished
    score_E3Components = [];
    score_E3Components.push(score_E3_text);
    score_E3Components.push(key_resp_12);
    
    for (const thisComponent of score_E3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_E3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_E3' ---
    // get current time
    t = score_E3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_E3_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_E3_text.setText(feedback_msg, false);
    }
    
    // *score_E3_text* updates
    if (t >= 0.0 && score_E3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_E3_text.tStart = t;  // (not accounting for frame time here)
      score_E3_text.frameNStart = frameN;  // exact frame index
      
      score_E3_text.setAutoDraw(true);
    }
    
    
    // *key_resp_12* updates
    if (t >= 0.0 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_12.tStart = t;  // (not accounting for frame time here)
      key_resp_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.clearEvents(); });
    }
    
    if (key_resp_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_12.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_12_allKeys = _key_resp_12_allKeys.concat(theseKeys);
      if (_key_resp_12_allKeys.length > 0) {
        key_resp_12.keys = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].name;  // just the last key pressed
        key_resp_12.rt = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].rt;
        key_resp_12.duration = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_E3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_E3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_E3' ---
    for (const thisComponent of score_E3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_E3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_12.corr, level);
    }
    psychoJS.experiment.addData('key_resp_12.keys', key_resp_12.keys);
    if (typeof key_resp_12.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_12.rt', key_resp_12.rt);
        psychoJS.experiment.addData('key_resp_12.duration', key_resp_12.duration);
        routineTimer.reset();
        }
    
    key_resp_12.stop();
    // the Routine "score_E3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_F1MaxDurationReached;
var _key_resp_32_allKeys;
var reminder_F1MaxDuration;
var reminder_F1Components;
function reminder_F1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_F1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_F1Clock.reset();
    routineTimer.reset();
    reminder_F1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_32.keys = undefined;
    key_resp_32.rt = undefined;
    _key_resp_32_allKeys = [];
    psychoJS.experiment.addData('reminder_F1.started', globalClock.getTime());
    reminder_F1MaxDuration = null
    // keep track of which components have finished
    reminder_F1Components = [];
    reminder_F1Components.push(text_53);
    reminder_F1Components.push(key_resp_32);
    
    for (const thisComponent of reminder_F1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_F1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_F1' ---
    // get current time
    t = reminder_F1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_53* updates
    if (t >= 0.0 && text_53.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_53.tStart = t;  // (not accounting for frame time here)
      text_53.frameNStart = frameN;  // exact frame index
      
      text_53.setAutoDraw(true);
    }
    
    
    // *key_resp_32* updates
    if (t >= 0.0 && key_resp_32.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_32.tStart = t;  // (not accounting for frame time here)
      key_resp_32.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_32.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_32.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_32.clearEvents(); });
    }
    
    if (key_resp_32.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_32.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_32_allKeys = _key_resp_32_allKeys.concat(theseKeys);
      if (_key_resp_32_allKeys.length > 0) {
        key_resp_32.keys = _key_resp_32_allKeys[_key_resp_32_allKeys.length - 1].name;  // just the last key pressed
        key_resp_32.rt = _key_resp_32_allKeys[_key_resp_32_allKeys.length - 1].rt;
        key_resp_32.duration = _key_resp_32_allKeys[_key_resp_32_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_F1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_F1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_F1' ---
    for (const thisComponent of reminder_F1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_F1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_32.corr, level);
    }
    psychoJS.experiment.addData('key_resp_32.keys', key_resp_32.keys);
    if (typeof key_resp_32.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_32.rt', key_resp_32.rt);
        psychoJS.experiment.addData('key_resp_32.duration', key_resp_32.duration);
        routineTimer.reset();
        }
    
    key_resp_32.stop();
    // the Routine "reminder_F1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_F1MaxDurationReached;
var _key_resp_F1_allKeys;
var record_Task_F1MaxDuration;
var record_Task_F1Components;
function record_Task_F1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_F1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_F1Clock.reset();
    routineTimer.reset();
    record_Task_F1MaxDurationReached = false;
    // update component parameters for each repeat
    text_F1.setText(name);
    key_resp_F1.keys = undefined;
    key_resp_F1.rt = undefined;
    _key_resp_F1_allKeys = [];
    psychoJS.experiment.addData('record_Task_F1.started', globalClock.getTime());
    record_Task_F1MaxDuration = null
    // keep track of which components have finished
    record_Task_F1Components = [];
    record_Task_F1Components.push(text_F1);
    record_Task_F1Components.push(key_resp_F1);
    
    for (const thisComponent of record_Task_F1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_F1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_F1' ---
    // get current time
    t = record_Task_F1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_F1* updates
    if (t >= 0.0 && text_F1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_F1.tStart = t;  // (not accounting for frame time here)
      text_F1.frameNStart = frameN;  // exact frame index
      
      text_F1.setAutoDraw(true);
    }
    
    
    // *key_resp_F1* updates
    if (t >= 0.0 && key_resp_F1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_F1.tStart = t;  // (not accounting for frame time here)
      key_resp_F1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_F1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_F1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_F1.clearEvents(); });
    }
    
    if (key_resp_F1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_F1.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_F1_allKeys = _key_resp_F1_allKeys.concat(theseKeys);
      if (_key_resp_F1_allKeys.length > 0) {
        key_resp_F1.keys = _key_resp_F1_allKeys[_key_resp_F1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_F1.rt = _key_resp_F1_allKeys[_key_resp_F1_allKeys.length - 1].rt;
        key_resp_F1.duration = _key_resp_F1_allKeys[_key_resp_F1_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_F1.keys == keypad) {
            key_resp_F1.corr = 1;
        } else {
            key_resp_F1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_F1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_F1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_F1' ---
    for (const thisComponent of record_Task_F1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_F1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_F1.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_F1.corr = 1;  // correct non-response
      } else {
         key_resp_F1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_F1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_F1.keys', key_resp_F1.keys);
    psychoJS.experiment.addData('key_resp_F1.corr', key_resp_F1.corr);
    if (typeof key_resp_F1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_F1.rt', key_resp_F1.rt);
        psychoJS.experiment.addData('key_resp_F1.duration', key_resp_F1.duration);
        routineTimer.reset();
        }
    
    key_resp_F1.stop();
    // the Routine "record_Task_F1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_F1MaxDurationReached;
var feedback_F1MaxDuration;
var feedback_F1Components;
function feedback_F1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_F1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_F1Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_F1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_F1
    key_resp_F1_rt_sum_temp = (key_resp_F1_rt_sum_temp + Number.parseFloat(key_resp_F1.rt.toString()));
    if (key_resp_F1.corr) {
        key_resp_F1_corr_sum_temp = (key_resp_F1_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_F1.setText(msg);
    psychoJS.experiment.addData('feedback_F1.started', globalClock.getTime());
    feedback_F1MaxDuration = null
    // keep track of which components have finished
    feedback_F1Components = [];
    feedback_F1Components.push(feedback_text_F1);
    
    for (const thisComponent of feedback_F1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_F1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_F1' ---
    // get current time
    t = feedback_F1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_F1* updates
    if (t >= 0.0 && feedback_text_F1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_F1.tStart = t;  // (not accounting for frame time here)
      feedback_text_F1.frameNStart = frameN;  // exact frame index
      
      feedback_text_F1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_F1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_F1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_F1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_F1_corr_sum;
var key_resp_F1_rt_sum;
function feedback_F1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_F1' ---
    for (const thisComponent of feedback_F1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_F1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_F1
    key_resp_F1_corr_sum = key_resp_F1_corr_sum_temp;
    key_resp_F1_rt_sum = key_resp_F1_rt_sum_temp;
    
    if (feedback_F1MaxDurationReached) {
        feedback_F1Clock.add(feedback_F1MaxDuration);
    } else {
        feedback_F1Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_F1MaxDurationReached;
var _key_resp_13_allKeys;
var score_F1MaxDuration;
var score_F1Components;
function score_F1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_F1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_F1Clock.reset();
    routineTimer.reset();
    score_F1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_F1_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_F1_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_F1_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_13.keys = undefined;
    key_resp_13.rt = undefined;
    _key_resp_13_allKeys = [];
    psychoJS.experiment.addData('score_F1.started', globalClock.getTime());
    score_F1MaxDuration = null
    // keep track of which components have finished
    score_F1Components = [];
    score_F1Components.push(score_F1_text);
    score_F1Components.push(key_resp_13);
    
    for (const thisComponent of score_F1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_F1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_F1' ---
    // get current time
    t = score_F1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_F1_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_F1_text.setText(feedback_msg, false);
    }
    
    // *score_F1_text* updates
    if (t >= 0.0 && score_F1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_F1_text.tStart = t;  // (not accounting for frame time here)
      score_F1_text.frameNStart = frameN;  // exact frame index
      
      score_F1_text.setAutoDraw(true);
    }
    
    
    // *key_resp_13* updates
    if (t >= 0.0 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_13.tStart = t;  // (not accounting for frame time here)
      key_resp_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
    }
    
    if (key_resp_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_13.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_13_allKeys = _key_resp_13_allKeys.concat(theseKeys);
      if (_key_resp_13_allKeys.length > 0) {
        key_resp_13.keys = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].name;  // just the last key pressed
        key_resp_13.rt = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].rt;
        key_resp_13.duration = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_F1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_F1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_F1' ---
    for (const thisComponent of score_F1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_F1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_13.corr, level);
    }
    psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
    if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
        psychoJS.experiment.addData('key_resp_13.duration', key_resp_13.duration);
        routineTimer.reset();
        }
    
    key_resp_13.stop();
    // the Routine "score_F1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_G1MaxDurationReached;
var _key_resp_33_allKeys;
var reminder_G1MaxDuration;
var reminder_G1Components;
function reminder_G1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_G1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_G1Clock.reset();
    routineTimer.reset();
    reminder_G1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_33.keys = undefined;
    key_resp_33.rt = undefined;
    _key_resp_33_allKeys = [];
    psychoJS.experiment.addData('reminder_G1.started', globalClock.getTime());
    reminder_G1MaxDuration = null
    // keep track of which components have finished
    reminder_G1Components = [];
    reminder_G1Components.push(text_54);
    reminder_G1Components.push(key_resp_33);
    
    for (const thisComponent of reminder_G1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_G1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_G1' ---
    // get current time
    t = reminder_G1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_54* updates
    if (t >= 0.0 && text_54.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_54.tStart = t;  // (not accounting for frame time here)
      text_54.frameNStart = frameN;  // exact frame index
      
      text_54.setAutoDraw(true);
    }
    
    
    // *key_resp_33* updates
    if (t >= 0.0 && key_resp_33.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_33.tStart = t;  // (not accounting for frame time here)
      key_resp_33.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_33.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_33.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_33.clearEvents(); });
    }
    
    if (key_resp_33.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_33.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_33_allKeys = _key_resp_33_allKeys.concat(theseKeys);
      if (_key_resp_33_allKeys.length > 0) {
        key_resp_33.keys = _key_resp_33_allKeys[_key_resp_33_allKeys.length - 1].name;  // just the last key pressed
        key_resp_33.rt = _key_resp_33_allKeys[_key_resp_33_allKeys.length - 1].rt;
        key_resp_33.duration = _key_resp_33_allKeys[_key_resp_33_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_G1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_G1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_G1' ---
    for (const thisComponent of reminder_G1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_G1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_33.corr, level);
    }
    psychoJS.experiment.addData('key_resp_33.keys', key_resp_33.keys);
    if (typeof key_resp_33.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_33.rt', key_resp_33.rt);
        psychoJS.experiment.addData('key_resp_33.duration', key_resp_33.duration);
        routineTimer.reset();
        }
    
    key_resp_33.stop();
    // the Routine "reminder_G1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_Task_G1MaxDurationReached;
var _key_resp_G1_allKeys;
var practice_Task_G1MaxDuration;
var practice_Task_G1Components;
function practice_Task_G1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_Task_G1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_Task_G1Clock.reset();
    routineTimer.reset();
    practice_Task_G1MaxDurationReached = false;
    // update component parameters for each repeat
    text_G1.setText(words);
    key_resp_G1.keys = undefined;
    key_resp_G1.rt = undefined;
    _key_resp_G1_allKeys = [];
    psychoJS.experiment.addData('practice_Task_G1.started', globalClock.getTime());
    practice_Task_G1MaxDuration = null
    // keep track of which components have finished
    practice_Task_G1Components = [];
    practice_Task_G1Components.push(text_G1);
    practice_Task_G1Components.push(key_resp_G1);
    
    for (const thisComponent of practice_Task_G1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_Task_G1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_Task_G1' ---
    // get current time
    t = practice_Task_G1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_G1* updates
    if (t >= 0.0 && text_G1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_G1.tStart = t;  // (not accounting for frame time here)
      text_G1.frameNStart = frameN;  // exact frame index
      
      text_G1.setAutoDraw(true);
    }
    
    
    // *key_resp_G1* updates
    if (t >= 0.0 && key_resp_G1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_G1.tStart = t;  // (not accounting for frame time here)
      key_resp_G1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_G1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_G1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_G1.clearEvents(); });
    }
    
    if (key_resp_G1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_G1.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_G1_allKeys = _key_resp_G1_allKeys.concat(theseKeys);
      if (_key_resp_G1_allKeys.length > 0) {
        key_resp_G1.keys = _key_resp_G1_allKeys[_key_resp_G1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_G1.rt = _key_resp_G1_allKeys[_key_resp_G1_allKeys.length - 1].rt;
        key_resp_G1.duration = _key_resp_G1_allKeys[_key_resp_G1_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_G1.keys == keypad) {
            key_resp_G1.corr = 1;
        } else {
            key_resp_G1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_Task_G1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_Task_G1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_Task_G1' ---
    for (const thisComponent of practice_Task_G1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_Task_G1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_G1.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_G1.corr = 1;  // correct non-response
      } else {
         key_resp_G1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_G1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_G1.keys', key_resp_G1.keys);
    psychoJS.experiment.addData('key_resp_G1.corr', key_resp_G1.corr);
    if (typeof key_resp_G1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_G1.rt', key_resp_G1.rt);
        psychoJS.experiment.addData('key_resp_G1.duration', key_resp_G1.duration);
        routineTimer.reset();
        }
    
    key_resp_G1.stop();
    // the Routine "practice_Task_G1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_G1MaxDurationReached;
var feedback_G1MaxDuration;
var feedback_G1Components;
function feedback_G1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_G1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_G1Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_G1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_G1
    key_resp_G1_rt_sum_temp = (key_resp_G1_rt_sum_temp + Number.parseFloat(key_resp_G1.rt.toString()));
    if (key_resp_G1.corr) {
        key_resp_G1_corr_sum_temp = (key_resp_G1_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_G1.setText(msg);
    psychoJS.experiment.addData('feedback_G1.started', globalClock.getTime());
    feedback_G1MaxDuration = null
    // keep track of which components have finished
    feedback_G1Components = [];
    feedback_G1Components.push(feedback_text_G1);
    
    for (const thisComponent of feedback_G1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_G1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_G1' ---
    // get current time
    t = feedback_G1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_G1* updates
    if (t >= 0.0 && feedback_text_G1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_G1.tStart = t;  // (not accounting for frame time here)
      feedback_text_G1.frameNStart = frameN;  // exact frame index
      
      feedback_text_G1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_G1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_G1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_G1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_G1_corr_sum;
var key_resp_G1_rt_sum;
function feedback_G1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_G1' ---
    for (const thisComponent of feedback_G1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_G1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_G1
    key_resp_G1_corr_sum = key_resp_G1_corr_sum_temp;
    key_resp_G1_rt_sum = key_resp_G1_rt_sum_temp;
    
    if (feedback_G1MaxDurationReached) {
        feedback_G1Clock.add(feedback_G1MaxDuration);
    } else {
        feedback_G1Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_G1MaxDurationReached;
var _key_resp_14_allKeys;
var score_G1MaxDuration;
var score_G1Components;
function score_G1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_G1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_G1Clock.reset();
    routineTimer.reset();
    score_G1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_G1_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_G1_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_G1_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_14.keys = undefined;
    key_resp_14.rt = undefined;
    _key_resp_14_allKeys = [];
    psychoJS.experiment.addData('score_G1.started', globalClock.getTime());
    score_G1MaxDuration = null
    // keep track of which components have finished
    score_G1Components = [];
    score_G1Components.push(score_G1_text);
    score_G1Components.push(key_resp_14);
    
    for (const thisComponent of score_G1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_G1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_G1' ---
    // get current time
    t = score_G1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_G1_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_G1_text.setText(feedback_msg, false);
    }
    
    // *score_G1_text* updates
    if (t >= 0.0 && score_G1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_G1_text.tStart = t;  // (not accounting for frame time here)
      score_G1_text.frameNStart = frameN;  // exact frame index
      
      score_G1_text.setAutoDraw(true);
    }
    
    
    // *key_resp_14* updates
    if (t >= 0.0 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_14.tStart = t;  // (not accounting for frame time here)
      key_resp_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.clearEvents(); });
    }
    
    if (key_resp_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_14.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_14_allKeys = _key_resp_14_allKeys.concat(theseKeys);
      if (_key_resp_14_allKeys.length > 0) {
        key_resp_14.keys = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].name;  // just the last key pressed
        key_resp_14.rt = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].rt;
        key_resp_14.duration = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_G1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_G1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_G1' ---
    for (const thisComponent of score_G1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_G1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_14.corr, level);
    }
    psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
    if (typeof key_resp_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
        psychoJS.experiment.addData('key_resp_14.duration', key_resp_14.duration);
        routineTimer.reset();
        }
    
    key_resp_14.stop();
    // the Routine "score_G1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_G2MaxDurationReached;
var _key_resp_35_allKeys;
var reminder_G2MaxDuration;
var reminder_G2Components;
function reminder_G2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_G2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_G2Clock.reset();
    routineTimer.reset();
    reminder_G2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_35.keys = undefined;
    key_resp_35.rt = undefined;
    _key_resp_35_allKeys = [];
    psychoJS.experiment.addData('reminder_G2.started', globalClock.getTime());
    reminder_G2MaxDuration = null
    // keep track of which components have finished
    reminder_G2Components = [];
    reminder_G2Components.push(text_55);
    reminder_G2Components.push(key_resp_35);
    
    for (const thisComponent of reminder_G2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_G2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_G2' ---
    // get current time
    t = reminder_G2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_55* updates
    if (t >= 0.0 && text_55.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_55.tStart = t;  // (not accounting for frame time here)
      text_55.frameNStart = frameN;  // exact frame index
      
      text_55.setAutoDraw(true);
    }
    
    
    // *key_resp_35* updates
    if (t >= 0.0 && key_resp_35.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_35.tStart = t;  // (not accounting for frame time here)
      key_resp_35.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_35.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_35.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_35.clearEvents(); });
    }
    
    if (key_resp_35.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_35.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_35_allKeys = _key_resp_35_allKeys.concat(theseKeys);
      if (_key_resp_35_allKeys.length > 0) {
        key_resp_35.keys = _key_resp_35_allKeys[_key_resp_35_allKeys.length - 1].name;  // just the last key pressed
        key_resp_35.rt = _key_resp_35_allKeys[_key_resp_35_allKeys.length - 1].rt;
        key_resp_35.duration = _key_resp_35_allKeys[_key_resp_35_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_G2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_G2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_G2' ---
    for (const thisComponent of reminder_G2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_G2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_35.corr, level);
    }
    psychoJS.experiment.addData('key_resp_35.keys', key_resp_35.keys);
    if (typeof key_resp_35.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_35.rt', key_resp_35.rt);
        psychoJS.experiment.addData('key_resp_35.duration', key_resp_35.duration);
        routineTimer.reset();
        }
    
    key_resp_35.stop();
    // the Routine "reminder_G2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_G2MaxDurationReached;
var _key_resp_G2_allKeys;
var record_Task_G2MaxDuration;
var record_Task_G2Components;
function record_Task_G2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_G2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_G2Clock.reset();
    routineTimer.reset();
    record_Task_G2MaxDurationReached = false;
    // update component parameters for each repeat
    text_G2.setText(words);
    key_resp_G2.keys = undefined;
    key_resp_G2.rt = undefined;
    _key_resp_G2_allKeys = [];
    psychoJS.experiment.addData('record_Task_G2.started', globalClock.getTime());
    record_Task_G2MaxDuration = null
    // keep track of which components have finished
    record_Task_G2Components = [];
    record_Task_G2Components.push(text_G2);
    record_Task_G2Components.push(key_resp_G2);
    
    for (const thisComponent of record_Task_G2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_G2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_G2' ---
    // get current time
    t = record_Task_G2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_G2* updates
    if (t >= 0.0 && text_G2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_G2.tStart = t;  // (not accounting for frame time here)
      text_G2.frameNStart = frameN;  // exact frame index
      
      text_G2.setAutoDraw(true);
    }
    
    
    // *key_resp_G2* updates
    if (t >= 0.0 && key_resp_G2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_G2.tStart = t;  // (not accounting for frame time here)
      key_resp_G2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_G2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_G2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_G2.clearEvents(); });
    }
    
    if (key_resp_G2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_G2.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_G2_allKeys = _key_resp_G2_allKeys.concat(theseKeys);
      if (_key_resp_G2_allKeys.length > 0) {
        key_resp_G2.keys = _key_resp_G2_allKeys[_key_resp_G2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_G2.rt = _key_resp_G2_allKeys[_key_resp_G2_allKeys.length - 1].rt;
        key_resp_G2.duration = _key_resp_G2_allKeys[_key_resp_G2_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_G2.keys == kaypad) {
            key_resp_G2.corr = 1;
        } else {
            key_resp_G2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_G2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_G2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_G2' ---
    for (const thisComponent of record_Task_G2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_G2.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_G2.keys === undefined) {
      if (['None','none',undefined].includes(kaypad)) {
         key_resp_G2.corr = 1;  // correct non-response
      } else {
         key_resp_G2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_G2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_G2.keys', key_resp_G2.keys);
    psychoJS.experiment.addData('key_resp_G2.corr', key_resp_G2.corr);
    if (typeof key_resp_G2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_G2.rt', key_resp_G2.rt);
        psychoJS.experiment.addData('key_resp_G2.duration', key_resp_G2.duration);
        routineTimer.reset();
        }
    
    key_resp_G2.stop();
    // the Routine "record_Task_G2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_G2MaxDurationReached;
var feedback_G2MaxDuration;
var feedback_G2Components;
function feedback_G2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_G2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_G2Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_G2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_G2
    key_resp_G2_rt_sum_temp = (key_resp_G2_rt_sum_temp + Number.parseFloat(key_resp_G2.rt.toString()));
    if (key_resp_G2.corr) {
        key_resp_G2_corr_sum_temp = (key_resp_G2_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_G2.setText(msg);
    psychoJS.experiment.addData('feedback_G2.started', globalClock.getTime());
    feedback_G2MaxDuration = null
    // keep track of which components have finished
    feedback_G2Components = [];
    feedback_G2Components.push(feedback_text_G2);
    
    for (const thisComponent of feedback_G2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_G2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_G2' ---
    // get current time
    t = feedback_G2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_G2* updates
    if (t >= 0.0 && feedback_text_G2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_G2.tStart = t;  // (not accounting for frame time here)
      feedback_text_G2.frameNStart = frameN;  // exact frame index
      
      feedback_text_G2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_G2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_G2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_G2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_G2_corr_sum;
var key_resp_G2_rt_sum;
function feedback_G2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_G2' ---
    for (const thisComponent of feedback_G2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_G2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_G2
    key_resp_G2_corr_sum = key_resp_G2_corr_sum_temp;
    key_resp_G2_rt_sum = key_resp_G2_rt_sum_temp;
    
    if (feedback_G2MaxDurationReached) {
        feedback_G2Clock.add(feedback_G2MaxDuration);
    } else {
        feedback_G2Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_G2MaxDurationReached;
var _key_resp_15_allKeys;
var score_G2MaxDuration;
var score_G2Components;
function score_G2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_G2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_G2Clock.reset();
    routineTimer.reset();
    score_G2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_G2_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_G2_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_G2_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_15.keys = undefined;
    key_resp_15.rt = undefined;
    _key_resp_15_allKeys = [];
    psychoJS.experiment.addData('score_G2.started', globalClock.getTime());
    score_G2MaxDuration = null
    // keep track of which components have finished
    score_G2Components = [];
    score_G2Components.push(score_G2_text);
    score_G2Components.push(key_resp_15);
    
    for (const thisComponent of score_G2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_G2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_G2' ---
    // get current time
    t = score_G2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_G2_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_G2_text.setText(feedback_msg, false);
    }
    
    // *score_G2_text* updates
    if (t >= 0.0 && score_G2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_G2_text.tStart = t;  // (not accounting for frame time here)
      score_G2_text.frameNStart = frameN;  // exact frame index
      
      score_G2_text.setAutoDraw(true);
    }
    
    
    // *key_resp_15* updates
    if (t >= 0.0 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_15.tStart = t;  // (not accounting for frame time here)
      key_resp_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
    }
    
    if (key_resp_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_15.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_15_allKeys = _key_resp_15_allKeys.concat(theseKeys);
      if (_key_resp_15_allKeys.length > 0) {
        key_resp_15.keys = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].name;  // just the last key pressed
        key_resp_15.rt = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].rt;
        key_resp_15.duration = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_G2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_G2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_G2' ---
    for (const thisComponent of score_G2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_G2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_15.corr, level);
    }
    psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
    if (typeof key_resp_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
        psychoJS.experiment.addData('key_resp_15.duration', key_resp_15.duration);
        routineTimer.reset();
        }
    
    key_resp_15.stop();
    // the Routine "score_G2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_G3MaxDurationReached;
var _key_resp_34_allKeys;
var reminder_G3MaxDuration;
var reminder_G3Components;
function reminder_G3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_G3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_G3Clock.reset();
    routineTimer.reset();
    reminder_G3MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_34.keys = undefined;
    key_resp_34.rt = undefined;
    _key_resp_34_allKeys = [];
    psychoJS.experiment.addData('reminder_G3.started', globalClock.getTime());
    reminder_G3MaxDuration = null
    // keep track of which components have finished
    reminder_G3Components = [];
    reminder_G3Components.push(text_56);
    reminder_G3Components.push(key_resp_34);
    
    for (const thisComponent of reminder_G3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_G3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_G3' ---
    // get current time
    t = reminder_G3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_56* updates
    if (t >= 0.0 && text_56.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_56.tStart = t;  // (not accounting for frame time here)
      text_56.frameNStart = frameN;  // exact frame index
      
      text_56.setAutoDraw(true);
    }
    
    
    // *key_resp_34* updates
    if (t >= 0.0 && key_resp_34.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_34.tStart = t;  // (not accounting for frame time here)
      key_resp_34.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_34.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_34.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_34.clearEvents(); });
    }
    
    if (key_resp_34.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_34.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_34_allKeys = _key_resp_34_allKeys.concat(theseKeys);
      if (_key_resp_34_allKeys.length > 0) {
        key_resp_34.keys = _key_resp_34_allKeys[_key_resp_34_allKeys.length - 1].name;  // just the last key pressed
        key_resp_34.rt = _key_resp_34_allKeys[_key_resp_34_allKeys.length - 1].rt;
        key_resp_34.duration = _key_resp_34_allKeys[_key_resp_34_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_G3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_G3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_G3' ---
    for (const thisComponent of reminder_G3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_G3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_34.corr, level);
    }
    psychoJS.experiment.addData('key_resp_34.keys', key_resp_34.keys);
    if (typeof key_resp_34.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_34.rt', key_resp_34.rt);
        psychoJS.experiment.addData('key_resp_34.duration', key_resp_34.duration);
        routineTimer.reset();
        }
    
    key_resp_34.stop();
    // the Routine "reminder_G3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_G3MaxDurationReached;
var _key_resp_G3_allKeys;
var record_Task_G3MaxDuration;
var record_Task_G3Components;
function record_Task_G3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_G3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_G3Clock.reset();
    routineTimer.reset();
    record_Task_G3MaxDurationReached = false;
    // update component parameters for each repeat
    text_G3.setText(words);
    key_resp_G3.keys = undefined;
    key_resp_G3.rt = undefined;
    _key_resp_G3_allKeys = [];
    psychoJS.experiment.addData('record_Task_G3.started', globalClock.getTime());
    record_Task_G3MaxDuration = null
    // keep track of which components have finished
    record_Task_G3Components = [];
    record_Task_G3Components.push(text_G3);
    record_Task_G3Components.push(key_resp_G3);
    
    for (const thisComponent of record_Task_G3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_G3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_G3' ---
    // get current time
    t = record_Task_G3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_G3* updates
    if (t >= 0.0 && text_G3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_G3.tStart = t;  // (not accounting for frame time here)
      text_G3.frameNStart = frameN;  // exact frame index
      
      text_G3.setAutoDraw(true);
    }
    
    
    // *key_resp_G3* updates
    if (t >= 0.0 && key_resp_G3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_G3.tStart = t;  // (not accounting for frame time here)
      key_resp_G3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_G3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_G3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_G3.clearEvents(); });
    }
    
    if (key_resp_G3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_G3.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_G3_allKeys = _key_resp_G3_allKeys.concat(theseKeys);
      if (_key_resp_G3_allKeys.length > 0) {
        key_resp_G3.keys = _key_resp_G3_allKeys[_key_resp_G3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_G3.rt = _key_resp_G3_allKeys[_key_resp_G3_allKeys.length - 1].rt;
        key_resp_G3.duration = _key_resp_G3_allKeys[_key_resp_G3_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_G3.keys == keypad) {
            key_resp_G3.corr = 1;
        } else {
            key_resp_G3.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_G3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_G3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_G3' ---
    for (const thisComponent of record_Task_G3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_G3.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_G3.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_G3.corr = 1;  // correct non-response
      } else {
         key_resp_G3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_G3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_G3.keys', key_resp_G3.keys);
    psychoJS.experiment.addData('key_resp_G3.corr', key_resp_G3.corr);
    if (typeof key_resp_G3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_G3.rt', key_resp_G3.rt);
        psychoJS.experiment.addData('key_resp_G3.duration', key_resp_G3.duration);
        routineTimer.reset();
        }
    
    key_resp_G3.stop();
    // the Routine "record_Task_G3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_G3MaxDurationReached;
var feedback_G3MaxDuration;
var feedback_G3Components;
function feedback_G3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_G3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_G3Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_G3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_G3
    key_resp_G3_rt_sum_temp = (key_resp_G3_rt_sum_temp + Number.parseFloat(key_resp_G3.rt.toString()));
    if (key_resp_G3.corr) {
        key_resp_G3_corr_sum_temp = (key_resp_G3_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_G3.setText(msg);
    psychoJS.experiment.addData('feedback_G3.started', globalClock.getTime());
    feedback_G3MaxDuration = null
    // keep track of which components have finished
    feedback_G3Components = [];
    feedback_G3Components.push(feedback_text_G3);
    
    for (const thisComponent of feedback_G3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_G3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_G3' ---
    // get current time
    t = feedback_G3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_G3* updates
    if (t >= 0.0 && feedback_text_G3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_G3.tStart = t;  // (not accounting for frame time here)
      feedback_text_G3.frameNStart = frameN;  // exact frame index
      
      feedback_text_G3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_G3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_G3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_G3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_G3_corr_sum;
var key_resp_G3_rt_sum;
function feedback_G3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_G3' ---
    for (const thisComponent of feedback_G3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_G3.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_G3
    key_resp_G3_corr_sum = key_resp_G3_corr_sum_temp;
    key_resp_G3_rt_sum = key_resp_G3_rt_sum_temp;
    
    if (feedback_G3MaxDurationReached) {
        feedback_G3Clock.add(feedback_G3MaxDuration);
    } else {
        feedback_G3Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_G3MaxDurationReached;
var _key_resp_16_allKeys;
var score_G3MaxDuration;
var score_G3Components;
function score_G3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_G3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_G3Clock.reset();
    routineTimer.reset();
    score_G3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_G3_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_G3_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_G3_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_16.keys = undefined;
    key_resp_16.rt = undefined;
    _key_resp_16_allKeys = [];
    psychoJS.experiment.addData('score_G3.started', globalClock.getTime());
    score_G3MaxDuration = null
    // keep track of which components have finished
    score_G3Components = [];
    score_G3Components.push(score_G3_text);
    score_G3Components.push(key_resp_16);
    
    for (const thisComponent of score_G3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_G3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_G3' ---
    // get current time
    t = score_G3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_G3_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_G3_text.setText(feedback_msg, false);
    }
    
    // *score_G3_text* updates
    if (t >= 0.0 && score_G3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_G3_text.tStart = t;  // (not accounting for frame time here)
      score_G3_text.frameNStart = frameN;  // exact frame index
      
      score_G3_text.setAutoDraw(true);
    }
    
    
    // *key_resp_16* updates
    if (t >= 0.0 && key_resp_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_16.tStart = t;  // (not accounting for frame time here)
      key_resp_16.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_16.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.clearEvents(); });
    }
    
    if (key_resp_16.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_16.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_16_allKeys = _key_resp_16_allKeys.concat(theseKeys);
      if (_key_resp_16_allKeys.length > 0) {
        key_resp_16.keys = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].name;  // just the last key pressed
        key_resp_16.rt = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].rt;
        key_resp_16.duration = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_G3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_G3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_G3' ---
    for (const thisComponent of score_G3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_G3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_16.corr, level);
    }
    psychoJS.experiment.addData('key_resp_16.keys', key_resp_16.keys);
    if (typeof key_resp_16.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_16.rt', key_resp_16.rt);
        psychoJS.experiment.addData('key_resp_16.duration', key_resp_16.duration);
        routineTimer.reset();
        }
    
    key_resp_16.stop();
    // the Routine "score_G3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_H1MaxDurationReached;
var _key_resp_H1_allKeys;
var reminder_H1MaxDuration;
var reminder_H1Components;
function reminder_H1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_H1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_H1Clock.reset();
    routineTimer.reset();
    reminder_H1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_H1.keys = undefined;
    key_resp_H1.rt = undefined;
    _key_resp_H1_allKeys = [];
    psychoJS.experiment.addData('reminder_H1.started', globalClock.getTime());
    reminder_H1MaxDuration = null
    // keep track of which components have finished
    reminder_H1Components = [];
    reminder_H1Components.push(text_H1);
    reminder_H1Components.push(key_resp_H1);
    
    for (const thisComponent of reminder_H1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_H1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_H1' ---
    // get current time
    t = reminder_H1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_H1* updates
    if (t >= 0.0 && text_H1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_H1.tStart = t;  // (not accounting for frame time here)
      text_H1.frameNStart = frameN;  // exact frame index
      
      text_H1.setAutoDraw(true);
    }
    
    
    // *key_resp_H1* updates
    if (t >= 0.0 && key_resp_H1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_H1.tStart = t;  // (not accounting for frame time here)
      key_resp_H1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_H1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_H1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_H1.clearEvents(); });
    }
    
    if (key_resp_H1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_H1.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_H1_allKeys = _key_resp_H1_allKeys.concat(theseKeys);
      if (_key_resp_H1_allKeys.length > 0) {
        key_resp_H1.keys = _key_resp_H1_allKeys[_key_resp_H1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_H1.rt = _key_resp_H1_allKeys[_key_resp_H1_allKeys.length - 1].rt;
        key_resp_H1.duration = _key_resp_H1_allKeys[_key_resp_H1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_H1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_H1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_H1' ---
    for (const thisComponent of reminder_H1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_H1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_H1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_H1.keys', key_resp_H1.keys);
    if (typeof key_resp_H1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_H1.rt', key_resp_H1.rt);
        psychoJS.experiment.addData('key_resp_H1.duration', key_resp_H1.duration);
        routineTimer.reset();
        }
    
    key_resp_H1.stop();
    // the Routine "reminder_H1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_H1MaxDurationReached;
var _key_resp_19_allKeys;
var record_Task_H1MaxDuration;
var record_Task_H1Components;
function record_Task_H1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_H1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_H1Clock.reset();
    routineTimer.reset();
    record_Task_H1MaxDurationReached = false;
    // update component parameters for each repeat
    text_37.setText(name);
    key_resp_19.keys = undefined;
    key_resp_19.rt = undefined;
    _key_resp_19_allKeys = [];
    psychoJS.experiment.addData('record_Task_H1.started', globalClock.getTime());
    record_Task_H1MaxDuration = null
    // keep track of which components have finished
    record_Task_H1Components = [];
    record_Task_H1Components.push(text_37);
    record_Task_H1Components.push(key_resp_19);
    
    for (const thisComponent of record_Task_H1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_H1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_H1' ---
    // get current time
    t = record_Task_H1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_37* updates
    if (t >= 0.0 && text_37.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_37.tStart = t;  // (not accounting for frame time here)
      text_37.frameNStart = frameN;  // exact frame index
      
      text_37.setAutoDraw(true);
    }
    
    
    // *key_resp_19* updates
    if (t >= 0.0 && key_resp_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_19.tStart = t;  // (not accounting for frame time here)
      key_resp_19.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_19.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.clearEvents(); });
    }
    
    if (key_resp_19.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_19.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_19_allKeys = _key_resp_19_allKeys.concat(theseKeys);
      if (_key_resp_19_allKeys.length > 0) {
        key_resp_19.keys = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].name;  // just the last key pressed
        key_resp_19.rt = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].rt;
        key_resp_19.duration = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_19.keys == keypad) {
            key_resp_19.corr = 1;
        } else {
            key_resp_19.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_H1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_H1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_H1' ---
    for (const thisComponent of record_Task_H1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_H1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_19.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_19.corr = 1;  // correct non-response
      } else {
         key_resp_19.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_19.corr, level);
    }
    psychoJS.experiment.addData('key_resp_19.keys', key_resp_19.keys);
    psychoJS.experiment.addData('key_resp_19.corr', key_resp_19.corr);
    if (typeof key_resp_19.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_19.rt', key_resp_19.rt);
        psychoJS.experiment.addData('key_resp_19.duration', key_resp_19.duration);
        routineTimer.reset();
        }
    
    key_resp_19.stop();
    // the Routine "record_Task_H1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_H1MaxDurationReached;
var feedback_H1MaxDuration;
var feedback_H1Components;
function feedback_H1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_H1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_H1Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_H1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_H1
    key_resp_H1_rt_sum_temp = (key_resp_H1_rt_sum_temp + Number.parseFloat(key_resp_H1.rt.toString()));
    if (key_resp_H1.corr) {
        key_resp_H1_corr_sum_temp = (key_resp_H1_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_H1.setText(msg);
    psychoJS.experiment.addData('feedback_H1.started', globalClock.getTime());
    feedback_H1MaxDuration = null
    // keep track of which components have finished
    feedback_H1Components = [];
    feedback_H1Components.push(feedback_text_H1);
    
    for (const thisComponent of feedback_H1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_H1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_H1' ---
    // get current time
    t = feedback_H1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_H1* updates
    if (t >= 0.0 && feedback_text_H1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_H1.tStart = t;  // (not accounting for frame time here)
      feedback_text_H1.frameNStart = frameN;  // exact frame index
      
      feedback_text_H1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_H1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_H1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_H1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_H1_corr_sum;
var key_resp_H1_rt_sum;
function feedback_H1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_H1' ---
    for (const thisComponent of feedback_H1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_H1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_H1
    key_resp_H1_corr_sum = key_resp_H1_corr_sum_temp;
    key_resp_H1_rt_sum = key_resp_H1_rt_sum_temp;
    
    if (feedback_H1MaxDurationReached) {
        feedback_H1Clock.add(feedback_H1MaxDuration);
    } else {
        feedback_H1Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_H1MaxDurationReached;
var _key_resp_17_allKeys;
var score_H1MaxDuration;
var score_H1Components;
function score_H1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_H1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_H1Clock.reset();
    routineTimer.reset();
    score_H1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_H1_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_H1_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_H1_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_17.keys = undefined;
    key_resp_17.rt = undefined;
    _key_resp_17_allKeys = [];
    psychoJS.experiment.addData('score_H1.started', globalClock.getTime());
    score_H1MaxDuration = null
    // keep track of which components have finished
    score_H1Components = [];
    score_H1Components.push(score_H1_text);
    score_H1Components.push(key_resp_17);
    
    for (const thisComponent of score_H1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_H1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_H1' ---
    // get current time
    t = score_H1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_H1_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_H1_text.setText(feedback_msg, false);
    }
    
    // *score_H1_text* updates
    if (t >= 0.0 && score_H1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_H1_text.tStart = t;  // (not accounting for frame time here)
      score_H1_text.frameNStart = frameN;  // exact frame index
      
      score_H1_text.setAutoDraw(true);
    }
    
    
    // *key_resp_17* updates
    if (t >= 0.0 && key_resp_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_17.tStart = t;  // (not accounting for frame time here)
      key_resp_17.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_17.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.clearEvents(); });
    }
    
    if (key_resp_17.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_17.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_17_allKeys = _key_resp_17_allKeys.concat(theseKeys);
      if (_key_resp_17_allKeys.length > 0) {
        key_resp_17.keys = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].name;  // just the last key pressed
        key_resp_17.rt = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].rt;
        key_resp_17.duration = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_H1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_H1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_H1' ---
    for (const thisComponent of score_H1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_H1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_17.corr, level);
    }
    psychoJS.experiment.addData('key_resp_17.keys', key_resp_17.keys);
    if (typeof key_resp_17.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_17.rt', key_resp_17.rt);
        psychoJS.experiment.addData('key_resp_17.duration', key_resp_17.duration);
        routineTimer.reset();
        }
    
    key_resp_17.stop();
    // the Routine "score_H1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_I1MaxDurationReached;
var _key_resp_37_allKeys;
var reminder_I1MaxDuration;
var reminder_I1Components;
function reminder_I1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_I1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_I1Clock.reset();
    routineTimer.reset();
    reminder_I1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_37.keys = undefined;
    key_resp_37.rt = undefined;
    _key_resp_37_allKeys = [];
    psychoJS.experiment.addData('reminder_I1.started', globalClock.getTime());
    reminder_I1MaxDuration = null
    // keep track of which components have finished
    reminder_I1Components = [];
    reminder_I1Components.push(text_58);
    reminder_I1Components.push(key_resp_37);
    
    for (const thisComponent of reminder_I1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_I1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_I1' ---
    // get current time
    t = reminder_I1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_58* updates
    if (t >= 0.0 && text_58.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_58.tStart = t;  // (not accounting for frame time here)
      text_58.frameNStart = frameN;  // exact frame index
      
      text_58.setAutoDraw(true);
    }
    
    
    // *key_resp_37* updates
    if (t >= 0.0 && key_resp_37.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_37.tStart = t;  // (not accounting for frame time here)
      key_resp_37.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_37.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_37.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_37.clearEvents(); });
    }
    
    if (key_resp_37.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_37.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_37_allKeys = _key_resp_37_allKeys.concat(theseKeys);
      if (_key_resp_37_allKeys.length > 0) {
        key_resp_37.keys = _key_resp_37_allKeys[_key_resp_37_allKeys.length - 1].name;  // just the last key pressed
        key_resp_37.rt = _key_resp_37_allKeys[_key_resp_37_allKeys.length - 1].rt;
        key_resp_37.duration = _key_resp_37_allKeys[_key_resp_37_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_I1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_I1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_I1' ---
    for (const thisComponent of reminder_I1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_I1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_37.corr, level);
    }
    psychoJS.experiment.addData('key_resp_37.keys', key_resp_37.keys);
    if (typeof key_resp_37.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_37.rt', key_resp_37.rt);
        psychoJS.experiment.addData('key_resp_37.duration', key_resp_37.duration);
        routineTimer.reset();
        }
    
    key_resp_37.stop();
    // the Routine "reminder_I1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_Task_I1MaxDurationReached;
var _key_resp_I1_allKeys;
var practice_Task_I1MaxDuration;
var practice_Task_I1Components;
function practice_Task_I1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_Task_I1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_Task_I1Clock.reset();
    routineTimer.reset();
    practice_Task_I1MaxDurationReached = false;
    // update component parameters for each repeat
    text_I1.setText(words);
    key_resp_I1.keys = undefined;
    key_resp_I1.rt = undefined;
    _key_resp_I1_allKeys = [];
    psychoJS.experiment.addData('practice_Task_I1.started', globalClock.getTime());
    practice_Task_I1MaxDuration = null
    // keep track of which components have finished
    practice_Task_I1Components = [];
    practice_Task_I1Components.push(text_I1);
    practice_Task_I1Components.push(key_resp_I1);
    
    for (const thisComponent of practice_Task_I1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_Task_I1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_Task_I1' ---
    // get current time
    t = practice_Task_I1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_I1* updates
    if (t >= 0.0 && text_I1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_I1.tStart = t;  // (not accounting for frame time here)
      text_I1.frameNStart = frameN;  // exact frame index
      
      text_I1.setAutoDraw(true);
    }
    
    
    // *key_resp_I1* updates
    if (t >= 0.0 && key_resp_I1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_I1.tStart = t;  // (not accounting for frame time here)
      key_resp_I1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_I1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_I1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_I1.clearEvents(); });
    }
    
    if (key_resp_I1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_I1.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_I1_allKeys = _key_resp_I1_allKeys.concat(theseKeys);
      if (_key_resp_I1_allKeys.length > 0) {
        key_resp_I1.keys = _key_resp_I1_allKeys[_key_resp_I1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_I1.rt = _key_resp_I1_allKeys[_key_resp_I1_allKeys.length - 1].rt;
        key_resp_I1.duration = _key_resp_I1_allKeys[_key_resp_I1_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_I1.keys == keypad) {
            key_resp_I1.corr = 1;
        } else {
            key_resp_I1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_Task_I1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_Task_I1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_Task_I1' ---
    for (const thisComponent of practice_Task_I1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_Task_I1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_I1.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_I1.corr = 1;  // correct non-response
      } else {
         key_resp_I1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_I1.corr, level);
    }
    psychoJS.experiment.addData('key_resp_I1.keys', key_resp_I1.keys);
    psychoJS.experiment.addData('key_resp_I1.corr', key_resp_I1.corr);
    if (typeof key_resp_I1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_I1.rt', key_resp_I1.rt);
        psychoJS.experiment.addData('key_resp_I1.duration', key_resp_I1.duration);
        routineTimer.reset();
        }
    
    key_resp_I1.stop();
    // the Routine "practice_Task_I1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_I1MaxDurationReached;
var feedback_I1MaxDuration;
var feedback_I1Components;
function feedback_I1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_I1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_I1Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_I1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_I1
    key_resp_I1_rt_sum_temp = (key_resp_I1_rt_sum_temp + Number.parseFloat(key_resp_I1.rt.toString()));
    if (key_resp_I1.corr) {
        key_resp_I1_corr_sum_temp = (key_resp_I1_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_I1.setText(msg);
    psychoJS.experiment.addData('feedback_I1.started', globalClock.getTime());
    feedback_I1MaxDuration = null
    // keep track of which components have finished
    feedback_I1Components = [];
    feedback_I1Components.push(feedback_text_I1);
    
    for (const thisComponent of feedback_I1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_I1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_I1' ---
    // get current time
    t = feedback_I1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_I1* updates
    if (t >= 0.0 && feedback_text_I1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_I1.tStart = t;  // (not accounting for frame time here)
      feedback_text_I1.frameNStart = frameN;  // exact frame index
      
      feedback_text_I1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_I1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_I1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_I1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_I1_corr_sum;
var key_resp_I1_rt_sum;
function feedback_I1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_I1' ---
    for (const thisComponent of feedback_I1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_I1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_I1
    key_resp_I1_corr_sum = key_resp_I1_corr_sum_temp;
    key_resp_I1_rt_sum = key_resp_I1_rt_sum_temp;
    
    if (feedback_I1MaxDurationReached) {
        feedback_I1Clock.add(feedback_I1MaxDuration);
    } else {
        feedback_I1Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_I1MaxDurationReached;
var _key_resp_18_allKeys;
var score_I1MaxDuration;
var score_I1Components;
function score_I1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_I1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_I1Clock.reset();
    routineTimer.reset();
    score_I1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_I1_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_I1_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_I1_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_18.keys = undefined;
    key_resp_18.rt = undefined;
    _key_resp_18_allKeys = [];
    psychoJS.experiment.addData('score_I1.started', globalClock.getTime());
    score_I1MaxDuration = null
    // keep track of which components have finished
    score_I1Components = [];
    score_I1Components.push(score_I1_text);
    score_I1Components.push(key_resp_18);
    
    for (const thisComponent of score_I1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_I1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_I1' ---
    // get current time
    t = score_I1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_I1_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_I1_text.setText(feedback_msg, false);
    }
    
    // *score_I1_text* updates
    if (t >= 0.0 && score_I1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_I1_text.tStart = t;  // (not accounting for frame time here)
      score_I1_text.frameNStart = frameN;  // exact frame index
      
      score_I1_text.setAutoDraw(true);
    }
    
    
    // *key_resp_18* updates
    if (t >= 0.0 && key_resp_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_18.tStart = t;  // (not accounting for frame time here)
      key_resp_18.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_18.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.clearEvents(); });
    }
    
    if (key_resp_18.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_18.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_18_allKeys = _key_resp_18_allKeys.concat(theseKeys);
      if (_key_resp_18_allKeys.length > 0) {
        key_resp_18.keys = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].name;  // just the last key pressed
        key_resp_18.rt = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].rt;
        key_resp_18.duration = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_I1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_I1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_I1' ---
    for (const thisComponent of score_I1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_I1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_18.corr, level);
    }
    psychoJS.experiment.addData('key_resp_18.keys', key_resp_18.keys);
    if (typeof key_resp_18.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_18.rt', key_resp_18.rt);
        psychoJS.experiment.addData('key_resp_18.duration', key_resp_18.duration);
        routineTimer.reset();
        }
    
    key_resp_18.stop();
    // the Routine "score_I1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_I2MaxDurationReached;
var _key_resp_38_allKeys;
var reminder_I2MaxDuration;
var reminder_I2Components;
function reminder_I2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_I2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_I2Clock.reset();
    routineTimer.reset();
    reminder_I2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_38.keys = undefined;
    key_resp_38.rt = undefined;
    _key_resp_38_allKeys = [];
    psychoJS.experiment.addData('reminder_I2.started', globalClock.getTime());
    reminder_I2MaxDuration = null
    // keep track of which components have finished
    reminder_I2Components = [];
    reminder_I2Components.push(text_59);
    reminder_I2Components.push(key_resp_38);
    
    for (const thisComponent of reminder_I2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_I2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_I2' ---
    // get current time
    t = reminder_I2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_59* updates
    if (t >= 0.0 && text_59.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_59.tStart = t;  // (not accounting for frame time here)
      text_59.frameNStart = frameN;  // exact frame index
      
      text_59.setAutoDraw(true);
    }
    
    
    // *key_resp_38* updates
    if (t >= 0.0 && key_resp_38.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_38.tStart = t;  // (not accounting for frame time here)
      key_resp_38.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_38.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_38.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_38.clearEvents(); });
    }
    
    if (key_resp_38.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_38.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_38_allKeys = _key_resp_38_allKeys.concat(theseKeys);
      if (_key_resp_38_allKeys.length > 0) {
        key_resp_38.keys = _key_resp_38_allKeys[_key_resp_38_allKeys.length - 1].name;  // just the last key pressed
        key_resp_38.rt = _key_resp_38_allKeys[_key_resp_38_allKeys.length - 1].rt;
        key_resp_38.duration = _key_resp_38_allKeys[_key_resp_38_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_I2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_I2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_I2' ---
    for (const thisComponent of reminder_I2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_I2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_38.corr, level);
    }
    psychoJS.experiment.addData('key_resp_38.keys', key_resp_38.keys);
    if (typeof key_resp_38.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_38.rt', key_resp_38.rt);
        psychoJS.experiment.addData('key_resp_38.duration', key_resp_38.duration);
        routineTimer.reset();
        }
    
    key_resp_38.stop();
    // the Routine "reminder_I2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_I2MaxDurationReached;
var _key_resp_I2_allKeys;
var record_Task_I2MaxDuration;
var record_Task_I2Components;
function record_Task_I2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_I2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_I2Clock.reset();
    routineTimer.reset();
    record_Task_I2MaxDurationReached = false;
    // update component parameters for each repeat
    text_I2.setText(words);
    key_resp_I2.keys = undefined;
    key_resp_I2.rt = undefined;
    _key_resp_I2_allKeys = [];
    psychoJS.experiment.addData('record_Task_I2.started', globalClock.getTime());
    record_Task_I2MaxDuration = null
    // keep track of which components have finished
    record_Task_I2Components = [];
    record_Task_I2Components.push(text_I2);
    record_Task_I2Components.push(key_resp_I2);
    
    for (const thisComponent of record_Task_I2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_I2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_I2' ---
    // get current time
    t = record_Task_I2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_I2* updates
    if (t >= 0.0 && text_I2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_I2.tStart = t;  // (not accounting for frame time here)
      text_I2.frameNStart = frameN;  // exact frame index
      
      text_I2.setAutoDraw(true);
    }
    
    
    // *key_resp_I2* updates
    if (t >= 0.0 && key_resp_I2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_I2.tStart = t;  // (not accounting for frame time here)
      key_resp_I2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_I2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_I2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_I2.clearEvents(); });
    }
    
    if (key_resp_I2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_I2.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_I2_allKeys = _key_resp_I2_allKeys.concat(theseKeys);
      if (_key_resp_I2_allKeys.length > 0) {
        key_resp_I2.keys = _key_resp_I2_allKeys[_key_resp_I2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_I2.rt = _key_resp_I2_allKeys[_key_resp_I2_allKeys.length - 1].rt;
        key_resp_I2.duration = _key_resp_I2_allKeys[_key_resp_I2_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_I2.keys == keypad) {
            key_resp_I2.corr = 1;
        } else {
            key_resp_I2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_I2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_I2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_I2' ---
    for (const thisComponent of record_Task_I2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_I2.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_I2.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_I2.corr = 1;  // correct non-response
      } else {
         key_resp_I2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_I2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_I2.keys', key_resp_I2.keys);
    psychoJS.experiment.addData('key_resp_I2.corr', key_resp_I2.corr);
    if (typeof key_resp_I2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_I2.rt', key_resp_I2.rt);
        psychoJS.experiment.addData('key_resp_I2.duration', key_resp_I2.duration);
        routineTimer.reset();
        }
    
    key_resp_I2.stop();
    // the Routine "record_Task_I2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_I2MaxDurationReached;
var feedback_I2MaxDuration;
var feedback_I2Components;
function feedback_I2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_I2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_I2Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_I2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_I2
    key_resp_I2_rt_sum_temp = (key_resp_I2_rt_sum_temp + Number.parseFloat(key_resp_I2.rt.toString()));
    if (key_resp_I2.corr) {
        key_resp_I2_corr_sum_temp = (key_resp_I2_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_I2.setText(msg);
    psychoJS.experiment.addData('feedback_I2.started', globalClock.getTime());
    feedback_I2MaxDuration = null
    // keep track of which components have finished
    feedback_I2Components = [];
    feedback_I2Components.push(feedback_text_I2);
    
    for (const thisComponent of feedback_I2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_I2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_I2' ---
    // get current time
    t = feedback_I2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_I2* updates
    if (t >= 0.0 && feedback_text_I2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_I2.tStart = t;  // (not accounting for frame time here)
      feedback_text_I2.frameNStart = frameN;  // exact frame index
      
      feedback_text_I2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_I2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_I2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_I2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_I2_corr_sum;
var key_resp_I2_rt_sum;
function feedback_I2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_I2' ---
    for (const thisComponent of feedback_I2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_I2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_I2
    key_resp_I2_corr_sum = key_resp_I2_corr_sum_temp;
    key_resp_I2_rt_sum = key_resp_I2_rt_sum_temp;
    
    if (feedback_I2MaxDurationReached) {
        feedback_I2Clock.add(feedback_I2MaxDuration);
    } else {
        feedback_I2Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_I2MaxDurationReached;
var _key_resp_20_allKeys;
var score_I2MaxDuration;
var score_I2Components;
function score_I2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_I2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_I2Clock.reset();
    routineTimer.reset();
    score_I2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_I2_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_I2_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_I2_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_20.keys = undefined;
    key_resp_20.rt = undefined;
    _key_resp_20_allKeys = [];
    psychoJS.experiment.addData('score_I2.started', globalClock.getTime());
    score_I2MaxDuration = null
    // keep track of which components have finished
    score_I2Components = [];
    score_I2Components.push(score_I2_text);
    score_I2Components.push(key_resp_20);
    
    for (const thisComponent of score_I2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_I2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_I2' ---
    // get current time
    t = score_I2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_I2_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_I2_text.setText(feedback_msg, false);
    }
    
    // *score_I2_text* updates
    if (t >= 0.0 && score_I2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_I2_text.tStart = t;  // (not accounting for frame time here)
      score_I2_text.frameNStart = frameN;  // exact frame index
      
      score_I2_text.setAutoDraw(true);
    }
    
    
    // *key_resp_20* updates
    if (t >= 0.0 && key_resp_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_20.tStart = t;  // (not accounting for frame time here)
      key_resp_20.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_20.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.clearEvents(); });
    }
    
    if (key_resp_20.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_20.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_20_allKeys = _key_resp_20_allKeys.concat(theseKeys);
      if (_key_resp_20_allKeys.length > 0) {
        key_resp_20.keys = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].name;  // just the last key pressed
        key_resp_20.rt = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].rt;
        key_resp_20.duration = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_I2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_I2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_I2' ---
    for (const thisComponent of score_I2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_I2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_20.corr, level);
    }
    psychoJS.experiment.addData('key_resp_20.keys', key_resp_20.keys);
    if (typeof key_resp_20.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_20.rt', key_resp_20.rt);
        psychoJS.experiment.addData('key_resp_20.duration', key_resp_20.duration);
        routineTimer.reset();
        }
    
    key_resp_20.stop();
    // the Routine "score_I2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reminder_I3MaxDurationReached;
var _key_resp_39_allKeys;
var reminder_I3MaxDuration;
var reminder_I3Components;
function reminder_I3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_I3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    reminder_I3Clock.reset();
    routineTimer.reset();
    reminder_I3MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_39.keys = undefined;
    key_resp_39.rt = undefined;
    _key_resp_39_allKeys = [];
    psychoJS.experiment.addData('reminder_I3.started', globalClock.getTime());
    reminder_I3MaxDuration = null
    // keep track of which components have finished
    reminder_I3Components = [];
    reminder_I3Components.push(text_60);
    reminder_I3Components.push(key_resp_39);
    
    for (const thisComponent of reminder_I3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_I3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_I3' ---
    // get current time
    t = reminder_I3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_60* updates
    if (t >= 0.0 && text_60.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_60.tStart = t;  // (not accounting for frame time here)
      text_60.frameNStart = frameN;  // exact frame index
      
      text_60.setAutoDraw(true);
    }
    
    
    // *key_resp_39* updates
    if (t >= 0.0 && key_resp_39.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_39.tStart = t;  // (not accounting for frame time here)
      key_resp_39.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_39.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_39.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_39.clearEvents(); });
    }
    
    if (key_resp_39.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_39.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_39_allKeys = _key_resp_39_allKeys.concat(theseKeys);
      if (_key_resp_39_allKeys.length > 0) {
        key_resp_39.keys = _key_resp_39_allKeys[_key_resp_39_allKeys.length - 1].name;  // just the last key pressed
        key_resp_39.rt = _key_resp_39_allKeys[_key_resp_39_allKeys.length - 1].rt;
        key_resp_39.duration = _key_resp_39_allKeys[_key_resp_39_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_I3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_I3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_I3' ---
    for (const thisComponent of reminder_I3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reminder_I3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_39.corr, level);
    }
    psychoJS.experiment.addData('key_resp_39.keys', key_resp_39.keys);
    if (typeof key_resp_39.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_39.rt', key_resp_39.rt);
        psychoJS.experiment.addData('key_resp_39.duration', key_resp_39.duration);
        routineTimer.reset();
        }
    
    key_resp_39.stop();
    // the Routine "reminder_I3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var record_Task_I3MaxDurationReached;
var _key_resp_I3_allKeys;
var record_Task_I3MaxDuration;
var record_Task_I3Components;
function record_Task_I3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'record_Task_I3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    record_Task_I3Clock.reset();
    routineTimer.reset();
    record_Task_I3MaxDurationReached = false;
    // update component parameters for each repeat
    text_I3.setText(words);
    key_resp_I3.keys = undefined;
    key_resp_I3.rt = undefined;
    _key_resp_I3_allKeys = [];
    psychoJS.experiment.addData('record_Task_I3.started', globalClock.getTime());
    record_Task_I3MaxDuration = null
    // keep track of which components have finished
    record_Task_I3Components = [];
    record_Task_I3Components.push(text_I3);
    record_Task_I3Components.push(key_resp_I3);
    
    for (const thisComponent of record_Task_I3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function record_Task_I3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'record_Task_I3' ---
    // get current time
    t = record_Task_I3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_I3* updates
    if (t >= 0.0 && text_I3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_I3.tStart = t;  // (not accounting for frame time here)
      text_I3.frameNStart = frameN;  // exact frame index
      
      text_I3.setAutoDraw(true);
    }
    
    
    // *key_resp_I3* updates
    if (t >= 0.0 && key_resp_I3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_I3.tStart = t;  // (not accounting for frame time here)
      key_resp_I3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_I3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_I3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_I3.clearEvents(); });
    }
    
    if (key_resp_I3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_I3.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_I3_allKeys = _key_resp_I3_allKeys.concat(theseKeys);
      if (_key_resp_I3_allKeys.length > 0) {
        key_resp_I3.keys = _key_resp_I3_allKeys[_key_resp_I3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_I3.rt = _key_resp_I3_allKeys[_key_resp_I3_allKeys.length - 1].rt;
        key_resp_I3.duration = _key_resp_I3_allKeys[_key_resp_I3_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_I3.keys == keypad) {
            key_resp_I3.corr = 1;
        } else {
            key_resp_I3.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of record_Task_I3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function record_Task_I3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'record_Task_I3' ---
    for (const thisComponent of record_Task_I3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('record_Task_I3.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_I3.keys === undefined) {
      if (['None','none',undefined].includes(keypad)) {
         key_resp_I3.corr = 1;  // correct non-response
      } else {
         key_resp_I3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_I3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_I3.keys', key_resp_I3.keys);
    psychoJS.experiment.addData('key_resp_I3.corr', key_resp_I3.corr);
    if (typeof key_resp_I3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_I3.rt', key_resp_I3.rt);
        psychoJS.experiment.addData('key_resp_I3.duration', key_resp_I3.duration);
        routineTimer.reset();
        }
    
    key_resp_I3.stop();
    // the Routine "record_Task_I3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_I3MaxDurationReached;
var feedback_I3MaxDuration;
var feedback_I3Components;
function feedback_I3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_I3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_I3Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    feedback_I3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_I3
    key_resp_I3_rt_sum_temp = (key_resp_I3_rt_sum_temp + Number.parseFloat(key_resp_I3.rt.toString()));
    if (key_resp_I3.corr) {
        key_resp_I3_corr_sum_temp = (key_resp_I3_corr_sum_temp + 1);
        continueRoutine = false;
    } else {
        msg = "error";
    }
    
    feedback_text_I3.setText(msg);
    psychoJS.experiment.addData('feedback_I3.started', globalClock.getTime());
    feedback_I3MaxDuration = null
    // keep track of which components have finished
    feedback_I3Components = [];
    feedback_I3Components.push(feedback_text_I3);
    
    for (const thisComponent of feedback_I3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_I3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_I3' ---
    // get current time
    t = feedback_I3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text_I3* updates
    if (t >= 0.0 && feedback_text_I3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text_I3.tStart = t;  // (not accounting for frame time here)
      feedback_text_I3.frameNStart = frameN;  // exact frame index
      
      feedback_text_I3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text_I3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text_I3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_I3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var key_resp_I3_corr_sum;
var key_resp_I3_rt_sum;
function feedback_I3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_I3' ---
    for (const thisComponent of feedback_I3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_I3.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_I3
    key_resp_I3_corr_sum = key_resp_I3_corr_sum_temp;
    key_resp_I3_rt_sum = key_resp_I3_rt_sum_temp;
    
    if (feedback_I3MaxDurationReached) {
        feedback_I3Clock.add(feedback_I3MaxDuration);
    } else {
        feedback_I3Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var score_I3MaxDurationReached;
var _key_resp_21_allKeys;
var score_I3MaxDuration;
var score_I3Components;
function score_I3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'score_I3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    score_I3Clock.reset();
    routineTimer.reset();
    score_I3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from score_I3_code
    feedback_msg = "";
    accuracy = util.round(((key_resp_I3_corr_sum / 50) * 100), 2);
    rt_average = util.round(((key_resp_I3_rt_sum / 50) * 1000), 2);
    feedback_msg += (("Accuracy: " + accuracy.toString()) + "%\n");
    feedback_msg += (("RT Average: " + rt_average.toString()) + " ms\n");
    feedback_msg += "Press space bar to continue.";
    
    key_resp_21.keys = undefined;
    key_resp_21.rt = undefined;
    _key_resp_21_allKeys = [];
    psychoJS.experiment.addData('score_I3.started', globalClock.getTime());
    score_I3MaxDuration = null
    // keep track of which components have finished
    score_I3Components = [];
    score_I3Components.push(score_I3_text);
    score_I3Components.push(key_resp_21);
    
    for (const thisComponent of score_I3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function score_I3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'score_I3' ---
    // get current time
    t = score_I3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (score_I3_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      score_I3_text.setText(feedback_msg, false);
    }
    
    // *score_I3_text* updates
    if (t >= 0.0 && score_I3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      score_I3_text.tStart = t;  // (not accounting for frame time here)
      score_I3_text.frameNStart = frameN;  // exact frame index
      
      score_I3_text.setAutoDraw(true);
    }
    
    
    // *key_resp_21* updates
    if (t >= 0.0 && key_resp_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_21.tStart = t;  // (not accounting for frame time here)
      key_resp_21.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_21.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_21.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_21.clearEvents(); });
    }
    
    if (key_resp_21.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_21.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_21_allKeys = _key_resp_21_allKeys.concat(theseKeys);
      if (_key_resp_21_allKeys.length > 0) {
        key_resp_21.keys = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].name;  // just the last key pressed
        key_resp_21.rt = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].rt;
        key_resp_21.duration = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of score_I3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function score_I3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'score_I3' ---
    for (const thisComponent of score_I3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('score_I3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_21.corr, level);
    }
    psychoJS.experiment.addData('key_resp_21.keys', key_resp_21.keys);
    if (typeof key_resp_21.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_21.rt', key_resp_21.rt);
        psychoJS.experiment.addData('key_resp_21.duration', key_resp_21.duration);
        routineTimer.reset();
        }
    
    key_resp_21.stop();
    // the Routine "score_I3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
