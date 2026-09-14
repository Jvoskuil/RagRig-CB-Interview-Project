You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just so you know, I'll ask you to walk through a specific turnaround and explain your thinking as it unfolded, not just what ended up happening. Can you tell me your role and a bit about your background?

Participant: Sure. I've been a load controller about nine years, mostly narrow-body combi work. Normally I build the load sheet, issue the loading instruction to the ramp, check weight and balance against structural limits, and finalize the NOTOC for the captain. This one wasn't a normal turn, though—the inbound aircraft came in late, so instead of our usual 45 minutes on the ground, we were looking at more like 30 before the slot.

Interviewer: How did that change things going in?

Participant: Right away I knew I'd be compressing steps I'd normally spread out a bit more. Nothing about the flight itself was unusual—same route, same aircraft type—it was just less time to work with.

Interviewer: Walk me through what happened.

Participant: I got the cargo manifest with about 30 minutes left. Mixed load—regular bags, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what typically goes through, not palletized. Our load-control software generates an automatic load instruction, and it put that machinery item into hold 3. That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately. About fifteen minutes later, the ramp called and said the aircraft was sitting slightly tail-heavy—not out of limits, just aft of where you'd expect.

Interviewer: What did you do with that?

Participant: Logged it and kept going, because right then an LMC came in—about 380 kilos of mail plus six late bags that missed the original manifest. That mail got assigned to hold 5, our aft bulk hold. With the time we had left, I looked at the total weight, saw it was in line with the LMCs we'd been getting all week on this route—three similar ones, same range, none of those needed redistribution—and cleared it on that basis so I could move to the trim sheet.

Interviewer: And the trim sheet itself?

Participant: I pulled the dispatch log for a quick check, given the tail-heavy call from the ramp. Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required.

Interviewer: Let's go through each of those moments in more detail. Starting with the ALI and the machinery item—what specifically told you it was fine to run with as generated?

Participant: Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me.

Interviewer: Was there a manual chart you could have checked against for that kind of cargo?

Participant: There is, for exactly that situation. I know where it is. I just didn't reach for it that day.

Interviewer: What would have made you stop and pull it?

Participant: If we'd had the full 45, probably. Or if the system itself had thrown some kind of flag saying this needs manual sign-off. Neither of those happened, so I treated it like any other ALI.

Interviewer: On the LMC—what exactly did you compare when the mail and bags came in?

Participant: Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest.

Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs went?

Participant: No, not specifically. The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it.

Interviewer: What would it have taken to run that calculation directly?

Participant: A few extra minutes at the trim computer. It wasn't unavailable to me. I just didn't think it was worth the time against the schedule we were on.

Interviewer: On the trim sheet redistribution—how did you connect the two previous flights to this one?

Participant: They were on the same rotation, back to back, and both needed aft correction. Two in a row felt like it meant something about how the rotation was running that day, so I built in a forward shift before signing off, and honestly, with the time we had left, I didn't feel like there was room to dig into it further.

Interviewer: What did your own calculated index for this flight show on its own?

Participant: It was fine—within the normal forward range with margin. The redistribution wasn't because my numbers were bad. It was more that seeing two prior aft trims made me not fully trust it, and I didn't have the minutes to sit with that discomfort.

Interviewer: Did you find out afterward why those two flights ran tail-heavy?

Participant: Yeah—one was a fuel imbalance, the other had extra catering loaded late. Different tails, unrelated causes. Nothing tying them to each other or to this flight.

Interviewer: Last one—the final sign-off. What was the situation?

Participant: Closeout figures looked clean, within limits. But the ramp tally was one bag short of the NOTOC and manifest. Small discrepancy, and the slot was closing faster than a normal turn would allow.

Interviewer: What did you decide, and what were you weighing?

Participant: I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself. It turned out to be a manifest correction afterward—the weight and balance conclusion didn't change. I can see someone holding a couple minutes to chase it down instead. Neither call feels obviously wrong to me.

Interviewer: How confident were you in each of these at the time, versus now?

Participant: The ALI and the LMC, fairly confident in the moment, more than I'd be now looking back. The trim redistribution, less sure even then—it felt like caution more than certainty. The sign-off, I'm still not positive I made the better call, but I don't think it was unreasonable given the time.

