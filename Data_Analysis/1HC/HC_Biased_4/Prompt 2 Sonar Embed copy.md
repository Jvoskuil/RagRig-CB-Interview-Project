You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about how you approach clinical decisions, and I'll be asking about a specific case you flagged from a recent shift. Nothing you say will be attached to your name in any report. Sound okay?

Participant: Sure, that's fine. I've done a couple of these before for QI purposes, so I know the drill.

Interviewer: Great. Can you tell me your role and roughly how long you've been practicing?

Participant: I'm a hospitalist, internal medicine. I've been an attending for about nine years now, mostly at this hospital. I take the day handoff from the night team and round on the general medicine floor.

Interviewer: Perfect. Let's start broad — walk me through the case you had in mind.

Participant: Sure. This was a 68-year-old man who came in overnight through the ED. Fever, around 38.9, heart rate up around 112, blood pressure a little soft, 98 over 62, and the nurse noted he was mildly confused for a bit overnight. No clear source jumped out — no cough, no dysuria that he reported, no obvious skin findings on the ED note. Labs showed a mild leukocytosis. So basically a nonspecific presentation that could've been urinary, pulmonary, early skin or soft tissue, honestly a handful of things.

Interviewer: What was going through your mind when you first saw this?

Participant: Two things, really. Clinically, it's a fairly textbook SIRS picture without a clear source yet — common enough. But I'll be honest, it reminded me a lot of a patient I had maybe three weeks earlier. Similar vitals, similar vague presentation, and that one turned out to be a very fast-moving soft tissue infection that we caught late. It didn't go well. So when I saw this chart, that case was sitting in the back of my mind.

Interviewer: How did that shape what you did next?

Participant: I ordered a CT of the torso pretty much right away, before we even had urinalysis back. My reasoning at the time was I didn't want to be in that position again where we're playing catch-up on a soft tissue source. In hindsight, if I strip away that recent memory, this patient didn't actually have any exam findings pointing that direction — no erythema, no crepitus, nothing focal. But it felt like the responsible thing given what I'd just been through.

Interviewer: Got it. What other options were on the table?

Participant: I could've done a more stepwise workup — basic labs, urinalysis, maybe a chest film first, and reserved cross-sectional imaging if something localized. Or waited to see how his vitals trended over the next hour or two before committing to advanced imaging. Both were reasonable. I just didn't feel comfortable waiting.

Interviewer: What did the imaging show?

Participant: Came back about three hours later — clean. No abscess, no fasciitis, no intra-abdominal process. Urinalysis was still pending at that point anyway.

Interviewer: Let's move to antibiotics. What happened there?

Participant: Once the SIRS criteria were clearly met, I pulled up our sepsis order set. It gives you three empiric bundles — a narrow single-agent option, a broad two-drug "standard" bundle, and then a three-drug "extended" bundle that basically tacks on an extra agent covering organisms the standard bundle already handles for a case like this, just with more infusion time and extra renal monitoring tacked on.

Interviewer: How did you choose among those?

Participant: He was hemodynamically stable enough — SIRS positive but not meeting severe sepsis criteria. Looking at the three side by side, that third option didn't really buy you anything extra for a stable patient like him, it just added burden. But honestly, seeing it sitting there next to the standard bundle made the standard one look like the obviously sensible choice — clearly more coverage than the narrow option, without the extra baggage of the third one. So that's what I went with.

Interviewer: Did you separately work out what spectrum his actual severity called for, independent of the three options in front of you?

Participant: That's a fair question. Looking back, I think seeing that third bundle sitting there made the standard one look better by comparison, more than me actually starting from his numbers and building up from there. Pharmacy flagged later that the extended bundle is rarely indicated at this severity level anyway, and when ID called back, they said the standard bundle was reasonable but that the narrow one probably would've covered him fine given how stable he was.

Interviewer: How did you take that feedback?

Participant: A little bit of "huh, okay." Not wrong exactly, just broader than strictly necessary in retrospect.

Interviewer: Let's talk about the monitoring orders — telemetry and the catheter.

Participant: Right, so by mid-morning he was much improved. Heart rate down to 88, pressure 118 over 74, mentating clearly. Our sepsis order set auto-populates five days of continuous telemetry and continues the indwelling catheter as part of the standard pathway. Nursing actually flagged that he was up and walking around and asked whether the catheter was still needed.

Interviewer: What did you do with those orders?

Participant: I signed off on them as they were configured. Didn't actively shorten the telemetry window or pull the catheter order at that point.

Interviewer: Was there a specific reason you left them as configured versus reassessing given how much better he looked?

