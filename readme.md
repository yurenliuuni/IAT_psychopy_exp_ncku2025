# Implicit Association Test (IAT) - PsychoPy Experiment (NCKU 2025)

This repository contains an **Implicit Association Test (IAT)** built using **PsychoPy**. It is fully configured for both local laboratory testing (Python) and online web-based deployment (JavaScript via PsychoJS / Pavlovia). 

> **Note:** This specific configuration is optimized for Japanese language stimuli and instructions.

---

## Demo Videos
[PsychoPy program demo](https://www.youtube.com/watch?v=Yj3oj1mvT7o)
[Presentation video](https://www.canva.com/design/DAGpMDHl7Lw/C-rQPS52TExfv2sTtzCDUA/view?utm_content=DAGpMDHl7Lw&utm_campaign=designshare&utm_medium=link&utm_source=recording_view)
---

## 📂 Repository Structure

* 📂 `data/` — Contains experimental data outputs and participant response logs.
* 📂 `excel/` — Holds the condition files and stimulus lists used to drive the IAT blocks.
* 📂 `lib/` — Contains JavaScript/Python dependencies and helper functions.
* 📂 `picture/` — Image assets and visual stimuli used within the experiment.
* 📄 `IAT.psyexp` — The core PsychoPy Builder file (open this to edit the experiment visually).
* 📄 `IAT.py` / `IAT_lastrun.py` — Generated Python scripts for local execution.
* 📄 `IAT.js` / `index.html` — Exported PsychoJS code for web deployment (e.g., Pavlovia).

---

## 🛠️ Getting Started

### Local Setup (Python)
1. Download and install [PsychoPy](https://www.psychopy.org/download.html).
2. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/yurenliuuni/IAT_psychopy_exp_ncku2025.git](https://github.com/yurenliuuni/IAT_psychopy_exp_ncku2025.git)

   ```
3. Open `IAT.psyexp` in the PsychoPy Builder and click **Run**, or run the script directly from your terminal:
```bash
python IAT_lastrun.py

```



### Online Deployment (PsychoJS)

This experiment is ready to be synced with [Pavlovia](https://pavlovia.org/).

1. Open `IAT.psyexp` in PsychoPy.
2. Click on the **Sync with web project** icon.
3. Once pushed, the `index.html` and `IAT.js` files will handle the online web rendering for participants.

---

## ⚙️ Customization

To change the words, categories, or attributes used in the IAT:

1. Navigate to the `excel/` directory.
2. Update the target and attribute stimuli tracking files with your preferred Japanese words or translations.
3. Save and re-run/re-sync the experiment.



