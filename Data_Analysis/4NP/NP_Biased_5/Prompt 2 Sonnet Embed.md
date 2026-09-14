You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm trying to understand your reasoning process during the AFW procedure revision, not evaluating performance. Everything stays de-identified in my notes. Sound okay?

Participant: Sure, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me what this revision was for and why it came up?

Participant: So we had a design change package come through — the legacy analog level transmitter on one of the AFW trains got swapped for a new digital unit. Different response curve, different failure modes than what the old EOP steps were written around. My job was to update the Emergency Operating Procedure sequence so the initiation steps matched the new instrumentation, get it through V&V and human-factors review, and have it ready before the outage window opened. We had about three days.

Interviewer: What was your main objective going in?

Participant: Get an accurate, defensible procedure revision done on time. Accurate matters obviously, but the deadline was real — outage planning had already built the implementation window around this, so slipping it wasn't really an option without a whole scheduling conversation nobody wanted to have.

Interviewer: Walk me through the incident from the beginning.

Participant: Right when I started, an industry OE report landed in my queue — a transmitter failure at another station involving a new digital level transmitter. My first reaction was, okay, this is directly relevant, new digital unit, level transmitter, similar failure. I started pulling language from it into my draft pretty quickly. It was only later, when I looped in the I&C engineer who'd actually executed our design change, that he pointed out the OE unit used a different sensing technology than ours — different vendor family entirely. So the applicability wasn't as clean as I'd assumed.

From there I moved into drafting the actual verification steps. The new transmitter needed a two-point calibration check that the old analog unit never required. I've written a lot of these AFW revisions over the years, so I built the verification section using the template sequence I normally use. That went to peer review, and the reviewer caught that the calibration check wasn't in there at all — I'd basically carried over the old pattern without building it fresh around the new requirement.

Interviewer: What happened next?

Participant: I had to set validation criteria — basically, what surveillance test data to use as the benchmark for confirming the new steps work as intended. We've got five years of AFW surveillance history, but I also had a test from two weeks earlier on a different, unrelated procedure that happened to use a similar-looking verification form. That one was fresh in my head, so I anchored the validation criteria around it. Turned out later, when someone did a fuller data pull, that some of the older historical tests actually covered operating conditions closer to this transmitter's actual fault signature than the recent one did.

Interviewer: And the final stretch?

Participant: Last day, deadline under 24 hours out. I wanted to check the OE database more thoroughly, but part of it was locked because of a concurrent audit. So I worked off what I had — control room log, my own notes — and judged that was enough to close it out. I did a mental run-through of the failure modes and figured we'd covered the main ones, so I signed off and sent it to the approval board. They came back afterward asking for a supplemental risk note because there was a failure mode the draft hadn't addressed.

Interviewer: Let's go back to that OE report moment. What specifically made you decide it applied to your transmitter?

Participant: Honestly, the framing — "new digital level transmitter failure" — matched our situation closely enough that it registered as the same kind of event. I didn't stop to verify the sensing technology before I started drafting around it. In hindsight I probably should've asked the I&C engineer first, but it read as applicable on its face.

Interviewer: What alternatives did you consider there?

Participant: I could've tabled it as low relevance until I confirmed equivalence, or gone straight to the I&C engineer before touching the draft. I didn't do either — I just moved forward with incorporating it.

Interviewer: On the verification steps — what sources did you actually rely on when drafting?

Participant: Mostly my own prior work. I've done this enough times that I have a rhythm to how these sections get built. I did have the design change package open, but I wrote the structure first and meant to reconcile it against the specific requirements after — that reconciliation step is where the calibration check got missed.

Interviewer: Was consulting the I&C engineer before drafting ever on the table?

Participant: It was an option. I just didn't think I needed it at that stage — this felt like standard territory.

Interviewer: How did you decide which historical test data to weight most heavily for the validation criteria?

Participant: The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes. In hindsight, the older data had more operating conditions represented.

