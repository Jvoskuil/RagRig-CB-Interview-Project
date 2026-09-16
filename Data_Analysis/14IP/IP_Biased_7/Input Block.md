<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process-review purposes, and it's fine to speak candidly about decisions, including ones that didn't pan out the way you expected. Can you start by telling me your role and how you got pulled into the micro-pitting issue on the anodizing line?

Participant: Sure. I'm the process engineer responsible for surface treatment qualification on new equipment. I got pulled in when QA flagged intermittent pitting on aluminum brackets coming off the new anodizing line — this was about three weeks before a customer PPAP submission, so there wasn't a lot of slack in the schedule.

Interviewer: Walk me through what happened when you were first assigned.

Participant: The first thing on my desk that morning was a handoff note from the night-shift operator saying the bath temperature had spiked overnight and he suspected that was causing the pitting. That made immediate sense to me — anodizing bath temperature is a classic culprit for pitting, it's easy to check, and it fit a story I could act on right away. So I started there. I pulled the chiller maintenance history and had our tech verify the temperature controller. There was actually a short rectifier-log summary sitting in the same folder that flagged a calibration deviation from a few days earlier, but I didn't open it that week — the temperature story was already the frame I was working from, so the chiller took priority and the rectifier note just sat there.

Interviewer: What was your objective at that point?

Participant: Just to stop the bleeding — figure out the root cause fast enough that we could run a clean trial lot and still hit the PPAP window.

Interviewer: Let's reconstruct the timeline a bit before we get into specifics. What information did you have on day one versus what came later?

Participant: Day one, I had the operator's note, the unopened rectifier summary, and a defect-rate report showing day-shift batches were pitting more than night-shift batches. Coil certs also existed but I hadn't reviewed them. Within about a day we fixed the chiller and temperatures stabilized. But pitting didn't disappear — it dropped, but a low rate persisted. That told me temperature wasn't the whole story. From there we moved into looking at the dosing system, since the residual defect pattern looked more like a chemistry consistency issue.

Interviewer: When you saw that day-shift batches had a higher defect rate than night-shift, what was your read on that?

Participant: Honestly, my first instinct was that the day-shift operator was less careful — he's newer, and I'd noticed him rushing rack loading a couple times. I flagged it in my notes as a contributing factor. Looking back, I didn't spend much time asking whether the equipment was in worse condition during the day, or whether the chemistry itself might drift over the course of a shift. I focused on him.

Interviewer: Did you consider other explanations for that gap?

Participant: Not seriously at the time, no. It seemed like a reasonably clean explanation given what I'd observed of him.

Interviewer: Let's move to the second decision — selecting a corrective dosing technology. What were you weighing?

Participant: Once we knew residual pitting was chemistry-related, we needed a better dosing control system. There were two options. Vendor A had an automated retrofit already running at three of our sister plants. Vendor B had a newer inline sensor-based system with a stronger spec sheet on paper — actually stronger on the sensing and control criteria we cared about most — but only one reference installation, and their documentation was thin, with gaps in the install manual and unclear commissioning steps.

Interviewer: How did you decide between them?

Participant: I called a couple of engineers at sister plants, and they were generally happy with Vendor A — three plants running it gave me some confidence it was a known quantity. We'd started a requirement-by-requirement comparison of the two systems, and early on it was actually tilting toward Vendor B on the technical side. But once I had three sister plants confirming Vendor A worked, that was enough for me — I didn't finish walking through the rest of the comparison. Vendor B's applications engineer even offered to walk us through the open commissioning questions, and there wasn't any identified incompatibility, but the unresolved gaps still felt less acceptable to me than Vendor A's familiar unknowns, so I didn't take him up on it.

Interviewer: Did anything about Vendor A's track record give you pause?

Participant: One of the three plants had reported mixed results with it. I knew that going in. But with three plants running it versus one incomplete installation elsewhere, it felt like the safer bet.

Interviewer: What happened after installation?

Participant: Retrofit went in within three days. First two batches still showed minor pitting, which was a little concerning. Then the next five batches came back completely clean.

Interviewer: What was your interpretation of that pattern?