Interviewer: If you'd had the full 45 minutes instead of 30, would you have handled the machinery cargo differently?

Participant: Probably, yes. I think I'd have pulled the manual chart. The shorter window is what pushed me to just trust the system's history instead.

Interviewer: If the mail had gone to the usual forward hold instead of hold 5?

Participant: Then the weight comparison would've actually held up fine, since placement wouldn't have mattered as much. It was the aft location that made that comparison misleading, not the comparison itself.

Interviewer: If you'd known upfront the two prior tail-heavy events were unrelated, would you have redistributed the same way?

Participant: No. I'd have trusted my own numbers for this flight instead of layering in a correction based on two other tails.

Interviewer: Anything you'd do differently facing this same sequence again, under the same shortened window?

Participant: Pull the manual chart for anything irregular no matter how tight the clock is, and keep this flight's numbers separate from what happened on previous ones unless I actually know there's a shared cause. The LMC piece I'd still have to think through—weight alone wasn't the full story that day, and less time made that easier to miss, not harder.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Counterfactual_3",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Load Controller / Loadmaster (Commercial)",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Late Reload and Trim Discrepancy on a Compressed Narrow-Body Turnaround",
    "scenario_summary_internal": "This is the causal-variable counterfactual pairing of AV_Biased_3. The incident, cargo mix, LMC, rotation trim history, and final bag-count discrepancy are held materially constant. The single causal variable changed is the length of the turnaround window: instead of a routine 45-minute turnaround, an inbound delay compresses the ground time to approximately 30 minutes before the fixed departure slot. All other facts, actors, and the sequence of four decision points are preserved so that any difference in the load controller's reasoning can be attributed to the tighter time window rather than to a different incident. The same three intended bias instances are implemented at the same decision points as in the base scenario: automation bias at decision point 1 (accepting the automatically generated load instruction for atypical cargo without an independent manual cross-check), substitution bias at decision point 2 (using aggregate LMC weight similarity as a proxy for placement-specific index verification), and apophenia/correlation bias at decision point 3 (inferring a causal recurring trim pattern from two unrelated preceding events). Decision point 4 remains neutral and genuinely ambiguous.",
    "occupational_realism": {
      "objective": "Produce and sign off a compliant final load sheet (weight, balance, and CG within structural and CG envelope limits) before a fixed departure slot that now allows less buffer than usual, while correctly incorporating a non-standard cargo item and a late cargo addition.",
      "setting": "Regional hub airport ramp and load control office; ground time compressed to roughly 30 minutes because the inbound aircraft arrived late, on a narrow-body combi aircraft with belly holds 1-5.",
      "constraints": [
        "Compressed ~30-minute turnaround due to a delayed inbound aircraft, with the same fixed departure slot as originally scheduled",
        "Atypical, irregularly shaped machinery cargo requiring non-standard hold placement",
        "Late cargo/baggage change (LMC) received after the initial load instruction was generated",
        "Dangerous goods segregation and NOTOC accuracy requirements",
        "Structural per-hold and cumulative weight limits",
        "Reliance on a load-control software system (ALI generator) validated for standard palletized loads",
        "Heightened ramp crew and dispatcher time pressure relative to the base scenario, competing with verification thoroughness"
      ],
      "stakeholders": [
        "Load controller (interviewee)",
        "Ramp supervisor",
        "Ground handling agents",
        "Dispatcher / operations control",
        "Captain (recipient of NOTOC and final load sheet)"
      ],
      "technical_terms_to_use": [
        "load sheet", "weight and balance (W&B)", "center of gravity (CG)", "unit load device (ULD)",
        "automatic load instruction (ALI)", "last-minute change (LMC)", "NOTOC", "zero fuel weight (ZFW)",
        "trim sheet", "index units", "mean aerodynamic chord (MAC)", "bulk hold", "closeout figures"
      ],
      "technical_terms_to_avoid": [
        "automation bias", "substitution bias", "apophenia", "correlation bias", "heuristic",
        "cognitive bias", "anchoring", "pattern recognition error"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Inbound delay has compressed ground time to about 30 minutes, less than the usual 45",
          "Load-control software has generated a correct ALI for this fleet type over many months",
          "An irregularly shaped machinery cargo item (heavier and non-palletized) has been assigned to hold 3 by the ALI",
          "Ramp crew is waiting, now with less buffer than usual, for the final hold assignment"
        ],
        "new_information_after_decision": [
          "Ramp later reports the aircraft trimming slightly tail-heavy after loading per the ALI-assigned placement"
        ],
        "alternatives": [
          "Accept the automatically generated ALI as-is and issue loading instructions immediately given the shorter window",
          "Independently cross-check the ALI's hold assignment for the irregular machinery item against the manual structural limits chart before issuing instructions"
        ],
        "intended_action": "Loadmaster accepts the ALI output without the independent manual cross-check specifically indicated for non-standard/irregular cargo, citing the system's long track record of accuracy and the now-tighter schedule."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "An LMC of approximately 380kg of mail plus 6 late bags arrives after the initial load sheet was drafted, with even less time remaining than in a normal turn",
          "The mail is assigned to aft hold 5, a smaller hold not typically used for this route's routine LMCs",
          "The past three flights this week had LMCs of comparable total weight that did not require redistribution"
        ],
        "new_information_after_decision": [
          "The specific aft placement in hold 5 produces a larger index/moment shift than prior weeks' LMCs, which were placed forward"
        ],
        "alternatives": [
          "Run a full recalculation of the index/moment shift specific to placing this LMC in hold 5",
          "Judge the LMC acceptable based on its total weight being similar to this week's routine LMCs, without checking placement-specific index impact"
        ],
        "intended_action": "Loadmaster judges the LMC acceptable primarily because its aggregate weight resembles this week's typical LMCs, without independently verifying the placement-specific index effect of the aft hold assignment, under greater time constraint than the base scenario."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch log shows the previous two flights on this aircraft rotation (different tail numbers, one to a different destination) required aft trim adjustments",
          "This flight's own computed index, based on its actual load configuration, falls within the normal forward range",
          "Very little time remains before the trim sheet must be finalized given the compressed window"
        ],
        "new_information_after_decision": [
          "The two prior tail-heavy events are later attributed to unrelated causes: one to a fuel imbalance, the other to additional catering load, not a rotation-wide pattern"
        ],
        "alternatives": [
          "Base the trim sheet strictly on this flight's own computed index and load configuration",
          "Pre-emptively shift cargo distribution forward because the same rotation trended tail-heavy on the two preceding flights"
        ],
        "intended_action": "Loadmaster pre-emptively redistributes cargo forward based on an inferred recurring 'tail-heavy rotation' pattern drawn from two unrelated preceding events, rather than relying on this flight's own within-limits computed index, reasoning that there is no time left to investigate further."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Closeout figures appear balanced and within limits under the current load sheet",
          "A minor discrepancy of one bag count is noted between the ramp tally and the NOTOC/baggage manifest",
          "The compressed departure slot window is closing faster than usual, and holding for re-verification risks a delay"
        ],
        "new_information_after_decision": [
          "The bag-count discrepancy is resolved shortly after release, either matching a clerical miscount or requiring a minor manifest correction, without changing the overall weight and balance conclusion"
        ],
        "alternatives": [
          "Sign and release the final load sheet with the current closeout figures",
          "Request a short hold to re-verify the closeout figures and bag count against the NOTOC before final sign-off"
        ],
        "intended_action": "Loadmaster weighs the operational cost of a short hold, now more costly given the compressed schedule, against the apparent minor nature of the discrepancy, and makes a judgment call; no intended bias is embedded here, and either choice remains professionally defensible."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe your role and what this particular turnaround looked like compared to a typical one?",
        "Walk me through what changed when you learned the ground time would be shorter than planned."
      ],
      "timeline_reconstruction": [
        "What was the first piece of information you received about the cargo mix for this flight?",
        "When did the last-minute change come in, and how did the shorter window affect how you handled it?",
        "What did the trim history for this rotation look like leading up to this flight?",
        "What happened right before you finalized and signed the load sheet, given how little time was left?"
      ],
      "decision_point_probes": [
        "What specific cues told you the automated load instruction was ready to use as generated, especially with less time available?",
        "What information sources did you consult when the mail and late bags came in, and what did you rely on most under that time constraint?",
        "What was your goal when you decided to adjust the cargo distribution forward before finalizing the trim sheet?",
        "What alternatives did you consider at each of these points, and did the shorter window change which alternative felt realistic?",
        "How much time pressure were you under at each of these moments compared to a normal turn, and how did that affect your approach?",
        "How confident were you in each of these judgments at the time, versus after the fact?",
        "Had you seen similar situations before in your experience, and how did that shape your response this time?"
      ],
      "closing_hypotheticals": [
        "If you had had the full 45 minutes instead of 30, do you think you would have handled the machinery cargo differently?",
        "If the LMC mail had been placed in the usual forward hold instead of hold 5, would your assessment have differed?",
        "Looking back, if you had known the two prior tail-heavy events had unrelated causes, would you have redistributed the cargo the same way?",
        "What would you do differently if you faced this exact sequence of events again, with the same shortened window?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "au_01",
        "bias": "Automaticity or Automation Bias",
        "decision_point": 1,
        "mechanism": "Over-reliance on the automatically generated ALI for an atypical, irregularly shaped machinery cargo item, treating the system's general track record on standard palletized loads as sufficient justification to skip the manual cross-check specifically indicated for non-standard cargo, now reinforced by the compressed schedule.",
        "affected_reasoning_operation": "Verification/checking of a system-generated output before acting on it",
        "evidence_available_at_time": [
          "System's consistent accuracy over months on standard loads",
          "Awareness that this cargo item is irregular and non-standard",
          "Heightened time pressure from the compressed ~30-minute turnaround"
        ],
        "required_textual_manifestation": "Loadmaster explicitly cites the system's past reliability and the shorter window as reasons for not independently checking the hold assignment for the atypical item, despite acknowledging its non-standard nature.",
        "plausible_nonbias_interpretation": "Reasonable trust in a validated tool under an unusually tight schedule, consistent with normal operational triage when time is scarce.",
        "strength": "subtle",
        "do_not_make_explicit": ["automation bias", "over-reliance", "system trust heuristic"]
      },
      {
        "instance_id": "sub_01",
        "bias": "Substitution bias",
        "decision_point": 2,
        "mechanism": "Replacing the harder question ('what precise index/moment shift does this specific LMC placement in hold 5 produce') with an easier proxy question ('does this LMC's total weight resemble this week's routine LMCs'), and treating the proxy answer as resolving the original question, under greater time scarcity than the base scenario.",
        "affected_reasoning_operation": "Evaluation of whether a new piece of evidence (the LMC) requires a full recalculation",
        "evidence_available_at_time": [
          "Total weight of the new LMC (~380kg plus 6 bags)",
          "Historical pattern of similar-weight LMCs this week",
          "Fact that this LMC's hold placement (aft, hold 5) differs from prior LMCs (forward holds)"
        ],
        "required_textual_manifestation": "Loadmaster states or implies that the LMC was judged acceptable mainly by comparing its total weight to past LMCs, without describing a placement-specific index check for hold 5, and references the shorter window as part of the justification.",
        "plausible_nonbias_interpretation": "A reasonable use of pattern-based experience to triage low-risk changes under unusually tight time pressure, when weight similarity is genuinely informative in most cases.",
        "strength": "subtle",
        "do_not_make_explicit": ["substitution bias", "proxy question", "attribute substitution"]
      },
      {
        "instance_id": "ap_01",
        "bias": "Apophenia or Correlation Bias",
        "decision_point": 3,
        "mechanism": "Inferring a causal, recurring 'tail-heavy rotation' pattern from two temporally adjacent but causally unrelated trim events on different tail numbers, and using that inferred pattern to override this flight's own within-limits computed index, with the compressed schedule cited as the reason further investigation was skipped.",
        "affected_reasoning_operation": "Causal attribution and generalization from a small, coincidental sample to guide a current decision",
        "evidence_available_at_time": [
          "Two prior flights on the same rotation logged aft trim adjustments",
          "Those two flights differed in tail number and one differed in destination",
          "This flight's own index, computed from its actual load, was within normal forward range"
        ],
        "required_textual_manifestation": "Loadmaster explains the pre-emptive forward redistribution by referencing the rotation's recent trim history as if it were a causal or recurring property of the rotation, rather than treating the two events as potentially coincidental, and notes there was no time left to check further.",
        "plausible_nonbias_interpretation": "A cautious, experience-based safety margin applied given recent operational history and limited time, which is a defensible judgment call absent further information.",
        "strength": "subtle",
        "do_not_make_explicit": ["apophenia", "correlation bias", "illusory pattern", "small sample"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "AV_Biased_3",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is a counterfactual pairing, not a vocabulary or ambiguous control."
    },
    "counterfactual_specification": {
      "causal_variable": "Length of the turnaround window before the fixed departure slot",
      "original_state": "A routine 45-minute turnaround with no additional schedule compression (as in AV_Biased_3)",
      "counterfactual_state": "A compressed ~30-minute turnaround caused by a delayed inbound aircraft, with the same fixed departure slot",
      "variables_to_hold_constant": [
        "Cargo mix and weights, including the irregular machinery item",
        "LMC content, weight, and hold placement",
        "Rotation trim history and its two prior unrelated causes",
        "Aircraft type and route",
        "Actors and stakeholder roles",
        "ALI system behavior and its lack of a mandatory manual-check flag",
        "The final bag-count discrepancy and its resolution"
      ],
      "expected_causal_difference": "The same three reasoning patterns (automation reliance, weight-based proxy judgment, and unrelated-event pattern inference) are expected to persist, but should be framed more explicitly around time scarcity as the stated justification, testing whether the same bias mechanisms are attributed mainly to the shorter window rather than disappearing under greater pressure.",
      "causal_test_question": "Does compressing the turnaround from 45 to 30 minutes change how strongly the load controller invokes time pressure as the reason for the same three reasoning shortcuts, without changing whether those shortcuts occur?"
    },
    "generation_checks": [
      "Exactly 3 total intended bias instances planned, matching the manifest sum (1+1+1)",
      "Exactly 4 decision points defined, each with at least two alternatives",
      "Each bias instance assigned to a distinct decision point (DP1, DP2, DP3), matching the base scenario's assignment; DP4 left intentionally neutral/ambiguous",
      "Only the turnaround-window variable and its direct time-pressure framing differ from AV_Biased_3; all other material facts are held constant",
      "No bias terminology or psychological labels appear in probe plan or timeline text",
      "Each instance has a plausible non-bias interpretation distinct from its intended mechanism",
      "Decision point 4 contains no intended bias instance and has a genuinely ambiguous, non-mechanical outcome",
      "Target word count (1,215-1,485 words) is achievable given four decision points with probes, without repetitive exposition"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Substitution bias", "occurrences": 1, "mechanism_constraint": "Must manifest as answering an easier proxy question (aggregate weight similarity) in place of the harder question (placement-specific index/moment impact) at decision point 2, with time scarcity cited as contributing justification." },
      { "bias": "Apophenia or Correlation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as inferring a causal recurring pattern from two temporally adjacent but causally unrelated trim events at decision point 3, with time scarcity cited as the reason further checking was skipped." },
      { "bias": "Automaticity or Automation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as bypassing an independent manual check on an automated system output specifically for an atypical/non-standard case at decision point 1, with the compressed schedule cited as reinforcing justification." }
    ],
    "target_bias_names": [
      "Substitution bias",
      "Apophenia or Correlation Bias",
      "Automaticity or Automation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Substitution bias", "requested_occurrences": 1 },
      { "bias": "Apophenia or Correlation Bias", "requested_occurrences": 1 },
      { "bias": "Automaticity or Automation Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias" },
      { "instance_id": "sub_01", "bias": "Substitution bias" },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias", "decision_point": 1 },
      { "instance_id": "sub_01", "bias": "Substitution bias", "decision_point": 2 },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "au_01",
        "bias": "Automaticity or Automation Bias",
        "mechanism": "Skipping manual cross-check for irregular cargo based on general system reliability, reinforced by compressed schedule framing",
        "affected_reasoning_operation": "Verification of system-generated output before action",
        "evidence_source": "ALI output plus known irregularity of the machinery cargo item plus stated 30-minute window",
        "distinctiveness_requirement": "Must be the only instance in the interview where a system output is accepted without a check specifically warranted by an atypical case; not repeated elsewhere."
      },
      {
        "instance_id": "sub_01",
        "bias": "Substitution bias",
        "mechanism": "Substituting an easier proxy question (weight similarity) for the harder question (placement-specific index impact), reinforced by compressed schedule framing",
        "affected_reasoning_operation": "Evaluation of whether new evidence (LMC) requires full recalculation",
        "evidence_source": "LMC weight and placement data compared against historical LMC pattern, under stated time scarcity",
        "distinctiveness_requirement": "Must be the only instance where a harder quantitative question is answered via an easier proxy comparison; distinct from au_01 in that no automated system output is involved."
      },
      {
        "instance_id": "ap_01",
        "bias": "Apophenia or Correlation Bias",
        "mechanism": "Inferring a causal recurring pattern from two coincidental, causally unrelated prior events, reinforced by compressed schedule framing",
        "affected_reasoning_operation": "Causal attribution/generalization applied to override a current, independently valid computed value",
        "evidence_source": "Trim log history of two preceding flights on the same rotation, under stated time scarcity",
        "distinctiveness_requirement": "Must be the only instance involving inference of a causal pattern from a small historical sample; distinct from sub_01, which involves comparing current data to past data without asserting causality."
      }
    ],
    "intended_strength": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias", "strength": "subtle" },
      { "instance_id": "sub_01", "bias": "Substitution bias", "strength": "subtle" },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": "AV_Biased_3",
    "counterfactual_variable": {
      "name": "Length of the turnaround window before the fixed departure slot",
      "original_state": "Routine 45-minute turnaround with no additional schedule compression",
      "changed_state": "Compressed ~30-minute turnaround due to a delayed inbound aircraft, same fixed departure slot",
      "variables_to_hold_constant": [
        "Cargo mix and weights, including the irregular machinery item",
        "LMC content, weight, and hold placement",
        "Rotation trim history and its two prior unrelated causes",
        "Aircraft type and route",
        "Actors and stakeholder roles",
        "ALI system behavior and its lack of a mandatory manual-check flag",
        "The final bag-count discrepancy and its resolution"
      ]
    },
    "scenario_id": "AV_Counterfactual_3",
    "domain_id": "AV",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Each of the three requested biases was assigned to exactly one distinct decision point (DP1, DP2, DP3), mirroring the allocation used in the paired base scenario AV_Biased_3, so that only the turnaround-window causal variable differs between the pair. Decision point 4 was deliberately left free of intended bias instances to preserve an ambiguous, non-mechanical outcome, consistent with the base scenario.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Cargo mix and weights, including the irregular machinery item",
      "LMC content, weight, and hold placement",
      "Rotation trim history and its two prior unrelated causes",
      "Aircraft type and route",
      "Actors and stakeholder roles",
      "ALI system behavior and its lack of a mandatory manual-check flag",
      "The final bag-count discrepancy and its resolution"
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
        "segment_type": "context_reasoning",
        "raw_interview_anchor": "Right away I knew I'd be compressing steps I'd normally spread out a bit more. Nothing about the flight itself was unusual—it was just less time to work with.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This explains operational compression caused by the shortened turnaround but does not itself contain a hidden bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The irregular machinery item was assigned to hold 3 by the automatic load instruction, and the participant issued the ALI as generated because the system had been reliable and time was short; follow-up confirms the available manual chart was not used.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "au_01"
        ],
        "ground_truth_rationale": "Decision point 1 contains the intended automation-bias mechanism: an automated output for atypical cargo was accepted without the situation-specific manual cross-check, with system reliability and schedule compression cited as reasons."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The participant cleared the 380-kilogram mail and six late bags in aft hold 5 after comparing total weight with three recent LMCs, without calculating the placement-specific index shift.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sub_01"
        ],
        "ground_truth_rationale": "Decision point 2 contains the intended substitution mechanism: aggregate weight similarity was used as an easier proxy for the harder placement-specific index calculation under time scarcity."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The participant inferred that the rotation was running tail-heavy from the ramp report and two prior aft-trim events, then shifted cargo forward beyond what the current flight's own index required.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ap_01"
        ],
        "ground_truth_rationale": "Decision point 3 contains the intended apophenia/correlation mechanism: a recurring causal pattern was inferred from two temporally adjacent events and used to override valid current-flight data."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The participant signed and released with a one-bag discrepancy after weighing delay risk against the possibility of a routine miscount; the discrepancy was later corrected without changing the W&B conclusion.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Decision point 4 is deliberately neutral and genuinely ambiguous. The participant made an explicit operational risk tradeoff, and either sign-off or a short hold was professionally defensible."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective_recommendation",
        "raw_interview_anchor": "The participant recommended pulling the manual chart for irregular cargo and keeping the current flight's numbers separate from prior flights unless a shared cause is known, while remaining uncertain about the LMC issue.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective recommendation and uncertainty statement, not an additional hidden occurrence."
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
    "analysis_scope_note": "The interview transcript was analyzed without access to retrieved scientific-paper passages. Bias labels and definitions are therefore drawn from widely established cognitive-science knowledge, and the absence of retrieved corpus support is disclosed for each occurrence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "illusory correlation",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation bias",
      "alternative_labels": ["automation-induced complacency", "overreliance on automation"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to over-rely on automated system output and to insufficiently scrutinize or override it, especially when the system has a history of reliability.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Issuing the automatic load instruction for irregular machinery cargo",
      "decision_point_description": "Deciding whether to manually verify an automatically generated hold assignment for a heavier-than-usual, non-palletized machinery item",
      "affected_reasoning_operation": "Verification and override decision for automated load-control output",
      "bias_specific_mechanism": "The participant accepted the load-control software's output primarily because the system had been reliable on this fleet, even though he had noticed the cargo item was irregular, non-palletized, and heavier than typical.",
      "manifestation_in_interview": "He issued the ALI basically as generated and did not pull the available manual chart, despite recognizing the irregular cargo.",
      "effect_on_reasoning_or_decision": "The automatic hold assignment was accepted without manual verification, allowing an unusual heavy item to be loaded without the specific manual check that the participant said the situation warranted.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our load-control software generates an automatic load instruction, and it put that machinery item into hold 3. That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately.",
          "evidence_explanation": "This shows that the system's reliability history was a central reason for acting on the automated output without manual scrutiny."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me.",
          "evidence_explanation": "This shows the participant noticed a concrete reason to verify manually, but the automation's history and time pressure carried the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There is, for exactly that situation. I know where it is. I just didn't reach for it that day.",
          "evidence_explanation": "This confirms that a manual verification procedure was available and was not used."
        }
      ],
      "correction_or_counterevidence": "Time pressure was also present and the participant says he probably would have pulled the manual chart with a full 45 minutes. However, the automation-specific reliance on system history is explicitly stated.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available in this analysis; the label is assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the need for redistribution by the ease with which similar recent LMCs came to mind rather than by running the specific placement-sensitive weight-and-balance calculation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Clearing the late mail and bags LMC assigned to aft hold 5",
      "decision_point_description": "Deciding whether a 380 kg mail plus six late bags LMC in hold 5 required redistribution, based on total weight comparisons to earlier LMCs",
      "affected_reasoning_operation": "Assessment of the weight-and-balance impact of LMC placement",
      "bias_specific_mechanism": "The participant relied on readily available recent examples—three similar-weight LMCs earlier in the week that had not required redistribution—rather than calculating the index shift for the current aft-hold placement.",
      "manifestation_in_interview": "He cleared the LMC because its total weight matched recent examples, while acknowledging he did not check that the earlier LMCs went forward and the current one went aft.",
      "effect_on_reasoning_or_decision": "The LMC was cleared without an index-shift calculation for the aft hold 5 placement, using a total-weight comparison that may not have been valid for the actual loading location.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "With the time we had left, I looked at the total weight, saw it was in line with the LMCs we'd been getting all week on this route—three similar ones, same range, none of those needed redistribution—and cleared it on that basis so I could move to the trim sheet.",
          "evidence_explanation": "This shows that recent remembered LMCs were used as the primary basis for clearing the current LMC."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest.",
          "evidence_explanation": "This explicitly identifies the accessibility of the recent examples as the reason for using that comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it.",
          "evidence_explanation": "This shows the comparison was non-equivalent because of hold placement, but the available similar-weight examples were still used."
        }
      ],
      "correction_or_counterevidence": "The participant later noted that the comparison would have been adequate if the mail had gone to the usual forward hold, suggesting the core problem was using weight similarity alone and ignoring placement. Time pressure was also present, but the availability of recent examples is specifically described.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available in this analysis; the label is assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "illusory correlation",
      "alternative_labels": ["clustering illusion", "representativeness heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Perceiving a meaningful relationship—that the rotation was running tail-heavy that day—from two prior independent aft trim corrections, despite different aircraft and unrelated causes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Forward redistribution on the trim sheet",
      "decision_point_description": "Deciding whether to shift cargo forward beyond the current flight's calculated index requirement based on previous flights on the same rotation",
      "affected_reasoning_operation": "Inference about aircraft trim behavior and pattern recognition",
      "bias_specific_mechanism": "The participant treated two consecutive prior aft trim corrections as evidence of a stable rotation-level pattern, even though they involved different aircraft, one had a different destination, and there was no known common cause.",
      "manifestation_in_interview": "He shifted cargo forward beyond what his own index required because seeing two prior aft trims made him distrust an otherwise acceptable calculation.",
      "effect_on_reasoning_or_decision": "A forward trim correction was applied to this flight even though the flight's own calculated index was within the normal forward range with margin.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required.",
          "evidence_explanation": "This directly shows the inference from two prior events to a rotation-level pattern and the resulting action."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "They were on the same rotation, back to back, and both needed aft correction. Two in a row felt like it meant something about how the rotation was running that day, so I built in a forward shift before signing off, and honestly, with the time we had left, I didn't feel like there was room to dig into it further.",
          "evidence_explanation": "This demonstrates the perception that two consecutive events formed a meaningful pattern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If you'd known upfront the two prior tail-heavy events were unrelated, would you have redistributed the same way? Participant: No. I'd have trusted my own numbers for this flight instead of layering in a correction based on two other tails.",
          "evidence_explanation": "This counterfactual confirms that the perceived relationship between prior flights was the basis for the unnecessary correction."
        }
      ],
      "correction_or_counterevidence": "The current ramp report was genuine but described the aircraft as only slightly tail-heavy and not out of limits. The participant later learned the two prior aft trim corrections had unrelated causes: one was a fuel imbalance and the other was late catering.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available in this analysis; the label is assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "normalization of deviance",
      "alternative_labels": ["optimism bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final sign-off with one-bag ramp tally discrepancy",
      "supporting_interview_quote": "I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself.",
      "plausible_mechanism": "The participant may have normalized a small discrepancy because prior one-bag shortages were usually miscounts, reducing the perceived need to chase the discrepancy before release.",
      "why_not_identified": "The interview does not provide affirmative evidence that a bias-specific mechanism distorted the sign-off decision. The participant describes an explicit delay-risk trade-off, acknowledges another reasonable course of action, and notes the weight-and-balance conclusion did not change, so this is better classified as an ordinary risk judgment under time pressure."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based solely on the interview transcript; no external verification of aircraft loading, timestamps, system outputs, or outcome records was available.",
    "No scientific-paper corpus passages were available in this analysis, so bias labels and definitions rely on general cognitive-science knowledge rather than retrieved corpus evidence.",
    "The speaker's statements are retrospective self-reports and may be affected by memory, hindsight, or self-presentation.",
    "Time pressure and operational constraints are significant context factors in this scenario and are not by themselves classified as biases."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Counterfactual_3_Sonar_off",
  "interview_id": "AV_Counterfactual_3",
  "system_prompt_id": "Sonar",
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