Interviewer: When time got short at the end, how did you decide the draft was ready to submit?

Participant: I looked at what was actually accessible — the control room log, my notes — and it felt like enough to call it done. The audit had the fuller OE records locked up, and requesting an extension felt like it would just push the whole outage schedule, so I didn't pursue that. On the risk side, I ran through the failure modes I could recall from the design package, felt like the major ones were addressed, and made the call that residual risk was acceptable.

Interviewer: Did escalating to the Shift Technical Advisor come up as an option?

Participant: It did cross my mind, but I didn't think the open question was significant enough to escalate at the time.

Interviewer: If you'd had another full day for the OE report review, would you have handled that differently?

Participant: Probably — I'd have gotten the I&C engineer's read on technical equivalence before drafting anything, rather than after.

Interviewer: If the audit hadn't locked the database, what would you have checked?

Participant: I'd have wanted to search for any other OE items involving this exact transmitter model, and cross-check the failure-mode list more completely instead of relying on memory.

Interviewer: Looking back, is there a point you'd have wanted a second set of eyes earlier?

Participant: Probably right after the OE report came in, before I started building language around it.

Interviewer: How confident were you in that final risk judgment at the time, compared to now?

Participant: At the time, reasonably confident — it felt sufficient given what I had access to. Now, knowing the board found a gap, I'd say I was more confident than the evidence actually supported.

