You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific inspection you handled, purely for understanding how you approached the decisions — not an audit of your conclusions. That okay with you?

Participant: Sure, no problem. I've got the file pulled up if I need to check dates.

Interviewer: Great. Can you give me your role and a bit of background first?

Participant: I'm a fire inspector, been doing building code compliance for about nine years now, mostly commercial and mixed-use properties. This particular case was an annual re-inspection tied to a certificate of occupancy renewal for a three-story building — retail on the ground floor, offices above. They'd just finished a tenant fit-out renovation, so the stakes were a little higher than a routine annual check.

Interviewer: Walk me through what happened, from arrival to wrap-up.

Participant: I got there in the morning, met the building manager — I've worked with him for probably four years across different properties he's managed. Good guy, very responsive, easy to deal with. The building was operating normally, tenants open, so I had to work around foot traffic in a few spots. First thing I did was the egress corridors. Near the loading dock there's a secondary egress path, and I found it partially narrowed by stacked delivery pallets. He told me it was just for that morning's delivery. I measured it anyway — clear width was under the code minimum with the pallets there. I wrote that up as a formal minor violation with a short correction window, regardless of what he said about the timing. Later, actually, one of the retail staff mentioned in passing that the pallets had been sitting there off and on for a couple weeks, not just that morning. Didn't change my classification, but it stuck with me.

Then we went up to check the secondary stairwell door. That's when I found the self-closing device disconnected — the arm was just hanging loose. That's a meaningful finding; a fire door that won't close on its own defeats the whole point of the assembly during smoke or fire conditions. He was pretty apologetic about it, said maintenance had already been told about it the week before, and he offered to have someone reattach it right then while I was standing there.

Interviewer: And the alarm system?

Participant: Right, that was next. I pulled the monthly test log and there was a gap — one month with nothing recorded. He said the test had definitely happened, it just hadn't been logged properly. I didn't take that at face value. I asked for the monitoring company's records instead of just accepting the verbal explanation, and I flagged the gap as an open documentation item pending that verification rather than closing it out.

Interviewer: Let's go through each of those decisions in a bit more detail, starting with the pallets. What made you decide to formally cite that instead of just noting it informally?

Participant: The corridor width is objective — I measured it, it was under the minimum, full stop. Doesn't matter what the explanation is for why it's narrow. That one felt straightforward to me; the measurement does the talking.

Interviewer: And the door closer — how did you land on an advisory note instead of a formal citation, given you just described it as a meaningful life-safety item?

Participant: Yeah, that one I went back and forth on a bit. Technically, sure, it's a significant deficiency — no-questions-asked at the code level. But he was really upfront about it, apologized a couple times, said his team already knew and it just hadn't been actioned yet, and he wanted to fix it right there in front of me. After four years of him being straight with me on other properties, going in hard with a formal citation over something he was already fixing on the spot felt like more friction than the moment called for. So I logged it as an advisory note instead — get it corrected, follow up next visit, no formal paperwork trail.

Interviewer: Did you check the maintenance ticket he referenced, or look at whether this had come up before at that building?

Participant: Not in the moment, no. I didn't pull the ticket timestamp, and I didn't cross-check last year's report right there. In hindsight I probably should have — turned out the ticket was only logged that morning, not the week before like he said, and there'd actually been a near-identical closer issue flagged and marked corrected in last year's inspection. So it wasn't new, it was a repeat. I didn't know that at the time I made the call, though.

Interviewer: What was going through your mind that made the apology and the offer to fix it feel like enough?

Participant: Honestly, it just felt like the reasonable, low-friction way to handle it with someone who's generally cooperative. I wasn't thinking about whether it had happened before — I was thinking about the guy standing in front of me being embarrassed about it and already moving to fix it. Writing him up formally in that moment felt like it would've been an unnecessarily hard line to take.

Interviewer: Third decision — the alarm log gap. Why request outside verification there but not for the door closer?

Participant: Different kind of claim, I think. "The test happened but wasn't logged" is something I can actually check against a third party — the monitoring company has their own records independent of him. There's no equivalent independent record for a closer that's already been reattached; once it's fixed, the evidence is gone. So partly it was about what was still verifiable versus what wasn't.

