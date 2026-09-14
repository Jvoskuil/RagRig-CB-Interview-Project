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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
