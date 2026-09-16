You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. As we discussed, this is a debrief to understand your reasoning during the Stope 14-East incident, not an audit of the outcome. Everything you share helps us understand how decisions get made in the field. You're comfortable proceeding?

Participant: Yeah, that's fine. I've done these debriefs before after other events. Happy to walk through it.

Interviewer: Great. Can you first tell me a bit about your role and what your objective was that shift?

Participant: I'm the Health and Safety Officer for the site, dayshift. My main job that day was routine — checks, permits, and keeping an eye on the ground conditions in the active stopes, including 14-East, which was mid-cycle in a longhole stope. We were also under a bit of pressure to hit weekly tonnage, so there was always that background tension between keeping things moving and not cutting corners.

Interviewer: Walk me through what happened when you first got word of the noise.

Participant: Around 06:40 one of the miners came up on radio saying he'd heard some cracking, almost like popping, in the back of 14-East. Intermittent, not constant. No alarm had gone off on the microseismic array at that point. Normally that would make me lean toward "let's just check it," but honestly, my mind went straight to what happened at our sister operation two months earlier — that rockburst that made the trade press and had everyone in the region talking. It wasn't identical conditions, but it was the same ore body region, and that event was still very much front of mind for the whole crew. So even without an alarm, I treated that report as something that could be heading toward a similar event, more than I think the instrument data alone would have justified.

Interviewer: What alternatives did you weigh at that point?

Participant: There were really three options — full evacuation and stop work pending a geotech look, allow work to continue with tighter monitoring and a reviewed escape route, or just get the instrument tech to check readings first without restricting anyone. I went with the middle option: enhanced monitoring, limited access, no full evacuation. Partly because the instruments weren't flagging anything, but I'll admit the sister-mine incident weighed heavily on how urgent it felt to me in the moment.

Interviewer: Let's move to later that morning — the extensometer readings.

Participant: Right, so the 05:00 baseline was 0.2mm, which is our normal quiet reading. At 09:40 the tech radioed that it had moved to 0.6mm. That's three times the baseline in about three hours. I looked at it and thought, well, compared to this morning it's still a small number, still sub-millimeter, nothing dramatic. I didn't go back and check it against the rate-of-change table in the GCMP, which is actually the correct way to assess it — that plan cares about how fast it's moving, not just where it sits relative to where it started. In hindsight I was comparing it to the wrong reference.

Interviewer: What made the baseline feel like the right comparison at the time?

Participant: It's just naturally what you have in front of you — you saw it at 0.2 that morning, now it's 0.6, and 0.6 still sounds low in absolute terms. Ventilation had nothing unusual either, no gas, no temperature anomaly, so there was nothing else pulling my attention toward the rate-of-change side of things.

Interviewer: Did anything else factor into that call?

Participant: The mine manager was also asking for a production ETA, so there was some pull to land on "we're fine" rather than dig deeper into the trend math right then.

Interviewer: Let's talk about the conversation with your shift supervisor.

Participant: That was maybe an hour later. He's got twenty-two years underground, most of it at this site. He mentioned he'd heard similar popping back in 2009, and it hadn't come to anything. He was pretty confident it was "nothing." Around that same time the microseismic count for the shift had actually climbed to six events an hour, which is right at — actually just over — the flag threshold in our plan. I didn't push hard on whether the 2009 case actually matched today's rock type, blast pattern, or depth. His track record is strong, so his read carried a lot of weight for me in that moment, maybe more than it should have on its own.

Interviewer: You also looked at a crack in the same panel. Can you describe that?

Participant: Yes — there was a hairline crack, about a millimeter wide, that had been photographed and logged the week before as insignificant. When I looked at today's crack, I compared it side-by-side with that old photo, and it looked about the same width to me, so I read it as "consistent with what we already know is fine." What I didn't do at that point was connect it back to the microseismic number that had just ticked over the threshold — I was judging the crack against the old photo rather than against the newer seismic data.

Interviewer: What alternatives did you consider before allowing continued access?

Participant: Follow the seismic threshold strictly and pull back until the engineer signed off, split the difference and reduce crew size, or trust the supervisor's read and keep going with limited crew. I went with limited access, mostly on the supervisor's confidence and my own read of that crack photo.