Interviewer: That's really helpful. Thanks for walking through all of that in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Biased_5",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Procedure Engineer / Technical Procedure Writer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "AFW Instrumentation Procedure Revision Under Deadline",
    "scenario_summary_internal": "A procedure engineer at a nuclear station must revise the Emergency Operating Procedure (EOP) step sequence for Auxiliary Feedwater (AFW) initiation after a design change replaces an analog level transmitter with a new digital unit. The revision must be completed before the next scheduled outage window closes, incorporating a newly issued industry Operating Experience (OE) report describing an instrumentation-related event at another plant. The engineer works through triage of the OE report, drafting of validation steps, weighting of historical test data, and final sign-off under time pressure, each step offering at least two plausible paths.",
    "occupational_realism": {
      "objective": "Revise and validate the AFW initiation procedure steps to correctly reflect the new digital level transmitter before the outage-driven implementation deadline, while ensuring the change is defensible under the site's 10CFR50.59 screening and human-factors review.",
      "setting": "Procedure engineering office and control room simulator mock-up at a pressurized water reactor station, three days before the scheduled outage window for procedure implementation.",
      "constraints": [
        "Hard deadline tied to outage schedule; procedure must be approved before implementation window opens",
        "Limited access to the full OE database due to a concurrent audit locking some records",
        "Only one qualified peer reviewer available due to staffing rotation",
        "New transmitter has different response curve and failure modes than legacy unit",
        "Procedure change must pass human-factors and V&V review before submission to plant approval board"
      ],
      "stakeholders": [
        "Procedure Engineer (interviewee)",
        "Shift Technical Advisor",
        "Instrumentation & Controls engineer who executed the design change",
        "Independent peer reviewer",
        "Outage planning coordinator",
        "Plant approval board"
      ],
      "technical_terms_to_use": [
        "Emergency Operating Procedure (EOP)",
        "Auxiliary Feedwater (AFW)",
        "level transmitter",
        "setpoint",
        "Operating Experience (OE) report",
        "design change package",
        "10CFR50.59 screening",
        "verification and validation (V&V)",
        "independent peer review",
        "surveillance test",
        "control room walkthrough",
        "nonconformance report"
      ],
      "technical_terms_to_avoid": [
        "similarity bias",
        "habit intrusion",
        "bounded rationality",
        "recency bias",
        "imperfect rationality",
        "cognitive bias",
        "heuristic error"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "A new OE report describes a transmitter failure at another station using a similar-looking digital unit from a different vendor family",
          "The design change package for this station's new transmitter has different calibration and failure-mode documentation",
          "Outage schedule leaves limited time to fully cross-reference the OE report against the local design change"
        ],
        "new_information_after_decision": [
          "The I&C engineer later notes the OE report's transmitter uses a different sensing technology than the one installed locally"
        ],
        "alternatives": [
          "Treat the OE report as directly applicable and adopt its recommended step language without further comparison",
          "Request the I&C engineer confirm technical equivalence between the two transmitter models before incorporating OE guidance",
          "Table the OE report as low relevance and proceed with the original design change package only"
        ],
        "intended_action": "Engineer judges the OE event as applicable based on surface resemblance (both are 'new digital level transmitters') and begins drafting revised steps around it."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The new transmitter requires a distinct verification step involving a two-point calibration check not previously required for the legacy analog unit",
          "The engineer has written dozens of prior AFW-related procedure revisions using a standard verification template",
          "Time is limited before the draft must go to peer review"
        ],
        "new_information_after_decision": [
          "The peer reviewer flags that the two-point calibration check is missing from the draft"
        ],
        "alternatives": [
          "Draft the new verification section from the design change package's specific requirements",
          "Reuse the standard template sequence from prior revisions and adapt wording only superficially",
          "Consult the I&C engineer directly before drafting any verification steps"
        ],
        "intended_action": "Engineer defaults to the familiar template sequence used across many past revisions, carrying over the accustomed verification pattern rather than building the sequence from the new transmitter's specific requirements."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The engineer has access to five years of historical AFW surveillance test data, plus a test performed just two weeks earlier on an unrelated but recently revised procedure",
          "The two-week-old test used a similar-looking verification form",
          "Older test data covers more operating conditions relevant to the current transmitter's failure modes"
        ],
        "new_information_after_decision": [
          "A later data review shows the older test set included conditions closer to the actual transmitter fault signature"
        ],
        "alternatives": [
          "Weight the full five-year historical data set proportionally to its relevance",
          "Anchor primarily on the two-week-old test as the most representative baseline",
          "Request additional historical data pulls before finalizing validation criteria"
        ],
        "intended_action": "Engineer gives outsized weight to the two-week-old test result when setting validation criteria, treating it as the most representative baseline because it is freshest in mind."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Deadline is now less than 24 hours away",
          "Only the control room log and the engineer's own notes are readily at hand; the locked-audit OE database section cannot be accessed in time",
          "The draft procedure has passed an initial informal check but not full independent V&V",
          "The engineer must judge whether residual failure-mode risk from the new transmitter is acceptable for submission"
        ],
        "new_information_after_decision": [
          "The approval board later requests a supplemental risk note before final sign-off, revealing a failure mode not addressed in the submitted draft"
        ],
        "alternatives": [
          "Submit the draft as sufficiently validated based on readily available records and proceed to approval",
          "Request a short extension to complete a fuller independent search of the OE database",
          "Escalate the unresolved failure-mode question to the Shift Technical Advisor before submission"
        ],
        "intended_action": "Engineer stops searching once the readily accessible records seem adequate (satisficing under time and access constraints), then finalizes a risk judgment using a simplified mental estimate of failure-mode coverage rather than a fuller structured analysis."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this procedure revision was for and why it came up?",
        "What was your main objective when you started this task?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "Walk me through each step you took from receiving the design change package to submitting the draft.",
        "What new information came in as you worked through the revision?"
      ],
      "decision_point_probes": [
        "At the point you reviewed the OE report, what made you decide it applied to this transmitter?",
        "When drafting the verification steps, what sources did you rely on and why?",
        "How did you decide which historical test data to weight most heavily?",
        "When time got short, how did you decide the draft was ready to submit?",
        "What alternatives did you consider at each of these points, and why did you rule them out?"
      ],
      "closing_hypotheticals": [
        "If you'd had another full day, would you have approached the OE report review differently?",
        "If the audit hadn't locked part of the OE database, what would you have checked?",
        "Looking back, is there a point where you'd have wanted a second set of eyes earlier?",
        "How confident were you in the final risk judgment at the time, versus now?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "sb_01",
        "bias": "Similarity Bias",
        "decision_point": 1,
        "mechanism": "Engineer judges the OE report applicable to the local design change primarily because both involve 'new digital level transmitters,' relying on surface-level resemblance rather than confirmed technical equivalence.",
        "affected_reasoning_operation": "Relevance/applicability judgment during evidence triage",
        "evidence_available_at_time": [
          "OE report describing a different vendor's transmitter",
          "Local design change package with distinct calibration and failure-mode documentation"
        ],
        "required_textual_manifestation": "Engineer states the OE event 'looked like the same kind of situation' and proceeds to incorporate its guidance before checking whether the sensing technologies match.",
        "plausible_nonbias_interpretation": "A cautious engineer might reasonably treat any OE report on similar equipment as worth incorporating as a precaution, regardless of exact technical match.",
        "strength": "subtle",
        "do_not_make_explicit": ["similarity", "bias", "surface resemblance"]
      },
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "decision_point": 2,
        "mechanism": "Engineer's drafting defaults to the standard verification template used across numerous prior AFW procedure revisions, a well-practiced behavioral pattern, rather than being generated fresh from the new transmitter's specific design change requirements.",
        "affected_reasoning_operation": "Action selection during procedure drafting",
        "evidence_available_at_time": [
          "Design change package specifying a distinct two-point calibration requirement",
          "Engineer's long history of writing similar procedures with a standard template"
        ],
        "required_textual_manifestation": "Engineer describes writing the verification section 'the way I always do it' before realizing later that the template didn't include the new calibration step.",
        "plausible_nonbias_interpretation": "Using a proven template could be a reasonable efficiency practice when time is short, not necessarily an error.",
        "strength": "moderate",
        "do_not_make_explicit": ["habit", "intrusion", "automatic pattern"]
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "decision_point": 3,
        "mechanism": "Engineer disproportionately weights the two-week-old test result as the representative baseline for validation criteria, despite older historical data covering conditions more relevant to the transmitter's actual failure signature.",
        "affected_reasoning_operation": "Evidence weighting during validation-criteria setting",
        "evidence_available_at_time": [
          "Five years of historical AFW surveillance test data",
          "A recent (two-week-old) test using a similar-looking form"
        ],
        "required_textual_manifestation": "Engineer explains choosing the recent test as the anchor because 'it was the freshest data I had in mind,' without weighing it against the fuller historical set.",
        "plausible_nonbias_interpretation": "Recent test data could genuinely be considered more current and thus preferable on procedural-currency grounds.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency", "bias", "freshest in mind"]
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 4,
        "mechanism": "Under deadline and access constraints, engineer stops the information search once readily available records (control room log, own notes) seem minimally sufficient, rather than continuing to seek fuller information as an unconstrained search would.",
        "affected_reasoning_operation": "Information-gathering termination decision",
        "evidence_available_at_time": [
          "Locked audit preventing full OE database access",
          "Control room log and personal notes readily accessible",
          "Less than 24 hours remaining before deadline"
        ],
        "required_textual_manifestation": "Engineer states they 'went with what was on hand because there wasn't time to dig further,' treating the limited accessible evidence as adequate for closure.",
        "plausible_nonbias_interpretation": "Given a genuine hard deadline and blocked database access, stopping the search could be a reasonable resource-constrained judgment call.",
        "strength": "moderate",
        "do_not_make_explicit": ["bounded rationality", "satisficing", "limited search"]
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "decision_point": 4,
        "mechanism": "In forming the final risk judgment on residual failure-mode coverage, engineer relies on a simplified mental estimate ('it's probably fine, most of the cases are covered') rather than a structured comparison against the full failure-mode list, producing a judgment that deviates from what a fuller analysis would show.",
        "affected_reasoning_operation": "Final risk-acceptability synthesis prior to submission",
        "evidence_available_at_time": [
          "Draft procedure with incomplete independent V&V",
          "Partial failure-mode documentation from the design change package",
          "Engineer's own rough mental tally of covered versus uncovered scenarios"
        ],
        "required_textual_manifestation": "Engineer describes concluding the residual risk was acceptable based on a quick mental tally rather than a systematic failure-mode-by-failure-mode check, later shown incomplete when the approval board requests a supplemental risk note.",
        "plausible_nonbias_interpretation": "Experienced engineers often use rapid holistic judgment as legitimate expert shortcut when full analysis isn't feasible in time available.",
        "strength": "moderate",
        "do_not_make_explicit": ["imperfect rationality", "systematic deviation", "heuristic judgment"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for biased condition; no control variant generated under this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable — no counterfactual condition requested",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Exactly 5 total bias instances planned across exactly 4 decision points",
      "No decision point contains more than one instance of the same bias",
      "Decision point 4 contains two distinct biases (Bounded Rationality, Imperfect Rationality) with clearly differentiated reasoning operations (search termination vs. final judgment synthesis)",
      "No bias label, definition, or psychological terminology appears in probe_plan or timeline wording",
      "Each instance has a plausible non-bias explanation to avoid mechanical detectability",
      "Target word count 1,215–1,485 achievable given 4 decision points with moderate probe depth"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Similarity Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Habit Intrusion",
        "occurrences": 1,
        "mechanism_constraint": "human performance often can be captured by familiar behavioral patterns that occur so frequently in their experiences."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Recency Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Imperfect Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Similarity Bias",
      "Habit Intrusion",
      "Bounded Rationality",
      "Recency Bias",
      "Imperfect Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Similarity Bias", "requested_occurrences": 1},
      {"bias": "Habit Intrusion", "requested_occurrences": 1},
      {"bias": "Bounded Rationality", "requested_occurrences": 1},
      {"bias": "Recency Bias", "requested_occurrences": 1},
      {"bias": "Imperfect Rationality", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "sb_01", "bias": "Similarity Bias"},
      {"instance_id": "hi_01", "bias": "Habit Intrusion"},
      {"instance_id": "rb_01", "bias": "Recency Bias"},
      {"instance_id": "br_01", "bias": "Bounded Rationality"},
      {"instance_id": "ir_01", "bias": "Imperfect Rationality"}
    ],
    "intended_decision_points": [
      {"instance_id": "sb_01", "bias": "Similarity Bias", "decision_point": 1},
      {"instance_id": "hi_01", "bias": "Habit Intrusion", "decision_point": 2},
      {"instance_id": "rb_01", "bias": "Recency Bias", "decision_point": 3},
      {"instance_id": "br_01", "bias": "Bounded Rationality", "decision_point": 4},
      {"instance_id": "ir_01", "bias": "Imperfect Rationality", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sb_01",
        "bias": "Similarity Bias",
        "mechanism": "Applicability judged from surface resemblance between OE report equipment and local transmitter rather than confirmed technical equivalence",
        "affected_reasoning_operation": "Relevance/applicability judgment during evidence triage",
        "evidence_source": "OE report vs. local design change package",
        "distinctiveness_requirement": "Only instance of Similarity Bias; occurs solely at decision point 1 during initial OE triage, not repeated elsewhere"
      },
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "mechanism": "Well-practiced standard procedure-writing template is applied automatically instead of the new transmitter's specific requirements",
        "affected_reasoning_operation": "Action selection during procedure drafting",
        "evidence_source": "Design change package requirement vs. engineer's habitual template use",
        "distinctiveness_requirement": "Only instance of Habit Intrusion; occurs solely at decision point 2 during drafting, distinct from OE triage or data weighting"
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "mechanism": "Most recently encountered test result is disproportionately weighted as the representative baseline over more relevant older historical data",
        "affected_reasoning_operation": "Evidence weighting during validation-criteria setting",
        "evidence_source": "Five-year historical test data vs. two-week-old test result",
        "distinctiveness_requirement": "Only instance of Recency Bias; occurs solely at decision point 3 during data weighting, distinct from drafting or final judgment"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Information search terminated once readily accessible records seem minimally sufficient, under time and access constraints, rather than continuing an exhaustive search",
        "affected_reasoning_operation": "Information-gathering termination decision",
        "evidence_source": "Control room log and personal notes vs. inaccessible locked OE database",
        "distinctiveness_requirement": "Shares decision point 4 with ir_01 but addresses the search-termination operation, using a different evidence source (accessible records) and occurring earlier in the DP4 sequence than the final judgment"
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Final risk-acceptability judgment relies on a simplified holistic mental estimate rather than structured failure-mode-by-failure-mode analysis",
        "affected_reasoning_operation": "Final risk-acceptability synthesis prior to submission",
        "evidence_source": "Partial failure-mode documentation and engineer's own rough mental tally",
        "distinctiveness_requirement": "Shares decision point 4 with br_01 but addresses the final judgment-synthesis operation, occurring after the search-termination step and using the incomplete failure-mode list as its distinct evidence basis"
      }
    ],
    "intended_strength": [
      {"instance_id": "sb_01", "bias": "Similarity Bias", "strength": "subtle"},
      {"instance_id": "hi_01", "bias": "Habit Intrusion", "strength": "moderate"},
      {"instance_id": "rb_01", "bias": "Recency Bias", "strength": "subtle"},
      {"instance_id": "br_01", "bias": "Bounded Rationality", "strength": "moderate"},
      {"instance_id": "ir_01", "bias": "Imperfect Rationality", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Not applicable — no counterfactual condition requested",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Biased_5",
    "domain_id": "NP",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences distributed across 4 decision points by mechanism fit and narrative realism: one bias per decision point at DPs 1-3 (Similarity Bias at OE triage, Habit Intrusion at drafting, Recency Bias at data weighting), with two distinct biases (Bounded Rationality, Imperfect Rationality) co-located at DP4 because both naturally arise under the same terminal time-pressured submission decision but target different reasoning operations (search termination vs. final judgment synthesis) with separate evidence sources, satisfying the same-bias co-location restriction and the distinct-evidence requirement.",
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
          "segment_type": "decision_episode",
          "raw_interview_anchor": "Initial OE report applicability assessment: the participant called the report directly relevant and began pulling language into the draft before checking sensing technology or vendor family.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sb_01"
          ],
          "ground_truth_rationale": "Surface resemblance drove the relevance judgment before technical equivalence was verified."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_episode",
          "raw_interview_anchor": "Verification section drafting: the participant used the familiar template sequence, and peer review later found the new two-point calibration check missing.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "hi_01"
          ],
          "ground_truth_rationale": "A practiced prior template displaced construction from the new transmitter requirements."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "decision_episode",
          "raw_interview_anchor": "Validation criteria selection: the participant anchored on a two-week-old unrelated test because it was fresh and top of mind instead of systematically comparing the five-year history.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rb_01"
          ],
          "ground_truth_rationale": "The recent test was overweighted despite older data being more relevant to the fault signature."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_episode",
          "raw_interview_anchor": "Search termination under deadline: with the OE database locked, the participant worked from the control-room log and personal notes, judged them sufficient, and did not seek an extension.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "br_01"
          ],
          "ground_truth_rationale": "The information search stopped at readily accessible records under time and access constraints."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "decision_episode",
          "raw_interview_anchor": "Final risk synthesis: the participant mentally ran through recalled failure modes, judged residual risk acceptable, signed off, and later acknowledged confidence exceeded the evidence.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ir_01"
          ],
          "ground_truth_rationale": "Final acceptability was based on a quick mental coverage estimate rather than a structured failure-mode comparison."
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
    "analysis_scope_note": "Conservative, mechanism-first analysis of participant reasoning during an AFW procedure revision; only transcript-affirmed bias mechanisms are classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "overconfidence bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging relevance or category membership by resemblance to a salient prototype rather than by diagnostically relevant underlying features.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial assessment of OE report relevance",
      "decision_point_description": "Deciding whether to incorporate the new digital-transmitter OE report into the draft before verifying technical equivalence.",
      "affected_reasoning_operation": "Similarity-based categorization of an operational event as applicable",
      "bias_specific_mechanism": "Salient surface framing, 'new digital level transmitter failure,' activated a same-category prototype and led to a premature applicability judgment without checking underlying sensing technology or vendor family.",
      "manifestation_in_interview": "The participant saw the OE report as directly relevant based on surface similarity, began drafting from it, and only later learned from the I&C engineer that the OE unit used a different sensing technology and vendor family.",
      "effect_on_reasoning_or_decision": "It led to incorporating OE language into the draft before technical equivalence was confirmed, requiring later correction by the I&C engineer and creating rework in the revision process.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right when I started, an industry OE report landed in my queue — a transmitter failure at another station involving a new digital level transmitter. My first reaction was, okay, this is directly relevant, new digital unit, level transmitter, similar failure. I started pulling language from it into my draft pretty quickly.",
          "evidence_explanation": "Shows immediate similarity-based relevance judgment and drafting action before verification of technical equivalence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the framing — 'new digital level transmitter failure' — matched our situation closely enough that it registered as the same kind of event. I didn't stop to verify the sensing technology before I started drafting around it.",
          "evidence_explanation": "Explicitly identifies surface framing as the basis for same-category judgment and acknowledges failure to verify the diagnostically relevant underlying feature."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I could've tabled it as low relevance until I confirmed equivalence, or gone straight to the I&C engineer before touching the draft. I didn't do either — I just moved forward with incorporating it.",
          "evidence_explanation": "Demonstrates that alternative verification pathways were available and that the biased similarity judgment directly shaped the decision to proceed."
        }
      ],
      "correction_or_counterevidence": "Later, the I&C engineer who executed the design change pointed out the OE unit used a different sensing technology and vendor family; the participant acknowledged in hindsight that he should have checked technical equivalence first.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported the representativeness heuristic; the label rests on established cognitive-science knowledge and is not represented as retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "recency effect",
      "alternative_labels": [
        "recency bias",
        "availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overweight or more clearly recall recently encountered information relative to older information, independent of its diagnostic relevance.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of historical test data for validation criteria",
      "decision_point_description": "Choosing which historical test data to use as the benchmark for validating the revised AFW procedure.",
      "affected_reasoning_operation": "Weighting and selection of historical test data for validation benchmarking",
      "bias_specific_mechanism": "A recent, top-of-mind test form from an unrelated procedure was used as a proxy and anchor because it was fresh in memory, without systematic comparison against the larger five-year historical dataset.",
      "manifestation_in_interview": "The participant anchored validation criteria around a two-week-old test from a different, unrelated procedure because it was 'fresh in my head,' rather than systematically comparing it with older AFW surveillance data.",
      "effect_on_reasoning_or_decision": "The validation criteria were built around less relevant recent data, while a later fuller data pull indicated that older historical tests more closely matched the transmitter's actual fault signature.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We've got five years of AFW surveillance history, but I also had a test from two weeks earlier on a different, unrelated procedure that happened to use a similar-looking verification form. That one was fresh in my head, so I anchored the validation criteria around it. Turned out later, when someone did a fuller data pull, that some of the older historical tests actually covered operating conditions closer to this transmitter's actual fault signature than the recent one did.",
          "evidence_explanation": "Shows temporal recency and top-of-mind salience caused the recent test to outweigh the broader historical dataset, with later evidence confirming the older tests were more relevant."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes. In hindsight, the older data had more operating conditions represented.",
          "evidence_explanation": "Explicitly attributes the selection to recent exposure and top-of-mind availability, and confirms the absence of a systematic relevance comparison."
        }
      ],
      "correction_or_counterevidence": "A later fuller data pull found that older historical tests covered operating conditions closer to the transmitter's actual fault signature; the participant acknowledged in hindsight that the older data had more relevant operating conditions represented.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Defines the recency effect as a memory bias favoring recent events.",
          "relevance_to_this_occurrence": "The participant's use of a recent, top-of-mind test from an unrelated procedure over older more relevant historical data instantiates the recency effect in validation benchmark selection."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "overconfidence bias",
      "alternative_labels": [
        "overconfidence effect",
        "calibration bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A miscalibration between subjective confidence and objective evidence, leading a person to overestimate the completeness or accuracy of a judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final readiness and risk judgment before submission",
      "decision_point_description": "Deciding that the draft was complete and residual risk acceptable without full database access or escalation.",
      "affected_reasoning_operation": "Risk assessment and sufficiency judgment under incomplete information",
      "bias_specific_mechanism": "Subjective confidence in the completeness of recalled failure modes and accessible records exceeded the available evidence, leading to a judgment that residual risk was acceptable without further information retrieval or escalation.",
      "manifestation_in_interview": "With the OE database partly locked and under time pressure, the participant relied on accessible notes and recalled failure modes, judged the major failure modes addressed, and signed off; the board later identified a gap.",
      "effect_on_reasoning_or_decision": "The participant submitted the procedure revision without a supplemental risk note or escalation; the approval board subsequently identified an unaddressed failure mode and required supplemental risk documentation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at what was actually accessible — the control room log, my notes — and it felt like enough to call it done. The audit had the fuller OE records locked up, and requesting an extension felt like it would just push the whole outage schedule, so I didn't pursue that. On the risk side, I ran through the failure modes I could recall from the design package, felt like the major ones were addressed, and made the call that residual risk was acceptable.",
          "evidence_explanation": "Shows the participant treated accessible records and memory-based failure-mode review as sufficient, and directly acted on that confidence by signing off."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At the time, reasonably confident — it felt sufficient given what I had access to. Now, knowing the board found a gap, I'd say I was more confident than the evidence actually supported.",
          "evidence_explanation": "Explicitly states that at-the-time confidence exceeded the available evidence, which is the core miscalibration of overconfidence."
        }
      ],
      "correction_or_counterevidence": "The approval board subsequently identified an unaddressed failure mode and asked for a supplemental risk note; the participant now judges his earlier confidence as exceeding the evidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported overconfidence bias; the label rests on established cognitive-science knowledge and is not represented as retrieved evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "mental set",
      "alternative_labels": [
        "Einstellung effect",
        "default bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Drafting verification steps for the new digital transmitter",
      "supporting_interview_quote": "I've written a lot of these AFW revisions over the years, so I built the verification section using the template sequence I normally use. That went to peer review, and the reviewer caught that the calibration check wasn't in there at all — I'd basically carried over the old pattern without building it fresh around the new requirement.",
      "plausible_mechanism": "A strong pre-existing response pattern for AFW verification sections led to automatic reuse of the old analog template, causing omission of the new two-point calibration check.",
      "why_not_identified": "Could not be affirmatively distinguished from ordinary skill-based omission or procedure/documentation error under time pressure; the transcript does not show sufficient bias-specific mechanism beyond reliance on a familiar template, and peer review caught the omission before final approval."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus coverage was sparse and did not include direct passages for representativeness heuristic or overconfidence bias; those labels rely on established general knowledge with disclosure.",
    "The interview is retrospective self-report; while statements were used conservatively, memory and hindsight may color some explanations.",
    "Some decision episodes, such as template reuse, were treated as candidates rather than identified biases because ordinary skill-based omission could not be ruled out."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Biased_5_Sonnet_on",
  "interview_id": "NP_Biased_5",
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
