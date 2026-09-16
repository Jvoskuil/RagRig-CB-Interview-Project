You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. As before, this is about understanding your reasoning process during the Stope 14-East event, not evaluating the outcome. Alright to continue?

Participant: Yes, fine.

Interviewer: Can you set the scene — your role, and what you were working toward that shift?

Participant: I'm the Health and Safety Officer, dayshift. My job that day was mostly routine oversight of active headings, including Stope 14-East, a longhole stope. One thing that was a bit different from a typical week was that our tonnage target had just been reset to a weekly figure rather than a shift figure, so there wasn't the usual same-day scramble hanging over us. That gave us a bit more room to breathe on scheduling, in theory.

Interviewer: Walk me through what happened when you first heard about the noise.

Participant: Around 06:40 a miner radioed in saying he'd heard intermittent cracking, kind of a popping sound, in the back of 14-East. No alarm had tripped on the microseismic array at that point. Even with the weekly target giving us some slack, my first thought went straight to the rockburst at our sister operation two months back — that made the trade press, and it was still something everyone on site talked about. The conditions weren't identical, but same ore body region, and it was vivid enough that I treated the report as more likely to be heading toward something serious than the instruments alone would have suggested.

Interviewer: What alternatives did you weigh at that point?

Participant: Full evacuation and stop-work pending geotech, enhanced monitoring with limited access, or just getting the instrument tech to check readings first. I went with enhanced monitoring and limited access. The instruments weren't flagging anything, but that sister-mine memory carried a lot of weight for me regardless of what the schedule looked like that day.

Interviewer: Let's move to the extensometer readings later that morning.

Participant: The 05:00 baseline was 0.2mm, our normal quiet reading. By 09:40 it had moved to 0.6mm — three times the baseline in about three hours. I looked at that and thought, well, compared to this morning, it's still a small number. I didn't go back to the GCMP's rate-of-change table, which is actually how you're supposed to judge it — the plan cares about the speed of movement, not just where it sits against an earlier point. Looking back, I was using the wrong reference.

Interviewer: What information, if you'd had it in front of you right then, would have changed that call?

Participant: If the rate-of-change figure had been sitting right next to the raw number, I think I'd have caught it. As it was, all I had was two numbers from two different times, and comparing them felt natural.

Interviewer: Did the weekly target play into that decision at all?

Participant: Honestly, not much. There wasn't pressure to rush a call because production wasn't riding on that hour. It was more just how I read the two numbers side by side.

Interviewer: Tell me about the conversation with your shift supervisor.

Participant: About an hour later. He's got twenty-two years underground, most of it here. He mentioned hearing similar popping back in 2009 that came to nothing, and he was confident this was the same kind of thing. Around then the microseismic count for the shift had actually climbed to six events an hour, just over our flag threshold of five. I didn't really push on whether the 2009 case matched today's rock type or blast pattern. His track record carried a lot of weight for me in that moment.

Interviewer: You also looked at a crack in that panel — can you describe that?

Participant: There was a hairline crack, about a millimeter, photographed and logged the week before as insignificant. Today's crack looked about the same width to me, so I read it as consistent with what we already knew was fine. What I didn't do was connect it to the seismic count that had just crossed the threshold — I was judging the crack against the old photo instead of against the newer number.

Interviewer: What alternatives did you consider before allowing continued access?

Participant: Follow the seismic threshold strictly and hold the stope for engineer sign-off, reduce crew size as a middle path, or trust the supervisor's read and continue with limited crew. I went with limited access, mostly on his confidence and my own read of the crack photo.

Interviewer: Given that production wasn't due until end of week, did that change how you approached this call?

Participant: Not really — there wasn't an obvious reason to hurry one way or the other. It felt more like I was weighing the supervisor's experience and that photo comparison on their own terms.

Interviewer: What happened after that?

Participant: The engineer eventually called back wanting the full event log, and around the same time someone noticed a second, wider crack near the first. Then at 13:15 we had a minor spall — no injuries, some equipment damage. Shift change had happened about ninety minutes earlier.

Interviewer: When you wrote the incident report, how did you land on the causes?

Participant: Putting it together — the overnight temperature drop, the shift change not long before, and the blasting in the next panel the previous week — it read as a pretty clean explanation: cooling stress plus the handover timing plus residual vibration from that blast. That's what I put forward as the account, even though the engineer's later note said several factors were plausible and none could be confirmed as dominant.

Interviewer: And how did you frame responsibility?

Participant: I focused mainly on the miner who first reported the sounds and didn't flag it again once the popping continued — I felt if he'd called it in a second time, we might have caught it sooner. I did mention the missing engineer sign-off after the six-events flag, but it came across more as a process note than a central cause.

Interviewer: If the sister-mine rockburst had never happened, would your first call have gone differently?

Participant: Probably. Without that fresh in mind, I think I'd have waited on the instrument tech's check before doing anything.

Interviewer: If a less experienced supervisor had said the same thing about 2009, would you have weighted it the same way?

Participant: No, I don't think so. His years underground were a big part of why I trusted the read.

Interviewer: Last one — how confident are you now that the causes in the report were the real ones?