Interviewer: Fourth decision — writing the final recommendation. How did you weigh the three findings together?

Participant: I recommended conditional renewal — correct the pallet obstruction, get the alarm verification resolved, and monitor the door closer as an open advisory item. My supervisor actually pushed back a little, asked why the closer wasn't a formal citation given the classification. I explained the on-site correction and the manager's responsiveness. He wasn't fully satisfied but didn't override it. The manager also messaged me afterward thanking me for being reasonable during the visit.

Interviewer: What information, if you'd had it at the time, would have changed your call on the door closer?

Participant: Knowing it was a repeat finding from last year would have changed things for sure — that's a pattern, not a one-off. If I'd pulled that file before finalizing the note instead of after, I think I'd have citied it formally.

Interviewer: If the manager had reacted differently — say, defensively or dismissively instead of apologetically — do you think your classification would have been different?

Participant: Probably, yeah. If he'd pushed back or acted like it wasn't a big deal, I think I'd have gone straight to a formal citation without much hesitation. The fact that he was already owning it and fixing it changed how I approached writing it up.

Interviewer: Looking back, is there a point where you'd want more information before deciding again?

Participant: The closer, for sure. I'd want the maintenance ticket pulled and last year's report checked before I finalize any classification, not after.

Interviewer: Anything you'd tell a newer inspector handling a similar situation with a cooperative, familiar contact?

