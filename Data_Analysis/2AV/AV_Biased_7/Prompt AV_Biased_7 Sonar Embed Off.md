You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and you're comfortable speaking openly about how the decisions unfolded?

Participant: Yes, that's fine. I've done these debriefs before after audits.

Interviewer: Great. Can you start by telling me your role and a bit about the situation we're discussing?

Participant: I'm the Continuing Airworthiness Manager for our turboprop fleet. This one involved a lease-return aircraft — we had five days to get it back to the lessor in contract condition, and during the pre-return borescope inspection, the hangar crew flagged hydraulic seepage at a fitting that had already come up twice in the prior eight months.

Interviewer: What was going through your mind when that finding came in?

Participant: Honestly, my first reaction was "there it is again." We'd seen this fitting seep before, logged it, and it never went anywhere. The reliability trend data showed the seepage rate was within MEL tolerance historically, so nothing about the number itself was alarming. But we were also five days from a contractual deadline with financial penalties attached, so I wanted to move quickly.

Interviewer: Walk me through what happened next, chronologically.

Participant: Sure. Day one, the borescope finding comes in. I pull up the maintenance history, see the two prior logs, and my line engineer — Tomas, he's been with us over twenty years — takes a look and says it's the same seepage pattern we've always seen. Day two, we're deciding how to formally classify it. Tomas is confident it's cosmetic, says this fitting type "just seeps, it doesn't fail badly." Day three, I pull the reliability dashboard for a broader read before writing the disposition memo. Day four and five, we're finalizing release paperwork against the clock, because MRO's engineering support was only contracted through day three.

Interviewer: Let's go back to that first day. What exactly made you comfortable classifying it as routine rather than escalating for expanded inspection?

Participant: The recurrence itself, honestly. Two prior instances, same location, same profile — it fit the pattern we'd already established for this aircraft. Once I saw the third one lined up with the first two, it read to me as confirmation that this was just how this particular fitting behaves, not something new developing. So I deferred it under MEL rather than pulling it into an unscheduled inspection.

Interviewer: Did you consider that three data points over eight months might not be enough to establish a real pattern?

Participant: I mean — in hindsight, sure, three isn't a huge number. But in the moment it felt consistent enough. It wasn't like the readings were random or inconsistent with each other.

Interviewer: What alternative did you weigh at that point?

Participant: The other option was escalating to Quality immediately for an expanded inspection. I set that aside because nothing in the numbers themselves crossed a threshold — it was really the shape of the recurrence that drove my read, not the raw values.

Interviewer: Moving to day two — Tomas's assessment. What was your process for validating what he told you?

Participant: Tomas has been doing this longer than almost anyone on my team. When he said this fitting type doesn't fail catastrophically, just seeps, that carries weight. We didn't commission a fault-tree analysis at that point — partly hangar time, partly that his read seemed like sufficient technical grounds on its own.

Interviewer: Was there a dissenting view from anyone else?

Participant: There was, actually. One of our junior engineers suggested we pull the torque and seal specs to check whether something in the installation had drifted. I didn't follow up on that. It felt like duplicating effort when Tomas had already given a clear read.

Interviewer: What would it have taken for you to pursue the junior engineer's suggestion instead?

Participant: Probably if Tomas himself had seemed less certain, or if the seepage rate had ticked up rather than stayed flat. Even setting his read aside, the earlier occurrences had stayed level and hadn't progressed into anything worse across those eight months, so a new failure mode showing up now just didn't seem likely to me. That's really what made the spec check feel unnecessary at that point.

Interviewer: Let's talk about day three, the reliability dashboard. What did that show you?

Participant: Green status for that defect category, fleet-wide. That was reassuring — I referenced it directly in the disposition memo as supporting evidence for continued airworthiness.

Interviewer: Did you check whether that green rating accounted for this tail number's specific recurrence history, or whether it was a fleet-average figure?

Participant: I didn't dig into the calculation, no. It's an approved tool, it's what we use for these calls day to day. Between the dashboard and Tomas's read, everything was pointing the same direction, so that consistency across sources gave me a fair amount of confidence in the memo's conclusion.

Interviewer: When you say "everything pointing the same direction" — did you consider that the dashboard and Tomas's assessment might share the same blind spot rather than genuinely corroborating each other?

Participant: That's a fair question. I didn't frame it that way at the time. It felt like two independent checks agreeing, which is usually a good sign.

Interviewer: Let's move to the final decision — releasing the aircraft. What was the state of play by day four?

Participant: MRO's engineering support had already left, deadline was two days out, and the seepage was still within tolerance with no new defect. I authorized release to service and we returned the aircraft on schedule. I did flag a borescope recheck for the next inspection interval, but didn't make it mandatory before dispatch.

Interviewer: How much did the two-day deadline weigh on that call?

Participant: Some, sure — everyone in this industry feels the schedule. But I want to be clear, my release decision itself was based on the tolerance readings and history, not the clock. Other managers might let a deadline push them into a call they're not comfortable with. I don't think that happened here.

Interviewer: You mentioned earlier that hangar pressure and the departing MRO support were very much on your mind through days two and three. How does that square with the release decision being unaffected by timing?

Participant: I see what you're asking. I suppose the schedule was in the background the whole way through — I just don't experience it as something that colors my technical judgment specifically at the end.