Participant: Less than when I wrote it. It felt like a complete picture at the time, but there were threads I didn't fully chase down.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Counterfactual_6",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Mine Safety/Health & Safety Officer",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Strata Noise Escalation in Stope 14-East — Reduced-Urgency Production Variant",
    "scenario_summary_internal": "This is the counterfactual pair to MU_Biased_6. All material facts, actors, instrument readings, the supervisor conversation, the sister-mine memory, the crack photographs, and the spall event are held constant. The single altered causal variable is the production quota deadline: instead of tonnage being due by the end of the current dayshift (acute same-day pressure), the quota is due by the end of the week, giving the HSO materially more schedule slack across the same sequence of decisions. The same six bias instances specified in the manifest are still planned, since they arise from evidence-processing patterns (recall, comparison, credibility weighting, causal narrative-building, responsibility attribution) that are not mechanically caused by the deadline variable itself.",
    "occupational_realism": {
      "objective": "Determine, at four successive points during the shift, whether Stope 14-East can safely continue production or must be restricted/evacuated, and afterward produce an accurate incident account of a minor rock-spall event, under a relaxed same-week production deadline rather than a same-shift deadline.",
      "setting": "Underground hard-rock mine, approximately 900m depth, longhole stoping method, instrumented with extensometers and a microseismic monitoring array; remote geotechnical engineer on-call; production quota due by end of week rather than end of shift.",
      "constraints": [
        "Production quota due by end of week, giving more scheduling flexibility than a same-shift deadline",
        "Limited real-time geotechnical staff presence (engineer off-site, reachable by radio/phone only)",
        "Ground Control Management Plan (GCMP) specifies rate-of-change and event-count thresholds for escalation, not just absolute readings",
        "Two-month-old widely publicized rockburst at a sister operation still fresh in workforce/industry consciousness",
        "Shift-change occurring mid-incident, creating handover risk",
        "Time pressure at each decision point remains present (minutes-scale operational urgency) even though the overall production deadline is less acute"
      ],
      "stakeholders": [
        "Health & Safety Officer (HSO, protagonist)",
        "Veteran shift supervisor (22 years underground experience)",
        "Remote geotechnical engineer (on-call)",
        "Mine manager (production accountability, now working to a weekly rather than shift target)",
        "Ventilation/monitoring technician",
        "Miners working in Stope 14-East"
      ],
      "technical_terms_to_use": [
        "back (roof)",
        "extensometer",
        "microseismic event count",
        "displacement rate",
        "Ground Control Management Plan (GCMP)",
        "stope",
        "spall",
        "hang-up",
        "escalation threshold",
        "ground support"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "availability",
        "narrative fallacy",
        "attribution error",
        "confirmation",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Verbal report at 06:40 from a miner of intermittent cracking/popping sounds in the back of Stope 14-East",
          "No automated alarm triggered yet from the microseismic array",
          "Two months earlier, a rockburst at a sister mine (same ore body region) caused significant disruption and was widely covered in trade press and internal safety bulletins",
          "Production schedule now allows the week (not the shift) to absorb any delay in Stope 14-East output"
        ],
        "new_information_after_decision": [
          "Instrument technician confirms no alarm state at time of report",
          "Mine manager asks for a general sense of timeline, not an immediate ETA, given the weekly target"
        ],
        "alternatives": [
          "Immediately evacuate and halt work in Stope 14-East pending full geotechnical assessment",
          "Allow continued work with enhanced monitoring and a designated escape route review",
          "Request only an instrument check before deciding, without restricting access"
        ],
        "intended_action": "HSO orders enhanced monitoring and limited access rather than full evacuation, treating the verbal report as a high-probability precursor to a rockburst-type event, drawing heavily on the vivid recent sister-mine incident rather than current instrument state; the relaxed weekly deadline reduces external pressure to resume full output quickly but does not change how the HSO weighs the sister-mine memory."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "05:00 baseline extensometer reading: 0.2mm displacement, logged as normal",
          "09:40 updated extensometer reading: 0.6mm displacement, a threefold increase over roughly 3 hours",
          "GCMP specifies escalation is triggered by displacement rate-of-change, not solely by absolute magnitude",
          "Ventilation technician confirms no other anomalies (gas, temperature) at this time"
        ],
        "new_information_after_decision": [
          "Microseismic technician reports event count for the shift is trending upward",
          "Mine manager notes the weekly target still leaves room to adjust the schedule if needed"
        ],
        "alternatives": [
          "Treat the displacement trend as within acceptable range relative to the morning baseline and continue normal operations",
          "Recalculate against the GCMP rate-of-change threshold and restrict access pending geotechnical sign-off",
          "Order immediate reinstallation of additional ground support before any further work"
        ],
        "intended_action": "HSO judges the 0.6mm reading as still 'normal' because it is compared against the initial 0.2mm baseline rather than evaluated against the GCMP's rate-of-change escalation threshold, and authorizes continued limited work; the reduced deadline pressure is present in the background but the comparison error stems from which reference point is used, not from urgency."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Veteran shift supervisor (22 years) recalls similar popping sounds from 2009 that resolved without incident and voices confidence the current situation is 'nothing'",
          "Microseismic event count has now reached 6 events/hour, at the GCMP's stated escalation flag of 5 events/hour",
          "A hairline crack (approx. 1mm width) was photographed and logged as insignificant the previous week in the same panel",
          "Geotechnical engineer has not yet called back"
        ],
        "new_information_after_decision": [
          "Engineer eventually calls back and requests the day's full event-count log",
          "A second, wider crack is noticed near the original hairline crack location"
        ],
        "alternatives": [
          "Follow the GCMP microseismic threshold and restrict the stope pending engineer review",
          "Defer to the supervisor's experiential read and permit continued limited access",
          "Split the difference: reduce crew size but keep the stope open"
        ],
        "intended_action": "HSO permits continued limited access, weighting the supervisor's tenure-based recollection of a past, unrelated event as strong evidence the current situation is benign, and separately evaluates today's crack photos against last week's 1mm reference rather than against the newly reached microseismic threshold; the weekly deadline gives no particular reason to rush this call, underscoring that the reasoning pattern is not solely a function of schedule pressure."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "A minor rock spall occurred in Stope 14-East at 13:15; no injuries, minor equipment damage",
          "Overnight temperature had dropped several degrees before the shift",
          "Shift change occurred approximately 90 minutes before the spall",
          "Blasting in an adjacent panel had occurred the previous week",
          "GCMP escalation protocol required a documented engineer sign-off before continued access after the 6 events/hour flag, which had not been completed"
        ],
        "new_information_after_decision": [
          "Incident report is submitted to the mine manager and regulator liaison",
          "Geotechnical engineer's later analysis notes multiple plausible contributing factors, none confirmed as dominant"
        ],
        "alternatives": [
          "Report the spall as resulting from a specific, well-defined causal chain (temperature drop plus shift-change vigilance lapse plus prior blasting)",
          "Report the event as multifactorial with several unresolved contributing conditions",
          "Attribute the escalation primarily to systemic gaps in escalation follow-through rather than to any single factor or individual"
        ],
        "intended_action": "HSO writes an incident narrative that links the temperature drop, shift change, and prior blasting into a single coherent causal story, and assigns primary responsibility for the escalation to the on-shift miner's delayed reporting rather than to the unresolved GCMP sign-off gap; the relaxed weekly quota removes any incentive to minimize the event for scheduling reasons, isolating the reasoning pattern from production-pressure explanations."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were doing when you first heard about the noise in Stope 14-East.",
        "What was your overall objective during this shift, given where the week's production stood?"
      ],
      "timeline_reconstruction": [
        "What happened right after the 06:40 report came in?",
        "What did the extensometer readings show at each check, and when did you see them?",
        "When did you speak with the shift supervisor, and what did that conversation cover?",
        "Walk me through what happened between the 09:40 reading and the spall at 13:15."
      ],
      "decision_point_probes": [
        "At 06:40, what information sources did you weigh, and how did you weigh them against each other?",
        "What alternatives did you consider before deciding on enhanced monitoring instead of evacuation?",
        "When you compared the 09:40 reading to the morning baseline, what made you conclude it was still acceptable?",
        "What information, if it had been available at that point, would have changed your call on the 09:40 reading?",
        "How did the supervisor's comments from 2009 factor into your access decision?",
        "How did you compare today's crack photos to last week's reading, and why?",
        "What alternatives to permitting continued access did you consider at that point?",
        "In writing the incident report, how did you decide which factors to include as causes?",
        "How did you decide where responsibility for the escalation belonged?"
      ],
      "closing_hypotheticals": [
        "If the sister-mine rockburst two months ago had never happened, do you think your first decision would have been different?",
        "If the GCMP's rate-of-change threshold had been displayed automatically alongside the raw reading, would your second decision have changed?",
        "If a less experienced supervisor had made the same comment, would you have weighted it the same way?",
        "Given that the tonnage target that week wasn't due until the end of the week rather than that same shift, do you think that changed how you approached any of these calls?",
        "How confident are you, in hindsight, that the causes you listed in the report are the real causes?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cf_av_01",
        "bias": "Availability Bias",
        "decision_point": 1,
        "mechanism": "Ease of recall of a vivid, recent, widely publicized rockburst at a sister mine inflates perceived likelihood/severity of the current ambiguous auditory report, independent of current instrument data and independent of the relaxed production deadline.",
        "affected_reasoning_operation": "Risk-likelihood estimation from an initial verbal cue",
        "evidence_available_at_time": [
          "Verbal report of intermittent cracking sounds",
          "No active alarm state",
          "Recollection of the sister-mine rockburst two months prior"
        ],
        "required_textual_manifestation": "HSO explicitly references the sister-mine event as the reason the noise felt urgent, disproportionate to what current instrumentation indicated, while noting the schedule itself was not the source of that urgency.",
        "plausible_nonbias_interpretation": "A cautious safety officer reasonably erring toward caution given any recent industry incident, regardless of recall vividness or schedule slack.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability", "recall", "vividness", "bias"]
      },
      {
        "instance_id": "cf_exp_01",
        "bias": "Experience Bias",
        "decision_point": 3,
        "mechanism": "Overweighting the supervisor's general tenure/seniority as validating evidence, without verifying that the supervisor's 2009 recollection actually shares the relevant geological or instrumentation conditions with today's situation.",
        "affected_reasoning_operation": "Credibility weighting of an informal expert opinion versus current threshold data",
        "evidence_available_at_time": [
          "Supervisor's verbal recollection of a 2009 event",
          "Current microseismic event count at the GCMP flag threshold",
          "No documented similarity check between 2009 conditions and today's panel"
        ],
        "required_textual_manifestation": "HSO cites the supervisor's years of experience as the primary reason for trusting the 'it's nothing' assessment, without probing whether the 2009 case matches today's specific conditions.",
        "plausible_nonbias_interpretation": "Reasonably valuing frontline tacit knowledge as one legitimate input among several.",
        "strength": "subtle",
        "do_not_make_explicit": ["experience bias", "seniority heuristic", "bias"]
      },
      {
        "instance_id": "cf_anc_01",
        "bias": "Anchoring Bias",
        "decision_point": 2,
        "mechanism": "The initial 05:00 baseline extensometer reading serves as a reference point against which the later reading is judged 'still normal,' rather than applying the GCMP's rate-of-change threshold; this comparison error is unaffected by whether the quota deadline is same-shift or end-of-week.",
        "affected_reasoning_operation": "Comparative evaluation of updated instrument data against a fixed initial reference",
        "evidence_available_at_time": [
          "05:00 baseline reading (0.2mm)",
          "09:40 updated reading (0.6mm)",
          "GCMP rate-of-change escalation criterion"
        ],
        "required_textual_manifestation": "HSO frames the 0.6mm reading relative to the 0.2mm baseline ('still low compared to this morning') instead of relative to the rate-of-change rule.",
        "plausible_nonbias_interpretation": "A reasonable simplification when a formal rate-of-change calculation is not immediately at hand.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "reference point", "bias"]
      },
      {
        "instance_id": "cf_anc_02",
        "bias": "Anchoring Bias",
        "decision_point": 3,
        "mechanism": "The prior week's 1mm hairline crack photograph serves as the reference point for judging today's crack severity, displacing attention from the newly reached microseismic event-count threshold, a distinct evidence source and reasoning moment from cf_anc_01's instrument-baseline anchor.",
        "affected_reasoning_operation": "Visual/photographic comparison of crack evidence against a prior fixed reference rather than integrating a separate concurrent data stream",
        "evidence_available_at_time": [
          "Photograph and log entry of last week's 1mm hairline crack, deemed insignificant",
          "Today's crack photos",
          "Microseismic event count reaching the 5 events/hour flag (now at 6)"
        ],
        "required_textual_manifestation": "HSO explicitly compares today's crack to last week's photo ('about the same as what we saw before') rather than cross-referencing the microseismic threshold that had just been reached.",
        "plausible_nonbias_interpretation": "Using recent, directly comparable visual history as a reasonable check when photographic baselines are readily available.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "reference photo", "bias"]
      },
      {
        "instance_id": "cf_narr_01",
        "bias": "Narrative Fallacy",
        "decision_point": 4,
        "mechanism": "Post-hoc construction of a single coherent causal chain (temperature drop, shift change, prior blasting) that feels satisfying and complete, overstating the certainty of causal linkage among factors whose individual contribution is unverified; the relaxed deadline removes any scheduling motive for the tidy story, isolating this pattern as evidence-processing rather than expedience.",
        "affected_reasoning_operation": "Causal reconstruction and incident narrative-writing after the outcome is known",
        "evidence_available_at_time": [
          "Overnight temperature drop",
          "Shift-change timing",
          "Prior week's blasting in an adjacent panel",
          "Engineer's later note that multiple factors are plausible but none confirmed dominant"
        ],
        "required_textual_manifestation": "HSO's report presents the three factors as a tidy, sequential explanation of 'why it happened,' with confident causal language despite unresolved uncertainty.",
        "plausible_nonbias_interpretation": "A reasonable attempt to summarize a complex event for a report audience that expects a clear explanation.",
        "strength": "subtle",
        "do_not_make_explicit": ["narrative fallacy", "coherence", "storytelling", "bias"]
      },
      {
        "instance_id": "cf_attr_01",
        "bias": "Attribution Bias",
        "decision_point": 4,
        "mechanism": "Primary responsibility for the escalation is assigned to the on-shift miner's individual delay in reporting, rather than to the systemic gap of the missing GCMP-required engineer sign-off after the event-count flag was reached; again independent of deadline pressure since no production motive to protect a shift target exists here.",
        "affected_reasoning_operation": "Causal attribution of responsibility between individual actor and systemic/process factors",
        "evidence_available_at_time": [
          "Miner's reporting timeline",
          "GCMP requirement for engineer sign-off after reaching the 6 events/hour flag, which was not completed",
          "Shift-change handover timing"
        ],
        "required_textual_manifestation": "HSO's report language centers on the miner 'should have flagged it sooner' as the leading explanation, while treating the missing sign-off step as a secondary or procedural footnote.",
        "plausible_nonbias_interpretation": "Individual vigilance genuinely is one legitimate contributing factor worth noting in any incident report.",
        "strength": "subtle",
        "do_not_make_explicit": ["attribution bias", "fundamental attribution", "systemic vs individual", "bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "MU_Biased_6",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a counterfactual variant, not a vocabulary_control or ambiguous_control."
    },
    "counterfactual_specification": {
      "causal_variable": "Timing/urgency of the production quota deadline",
      "original_state": "Tonnage from Stope 14-East is due by the end of the current dayshift, creating acute same-day scheduling pressure on the mine manager and, indirectly, on the HSO.",
      "counterfactual_state": "Tonnage from Stope 14-East is due by the end of the week, giving materially more scheduling slack; the mine manager no longer requires a same-day ETA on resuming full production.",
      "variables_to_hold_constant": [
        "All instrument readings (extensometer baseline and update, microseismic event counts)",
        "The sister-mine rockburst memory and its timing (two months prior)",
        "The supervisor's tenure, his 2009 recollection, and the wording of his reassurance",
        "The hairline crack photograph and today's crack photos",
        "The spall event (13:15, no injuries, minor equipment damage)",
        "The shift-change timing and the adjacent-panel blasting the prior week",
        "The GCMP thresholds and the missing engineer sign-off",
        "The four decision points and their alternatives",
        "The six planned bias instances and their mechanisms"
      ],
      "expected_causal_difference": "With reduced same-day production urgency, any explanation of the HSO's decisions that relies on schedule pressure as the driver becomes less available, making it clearer that the same reasoning patterns (reliance on a vivid recent memory, comparison to an initial baseline instead of a rate rule, deference to seniority, tidy post-hoc storytelling, and individual-focused attribution) persist even without acute deadline pressure.",
      "causal_test_question": "Did reducing the production deadline's urgency change the pattern or degree of the HSO's reasoning at each decision point, or did the same evidence-processing patterns occur regardless of schedule pressure?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points, each with at least two plausible alternatives.",
      "Confirm exactly 6 total bias instances embedded, matching MU_Biased_6's manifest: 1 Availability, 1 Experience, 2 Anchoring (distinct decision points 2 and 3, distinct evidence sources), 1 Narrative Fallacy, 1 Attribution.",
      "Confirm only the production-deadline variable differs materially from MU_Biased_6; all instrument readings, memories, conversations, and the spall event are held constant.",
      "Confirm no bias terminology, labels, or psychological explanations appear in probe language or intended answers.",
      "Confirm each instance has a plausible non-bias interpretation available to the validator.",
      "Confirm the two Anchoring instances use different evidence sources (extensometer baseline vs. crack photograph) and different decision points.",
      "Confirm interview draft target is 1,350 words (acceptable range 1,215-1,485) and can be reached without repeating bias-relevant content across probes.",
      "Confirm consequences (minor spall, no injuries) do not mechanically prove any decision was biased.",
      "Confirm at least one probe asks what information would have changed a decision and one probe asks about a hypothetical change to a key feature (the deadline variable)."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to recall of the specific sister-mine rockburst, not a generic caution statement, and must be independent of the deadline variable." },
      { "bias": "Experience Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to overweighting supervisor tenure without verifying situational similarity." },
      { "bias": "Anchoring Bias", "occurrences": 2, "mechanism_constraint": "Each instance must reference a distinct evidence source (instrument baseline reading vs. crack photograph) at a distinct decision point." },
      { "bias": "Narrative Fallacy", "occurrences": 1, "mechanism_constraint": "Must occur only in the post-event causal explanation, not in earlier probes." },
      { "bias": "Attribution Bias", "occurrences": 1, "mechanism_constraint": "Must contrast individual worker blame against an identifiable systemic/process factor." }
    ],
    "target_bias_names": [
      "Availability Bias",
      "Experience Bias",
      "Anchoring Bias",
      "Narrative Fallacy",
      "Attribution Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Availability Bias", "requested_occurrences": 1 },
      { "bias": "Experience Bias", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 2 },
      { "bias": "Narrative Fallacy", "requested_occurrences": 1 },
      { "bias": "Attribution Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cf_av_01", "bias": "Availability Bias" },
      { "instance_id": "cf_exp_01", "bias": "Experience Bias" },
      { "instance_id": "cf_anc_01", "bias": "Anchoring Bias" },
      { "instance_id": "cf_anc_02", "bias": "Anchoring Bias" },
      { "instance_id": "cf_narr_01", "bias": "Narrative Fallacy" },
      { "instance_id": "cf_attr_01", "bias": "Attribution Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cf_av_01", "bias": "Availability Bias", "decision_point": 1 },
      { "instance_id": "cf_anc_01", "bias": "Anchoring Bias", "decision_point": 2 },
      { "instance_id": "cf_exp_01", "bias": "Experience Bias", "decision_point": 3 },
      { "instance_id": "cf_anc_02", "bias": "Anchoring Bias", "decision_point": 3 },
      { "instance_id": "cf_narr_01", "bias": "Narrative Fallacy", "decision_point": 4 },
      { "instance_id": "cf_attr_01", "bias": "Attribution Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cf_av_01",
        "bias": "Availability Bias",
        "mechanism": "Vivid recall of the recent sister-mine rockburst inflates the perceived likelihood of the current ambiguous noise report, independent of deadline urgency.",
        "affected_reasoning_operation": "Risk-likelihood estimation from a verbal cue",
        "evidence_source": "Memory of a widely publicized recent industry incident",
        "distinctiveness_requirement": "Occurs only at decision point 1, tied specifically to the sister-mine memory, not repeated later."
      },
      {
        "instance_id": "cf_anc_01",
        "bias": "Anchoring Bias",
        "mechanism": "Morning baseline extensometer reading anchors judgment of the later reading as 'still normal' instead of applying the rate-of-change rule.",
        "affected_reasoning_operation": "Comparative evaluation of updated instrument data against fixed initial reference",
        "evidence_source": "Extensometer displacement readings (05:00 baseline vs. 09:40 update)",
        "distinctiveness_requirement": "Uses instrument telemetry evidence at decision point 2; distinct from cf_anc_02's photographic evidence at decision point 3."
      },
      {
        "instance_id": "cf_exp_01",
        "bias": "Experience Bias",
        "mechanism": "Supervisor's tenure is treated as sufficient validation of a benign read, without checking situational similarity to today's conditions.",
        "affected_reasoning_operation": "Credibility weighting of informal expert opinion vs. threshold data",
        "evidence_source": "Supervisor's verbal recollection of a 2009 event",
        "distinctiveness_requirement": "Occurs only at decision point 3, distinct reasoning operation (credibility weighting) from cf_anc_02's evidence comparison at the same decision point."
      },
      {
        "instance_id": "cf_anc_02",
        "bias": "Anchoring Bias",
        "mechanism": "Prior week's photographed hairline crack anchors judgment of today's crack severity, displacing attention from the newly reached microseismic threshold.",
        "affected_reasoning_operation": "Visual/photographic comparison against a prior fixed reference",
        "evidence_source": "Crack-width photographs (last week vs. today)",
        "distinctiveness_requirement": "Uses photographic evidence at decision point 3; distinct evidence type and moment from cf_anc_01's instrument-baseline anchor at decision point 2."
      },
      {
        "instance_id": "cf_narr_01",
        "bias": "Narrative Fallacy",
        "mechanism": "Multiple loosely-related factors are woven into a single tidy causal chain in the post-event report, overstating certainty of the causal linkage, regardless of deadline pressure.",
        "affected_reasoning_operation": "Post-hoc causal reconstruction for incident reporting",
        "evidence_source": "Temperature log, shift-change timing, prior blasting record",
        "distinctiveness_requirement": "Occurs only in the decision point 4 incident narrative, not in earlier probes or hypotheticals."
      },
      {
        "instance_id": "cf_attr_01",
        "bias": "Attribution Bias",
        "mechanism": "Escalation responsibility is assigned mainly to the on-shift miner's reporting delay rather than to the missing systemic GCMP sign-off step.",
        "affected_reasoning_operation": "Causal attribution of responsibility between individual and systemic factors",
        "evidence_source": "Miner reporting timeline vs. GCMP sign-off requirement",
        "distinctiveness_requirement": "Occurs only in the decision point 4 responsibility assessment, distinct reasoning operation from cf_narr_01's causal-chain construction at the same decision point."
      }
    ],
    "intended_strength": [
      { "instance_id": "cf_av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "cf_exp_01", "bias": "Experience Bias", "strength": "subtle" },
      { "instance_id": "cf_anc_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cf_anc_02", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cf_narr_01", "bias": "Narrative Fallacy", "strength": "subtle" },
      { "instance_id": "cf_attr_01", "bias": "Attribution Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": "MU_Biased_6",
    "counterfactual_variable": {
      "name": "Timing/urgency of the production quota deadline",
      "original_state": "Tonnage from Stope 14-East due by end of the current dayshift (acute same-day pressure)",
      "changed_state": "Tonnage from Stope 14-East due by end of the week (relaxed schedule slack)",
      "variables_to_hold_constant": [
        "Instrument readings (extensometer baseline/update, microseismic counts)",
        "Sister-mine rockburst memory and timing",
        "Supervisor's tenure, 2009 recollection, and reassurance wording",
        "Hairline crack photograph and today's crack photos",
        "Spall event details (time, no injuries, equipment damage)",
        "Shift-change timing and prior-week blasting",
        "GCMP thresholds and the missing engineer sign-off",
        "The four decision points, their alternatives, and the six planned bias instances"
      ]
    },
    "scenario_id": "MU_Counterfactual_6",
    "domain_id": "MU",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrence allocation mirrors the paired biased scenario (MU_Biased_6) exactly in decision-point placement and mechanism, since the manifest and CTA structure are held constant under the counterfactual condition: Availability Bias at DP1 (sister-mine recall), Anchoring Bias split across DP2 (instrument baseline) and DP3 (photographic reference) using distinct evidence sources, Experience Bias at DP3 alongside but reasoning-operation-distinct from the second Anchoring instance, and Narrative Fallacy plus Attribution Bias both at DP4 but targeting different reasoning operations. The only altered element is the production-deadline causal variable, which does not itself drive any bias mechanism and is deliberately kept orthogonal to all six instances so the counterfactual isolates the deadline's causal effect on outcome/framing rather than on reasoning-pattern presence.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Instrument readings (extensometer baseline/update, microseismic counts)",
      "Sister-mine rockburst memory and timing",
      "Supervisor's tenure, 2009 recollection, and reassurance wording",
      "Hairline crack photograph and today's crack photos",
      "Spall event details (time, no injuries, equipment damage)",
      "Shift-change timing and prior-week blasting",
      "GCMP thresholds and the missing engineer sign-off",
      "The four decision points, their alternatives, and the six planned bias instances"
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
        "segment_type": "initial risk assessment and access decision",
        "raw_interview_anchor": "Around 06:40 ... my first thought went straight to the rockburst at our sister operation two months back ... I treated the report as more likely to be heading toward something serious ... I went with enhanced monitoring and limited access.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cf_av_01"
        ],
        "ground_truth_rationale": "The elevated initial risk judgment is explicitly linked to recall of the vivid recent sister-mine rockburst despite no current alarm."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "instrument-reading interpretation and threshold judgment",
        "raw_interview_anchor": "The 05:00 baseline was 0.2mm ... By 09:40 it had moved to 0.6mm ... compared to this morning, it's still a small number ... I didn't go back to the GCMP's rate-of-change table.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cf_anc_01"
        ],
        "ground_truth_rationale": "The participant explains the comparison rule used to judge the updated extensometer reading and acknowledges that the rate criterion was not applied."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "supervisor credibility weighting and access decision",
        "raw_interview_anchor": "He mentioned hearing similar popping back in 2009 ... His track record carried a lot of weight for me in that moment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cf_exp_01"
        ],
        "ground_truth_rationale": "Supervisor tenure and reassurance are given substantial weight without checking whether the historical comparison fits current conditions."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "crack comparison and visual evidence interpretation",
        "raw_interview_anchor": "Today's crack looked about the same width to me ... I read it as consistent with what we already knew was fine ... I was judging the crack against the old photo instead of against the newer number.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cf_anc_02"
        ],
        "ground_truth_rationale": "The prior crack photograph and classification are used as the reference while the new seismic threshold is not integrated."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "post-event causal reconstruction",
        "raw_interview_anchor": "Putting it together ... it read as a pretty clean explanation: cooling stress plus the handover timing plus residual vibration from that blast.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cf_narr_01"
        ],
        "ground_truth_rationale": "Several plausible factors are presented as one clean causal explanation despite no factor being confirmed as dominant."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "responsibility attribution",
        "raw_interview_anchor": "I focused mainly on the miner who first reported the sounds ... I did mention the missing engineer sign-off ... but it came across more as a process note than a central cause.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cf_attr_01"
        ],
        "ground_truth_rationale": "Responsibility is centered on the individual miner while the missing GCMP engineer sign-off is secondary."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "retrospective confidence assessment",
        "raw_interview_anchor": "Less than when I wrote it. It felt like a complete picture at the time, but there were threads I didn't fully chase down.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive confidence judgment but does not express another hidden bias mechanism."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analyzed the interview transcript as self-contained evidence. No retrieved corpus passages were supplied, so labels and definitions rest on general cognitive-science knowledge; no corpus citations are included."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "fundamental attribution error",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "hindsight bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging probability or seriousness by how easily a vivid or salient similar instance comes to mind, rather than by all relevant objective indicators.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial response to 06:40 cracking report in Stope 14-East",
      "decision_point_description": "Whether to treat the reported cracking as likely serious after no microseismic alarm, and what initial access and monitoring control to apply.",
      "affected_reasoning_operation": "Probability and seriousness assessment leading to initial safety-control selection",
      "bias_specific_mechanism": "The vivid, recent sister-operation rockburst was mentally available and salient, so the participant over-weighted it when judging the current cracking as likely to become serious even though current local instruments were not yet flagging.",
      "manifestation_in_interview": "The participant spontaneously linked the noise report to the sister-mine rockburst, said the memory was vivid and carried a lot of weight, and chose enhanced monitoring with limited access rather than waiting for the instrument check.",
      "effect_on_reasoning_or_decision": "It shifted the initial response toward enhanced monitoring and limited access based on a dramatic available memory rather than on the current objective microseismic data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "my first thought went straight to the rockburst at our sister operation two months back — that made the trade press, and it was still something everyone on site talked about. The conditions weren't identical, but same ore body region, and it was vivid enough that I treated the report as more likely to be heading toward something serious than the instruments alone would have suggested.",
          "evidence_explanation": "This explicitly states that a vivid, easily recalled prior rockburst raised the participant's subjective likelihood judgment above what current objective instruments suggested, which is the availability mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The instruments weren't flagging anything, but that sister-mine memory carried a lot of weight for me regardless of what the schedule looked like that day.",
          "evidence_explanation": "This shows the available memory outweighed current instrument evidence during the initial safety decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without that fresh in mind, I think I'd have waited on the instrument tech's check before doing anything.",
          "evidence_explanation": "The participant's own counterfactual confirms that the salient memory, not the objective current data alone, changed the initial response."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction is reported. The possible competing explanation of schedule pressure is explicitly denied by the participant.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism reflect general cognitive-science knowledge rather than retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and insufficient adjustment",
        "anchoring effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient adjustment from a salient initial numerical value when making a later judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of 09:40 extensometer movement from 0.2mm to 0.6mm",
      "decision_point_description": "Whether the observed extensometer change warranted escalation under the GCMP rate-of-change criterion.",
      "affected_reasoning_operation": "Magnitude and risk judgment from numerical trend data",
      "bias_specific_mechanism": "The 05:00 baseline reading of 0.2mm served as a mental reference point, and the participant judged the 0.6mm value mainly against that initial small number rather than applying the rate-of-change standard, producing insufficient adjustment from the anchor.",
      "manifestation_in_interview": "The participant described 0.6mm as still a small number compared with the morning, did not consult the GCMP rate-of-change table, and later stated that he used the wrong reference.",
      "effect_on_reasoning_or_decision": "He did not escalate based on the actual speed of movement because the anchored comparison made the change feel less significant than the plan required it to be judged.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "By 09:40 it had moved to 0.6mm — three times the baseline in about three hours. I looked at that and thought, well, compared to this morning, it's still a small number.",
          "evidence_explanation": "This explicitly shows the participant using the morning baseline as the comparison point and judging the new reading as small relative to that anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go back to the GCMP's rate-of-change table, which is actually how you're supposed to judge it — the plan cares about the speed of movement, not just where it sits against an earlier point. Looking back, I was using the wrong reference.",
          "evidence_explanation": "This demonstrates that the appropriate standard was rate of change, but the participant instead used an earlier point as the reference, consistent with anchoring and insufficient adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the rate-of-change figure had been sitting right next to the raw number, I think I'd have caught it. As it was, all I had was two numbers from two different times, and comparing them felt natural.",
          "evidence_explanation": "This supports the mechanism by showing that comparing two time-specific numbers felt natural and displaced the rate-of-change judgment."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction occurred. A possible competing explanation is that the rate-of-change figure was not displayed alongside the raw value, but the participant knew the GCMP table existed and still used the baseline comparison.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism reflect general cognitive-science knowledge rather than retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "authority bias",
      "alternative_labels": [
        "expertise bias",
        "appeal to authority"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Over-weighting a source's opinion or information because of perceived authority or expertise while under-examining the substantive match of the evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Conversation with shift supervisor about the 2009 popping history and continued limited access",
      "decision_point_description": "Whether to follow the seismic threshold strictly and hold the stope, reduce crew size, or trust the supervisor's experience and continue with limited crew.",
      "affected_reasoning_operation": "Evaluation of supervisor advice and subsequent access decision",
      "bias_specific_mechanism": "The supervisor's decades of underground experience and track record functioned as an authority or expertise cue, leading the participant to accept the 2009 analogy and choose limited access without examining whether the 2009 case matched current rock type or blast pattern.",
      "manifestation_in_interview": "The participant explicitly said the supervisor's track record carried a lot of weight and that he did not push on whether the 2009 case matched current conditions.",
      "effect_on_reasoning_or_decision": "The access decision relied substantially on the supervisor's confident read rather than on the microseismic flag threshold, resulting in continued limited access.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He mentioned hearing similar popping back in 2009 that came to nothing, and he was confident this was the same kind of thing. Around then the microseismic count for the shift had actually climbed to six events an hour, just over our flag threshold of five. I didn't really push on whether the 2009 case matched today's rock type or blast pattern.",
          "evidence_explanation": "This shows the participant accepted an experienced supervisor's analogy despite an objective threshold crossing and without testing the analogy's relevance."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "His track record carried a lot of weight for me in that moment.",
          "evidence_explanation": "This explicitly attributes the influence to the supervisor's track record rather than the substance of the comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, I don't think so. His years underground were a big part of why I trusted the read.",
          "evidence_explanation": "The participant confirms that the supervisor's experience, rather than the quality of the evidence, was a major reason for trust."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction is reported. The microseismic count had crossed the flag threshold, which was a disconfirming signal that did not override the authority-based trust.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism reflect general cognitive-science knowledge rather than retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "selective information processing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Interpreting or favoring information in a way that confirms an existing belief or expectation while not integrating contradictory information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of hairline crack against prior photograph and continued access decision",
      "decision_point_description": "Whether the visible crack was still consistent with the prior 'insignificant' assessment or should be re-evaluated in light of the newly crossed seismic threshold.",
      "affected_reasoning_operation": "Diagnostic interpretation of crack evidence and integration with seismic threshold information",
      "bias_specific_mechanism": "The participant held a pre-existing 'insignificant' assessment from the prior week's photograph, interpreted the current crack as consistent with that assessment because it looked similar, and failed to connect it to the newly crossed microseismic threshold.",
      "manifestation_in_interview": "The participant reported reading the crack as consistent with what was already known to be fine and judging it against the old photo instead of against the newer seismic number.",
      "effect_on_reasoning_or_decision": "The participant continued limited access partly based on the crack photograph, without re-evaluating the crack in the context of the crossing microseismic flag.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a hairline crack, about a millimeter, photographed and logged the week before as insignificant. Today's crack looked about the same width to me, so I read it as consistent with what we already knew was fine. What I didn't do was connect it to the seismic count that had just crossed the threshold — I was judging the crack against the old photo instead of against the newer number.",
          "evidence_explanation": "This explicitly shows the participant interpreting new crack evidence as confirming a prior 'insignificant' label and not integrating the contradictory seismic-threshold information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Follow the seismic threshold strictly and hold the stope for engineer sign-off, reduce crew size as a middle path, or trust the supervisor's read and continue with limited crew. I went with limited access, mostly on his confidence and my own read of the crack photo.",
          "evidence_explanation": "This shows the crack interpretation contributed to the decision to continue limited access rather than following the stricter seismic threshold."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction is reported. The participant retrospectively described what he did not do, but this recognition came after the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism reflect general cognitive-science knowledge rather than retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect",
        "retrospective determinism"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "After an outcome is known, overestimating the clarity or predictability of its causes, or constructing a post hoc causal account as more certain than the evidence supports.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Incident report causal explanation after the minor spall",
      "decision_point_description": "Selecting the primary causes to put forward in the formal incident report after the 13:15 spall.",
      "affected_reasoning_operation": "Post-event causal attribution and confidence in the causal account",
      "bias_specific_mechanism": "Knowing that the spall occurred, the participant assembled several plausible antecedents into a 'clean explanation' and presented that account with greater causal certainty than the available evidence could support; the engineer later noted several factors were plausible and none could be confirmed as dominant.",
      "manifestation_in_interview": "The participant stated that the causes read as a pretty clean explanation and that the report felt like a complete picture at the time, despite later acknowledging unchased threads.",
      "effect_on_reasoning_or_decision": "The incident report advanced a particular causal narrative as central, potentially underweighting uncertainty and alternative factors.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Putting it together — the overnight temperature drop, the shift change not long before, and the blasting in the next panel the previous week — it read as a pretty clean explanation: cooling stress plus the handover timing plus residual vibration from that blast. That's what I put forward as the account, even though the engineer's later note said several factors were plausible and none could be confirmed as dominant.",
          "evidence_explanation": "This shows the participant formed a coherent post-event causal account and reported it as more definitive than the engineer's subsequent uncertainty supported."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Less than when I wrote it. It felt like a complete picture at the time, but there were threads I didn't fully chase down.",
          "evidence_explanation": "This demonstrates that outcome knowledge contributed to an inflated feeling of completeness in the causal report at the time."
        }
      ],
      "correction_or_counterevidence": "The engineer's note that several factors were plausible and none could be confirmed as dominant is present as counterevidence, and the participant now reports lower confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism reflect general cognitive-science knowledge rather than retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "fundamental attribution error",
      "alternative_labels": [
        "correspondence bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Over-attributing another person's behavior to dispositional factors while underweighting situational or systemic constraints.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Responsibility framing in incident report",
      "decision_point_description": "How to assign primary responsibility for the delayed recognition of worsening conditions.",
      "affected_reasoning_operation": "Causal attribution of responsibility and blame",
      "bias_specific_mechanism": "The participant centered responsibility on the miner's failure to report popping a second time, a dispositional or behavioral attribution, while treating the missing engineer sign-off after the six-events threshold as a secondary process note rather than a central systemic failure.",
      "manifestation_in_interview": "The participant said he focused mainly on the miner and felt a second call might have caught it sooner; the missing engineer sign-off was mentioned but not framed as a central cause.",
      "effect_on_reasoning_or_decision": "The incident report may have assigned blame to an individual rather than reflecting the systemic safety-control breakdown, potentially shaping post-event corrective action.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I focused mainly on the miner who first reported the sounds and didn't flag it again once the popping continued — I felt if he'd called it in a second time, we might have caught it sooner. I did mention the missing engineer sign-off after the six-events flag, but it came across more as a process note than a central cause.",
          "evidence_explanation": "This shows a dispositional attribution to the miner while the systemic missing sign-off is minimized, which is the core pattern of fundamental attribution error."
        }
      ],
      "correction_or_counterevidence": "The participant did mention the missing engineer sign-off, indicating partial awareness of a situational factor, but he explicitly framed it as secondary rather than central.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism reflect general cognitive-science knowledge rather than retrieved corpus support.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided for this analysis, so all bias labels and definitions rely on general cognitive-science knowledge rather than retrieval-grounded support.",
    "The interview is a single-participant retrospective self-report, so cognitive mechanisms are inferred from the participant's descriptions rather than from direct observation of real-time cognition.",
    "Because corpus support is unavailable, all corpus_evidence arrays are empty and source metadata are not provided."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Counterfactual_6_Sonnet_off",
  "interview_id": "MU_Counterfactual_6",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
