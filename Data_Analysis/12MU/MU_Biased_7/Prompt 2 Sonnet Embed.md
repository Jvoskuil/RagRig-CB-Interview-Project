You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
**Interviewer:** Thanks for making time for this. Just to confirm, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the incident, not in second-guessing the outcome. Everything's confidential and used for training and research purposes only. You're an Assistant Mine Manager at the site, correct?

**Participant:** That's right. I've been in that role about three years, twenty years underground total, mostly hard rock.

**Interviewer:** Good. Let's start broad — can you walk me through what was happening in Stope 14 East during that shift?

**Participant:** Sure. We were running a stope on the 950 level, standard longhole retreat mining. We'd had three microseismic events overnight — moderate magnitude, above what the array normally logs for that block over a rolling thirty-day average. No visible damage reported by the night shift, though. At the same time, we were two days behind on the monthly tonnage target, so there was some pressure from the production side to keep things moving.

**Interviewer:** What was your main objective going into that morning?

**Participant:** Keep the crew safe, obviously, but also not create a stoppage we couldn't justify. We'd had false alarms before — events that looked concerning on paper but turned out to be nothing. You don't want to shut a stope every time the array blips, or the crew starts tuning out the real warnings.

**Interviewer:** Take me through what you actually decided that morning.

**Participant:** The ground support plan for that stope had been signed off about four months earlier, and nothing had changed structurally since then — no fall of ground, nothing visible. So my read was that the plan was still sound, and I didn't see a reason to hold the crew back. We had options — pause entry and get an unscheduled inspection, or drop crew numbers until someone looked at it — but honestly, revising an approved plan on the back of three events felt like more disruption than the situation called for. We let day shift go in and start drilling as scheduled.

**Interviewer:** Did anything happen during that shift that stood out?

**Participant:** A bit of loose rock came off a rib wall mid-shift. Crew scaled it down, logged it as routine. Nothing that changed my thinking at that point.

**Interviewer:** Let's move to later that day — you mentioned a hazard rating came in.

**Participant:** Yes, our geotech support is remote most of the week — the engineer's only on-site two days. The model came back with a 2.3 on their five-point scale, tagged "moderate but manageable." The Stope 9 situation was actually the first thing that came to mind — it had come up on the shift handover just a few days earlier, almost the exact same rating and event cluster, and it had resolved completely fine, no incident. Between the number and that memory, I felt reasonably comfortable.

**Interviewer:** Were there other options at that point?

**Participant:** We could have asked for an updated rating that accounted for the blind spot near the intersection — the array doesn't read well there — or just held the blast until the engineer was back on-site the next day. I didn't go pull the broader run of comparable events across other stopes to see how those had generally played out; Stope 9 was just the one that was fresh in my head, so that's what I went with. The 2.3 read as solid enough, and Stope 9 had gone fine under similar numbers, so I authorized the afternoon blast clearance.

**Interviewer:** How much weight did that number carry versus other considerations?

**Participant:** A fair amount. It came from the model, and it was specific and official-looking, which made it easy to treat as settled rather than something to test against the blind spot we already knew was there.

**Interviewer:** What happened after the blast was cleared?

**Participant:** About two hours later there was a second event, larger than the first three, and outside what the model's confidence range would have predicted.

**Interviewer:** Let's talk about what happened next — the cracking.

**Participant:** Right, after the blast, the shift supervisor flagged some hairline cracking in the shotcrete on one rib. Around the same time a junior inspector — one of the geotech contractor's people — sent an email recommending we re-support before doing any more blasting. But two other crew members separately told me it looked like typical post-blast settling, nothing unusual.

**Interviewer:** How did you weigh those two views?

**Participant:** I leaned toward the crew's read. We'd seen a very similar crack pattern in Stope 9 previously that never led anywhere. So when the reporting went up to the production superintendent, I passed along the crew's "typical settling" assessments. The inspector's note got filed — I didn't raise it on the shift call, mostly because it felt like it would just muddy a picture that already seemed clear enough from the people who were actually standing there.

**Interviewer:** Was there a version of that decision where the inspector's note carried equal weight?

**Participant:** Looking back, sure — we could have treated the cracking as inconclusive and brought in an independent check rather than leaning on precedent and the on-the-ground opinions. At the time it didn't feel necessary because the Stope 9 comparison made the pattern seem like something we already understood.

**Interviewer:** Let's get to the final decision point — the next scheduled blast.

**Participant:** Right before that decision, one of the array nodes had sensor lag, so we didn't have confirmed magnitude data for recent ground movement. Then a small rock fall happened near the access drift — no injuries, minor. The superintendent was pushing to keep the blast on schedule to hit the month-end number.

