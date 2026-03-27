# CCU cath IABP troubleshooting Eng

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-03-27**

---

\maketitle
empty


importantbox
**Learning Objectives**

- Understand indications and contraindications of IABP
- Master the complete setup procedure of the CS300 console
- Be familiar with operation mode selection and parameter adjustment
- Learn timing adjustment techniques and troubleshooting
- Recognize common problems and management strategies


importantbox

\tableofcontents

---


## Introduction


The Intra-Aortic Balloon Pump (IABP) is an essential mechanical circulatory support device that improves cardiac perfusion through the principle of counterpulsation. This manual provides detailed guidance on IABP setup, operation, and troubleshooting to ensure safe and effective use in the intensive care unit.

Please use this manual in conjunction with the video: [Intra-aortic balloon pump troubleshooting - Prague ICU](https://www.youtube.com/watch?v=hDaLAzj3MlQ)


### Origin of This Training Material


This manual is adapted from the excellent Prague ICU teaching video. With the assistance of AI tools (yt-dlp, OpenAI-Whisper, and Claude.ai), the video content has been transformed into structured English training material to facilitate systematic learning of IABP operation and management for ICU staff. 

The English version of this handout was prepared for Dr. Arvin Martin (international interventional cardiology fellow in 2025). Wish him all the best in leading his team in his country. 


## Video Timestamp Reference Table


This table indicates the timing of each topic in the video, allowing easy cross-referencing with manual sections.


| p{6cm}p{5.5cm}}   **Time** | **Topic** | **Manual Section** |
| --- | --- | --- |
| 00:00 - 00:22 | Opening introduction and demonstration | Section 1 Introduction |
| **CS300 Console Setup** |  |  |
| 00:22 - 00:50 | Three cables in the side pocket | Section 3.1 Console and accessories |
| 00:50 - 01:05 | External signal cable (ECG and pressure) | Section 3.1 Console and accessories |
| 01:05 - 01:23 | Internal ECG cable connection | Section 3.2 Cable connection steps |
| 01:23 - 01:33 | Internal pressure cable (rarely used) | Section 3.2 Cable connection steps |
| 01:33 - 01:54 | External signal cable to patient monitor | Section 3.2 Cable connection steps |
| 01:54 - 02:12 | External trigger source display on screen | Section 4 Screen interpretation |
| **Balloon Catheter Selection** |  |  |
| 02:01 - 02:27 | 7Fr 40mL balloon (162–183 cm) | Section 3.3 Balloon catheter selection |
| 02:13 - 02:27 | Fiber-optic cable function | Section 3.3 Balloon catheter selection |
| 02:27 - 02:42 | 8Fr 50mL balloon (>183 cm) | Section 3.3 Balloon catheter selection |
| **Catheter Connection and Screen Display** |  |  |
| 02:42 - 03:09 | Connect helium balloon pump cable to console | Section 3.4 Catheter connection steps |
| 03:09 - 03:21 | ECG trigger and diastolic baseline | Section 4.1 Upper ECG waveform |
| 03:21 - 03:36 | Arterial pressure waveform and dicrotic notch | Section 4.2 Lower arterial pressure waveform |
| **Operation Mode Selection** |  |  |
| 03:36 - 03:55 | Auto mode explanation | Section 5.1 Overview of operation modes |
| 03:55 - 04:11 | Semi-Auto mode and ECG trigger | Section 5.1 Overview of operation modes |
| 04:00 - 04:11 | Atrial pacer trigger mode | Section 5.2 Trigger source selection |
| 04:11 - 04:25 | Internal fixed rate 80 bpm | Section 5.2 Trigger source selection |
| 04:25 - 04:31 | Manual mode (pediatric only) | Section 5.1 Overview of operation modes |
| **Weaning Strategy** |  |  |
| 04:32 - 04:53 | Reduce frequency to 1:2 or 1:3 | Section 7.2 Weaning steps |
| 04:53 - 05:02 | Augmentation must not fall below 50 | Section 7.2 Weaning steps |
| **Timing Adjustment** |  |  |
| 05:02 - 05:08 | Auto mode: only deflation adjustable | Section 8.1 Deflation fine-tuning in Auto mode |
| 05:08 - 05:15 | Semi-Auto: both inflation and deflation adjustable | Section 8.2 Full adjustment in Semi-Auto mode |
| **Starting and Waveform Observation** |  |  |
| 05:15 - 05:29 | Press START button and balloon pressure waveform | Section 6.2 Press START button |
| 05:29 - 05:47 | Fiber-optic arterial waveform diastolic augmentation | Section 6.2 Press START button |
| 05:36 - 05:47 | Assisted vs unassisted pressure comparison | Section 4.2 Lower arterial pressure waveform |
| 05:47 - 06:13 | 1:2 frequency mode observation | Section 7.3 Key observations in 1:2 mode |
| 06:13 - 06:29 | Augmented pressure value (114 mmHg) | Section 7.3 Key observations in 1:2 mode |
| **Waveform Interpretation** |  |  |
| 06:22 - 06:29 | Normal augmentation waveform pattern | Section 10.1 Normal waveform characteristics |
| 06:29 - 06:48 | Abnormal waveform due to catheter kinking | Section 10.2 Abnormal waveform: catheter kinking |
| **Timing Errors** |  |  |
| 06:49 - 07:06 | Early inflation | Section 9.1 Early Inflation |
| 06:57 - 07:06 | Physiological effects of early inflation | Section 9.1.2 Physiological effects |
| 07:06 - 07:19 | Late inflation | Section 9.2 Late Inflation |
| 07:19 - 07:41 | Early deflation | Section 9.3 Early Deflation |
| 07:32 - 07:41 | Early deflation waveform characteristics | Section 9.3.1 Characteristics |
| 07:41 - 07:55 | Late deflation | Section 9.4 Late Deflation |
| 07:50 - 07:55 | Severe physiological effects of late deflation | Section 9.4.2 Physiological effects |
| 07:55 - 08:04 | Closing remarks and acknowledgements | --- |