Participant: Honestly, I didn't sit down and re-derive whether five days was still appropriate. It's just what comes up when you open the pathway, and it's what most patients on this protocol get. Case management mentioned afterward that prolonged catheter use bumps up infection risk and can drag out length of stay, and telemetry didn't show anything over the next two days anyway, so it's hard to say it changed his outcome. But I probably could have revisited it earlier than I did.

Interviewer: Now the rounds discussion the next morning — what happened there?

Participant: The overnight resident's handoff, and how she presented it verbally at rounds, framed this as "likely urosepsis" — she'd seen mild pyuria on the early UA. That was the first thing said about the case, and honestly that framing kind of stuck for the group.

Interviewer: What new information came in around that time?

Participant: During that same discussion, the finalized urine culture came back with no significant growth, and the blood culture flagged preliminarily as gram-positive cocci in clusters — which honestly points more toward a skin or line source than urinary.

Interviewer: How did the team handle that shift in the data?

Participant: We acknowledged it, but the conversation kept circling back to the urosepsis framing for a while — talking about tweaking coverage for a urinary source, whether to repeat the UA, that kind of thing. It wasn't until a bit later, after we looked at his peripheral IV site and saw some redness there, that we really pivoted and started treating it as a likely catheter-related bacteremia instead.

Interviewer: Looking back, what do you think anchored the conversation to the urinary framing for as long as it did?

Participant: Probably that it was the first explanation on the table. Once you've got a plausible story and a room full of people nodding along, it takes a beat for contradictory data to really land, especially if it comes in mid-discussion rather than as the headline.

Interviewer: If the culture results had come back before rounds even started, do you think the discussion would've gone differently?

Participant: Probably, yeah. If gram-positive cocci and a negative urine culture were the opening facts instead of "likely urosepsis," I think we'd have gone straight to the IV site exam.

Interviewer: How much time pressure were you under across the shift overall?

Participant: Constant, honestly. ED wanted the bed, rounds have a hard start time, and you're juggling four or five other patients too. None of these felt like decisions I had the luxury of sitting with for twenty minutes each.

Interviewer: If you were handed this exact same information again tomorrow, is there a point you'd approach differently?

Participant: I think I'd force myself to write down the actual severity-based reasoning before looking at the order set options, rather than comparing across them first. And on the monitoring orders, I'd build in a habit of re-checking defaults once the patient's status changes, instead of just carrying them forward. The imaging call I'm less sure about — I still don't know that I'd talk myself out of it given how that last case ended.

Interviewer: That's really helpful. Anything else stand out from this case you think is worth noting?

Participant: Just that none of these felt like bad calls in the moment. It's only looking back at the sequence that you notice how much the earlier stuff — a past case, the first diagnosis mentioned, what's already checked in the system — shapes what happens next.