**Interviewer:** What went into your call there?

**Participant:** Honestly, that rock fall didn't worry me much. I've personally been through plenty of similar events over twenty years underground, and they almost never escalate. If anything, it read to me as consistent with what we'd already been seeing — minor settling, nothing structural. I authorized the blast.

**Interviewer:** Were you uncertain at all in that moment?

**Participant:** There was a gap, sure — we didn't have the sensor confirmation we'd normally want. But I was confident in the call. Twenty years gives you a feel for these things that a delayed sensor reading doesn't necessarily add to.

**Interviewer:** Could you have suspended the blast pending that data, or escalated to the engineer for a fresh look?

**Participant:** Both were on the table. I just didn't think either was warranted given how the shift had gone.

**Interviewer:** What happened afterward?

**Participant:** The blast went fine. Ground stayed stable through the rest of the shift. We did schedule a post-shift review, though the underlying ground support plan wasn't actually revised.

**Interviewer:** Stepping back — if the geotechnical engineer had been on-site the whole time rather than remote, would anything have gone differently?

**Participant:** Possibly. Having someone physically there to look at the cracking directly, rather than relying on an email and crew impressions, might have changed how that got weighted.

**Interviewer:** And if the hazard rating had come back at 3.5 instead of 2.3?

**Participant:** That would have stopped me. A 3.5 doesn't let you lean on a comfortable memory the way a 2.3 does.

**Interviewer:** Looking back, would you make the same call on continuing under the existing support plan that first morning?