Interviewer: What happened next?

Participant: The engineer eventually called back wanting the full event log, and around then someone noticed a second, wider crack near the first one. Then at 13:15 we had a minor spall — no injuries, some equipment damage. Shift change had happened about ninety minutes before that.

Interviewer: When you wrote up the incident report, how did you decide what caused it?

Participant: Looking at everything together — the overnight temperature drop, the shift change happening not long before, and the blasting in the panel next door the prior week — it came together into a pretty clean story: cooling stresses plus the handover timing plus the residual vibration from that blast. It read as a coherent explanation, so that's what I put forward as the primary account, even though the engineer's later note said several factors were plausible and none could really be confirmed as the dominant cause.

Interviewer: And on responsibility — how did you frame that?

Participant: I focused mainly on the miner who first heard the sounds and didn't escalate again after the initial 06:40 report — I felt if he'd flagged it again once the popping continued, we might have caught it sooner. I did note the missing engineer sign-off after the six-events flag, but that came across more as a process footnote than as a central cause in the report.

Interviewer: If the sister-mine rockburst had never happened, do you think your first call would have gone differently?

Participant: Possibly. I think without that fresh in everyone's mind, I might have waited for the instrument tech's check before doing anything, rather than jumping to enhanced monitoring right away.

Interviewer: If the rate-of-change threshold had displayed automatically next to the raw reading, would the second decision have changed?

Participant: Probably, yeah. If it had flagged red rather than just showing a number, I don't think I'd have leaned on the morning comparison the way I did.

Interviewer: What would you tell a newer HSO to watch for in a similar shift?

Participant: To always check the plan's actual thresholds rather than trusting a gut comparison to whatever reading you saw earlier, and to weigh a senior person's read alongside the data, not instead of it.

Interviewer: Last one — how confident are you now that the causes you listed in the report are the real ones?