**Usage Recommendations**


- Watch the full video once first for an overall understanding
- When reading the manual, use this table to locate and re-watch corresponding video segments
- Pay special attention to sections highlighted in blue—these are major chapters
- Repeatedly review the timing errors section (06:49–07:55) to master identification of all four errors


importantbox
**Critical Timestamps**

**Must-watch segments**:

- **04:53–05:02**: Augmentation must never fall below 50
- **06:29–06:48**: Waveform recognition of catheter kinking
- **06:49–07:55**: Complete explanation of all four timing errors
- **07:41–07:55**: Why late deflation is the most dangerous


importantbox


## IABP Overview


### Definition and Principle of Operation


The Intra-Aortic Balloon Pump (IABP) is a catheter-based balloon device inserted into the aorta that operates via precise timing:


- **Diastolic inflation**: Increases aortic diastolic pressure, enhancing coronary artery perfusion
- **Systolic deflation**: Reduces left ventricular afterload, decreasing myocardial oxygen demand


### Clinical Indications


| p{10cm}}   **Indication** | **Description** |  |
| --- | --- | --- |
| Cardiogenic shock | Acute myocardial infarction with hemodynamic instability |  |
| High-risk PCI | Left main or multivessel percutaneous coronary intervention |  |
| Refractory angina | Acute coronary syndrome unresponsive to medical therapy |  |
| Mechanical complications | Post-MI ventricular septal defect or severe mitral regurgitation |  |
| Cardiac surgery support | Hemodynamic support before and after cardiopulmonary bypass |  |


### Absolute Contraindications


importantbox
****Absolute contraindications – IABP must NOT be used****


1. **Aortic regurgitation**: Worsens regurgitation
2. **Aortic dissection**: May extend the dissection
3. **Aortic aneurysm**: Risk of rupture
4. **Patent ductus arteriosus**: Alters blood flow distribution


importantbox


## CS300 Console Setup


### Console and Accessories


The CS300 console is the core equipment for IABP operation. This section details the function and connection of all accessories.


#### Three Cables in the Side Pocket


| p{10cm}}   **Cable Name** | **Function** |  |
| --- | --- | --- |
| External signal cable | Connects to patient monitor to receive ECG and arterial pressure signals |  |
| Internal pressure cable | Connects to pressure transducer for traditional pressure triggering (rarely used) |  |
| Internal ECG cable | Directly connects patient ECG leads to the console |  |


### Cable Connection Steps


1. **Internal ECG cable**      - Insert cable into console ECG port - Attach ECG electrodes to patient - Confirm clear ECG waveform on console screen
2. **Internal pressure cable** (rarely used)      - Connect to pressure transducer - Used only in traditional pressure trigger mode
3. **External signal cable**      - Connect to bedside patient monitor - Console screen displays ECG and arterial pressure from the monitor - Serves as primary or backup trigger source


### Balloon Catheter Selection