**Participant:** I'd probably want more of a structured comparison next time — actually laying the new seismic readings against the plan's original assumptions, rather than just defaulting to "nothing's changed, so we haven't changed anything." At the time, though, it felt like the obvious choice.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Biased_7",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Underground Mine Manager / Assistant Mine Manager",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Elevated Microseismicity Near Stope 14 East During a Behind-Schedule Production Push",
    "scenario_summary_internal": "An Assistant Mine Manager at a deep underground hard-rock mine must decide how to respond to a sequence of elevated microseismic events near an active stope while production is behind schedule. Ground control monitoring, a proprietary seismic hazard-rating model, shift-crew reports, and the manager's own recent experience with a similar 'false alarm' event all feed into four sequential decisions spanning roughly one shift-and-a-half, ending with a decision to proceed with a scheduled blast despite unresolved warning signs.",
    "occupational_realism": {
      "objective": "Maintain safe ground conditions in Stope 14 East while meeting a tightening weekly ore-production target, without triggering an unnecessary work stoppage.",
      "setting": "A deep underground hard-rock (gold/base-metal analog) mine, 950m level, active stoping area with a real-time microseismic monitoring array and a contracted geotechnical engineering team providing periodic hazard ratings.",
      "constraints": [
        "Production schedule is two days behind target for the month",
        "Geotechnical engineer is only on-site two days per week; remote support is used the rest of the time",
        "Evacuating or re-supporting the stope costs 12-18 hours of lost production",
        "Seismic monitoring array has known blind spots near intersections and old workings",
        "Shift crew morale and trust in management is affected by perceived overreaction to false alarms"
      ],
      "stakeholders": [
        "Assistant Mine Manager (interviewee)",
        "Shift supervisor on Stope 14 East",
        "Contract geotechnical engineer",
        "Production superintendent",
        "Underground crew (drill and blast team)"
      ],
      "technical_terms_to_use": [
        "microseismic event",
        "seismic hazard rating",
        "ground support plan",
        "stope",
        "shotcrete",
        "rockburst potential",
        "re-entry protocol",
        "blast clearance",
        "strain energy",
        "fall of ground (FOG)"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "status quo bias",
        "illusion of validity",
        "overconfidence bias",
        "availability bias",
        "heuristic",
        "cognitive bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Microseismic array logs three moderate-magnitude events near Stope 14 East overnight, above the 30-day baseline",
          "The existing ground support plan for the stope was approved four months ago and has not been revised since",
          "Production is two days behind schedule for the month",
          "No visible ground damage reported by night shift"
        ],
        "new_information_after_decision": [
          "Day shift crew enters Stope 14 East and begins scheduled drilling without additional ground inspection",
          "A minor loose rock is scaled off a rib wall mid-shift, logged as routine"
        ],
        "alternatives": [
          "Continue operations under the existing ground support plan as approved",
          "Pause entry and request an unscheduled ground control inspection before crew entry",
          "Reduce crew numbers in the stope while inspection is pending"
        ],
        "intended_action": "Continue operations under the existing, unrevised ground support plan"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The remote geotechnical model returns a numeric seismic hazard rating of 2.3 on a 5-point scale for the affected zone, labeled 'moderate but manageable'",
          "The manager recalls a similar rating and event cluster six weeks earlier near Stope 9 that resolved without incident",
          "The monitoring array has a documented blind spot near the intersection adjacent to Stope 14 East",
          "The geotechnical engineer is off-site until the following day"
        ],
        "new_information_after_decision": [
          "Blast clearance is granted for the afternoon round based on the hazard rating",
          "A second, larger microseismic event is logged two hours after the rating was issued, outside the model's confidence interval"
        ],
        "alternatives": [
          "Accept the 2.3 rating as sufficient basis to proceed with the planned blast",
          "Request an updated rating incorporating the array's known blind spot before authorizing the blast",
          "Delay the blast until the geotechnical engineer returns on-site"
        ],
        "intended_action": "Accept the numeric hazard rating and authorize the afternoon blast, citing the earlier Stope 9 experience as reassurance"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Following the blast, shotcrete on one rib shows new hairline cracking, reported by the shift supervisor as concerning",
          "A junior geotechnical inspector emails a cautionary note recommending re-support before further blasting",
          "Two other crew members separately describe the cracking as 'typical settling after a blast'",
          "Historical logs show a comparable crack pattern in Stope 9 that did not precede a fall of ground"
        ],
        "new_information_after_decision": [
          "The manager forwards only the crew's 'typical settling' assessments to the production superintendent",
          "The junior inspector's cautionary note is filed but not escalated or discussed on the shift call"
        ],
        "alternatives": [
          "Treat the cracking as inconclusive and commission an independent structural check before continuing",
          "Weigh the junior inspector's recommendation equally against crew observations",
          "Proceed on the basis that crew observations and the Stope 9 precedent are sufficient"
        ],
        "intended_action": "Proceed with the production plan, emphasizing crew reassurance and downplaying the inspector's caution"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Sensor lag on one array node delays confirmation of ground movement magnitude for the next scheduled blast",
          "A small unplanned rock fall (no injuries) occurs near the stope access drift shortly before the decision window",
          "The manager has 20 years of underground experience and has personally overseen similar rock falls without escalation",
          "Production superintendent is pressing for the blast to proceed to hit the monthly target"
        ],
        "new_information_after_decision": [
          "The blast proceeds as scheduled; ground conditions remain stable through the shift",
          "A post-shift review is scheduled but the underlying ground support plan is not revised"
        ],
        "alternatives": [
          "Authorize the blast based on personal judgment and past experience with similar rock falls",
          "Suspend the blast pending confirmed sensor data",
          "Escalate to the geotechnical engineer for a fresh independent assessment"
        ],
        "intended_action": "Authorize the blast, expressing high confidence in personal judgment despite the sensor lag and interpreting the rock fall as further confirmation that conditions are stable"
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what was happening in Stope 14 East that shift?",
        "What was your main objective going into that decision window?"
      ],
      "timeline_reconstruction": [
        "What did you know at the moment you decided to continue under the existing ground support plan?",
        "Walk me through what happened right after the hazard rating came in.",
        "What did the shift supervisor and the junior inspector each tell you, and in what order?",
        "What information arrived after the blast that changed or didn't change your view?"
      ],
      "decision_point_probes": [
        "What alternatives did you consider before continuing operations under the existing plan?",
        "How much weight did the numeric hazard rating carry in your decision, and why?",
        "How did you decide which reports to pass along to the superintendent?",
        "What made you confident enough to authorize the final blast despite the sensor lag?"
      ],
      "goals": [
        "What were you trying to balance between safety and production that day?"
      ],
      "information_sources": [
        "Which sources of information did you trust most in that shift, and why?"
      ],
      "alternatives": [
        "Looking back, what other options were realistically available at each of those points?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision at each step?"
      ],
      "prior_experience": [
        "Did anything from your past experience underground shape how you read these signals?"
      ],
      "time_pressure": [
        "How much did the production schedule affect the pace of your decisions?"
      ],
      "uncertainty": [
        "Where did you feel most uncertain, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the geotechnical engineer had been on-site the whole time, would anything have changed?",
        "If the hazard rating had come back at 3.5 instead of 2.3, what would you have done differently?",
        "Looking back, would you make the same call on continuing under the existing ground support plan?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "sqb_01",
        "bias": "Status quo bias",
        "decision_point": 1,
        "mechanism": "Manager defaults to the existing, unrevised ground support plan despite new seismic evidence, treating the cost/effort of deviation as decisive without directly weighing the new risk information",
        "affected_reasoning_operation": "Option evaluation under a default anchor",
        "evidence_available_at_time": [
          "Three above-baseline microseismic events overnight",
          "Ground support plan unrevised for four months",
          "Production two days behind schedule"
        ],
        "required_textual_manifestation": "Manager states or implies that changing the approved plan felt unnecessary/disruptive and that continuing as planned was the natural choice, without describing a substantive comparison of the new seismic data against the plan's original assumptions",
        "plausible_nonbias_interpretation": "The manager reasonably judged the plan still valid based on the absence of visible damage",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "default effect", "anchoring to existing plan"]
      },
      {
        "instance_id": "iv_01",
        "bias": "Illusion of validity",
        "decision_point": 2,
        "mechanism": "Manager treats the precise numeric hazard rating (2.3) as a reliable, well-calibrated predictor of localized risk despite the model's known blind spot and lack of site-specific validation",
        "affected_reasoning_operation": "Confidence calibration in a quantitative model output",
        "evidence_available_at_time": [
          "Numeric hazard rating of 2.3 labeled 'moderate but manageable'",
          "Known monitoring blind spot near the adjacent intersection",
          "Geotechnical engineer off-site"
        ],
        "required_textual_manifestation": "Manager describes treating the specific numeric rating as strong, decisive evidence of manageable risk, without acknowledging the model's blind-spot limitation as reducing confidence",
        "plausible_nonbias_interpretation": "The rating came from a credentialed remote model and represented the best available quantitative input at the time",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "model limitations", "false precision"]
      },
      {
        "instance_id": "iv_02",
        "bias": "Illusion of validity",
        "decision_point": 3,
        "mechanism": "Manager infers strong predictive confidence from the apparent coherence between the new crack pattern and a past Stope 9 case, treating narrative similarity as proof the pattern is benign rather than as one uncertain data point",
        "affected_reasoning_operation": "Pattern-matching against historical case as validation",
        "evidence_available_at_time": [
          "New hairline cracking in shotcrete",
          "Historical log of comparable Stope 9 crack pattern that resolved without a fall of ground",
          "Junior inspector's cautionary note"
        ],
        "required_textual_manifestation": "Manager expresses that because the crack pattern 'matched' Stope 9's history, this made the current situation predictable/understood, without noting how different one prior case is as a basis for confidence",
        "plausible_nonbias_interpretation": "Drawing on relevant precedent is a legitimate part of experienced judgment in ground control",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "pattern coherence", "overgeneralization from one case"]
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3,
        "mechanism": "Manager selectively forwards crew accounts that support the 'normal settling' hypothesis while filing away, without escalation, the junior inspector's dissenting recommendation",
        "affected_reasoning_operation": "Selective evidence transmission/weighting",
        "evidence_available_at_time": [
          "Two crew accounts describing cracking as typical settling",
          "Junior inspector's cautionary email recommending re-support"
        ],
        "required_textual_manifestation": "Manager describes choosing to pass along the reassuring crew reports to the superintendent while not raising or discussing the inspector's note on the shift call",
        "plausible_nonbias_interpretation": "Crew observations from people physically present may reasonably be weighted alongside a remote junior inspector's note",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "selective reporting", "cherry-picking evidence"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Confirmation Bias",
        "decision_point": 4,
        "mechanism": "Manager interprets an ambiguous, minor rock fall as further confirmation that ground conditions are stable, rather than as an update that should increase caution given the pending sensor data gap",
        "affected_reasoning_operation": "Interpretation of ambiguous new evidence relative to a prior belief",
        "evidence_available_at_time": [
          "Small unplanned rock fall near stope access drift",
          "Sensor lag delaying confirmed ground movement magnitude",
          "Prior belief that conditions were manageable"
        ],
        "required_textual_manifestation": "Manager frames the rock fall as consistent with/expected under the 'stable conditions' view rather than treating it as new evidence warranting reassessment, distinct from cb_01's evidence-selection act",
        "plausible_nonbias_interpretation": "Minor rock falls are common and can reasonably be treated as routine background risk",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "belief-consistent interpretation", "biased assimilation"]
      },
      {
        "instance_id": "ob_01",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Manager expresses high personal certainty in the decision to authorize the blast, citing 20 years of experience, while the objective uncertainty (sensor lag, unresolved crack report, superintendent pressure) remains substantial and unaddressed",
        "affected_reasoning_operation": "Self-assessed confidence in a judgment under incomplete information",
        "evidence_available_at_time": [
          "Sensor lag preventing confirmed data",
          "20 years of personal underground experience",
          "Production pressure from superintendent"
        ],
        "required_textual_manifestation": "Manager states strong personal certainty that the call was correct and downplays the significance of the missing sensor confirmation, without qualifying the confidence level against the actual gaps in evidence",
        "plausible_nonbias_interpretation": "Extensive experience is a legitimate basis for professional judgment under uncertainty",
        "strength": "moderate",
        "do_not_make_explicit": ["overconfidence bias", "miscalibrated certainty", "experience-based overconfidence"]
      },
      {
        "instance_id": "ab_01",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "Manager judges current risk as low primarily because a vivid, easily recalled recent event (Stope 9, six weeks earlier) resolved without incident, rather than referencing base-rate statistics on seismic-event escalation",
        "affected_reasoning_operation": "Risk judgment via recall of a salient prior instance",
        "evidence_available_at_time": [
          "Memory of the Stope 9 event cluster six weeks earlier",
          "Absence of readily recalled base-rate data on escalation frequency"
        ],
        "required_textual_manifestation": "Manager explains reassurance about the current rating mainly by referencing how the Stope 9 case turned out, without citing broader statistics or a wider sample of past events",
        "plausible_nonbias_interpretation": "Recent, directly relevant experience is often a reasonable input to operational judgment",
        "strength": "subtle",
        "do_not_make_explicit": ["availability bias", "recency effect", "salience of recalled event"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, no paired control is being generated in this specification"
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
      "Confirm exactly 7 total bias instances are embedded: 1 status quo, 2 illusion of validity, 2 confirmation bias, 1 overconfidence, 1 availability",
      "Confirm exactly 4 decision points, each with at least two plausible alternatives",
      "Confirm no bias-name vocabulary or explicit psychological labels appear in the interview text",
      "Confirm each instance has a distinct evidence trace and decision moment distinguishing it from any other instance of the same bias",
      "Confirm interview draft falls between 1,215 and 1,485 words, targeting 1,350",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm consequences described (stable shift outcome) do not mechanically prove or disprove bias presence",
      "Confirm no unrequested bias (e.g., anchoring, sunk cost) is intentionally embedded"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Status quo bias", "occurrences": 1, "mechanism_constraint": "Defaulting to unrevised ground support plan despite new seismic evidence"},
      {"bias": "Illusion of validity", "occurrences": 2, "mechanism_constraint": "Overconfidence in numeric model precision (DP2) and in narrative case-pattern coherence (DP3)"},
      {"bias": "Confirmation Bias", "occurrences": 2, "mechanism_constraint": "Selective evidence transmission (DP3) and belief-consistent interpretation of ambiguous new evidence (DP4)"},
      {"bias": "Overconfidence Bias", "occurrences": 1, "mechanism_constraint": "Miscalibrated personal certainty despite unresolved sensor gap and dissenting input"},
      {"bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Risk judgment anchored to a single vivid recalled prior event rather than base rates"}
    ],
    "target_bias_names": [
      "Status quo bias",
      "Illusion of validity",
      "Confirmation Bias",
      "Overconfidence Bias",
      "Availability Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Status quo bias", "requested_occurrences": 1},
      {"bias": "Illusion of validity", "requested_occurrences": 2},
      {"bias": "Confirmation Bias", "requested_occurrences": 2},
      {"bias": "Overconfidence Bias", "requested_occurrences": 1},
      {"bias": "Availability Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "sqb_01", "bias": "Status quo bias"},
      {"instance_id": "iv_01", "bias": "Illusion of validity"},
      {"instance_id": "iv_02", "bias": "Illusion of validity"},
      {"instance_id": "cb_01", "bias": "Confirmation Bias"},
      {"instance_id": "cb_02", "bias": "Confirmation Bias"},
      {"instance_id": "ob_01", "bias": "Overconfidence Bias"},
      {"instance_id": "ab_01", "bias": "Availability Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "sqb_01", "bias": "Status quo bias", "decision_point": 1},
      {"instance_id": "iv_01", "bias": "Illusion of validity", "decision_point": 2},
      {"instance_id": "ab_01", "bias": "Availability Bias", "decision_point": 2},
      {"instance_id": "iv_02", "bias": "Illusion of validity", "decision_point": 3},
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 3},
      {"instance_id": "cb_02", "bias": "Confirmation Bias", "decision_point": 4},
      {"instance_id": "ob_01", "bias": "Overconfidence Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sqb_01",
        "bias": "Status quo bias",
        "mechanism": "Default retention of existing ground support plan despite new seismic evidence, without substantive re-evaluation",
        "affected_reasoning_operation": "Option evaluation under a default anchor",
        "evidence_source": "Overnight microseismic logs vs. four-month-old approved plan",
        "distinctiveness_requirement": "Sole status quo instance; no other decision point may exhibit this mechanism"
      },
      {
        "instance_id": "iv_01",
        "bias": "Illusion of validity",
        "mechanism": "Overweighting precision of a numeric hazard rating despite known model blind spot",
        "affected_reasoning_operation": "Confidence calibration on quantitative model output",
        "evidence_source": "Remote geotechnical model's 2.3 rating",
        "distinctiveness_requirement": "Must be based on numeric/model precision, distinct from iv_02's case-pattern basis"
      },
      {
        "instance_id": "iv_02",
        "bias": "Illusion of validity",
        "mechanism": "Overweighting predictive confidence from apparent similarity to a single past case",
        "affected_reasoning_operation": "Pattern-matching against historical precedent as validation",
        "evidence_source": "Stope 9 historical crack-pattern log",
        "distinctiveness_requirement": "Must be based on case-pattern coherence, distinct from iv_01's numeric-model basis; different decision point"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective forwarding of belief-consistent crew reports while sidelining a dissenting inspector note",
        "affected_reasoning_operation": "Selective evidence transmission/weighting",
        "evidence_source": "Crew verbal reports vs. junior inspector's email",
        "distinctiveness_requirement": "Must be an evidence-selection/transmission act, distinct from cb_02's interpretation act; different decision point"
      },
      {
        "instance_id": "cb_02",
        "bias": "Confirmation Bias",
        "mechanism": "Interpreting an ambiguous new event (rock fall) as confirming a prior belief rather than as reason to reassess",
        "affected_reasoning_operation": "Belief-consistent interpretation of ambiguous evidence",
        "evidence_source": "Minor rock fall near stope access drift",
        "distinctiveness_requirement": "Must be an interpretation act on new evidence, distinct from cb_01's selective-transmission act; different decision point"
      },
      {
        "instance_id": "ob_01",
        "bias": "Overconfidence Bias",
        "mechanism": "Expressed high personal certainty in judgment despite unresolved sensor gap and unaddressed dissent",
        "affected_reasoning_operation": "Self-assessed confidence calibration under incomplete information",
        "evidence_source": "Manager's stated certainty vs. sensor lag and prior unresolved cautionary note",
        "distinctiveness_requirement": "Sole overconfidence instance; must be framed as self-certainty, not evidence interpretation"
      },
      {
        "instance_id": "ab_01",
        "bias": "Availability Bias",
        "mechanism": "Risk judgment anchored to one vivid, easily recalled past event rather than base-rate data",
        "affected_reasoning_operation": "Risk judgment via recall salience",
        "evidence_source": "Recalled Stope 9 event from six weeks prior",
        "distinctiveness_requirement": "Sole availability instance; must be recall-driven, distinct from iv_02's case-pattern illusion-of-validity framing"
      }
    ],
    "intended_strength": [
      {"instance_id": "sqb_01", "bias": "Status quo bias", "strength": "subtle"},
      {"instance_id": "iv_01", "bias": "Illusion of validity", "strength": "moderate"},
      {"instance_id": "iv_02", "bias": "Illusion of validity", "strength": "moderate"},
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle"},
      {"instance_id": "cb_02", "bias": "Confirmation Bias", "strength": "subtle"},
      {"instance_id": "ob_01", "bias": "Overconfidence Bias", "strength": "moderate"},
      {"instance_id": "ab_01", "bias": "Availability Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_7",
    "domain_id": "MU",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across decision points by mechanism fit and narrative realism: status quo bias placed solely at the initial anomaly-response decision (DP1); illusion of validity split between a numeric-model-trust manifestation (DP2) and a case-pattern-coherence manifestation (DP3) to ensure distinct evidence sources; confirmation bias split between a selective-transmission manifestation (DP3) and a belief-consistent-interpretation manifestation (DP4) to ensure distinct reasoning operations; overconfidence and availability bias each assigned a single instance at the decision points (DP4 and DP2 respectively) where personal certainty and recalled-precedent reasoning are most narratively plausible. No bias exceeds two occurrences at any single decision point, and no two occurrences of the same bias share both decision point and evidence source.",
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
        "segment_id": "dp1",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "The ground support plan for that stope had been signed off about four months earlier... We let day shift go in and start drilling as scheduled.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sqb_01"
        ],
        "ground_truth_rationale": "The participant defaults to the unrevised support plan despite above-baseline microseismic events and available inspection alternatives."
      },
      {
        "segment_id": "dp2",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "The model came back with a 2.3... Stope 9 was just the one that was fresh in my head... I authorized the afternoon blast clearance.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "iv_01",
          "ab_01"
        ],
        "ground_truth_rationale": "The participant treats a precise model rating as settled despite a known blind spot and relies on one vivid prior event instead of broader comparison."
      },
      {
        "segment_id": "dp3",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "I leaned toward the crew's read... The inspector's note got filed... because the Stope 9 comparison made the pattern seem like something we already understood.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "iv_02",
          "cb_01"
        ],
        "ground_truth_rationale": "The participant treats similarity to one prior crack pattern as validating and selectively transmits reassuring reports while sidelining dissent."
      },
      {
        "segment_id": "dp4",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "That rock fall didn't worry me much... it read to me as consistent with... minor settling... Twenty years gives you a feel for these things... I authorized the blast.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02",
          "ob_01"
        ],
        "ground_truth_rationale": "The participant interprets a minor rock fall as consistent with stability and expresses high confidence despite sensor lag and unresolved warning signs."
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
    "analysis_scope_note": "Analyzed the participant's reported reasoning and decisions for affirmatively evidenced cognitive bias mechanisms, without inferring bias from outcome or production pressure alone."
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
      "bias_definition": "Tendency to judge probability or risk based on how easily examples come to mind, rather than on a systematic analysis of all relevant cases or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting the 2.3 hazard rating against the recent Stope 9 comparison and authorizing the afternoon blast clearance.",
      "decision_point_description": "After receiving the 2.3 hazard rating, the participant judged whether the rating warranted stopping the blast or seeking additional comparative event data.",
      "affected_reasoning_operation": "Risk and likelihood assessment based on recall of a single comparable past case.",
      "bias_specific_mechanism": "The easily recalled, recent Stope 9 case dominated the participant's risk judgment because it was fresh from a recent handover, substituting for a broader base-rate comparison across other stopes.",
      "manifestation_in_interview": "The participant stated that Stope 9 was the first thing that came to mind and that he did not pull comparable events across other stopes because Stope 9 was fresh in memory.",
      "effect_on_reasoning_or_decision": "The available Stope 9 memory made the 2.3 rating feel more benign and supported the decision to authorize the afternoon blast rather than pursuing a broader risk analysis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The Stope 9 situation was actually the first thing that came to mind — it had come up on the shift handover just a few days earlier, almost the exact same rating and event cluster, and it had resolved completely fine, no incident.",
          "evidence_explanation": "This explicitly identifies an easily recalled, recent case as the primary reference point for evaluating the current hazard rating."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go pull the broader run of comparable events across other stopes to see how those had generally played out; Stope 9 was just the one that was fresh in my head, so that's what I went with.",
          "evidence_explanation": "This demonstrates the availability mechanism: a vivid, recent memory substituted for systematic base-rate information and directly shaped the decision."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged later that a broader run of comparable events could have been reviewed, but no contemporaneous correction was made.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved passages did not directly address the availability heuristic; label and mechanism are assigned from established cognitive-science knowledge without corpus evidence for this occurrence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment",
        "anchoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to rely heavily on an initial value or piece of information as an anchor and make insufficient adjustments from that anchor when evaluating later information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Treating the 2.3 hazard rating as sufficiently settled and authorizing the afternoon blast clearance.",
      "decision_point_description": "Once the geotech model returned a 2.3 rating, the participant decided whether to accept that rating as the basis for the blast decision or to adjust for the known blind spot and missing model coverage.",
      "affected_reasoning_operation": "Interpreting a specific numerical hazard rating and deciding whether additional adjustment or data collection was necessary.",
      "bias_specific_mechanism": "The official-looking 2.3 hazard rating served as an anchor; the participant treated it as a settled value and insufficiently adjusted for the known blind spot near the intersection where the array does not read well.",
      "manifestation_in_interview": "The participant described the 2.3 as specific and official-looking, which made it easy to treat as settled rather than testing it against the known blind spot.",
      "effect_on_reasoning_or_decision": "The anchored interpretation of 2.3 reduced perceived need to seek an updated rating or hold the blast for the engineer to return, contributing directly to blast clearance.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The 2.3 read as solid enough, and Stope 9 had gone fine under similar numbers, so I authorized the afternoon blast clearance.",
          "evidence_explanation": "The participant treated the initial rating as sufficiently reliable to justify action without obtaining an updated rating for the blind spot."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It came from the model, and it was specific and official-looking, which made it easy to treat as settled rather than something to test against the blind spot we already knew was there.",
          "evidence_explanation": "This directly demonstrates the anchoring process: the number's authoritative appearance anchored judgment and discouraged adjustment for a known data limitation."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that a 3.5 would have stopped him, which shows awareness that the number was highly influential, but this does not show contemporaneous adjustment for the blind spot.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The anchoring and adjustment heuristic is supported by the retrieved space-flight verification passage.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, and adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "People base estimates on an initial value and adjust insufficiently from that anchor when additional information emerges.",
          "relevance_to_this_occurrence": "The participant accepted the 2.3 rating as the initial anchor and made insufficient adjustment for the known blind spot, consistent with this mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "confirmation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in ways that confirm or support pre-existing beliefs or preferred conclusions while discounting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Weighing the junior inspector's re-support recommendation against crew assessments of typical post-blast settling.",
      "decision_point_description": "After hairline cracking was reported, the participant had to decide how to weigh the inspector's email recommendation against the crew's on-the-ground view and what to pass up to the production superintendent.",
      "affected_reasoning_operation": "Integration and weighting of conflicting safety evidence in a risk assessment and reporting decision.",
      "bias_specific_mechanism": "The participant preferentially weighted information consistent with the view that the cracking was routine and non-serious, while suppressing the disconfirming inspector recommendation that would have required re-support.",
      "manifestation_in_interview": "The participant reported leaning toward the crew's read, filing the inspector's note, and not raising it on the shift call because it would muddy an already clear picture.",
      "effect_on_reasoning_or_decision": "The disconfirming inspector recommendation was excluded from the immediate reporting to the superintendent, and the situation was represented as typical settling rather than as requiring further independent assessment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned toward the crew's read. We'd seen a very similar crack pattern in Stope 9 previously that never led anywhere.",
          "evidence_explanation": "This shows preferential acceptance of the crew's assessment as consistent with a past pattern the participant already treated as benign."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The inspector's note got filed — I didn't raise it on the shift call, mostly because it felt like it would just muddy a picture that already seemed clear enough from the people who were actually standing there.",
          "evidence_explanation": "This demonstrates suppression of disconfirming evidence and reliance on confirmatory sources to maintain the preferred assessment."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that the cracking could have been treated as inconclusive and subjected to an independent check, but no contemporaneous correction or escalation was made.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit cognitive-bias document provides relevant confirmation-bias support.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The accident report of flight JZA7795 (2015) which landed short of the runway in poor weather, found t influenced the false perception that the aircraft was in a stable condition, and the crew’s confirmation bias focussed on the factors that indicated the approach was safe while ignoring those that did no t.",
          "mechanism_supported_by_source": "Confirmation bias focuses attention on factors indicating the preferred safe or stable interpretation while ignoring factors that indicate otherwise.",
          "relevance_to_this_occurrence": "The participant similarly focused on crew assessments indicating routine settling and did not elevate the inspector's contradictory recommendation."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "overconfidence effect",
      "alternative_labels": [
        "overconfidence bias",
        "miscalibration"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final authorization of the next scheduled blast despite sensor lag and a small rockfall near the access drift.",
      "supporting_interview_quote": "But I was confident in the call. Twenty years gives you a feel for these things that a delayed sensor reading doesn't necessarily add to.",
      "plausible_mechanism": "Subjective confidence in experiential judgment may have exceeded the information available after the sensor data gap and the small rockfall.",
      "why_not_identified": "The transcript does not provide objective calibration evidence showing the confidence was miscalibrated, and the judgment could reflect a legitimate expert heuristic rather than a discrete bias mechanism."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation",
        "continuation bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Morning decision to continue with the approved ground support plan after microseismic events.",
      "supporting_interview_quote": "revising an approved plan on the back of three events felt like more disruption than the situation called for.",
      "plausible_mechanism": "Continued with the existing plan and interpreted the absence of visible damage as sufficient despite emerging microseismic risk cues.",
      "why_not_identified": "The decision may reflect legitimate operational and production considerations under uncertainty; a distinct bias-specific mechanism is not affirmatively isolated from ordinary plan stability and risk acceptance."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Production pressure and remote geotechnical support are structural/organizational factors that likely shaped decisions but were not classified as cognitive biases.",
    "The retrieved corpus had limited direct coverage of the availability heuristic and overconfidence effect.",
    "Some quotations contain OCR artifacts from the retrieved corpus passages, so source passages were quoted as retrieved rather than normalized."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Biased_7_Sonnet_on",
  "interview_id": "MU_Biased_7",
  "system_prompt_id": "Sonnet",
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