Participant: Honestly, after those two rough batches, having five clean ones in a row felt like the process had settled the score — like whatever bad luck or instability had been in the system early on had been used up, so another rough batch felt a lot less likely right then. I remember telling the quality manager the odds of another bad one showing up were pretty low, given the run we'd had.

Interviewer: Did you complete the full SPC sample size that's normally recommended before declaring a process stable?

Participant: No, we hadn't hit the full sample yet. We started prepping the certification paperwork in parallel because the timeline demanded it, not because I was ready to call the process stable — I was still treating that call as open. The streak affected my gut read more than it should have, but the certification-prep timing itself was really about the calendar.

Interviewer: Was there anything else happening during that same window that could have contributed to the improvement?

Participant: There was a routine bath chemistry replenishment scheduled in there too. But honestly, I attributed most of the turnaround to the manual rectifier voltage adjustments I was making between runs — small tweaks based on how the previous batch looked. I felt like I was actively steering it back into spec. I never really separated the two effects out.

Interviewer: That leads to the final decision — signing off for PPAP. What did that process look like?

Participant: We had a full two-week trial dataset with real variability in the earlier lots, and then a final validation lot the day before the deadline that came back completely clean. The customer SQE needed the sign-off memo within 24 hours.

Interviewer: How did you weigh the earlier variability against that final lot?

Participant: The final lot was really what tipped my confidence. It was the cleanest result we'd seen, run right before submission, so it felt like the truest picture of where the process actually stood. I referenced the earlier trial data in the memo, but the final lot carried most of the weight in my recommendation to certify.

Interviewer: Was there any other data available at that point, like the Cpk finding from the independent audit?

Participant: There was a marginal Cpk result from a quality audit, yes, but it had been filed separately from the sign-off packet, so it wasn't front and center when I was writing the recommendation.

Interviewer: Under less time pressure, would you have handled that differently?

Participant: Maybe. I think I would have pulled that Cpk data into the memo directly rather than letting the last lot speak for itself.

Interviewer: Let me ask a couple of hypotheticals. If you'd reviewed the rectifier calibration logs before the operator's temperature note, do you think the investigation would have unfolded differently?

Participant: Possibly — if the rectifier deviation had been the first thing in front of me, I probably would have chased that first instead of the chiller. It's hard to say which one I'd have found more compelling, but the order I got things in definitely shaped where I looked first.

Interviewer: And if that final validation lot had shown pitting instead of coming back clean?

Participant: Then I'd have had to delay and either extend the deadline or issue something conditional. It would have forced a harder look at the full dataset rather than leaning on one result.

Interviewer: Looking back, is there anything about how you weighed the evidence you'd reconsider?

Participant: Probably how much credit I gave myself for the manual adjustments versus the chemistry replenishment — I never really separated those out. And I'd want to revisit that attribution I made about the day-shift operator; I never fully ruled out equipment or process factors there. I'd also go back and actually open that rectifier summary on day one instead of letting the first explanation carry the week. Otherwise, given the time we had, I think the calls were defensible.

