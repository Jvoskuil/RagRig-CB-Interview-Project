You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time today. This is a cognitive task analysis interview — I'm just trying to understand how you actually worked through a real production issue, step by step, including what you knew at each point and how you decided what to do. Nothing here is evaluative of you personally, and I may ask you to reconstruct things in detail even if they seem obvious. Sound okay?

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
}}
- Hidden generation specification: {{"hidden_validation_specification": {
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
  }}}
- Validation report: {{VALIDATION_REPORT}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