Participant: Honestly, less than I was when I wrote it. It felt tidy at the time, but there were a few threads I didn't fully chase down.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Biased_6",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Mine Safety/Health & Safety Officer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Strata Noise Escalation in Stope 14-East",
    "scenario_summary_internal": "A Health & Safety Officer (HSO) at an underground hard-rock mine responds to a report of intermittent cracking/popping noise in the back (roof) of Stope 14-East during dayshift. Over several hours the HSO must weigh verbal reports, instrument telemetry (extensometer displacement, microseismic event counts), a veteran supervisor's informal read of the situation, and a widely publicized rockburst at a sister mine two months earlier, against production pressure to keep the stope running. A minor rock spall (no injuries) occurs later in the shift, prompting a post-event review and incident report in which the HSO must explain the escalation and assign contributing causes.",
    "occupational_realism": {
      "objective": "Determine, at four successive points during the shift, whether Stope 14-East can safely continue production or must be restricted/evacuated, and afterward produce an accurate incident account of a minor rock-spall event.",
      "setting": "Underground hard-rock mine, approximately 900m depth, longhole stoping method, instrumented with extensometers and a microseismic monitoring array; remote geotechnical engineer on-call, production quota deadline mid-shift.",
      "constraints": [
        "Production quota pressure from mine manager to avoid unnecessary stoppages",
        "Limited real-time geotechnical staff presence (engineer off-site, reachable by radio/phone only)",
        "Ground Control Management Plan (GCMP) specifies rate-of-change and event-count thresholds for escalation, not just absolute readings",
        "Two-month-old widely publicized rockburst at a sister operation still fresh in workforce/industry consciousness",
        "Shift-change occurring mid-incident, creating handover risk",
        "Time pressure: decisions must be made within minutes of each new data point"
      ],
      "stakeholders": [
        "Health & Safety Officer (HSO, protagonist)",
        "Veteran shift supervisor (22 years underground experience)",
        "Remote geotechnical engineer (on-call)",
        "Mine manager (production accountability)",
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
          "Production schedule requires Stope 14-East output today to meet weekly quota"
        ],
        "new_information_after_decision": [
          "Instrument technician confirms no alarm state at time of report",
          "Mine manager asks for an ETA on resuming full production"
        ],
        "alternatives": [
          "Immediately evacuate and halt work in Stope 14-East pending full geotechnical assessment",
          "Allow continued work with enhanced monitoring and a designated escape route review",
          "Request only an instrument check before deciding, without restricting access"
        ],
        "intended_action": "HSO orders enhanced monitoring and limited access rather than full evacuation, treating the verbal report as a high-probability precursor to a rockburst-type event, drawing heavily on the vivid recent sister-mine incident rather than current instrument state."
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
          "Mine manager reiterates production timeline"
        ],
        "alternatives": [
          "Treat the displacement trend as within acceptable range relative to the morning baseline and continue normal operations",
          "Recalculate against the GCMP rate-of-change threshold and restrict access pending geotechnical sign-off",
          "Order immediate reinstallation of additional ground support before any further work"
        ],
        "intended_action": "HSO judges the 0.6mm reading as still 'normal' because it is compared against the initial 0.2mm baseline rather than evaluated against the GCMP's rate-of-change escalation threshold, and authorizes continued limited work."
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
        "intended_action": "HSO permits continued limited access, weighting the supervisor's tenure-based recollection of a past, unrelated event as strong evidence the current situation is benign, and separately evaluates today's crack photos against last week's 1mm reference rather than against the newly reached microseismic threshold."
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
        "intended_action": "HSO writes an incident narrative that links the temperature drop, shift change, and prior blasting into a single coherent causal story, and assigns primary responsibility for the escalation to the on-shift miner's delayed reporting rather than to the unresolved GCMP sign-off gap."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were doing when you first heard about the noise in Stope 14-East.",
        "What was your overall objective during this shift?"
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
        "Looking back, what would you tell a new HSO to watch for in a similar shift?",
        "How confident are you, in hindsight, that the causes you listed in the report are the real causes?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 1,
        "mechanism": "Ease of recall of a vivid, recent, widely publicized rockburst at a sister mine inflates perceived likelihood/severity of the current ambiguous auditory report, independent of current instrument data.",
        "affected_reasoning_operation": "Risk-likelihood estimation from an initial verbal cue",
        "evidence_available_at_time": [
          "Verbal report of intermittent cracking sounds",
          "No active alarm state",
          "Recollection of the sister-mine rockburst two months prior"
        ],
        "required_textual_manifestation": "HSO explicitly references the sister-mine event as the reason the noise felt urgent, disproportionate to what current instrumentation indicated.",
        "plausible_nonbias_interpretation": "A cautious safety officer reasonably erring toward caution given any recent industry incident, regardless of recall vividness.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability", "recall", "vividness", "bias"]
      },
      {
        "instance_id": "exp_01",
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
        "instance_id": "anc_01",
        "bias": "Anchoring Bias",
        "decision_point": 2,
        "mechanism": "The initial 05:00 baseline extensometer reading serves as a reference point against which the later reading is judged 'still normal,' rather than applying the GCMP's rate-of-change threshold.",
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
        "instance_id": "anc_02",
        "bias": "Anchoring Bias",
        "decision_point": 3,
        "mechanism": "The prior week's 1mm hairline crack photograph serves as the reference point for judging today's crack severity, displacing attention from the newly reached microseismic event-count threshold, a distinct evidence source and reasoning moment from anc_01's instrument-baseline anchor.",
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
        "instance_id": "narr_01",
        "bias": "Narrative Fallacy",
        "decision_point": 4,
        "mechanism": "Post-hoc construction of a single coherent causal chain (temperature drop, shift change, prior blasting) that feels satisfying and complete, overstating the certainty of causal linkage among factors whose individual contribution is unverified.",
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
        "instance_id": "attr_01",
        "bias": "Attribution Bias",
        "decision_point": 4,
        "mechanism": "Primary responsibility for the escalation is assigned to the on-shift miner's individual delay in reporting, rather than to the systemic gap of the missing GCMP-required engineer sign-off after the event-count flag was reached.",
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
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' with no paired control scenario supplied."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly 4 decision points, each with at least two plausible alternatives.",
      "Confirm exactly 6 total bias instances embedded: 1 Availability, 1 Experience, 2 Anchoring (at distinct decision points 2 and 3, distinct evidence sources), 1 Narrative Fallacy, 1 Attribution.",
      "Confirm no bias terminology, labels, or psychological explanations appear in probe language or intended answers.",
      "Confirm each instance has a plausible non-bias interpretation available to the validator.",
      "Confirm the two Anchoring instances use different evidence sources (extensometer baseline vs. crack photograph) and different decision points.",
      "Confirm interview draft target is 1,350 words (acceptable range 1,215-1,485) and can be reached without repeating bias-relevant content across probes.",
      "Confirm consequences (minor spall, no injuries) do not mechanically prove any decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to recall of the specific sister-mine rockburst, not a generic caution statement." },
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
      { "instance_id": "av_01", "bias": "Availability Bias" },
      { "instance_id": "exp_01", "bias": "Experience Bias" },
      { "instance_id": "anc_01", "bias": "Anchoring Bias" },
      { "instance_id": "anc_02", "bias": "Anchoring Bias" },
      { "instance_id": "narr_01", "bias": "Narrative Fallacy" },
      { "instance_id": "attr_01", "bias": "Attribution Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "av_01", "bias": "Availability Bias", "decision_point": 1 },
      { "instance_id": "anc_01", "bias": "Anchoring Bias", "decision_point": 2 },
      { "instance_id": "exp_01", "bias": "Experience Bias", "decision_point": 3 },
      { "instance_id": "anc_02", "bias": "Anchoring Bias", "decision_point": 3 },
      { "instance_id": "narr_01", "bias": "Narrative Fallacy", "decision_point": 4 },
      { "instance_id": "attr_01", "bias": "Attribution Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Vivid recall of the recent sister-mine rockburst inflates the perceived likelihood of the current ambiguous noise report.",
        "affected_reasoning_operation": "Risk-likelihood estimation from a verbal cue",
        "evidence_source": "Memory of a widely publicized recent industry incident",
        "distinctiveness_requirement": "Occurs only at decision point 1, tied specifically to the sister-mine memory, not repeated later."
      },
      {
        "instance_id": "anc_01",
        "bias": "Anchoring Bias",
        "mechanism": "Morning baseline extensometer reading anchors judgment of the later reading as 'still normal' instead of applying the rate-of-change rule.",
        "affected_reasoning_operation": "Comparative evaluation of updated instrument data against fixed initial reference",
        "evidence_source": "Extensometer displacement readings (05:00 baseline vs. 09:40 update)",
        "distinctiveness_requirement": "Uses instrument telemetry evidence at decision point 2; distinct from anc_02's photographic evidence at decision point 3."
      },
      {
        "instance_id": "exp_01",
        "bias": "Experience Bias",
        "mechanism": "Supervisor's tenure is treated as sufficient validation of a benign read, without checking situational similarity to today's conditions.",
        "affected_reasoning_operation": "Credibility weighting of informal expert opinion vs. threshold data",
        "evidence_source": "Supervisor's verbal recollection of a 2009 event",
        "distinctiveness_requirement": "Occurs only at decision point 3, distinct reasoning operation (credibility weighting) from anc_02's evidence comparison at the same decision point."
      },
      {
        "instance_id": "anc_02",
        "bias": "Anchoring Bias",
        "mechanism": "Prior week's photographed hairline crack anchors judgment of today's crack severity, displacing attention from the newly reached microseismic threshold.",
        "affected_reasoning_operation": "Visual/photographic comparison against a prior fixed reference",
        "evidence_source": "Crack-width photographs (last week vs. today)",
        "distinctiveness_requirement": "Uses photographic evidence at decision point 3; distinct evidence type and moment from anc_01's instrument-baseline anchor at decision point 2."
      },
      {
        "instance_id": "narr_01",
        "bias": "Narrative Fallacy",
        "mechanism": "Multiple loosely-related factors are woven into a single tidy causal chain in the post-event report, overstating certainty of the causal linkage.",
        "affected_reasoning_operation": "Post-hoc causal reconstruction for incident reporting",
        "evidence_source": "Temperature log, shift-change timing, prior blasting record",
        "distinctiveness_requirement": "Occurs only in the decision point 4 incident narrative, not in earlier probes or hypotheticals."
      },
      {
        "instance_id": "attr_01",
        "bias": "Attribution Bias",
        "mechanism": "Escalation responsibility is assigned mainly to the on-shift miner's reporting delay rather than to the missing systemic GCMP sign-off step.",
        "affected_reasoning_operation": "Causal attribution of responsibility between individual and systemic factors",
        "evidence_source": "Miner reporting timeline vs. GCMP sign-off requirement",
        "distinctiveness_requirement": "Occurs only in the decision point 4 responsibility assessment, distinct reasoning operation from narr_01's causal-chain construction at the same decision point."
      }
    ],
    "intended_strength": [
      { "instance_id": "av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "exp_01", "bias": "Experience Bias", "strength": "subtle" },
      { "instance_id": "anc_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "anc_02", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "narr_01", "bias": "Narrative Fallacy", "strength": "subtle" },
      { "instance_id": "attr_01", "bias": "Attribution Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_6",
    "domain_id": "MU",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across the 4 decision points by mechanism fit and narrative realism: Availability Bias placed at the initial ambiguous-report decision (DP1) where recall of a recent vivid event is most plausible; Anchoring Bias split across DP2 (instrument baseline) and DP3 (photographic reference) using two distinct evidence sources to satisfy the same-decision-point distinctiveness rule; Experience Bias placed at DP3 alongside but reasoning-operation-distinct from the second Anchoring instance; Narrative Fallacy and Attribution Bias both placed at DP4 (post-event review) but targeting different reasoning operations (causal-chain construction vs. responsibility attribution). No bias exceeds two occurrences at a single decision point.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
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
        "segment_type": "initial risk interpretation and escalation choice",
        "raw_interview_anchor": "my mind went straight to what happened at our sister operation two months earlier ... So even without an alarm, I treated that report as something that could be heading toward a similar event, more than I think the instrument data alone would have justified",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["av_01"],
        "ground_truth_rationale": "The participant explicitly states that recall of the recent sister-mine rockburst inflated the urgency assigned to the current non-alarmed report."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "instrument-reading interpretation",
        "raw_interview_anchor": "the 05:00 baseline was 0.2mm ... at 09:40 ... 0.6mm ... I was comparing it to the wrong reference",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["anc_01"],
        "ground_truth_rationale": "The later extensometer value is judged against the initial baseline instead of the GCMP rate-of-change rule."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "supervisor-evidence weighting",
        "raw_interview_anchor": "His track record is strong, so his read carried a lot of weight for me in that moment, maybe more than it should have on its own",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["exp_01"],
        "ground_truth_rationale": "Supervisor tenure and track record are overweighted without checking whether the 2009 situation matches the current conditions."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "visual evidence comparison",
        "raw_interview_anchor": "I compared it side-by-side with that old photo ... so I read it as consistent with what we already know is fine ... I was judging the crack against the old photo rather than against the newer seismic data",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["anc_02"],
        "ground_truth_rationale": "The prior crack photograph becomes the reference point and displaces attention from the newly crossed microseismic threshold."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "production-continuation pressure",
        "raw_interview_anchor": "The mine manager was also asking for a production ETA, so there was some pull to land on 'we're fine' rather than dig deeper into the trend math right then",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Production pressure is a documented contextual factor, but plan continuation bias is not part of the exhaustive hidden manifest for this interview."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "post-event causal explanation",
        "raw_interview_anchor": "it came together into a pretty clean story: cooling stresses plus the handover timing plus the residual vibration from that blast ... a coherent explanation ... none could really be confirmed as the dominant cause",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["narr_01"],
        "ground_truth_rationale": "The incident report turns several unresolved contributors into one tidy causal account after the event."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "responsibility attribution",
        "raw_interview_anchor": "I focused mainly on the miner ... if he'd flagged it again ... I did note the missing engineer sign-off ... but that came across more as a process footnote than as a central cause",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["attr_01"],
        "ground_truth_rationale": "Primary responsibility is assigned to an individual reporting delay while the missing GCMP sign-off is treated as secondary."
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
    "analysis_scope_note": "No retrieved scientific corpus passages were supplied in the analysis context; bias classifications rely on established cognitive-science knowledge and the transcript alone."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 2
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
      "bias_label": "fundamental attribution error",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "narrative fallacy",
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
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or urgency of an event by how easily salient examples come to mind, rather than by systematic assessment of current objective indicators.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial response to 06:40 cracking report",
      "decision_point_description": "Choosing among full evacuation and stop work, enhanced monitoring with limited access, or instrument technician check only.",
      "affected_reasoning_operation": "Risk assessment and initial diagnostic escalation",
      "bias_specific_mechanism": "A recent, emotionally salient sister-mine rockburst was highly available in memory, leading the participant to treat the current cracking report as more likely to be a similar event than current seismic monitoring or local condition data would support.",
      "manifestation_in_interview": "The participant immediately connected the report to the sister-mine incident and escalated to enhanced monitoring despite no alarm and admittedly weaker instrument data.",
      "effect_on_reasoning_or_decision": "The participant selected enhanced monitoring and limited access rather than a more instrument-driven check, and acknowledged that salience of the prior event made the situation feel more urgent.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "honestly, my mind went straight to what happened at our sister operation two months earlier — that rockburst that made the trade press and had everyone in the region talking. It wasn't identical conditions, but it was the same ore body region, and that event was still very much front of mind for the whole crew. So even without an alarm, I treated that report as something that could be heading toward a similar event, more than I think the instrument data alone would have justified.",
          "evidence_explanation": "The participant explicitly states that a salient recent rockburst, not current instrument data, drove his initial risk judgment, which is the mechanism of availability."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think without that fresh in everyone's mind, I might have waited for the instrument tech's check before doing anything, rather than jumping to enhanced monitoring right away.",
          "evidence_explanation": "The counterfactual supports availability: without the salient memory, he likely would not have escalated immediately."
        }
      ],
      "correction_or_counterevidence": "Heightened vigilance after a nearby rockburst could be a legitimate, conservative mining response. However the participant's own counterfactual and explicit statement that he treated the report as heading toward a similar event 'more than... instrument data alone would have justified' indicates availability distorted the diagnostic weighting.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No corpus passages were supplied; availability heuristic is classified from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring heuristic",
        "anchoring and adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial reference value when making judgments, leading to insufficient adjustment to newer or more diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of 09:40 extensometer reading",
      "decision_point_description": "Determining whether the movement from 0.2mm to 0.6mm warranted escalation according to the Ground Control Management Plan.",
      "affected_reasoning_operation": "Numerical inference and threshold evaluation",
      "bias_specific_mechanism": "The participant anchored on the morning baseline reading of 0.2mm and on the absolute sub-millimeter value of 0.6mm, rather than adjusting to the rate-of-change threshold specified in the GCMP, which was the relevant diagnostic criterion.",
      "manifestation_in_interview": "He interpreted a tripling of baseline movement as 'nothing dramatic' because 0.6mm still sounded small, and did not check the rate-of-change table.",
      "effect_on_reasoning_or_decision": "He failed to escalate the extensometer trend correctly; this contributed to a missed opportunity to update risk before the later spall.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At 09:40 the tech radioed that it had moved to 0.6mm. That's three times the baseline in about three hours. I looked at it and thought, well, compared to this morning it's still a small number, still sub-millimeter, nothing dramatic. I didn't go back and check it against the rate-of-change table in the GCMP, which is actually the correct way to assess it — that plan cares about how fast it's moving, not just where it sits relative to where it started. In hindsight I was comparing it to the wrong reference.",
          "evidence_explanation": "The participant identifies that he used the morning baseline as the comparison point and failed to use the plan's rate-of-change threshold, which is the anchoring distortion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It's just naturally what you have in front of you — you saw it at 0.2 that morning, now it's 0.6, and 0.6 still sounds low in absolute terms.",
          "evidence_explanation": "This further illustrates the anchor on the previously observed baseline and the absolute number, rather than the trend."
        }
      ],
      "correction_or_counterevidence": "Production pressure from the mine manager's ETA request was present and may have contributed to a 'we're fine' preference, but the participant explicitly attributes the cognitive error to comparing against the wrong reference rather than to deliberate rule violation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No corpus passages were supplied; anchoring bias is classified from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "authority bias",
      "alternative_labels": [
        "authority heuristic",
        "expert halo effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to over-weight the judgment of a perceived authority or highly experienced person, sometimes reducing independent verification or data-based decision-making.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Conversation with shift supervisor about 2009 popping and microseismic threshold",
      "decision_point_description": "Deciding whether to follow the seismic flag threshold strictly, reduce crew size, or accept the supervisor's reassurance and continue limited access.",
      "affected_reasoning_operation": "Evidence weighting and decision to continue access",
      "bias_specific_mechanism": "The supervisor's 22 years underground and strong track record led the participant to accept his 'nothing' assessment and not challenge whether the 2009 event matched current rock type, blast pattern, or depth, even though microseismic counts had just exceeded the plan threshold.",
      "manifestation_in_interview": "The participant noted the supervisor's confidence and track record carried 'maybe more than it should have' and chose limited access rather than strict seismic threshold follow-up.",
      "effect_on_reasoning_or_decision": "He selected reduced crew and limited access based partly on a non-validated analog and seniority, rather than the plan's flag threshold.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He's got twenty-two years underground, most of it at this site. He mentioned he'd heard similar popping back in 2009, and it hadn't come to anything. He was pretty confident it was 'nothing.' Around that same time the microseismic count for the shift had actually climbed to six events an hour, which is right at — actually just over — the flag threshold in our plan. I didn't push hard on whether the 2009 case actually matched today's rock type, blast pattern, or depth. His track record is strong, so his read carried a lot of weight for me in that moment, maybe more than it should have on its own.",
          "evidence_explanation": "The participant explicitly describes deferring to the supervisor's judgment because of his experience and track record, while failing to verify the analog or act on the threshold breach."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with limited access, mostly on the supervisor's confidence and my own read of that crack photo.",
          "evidence_explanation": "This directly links the supervisor's confidence to the decision, supporting authority bias."
        }
      ],
      "correction_or_counterevidence": "Consulting senior experienced personnel is legitimate in mining; authority bias is identified because the participant explicitly says the supervisor's read carried more weight than it should have on its own and it displaced the objective threshold.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No corpus passages were supplied; authority bias is classified from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring heuristic",
        "anchoring and adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial reference value when making judgments, leading to insufficient adjustment to newer or more diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Crack inspection in the same panel",
      "decision_point_description": "Assessing whether the existing hairline crack was stable or insignificant before allowing continued access.",
      "affected_reasoning_operation": "Visual inspection, risk updating, and integration of seismic data",
      "bias_specific_mechanism": "The prior week's photo and 'insignificant' classification served as an anchor, so the participant judged the current crack by side-by-side visual similarity to that old baseline rather than by integrating the newer threshold-exceeding microseismic data.",
      "manifestation_in_interview": "He read the crack as 'consistent with what we already know is fine' and did not update with the newer seismic information.",
      "effect_on_reasoning_or_decision": "This supported continued limited access even though the current seismic data had crossed the plan's flag threshold.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I looked at today's crack, I compared it side-by-side with that old photo, and it looked about the same width to me, so I read it as 'consistent with what we already know is fine.' What I didn't do at that point was connect it back to the microseismic number that had just ticked over the threshold — I was judging the crack against the old photo rather than against the newer seismic data.",
          "evidence_explanation": "The participant explicitly describes using the old photo as the reference point and failing to integrate the newer seismic data, which is an anchoring-based updating failure."
        }
      ],
      "correction_or_counterevidence": "Comparing against baseline photography is a standard field practice; however the selected baseline had been classified as insignificant and did not incorporate new seismic threshold information.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No corpus passages were supplied; anchoring bias is classified from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "narrative fallacy",
      "alternative_labels": [
        "narrative bias",
        "coherence bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to assemble available facts into a coherent story and then confuse the tidiness or plausibility of that story with demonstrated causation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-incident causal attribution in report",
      "decision_point_description": "Determining the primary cause in the incident report.",
      "affected_reasoning_operation": "Causal attribution and explanatory confidence",
      "bias_specific_mechanism": "After the event, the participant combined temperature, shift change, and prior blast into a clean causal account; the coherence of this account increased his confidence in it as the primary explanation despite acknowledged ambiguity.",
      "manifestation_in_interview": "He wrote the clean story as the primary cause, while the engineer's note said several factors were plausible and none could be confirmed as dominant.",
      "effect_on_reasoning_or_decision": "The report overcommitted to a single causal account, and the participant later reported lower confidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking at everything together — the overnight temperature drop, the shift change happening not long before, and the blasting in the panel next door the prior week — it came together into a pretty clean story: cooling stresses plus the handover timing plus the residual vibration from that blast. It read as a coherent explanation, so that's what I put forward as the primary account, even though the engineer's later note said several factors were plausible and none could really be confirmed as the dominant cause.",
          "evidence_explanation": "The participant describes forming a tidy causal story and selecting it as primary despite explicit uncertainty, which is the core mechanism of narrative fallacy."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It felt tidy at the time, but there were a few threads I didn't fully chase down.",
          "evidence_explanation": "This retrospective statement supports that the tidiness drove initial confidence rather than resolved causal certainty."
        }
      ],
      "correction_or_counterevidence": "The causal factors were plausible, and report writing cannot always include full uncertainty; however the participant selected a single 'pretty clean story' as primary despite explicit uncertainty from the engineer.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No corpus passages were supplied; narrative fallacy is classified from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "fundamental attribution error",
      "alternative_labels": [
        "correspondence bias",
        "dispositional attribution bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to over-attribute behavior or outcomes to individual disposition or intention and under-emphasize situational or systemic factors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Responsibility framing in incident report",
      "decision_point_description": "Determining how to frame responsibility and central cause in the incident report.",
      "affected_reasoning_operation": "Responsibility attribution and causal emphasis",
      "bias_specific_mechanism": "In assigning responsibility for the incident, the participant centered on the miner's failure to escalate again, while treating the missing engineer sign-off after the threshold breach as a background process footnote, which is an asymmetric dispositional attribution.",
      "manifestation_in_interview": "The report focused mainly on the miner; the systemic and procedural missing sign-off was noted but not given central causal weight.",
      "effect_on_reasoning_or_decision": "The report likely allocated responsibility disproportionately to a frontline individual and downplayed system or process control failures.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I focused mainly on the miner who first heard the sounds and didn't escalate again after the initial 06:40 report — I felt if he'd flagged it again once the popping continued, we might have caught it sooner. I did note the missing engineer sign-off after the six-events flag, but that came across more as a process footnote than as a central cause in the report.",
          "evidence_explanation": "This shows a clear asymmetry: individual non-escalation is treated as central, while the systemic missing sign-off is backgrounded, consistent with fundamental attribution error."
        }
      ],
      "correction_or_counterevidence": "The miner's failure to re-escalate may be a real causal factor, and the missing sign-off was not omitted entirely; the bias is in relative emphasis and attributional framing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No corpus passages were supplied; fundamental attribution error is classified from established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-incident causal attribution in report",
      "supporting_interview_quote": "Looking at everything together — the overnight temperature drop, the shift change happening not long before, and the blasting in the panel next door the prior week — it came together into a pretty clean story: cooling stresses plus the handover timing plus the residual vibration from that blast.",
      "plausible_mechanism": "After knowing the incident occurred, the participant may have reconstructed prior signals as fitting a predictable causal path.",
      "why_not_identified": "The transcript does not clearly evidence a sense of retrospective predictability; the stronger explicit mechanism is the tidy causal story itself, which was classified as narrative fallacy."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "self-serving bias",
      "alternative_labels": [
        "defensive attribution bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Responsibility attribution in incident report",
      "supporting_interview_quote": "I focused mainly on the miner who first heard the sounds and didn't escalate again after the initial 06:40 report — I felt if he'd flagged it again once the popping continued, we might have caught it sooner. I did note the missing engineer sign-off after the six-events flag, but that came across more as a process footnote than as a central cause in the report.",
      "plausible_mechanism": "As Health and Safety Officer, the participant may be motivated to assign primary blame to a frontline individual and minimize systemic or supervisory failures.",
      "why_not_identified": "The transcript does not provide direct evidence of defensive motivation; the attribution asymmetry is better explained by fundamental attribution error."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific corpus passages were supplied, so corpus support is unavailable for any classification.",
    "The analysis relies on a single retrospective self-report, which may be influenced by memory reconstruction and social desirability.",
    "Some episodes involve legitimate professional heuristics under uncertainty; labels are assigned only where the participant explicitly or structurally indicated distorting effects."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Biased_6_Gemini_off",
  "interview_id": "MU_Biased_6",
  "system_prompt_id": "Gemini",
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
