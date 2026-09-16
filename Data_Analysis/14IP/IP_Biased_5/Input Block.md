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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
