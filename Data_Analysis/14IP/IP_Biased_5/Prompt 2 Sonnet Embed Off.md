You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time today. This is a cognitive task analysis interview — I'm just trying to understand how you actually worked through a real production issue, step by step, including what you knew at each point and how you decided what to do. Nothing here is evaluative of you personally, and I may ask you to reconstruct things in detail even if they seem obvious. Sound okay?

Participant: Sure, happy to walk through it. I've got a good one — the Line 3 flash issue before the Meridian shipment a few weeks back.

Interviewer: Perfect. Before we get into the decisions, can you just describe the incident overall — what was the situation and what were you trying to achieve?

Participant: We run three shifts on Line 3, automotive interior clips for Meridian, and we had a 72-hour window to hit a shipment. Partway through a night shift, our scrap rate jumped from about 1.8% up to 6.4%, mostly flash defects, a few short shots mixed in. My objective was straightforward on paper — get quality back under 2% without blowing the ship date and without a full shutdown, since corporate wants VP sign-off for that and we didn't have time to chase approvals.

Interviewer: What were the first signs something was wrong?

Participant: Quality flagged the scrap numbers at shift change, and when I pulled the SPC chart, you could see cavity pressure had started drifting mid-shift. That's usually a decent early indicator. Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper.

Interviewer: So walk me through what you did with that first.

Participant: I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case. In hindsight, tooling wear was already flagged as a possibility by the tooling lead, but I didn't prioritize pulling that data until humidity came back clean.

Interviewer: What did you learn once the humidity results came in?

Participant: They were normal, well within range, so that ruled it out. That's when the tooling lead came back and said the mold had racked up wear cycles since the last inspection — more than we'd expected. So we lost a bit of time chasing the humidity angle before we got to the actual contributing factor.

Interviewer: If you'd had the pressure and wear data side by side from the start, would you have sequenced it differently?

Participant: Possibly. I think if I hadn't had that six-month-old case so fresh in mind, I might have pulled wear data in parallel instead of after.

Interviewer: Let's move to the fix itself. Once wear was confirmed, what were your options?

Participant: Wear was moderate, not severe. We had two real options — an incremental hold-pressure adjustment, which is lower risk but takes longer to validate, or a full mold-insert swap, which is more disruptive but felt like the more thorough fix. We had a press-down window shared with two other product runs, so timing was tight either way.

Interviewer: What tipped you toward the insert swap?

Participant: Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that. When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted.

Interviewer: Did you compare the wear numbers to your swap criteria directly?

Participant: Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing.

Interviewer: What happened after the swap?

Participant: It got done inside the window, which was good. But results were partial — scrap improved but didn't fully get back to baseline, so there was still something unresolved.

Interviewer: Let's go to the third point — the sister-plant call.

Participant: Right, around day two our quality engineer was out sick, so I had less statistical support than I wanted. I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network.

Interviewer: What did you decide?

Participant: I adopted it. Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out.

Interviewer: Did you consider waiting for that validation, or a modified version?

Participant: I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally.

Interviewer: What came out of that?

Participant: Short-term, flash defects dropped, which felt like a win. But two shifts later we started seeing a new warping issue on a subset of parts that hadn't shown up before.

Interviewer: Let's get to the final decision — the rollout call.

Participant: Right, so by the time Meridian's deadline was closing in, our most recent shift — the last eight hours — showed scrap down to 1.5%, best number we'd seen in four days. Corporate quality asked whether we should roll the fix out to Lines 4 and 6 as well.

Interviewer: What was your reasoning?

Participant: Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines.

Interviewer: How did that stack up against the full four-day trend?

Participant: The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call.

Interviewer: Did the warping incident factor into your confidence level at that point?

Participant: Less than it probably should have, looking back. I was focused on getting a clean answer to corporate fast.

Interviewer: What happened with the rollout?

Participant: Lines 4 and 6 looked fine initially, but one of them later threw a tooling alarm we hadn't seen before. And a fuller week-long review afterward showed the wear-related root cause was only partly addressed, not fully resolved like I'd said.