Interviewer: Thanks, this has been really useful.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HC_Biased_4",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Hospital Medicine Attending Physician (Internal Medicine Hospitalist)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Overnight-to-Morning Handoff: Managing a Suspected Sepsis Admission",
    "scenario_summary_internal": "An internal medicine hospitalist takes over care of a 68-year-old patient admitted overnight with fever, tachycardia, and borderline hypotension of unclear source. Across a single shift, the attending must decide how aggressively to work up the source of infection, which empiric antibiotic order set to select, how to configure ongoing monitoring orders, and how to interpret new culture data during multidisciplinary rounds. The case is nonroutine because the initial presentation is ambiguous (could be urinary, pulmonary, or skin/soft-tissue source) and institutional tools (EHR order sets, prior clinical experience, team handoff framing) shape the physician's reasoning in ways that are individually defensible but cumulatively distort the diagnostic and treatment path.",
    "occupational_realism": {
      "objective": "Correctly identify the infectious source and select an appropriately targeted, resource-proportionate treatment and monitoring plan within the first 24 hours of admission.",
      "setting": "Inpatient general medicine ward at a mid-sized community teaching hospital during a normal weekday, transitioning from night-shift coverage to day-shift attending rounds.",
      "constraints": [
        "Limited time before morning multidisciplinary rounds",
        "Incomplete overnight culture and imaging data",
        "EHR order sets with pre-configured default durations and tiered antibiotic bundles",
        "Need to balance antibiotic stewardship against risk of undertreating a potentially severe infection",
        "Competing demand from ED for bed turnover pressuring quick disposition decisions"
      ],
      "stakeholders": [
        "Attending hospitalist",
        "Overnight resident (handoff author)",
        "Bedside nurse",
        "Infectious disease consultant (available by page)",
        "Patient and family"
      ],
      "technical_terms_to_use": [
        "empiric antibiotic coverage",
        "pretest probability",
        "source control",
        "SIRS criteria",
        "telemetry order",
        "de-escalation",
        "differential diagnosis"
      ],
      "technical_terms_to_avoid": [
        "affect heuristic",
        "decoy effect",
        "default bias",
        "primacy bias",
        "cognitive bias",
        "anchoring"
      ],
      "excluded_themes": []
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient: 68-year-old male, fever 38.9C, HR 112, BP 98/62, mild confusion overnight",
          "No clear localizing symptoms yet; overnight labs show mild leukocytosis",
          "Attending recalls a recent case from three weeks prior where a similarly presenting patient was under-worked-up and later found to have rapidly progressive necrotizing fasciitis with a poor outcome"
        ],
        "new_information_after_decision": [
          "CT imaging is ordered emergently; results return three hours later showing no soft-tissue or abdominal source",
          "Urinalysis pending at time of decision"
        ],
        "alternatives": [
          "Order a stepwise, symptom-guided workup starting with basic labs and urinalysis before advanced imaging",
          "Order immediate broad cross-sectional imaging (CT torso) despite low localizing findings",
          "Defer imaging until vital sign trend and initial labs clarify severity"
        ],
        "intended_action": "Attending orders immediate CT imaging, citing a strong personal reaction tied to the recent adverse case rather than the patient's actual presenting probability of a soft-tissue emergency."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Blood and urine cultures pending, no organism identified yet",
          "EHR sepsis order set presents three empiric antibiotic bundles: (A) narrow-spectrum single-agent, (B) broad-spectrum dual-agent 'standard bundle', (C) broad-spectrum triple-agent 'extended bundle' with similar cost to (B) but broader, less-targeted coverage and higher toxicity risk with no clear added benefit for this presentation",
          "Patient hemodynamically stable, SIRS criteria met but not meeting severe sepsis threshold"
        ],
        "new_information_after_decision": [
          "Pharmacy flags the extended bundle as rarely indicated for this severity level",
          "ID consultant later notes bundle (B) was reasonable but confirms bundle (A) would likely have sufficed given stability"
        ],
        "alternatives": [
          "Select bundle (A), narrow-spectrum monotherapy consistent with stable presentation",
          "Select bundle (B), broad-spectrum dual-agent 'standard' bundle",
          "Select bundle (C), broad-spectrum triple-agent extended bundle"
        ],
        "intended_action": "Attending selects bundle (B), reasoning that it looks like the moderate, sensible middle option relative to the two bracketing choices, without independently re-deriving the appropriate spectrum from the patient's actual severity."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient stabilizing, HR now 88, BP 118/74, mentation clear",
          "EHR admission order set auto-populates a pre-checked 5-day continuous telemetry order and a pre-checked indwelling urinary catheter continuation order as part of the standard sepsis pathway",
          "Nursing flags that patient is ambulating well and catheter may no longer be indicated"
        ],
        "new_information_after_decision": [
          "Case management later notes prolonged catheter use is a known driver of hospital-acquired infection risk and length of stay",
          "Telemetry data over the next two days shows no arrhythmia events"
        ],
        "alternatives": [
          "Actively reassess and shorten telemetry duration and discontinue the catheter based on current clinical status",
          "Accept the pre-populated 5-day telemetry and catheter continuation orders as configured in the order set",
          "Escalate monitoring further out of caution"
        ],
        "intended_action": "Attending signs off on the pre-checked telemetry and catheter orders without modification, treating the order-set default as the appropriate plan rather than re-evaluating necessity given the patient's improved status."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Overnight resident's handoff note and initial verbal presentation at rounds framed the case as 'likely urosepsis' based on early urinalysis showing mild pyuria",
          "New morning data: urine culture is now finalized and shows no significant bacterial growth; blood culture is flagged preliminarily positive with gram-positive cocci in clusters, more consistent with a skin or line-related source",
          "Team discussion at rounds begins with, and largely stays anchored to, the urosepsis framing introduced first"
        ],
        "new_information_after_decision": [
          "Repeat blood cultures and skin/IV site examination two hours later reveal a peripheral IV site with local erythema, supporting a catheter-related bacteremia source",
          "Antibiotic coverage is later adjusted to target the newly identified source"
        ],
        "alternatives": [
          "Re-open the differential fully in light of the negative urine culture and positive blood culture morphology",
          "Continue treating the case primarily as urosepsis, the diagnosis introduced at the start of rounds, with only minor adjustments",
          "Request an infectious disease consult before finalizing the working diagnosis"
        ],
        "intended_action": "The team, including the attending, continues to frame ongoing management around the urosepsis diagnosis first proposed at the start of rounds, giving that initial framing more weight in discussion than the newer culture data that arrived later in the same conversation."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how you first learned about this patient and what your initial impression was.",
        "What was your role in this case, and what were you responsible for deciding?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you know at that point?",
        "What new information came in over the course of the shift, and when?",
        "How did the picture change between your first assessment and rounds?"
      ],
      "decision_point_probes": [
        "What made you decide to order imaging right away rather than wait for basic labs?",
        "How did you weigh the three antibiotic bundle options in the order set?",
        "Did you actively reconsider the telemetry and catheter orders, or did you leave them as they came up?",
        "When the new culture data came in, how did that change the working diagnosis discussed at rounds?"
      ],
      "goals_and_alternatives": [
        "What other options did you consider at each step, and why did you rule them out?",
        "What were you ultimately trying to balance or protect against in this case?"
      ],
      "decision_basis": [
        "What specific piece of information or experience most influenced your choice?",
        "Was there anything from a past case that came to mind while managing this one?"
      ],
      "prior_experience_time_pressure_uncertainty": [
        "How much time pressure did you feel at each stage?",
        "Where did you feel most uncertain, and how did you handle that uncertainty?",
        "Has a similar case shaped how you approach patients like this?"
      ],
      "closing_hypotheticals": [
        "If the order set had presented the antibiotic options differently, do you think you'd have chosen differently?",
        "If the urine culture result had come back before the team discussion started, would the conversation have gone differently?",
        "Looking back, is there a point where you'd handle things differently with the same information you had at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ah_01",
        "bias": "Affect Heuristic",
        "decision_point": 1,
        "mechanism": "Emotional residue from a recent, vivid adverse outcome (necrotizing fasciitis case) drives an elevated subjective risk judgment that overrides the low objective pretest probability suggested by the current patient's presentation, leading to a decision framed around feeling rather than probability.",
        "affected_reasoning_operation": "Risk estimation / diagnostic prioritization",
        "evidence_available_at_time": [
          "Non-specific fever and tachycardia without localizing soft-tissue findings",
          "Recollection of a recent unrelated case with a bad outcome"
        ],
        "required_textual_manifestation": "The physician explicitly links the urgency of the imaging decision to how the recent case made them feel ('I didn't want to miss it again' or equivalent) rather than to specific exam findings in the current patient.",
        "plausible_nonbias_interpretation": "Ordering early imaging could be framed as reasonable defensive/cautious practice given diagnostic uncertainty.",
        "strength": "subtle",
        "do_not_make_explicit": ["affect heuristic", "emotional bias", "cognitive bias"]
      },
      {
        "instance_id": "de_01",
        "bias": "Decoy Effect",
        "decision_point": 2,
        "mechanism": "The presence of a dominated 'extended bundle' option (broader coverage, similar cost, no added benefit, higher toxicity) makes the 'standard bundle' appear to be the sensible middle ground, pulling the choice toward it independent of an independent severity-based assessment.",
        "affected_reasoning_operation": "Option evaluation among asymmetric choice set",
        "evidence_available_at_time": [
          "Three EHU bundles: narrow monotherapy, standard dual-agent, extended triple-agent",
          "Patient's actual stability level supporting narrower coverage"
        ],
        "required_textual_manifestation": "The physician's stated rationale references the bundle's position relative to the other two options ('it seemed like the reasonable one in the middle') rather than an independent clinical derivation of required spectrum.",
        "plausible_nonbias_interpretation": "Choosing the standard bundle could be explained as adherence to common institutional practice patterns for sepsis rule-outs.",
        "strength": "subtle",
        "do_not_make_explicit": ["decoy effect", "asymmetric dominance"]
      },
      {
        "instance_id": "db_01",
        "bias": "Default Bias",
        "decision_point": 3,
        "mechanism": "The pre-checked telemetry and catheter continuation settings in the EHR order set are accepted without active reassessment, even though the patient's improved clinical status would support discontinuation or shortening.",
        "affected_reasoning_operation": "Order confirmation / status-quo evaluation",
        "evidence_available_at_time": [
          "Improved vital signs and mentation",
          "Nursing flag suggesting catheter may no longer be needed",
          "Pre-populated 5-day telemetry/catheter defaults in the order set"
        ],
        "required_textual_manifestation": "The physician describes signing off on the orders as configured, without describing an active re-evaluation step despite acknowledging the patient's improvement.",
        "plausible_nonbias_interpretation": "Leaving the standard pathway in place could be explained as reasonable adherence to a validated sepsis protocol pending full stabilization.",
        "strength": "subtle",
        "do_not_make_explicit": ["default bias", "status quo bias"]
      },
      {
        "instance_id": "pb_01",
        "bias": "Primacy Bias",
        "decision_point": 4,
        "mechanism": "The diagnostic framing ('likely urosepsis') introduced first at the start of rounds continues to anchor the team's discussion and management even after later-arriving culture data (negative urine culture, gram-positive blood culture) supports reconsidering the source.",
        "affected_reasoning_operation": "Belief updating / differential diagnosis revision",
        "evidence_available_at_time": [
          "Initial verbal framing of 'likely urosepsis' at start of rounds",
          "Newly returned urine culture (no significant growth)",
          "Newly returned blood culture morphology (gram-positive cocci in clusters)"
        ],
        "required_textual_manifestation": "The physician's account shows the team's discussion continuing to center on the urosepsis framing even while narrating the arrival of culture data that runs counter to it, before only later shifting focus.",
        "plausible_nonbias_interpretation": "Continuing to treat urosepsis as a working diagnosis briefly could be explained as reasonable caution against overreacting to a single preliminary culture result.",
        "strength": "subtle",
        "do_not_make_explicit": ["primacy bias", "anchoring", "first information effect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control scenario supplied."
    },
    "counterfactual_specification": {
      "causal_variable": "AUTOSELECT — not applicable, no counterfactual condition requested",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and none are merged or split.",
      "Confirm each of the 4 planned bias instances appears exactly once, at its assigned decision point, with no repetition elsewhere.",
      "Confirm no bias name, definition, or psychological label appears in the interview text.",
      "Confirm each decision point includes at least two plausible alternatives and both pre- and post-decision information.",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count falls between 1,215 and 1,485 words.",
      "Confirm consequences described do not conclusively prove or disprove bias presence (outcomes remain ambiguous as to causation)."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Affect Heuristic", "occurrences": 1, "mechanism_constraint": "Elevated risk judgment driven by emotional residue from a recent, unrelated adverse case rather than current patient's objective findings" },
      { "bias": "Decoy Effect", "occurrences": 1, "mechanism_constraint": "Choice among three antibiotic bundles is pulled toward the middle option by the presence of a dominated 'extended' option" },
      { "bias": "Default Bias", "occurrences": 1, "mechanism_constraint": "Pre-checked EHR order-set defaults (telemetry/catheter duration) accepted without active reassessment despite improved clinical status" },
      { "bias": "Primacy Bias", "occurrences": 1, "mechanism_constraint": "Initial diagnostic framing presented first at rounds continues to anchor team discussion despite later contradicting culture data" }
    ],
    "target_bias_names": ["Affect Heuristic", "Decoy Effect", "Default Bias", "Primacy Bias"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Affect Heuristic", "requested_occurrences": 1 },
      { "bias": "Decoy Effect", "requested_occurrences": 1 },
      { "bias": "Default Bias", "requested_occurrences": 1 },
      { "bias": "Primacy Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "ah_01", "bias": "Affect Heuristic" },
      { "instance_id": "de_01", "bias": "Decoy Effect" },
      { "instance_id": "db_01", "bias": "Default Bias" },
      { "instance_id": "pb_01", "bias": "Primacy Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "ah_01", "bias": "Affect Heuristic", "decision_point": 1 },
      { "instance_id": "de_01", "bias": "Decoy Effect", "decision_point": 2 },
      { "instance_id": "db_01", "bias": "Default Bias", "decision_point": 3 },
      { "instance_id": "pb_01", "bias": "Primacy Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ah_01",
        "bias": "Affect Heuristic",
        "mechanism": "Emotionally vivid memory of a prior adverse outcome elevates perceived risk and drives an urgent imaging decision independent of the current patient's objective pretest probability.",
        "affected_reasoning_operation": "Risk estimation / diagnostic prioritization",
        "evidence_source": "Physician's stated recollection of a prior case linked explicitly to the urgency of the current decision",
        "distinctiveness_requirement": "Must be tied to emotional recollection of a specific past case, not to current physical exam findings; distinct from default or primacy mechanisms, which involve order-set inertia and sequential framing respectively."
      },
      {
        "instance_id": "de_01",
        "bias": "Decoy Effect",
        "mechanism": "An asymmetrically dominated third option in the antibiotic order set makes the standard/moderate bundle appear preferable by comparison, rather than through independent severity-based clinical reasoning.",
        "affected_reasoning_operation": "Multi-option evaluation / choice justification",
        "evidence_source": "Physician's rationale referencing the bundle's relative position among three options rather than an independent severity assessment",
        "distinctiveness_requirement": "Must involve a three-option comparative structure with one dominated option; distinct from default bias, which involves accepting a single pre-set option rather than choosing among a comparison set."
      },
      {
        "instance_id": "db_01",
        "bias": "Default Bias",
        "mechanism": "Pre-checked EHR order-set settings for telemetry duration and catheter continuation are left unchanged despite clinical evidence (improved vitals, nursing input) supporting active modification.",
        "affected_reasoning_operation": "Order confirmation / status-quo re-evaluation",
        "evidence_source": "Narrative describing acceptance of pre-populated orders without an active reassessment step despite contrary clinical cues",
        "distinctiveness_requirement": "Must involve a single pre-set system default accepted passively; distinct from decoy effect, which requires an active comparative choice among multiple presented options."
      },
      {
        "instance_id": "pb_01",
        "bias": "Primacy Bias",
        "mechanism": "The diagnostic label introduced first at the start of rounds continues to dominate the team's ongoing interpretation even as later-arriving culture data suggests an alternative source.",
        "affected_reasoning_operation": "Belief updating / differential revision under sequential information",
        "evidence_source": "Sequence showing initial framing stated first, followed by contradicting data, with discussion continuing to center on the initial framing",
        "distinctiveness_requirement": "Must involve information presented in temporal sequence where the first-presented hypothesis retains disproportionate weight; distinct from affect heuristic, which is driven by emotional valence rather than order of presentation."
      }
    ],
    "intended_strength": [
      { "instance_id": "ah_01", "bias": "Affect Heuristic", "strength": "subtle" },
      { "instance_id": "de_01", "bias": "Decoy Effect", "strength": "subtle" },
      { "instance_id": "db_01", "bias": "Default Bias", "strength": "subtle" },
      { "instance_id": "pb_01", "bias": "Primacy Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Biased_4",
    "domain_id": "HC",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (1:1 mapping across the 4 decision points) chosen for mechanism fit: affect heuristic to initial risk-driven imaging decision, decoy effect to a three-option comparative choice, default bias to passive acceptance of a pre-set system default, primacy bias to sequential team belief-updating during rounds.",
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
        "segment_type": "initial_clinical_interpretation",
        "raw_interview_anchor": "Clinically, it's a fairly textbook SIRS picture without a clear source yet... a handful of things.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive differential-diagnosis and severity interpretation without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "imaging_decision_and_rationale",
        "raw_interview_anchor": "It reminded me a lot of a patient I had maybe three weeks earlier... I ordered a CT of the torso pretty much right away... it felt like the responsible thing given what I'd just been through.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ah_01"
        ],
        "ground_truth_rationale": "A vivid recent adverse case emotionally elevated perceived soft-tissue risk and drove urgent imaging despite absent focal findings."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "workup_alternatives",
        "raw_interview_anchor": "I could've done a more stepwise workup... Both were reasonable. I just didn't feel comfortable waiting.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicit comparison of reasonable workup alternatives without an additional hidden instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "antibiotic_bundle_selection",
        "raw_interview_anchor": "Seeing it sitting there next to the standard bundle made the standard one look like the obviously sensible choice... So that's what I went with.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "de_01"
        ],
        "ground_truth_rationale": "The dominated extended option made the standard bundle appear preferable by comparison rather than through independent severity-based derivation."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "monitoring_order_confirmation",
        "raw_interview_anchor": "I signed off on them as they were configured... I didn't sit down and re-derive whether five days was still appropriate. It's just what comes up when you open the pathway.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "db_01"
        ],
        "ground_truth_rationale": "Preconfigured telemetry and catheter defaults were accepted without active reassessment despite clinical improvement and nursing input."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "rounds_diagnostic_updating",
        "raw_interview_anchor": "That was the first thing said about the case, and honestly that framing kind of stuck for the group... the conversation kept circling back to the urosepsis framing for a while.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "pb_01"
        ],
        "ground_truth_rationale": "The first diagnostic framing continued to dominate discussion despite negative urine culture and blood-culture evidence favoring another source."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "time_pressure_context",
        "raw_interview_anchor": "Constant, honestly. ED wanted the bed, rounds have a hard start time, and you're juggling four or five other patients too.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive contextual explanation of time pressure, without a hidden bias instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_learning",
        "raw_interview_anchor": "I'd force myself to write down the actual severity-based reasoning... build in a habit of re-checking defaults once the patient's status changes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective improvement plan and uncertainty statement, not a new intended occurrence."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focuses on the participant's described clinical reasoning and decisions; interviewer questions are treated as context rather than as evidence of the participant's bias."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Decoy effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Status quo bias",
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
      "bias_definition": "Judging the likelihood or importance of an event by how easily examples come to mind, especially recent or emotionally salient examples.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial imaging workup for undifferentiated fever/SIRS",
      "decision_point_description": "Whether to order CT of the torso immediately versus a stepwise workup.",
      "affected_reasoning_operation": "Clinical judgment about likely infection source and urgency of advanced imaging",
      "bias_specific_mechanism": "A recent bad outcome from a soft tissue infection made that diagnosis highly available, inflating its subjective likelihood for a new patient with a nonspecific presentation.",
      "manifestation_in_interview": "The participant explicitly says the recent case was sitting in the back of his mind and that, without that memory, the current patient had no exam findings pointing toward a soft tissue source.",
      "effect_on_reasoning_or_decision": "Prompted immediate CT of the torso before less invasive or stepwise workup, despite no focal exam findings.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But I'll be honest, it reminded me a lot of a patient I had maybe three weeks earlier. Similar vitals, similar vague presentation, and that one turned out to be a very fast-moving soft tissue infection that we caught late. It didn't go well. So when I saw this chart, that case was sitting in the back of my mind.",
          "evidence_explanation": "The participant identifies a recent, emotionally salient case as being mentally active during the new patient's assessment, which is the recall-based mechanism underlying the availability heuristic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I ordered a CT of the torso pretty much right away, before we even had urinalysis back. My reasoning at the time was I didn't want to be in that position again where we're playing catch-up on a soft tissue source. In hindsight, if I strip away that recent memory, this patient didn't actually have any exam findings pointing that direction — no erythema, no crepitus, nothing focal.",
          "evidence_explanation": "The participant links the recent memory directly to the imaging decision and acknowledges that the available case, not the current clinical findings, drove the judgment."
        }
      ],
      "correction_or_counterevidence": "The CT came back clean, and the participant later acknowledged that the current patient had no erythema, crepitus, or focal findings pointing to soft tissue infection.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support identifies availability as a dominant clinical decision-making heuristic under uncertainty.",
      "corpus_evidence": [
        {
          "source_identifier": "Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf",
          "paper_title": null,
          "authors": "Uwe Dulleck, PhD",
          "publication_year": "2025",
          "retrieved_passage_or_finding": "align with previous research, suggesting that availability and anchoring are two dominant heuristics among emergency triage nurses.",
          "mechanism_supported_by_source": "Supports availability as a recognized driver of clinical judgment under uncertainty.",
          "relevance_to_this_occurrence": "This occurrence involves the participant using a recent salient case to judge the likelihood of a soft tissue source, consistent with availability-based judgment."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Decoy effect",
      "alternative_labels": ["Attraction effect", "Compromise effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A choice between options is influenced by the presence of a third, less attractive option that makes another option appear more favorable by comparison.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of empiric antibiotic bundle",
      "decision_point_description": "Choosing among narrow single-agent, standard two-drug, and extended three-drug empiric bundles.",
      "affected_reasoning_operation": "Antibiotic regimen selection from the sepsis order set",
      "bias_specific_mechanism": "The extended three-drug bundle served as a decoy; evaluating the options side-by-side made the standard bundle appear like the obviously sensible choice rather than deriving the appropriate spectrum from the patient's severity.",
      "manifestation_in_interview": "The participant said the third bundle made the standard one look better by comparison and acknowledged not independently building the decision from the patient's numbers.",
      "effect_on_reasoning_or_decision": "Led to selection of the broader standard two-drug bundle when a narrower regimen likely would have been sufficient based on severity.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He was hemodynamically stable enough — SIRS positive but not meeting severe sepsis criteria. Looking at the three side by side, that third option didn't really buy you anything extra for a stable patient like him, it just added burden. But honestly, seeing it sitting there next to the standard bundle made the standard one look like the obviously sensible choice — clearly more coverage than the narrow option, without the extra baggage of the third one. So that's what I went with.",
          "evidence_explanation": "The participant describes the third option as a comparison point that made the standard option appear more attractive, the core mechanism of the decoy effect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I think seeing that third bundle sitting there made the standard one look better by comparison, more than me actually starting from his numbers and building up from there.",
          "evidence_explanation": "This directly states that comparative context, rather than independent clinical assessment, drove the antibiotic choice."
        }
      ],
      "correction_or_counterevidence": "Pharmacy and ID later indicated the standard bundle was reasonable but broader than strictly necessary; the participant acknowledged this in retrospect.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this specific label was unavailable; the label is drawn from general cognitive science and behavioral economics knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Status quo bias",
      "alternative_labels": ["Default effect", "Default bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for the current state or pre-selected option, with acceptance of defaults rather than active reassessment when circumstances change.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Telemetry and indwelling catheter order management",
      "decision_point_description": "Whether to continue or revise default telemetry duration and catheter orders after the patient improved.",
      "affected_reasoning_operation": "Reassessment of monitoring and catheter orders after clinical improvement",
      "bias_specific_mechanism": "The order set's pre-populated telemetry and catheter defaults were carried forward without re-deriving whether they still fit the patient's improved clinical status.",
      "manifestation_in_interview": "The participant signed off on the orders as configured and said he did not re-derive whether five days was still appropriate; the default pathway was accepted as what most patients receive.",
      "effect_on_reasoning_or_decision": "Continued telemetry and indwelling catheter use longer than necessary, increasing monitoring burden and catheter-related infection risk.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I signed off on them as they were configured. Didn't actively shorten the telemetry window or pull the catheter order at that point.",
          "evidence_explanation": "This shows acceptance of the pre-configured default without active modification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I didn't sit down and re-derive whether five days was still appropriate. It's just what comes up when you open the pathway, and it's what most patients on this protocol get.",
          "evidence_explanation": "The participant explicitly describes carrying forward the default rather than reassessing the order in light of the patient's improvement."
        }
      ],
      "correction_or_counterevidence": "Nursing asked whether the catheter was still needed, and case management later noted prolonged catheter use increases infection risk and length of stay; the participant acknowledged he probably could have revisited the orders earlier.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this specific label was unavailable; the label is drawn from general cognitive science and behavioral economics knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment", "Diagnosis momentum"],
      "taxonomy_status": "established_label",
      "bias_definition": "Over-reliance on an initial piece of information, such that later judgments and probability updates are insufficiently adjusted away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Team diagnostic framing on morning rounds",
      "decision_point_description": "How to integrate negative urine culture and preliminary blood culture results after the initial urosepsis framing.",
      "affected_reasoning_operation": "Diagnostic updating and infection source identification during morning rounds",
      "bias_specific_mechanism": "The initial 'likely urosepsis' framing served as an anchor; despite negative urine culture and preliminary gram-positive cocci suggesting a skin or line source, the team continued to circle back to the urinary source.",
      "manifestation_in_interview": "The participant said the first explanation stayed stuck for the group and contradictory data took time to land.",
      "effect_on_reasoning_or_decision": "Delayed diagnostic pivot from urosepsis to catheter-related bacteremia, requiring later attention to the peripheral IV site to shift the team's framing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The overnight resident's handoff, and how she presented it verbally at rounds, framed this as 'likely urosepsis' — she'd seen mild pyuria on the early UA. That was the first thing said about the case, and honestly that framing kind of stuck for the group.",
          "evidence_explanation": "The participant identifies the initial diagnostic label as the anchor that persisted in the group's discussion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "During that same discussion, the finalized urine culture came back with no significant growth, and the blood culture flagged preliminarily as gram-positive cocci in clusters — which honestly points more toward a skin or line source than urinary.",
          "evidence_explanation": "This supplies the contradictory information that should have shifted the diagnostic probability away from urosepsis, but did not immediately do so."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We acknowledged it, but the conversation kept circling back to the urosepsis framing for a while — talking about tweaking coverage for a urinary source, whether to repeat the UA, that kind of thing.",
          "evidence_explanation": "This demonstrates insufficient adjustment away from the initial anchor despite new disconfirming evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably that it was the first explanation on the table. Once you've got a plausible story and a room full of people nodding along, it takes a beat for contradictory data to really land, especially if it comes in mid-discussion rather than as the headline.",
          "evidence_explanation": "The participant explicitly attributes the delayed shift to the initial explanation serving as the anchor."
        }
      ],
      "correction_or_counterevidence": "The team eventually examined the peripheral IV site, saw redness, and pivoted to likely catheter-related bacteremia; the participant also acknowledged that if the culture data had been the opening facts, the team likely would have gone straight to the IV site exam.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support identifies anchoring as a recognized clinical cognitive failure in which clinicians fix on an initial diagnosis or injury and under-adjust.",
      "corpus_evidence": [
        {
          "source_identifier": "From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf",
          "paper_title": "From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making",
          "authors": null,
          "publication_year": "2013",
          "retrieved_passage_or_finding": "The cognitive failures identified here are 'anchoring' and 'search satisficing.' The resident and attending staff both anchored onto the chest wound as the most significant injury. When they satisfied themselves that the chest wound was stable, the resident failed to conduct a sufficient search to rule out other significant injuries.",
          "mechanism_supported_by_source": "Supports anchoring as a failure mode in which clinicians fix on an initial diagnosis or injury and under-adjust to other possibilities.",
          "relevance_to_this_occurrence": "This occurrence mirrors the corpus example: the team anchored on the initial urosepsis framing and was slow to adjust to contradictory culture data."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective self-report, so recall and self-presentation may affect the described reasoning.",
    "Some bias labels, specifically Decoy effect and Status quo bias, draw on general cognitive science or behavioral economics knowledge because the retrieved corpus did not provide specific support.",
    "No objective baseline or control condition is available; decisions were not directly observed and outcomes were not independently verified.",
    "Retrieved corpus passages are brief and partly truncated, so corpus-based support is limited to the available snippets.",
    "Following standard order sets and pursuing early imaging in the context of recent bad outcomes may also reflect clinical caution or protocol-driven behavior; these non-bias explanations are noted as counterevidence where relevant."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HC_Biased_4_Sonar_on",
  "interview_id": "HC_Biased_4",
  "system_prompt_id": "Sonar",
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