Interviewer: That's a helpful place to stop. Thanks for walking through this in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IP_Biased_7",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Process/Manufacturing Engineer (Process Selection)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Anodizing Line Micro-Pitting: Root-Cause Diagnosis and Process Certification Decision",
    "scenario_summary_internal": "A process engineer at a Tier-1 automotive parts manufacturer investigates intermittent micro-pitting defects on aluminum brackets produced on a newly commissioned anodizing line, under a 10-day deadline to certify the corrected process before a customer PPAP audit. The engineer must diagnose root cause, select a corrective dosing technology, validate trial batches, and make a final certification recommendation, all under time and cost pressure with incomplete, ambiguous, and sequentially-arriving evidence.",
    "occupational_realism": {
      "objective": "Diagnose the cause of intermittent micro-pitting on anodized aluminum brackets and certify a corrected surface-treatment process in time for a customer PPAP submission.",
      "setting": "Surface-treatment department of a Tier-1 automotive components plant; newly commissioned anodizing line with rectifier, temperature-controlled bath, and chemical dosing system; 10 working days before customer audit.",
      "constraints": [
        "10-day deadline before customer PPAP audit",
        "Limited capacity for full trial batches due to cost of scrap aluminum stock",
        "Cross-shift handoffs (day/night) with inconsistent logging practices",
        "Corporate pressure not to delay a customer product launch",
        "Only one qualified quality lab technician available for SPC data review"
      ],
      "stakeholders": [
        "Plant manager",
        "Quality manager",
        "Night-shift line operator",
        "Day-shift line operator",
        "Chemical dosing vendor representative",
        "Customer supplier quality engineer (SQE)",
        "Process engineer at sister plant"
      ],
      "technical_terms_to_use": [
        "anodizing",
        "rectifier",
        "bath chemistry",
        "dwell time",
        "PPAP",
        "SPC",
        "Cpk",
        "dosing system",
        "chiller",
        "coil certification",
        "micro-pitting",
        "DOE",
        "sister plant",
        "trial lot"
      ],
      "technical_terms_to_avoid": [
        "primacy effect",
        "anchoring",
        "fundamental attribution",
        "gambler's fallacy",
        "illusion of control",
        "ambiguity aversion",
        "bandwagon effect",
        "recency effect",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Night-shift operator's handoff note attributing pitting to an overnight bath temperature spike, received first thing on day one",
          "Unreviewed rectifier calibration logs from the past two weeks",
          "Unreviewed incoming aluminum coil chemistry certificates",
          "A defect-rate comparison report showing day-shift batches had a higher pitting rate than night-shift batches"
        ],
        "new_information_after_decision": [
          "Chiller repaired and bath temperature stabilized within one day",
          "Micro-pitting recurs at a reduced but nonzero rate, suggesting temperature was not the sole cause"
        ],
        "alternatives": [
          "Prioritize chiller repair and temperature control as the primary corrective action",
          "Investigate rectifier calibration drift first",
          "Review incoming coil chemistry certificates first",
          "Commission a multi-factor DOE across temperature, rectifier output, and material chemistry before acting"
        ],
        "intended_action": "Engineer focuses corrective resources on the bath temperature/chiller system and cites day-shift operator competency as a contributing factor, deferring rectifier and material reviews."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Residual low-rate pitting persists after temperature correction",
          "Vendor A offers an automated dosing control retrofit already installed at three sister plants, with mixed results reported at one of them",
          "Vendor B offers a newer inline sensor-based dosing system with a stronger published spec sheet but only one reference installation and incomplete documentation",
          "Informal calls with sister-plant engineers describing general satisfaction with Vendor A"
        ],
        "new_information_after_decision": [
          "Vendor A retrofit installed within three days",
          "Initial trial batches show a marked drop in defect rate"
        ],
        "alternatives": [
          "Select Vendor A's established multi-plant dosing retrofit",
          "Select Vendor B's newer sensor-based dosing system",
          "Run a small parallel trial of both systems before committing",
          "Delay a technology decision and continue manual dosing adjustments"
        ],
        "intended_action": "Engineer selects Vendor A primarily because it is already used at multiple sister plants, and explicitly rules out Vendor B due to its incomplete documentation despite its stronger spec sheet."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "First two post-retrofit batches still show minor pitting",
          "Next five consecutive batches come back clean after the engineer makes manual rectifier voltage adjustments between runs",
          "Bath chemistry was also replenished on a routine schedule during this same window",
          "Full SPC sample size is still below the minimum recommended for capability confirmation"
        ],
        "new_information_after_decision": [
          "A later independent quality audit finds the process capability index (Cpk) is only marginally within specification, not fully stable"
        ],
        "alternatives": [
          "Declare the process stable based on the five-batch clean streak and proceed toward certification",
          "Run the full recommended SPC sample size before drawing conclusions",
          "Attribute the improvement to the two initial bad batches being an isolated fluke unlikely to recur",
          "Commission a short confirmatory DOE isolating voltage adjustment from chemistry replenishment"
        ],
        "intended_action": "Engineer proceeds toward certification testing without the full SPC sample, crediting personal mid-run voltage adjustments for the clean streak and treating the earlier bad batches as now behind a run of 'owed' good outcomes."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Full trial-lot dataset spans two weeks and shows real variability across early lots",
          "The final validation lot, run the day before the deadline, comes back completely clean",
          "Customer SQE requires a sign-off memo within 24 hours",
          "Marginal Cpk finding from the independent audit is available but was filed separately from the sign-off packet"
        ],
        "new_information_after_decision": [
          "Process is certified and PPAP is submitted on schedule; longer-term field performance remains unknown at the time of the interview"
        ],
        "alternatives": [
          "Certify the process based heavily on the clean final lot",
          "Base the certification decision on the full two-week trial dataset including earlier variability",
          "Request a short deadline extension for a complete statistical review",
          "Issue a conditional certification pending additional monitoring"
        ],
        "intended_action": "Engineer signs off on certification, emphasizing the final clean lot in the memo and giving comparatively little weight to the earlier variability documented across the full trial period."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what happened when you were first assigned to investigate the micro-pitting issue.",
        "What was your overall objective going into this investigation?"
      ],
      "timeline_reconstruction": [
        "What information did you have on day one, and what came in later?",
        "How did the investigation unfold from the initial report to the final certification decision?",
        "What changed in your understanding as new data arrived?"
      ],
      "decision_point_probes": [
        "At that point, what alternatives did you consider, and why did you choose the one you did?",
        "What evidence or cues were you weighing most heavily at that moment?",
        "Who or what influenced your thinking at this stage?",
        "How confident were you at the time, and what would have changed your mind?",
        "Was there time pressure affecting this particular decision?"
      ],
      "closing_hypotheticals": [
        "If you had reviewed the rectifier calibration logs before the operator's report, do you think your investigation would have gone differently?",
        "If the final validation lot had shown pitting instead of a clean result, how would that have changed your certification decision?",
        "Looking back, is there anything about how you weighed the evidence that you'd do differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Primacy Effect",
        "decision_point": 1,
        "mechanism": "The engineer gives disproportionate investigative weight to the first explanation received (night-shift operator's temperature-spike report) and organizes subsequent inquiry around confirming it, deferring review of rectifier and material data that arrived later.",
        "affected_reasoning_operation": "Hypothesis prioritization at the start of a diagnostic investigation",
        "evidence_available_at_time": [
          "Night-shift operator's handoff note (received first)",
          "Unreviewed rectifier calibration logs",
          "Unreviewed coil chemistry certificates"
        ],
        "required_textual_manifestation": "Engineer explicitly states that the temperature explanation 'made sense right away' or was the natural starting point because it was the first thing reported, and describes deferring the rectifier/material checks as a result.",
        "plausible_nonbias_interpretation": "Temperature control is a common and easily testable first suspect in anodizing defects, so starting there could reflect a reasonable triage heuristic rather than order-driven weighting.",
        "strength": "subtle",
        "do_not_make_explicit": ["primacy", "anchoring", "first impression bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Fundamental Attribution Bias",
        "decision_point": 1,
        "mechanism": "The engineer explains a defect-rate difference between shifts by attributing it to the day-shift operator's personal carelessness or insufficient skill, rather than considering situational factors like equipment condition, bath chemistry drift, or handoff documentation quality.",
        "affected_reasoning_operation": "Causal attribution of a performance difference between personnel",
        "evidence_available_at_time": [
          "Defect-rate comparison report showing day-shift batches had higher pitting rates than night-shift batches"
        ],
        "required_textual_manifestation": "Engineer characterizes the day-shift operator as careless, inattentive, or less capable when explaining the defect-rate gap, without weighing equipment or process-condition explanations for the same data.",
        "plausible_nonbias_interpretation": "If the day-shift operator genuinely had less experience or documented training gaps, personal-factor attribution could be a reasonable read of the same evidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["fundamental attribution error", "dispositional vs situational"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Ambiguity effect",
        "decision_point": 2,
        "mechanism": "The engineer avoids Vendor B's sensor-based dosing system specifically because its documentation is incomplete or unclear, even though its published specifications are stronger, preferring the more thoroughly documented but less proven-in-context option.",
        "affected_reasoning_operation": "Option elimination under incomplete information",
        "evidence_available_at_time": [
          "Vendor B's published spec sheet (favorable) and incomplete installation documentation (unfavorable clarity)"
        ],
        "required_textual_manifestation": "Engineer states that Vendor B was ruled out mainly because 'we didn't have enough clarity on how it performs' or similar, despite acknowledging its stronger specs.",
        "plausible_nonbias_interpretation": "Avoiding a poorly documented system before a customer audit could reflect legitimate risk management rather than aversion to ambiguity itself.",
        "strength": "subtle",
        "do_not_make_explicit": ["ambiguity aversion", "uncertainty avoidance"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "decision_point": 2,
        "mechanism": "The engineer selects Vendor A largely because it is already used at three sister plants and informally endorsed by peer engineers, despite one of those plants reporting mixed results, rather than basing the choice on independent technical evaluation.",
        "affected_reasoning_operation": "Vendor selection weighting based on peer adoption prevalence",
        "evidence_available_at_time": [
          "Informal calls with sister-plant engineers describing general satisfaction with Vendor A",
          "Knowledge that one sister plant had mixed results with Vendor A"
        ],
        "required_textual_manifestation": "Engineer justifies the choice with language like 'everyone else is running it' or 'three plants already use it,' downplaying the mixed-result data point.",
        "plausible_nonbias_interpretation": "Wide internal adoption can be a legitimate proxy for supportability and spare-parts availability, independent of peer-conformity pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon", "social proof", "conformity"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Gambler's Fallacy",
        "decision_point": 3,
        "mechanism": "The engineer or team reasons that after two defective batches, the process was statistically 'due' for a run of good batches, treating sequential independent batch outcomes as if they were anti-correlated.",
        "affected_reasoning_operation": "Probabilistic interpretation of a sequence of batch outcomes",
        "evidence_available_at_time": [
          "Batch outcome log showing two defective batches followed by five clean batches"
        ],
        "required_textual_manifestation": "Engineer explicitly frames the clean streak as the process having been 'due' for good results or the bad batches as making a further bad batch unlikely, rather than treating each batch as an independent trial.",
        "plausible_nonbias_interpretation": "A genuine underlying cause (e.g., dosing retrofit taking effect) could independently explain an improving trend, without any probabilistic reasoning error.",
        "strength": "subtle",
        "do_not_make_explicit": ["gambler's fallacy", "due for a win", "law of averages"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Illusion of control",
        "decision_point": 3,
        "mechanism": "The engineer attributes the clean batch streak primarily to their own manual mid-run rectifier voltage adjustments, overestimating personal control over an outcome also plausibly explained by a routine bath chemistry replenishment occurring in the same window.",
        "affected_reasoning_operation": "Causal credit assignment for a process outcome involving both personal action and an uncontrolled concurrent factor",
        "evidence_available_at_time": [
          "Engineer's own process-log annotations documenting manual voltage adjustments",
          "Record of a routine bath chemistry replenishment occurring in the same period"
        ],
        "required_textual_manifestation": "Engineer states confidence that their manual tuning is what stabilized the process, without acknowledging the concurrent chemistry replenishment as an alternative explanation.",
        "plausible_nonbias_interpretation": "Manual voltage tuning is a legitimate corrective action in anodizing and could genuinely have contributed to the improvement.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of control", "overestimating personal influence"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Recency effect",
        "decision_point": 4,
        "mechanism": "In the final certification sign-off, the engineer gives disproportionate weight to the most recently produced validation lot (completely clean) over the fuller two-week trial dataset that documented earlier variability.",
        "affected_reasoning_operation": "Evidence weighting in a final go/no-go certification judgment",
        "evidence_available_at_time": [
          "Full two-week trial-lot dataset showing earlier variability",
          "Final validation lot results (clean), produced immediately before the deadline"
        ],
        "required_textual_manifestation": "Engineer's sign-off reasoning emphasizes the final clean lot as the deciding factor, with the earlier variability mentioned only in passing or filed separately.",
        "plausible_nonbias_interpretation": "The most recent lot could legitimately be the most representative of the corrected process state, making recency-weighting a defensible engineering judgment rather than an error.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "recency bias", "last impression"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is 'biased', no paired control is generated under this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Order in which diagnostic evidence sources were reviewed at the start of the investigation",
      "original_state": "Night-shift operator's temperature-spike report is received and reviewed first, before rectifier calibration logs or coil chemistry certificates.",
      "counterfactual_state": "Rectifier calibration logs are reviewed first, before the operator's temperature-spike report or coil chemistry certificates.",
      "variables_to_hold_constant": [
        "Underlying true root cause(s) of the micro-pitting defect",
        "Deadline pressure and PPAP audit timing",
        "Vendor options and their documentation quality",
        "Batch outcome sequence during trial runs",
        "Personnel and stakeholder roles"
      ],
      "expected_causal_difference": "If rectifier data is reviewed first, the engineer's initial hypothesis prioritization at Decision Point 1 should anchor on rectifier calibration rather than bath temperature, testing whether order of evidence receipt (rather than the content of the operator's report) drives the initial hypothesis weighting.",
      "causal_test_question": "Does changing which evidence source is encountered first at the start of the investigation change which root-cause hypothesis the engineer prioritizes, holding all other facts constant?"
    },
    "generation_checks": [
      "Confirm exactly four decision points are present, each with at least two plausible alternatives.",
      "Confirm exactly one instance each of Primacy Effect, Fundamental Attribution Bias, Gambler's Fallacy, Illusion of control, Ambiguity effect, Bandwagon effect, and Recency effect is embedded, with no repetitions or additional unrequested bias instances.",
      "Confirm no bias name, definition, or psychological label appears anywhere in the public interview text.",
      "Confirm each embedded instance is textually distinguishable from a neutral, justified, or expertise-based explanation.",
      "Confirm instances sharing a decision point (cb_01/cb_02, cb_03/cb_04, cb_05/cb_06) each rely on distinct evidence sources or reasoning operations.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm final word count falls between 1,215 and 1,485 words without repetitive exposition.",
      "Confirm consequences described do not mechanically prove or disprove whether any decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Primacy Effect", "occurrences": 1, "mechanism_constraint": "Must manifest as disproportionate weighting of the first-received diagnostic explanation over later-arriving evidence." },
      { "bias": "Fundamental Attribution Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as personal/dispositional attribution for a performance gap where situational factors are also plausible and available." },
      { "bias": "Gambler's Fallacy", "occurrences": 1, "mechanism_constraint": "Must manifest as treating independent sequential batch outcomes as statistically compensatory." },
      { "bias": "Illusion of control", "occurrences": 1, "mechanism_constraint": "Must manifest as overattributing a process outcome to personal manual intervention over a concurrent uncontrolled factor." },
      { "bias": "Ambiguity effect", "occurrences": 1, "mechanism_constraint": "Must manifest as avoidance of an option due to unclear/incomplete information despite favorable known attributes." },
      { "bias": "Bandwagon effect", "occurrences": 1, "mechanism_constraint": "Must manifest as decision weighting driven by peer/prevalence adoption rather than independent technical evaluation." },
      { "bias": "Recency effect", "occurrences": 1, "mechanism_constraint": "Must manifest as overweighting the most recently obtained result relative to the fuller historical dataset in a final judgment." }
    ],
    "target_bias_names": [
      "Primacy Effect",
      "Fundamental Attribution Bias",
      "Gambler's Fallacy",
      "Illusion of control",
      "Ambiguity effect",
      "Bandwagon effect",
      "Recency effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Primacy Effect", "requested_occurrences": 1 },
      { "bias": "Fundamental Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Gambler's Fallacy", "requested_occurrences": 1 },
      { "bias": "Illusion of control", "requested_occurrences": 1 },
      { "bias": "Ambiguity effect", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Recency effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Primacy Effect" },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias" },
      { "instance_id": "cb_03", "bias": "Ambiguity effect" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect" },
      { "instance_id": "cb_05", "bias": "Gambler's Fallacy" },
      { "instance_id": "cb_06", "bias": "Illusion of control" },
      { "instance_id": "cb_07", "bias": "Recency effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias", "decision_point": 1 },
      { "instance_id": "cb_03", "bias": "Ambiguity effect", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "decision_point": 2 },
      { "instance_id": "cb_05", "bias": "Gambler's Fallacy", "decision_point": 3 },
      { "instance_id": "cb_06", "bias": "Illusion of control", "decision_point": 3 },
      { "instance_id": "cb_07", "bias": "Recency effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Primacy Effect",
        "mechanism": "Disproportionate weight given to the first-received explanation (temperature-spike report) over later-reviewed rectifier/material evidence.",
        "affected_reasoning_operation": "Hypothesis prioritization at investigation start",
        "evidence_source": "Order of arrival of diagnostic reports",
        "distinctiveness_requirement": "Must be distinguished from cb_02 by relying on order-of-information-receipt rather than personnel-performance data."
      },
      {
        "instance_id": "cb_02",
        "bias": "Fundamental Attribution Bias",
        "mechanism": "Attribution of a shift-level defect-rate gap to operator personal traits rather than situational/process factors.",
        "affected_reasoning_operation": "Causal attribution of personnel performance difference",
        "evidence_source": "Defect-rate comparison report between shifts",
        "distinctiveness_requirement": "Must be distinguished from cb_01 by relying on personnel-performance comparison data at a different moment in the same decision point."
      },
      {
        "instance_id": "cb_03",
        "bias": "Ambiguity effect",
        "mechanism": "Rejection of a technically favorable option specifically because of incomplete/unclear documentation.",
        "affected_reasoning_operation": "Option elimination under incomplete information",
        "evidence_source": "Vendor B documentation completeness and spec sheet",
        "distinctiveness_requirement": "Must be distinguished from cb_04 by focusing on documentation clarity for the rejected option, not peer adoption of the chosen option."
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "mechanism": "Vendor selection driven by peer/sister-plant prevalence rather than independent technical merit.",
        "affected_reasoning_operation": "Vendor selection weighting",
        "evidence_source": "Informal peer engineer endorsements and sister-plant adoption count",
        "distinctiveness_requirement": "Must be distinguished from cb_03 by relying on peer-adoption evidence for the chosen option, not documentation ambiguity of the rejected option."
      },
      {
        "instance_id": "cb_05",
        "bias": "Gambler's Fallacy",
        "mechanism": "Sequential independent batch outcomes treated as statistically self-correcting ('due' for good results).",
        "affected_reasoning_operation": "Probabilistic interpretation of outcome sequence",
        "evidence_source": "Chronological batch outcome log",
        "distinctiveness_requirement": "Must be distinguished from cb_06 by relying on the sequence/count of batch outcomes, not on causal credit for a specific intervention."
      },
      {
        "instance_id": "cb_06",
        "bias": "Illusion of control",
        "mechanism": "Overattribution of process stabilization to personal manual voltage adjustments over a concurrent uncontrolled factor (chemistry replenishment).",
        "affected_reasoning_operation": "Causal credit assignment for outcome with confounded personal and external factors",
        "evidence_source": "Engineer's own process-log annotations and concurrent replenishment record",
        "distinctiveness_requirement": "Must be distinguished from cb_05 by relying on personal-action attribution rather than sequence-based probability reasoning."
      },
      {
        "instance_id": "cb_07",
        "bias": "Recency effect",
        "mechanism": "Overweighting of the most recent validation lot relative to the full two-week trial dataset in the final certification judgment.",
        "affected_reasoning_operation": "Evidence weighting in final go/no-go judgment",
        "evidence_source": "Comparison of final lot result versus full trial-lot dataset",
        "distinctiveness_requirement": "Single instance; distinguished from earlier decision points by occurring only in the final sign-off judgment, not during trial monitoring."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Ambiguity effect", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "strength": "subtle" },
      { "instance_id": "cb_05", "bias": "Gambler's Fallacy", "strength": "subtle" },
      { "instance_id": "cb_06", "bias": "Illusion of control", "strength": "moderate" },
      { "instance_id": "cb_07", "bias": "Recency effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Order in which diagnostic evidence sources were reviewed at the start of the investigation",
      "original_state": "Operator's temperature-spike report reviewed first",
      "changed_state": "Rectifier calibration logs reviewed first",
      "variables_to_hold_constant": [
        "Underlying true root cause(s) of the micro-pitting defect",
        "Deadline pressure and PPAP audit timing",
        "Vendor options and their documentation quality",
        "Batch outcome sequence during trial runs",
        "Personnel and stakeholder roles"
      ]
    },
    "scenario_id": "IP_Biased_7",
    "domain_id": "IP",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across 4 decision points with a maximum of two distinct biases co-located per decision point (DP1: cb_01/cb_02, DP2: cb_03/cb_04, DP3: cb_05/cb_06, DP4: cb_07 alone); no bias assigned more than one instance total, so intra-bias separation rules were not triggered; co-located instances at the same decision point use distinct evidence sources and reasoning operations per instance as documented in intended_mechanisms.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Underlying true root cause(s) of the micro-pitting defect",
      "Deadline pressure and PPAP audit timing",
      "Vendor options and their documentation quality",
      "Batch outcome sequence during trial runs",
      "Personnel and stakeholder roles"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "diagnostic_hypothesis_prioritization",
        "raw_interview_anchor": "The first thing on my desk that morning was a handoff note ... That made immediate sense to me ... So I started there.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "The participant gives disproportionate weight to the first-received temperature explanation and uses it to prioritize the initial diagnostic search over available alternative evidence."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "causal_attribution",
        "raw_interview_anchor": "My first instinct was that the day-shift operator was less careful ... I focused on him.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "A shift-level defect-rate difference is attributed primarily to the operator's disposition while equipment and chemistry explanations remain underexamined."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_based_diagnostic_update",
        "raw_interview_anchor": "Temperatures stabilized. But pitting didn't disappear ... That told me temperature wasn't the whole story. From there we moved into looking at the dosing system.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive, evidence-responsive update after the chiller intervention; it contains no hidden manifested bias."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "option_evaluation_under_uncertainty",
        "raw_interview_anchor": "Vendor B ... [had] a stronger spec sheet ... but ... documentation was thin ... Vendor B's ... unresolved gaps still felt less acceptable ... so I didn't take him up on it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "The technically favorable option is rejected in part because its documentation and commissioning information are incomplete, despite an available path to resolve the uncertainty."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "peer_adoption_weighting",
        "raw_interview_anchor": "Once I had three sister plants confirming Vendor A worked, that was enough for me ... I didn't finish walking through the rest of the comparison.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_04"],
        "ground_truth_rationale": "Selection is materially driven by sister-plant adoption and endorsements before the independent technical comparison is completed."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "probability_interpretation",
        "raw_interview_anchor": "Having five clean ones in a row felt like the process had settled the score ... another rough batch felt a lot less likely.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_05"],
        "ground_truth_rationale": "The participant treats the sequence of outcomes as statistically compensatory and lowers the estimated probability of a future bad batch."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "causal_credit_assignment",
        "raw_interview_anchor": "I attributed most of the turnaround to the manual rectifier voltage adjustments ... There was a routine bath chemistry replenishment scheduled in there too ... I never really separated the two effects out.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_06"],
        "ground_truth_rationale": "The improvement is overattributed to the participant's manual intervention despite a concurrent uncontrolled chemistry replenishment."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "timeline_driven_certification_preparation",
        "raw_interview_anchor": "We hadn't hit the full sample yet. We started prepping the certification paperwork in parallel because the timeline demanded it ... the call [was] open.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This separates a calendar-driven preparation action from the gambler's-fallacy gut read and does not itself establish a hidden bias."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "final_evidence_weighting",
        "raw_interview_anchor": "The final lot was really what tipped my confidence ... it felt like the truest picture ... the final lot carried most of the weight in my recommendation to certify.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_07"],
        "ground_truth_rationale": "The most recent clean validation lot is weighted more heavily than the fuller two-week trial dataset and the marginal Cpk result."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