Interviewer: If the last shift's numbers had come in worse instead of better, do you think you'd have made the same call?

Participant: No, honestly, probably not — I think that reading was a big part of why I felt ready to greenlight it.

Interviewer: What would you do differently if this happened again?

Participant: Pull wear and pressure data in parallel from the start instead of chasing the familiar explanation first. And probably wait for a full trend view, not just the best shift, before telling corporate we were done.

Interviewer: This has been really useful — thank you for walking through it in this much detail.

Participant: No problem, happy to help.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IP_Biased_5",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Plant/Industrial Production Manager",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Line 3 Flash Defect Spike Before the Meridian Shipment",
    "scenario_summary_internal": "A plant manager at a mid-size injection molding facility must diagnose and correct a sudden rise in flash/short-shot defects on Line 3 in the four days before a large customer (Meridian Automotive) shipment deadline. The manager must balance throughput, scrap cost, and quality risk while under time pressure, incomplete sensor data, and pressure from corporate and sister-plant precedent. The narrative follows four sequential decision points: initial root-cause diagnosis, selection of a corrective fix, adoption of a plant-wide standard proposed by peers, and the final call to scale the fix to two additional lines before shipment.",
    "occupational_realism": {
      "objective": "Restore Line 3 output to spec-compliant quality (scrap rate back under 2%) in time to fulfill the Meridian shipment without triggering a full line shutdown or missing the ship date.",
      "setting": "A 24/7 mid-size automotive-parts injection molding plant running three shifts, with a quality lab, a maintenance/tooling team, and a corporate quality network linking four sister plants.",
      "constraints": [
        "72-hour window before the Meridian shipment must ship",
        "Limited access to the sister plant's full defect log, only a summary shared in a call",
        "Tooling change requires a scheduled press-down window shared with two other product runs",
        "Quality engineer is out sick during the second day, reducing statistical support",
        "Corporate directive discourages full-line shutdowns without VP sign-off"
      ],
      "stakeholders": [
        "Plant/Industrial Production Manager (interviewee)",
        "Shift supervisors (Shift A, B, C)",
        "Quality engineer",
        "Tooling/maintenance lead",
        "Sister-plant production manager (peer)",
        "Corporate quality director",
        "Meridian Automotive account representative"
      ],
      "technical_terms_to_use": [
        "flash defect",
        "short shot",
        "cycle time",
        "scrap rate",
        "mold cavity pressure",
        "resin lot",
        "tooling wear",
        "SPC chart",
        "press-down window",
        "hold pressure"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "anchoring",
        "availability heuristic",
        "bandwagon",
        "overconfidence",
        "recency effect",
        "heuristic",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Scrap rate on Line 3 jumped from 1.8% to 6.4% over the last 12-hour shift",
          "SPC chart shows a cavity-pressure drift starting mid-shift",
          "Six months earlier, a nearly identical defect pattern was traced to ambient humidity affecting resin drying",
          "Current humidity readings are within normal range and have not been checked yet"
        ],
        "new_information_after_decision": [
          "Humidity logs come back normal, ruling out the prior cause",
          "Tooling lead flags that the mold has accumulated wear cycles since the last inspection"
        ],
        "alternatives": [
          "Order an immediate humidity/resin-drying check based on the prior incident pattern",
          "Pull current cavity-pressure and tooling-wear data before assuming a cause",
          "Run a short diagnostic mold-inspection alongside a parallel resin check"
        ],
        "intended_action": "Manager directs the team to first re-check drying/humidity conditions because 'this looks just like the case from six months ago,' delaying the tooling-wear check."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tooling wear confirmed as a contributing factor; wear is moderate, not severe",
          "Two candidate fixes exist: incremental hold-pressure adjustment (lower risk, slower to validate) or a full mold-insert swap (faster perceived fix, requires press-down window)",
          "Three months ago, a widely discussed insert failure on Line 5 caused a two-day shutdown and was the subject of a plant-wide safety debrief that is still fresh in staff conversation"
        ],
        "new_information_after_decision": [
          "The insert swap is completed within the available press-down window",
          "Early results show partial improvement but scrap rate does not fully return to baseline"
        ],
        "alternatives": [
          "Choose the insert swap, citing the memorable Line 5 case as the reason for urgency",
          "Choose the incremental hold-pressure adjustment and monitor over several cycles",
          "Run both a small-scale hold-pressure trial and schedule the swap as a contingency"
        ],
        "intended_action": "Manager selects the full insert swap, explaining the decision mainly by referencing how vividly the Line 5 insert failure is remembered by the team, rather than by comparing current wear severity data against swap thresholds."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A call with the sister-plant manager reveals that three of the four sister plants adopted a standardized 'aggressive cooling time reduction' protocol for similar flash issues",
          "The plant's own quality engineer (now back) has not yet independently validated whether cooling-time reduction fits Line 3's specific resin lot and cavity geometry",
          "Corporate quality director mentions the protocol is becoming the informal network standard"
        ],
        "new_information_after_decision": [
          "Applying the cooling-time reduction produces a short-term drop in flash defects",
          "A new, unrelated warping issue emerges on a subset of parts two shifts later"
        ],
        "alternatives": [
          "Adopt the cooling-time reduction protocol because most sister plants are already using it",
          "Request the quality engineer validate the protocol against Line 3's specific resin lot before adopting",
          "Adopt a modified, more conservative version of the protocol pending local validation"
        ],
        "intended_action": "Manager adopts the sister-plant protocol largely because it is already the shared practice across the network, without waiting for the quality engineer's line-specific validation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The most recent shift (last 8 hours) shows scrap rate down to 1.5%, the best reading in four days",
          "The full four-day trend, including the warping issue from phase 3, is more mixed and shows only 2.9% average improvement with unresolved variability",
          "Meridian shipment must be finalized within hours, and the corporate quality director is asking whether the fix should be rolled out to Lines 4 and 6"
        ],
        "new_information_after_decision": [
          "Lines 4 and 6 initially show improvement, but one line later reports a new tooling alarm not previously seen",
          "A fuller week-long data review shows the underlying wear-related root cause was only partially addressed"
        ],
        "alternatives": [
          "Approve immediate rollout to Lines 4 and 6 based on the strong latest-shift numbers",
          "Request one more full day of Line 3 data across all shifts before recommending rollout",
          "Approve a limited pilot rollout to one additional line with added monitoring"
        ],
        "intended_action": "Manager expresses high confidence that the root cause is fully resolved and approves rollout to both additional lines, citing the strong last-shift numbers as sufficient proof, while downplaying the more mixed multi-day trend and the earlier warping incident."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first indicated something was wrong on Line 3?",
        "What was your primary objective when you were first notified?"
      ],
      "timeline_reconstruction": [
        "What happened right after you were told about the scrap rate spike?",
        "Walk me through the sequence of checks, calls, and decisions over the four days.",
        "What information came in after each major decision, and how did it change things?"
      ],
      "decision_point_probes": [
        "At that moment, what options did you consider, and why did you rule the others out?",
        "What evidence or past experience were you drawing on when you made that call?",
        "Who else was involved, and how much did their input shape your decision?",
        "Looking back, what information did you have available that you didn't use, or used less than others?"
      ],
      "closing_hypotheticals": [
        "If the sister plants had not shared their protocol, would your approach have been different?",
        "If the last shift's numbers had looked worse instead of better, would you have made the same rollout call?",
        "What would you do differently if a similar defect spike happened again next quarter?",
        "How much uncertainty did you feel you were operating under at each stage, in hindsight?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Initial diagnostic hypothesis is fixed on the six-month-old humidity/resin-drying cause because of surface similarity, and subsequent inquiry is organized around confirming or ruling out that anchor before considering other current evidence (tooling wear) already partially available.",
        "affected_reasoning_operation": "Initial hypothesis formation and information-gathering sequencing",
        "evidence_available_at_time": [
          "SPC cavity-pressure drift data",
          "Prior six-month-old humidity-related incident",
          "Untouched current humidity readings"
        ],
        "required_textual_manifestation": "Manager states the pattern 'looks just like' the earlier case and orders the humidity check first, delaying the tooling-wear check despite pressure data being available.",
        "plausible_nonbias_interpretation": "Checking a known prior cause first is a reasonable triage step given limited time.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchoring", "cognitive bias", "heuristic"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Heuristic",
        "decision_point": 2,
        "mechanism": "The choice of corrective fix is driven by how memorable and recently-discussed the Line 5 insert failure is, rather than by comparing current wear-severity data against objective swap-versus-adjustment thresholds.",
        "affected_reasoning_operation": "Option evaluation and justification for corrective action",
        "evidence_available_at_time": [
          "Confirmed moderate (not severe) tooling wear",
          "Two candidate fixes with different risk/time profiles",
          "Recent, widely-discussed Line 5 insert failure and debrief"
        ],
        "required_textual_manifestation": "Manager justifies choosing the full insert swap primarily by referencing how vivid and recent the Line 5 case is in staff memory, rather than citing wear-severity thresholds.",
        "plausible_nonbias_interpretation": "Choosing the faster, more thorough fix is a reasonable risk-averse choice given schedule pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability heuristic", "cognitive bias", "vividness"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Bandwagon effect",
        "decision_point": 3,
        "mechanism": "Adoption of the cooling-time reduction protocol is driven mainly by the fact that most sister plants and the corporate network already treat it as standard practice, ahead of the plant's own line-specific validation being completed.",
        "affected_reasoning_operation": "Selection of a corrective standard/protocol under social/organizational consensus",
        "evidence_available_at_time": [
          "Sister-plant adoption reported by peer manager",
          "Corporate framing of protocol as emerging network standard",
          "Quality engineer's validation not yet completed"
        ],
        "required_textual_manifestation": "Manager cites the fact that three of four sister plants already use the protocol as the main reason for adopting it now, ahead of local validation.",
        "plausible_nonbias_interpretation": "Leveraging proven practice from sister plants is a legitimate way to save diagnostic time under a deadline.",
        "strength": "moderate",
        "do_not_make_explicit": ["bandwagon", "social proof", "cognitive bias"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Recency effect",
        "decision_point": 4,
        "mechanism": "The rollout decision is disproportionately weighted toward the most recent 8-hour shift's strong numbers, while the more mixed four-day trend, including the intervening warping issue, is discounted in the manager's stated reasoning.",
        "affected_reasoning_operation": "Weighting of sequential performance data when forming a judgment of resolution",
        "evidence_available_at_time": [
          "Most recent shift's low scrap rate (1.5%)",
          "Four-day trend showing mixed results (2.9% average, unresolved variability)",
          "Prior warping incident from phase 3"
        ],
        "required_textual_manifestation": "Manager foregrounds the latest shift's numbers as the key evidence for resolution while giving comparatively little weight to the multi-day trend and the warping incident when explaining the basis for the decision.",
        "plausible_nonbias_interpretation": "The latest shift is the freshest and most direct evidence of whether the fix is working.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "cognitive bias", "weighting"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "The manager expresses high certainty that the root cause is fully resolved and approves rollout to two additional lines, exceeding what the available multi-day, multi-line evidence supports, and without acknowledging the earlier partial-improvement and warping signals as sources of uncertainty.",
        "affected_reasoning_operation": "Confidence calibration in final causal judgment and generalization decision",
        "evidence_available_at_time": [
          "Partial improvement noted after the insert swap (phase 2)",
          "Warping issue emerging after protocol adoption (phase 3)",
          "Only one strong shift of data supporting full resolution"
        ],
        "required_textual_manifestation": "Manager states strong certainty ('this has fully resolved it') and approves rollout to both additional lines without qualifying the claim against the mixed evidence already known at that point.",
        "plausible_nonbias_interpretation": "A production manager under deadline pressure may reasonably need to make a decisive call with available data.",
        "strength": "moderate",
        "do_not_make_explicit": ["overconfidence", "cognitive bias", "calibration"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition scenario with no paired control specified in this request."
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
      "Verify exactly 5 total intended bias instances are embedded, one per manifest entry.",
      "Verify each instance is tied to a distinct decision point and evidence source, with cb_04 and cb_05 both at decision point 4 but drawing on different evidence operations (trend-weighting vs. confidence calibration).",
      "Verify no bias name, definition, or psychological label appears in probes or narrative text.",
      "Verify exactly four decision points, each with at least two plausible alternatives.",
      "Verify consequences at each decision point do not mechanically confirm or deny whether the decision was biased.",
      "Verify total narrative length target of 1,350 words (range 1,215-1,485) is achievable without repetitive exposition, given four decision points and moderate probe density.",
      "Verify probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Bandwagon effect",
        "occurrences": 1,
        "mechanism_constraint": "Must be driven by sister-plant/network adoption pressure preceding local validation, at decision point 3."
      },
      {
        "bias": "Recency effect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve overweighting the most recent shift's data relative to the fuller multi-day trend, at decision point 4."
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve stated certainty exceeding what available mixed evidence supports, at decision point 4, distinct from the recency-weighting mechanism."
      },
      {
        "bias": "Availability Heuristic",
        "occurrences": 1,
        "mechanism_constraint": "Must be driven by vividness/memorability of the Line 5 insert failure rather than objective wear-severity data, at decision point 2."
      },
      {
        "bias": "Anchoring Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must be driven by surface similarity to a prior six-month-old incident shaping initial hypothesis and inquiry order, at decision point 1."
      }
    ],
    "target_bias_names": [
      "Bandwagon effect",
      "Recency effect",
      "Overconfidence Bias",
      "Availability Heuristic",
      "Anchoring Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Recency effect", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 },
      { "bias": "Availability Heuristic", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Anchoring Bias" },
      { "instance_id": "cb_02", "bias": "Availability Heuristic" },
      { "instance_id": "cb_03", "bias": "Bandwagon effect" },
      { "instance_id": "cb_04", "bias": "Recency effect" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Availability Heuristic", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Bandwagon effect", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Recency effect", "decision_point": 4 },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Anchoring Bias",
        "mechanism": "Initial diagnosis fixed on surface similarity to a six-month-old prior incident, shaping inquiry order ahead of available tooling-wear data.",
        "affected_reasoning_operation": "Initial hypothesis formation and information-gathering sequencing",
        "evidence_source": "SPC pressure data and prior incident record",
        "distinctiveness_requirement": "Only intended anchoring instance; occurs at decision point 1 only."
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Heuristic",
        "mechanism": "Fix selection driven by vividness/recency of the Line 5 insert failure narrative rather than current wear-severity data comparison.",
        "affected_reasoning_operation": "Option evaluation and justification for corrective action",
        "evidence_source": "Staff recollection of Line 5 debrief vs. current wear-severity data",
        "distinctiveness_requirement": "Only intended availability instance; occurs at decision point 2 only; distinct from recency effect at decision point 4, which concerns weighting of sequential performance data, not memorability of a past event."
      },
      {
        "instance_id": "cb_03",
        "bias": "Bandwagon effect",
        "mechanism": "Protocol adoption driven by sister-plant/network consensus ahead of local, line-specific validation.",
        "affected_reasoning_operation": "Selection of corrective standard under social/organizational consensus",
        "evidence_source": "Peer manager report of sister-plant adoption and corporate framing",
        "distinctiveness_requirement": "Only intended bandwagon instance; occurs at decision point 3 only."
      },
      {
        "instance_id": "cb_04",
        "bias": "Recency effect",
        "mechanism": "Rollout judgment disproportionately weighted toward the most recent shift's numbers versus the fuller multi-day trend.",
        "affected_reasoning_operation": "Weighting of sequential performance data in forming a resolution judgment",
        "evidence_source": "Most recent shift data vs. four-day trend data",
        "distinctiveness_requirement": "Only intended recency instance; occurs at decision point 4; distinct from overconfidence instance (cb_05), which concerns certainty calibration rather than data-weighting order."
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "mechanism": "Stated certainty of full resolution and rollout approval exceeds what mixed multi-line, multi-day evidence supports.",
        "affected_reasoning_operation": "Confidence calibration in causal judgment and generalization decision",
        "evidence_source": "Partial-improvement and warping signals from phases 2-3 vs. stated certainty",
        "distinctiveness_requirement": "Only intended overconfidence instance; occurs at decision point 4; distinct from recency instance (cb_04) via focus on certainty level rather than data-weighting mechanism."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Availability Heuristic", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Bandwagon effect", "strength": "moderate" },
      { "instance_id": "cb_04", "bias": "Recency effect", "strength": "subtle" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IP_Biased_5",
    "domain_id": "IP",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across four decision points by mechanism fit and narrative realism: one bias per decision point at DP1-DP3, and two distinct biases (Recency effect, Overconfidence Bias) co-located at DP4 using different evidence sources and reasoning operations (data-weighting order vs. certainty calibration), consistent with the no-more-than-two-per-point and distinct-evidence-source rules.",
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
          "segment_type": "goal_and_constraint_setting",
          "raw_interview_anchor": "Objective to restore quality under 2% before shipment without a full shutdown.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Substantive operational objective and constraint rationale, but no hidden bias manifestation."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "initial_hypothesis_and_information_gathering",
          "raw_interview_anchor": "The symptom pattern looked almost identical to the six-month-old humidity case; humidity and drying were checked first while tooling-wear data was delayed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "The prior case shaped the initial hypothesis and inquiry order ahead of currently available tooling and pressure evidence."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "evidence_update_and_cause_revision",
          "raw_interview_anchor": "Humidity was normal, so the manager moved to the tooling-lead information about accumulated wear cycles.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a non-biased update after the first check and does not introduce a separate hidden occurrence."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "option_comparison",
          "raw_interview_anchor": "Moderate wear left two options: incremental hold-pressure adjustment or a more disruptive full insert swap.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant lays out candidate fixes and their risk/time profiles without yet manifesting a hidden bias."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "corrective_action_selection",
          "raw_interview_anchor": "The vivid Line 5 insert failure remained on everyone's mind and pushed the manager toward the swap more than a comparison to current wear thresholds.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_02"
          ],
          "ground_truth_rationale": "The memorable prior failure displaced objective comparison of current wear severity in the fix-selection rationale."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "post_action_assessment",
          "raw_interview_anchor": "The swap finished within the window, but scrap improved only partially and something remained unresolved.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a consequence assessment, not a distinct hidden bias manifestation."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "protocol_adoption_decision",
          "raw_interview_anchor": "Three of four sister plants used aggressive cooling-time reduction, which gave confidence to adopt it despite no local validation against the resin lot and cavity geometry.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_03"
          ],
          "ground_truth_rationale": "Network adoption and corporate standardization were used as the main basis for adoption ahead of line-specific validation."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "post_protocol_assessment",
          "raw_interview_anchor": "Flash defects dropped in the short term, but a new warping issue appeared two shifts later.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The new issue is a reported consequence and is not itself a separate hidden occurrence."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "rollout_confidence_and_communication",
          "raw_interview_anchor": "The latest shift's 1.5% scrap rate made the manager feel they had nailed it; the manager told corporate the root cause was resolved and approved rollout to Lines 4 and 6.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_05"
          ],
          "ground_truth_rationale": "The manager expressed certainty of full resolution and generalized the fix despite mixed evidence already available."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "sequential_data_weighting",
          "raw_interview_anchor": "The manager acknowledged a messier 2.9% four-day average and warping, but treated the last shift as real proof that the issue had turned around.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_04"
          ],
          "ground_truth_rationale": "The latest shift was given disproportionate weight relative to the fuller trend and intervening contradictory signal."
        },
        {
          "segment_id": "seg_011",
          "speaker": "Participant",
          "segment_type": "retrospective_uncertainty_assessment",
          "raw_interview_anchor": "The manager acknowledged that warping affected confidence less than it should have and was focused on giving corporate a quick clean answer.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is retrospective acknowledgment of the already mapped recency mechanism, not a distinct hidden occurrence."
        },
        {
          "segment_id": "seg_012",
          "speaker": "Participant",
          "segment_type": "future_process_improvement",
          "raw_interview_anchor": "In a future incident, the manager would pull wear and pressure data in parallel and wait for a full trend before declaring the issue resolved.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a corrective hindsight recommendation rather than an additional manifested hidden occurrence."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Strictly transcript-grounded bias identification; no retrieved corpus context was available, so labels and mechanisms rely on general cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "Bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Recency bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments and decisions are influenced by how easily instances or associations come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial diagnosis of the Line 3 scrap-rate increase",
      "decision_point_description": "Deciding which diagnostic checks to prioritize first when scrap rates rose.",
      "affected_reasoning_operation": "Causal hypothesis generation and diagnostic information-seeking",
      "bias_specific_mechanism": "A salient recent incident with similar symptoms came easily to mind and led the participant to over-prioritize humidity/drying checks as the likely cause, while not initially pulling available pressure and tooling wear data.",
      "manifestation_in_interview": "The participant immediately interpreted the current flash defects as almost identical to a six-month-old humidity case and directed the team to check drying conditions and humidity logs first. He explicitly said the prior case was fresh in his mind and that this likely caused him to sequence tooling wear data later.",
      "effect_on_reasoning_or_decision": "It narrowed the initial diagnostic pathway toward humidity, delayed tooling wear investigation, and produced lost time when humidity results came back normal.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper.",
          "evidence_explanation": "This shows the immediate availability-driven retrieval of a prior similar case as the primary causal hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case. In hindsight, tooling wear was already flagged as a possibility by the tooling lead, but I didn't prioritize pulling that data until humidity came back clean.",
          "evidence_explanation": "The participant acted on the easily recalled previous cause rather than the currently available pressure data and tooling-lead warning, demonstrating that recall of the prior case shaped information-seeking."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think if I hadn't had that six-month-old case so fresh in my mind, I might have pulled wear data in parallel instead of after.",
          "evidence_explanation": "This directly attributes the diagnostic sequencing to the salience of the prior case, confirming the availability mechanism."
        }
      ],
      "correction_or_counterevidence": "Humidity results were normal, ruling out the initially favored cause, and the tooling lead had contemporaneously flagged tooling wear. The participant later acknowledged he would pull wear and pressure data in parallel next time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided, so this established label and mechanism are based on general cognitive-science knowledge rather than retrieved source support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments and decisions are influenced by how easily instances or associations come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of the mold-insert swap over the hold-pressure adjustment",
      "decision_point_description": "Choosing between a lower-risk hold-pressure adjustment and a more disruptive full mold-insert swap.",
      "affected_reasoning_operation": "Risk evaluation and treatment option selection",
      "bias_specific_mechanism": "The vivid, recent Line 5 insert-failure event came easily to mind during risk evaluation and outweighed a direct comparison of current wear severity against swap criteria.",
      "manifestation_in_interview": "While weighing the two options, the participant kept recalling the Line 5 insert failure and the resulting two-day shutdown. He said this case pushed him toward the insert swap more than a strict comparison of current wear severity against the threshold for a swap would have warranted.",
      "effect_on_reasoning_or_decision": "The participant selected the more aggressive insert swap without rigorously comparing wear numbers to decision criteria, and the later review showed the root cause was only partly addressed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that.",
          "evidence_explanation": "This demonstrates that a salient prior failure was mentally prominent during the current risk evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted.",
          "evidence_explanation": "The participant explicitly states that the recalled case influenced the decision more than the relevant current wear data, which is the availability mechanism operating on risk assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing.",
          "evidence_explanation": "This confirms the participant did not compare the wear numbers directly to decision criteria, allowing the recalled prior case to drive the choice."
        }
      ],
      "correction_or_counterevidence": "Time pressure from the press-down window was also present, but the participant's own explanation identifies the recalled Line 5 case as the dominant influence. No contemporaneous correction occurred before the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided, so this established label and mechanism are based on general cognitive-science knowledge rather than retrieved source support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Bandwagon effect",
      "alternative_labels": ["Social proof", "Herd behavior"],
      "taxonomy_status": "established_label",
      "bias_definition": "A social-influence bias in which adoption or belief is driven by prevalence among peers rather than independent evaluation of local evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Adoption of the sister-plant cooling-time reduction protocol",
      "decision_point_description": "Deciding whether to adopt the network cooling-time reduction protocol locally without full in-house validation.",
      "affected_reasoning_operation": "Evaluation of intervention appropriateness and local risk",
      "bias_specific_mechanism": "The number of sister plants already using the protocol was treated as strong evidence that it would work locally, reducing the perceived need for validation against local resin lot and cavity geometry.",
      "manifestation_in_interview": "The participant heard that three of four sister plants had adopted an aggressive cooling-time reduction protocol and that corporate quality was framing it as standard. He adopted it primarily because of that prevalence, despite lacking in-house statistical support to validate it locally.",
      "effect_on_reasoning_or_decision": "The participant implemented the protocol without local validation. Flash defects dropped initially, but a new warping issue later emerged.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network.",
          "evidence_explanation": "This establishes that adoption by other plants and corporate framing were the key inputs to the decision, rather than local technical analysis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out.",
          "evidence_explanation": "The participant directly states that the prevalence of adoption across plants drove his confidence, which is the bandwagon/social-proof mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally.",
          "evidence_explanation": "The participant equated widespread adoption with lower risk, reinforcing that peer prevalence outweighed independent local validation."
        }
      ],
      "correction_or_counterevidence": "The participant considered a more conservative version but rejected it because of how many plants were already using the protocol. The later warping issue suggests local validation would have been informative.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided, so this established label and mechanism are based on general cognitive-science knowledge rather than retrieved source support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Recency bias",
      "alternative_labels": ["Recency effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which recent observations are weighted more heavily than older or aggregate information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final rollout confidence judgment for Lines 4 and 6",
      "decision_point_description": "Deciding whether to approve rollout of the fix to Lines 4 and 6 based on recent line performance.",
      "affected_reasoning_operation": "Trend evaluation, confidence calibration, and generalization decision",
      "bias_specific_mechanism": "The participant overweighted the most recent favorable shift result and underweighted the broader four-day trend and the prior warping incident when judging whether the root cause was resolved.",
      "manifestation_in_interview": "After a final eight-hour shift showed scrap at 1.5%, the participant declared confidence that the root cause was resolved and approved rollout, despite a messier four-day trend averaging around 2.9% and a warping issue from the previous day.",
      "effect_on_reasoning_or_decision": "The participant approved rollout to Lines 4 and 6 based heavily on one favorable recent shift. A later review showed the root cause was only partly addressed, and one line later threw a tooling alarm.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines.",
          "evidence_explanation": "The participant's confidence and rollout decision were anchored to the most recent shift's numbers, demonstrating recency-weighting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call.",
          "evidence_explanation": "This explicitly shows the participant favoring the recent data point over the broader trend and contradictory evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Less than it probably should have, looking back. I was focused on getting a clean answer to corporate fast.",
          "evidence_explanation": "This reveals that the prior warping incident was underweighted in the final confidence judgment, consistent with recency-driven narrowing on the latest shift."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, honestly, probably not — I think that reading was a big part of why I felt ready to greenlight it.",
          "evidence_explanation": "The participant admits the final decision depended heavily on the favorable last-shift reading rather than a more complete trend evaluation."
        }
      ],
      "correction_or_counterevidence": "The broader trend and warping incident were available to the participant but were down-weighted during the decision. Later tooling and week-long review findings provided external correction after the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided, so this established label and mechanism are based on general cognitive-science knowledge rather than retrieved source support.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided in this analysis, so bias labels, definitions, and mechanisms rely on general cognitive-science knowledge rather than retrieved source support.",
    "The transcript is a retrospective self-report, so some reasoning descriptions may be reconstructive rather than contemporaneous."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IP_Biased_5_Sonnet_off",
  "interview_id": "IP_Biased_5",
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