| p{3cm}p{3cm}p{5cm}}   **Size** | **Volume** | **Patient Height** |
| --- | --- | --- |
| 7 Fr | 40 mL | 162–183 cm |
| 8 Fr | 50 mL | >183 cm |


**Importance of Fiber-Optic Cable**

The balloon catheter tip contains a fiber-optic sensor that transmits highly accurate arterial pressure signals at the speed of light. Compared to traditional fluid-filled transducers, it offers:

- Faster signal transmission
- Higher waveform fidelity
- Immunity to electromagnetic interference
- Real-time reflection of intra-aortic pressure changes


### Catheter Connection Steps


1. **Connect helium balloon pump cable to console**      - Ensure port is clean - Listen for “click” to confirm locking
2. **Connect catheter lumen**      - Can be connected to flush system - Or to pressure transducer for central pressure monitoring


## Screen Interpretation


### Upper ECG Waveform


- Displays electrocardiogram signal
- Horizontal line indicates **diastole** (balloon inflation period)
- Used to determine inflation and deflation timing


### Lower Arterial Pressure Waveform


- High-fidelity arterial pressure from fiber-optic sensor
- Horizontal line begins at **aortic valve closure** (dicrotic notch)
- Displays diastolic augmentation effect


**Key Points for Waveform Interpretation**


- Unassisted diastolic pressure: Diastolic pressure without assistance
- Assisted diastolic pressure: Should be lower than unassisted
- Augmented pressure: Pressure generated by balloon inflation
- Ideal: Augmented pressure significantly higher than unassisted systolic pressure


## Operation Mode Selection


### Overview of Three Operation Modes


| p{11cm}}   **Mode** | **Characteristics and Indications** |  |
| --- | --- | --- |
| Auto | - Console automatically selects best lead and trigger source - Operator cannot manually select trigger - Most commonly used mode - Only deflation timing can be fine-tuned |  |
| Semi-Auto | - Operator manually selects lead and trigger source - Both inflation and deflation timing adjustable - Suitable for experienced operators - Used in special situations (e.g., arrhythmias) |  |
| Manual | - **Pediatric use only** - **Not used** in adult ICU |  |


### Trigger Source Selection


In Semi-Auto mode, the following trigger sources are available:


| p{10.5cm}}   **Trigger Source** | **Description and Indications** |  |
| --- | --- | --- |
| ECG | - **Preferred choice** - Uses R-wave as trigger point - Suitable for most patients |  |
| Atrial Pacer | - Rarely used - Used when pacing spike is larger than R-wave - Prevents erroneous triggering |  |
| Internal | - Fixed 80 bpm asynchronous mode - **Only when no cardiac mechanical activity** - E.g., during cardiopulmonary bypass or asystole |  |


importantbox
****Trigger Source Selection Principles****


1. Prefer ECG trigger (R-wave)
2. Consider pressure trigger in arrhythmias
3. Internal mode only in exceptional circumstances
4. **Never** use Internal mode when cardiac mechanical activity is present


importantbox


## Initiating IABP Therapy


### Pre-Start Checklist


1. Confirm all cables and catheters correctly connected
2. Clear ECG and arterial pressure waveforms on screen
3. Adequate helium supply
4. Correct catheter position (confirmed by fluoroscopy or X-ray)


### Press START Button


After pressing START:

- **Balloon pressure waveform** appears
- **Fiber-optic arterial waveform** shows diastolic augmentation
- Numerical values:     itemize
- Assisted diastolic pressure lower than unassisted
- Augmented pressure significantly elevated


itemize


### Recommended Initial Settings


- Frequency: Usually start at 1:1
- Mode: Auto or Semi-Auto
- Trigger: ECG (R-wave)
- Augmentation: 100


## Weaning Strategy


### Timing for Weaning


Begin weaning when hemodynamics are stable:

- No longer requiring inotropic support
- Improved cardiac output
- Adequate tissue perfusion (urine output, lactate normal)
- No arrhythmias


### Weaning Steps


| p{11cm}}   **Step** | **Description** |  |
| --- | --- | --- |
| Reduce frequency | - Change from 1:1 to 1:2 - Observe patient response - May further reduce to 1:3 |  |
| Reduce augmentation | - Gradually decrease from 100 - ****Never below 50 - Risk of thrombosis increases below 50 |  |


importantbox
****Critical Safety Reminder****

**Augmentation must never fall below 50

Reasons:

- Incomplete balloon inflation
- Blood stasis
- Significantly increased thrombosis risk
- Potential for embolic events


Correct approach: Maintain ≥50
importantbox


### Key Observations in 1:2 Mode


In 1:2 mode:

