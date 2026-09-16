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
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single retrospective cognitive task analysis interview focused on a mining site ground-control and blast-authorization incident. Statements from the participant were analyzed for bias-specific reasoning mechanisms; interviewer questions were used only for context and elicitation."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
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
      "bias_label": "overconfidence bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "status quo bias",
      "alternative_labels": [
        "default bias",
        "status quo preference"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to prefer maintaining the current state or existing plan and to require stronger justification for changing it than for continuing it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "First-morning decision whether to pause or continue the planned stope work under an existing ground support plan",
      "decision_point_description": "After three overnight microseismic events and no visible damage, the participant decided to let the day shift enter and drill rather than pause for inspection, reduce crew, or revise the approved plan.",
      "affected_reasoning_operation": "Risk assessment and selection among maintain-plan, inspect, or revise-plan options",
      "bias_specific_mechanism": "The participant treated the absence of visible structural change as a reason to retain the signed-off plan and represented revising the approved plan as a disruption requiring stronger justification than continuing.",
      "manifestation_in_interview": "The participant explicitly framed the existing plan as still sound because nothing had changed, and characterized revising it as more disruption than the situation called for.",
      "effect_on_reasoning_or_decision": "The participant did not hold the crew back; day shift proceeded into the stope as scheduled under the existing plan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The ground support plan for that stope had been signed off about four months earlier, and nothing had changed structurally since then — no fall of ground, nothing visible. So my read was that the plan was still sound, and I didn't see a reason to hold the crew back.",
          "evidence_explanation": "This shows the existing plan as the default: no observed change is taken as sufficient justification for no action, a status-quo-preserving inference."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We had options — pause entry and get an unscheduled inspection, or drop crew numbers until someone looked at it — but honestly, revising an approved plan on the back of three events felt like more disruption than the situation called for. We let day shift go in and start drilling as scheduled.",
          "evidence_explanation": "The participant compares alternatives against the cost of changing the approved plan and selects continuation, indicating a preference for the current plan rather than a balanced risk comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd probably want more of a structured comparison next time — actually laying the new seismic readings against the plan's original assumptions, rather than just defaulting to 'nothing's changed, so we haven't changed anything.' At the time, though, it felt like the obvious choice.",
          "evidence_explanation": "Retrospective description explicitly names the status-quo-style default reasoning: 'nothing's changed, so we haven't changed anything.'"
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that a structured comparison would have been preferable; no visible damage and three overnight events could also support a legitimate heuristic rather than bias. However, the stated default reasoning is affirmative for status quo bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for status quo bias was not available; the label is applied from established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial numerical value or anchor, with insufficient adjustment from it when making subsequent judgments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of the 2.3 hazard rating and afternoon blast clearance",
      "decision_point_description": "After receiving the geotech model hazard rating of 2.3 ('moderate but manageable'), the participant decided whether to wait for engineer review, request an updated rating, or authorize blast clearance.",
      "affected_reasoning_operation": "Quantitative risk interpretation and blast clearance decision",
      "bias_specific_mechanism": "The initial specific numeric score of 2.3 served as an anchor, treated as settled and official, with insufficient adjustment for the known array blind spot.",
      "manifestation_in_interview": "The participant stated that the number was specific and official-looking, making it easy to treat as settled rather than something to test against the known blind spot.",
      "effect_on_reasoning_or_decision": "The participant did not request an updated rating accounting for the blind spot or hold the blast; he authorized the afternoon blast clearance.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The model came back with a 2.3 on their five-point scale, tagged 'moderate but manageable.'",
          "evidence_explanation": "This establishes the initial numeric and verbal anchor that the participant used to frame later risk judgments."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A fair amount. It came from the model, and it was specific and official-looking, which made it easy to treat as settled rather than something to test against the blind spot we already knew was there.",
          "evidence_explanation": "The participant explicitly describes treating the 2.3 as settled rather than adjusting for the array blind spot, which is the anchoring-and-insufficient-adjustment mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And if the hazard rating had come back at 3.5 instead of 2.3? That would have stopped me. A 3.5 doesn't let you lean on a comfortable memory the way a 2.3 does.",
          "evidence_explanation": "This counterfactual demonstrates that the decision was anchored to the specific 2.3 value: a different numeric anchor would have produced a different decision."
        }
      ],
      "correction_or_counterevidence": "The participant recognized that the model had a known blind spot and that an updated rating could have been requested, so the information needed for adjustment was available. The blast did not fail, but that retrospective outcome does not negate the anchoring mechanism in the decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages support the anchoring-and-adjustment mechanism: people make estimates from an initial value and adjustments are typically insufficient.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.” [16]",
          "mechanism_supported_by_source": "Anchoring and adjustment involves making estimates from an initial value with typically insufficient adjustments.",
          "relevance_to_this_occurrence": "The participant used the model's 2.3 rating as the initial value and did not sufficiently adjust for the known array blind spot before authorizing blast clearance."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or importance of an event by the ease with which examples come to mind, rather than by broader statistical information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Use of the Stope 9 precedent to judge the current hazard rating",
      "decision_point_description": "When interpreting the 2.3 hazard rating, the participant relied on the fresh Stope 9 memory and did not pull broader comparable events across other stopes.",
      "affected_reasoning_operation": "Likelihood and risk judgment for ground-control escalation",
      "bias_specific_mechanism": "The participant judged the current risk by the ease and vividness of a recent similar case, Stope 9, rather than by a broader comparison of comparable events.",
      "manifestation_in_interview": "The participant said Stope 9 was the first thing that came to mind and that he did not pull the broader run of comparable events; Stope 9 was the one fresh in his head.",
      "effect_on_reasoning_or_decision": "The participant felt reasonably comfortable with the 2.3 rating and authorized the afternoon blast clearance without examining broader base-rate information.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The Stope 9 situation was actually the first thing that came to mind — it had come up on the shift handover just a few days earlier, almost the exact same rating and event cluster, and it had resolved completely fine, no incident. Between the number and that memory, I felt reasonably comfortable.",
          "evidence_explanation": "This explicitly shows reliance on a salient, easily recalled case to assess current risk, a hallmark of the availability heuristic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go pull the broader run of comparable events across other stopes to see how those had generally played out; Stope 9 was just the one that was fresh in my head, so that's what I went with.",
          "evidence_explanation": "The participant acknowledges that he used the mentally available example rather than broader comparison data, which is the availability mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant recognized in the interview that broader comparable events could have been pulled; the availability-driven judgment was later described as the factor he went with at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the availability heuristic was not available; the label is applied from established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's existing beliefs or hypotheses, while underweighting or ignoring disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Assessment of post-blast cracking and conflicting views",
      "decision_point_description": "After hairline cracking was reported, the participant weighed a junior inspector's re-support recommendation against two crew members' 'typical settling' views and decided what to report upward.",
      "affected_reasoning_operation": "Evidence weighting and risk communication",
      "bias_specific_mechanism": "The participant preferentially accepted and passed along evidence consistent with the existing belief that the cracking was benign, while discounting and omitting the conflicting inspector recommendation.",
      "manifestation_in_interview": "The participant leaned toward the crew's read, filed the inspector's note rather than raising it, and said the inspector's note would just muddy a picture that already seemed clear.",
      "effect_on_reasoning_or_decision": "The reporting to the production superintendent emphasized 'typical settling' and omitted the inspector's re-support recommendation; no independent check was arranged.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Around the same time a junior inspector — one of the geotech contractor's people — sent an email recommending we re-support before doing any more blasting. But two other crew members separately told me it looked like typical post-blast settling, nothing unusual.",
          "evidence_explanation": "This establishes two conflicting information sources, one contrary to and one consistent with the participant's existing view."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned toward the crew's read. We'd seen a very similar crack pattern in Stope 9 previously that never led anywhere. So when the reporting went up to the production superintendent, I passed along the crew's 'typical settling' assessments. The inspector's note got filed — I didn't raise it on the shift call, mostly because it felt like it would just muddy a picture that already seemed clear enough from the people who were actually standing there.",
          "evidence_explanation": "This shows confirmation bias: favoring information consistent with the preferred 'typical settling' interpretation, while suppressing the disconfirming inspector recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At the time it didn't feel necessary because the Stope 9 comparison made the pattern seem like something we already understood.",
          "evidence_explanation": "The participant's existing understanding, reinforced by a prior case, made the ambiguous cracking seem already explained, reducing motivation to consider the conflicting recommendation."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged retrospectively that the cracking could have been treated as inconclusive and checked independently. No outcome-based correction exists because the blast went fine, so this is not a case of using later failure to infer bias.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus evidence supports confirmation bias as focusing on indicators consistent with a preferred safe interpretation while ignoring contradictory indicators.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The accident report of flight JZA7795 (2015) which landed short of the runway in poor weather, found t influenced the false perception that the aircraft was in a stable condition, and the crew’s confirmation bias focussed on the factors that indicated the approach was safe while ignoring those that did no t.",
          "mechanism_supported_by_source": "Confirmation bias involves focusing on factors consistent with a preferred safe interpretation while ignoring contradictory factors.",
          "relevance_to_this_occurrence": "The participant similarly focused on crew assessments that the cracking was normal settling and did not elevate or independently assess the inspector's contrary re-support recommendation."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "overconfidence bias",
      "alternative_labels": [
        "overconfidence effect",
        "illusion of validity"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to hold excessive subjective confidence in one's judgments or abilities, often exceeding what the available evidence supports.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final decision to authorize the next scheduled blast despite missing sensor data and a small rock fall",
      "decision_point_description": "With one array node lagging and a small rock fall near the access drift, the participant decided to proceed with the scheduled blast rather than suspend or escalate for a fresh engineering look.",
      "affected_reasoning_operation": "Risk judgment and decision-making under uncertainty",
      "bias_specific_mechanism": "The participant relied on subjective confidence in intuitive judgment based on twenty years of experience, discounting missing objective sensor confirmation.",
      "manifestation_in_interview": "The participant said he was confident in the call and that twenty years gives a feel that a delayed sensor reading does not necessarily add to.",
      "effect_on_reasoning_or_decision": "The participant authorized the blast without objective sensor confirmation and did not escalate to the engineer for a fresh look.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, that rock fall didn't worry me much. I've personally been through plenty of similar events over twenty years underground, and they almost never escalate. If anything, it read to me as consistent with what we'd already been seeing — minor settling, nothing structural. I authorized the blast.",
          "evidence_explanation": "This shows high subjective confidence in a personal-experience-based interpretation of a warning signal, independent of objective sensor data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a gap, sure — we didn't have the sensor confirmation we'd normally want. But I was confident in the call. Twenty years gives you a feel for these things that a delayed sensor reading doesn't necessarily add to.",
          "evidence_explanation": "The participant explicitly acknowledges missing objective data but expresses confidence in experiential feel, demonstrating overconfidence in his own judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Both were on the table. I just didn't think either was warranted given how the shift had gone.",
          "evidence_explanation": "The participant dismissed available safeguards because his judgment was sufficient, consistent with overconfidence rather than substantive evidence."
        }
      ],
      "correction_or_counterevidence": "The blast went fine and ground stayed stable, so the outcome did not reveal an error; the participant also scheduled a post-shift review. This does not negate the overconfidence mechanism at the time of the decision, but it does mean the bias is identified from reasoning rather than from a bad outcome.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for overconfidence bias was not available; the label is applied from established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "normalcy bias",
      "alternative_labels": [
        "false sense of normality"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final blast authorization after sensor lag and small rock fall",
      "supporting_interview_quote": "Honestly, that rock fall didn't worry me much. I've personally been through plenty of similar events over twenty years underground, and they almost never escalate.",
      "plausible_mechanism": "The participant may have normalized a warning sign because past similar events had not escalated, reducing perceived risk.",
      "why_not_identified": "The interview supports an overconfidence mechanism more directly, and the normalcy interpretation overlaps with availability and overconfidence; no distinct normalcy-bias effect was sufficiently separable."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Continued scheduled blasting across escalating warning cues",
      "supporting_interview_quote": "The superintendent was pushing to keep the blast on schedule to hit the month-end number. ... Both were on the table. I just didn't think either was warranted given how the shift had gone.",
      "plausible_mechanism": "The participant continued the original blast plan despite accumulating warning cues, possibly under production schedule pressure.",
      "why_not_identified": "Production pressure alone is not evidence of a cognitive bias, and the participant's stated reasoning emphasizes perceived sufficiency of evidence and experiential confidence rather than a distinct plan-continuation mechanism; therefore not identified."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Single retrospective participant account; no independent process tracing or outcome data.",
    "Retrieved corpus is sparse and not specific to mining; some bias labels are applied from general cognitive-science knowledge due to limited corpus support.",
    "The blast produced no negative outcome, so later statements about what might have been done differently are treated as retrospective rather than as proof of bias at the time.",
    "Analysis is conservative and mechanism-first; environmental factors such as production pressure were not treated as biases without affirmative evidence of a specific cognitive mechanism."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Biased_7_Sonar_on",
  "interview_id": "MU_Biased_7",
  "system_prompt_id": "Sonar",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
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