Participant: Probably to separate the paperwork from the personal read on the guy. The relationship can tell you how a conversation's going to go, but it shouldn't really be what decides the classification — the classification should hold up the same whether the person in front of you is anxious about it or not.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HE_Biased_1",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Fire Inspector (Building Code Compliance)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Annual Life-Safety Re-Inspection at a Renovated Mixed-Use Building",
    "scenario_summary_internal": "A fire inspector conducts the annual life-safety re-inspection of a three-story mixed-use building (ground-floor retail, upper-floor offices) that recently completed a tenant-fit-out renovation, ahead of certificate-of-occupancy renewal. The inspector must evaluate egress clearance, door hardware/closer function, fire alarm testing documentation, and overall compliance sufficiency across four sequential decision points, working with a long-standing, cordial building manager under a same-day inspection deadline.",
    "occupational_realism": {
      "objective": "Determine whether the building's fire/life-safety systems and egress paths meet code requirements sufficient to recommend renewal of the certificate of occupancy.",
      "setting": "A mid-rise mixed-use commercial building undergoing final walkthrough after tenant renovation, inspected during business hours with staff and customers present.",
      "constraints": [
        "Inspection must be completed within a single working day before the certificate expires",
        "Building manager has a multi-year cooperative working relationship with the inspector",
        "Retail tenants are operating during the inspection, limiting access to some areas",
        "Renovation contractor is not on-site to answer technical questions directly",
        "Inspector's supervisor expects a same-day summary recommendation"
      ],
      "stakeholders": [
        "Fire inspector (protagonist)",
        "Building manager",
        "Ground-floor retail tenant staff",
        "Inspector's supervising fire marshal",
        "Renovation contractor (off-site, referenced only)"
      ],
      "technical_terms_to_use": [
        "egress corridor",
        "self-closing device",
        "fire door assembly",
        "certificate of occupancy",
        "life-safety hazard classification",
        "fire alarm test log",
        "means of egress obstruction",
        "advisory note vs. formal violation"
      ],
      "technical_terms_to_avoid": [
        "courtesy bias",
        "social desirability",
        "conformity",
        "politeness bias",
        "impression management"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Stacked inventory pallets partially narrow the secondary egress corridor near the loading dock",
          "Code requires a minimum clear width for that corridor",
          "Manager states the pallets are 'just for today' during a delivery"
        ],
        "new_information_after_decision": [
          "A retail employee mentions the pallets have been stored there intermittently for two weeks",
          "The loading dock area has no alternate storage space identified"
        ],
        "alternatives": [
          "Issue a formal written violation for egress obstruction",
          "Log an informal advisory note and request voluntary correction",
          "Measure the corridor width precisely before deciding classification"
        ],
        "intended_action": "Inspector measures the obstruction, documents it as a formal minor violation with a short correction deadline, independent of the manager's explanation."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The stairwell door serving the secondary egress stair has a disconnected self-closing device",
          "Code classifies a non-functioning self-closer on a fire door assembly as a significant life-safety deficiency",
          "The manager personally apologizes, says maintenance was informed last week, and offers to fix it 'right now' in front of the inspector"
        ],
        "new_information_after_decision": [
          "The maintenance ticket referenced by the manager was actually logged only that morning, not last week",
          "A similar closer issue was noted as 'corrected' in the prior year's report but recurs"
        ],
        "alternatives": [
          "Classify the finding as an immediate life-safety hazard requiring formal citation and re-verification",
          "Downgrade the finding to an informal advisory note based on the manager's assurance and apologetic tone",
          "Request the maintenance ticket and prior-year records before classifying"
        ],
        "intended_action": "Inspector, moved by the manager's contrite demeanor and desire to avoid an awkward confrontation with a cooperative long-term contact, downgrades the classification to an advisory note without verifying the maintenance ticket or prior-year recurrence."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The monthly fire alarm test log shows a gap for one month with no recorded test",
          "Code requires monthly documented testing with no exceptions",
          "The manager verbally states the test was 'definitely done, just not logged'"
        ],
        "new_information_after_decision": [
          "The alarm monitoring company's records (available on request) show no test signal was received that month",
          "Two other months in the log have testing timestamps outside normal business hours, an irregular pattern"
        ],
        "alternatives": [
          "Require the manager to produce third-party monitoring records before accepting the log as complete",
          "Accept the verbal assurance and mark the log as substantially compliant",
          "Flag the gap as a documentation deficiency pending verification"
        ],
        "intended_action": "Inspector requests the monitoring company's records rather than relying on verbal assurance, and flags the gap as an open documentation deficiency pending verification."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Findings from phases 1-3: one formal egress violation, one downgraded advisory note on the stair door closer, one pending documentation deficiency on alarm testing",
          "Same-day deadline for a recommendation on certificate renewal",
          "Supervisor expects a clear pass/conditional-pass/fail summary"
        ],
        "new_information_after_decision": [
          "Supervisor asks why the stair door closer was not treated as a formal citation given its life-safety classification",
          "Manager sends a follow-up message thanking the inspector for being 'reasonable' during the visit"
        ],
        "alternatives": [
          "Recommend conditional certificate renewal pending correction of all three items, each classified independently on its own evidentiary merits",
          "Recommend full renewal, treating the advisory-note item as effectively resolved",
          "Recommend renewal denial pending complete re-inspection of all systems"
        ],
        "intended_action": "Inspector recommends conditional renewal, carrying forward the earlier advisory-note classification for the stair door closer without revisiting whether that classification matched the underlying life-safety evidence."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were asked to accomplish during this inspection.",
        "What was your first impression when you arrived at the building?"
      ],
      "timeline_reconstruction": [
        "What did you notice first, and in what order did you check each area?",
        "What information did you have before you made each classification decision, and what did you learn afterward?"
      ],
      "decision_point_probes": [
        "What specific cues led you to classify the loading-dock obstruction the way you did?",
        "When you found the disconnected door closer, what factors went into deciding how serious to mark it?",
        "How did the manager's response affect what you decided to record, if at all?",
        "What made you decide to request outside verification for the alarm log but not for the door closer?",
        "When writing the final recommendation, how did you weigh the three findings against each other?"
      ],
      "closing_hypotheticals": [
        "If a different, less familiar building manager had reacted defensively instead of apologetically, would your classification of the door closer have changed?",
        "If your supervisor had been present during the walkthrough, do you think your documentation would have looked different?",
        "Looking back, is there a decision point where you'd want more information before deciding again?",
        "What would you tell a newer inspector about handling a similar situation with a cooperative, long-term contact?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "decision_point": 2,
        "mechanism": "Inspector downgrades the severity classification of a life-safety-significant fire door closer deficiency from a formal hazard citation to an informal advisory note, driven primarily by the building manager's apologetic tone and the desire to preserve a cordial, non-confrontational relationship, rather than by re-examining the maintenance ticket timeline or the prior-year recurrence.",
        "affected_reasoning_operation": "Severity classification / risk categorization judgment under interpersonal pressure",
        "evidence_available_at_time": [
          "Disconnected self-closing device on a required fire door assembly",
          "Code classification standard treating this as a significant life-safety deficiency",
          "Manager's apologetic, reassuring in-person response and offer to fix immediately",
          "An unverified claim about when the maintenance ticket was logged"
        ],
        "required_textual_manifestation": "The inspector explicitly links the softened classification to not wanting to make the manager 'feel bad' or to avoid an uncomfortable exchange after years of easy cooperation, and does so without checking the maintenance ticket date or the prior-year repeat-finding record before finalizing the note.",
        "plausible_nonbias_interpretation": "The inspector could reasonably argue that on-the-spot correction of a simple mechanical fix legitimately warrants a lighter administrative touch, consistent with common field practice of allowing immediate remediation without formal citation.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "courtesy bias",
          "social politeness",
          "impression management",
          "any explicit psychological labeling of the reasoning"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition and no paired control is being generated in this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Building manager's interpersonal demeanor during the door-closer finding (apologetic/cordial vs. neutral/defensive)",
      "original_state": "Manager reacts apologetically and personally reassures the inspector, invoking the long cooperative history",
      "counterfactual_state": "Manager reacts neutrally or defensively, offering the same factual assurance about same-day repair without an apologetic or relationship-invoking tone",
      "variables_to_hold_constant": [
        "The underlying technical deficiency (disconnected self-closer)",
        "The code classification standard",
        "Time pressure and same-day deadline",
        "All other decision points and findings",
        "Overall building type, layout, and renovation context"
      ],
      "expected_causal_difference": "Under the counterfactual neutral/defensive demeanor, the inspector would be expected to classify the door-closer deficiency as a formal citation rather than an advisory note, since the softening in the original scenario is hypothesized to stem from social/relational pressure rather than technical judgment.",
      "causal_test_question": "Does the inspector's classification of the door-closer finding change when the manager's interpersonal demeanor changes, holding the technical facts constant?"
    },
    "generation_checks": [
      "Exactly one Courtesy Bias instance planned, matching manifest occurrences=1",
      "Instance cb_01 assigned to exactly one decision point (phase 2)",
      "No bias terminology or explicit psychological labels appear in the planned interview content",
      "Decision points 1, 3, and 4 contain no intentionally embedded bias instances",
      "Each decision point includes at least two plausible alternatives and pre/post information",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Scenario supports 1,215-1,485 word target without repetitive exposition across four chronological phases",
      "Consequences (supervisor query, manager's thank-you note) do not mechanically prove bias; they invite interpretation"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Courtesy Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a softened severity classification tied to interpersonal politeness toward a specific stakeholder at one decision point, not as a general disposition or repeated behavior."
      }
    ],
    "target_bias_names": [
      "Courtesy Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Courtesy Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "mechanism": "Downgrading a life-safety-significant fire door closer deficiency from a formal citation to an informal advisory note in direct response to the building manager's apologetic, relationship-invoking demeanor, without independently re-verifying the maintenance ticket timeline or prior-year recurrence.",
        "affected_reasoning_operation": "Severity classification / risk categorization judgment under interpersonal pressure",
        "evidence_source": "In-person interaction with the building manager (apology, reassurance, appeal to cooperative history) combined with an unverified maintenance-ticket claim",
        "distinctiveness_requirement": "This is the sole instance; no other decision point may contain a second softened classification driven by interpersonal courtesy toward any stakeholder."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Building manager's interpersonal demeanor during the door-closer finding",
      "original_state": "Apologetic, cordial, relationship-invoking response from the manager",
      "changed_state": "Neutral or defensive response with identical factual content",
      "variables_to_hold_constant": [
        "Underlying technical deficiency and code classification standard",
        "Time pressure and same-day deadline",
        "All other decision points and findings",
        "Building type, layout, and renovation context"
      ]
    },
    "scenario_id": "HE_Biased_1",
    "domain_id": "HE",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point with the strongest mechanism fit (interpersonal interaction during a severity-classification judgment); no splitting needed since occurrences=1.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Underlying technical deficiency and code classification standard",
      "Time pressure and same-day deadline",
      "All other decision points and findings",
      "Building type, layout, and renovation context"
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
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "I measured it anyway — clear width was under the code minimum with the pallets there. I wrote that up as a formal minor violation with a short correction window, regardless of what he said about the timing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant bases the egress classification on an objective measurement and explicitly separates it from the manager's explanation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "After four years of him being straight with me on other properties, going in hard with a formal citation over something he was already fixing on the spot felt like more friction than the moment called for. So I logged it as an advisory note instead — get it corrected, follow up next visit, no formal paperwork trail.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "This is the narrowest primary span for the hidden occurrence: a significant fire-door deficiency is softened to an advisory note because of the manager's apologetic, cooperative presentation and the desire to avoid friction with a familiar contact."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_review",
        "raw_interview_anchor": "Not in the moment, no. I didn't pull the ticket timestamp, and I didn't cross-check last year's report right there. In hindsight I probably should have — turned out the ticket was only logged that morning, not the week before like he said, and there'd actually been a near-identical closer issue flagged and marked corrected in last year's inspection.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is retrospective evidence about omitted verification and hindsight-only information, not a separate hidden occurrence."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "verification_rationale",
        "raw_interview_anchor": "I didn't take that at face value. I asked for the monitoring company's records instead of just accepting the verbal explanation, and I flagged the gap as an open documentation item pending that verification.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant requests independent verification of the alarm-log claim rather than accepting the manager's assurance; no hidden bias instance is planned here."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "synthesis_recommendation",
        "raw_interview_anchor": "I recommended conditional renewal — correct the pallet obstruction, get the alarm verification resolved, and monitor the door closer as an open advisory item.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This carries forward the earlier classifications into the final recommendation but does not introduce a second hidden instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "Knowing it was a repeat finding from last year would have changed things for sure — that's a pattern, not a one-off. If I'd pulled that file before finalizing the note instead of after, I think I'd have citied it formally.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The response identifies hindsight information that would have changed the classification; it is not an additional occurrence and is not credited as a new bias instance."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "reflective_guidance",
        "raw_interview_anchor": "The relationship can tell you how a conversation's going to go, but it shouldn't really be what decides the classification — the classification should hold up the same whether the person in front of you is anxious about it or not.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a corrective reflection about how classification should be made, not a separate hidden occurrence."
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
    "analysis_scope_note": "Single voluntary interview transcript analyzed for cognitive biases in inspection decisions. No retrieved scientific-paper passages were supplied; bias labels rely on established cognitive-science knowledge when corpus support is unavailable."
  },
  "identified_bias_summary": [
    {
      "bias_label": "affect heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "affect heuristic",
      "alternative_labels": ["liking bias", "halo effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which an immediate affective impression, such as liking, trust, or comfort with a person, guides a judgment or decision, sometimes overriding objective severity or risk information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Classification of the disconnected self-closing fire door as an advisory note rather than a formal citation",
      "decision_point_description": "Whether to issue a formal citation or an advisory note for a significant life-safety deficiency after the building manager apologized and offered to repair it on the spot.",
      "affected_reasoning_operation": "Risk/safety evaluation and enforcement classification decision",
      "bias_specific_mechanism": "The inspector's positive affect toward a familiar, cooperative building manager, developed over four years and reinforced by the manager's apologetic, embarrassed, and immediately corrective demeanor, reduced the perceived need for formal enforcement and made a low-friction response feel reasonable, even though the code-level severity was objectively significant.",
      "manifestation_in_interview": "The participant explicitly says the door-closer deficiency was 'a meaningful life-safety item' and 'no-questions-asked at the code level,' but he chose an advisory note because the manager was already owning it and fixing it and because a formal citation felt like 'more friction than the moment called for.' He also states he was thinking about 'the guy standing in front of me' rather than whether the issue had occurred before.",
      "effect_on_reasoning_or_decision": "A significant fire-door deficiency was formally recorded as an advisory note rather than a citation, reducing the enforcement paper trail and delaying consideration of whether this was a repeat issue until after the decision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Technically, sure, it's a significant deficiency — no-questions-asked at the code level. But he was really upfront about it, apologized a couple times, said his team already knew and it just hadn't been actioned yet, and he wanted to fix it right there in front of me. After four years of him being straight with me on other properties, going in hard with a formal citation over something he was already fixing on the spot felt like more friction than the moment called for.",
          "evidence_explanation": "This directly contrasts the objective severity of the deficiency with the manager's warm, cooperative presentation and the participant's positive relationship history, showing that positive interpersonal affect guided the enforcement classification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, it just felt like the reasonable, low-friction way to handle it with someone who's generally cooperative. I wasn't thinking about whether it had happened before — I was thinking about the guy standing in front of me being embarrassed about it and already moving to fix it.",
          "evidence_explanation": "The participant explicitly attributes the decision to his interpersonal feeling about the person rather than to a checkable compliance history or code-based reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If he'd pushed back or acted like it wasn't a big deal, I think I'd have gone straight to a formal citation without much hesitation. The fact that he was already owning it and fixing it changed how I approached writing it up.",
          "evidence_explanation": "This supports the affective mechanism: the same code deficiency would have been cited formally if the manager's demeanor had produced negative affect, showing that the classification was influenced substantially by the personal interaction."
        }
      ],
      "correction_or_counterevidence": "The participant did measure the pallet obstruction objectively and did not accept the manager's verbal explanation for that issue. For the alarm-log gap, he requested independent monitoring-company records rather than relying on the manager's account. For the door closer, he later acknowledged that knowing it was a repeat finding would have changed his classification, indicating partial retrospective awareness.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were available in the analysis context. The 'affect heuristic' label and mechanism are drawn from established cognitive-science knowledge rather than retrieved corpus evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "truth bias",
      "alternative_labels": ["truth-default", "trust bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Failure to verify the building manager's claim that the door-closer maintenance ticket had already been logged the prior week",
      "supporting_interview_quote": "Not in the moment, no. I didn't pull the ticket timestamp, and I didn't cross-check last year's report right there. In hindsight I probably should have — turned out the ticket was only logged that morning, not the week before like he said, and there'd actually been a near-identical closer issue flagged and marked corrected in last year's inspection. So it wasn't new, it was a repeat. I didn't know that at the time I made the call, though.",
      "plausible_mechanism": "The participant may have defaulted to accepting the familiar manager's explanation as truthful and therefore did not trigger independent verification, despite later treating the alarm-log claim as requiring third-party records.",
      "why_not_identified": "The non-verification can be substantially explained by the same affective, low-friction response already captured by the affect heuristic occurrence, and the transcript does not explicitly show the participant affirmatively believing the manager's statement as opposed to simply not checking while focused on the person rather than the history."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "outcome bias",
      "alternative_labels": ["result bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Use of immediate on-site repair as a reason to record the serious fire-door deficiency as an advisory note",
      "supporting_interview_quote": "There's no equivalent independent record for a closer that's already been reattached; once it's fixed, the evidence is gone. So partly it was about what was still verifiable versus what wasn't.",
      "plausible_mechanism": "The positive immediate outcome, namely the manager remediating the visible defect on the spot, may have made the original deficiency feel less serious and therefore less citation-worthy, even though the code-violation status had already occurred.",
      "why_not_identified": "The transcript does not clearly show the participant judging the quality of the enforcement decision by the repair outcome; immediate correction is also a legitimate enforcement consideration, making the bias mechanism too ambiguous to count as identified."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper passages were provided in the analysis context, so corpus-supported labels and mechanisms were unavailable; labels rely on general established cognitive-science knowledge.",
    "The transcript is retrospective self-report rather than direct observation of the original inspection, so some reasoning may be reconstructed or rationalized after the fact.",
    "Only one speaker's account is available; the building manager and supervisor perspectives are reported indirectly.",
    "The analysis applies a conservative, mechanism-first standard and does not treat ordinary use of inspector discretion or cooperation-based leniency as a bias absent a distinct cognitive mechanism."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Biased_1_Sonar_off",
  "interview_id": "HE_Biased_1",
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