- Screen alternates assisted and unassisted beats
- Compare blood pressure differences
- Unassisted beats should approach baseline systolic/diastolic pressures
- Assisted beats may show augmented pressure  114 mmHg (example)


## Timing Adjustment


### Deflation Fine-Tuning in Auto Mode


In Auto mode:

- Only deflation timing adjustable
- Inflation timing controlled automatically
- Adjust via on-screen controls


### Full Adjustment in Semi-Auto Mode


Semi-Auto mode allows adjustment of:

- Inflation timing
- Deflation timing


## Common Timing Errors


### Early Inflation


#### Characteristics


- Balloon inflates **before** aortic valve closure
- Inflation point before dicrotic notch
- Diastolic augmentation waveform encroaches into systole


#### Physiological Effects


importantbox
****Serious hemodynamic consequences****


- Increases left ventricular afterload
- Impedes ventricular ejection
- Increases myocardial oxygen demand
- May cause premature aortic valve closure
- Reduces stroke volume


importantbox


#### Management


1. Immediately adjust inflation timing
2. Delay inflation
3. Ensure inflation occurs after dicrotic notch


### Late Inflation


#### Characteristics


- Balloon inflates **significantly after** aortic valve closure
- Inflation point far from dicrotic notch
- Reduced diastolic augmentation


#### Physiological Effects


- Misses optimal coronary perfusion enhancement
- Suboptimal augmentation amplitude
- Reduced IABP benefit


#### Management


1. Adjust inflation timing
2. Advance inflation
3. Ensure inflation at dicrotic notch


### Early Deflation


#### Characteristics


- Balloon deflates in **mid-diastole**
- Sharp drop in arterial pressure after deflation
- Shortened augmentation duration


#### Physiological Effects


- Inadequate diastolic assistance duration
- Limited coronary perfusion improvement
- Reduced overall IABP efficacy


#### Management


1. Adjust deflation timing
2. Delay deflation
3. Ensure sufficient augmentation duration


### Late Deflation


#### Characteristics


- Balloon deflates **after** next systole begins
- Deflation delayed beyond mitral valve opening
- Impairs ventricular filling


#### Physiological Effects


importantbox
****Most dangerous timing error****


- Severely increases left ventricular afterload
- Obstructs ventricular ejection
- Increases myocardial oxygen demand
- Reduces cardiac output
- May cause hemodynamic deterioration


importantbox


#### Management


1. ****Immediately**** adjust deflation timing
2. Advance deflation
3. Ensure deflation completes before next R-wave


## Balloon Pressure Waveform Interpretation


### Normal Waveform Characteristics


**Normal balloon pressure waveform should show:**


- Sharp inflation upstroke
- Stable plateau
- Rapid deflation downstroke
- Full, undistorted waveform


### Abnormal Waveform: Catheter Kinking


If the catheter is kinked:

- Waveform becomes rounded and blunted
- Loss of plateau
- Slower inflation/deflation
- Reduced pressure rise amplitude


    
    [Image]
    When the IABP catheter is kinked, the balloon pressure waveform becomes blunted with reduced amplitude. In the image, the bottom purple waveform shows normal (leftmost) vs kinked (fifth–sixth beats).


importantbox
****Management of Kinked Waveform****


1. Immediately inspect catheter path
2. Reposition patient as needed
3. Reposition catheter if necessary
4. **Never** continue with a kinked catheter
5. Consider catheter replacement


importantbox


## Troubleshooting


### Common Problems Summary


| p{5cm}p{5cm}}   **Problem** | **Possible Causes** | **Management** |
| --- | --- | --- |
| Poor ECG signal | Loose leads, poor skin contact, dry electrodes | Check connections, replace electrodes, clean skin |
| Unstable triggering | Arrhythmia, small R-wave, EMI | Switch to pressure trigger, adjust lead selection, use external ECG |
| Balloon pressure abnormal | Catheter kink, low helium, obstruction | Reposition catheter, replace helium tank, check tubing |
| Poor augmentation | Timing error, wrong catheter position/size | Adjust timing, confirm position by X-ray, consider larger balloon |


### Emergency Situations


| p{10cm}}   **Emergency** | **Immediate Actions** |  |
| --- | --- | --- |
| Balloon rupture | 1. Stop IABP immediately 2. Notify physician 3. Prepare for catheter removal 4. Monitor for embolic events 5. Document time and circumstances |  |
| Limb ischemia | 1. Assess limb pulses 2. Notify physician 3. Consider frequency reduction 4. Remove IABP if necessary 5. Prepare vascular evaluation |  |
| Cardiac arrest | 1. Switch to Internal mode 2. Fixed 80 bpm 3. Begin CPR 4. Follow ACLS protocol |  |


