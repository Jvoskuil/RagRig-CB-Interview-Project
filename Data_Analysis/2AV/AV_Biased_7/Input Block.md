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
[ontology-free RAG JSON output]
</RAG_ANALYSIS_OUTPUT>