Interviewer: What gave you confidence specifically in this aircraft, as opposed to the fitting type generally?

Participant: Fifteen years at this airline, and I've never seen this exact fitting fail badly on any tail. That history made me comfortable that this one would be fine, even with the root cause investigation still technically open.

Interviewer: If a completed fault-tree analysis had already been finished and available before you finalized the disposition memo, with the same five-day return window in place, would anything have gone differently?

Participant: Possibly. If the analysis had come back clean, I'd have felt more settled citing it directly instead of leaning as much on Tomas's read and the dashboard together. If it had flagged something, obviously that changes the whole memo. Either way, I think I'd have leaned less on the two of those lining up and more on an actual finding.

Interviewer: And if a less senior engineer had given you the same "it just seeps" assessment — would you have weighed it the same way?

Participant: Probably not as heavily. Tomas's tenure is a big part of why that carried the weight it did.

Interviewer: Looking back, what would you do differently if this situation happened again tomorrow?

Participant: I'd probably push harder for that fault-tree analysis before finalizing the disposition, and maybe not treat the recurrence pattern alone as settling the question so early. The return itself went smoothly, but I know that on its own doesn't really tell us whether the process behind it was solid — it just means nothing surfaced in that window.

Interviewer: That's helpful context. Thank you for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Biased_7",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Continuing Airworthiness Manager (CAMO)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Recurring Hydraulic Leak Report",
    "scenario_summary_internal": "A CAMO manager at a regional airline oversees continuing airworthiness for a fleet of turboprops. A recurring but historically minor hydraulic seepage finding on one aircraft resurfaces during a pre-lease-return inspection window, coinciding with heavy schedule pressure and an experienced line engineer's reassurance. The manager must decide how to classify, defer, or escalate the finding across four sequential decisions, ultimately releasing the aircraft to service before a full root-cause investigation is closed out.",
    "occupational_realism": {
      "objective": "Determine airworthiness disposition of a recurring hydraulic seepage finding on a leased turboprop before a contractual lease-return deadline, while maintaining fleet dispatch reliability.",
      "setting": "Regional airline CAMO office and hangar line maintenance, mid-size fleet, third-party MRO involvement, lease-return inspection window with a fixed deadline in five days.",
      "constraints": [
        "Contractual lease-return deadline in five days with financial penalty for delay",
        "Limited hangar slot availability shared with two other aircraft",
        "MRO third-party engineering support only available for two more days",
        "Minimum equipment list and deferred defect procedures must be followed",
        "Regulatory reporting obligations for recurring defects"
      ],
      "stakeholders": [
        "CAMO Manager (interviewee)",
        "Line Maintenance Engineer (experienced, 22 years)",
        "Quality/Airworthiness Review Board",
        "Lessor's technical representative",
        "Fleet operations/scheduling manager"
      ],
      "technical_terms_to_use": [
        "MEL (Minimum Equipment List)",
        "deferred defect",
        "hydraulic seepage vs. leakage classification",
        "root cause analysis",
        "airworthiness directive",
        "reliability program trend data",
        "borescope inspection",
        "release to service"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "cognitive error",
        "psychological terminology"
      ],
      "timeline": [
        {
          "phase": 1,
          "decision_point": true,
          "facts_available_before_decision": [
            "Routine borescope and visual inspection flags hydraulic seepage at a fitting previously logged twice in the past 8 months",
            "Reliability trend data shows seepage rate within MEL tolerance historically",
            "Lease-return deadline is five days away"
          ],
          "new_information_after_decision": [
            "Line engineer notes the seepage pattern looks 'the same as always' and recommends standard wipe-and-monitor procedure",
            "No immediate escalation to Quality is made"
          ],
          "alternatives": [
            "Classify as routine recurring seepage and defer per MEL",
            "Escalate immediately for expanded inspection given recurrence"
          ],
          "intended_action": "Manager accepts the recurring classification and defers further action, treating the third occurrence as consistent with the prior benign pattern."
        },
        {
          "phase": 2,
          "decision_point": true,
          "facts_available_before_decision": [
            "Line engineer, citing decades of experience, states this fitting type 'never fails badly, it just seeps'",
            "No formal fault-tree or updated root cause analysis has been run for this tail number",
            "Hangar slot pressure is increasing"
          ],
          "new_information_after_decision": [
            "Manager defers ordering a full fault-tree analysis, relying on the engineer's judgment as sufficient technical basis",
            "A junior engineer's suggestion to pull torque and seal specs is not followed up"
          ],
          "alternatives": [
            "Commission a fault-tree/root cause analysis before further disposition",
            "Rely on the experienced engineer's field judgment and proceed to interim clearance"
          ],
          "intended_action": "Manager treats the engineer's confident assessment as equivalent to a validated technical finding and proceeds without independent analysis."
        },
        {
          "phase": 3,
          "decision_point": true,
          "facts_available_before_decision": [
            "Reliability program report (auto-generated trend dashboard) shows a green status indicator for this defect category fleet-wide",
            "The dashboard's green rating is based on fleet-average data, not this specific tail number's recurrence pattern",
            "Two hangar days remain before MRO support departs"
          ],
          "new_information_after_decision": [
            "Manager cites the dashboard's green status in the disposition memo as primary justification for continued airworthiness",
            "No manual cross-check of tail-specific history against the fleet-average calculation is performed"
          ],
          "alternatives": [
            "Treat the dashboard's green indicator as one input requiring manual verification against tail-specific history",
            "Accept the automated trend status as sufficient standalone justification for release"
          ],
          "intended_action": "Manager defers to the automated reliability dashboard output as authoritative without checking whether it accounts for the specific aircraft's repeat pattern."
        },
        {
          "phase": 4,
          "decision_point": true,
          "facts_available_before_decision": [
            "Deadline is now two days away; MRO engineering support has left",
            "No new defect has appeared since the last inspection, and the seepage measurement is technically within tolerance",
            "Manager has never seen this specific fitting fail catastrophically at this airline in 15 years"
          ],
          "new_information_after_decision": [
            "Aircraft is released to service and returned to the lessor on schedule",
            "A follow-up borescope inspection recommendation for the next check interval is noted but not made mandatory before dispatch"
          ],
          "alternatives": [
            "Release the aircraft on schedule based on current tolerance readings and past benign history",
            "Request a short deadline extension from the lessor to complete a mandatory root cause closure first"
          ],
          "intended_action": "Manager releases the aircraft on schedule, confident that because no serious failure has occurred before, none will occur now, without recognizing the deadline pressure's influence on that confidence."
        }
      ]
    },
    "probe_plan": {
      "opening": [
        "Can you walk me through what this aircraft's maintenance history looked like going into this inspection cycle?",
        "What was your primary objective during this five-day window?"
      ],
      "timeline_reconstruction": [
        "What specific data or reports did you review before each disposition decision?",
        "Who did you consult, and what did they tell you?",
        "What changed in the information you had between the first and last decision?"
      ],
      "decision_point_probes": [
        "At the point of the third seepage finding, what made you classify it the way you did?",
        "When the line engineer gave his assessment, what independent verification, if any, did you seek?",
        "How did you interpret the reliability dashboard's status indicator, and did you check what data it was built from?",
        "What made you confident enough to release the aircraft at the final deadline?"
      ],
      "decision_basis_and_alternatives": [
        "What alternative actions did you consider at each stage, and why were they set aside?",
        "Looking back, what other explanations could account for the recurring seepage pattern?"
      ],
      "prior_experience_and_time_pressure": [
        "How did your past experience with this fitting type shape your read of the situation?",
        "How much did the lease-return deadline weigh on your decisions at each stage?"
      ],
      "uncertainty_and_hypotheticals": [
        "What was your level of certainty at each decision point, on reflection?",
        "If the deadline had been three weeks out instead of five days, would any decision have changed?",
        "If a different engineer, with less seniority, had given the same assessment, would you have weighed it differently?"
      ],
      "closing_hypotheticals": [
        "If you had to make this same disposition decision again today, what would you do differently, if anything?",
        "What would have needed to be different in the data for you to escalate at the first decision point?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "AV7_apo_01",
        "bias": "Apophenia or Correlation Bias",
        "decision_point": 1,
        "mechanism": "Manager perceives the third seepage occurrence as confirming a stable, meaningful pattern ('consistent with prior benign behavior') from only two prior data points, treating recurrence itself as evidence of harmlessness rather than as an unresolved trend needing investigation.",
        "affected_reasoning_operation": "Pattern classification from limited historical data",
        "evidence_available_at_time": [
          "Two prior seepage logs in 8 months",
          "Reliability trend data showing tolerance-range values"
        ],
        "required_textual_manifestation": "Manager explicitly states the third finding 'fits the pattern we've seen before' and treats that perceived pattern as itself justifying deferral, without acknowledging the small sample size.",
        "plausible_nonbias_interpretation": "MEL procedures may legitimately permit deferral for seepage within tolerance regardless of recurrence count.",
        "strength": "subtle",
        "do_not_make_explicit": ["pattern recognition fallacy", "correlation vs causation", "small sample size"]
      },
      {
        "instance_id": "AV7_aut_01",
        "bias": "Automaticity or Automation Bias",
        "decision_point": 3,
        "mechanism": "Manager accepts the automated reliability dashboard's green/fleet-average status as authoritative justification without manually verifying it reflects this tail number's specific recurrence history.",
        "affected_reasoning_operation": "Evidence weighting and verification of automated output",
        "evidence_available_at_time": [
          "Dashboard green status indicator",
          "Underlying fleet-average (not tail-specific) data basis"
        ],
        "required_textual_manifestation": "Manager cites the dashboard status in the disposition memo as primary justification and does not describe checking whether it accounted for this aircraft's specific repeat pattern.",
        "plausible_nonbias_interpretation": "The dashboard may be a validated, approved tool that management is procedurally entitled to rely on.",
        "strength": "moderate",
        "do_not_make_explicit": ["automation reliance", "verification failure"]
      },
      {
        "instance_id": "AV7_bbs_01",
        "bias": "Bias Blind Spot",
        "decision_point": 4,
        "mechanism": "When asked how deadline pressure influenced the decision, manager acknowledges pressure exists generally in the industry but asserts their own final release decision was purely technical and unaffected by the deadline, despite describing timeline strain throughout the account.",
        "affected_reasoning_operation": "Self-assessment of one's own decision influences during a probe response",
        "evidence_available_at_time": [
          "Manager's own prior statements about escalating schedule pressure",
          "Explicit probe question about deadline influence"
        ],
        "required_textual_manifestation": "Manager states something like 'other managers might rush under deadline pressure, but I based this strictly on the numbers' immediately after having described the tightening schedule as a factor in earlier decisions.",
        "plausible_nonbias_interpretation": "The manager could genuinely have compartmentalized schedule awareness from the technical judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["blind spot", "self versus others asymmetry"]
      },
      {
        "instance_id": "AV7_norm_01",
        "bias": "Normalcy Bias",
        "decision_point": 2,
        "mechanism": "Manager assumes the situation will continue behaving as it always has ('it just seeps, never fails badly') and does not seriously entertain that a departure from the established pattern is possible, despite no root cause analysis ever being performed.",
        "affected_reasoning_operation": "Risk projection under uncertainty",
        "evidence_available_at_time": [
          "Absence of a formal root cause or fault-tree analysis for this tail number",
          "Engineer's characterization of the fitting type's typical behavior"
        ],
        "required_textual_manifestation": "Manager repeats an assumption of continuity ('it's always behaved this way, so it will keep behaving this way') as sufficient basis to skip deeper analysis.",
        "plausible_nonbias_interpretation": "Fitting-type behavior may be well documented industry-wide as low-risk, making continuity a reasonable technical assumption.",
        "strength": "subtle",
        "do_not_make_explicit": ["normalcy", "assumption of continuity"]
      },
      {
        "instance_id": "AV7_exp_01",
        "bias": "Experience Bias or Trusting expert intuition",
        "decision_point": 2,
        "mechanism": "Manager substitutes the senior line engineer's confident field intuition for a structured technical analysis (fault-tree/root cause), treating years of experience as sufficient evidentiary weight to bypass the junior engineer's suggested spec check.",
        "affected_reasoning_operation": "Evidence source selection and weighting",
        "evidence_available_at_time": [
          "Senior engineer's 22 years of experience and confident verbal assessment",
          "Junior engineer's unaddressed suggestion to pull torque/seal specifications"
        ],
        "required_textual_manifestation": "Manager explains deferring to the senior engineer's judgment specifically because of his tenure, and states the junior engineer's suggestion was not pursued as a result.",
        "plausible_nonbias_interpretation": "Deferring to the most experienced technician on a routine finding is a standard and often appropriate practice in maintenance operations.",
        "strength": "moderate",
        "do_not_make_explicit": ["expert intuition substitution", "seniority weighting"]
      },
      {
        "instance_id": "AV7_iov_01",
        "bias": "Illusion of Validity",
        "decision_point": 3,
        "mechanism": "Manager expresses high subjective confidence in the disposition memo's conclusion because the dashboard output and the engineer's assessment 'lined up consistently,' treating this internal consistency as proof of accuracy despite neither source having been independently validated against tail-specific data.",
        "affected_reasoning_operation": "Confidence calibration based on convergence of unverified sources",
        "evidence_available_at_time": [
          "Dashboard green status",
          "Engineer's verbal reassurance",
          "Absence of independent tail-specific verification"
        ],
        "required_textual_manifestation": "Manager states confidence was high specifically because 'everything pointed the same direction,' without noting that the sources shared the same underlying gap in tail-specific verification.",
        "plausible_nonbias_interpretation": "Convergent evidence from multiple independent sources can legitimately increase confidence when the sources are genuinely independent.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusion of validity", "false convergence"]
      },
      {
        "instance_id": "AV7_opt_01",
        "bias": "Optimism Bias",
        "decision_point": 4,
        "mechanism": "Manager releases the aircraft believing failure is unlikely specifically for this aircraft because of 15 years of personal experience without a catastrophic failure, projecting a favorable outcome for this specific case despite the unresolved investigation, rather than assessing base-rate risk neutrally.",
        "affected_reasoning_operation": "Outcome probability estimation under time pressure",
        "evidence_available_at_time": [
          "15-year personal failure-free history with this fitting type",
          "Unclosed root cause investigation status",
          "Two-day remaining deadline"
        ],
        "required_textual_manifestation": "Manager states confidence that 'this one will be fine' based on personal failure-free history, framing the specific release decision as low-risk without referencing the still-open investigation status.",
        "plausible_nonbias_interpretation": "A genuinely low base rate of failure for this fitting type could justify proceeding even without a closed investigation.",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "base rate neglect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition scenario with no paired control specified."
    },
    "counterfactual_specification": {
      "causal_variable": "Availability of a completed root cause / fault-tree analysis before the final release decision",
      "original_state": "No formal root cause analysis is performed; disposition relies on recurrence pattern, senior engineer intuition, and dashboard trend status",
      "counterfactual_state": "A completed fault-tree analysis is available before the final decision, providing an independently validated technical basis",
      "variables_to_hold_constant": [
        "Lease-return deadline and schedule pressure",
        "Aircraft type and defect history",
        "Personnel involved and their stated experience levels",
        "Reliability dashboard output and its underlying data basis"
      ],
      "expected_causal_difference": "With a validated fault-tree analysis available, the manager's confidence in the final release decision would rest on independently verified evidence rather than on convergent but unverified sources, altering the basis (though not necessarily the outcome) of the illusion-of-validity and experience-bias-driven decisions.",
      "causal_test_question": "Does the presence of an independently validated root cause analysis change how the manager weighs expert intuition and dashboard convergence when reaching the final release decision?"
    },
    "generation_checks": [
      "Exactly 7 biases requested, each with occurrences=1, totaling 7 planned instances",
      "Each instance assigned to a distinct decision point or distinct evidence/reasoning operation within a shared decision point",
      "No more than two instances of any bias share a decision point (max observed: 2, at decision points 2 and 3)",
      "Decision points 2 and 3 each host two distinct-bias instances with different evidence sources (engineer intuition vs. junior suggestion at DP2; dashboard vs. engineer convergence at DP3)",
      "No bias terminology, labels, or explanations appear in probe plan or timeline",
      "Target word count 1,350 (range 1,215-1,485) is achievable given 4 decision points, 7 embedded instances, and probe plan scope without repetitive exposition",
      "Consequences (on-time release, no immediate failure) do not mechanically prove or disprove bias presence"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Apophenia or Correlation Bias", "occurrences": 1, "mechanism_constraint": "Recurrence-as-pattern inference from limited sample"},
      {"bias": "Automaticity or Automation Bias", "occurrences": 1, "mechanism_constraint": "Unverified reliance on automated dashboard output"},
      {"bias": "Bias Blind Spot", "occurrences": 1, "mechanism_constraint": "Self-exemption from deadline pressure acknowledged generally in others"},
      {"bias": "Normalcy Bias", "occurrences": 1, "mechanism_constraint": "Assumption of behavioral continuity absent formal analysis"},
      {"bias": "Experience Bias or Trusting expert intuition", "occurrences": 1, "mechanism_constraint": "Seniority-based deference overriding structured analysis"},
      {"bias": "Illusion of Validity", "occurrences": 1, "mechanism_constraint": "Confidence from convergence of non-independent unverified sources"},
      {"bias": "Optimism Bias", "occurrences": 1, "mechanism_constraint": "Personal failure-free history projected onto specific unresolved case"}
    ],
    "target_bias_names": [
      "Apophenia or Correlation Bias",
      "Automaticity or Automation Bias",
      "Bias Blind Spot",
      "Normalcy Bias",
      "Experience Bias or Trusting expert intuition",
      "Illusion of Validity",
      "Optimism Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Apophenia or Correlation Bias", "requested_occurrences": 1},
      {"bias": "Automaticity or Automation Bias", "requested_occurrences": 1},
      {"bias": "Bias Blind Spot", "requested_occurrences": 1},
      {"bias": "Normalcy Bias", "requested_occurrences": 1},
      {"bias": "Experience Bias or Trusting expert intuition", "requested_occurrences": 1},
      {"bias": "Illusion of Validity", "requested_occurrences": 1},
      {"bias": "Optimism Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "AV7_apo_01", "bias": "Apophenia or Correlation Bias"},
      {"instance_id": "AV7_aut_01", "bias": "Automaticity or Automation Bias"},
      {"instance_id": "AV7_bbs_01", "bias": "Bias Blind Spot"},
      {"instance_id": "AV7_norm_01", "bias": "Normalcy Bias"},
      {"instance_id": "AV7_exp_01", "bias": "Experience Bias or Trusting expert intuition"},
      {"instance_id": "AV7_iov_01", "bias": "Illusion of Validity"},
      {"instance_id": "AV7_opt_01", "bias": "Optimism Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "AV7_apo_01", "bias": "Apophenia or Correlation Bias", "decision_point": 1},
      {"instance_id": "AV7_aut_01", "bias": "Automaticity or Automation Bias", "decision_point": 3},
      {"instance_id": "AV7_bbs_01", "bias": "Bias Blind Spot", "decision_point": 4},
      {"instance_id": "AV7_norm_01", "bias": "Normalcy Bias", "decision_point": 2},
      {"instance_id": "AV7_exp_01", "bias": "Experience Bias or Trusting expert intuition", "decision_point": 2},
      {"instance_id": "AV7_iov_01", "bias": "Illusion of Validity", "decision_point": 3},
      {"instance_id": "AV7_opt_01", "bias": "Optimism Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "AV7_apo_01",
        "bias": "Apophenia or Correlation Bias",
        "mechanism": "Treating third recurrence as confirming a meaningful stable pattern from a two-point history, using perceived pattern itself as justification for deferral",
        "affected_reasoning_operation": "Pattern classification from limited historical data",
        "evidence_source": "Two prior seepage logs plus current third finding",
        "distinctiveness_requirement": "Distinct from normalcy bias (AV7_norm_01) because this instance concerns inferring a causal/meaningful pattern from sparse data at intake, not assuming future continuity of an established norm at a later stage"
      },
      {
        "instance_id": "AV7_aut_01",
        "bias": "Automaticity or Automation Bias",
        "mechanism": "Accepting automated dashboard's fleet-average green status as authoritative without manual verification against tail-specific data",
        "affected_reasoning_operation": "Evidence weighting and verification of automated tool output",
        "evidence_source": "Reliability dashboard status indicator",
        "distinctiveness_requirement": "Distinct from illusion of validity (AV7_iov_01) because this instance is specifically about deferring to an automated system's output rather than about confidence arising from convergence of multiple sources"
      },
      {
        "instance_id": "AV7_bbs_01",
        "bias": "Bias Blind Spot",
        "mechanism": "Acknowledging deadline pressure affects others generally while denying it affected own final technical judgment, despite prior self-description of schedule strain",
        "affected_reasoning_operation": "Self-assessment during probe response about one's own decision influences",
        "evidence_source": "Manager's own probe response contrasted with earlier timeline statements",
        "distinctiveness_requirement": "Distinct from optimism bias (AV7_opt_01) because this instance concerns asymmetric self-perception of susceptibility to pressure, not projection of favorable outcome probability"
      },
      {
        "instance_id": "AV7_norm_01",
        "bias": "Normalcy Bias",
        "mechanism": "Assuming continued benign behavior of the fitting because it has always behaved that way, without seeking analysis that could reveal a departure from the pattern",
        "affected_reasoning_operation": "Risk projection under uncertainty at mid-timeline decision",
        "evidence_source": "Engineer's characterization of typical fitting behavior; absence of fault-tree analysis",
        "distinctiveness_requirement": "Distinct from experience bias (AV7_exp_01) at same decision point because this instance is the manager's own risk-continuity assumption, while AV7_exp_01 is the manager's deference to the engineer's authority/tenure as evidentiary substitute"
      },
      {
        "instance_id": "AV7_exp_01",
        "bias": "Experience Bias or Trusting expert intuition",
        "mechanism": "Substituting senior engineer's tenure-based confident intuition for structured fault-tree analysis, bypassing junior engineer's spec-check suggestion",
        "affected_reasoning_operation": "Evidence source selection and weighting based on perceived authority",
        "evidence_source": "Senior engineer's verbal assessment vs. junior engineer's unaddressed suggestion",
        "distinctiveness_requirement": "Distinct from normalcy bias (AV7_norm_01) at same decision point: this instance is about source authority/credibility weighting, not about assumed continuity of pattern"
      },
      {
        "instance_id": "AV7_iov_01",
        "bias": "Illusion of Validity",
        "mechanism": "High confidence in the disposition memo attributed to apparent consistency between dashboard status and engineer's reassurance, both of which share the same unverified data gap",
        "affected_reasoning_operation": "Confidence calibration based on convergence of unverified sources",
        "evidence_source": "Dashboard status plus engineer's verbal reassurance",
        "distinctiveness_requirement": "Distinct from automation bias (AV7_aut_01) at same decision point: this instance concerns confidence from perceived convergence across sources, not reliance on the automated source alone"
      },
      {
        "instance_id": "AV7_opt_01",
        "bias": "Optimism Bias",
        "mechanism": "Projecting favorable outcome for this specific aircraft based on personal 15-year failure-free history, disregarding the still-open investigation status",
        "affected_reasoning_operation": "Outcome probability estimation under time pressure at final decision",
        "evidence_source": "Personal historical experience; unresolved root cause investigation status",
        "distinctiveness_requirement": "Distinct from bias blind spot (AV7_bbs_01) at same decision point: this instance concerns favorable-outcome projection for the specific case, not self-exemption from a general susceptibility to pressure"
      }
    ],
    "intended_strength": [
      {"instance_id": "AV7_apo_01", "bias": "Apophenia or Correlation Bias", "strength": "subtle"},
      {"instance_id": "AV7_aut_01", "bias": "Automaticity or Automation Bias", "strength": "moderate"},
      {"instance_id": "AV7_bbs_01", "bias": "Bias Blind Spot", "strength": "subtle"},
      {"instance_id": "AV7_norm_01", "bias": "Normalcy Bias", "strength": "subtle"},
      {"instance_id": "AV7_exp_01", "bias": "Experience Bias or Trusting expert intuition", "strength": "moderate"},
      {"instance_id": "AV7_iov_01", "bias": "Illusion of Validity", "strength": "subtle"},
      {"instance_id": "AV7_opt_01", "bias": "Optimism Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Availability of a completed root cause / fault-tree analysis before final release decision",
      "original_state": "No formal root cause analysis performed before release",
      "changed_state": "Completed fault-tree analysis available before release",
      "variables_to_hold_constant": [
        "Lease-return deadline and schedule pressure",
        "Aircraft type and defect history",
        "Personnel involved and stated experience levels",
        "Reliability dashboard output and its underlying data basis"
      ]
    },
    "scenario_id": "AV_Biased_7",
    "domain_id": "AV",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Automatic assignment per mechanism fit and narrative realism: one instance per decision point 1 and 4 respectively (single-bias focus), two distinct-bias instances each sharing decision points 2 and 3 (each pair using different evidence sources and reasoning operations per instance independence rule); no bias exceeds one occurrence; no decision point hosts more than two total bias instances.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Lease-return deadline and schedule pressure",
      "Aircraft type and defect history",
      "Personnel involved and stated experience levels",
      "Reliability dashboard output and its underlying data basis"
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
        "segment_type": "initial evidence interpretation and urgency",
        "raw_interview_anchor": "My first reaction was 'there it is again' ... the seepage rate was within MEL tolerance historically ... we were also five days from a contractual deadline ... I wanted to move quickly.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Eligible rationale about initial reaction, tolerance history, and urgency, but not itself a complete hidden manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "pattern classification and deferral choice",
        "raw_interview_anchor": "Once I saw the third one lined up with the first two, it read to me as confirmation ... I deferred it under MEL rather than pulling it into an unscheduled inspection.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_apo_01"
        ],
        "ground_truth_rationale": "The participant treats a third recurrence as a meaningful benign pattern and uses that perceived pattern to justify deferral."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "expert evidence weighting and risk continuity judgment",
        "raw_interview_anchor": "Tomas ... says it's the same seepage pattern ... this fitting type 'just seeps, it doesn't fail badly' ... that carries weight ... the junior engineer's torque and seal check felt like duplicating effort.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_norm_01",
          "AV7_exp_01"
        ],
        "ground_truth_rationale": "The same decision episode contains both the continuity assumption about benign fitting behavior and tenure-based substitution of expert judgment for structured analysis."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "automated evidence acceptance",
        "raw_interview_anchor": "Green status for that defect category, fleet-wide ... I referenced it directly in the disposition memo ... I didn't dig into the calculation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_aut_01"
        ],
        "ground_truth_rationale": "The fleet-average dashboard is accepted as authoritative without checking tail-specific recurrence coverage."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "confidence calibration from source convergence",
        "raw_interview_anchor": "Between the dashboard and Tomas's read, everything was pointing the same direction ... it felt like two independent checks agreeing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_iov_01"
        ],
        "ground_truth_rationale": "Confidence is increased by apparent convergence of sources that were not independently validated against the tail-specific history."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "release authorization and follow-up choice",
        "raw_interview_anchor": "MRO's engineering support had already left ... the seepage was still within tolerance ... I authorized release to service ... flagged a borescope recheck ... but didn't make it mandatory before dispatch.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an eligible release rationale, but the hidden manifestations are mapped to the later self-assessment and aircraft-specific outcome projection."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "self-assessment of deadline influence",
        "raw_interview_anchor": "Other managers might let a deadline push them into a call they're not comfortable with. I don't think that happened here ... the schedule was in the background ... I don't experience it as something that colors my technical judgment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_bbs_01"
        ],
        "ground_truth_rationale": "The participant generalizes susceptibility to deadline pressure to other managers while exempting the own final technical judgment."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "case-specific outcome probability judgment",
        "raw_interview_anchor": "Fifteen years at this airline, and I've never seen this exact fitting fail badly on any tail. That history made me comfortable that this one would be fine, even with the root cause investigation still technically open.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_opt_01"
        ],
        "ground_truth_rationale": "Failure-free personal history is projected onto this unresolved aircraft-specific case as confidence in a favorable outcome."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "retrospective process correction",
        "raw_interview_anchor": "I'd probably push harder for that fault-tree analysis ... not treat the recurrence pattern alone as settling the question ... a smooth return ... doesn't really tell us whether the process behind it was solid.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective correction is eligible context but is not credited as a contemporaneous hidden manifestation."
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
    "analysis_scope_note": "Mechanism-first review of a single interview transcript. No retrieved scientific-corpus passages were available in this task context, so bias labels, definitions, and mechanisms draw on general cognitive-science knowledge; no corpus evidence is fabricated."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Sample-size neglect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Confirmatory reasoning", "Tendency to seek consistent evidence"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall evidence in ways that confirm or strengthen a pre-existing belief or expectation, while discounting or not seeking disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-1 classification of recurrent hydraulic seepage as routine",
      "decision_point_description": "Whether to defer the seepage under MEL as a recurrent benign pattern or escalate to Quality for expanded inspection.",
      "affected_reasoning_operation": "Interpretation of recurrence and weighting of corroborating evidence",
      "bias_specific_mechanism": "The participant had an existing belief that the fitting was benign. When the third similar seepage appeared, he interpreted its recurrence as confirmation of stable fitting behavior rather than as a possible signal to escalate. He then treated Tomas's read and the fleet dashboard as independent corroborating sources and did not examine whether they might share the same blind spot.",
      "manifestation_in_interview": "The participant explicitly says the recurrence itself read as confirmation. He set aside expanded inspection because the shape of recurrence drove his read rather than raw values. Later he described the dashboard and Tomas's assessment as feeling like two independent checks agreeing.",
      "effect_on_reasoning_or_decision": "Reinforced the decision to defer under MEL rather than escalate to Quality, and increased confidence in the disposition memo without disconfirming analysis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Once I saw the third one lined up with the first two, it read to me as confirmation that this was just how this particular fitting behaves, not something new developing. So I deferred it under MEL rather than pulling it into an unscheduled inspection.",
          "evidence_explanation": "This shows the ambiguous third recurrence being interpreted directly as confirmation of the prior belief that the fitting is benign."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The other option was escalating to Quality immediately for an expanded inspection. I set that aside because nothing in the numbers themselves crossed a threshold — it was really the shape of the recurrence that drove my read, not the raw values.",
          "evidence_explanation": "The decision was driven by perceived pattern consistency rather than a threshold-based technical indication, consistent with confirmatory pattern interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Between the dashboard and Tomas's read, everything was pointing the same direction, so that consistency across sources gave me a fair amount of confidence in the memo's conclusion.",
          "evidence_explanation": "The participant weighted agreement among sources as strongly supporting his conclusion without examining whether the sources were independent or shared a common blind spot."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that the dashboard and Tomas's assessment might share the same blind spot, and said he would push harder for fault-tree analysis and not treat recurrence pattern alone as settling the question next time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were available in this task context; label and mechanism draw on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Sample-size neglect",
      "alternative_labels": ["Insensitivity to sample size", "Belief in the law of small numbers"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to draw firm conclusions from small samples by overestimating their statistical information value and underweighting uncertainty due to limited sample size.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-1 recurrence pattern inference",
      "decision_point_description": "Whether three similar seepage logs over eight months were sufficient to establish a stable fitting behavior.",
      "affected_reasoning_operation": "Statistical inference from a small number of recurrent events",
      "bias_specific_mechanism": "The participant treated the internal consistency of three observations as sufficient evidence for a stable fitting pattern despite acknowledging in hindsight that three observations might not be a large sample.",
      "manifestation_in_interview": "When asked whether three data points might not be enough, the participant said that in hindsight three was not a huge number, but in the moment it felt consistent enough because the readings were not random or inconsistent with each other.",
      "effect_on_reasoning_or_decision": "Supported the initial classification that the recurrence reflected a known stable behavior rather than a developing problem, contributing to the MEL deferral.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I mean — in hindsight, sure, three isn't a huge number. But in the moment it felt consistent enough. It wasn't like the readings were random or inconsistent with each other.",
          "evidence_explanation": "The participant explicitly acknowledges the small sample size but reports having treated the consistency of the three observations as sufficiently diagnostic in the moment, which is the core mechanism of sample-size neglect."
        }
      ],
      "correction_or_counterevidence": "The participant did acknowledge in hindsight that three observations might not be a large number and said he would not treat recurrence pattern alone as settling the question next time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were available in this task context; label and mechanism draw on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Authority bias",
      "alternative_labels": ["Deference to seniority", "Expert-authority effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overweight the judgment or opinion of a perceived authority or high-status/expert individual and to underweight or defer to that person's conclusion without proportional independent verification.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-2 validation of Tomas's cosmetic-seepage assessment",
      "decision_point_description": "Whether to accept Tomas's engineering assessment as sufficient technical grounds or to investigate the junior engineer's suggestion to check torque and seal specs.",
      "affected_reasoning_operation": "Weighting of advice/source credibility and information search",
      "bias_specific_mechanism": "The participant accepted Tomas's assessment mainly because of Tomas's long tenure and perceived expertise, treated that assessment as sufficient technical grounds on its own, and dismissed a junior engineer's dissenting suggestion as duplicative effort.",
      "manifestation_in_interview": "The participant said Tomas's tenure carries weight, did not commission a fault-tree analysis partly because Tomas's read seemed sufficient, and acknowledged he probably would not weigh the same assessment from a less senior engineer as heavily.",
      "effect_on_reasoning_or_decision": "The torque and seal spec check was not pursued, and the decision process relied heavily on the senior engineer's view rather than on independent verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Tomas has been doing this longer than almost anyone on my team. When he said this fitting type doesn't fail catastrophically, just seeps, that carries weight. We didn't commission a fault-tree analysis at that point — partly hangar time, partly that his read seemed like sufficient technical grounds on its own.",
          "evidence_explanation": "The participant explicitly links the weight given to Tomas's view to his tenure and treats that view as sufficient basis for not conducting further analysis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "One of our junior engineers suggested we pull the torque and seal specs to check whether something in the installation had drifted. I didn't follow up on that. It felt like duplicating effort when Tomas had already given a clear read.",
          "evidence_explanation": "A dissenting suggestion was discounted because the senior engineer had already spoken, showing differential weighting by source seniority."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as heavily. Tomas's tenure is a big part of why that carried the weight it did.",
          "evidence_explanation": "The participant admits that the same assessment from a less senior engineer would have been weighted less heavily, directly evidencing authority/seniority-based weighting."
        }
      ],
      "correction_or_counterevidence": "The participant indicated he would have pursued the junior engineer's suggestion if Tomas had seemed less certain or the seepage rate had increased, and later said he would push harder for fault-tree analysis in future.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were available in this task context; label and mechanism draw on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Time-pressure / deadline-induced bias",
      "alternative_labels": ["Schedule-completion pressure", "Deadline salience effect"],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Five-day lease-return disposition and release decision",
      "supporting_interview_quote": "MRO's engineering support had already left, deadline was two days out, and the seepage was still within tolerance with no new defect. I authorized release to service and we returned the aircraft on schedule.",
      "plausible_mechanism": "Schedule pressure and loss of engineering support may have increased reliance on the available consistent evidence and reduced search for disconfirming information, even though the participant attributes the decision to tolerance readings and history.",
      "why_not_identified": "The participant explicitly denies that the deadline affected his technical judgment and attributes the release decision to tolerance readings and history. The transcript lacks affirmative evidence of a distinct time-pressure mechanism beyond the already identified confirmation, authority, and sample-size mechanisms."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-corpus passages were available in this task context, so bias labels and mechanisms rely on general cognitive-science knowledge rather than corpus-supported definitions.",
    "The analysis is based on a single retrospective self-report and does not include objective maintenance records or independent engineering findings.",
    "The participant's causal explanations may be shaped by after-the-fact reflection and social desirability.",
    "Professional maintenance judgment may differ from the laboratory contexts in which some of these biases were originally studied.",
    "The coding is conservative and does not infer bias from the eventual smooth return of the aircraft."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Biased_7_Sonar_off",
  "interview_id": "AV_Biased_7",
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