## Daily Care and Monitoring


### Hourly Checklist


| p{13cm}}   **IABP Monitoring Checklist** |  |  |
| --- | --- | --- |
| $\square$ | Clear ECG waveform, no interference |  |
| $\square$ | Normal arterial pressure waveform with diastolic augmentation |  |
| $\square$ | Normal balloon pressure waveform, no kinking |  |
| $\square$ | Correct timing (no early/late inflation or deflation) |  |
| $\square$ | Appropriate values (augmented pressure > systolic pressure) |  |
| $\square$ | Adequate helium pressure |  |
| $\square$ | No alarms |  |
| $\square$ | Catheter well secured, no migration |  |
| $\square$ | Insertion site dry, no bleeding |  |
| $\square$ | Affected limb pulses present and warm |  |
| $\square$ | No neurological symptoms (numbness, pain) |  |
| $\square$ | Adequate urine output |  |


### Shift Handover Key Points


- Current settings (mode, frequency, augmentation)
- Timing adjustment history
- Hemodynamic trends
- Complication monitoring results
- Weaning plan
- Special concerns


## Complications and Prevention


### Major Complications


| p{2.5cm}p{8cm}}   **Complication** | **Incidence** | **Prevention and Management** |
| --- | --- | --- |
| Limb ischemia | 2–5 | Regular limb pulse assessment, appropriate sheath size, early detection |
| Insertion site bleeding | 5–10 | Maintain appropriate ACT, secure catheter, monitor for oozing |
| Balloon rupture | <0.5 | Regular waveform checks, avoid over-inflation, monitor for kinking |
| Infection | 1–2 | Aseptic technique, minimize dwell time, monitor for signs |
| Thrombosis/Embolism | 1–3 | Maintain augmentation ≥50 |


## Key Take-Home Messages


### Core Operating Principles


importantbox
****Remember these five core principles****


1. **Correct connections**: Verify all cables and catheters
2. **Precise timing**: Inflation at dicrotic notch, deflation before next R-wave
3. **Safe weaning**: Never reduce augmentation below 50
4. **Vigilant monitoring**: Hourly waveform and limb checks
5. **Prompt response**: Immediate correction or physician notification for abnormalities


importantbox


### Common Errors and Avoidance


| p{8cm}}   **Common Error** | **Correct Practice** |  |
| --- | --- | --- |
| **Reducing augmentation below 50 | Maintain ≥50 |  |
| **Ignoring waveform changes** | Check waveforms hourly |  |
| **Uncorrected timing errors** | Correct immediately upon detection |  |
| **Inadequate limb assessment** | Full assessment every 2 hours |  |
| **Delayed response to balloon rupture** | Stop pump and notify physician immediately |  |


## Self-Assessment


### Questions


1. What are the three cables in the CS300 side pocket and their functions?
2. Height ranges for 7Fr and 8Fr balloons?
3. Main differences between Auto and Semi-Auto modes?
4. When is Internal trigger mode used?
5. Physiological effects of early inflation?
6. Why is late deflation the most dangerous timing error?
7. Minimum allowable augmentation during weaning? Reason?
8. How to recognize catheter kinking on waveform?
9. Incidence and monitoring frequency for limb ischemia?
10. Emergency steps for balloon rupture?


### Reference Answers


1. - External signal cable: connects monitor (ECG/pressure) - Internal pressure cable: connects transducer (rare) - Internal ECG cable: direct patient ECG
2. 7Fr 40mL: 162–183 cm; 8Fr 50mL: >183 cm
3. Auto: automatic selection, only deflation adjustable; Semi-Auto: manual selection, both timings adjustable
4. Only when no cardiac mechanical activity (e.g., bypass, asystole)
5. Increases afterload, impedes ejection, increases MVO$_2$, reduces stroke volume
6. Deflation after systole begins → maximal afterload increase and ejection obstruction
7. Never below 50
8. Rounded waveform, loss of plateau, slower inflation/deflation
9. 2–5
10. Stop IABP → notify physician → prepare removal → monitor for embolism → document


\vfill
\hrule


*Adapted from Prague ICU teaching video*
*Intra-aortic balloon pump troubleshooting*
[0.3cm]
Compiled by: Mu-Yang Hsieh, MD, PhD, FESC
Lin Wen-Hui, Radiologic Technologist RT
*For educational use only*