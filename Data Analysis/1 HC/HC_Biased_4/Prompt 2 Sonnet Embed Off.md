You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Your task is to compare:
1. A raw cognitive task analysis interview;
2. The complete interview-generation specification, including its hidden validation specification;
3. A RAG system's JSON analysis output; and
4. Optionally, a prevalidated evaluation segment map.

You must evaluate how closely the RAG system output overlaps with the hidden ground truth.

You are an evaluator, not a new cognitive-bias analyst. Do not award credit merely because a RAG prediction is psychologically plausible, academically reasonable, well-written, or supported by external knowledge. Evaluate the RAG output against the hidden generation specification, the hidden validation specification, and the raw interview.

OUTPUT REQUIREMENT

Return exactly one valid JSON object that conforms to the output schema specified below.

Do not return Markdown.
Do not wrap JSON in a code fence.
Do not provide text before or after the JSON.
Do not reveal chain-of-thought or hidden reasoning.
Do not add keys not included in the required schema.
Use concise, auditable explanations that refer to the supplied input materials.

INPUTS

You will receive input blocks with the following labels:

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

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Only the provided interview text was assessed. No retrieved scientific-paper passages were supplied in the RAG context, so classifications rely on the interview evidence and the reference-ontology definitions rather than on retrieved corpus support."
  },
  "identified_bias_summary": [
    {
      "canonical_bias_name": "Anchoring Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Decoy Effect",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Default Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "A cognitive bias in which perceived likelihood or importance is influenced by the ease with which examples come to mind, often favoring recent, vivid, or emotionally salient cases.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial diagnostic workup and early torso CT decision",
      "decision_point_description": "Decision to order a CT of the torso immediately, before urinalysis or stepwise evaluation, for a patient with SIRS and no focal source.",
      "affected_reasoning_operation": "Clinical judgment about the likelihood of an occult soft-tissue source and the need for early advanced imaging.",
      "bias_specific_mechanism": "A recent, emotionally salient case of fast-moving soft-tissue infection was highly available in memory and led the clinician to overestimate the probability of a similar source in this patient, prompting early imaging despite absent focal findings.",
      "manifestation_in_interview": "The participant explicitly connects the immediate CT order to a similar recent case that had a bad outcome, and then notes that without that memory there were no exam findings pointing to that direction.",
      "effect_on_reasoning_or_decision": "He ordered torso CT before basic stepwise workup; the CT was ultimately negative, and he retrospectively acknowledged the recent case shaped the decision more than objective findings did.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "it reminded me a lot of a patient I had maybe three weeks earlier. Similar vitals, similar vague presentation, and that one turned out to be a very fast-moving soft tissue infection that we caught late. It didn't go well. So when I saw this chart, that case was sitting in the back of my mind.",
          "evidence_explanation": "Shows a vivid recent case was mentally available at the time of the initial assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I ordered a CT of the torso pretty much right away, before we even had urinalysis back. My reasoning at the time was I didn't want to be in that position again where we're playing catch-up on a soft tissue source.",
          "evidence_explanation": "Directly links the recent memory to the decision to obtain early imaging."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, if I strip away that recent memory, this patient didn't actually have any exam findings pointing that direction — no erythema, no crepitus, nothing focal.",
          "evidence_explanation": "Confirms the memory, rather than current objective evidence, drove the direction of the workup."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction before the CT was described; the negative CT and later reflection exposed the influence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context, so corpus support could not be cited for this occurrence. The classification is based on the interview evidence and the reference-ontology definition of Availability Bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Decoy Effect",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "A context effect in which adding a less attractive option makes another option appear more attractive by comparison, altering choice among options.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Empiric antibiotic selection from sepsis order-set bundles",
      "decision_point_description": "Choice among narrow single-agent, standard two-drug, and extended three-drug empiric antibiotic bundles.",
      "affected_reasoning_operation": "Comparison of antibiotic options and selection of empiric treatment intensity.",
      "bias_specific_mechanism": "The extended three-drug bundle served as a decoy: it added burden without meaningful additional coverage for a stable patient, making the standard two-drug bundle appear like the obviously sensible middle option. Selection was shaped by comparative display rather than independent severity-based spectrum assessment.",
      "manifestation_in_interview": "Participant says the third bundle made the standard bundle look better by comparison, and later admits he did not start from the patient's severity and build up.",
      "effect_on_reasoning_or_decision": "He chose the broad standard two-drug bundle; pharmacy and ID later indicated the narrow option likely would have been sufficient.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He was hemodynamically stable enough — SIRS positive but not meeting severe sepsis criteria. Looking at the three side by side, that third option didn't really buy you anything extra for a stable patient like him, it just added burden. But honestly, seeing it sitting there next to the standard bundle made the standard one look like the obviously sensible choice — clearly more coverage than the narrow option, without the extra baggage of the third one. So that's what I went with.",
          "evidence_explanation": "Describes how the presence of the third bundle affected the attractiveness of the standard bundle during the choice."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I think seeing that third bundle sitting there made the standard one look better by comparison, more than me actually starting from his numbers and building up from there.",
          "evidence_explanation": "Explicitly identifies comparative option presentation, rather than independent severity-based reasoning, as the driver of the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Pharmacy flagged later that the extended bundle is rarely indicated at this severity level anyway, and when ID called back, they said the standard bundle was reasonable but that the narrow one probably would've covered him fine given how stable he was.",
          "evidence_explanation": "Supports the likelihood that the chosen standard bundle was broader than necessary and that the option comparison influenced selection."
        }
      ],
      "correction_or_counterevidence": "Post-choice feedback from pharmacy and ID suggested broader than necessary; participant recognized comparison-driven selection retrospectively.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context, so corpus support could not be cited for this occurrence. The classification is based on the interview evidence and the reference-ontology definition of Decoy Effect.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Default Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Tendency to accept a pre-set or default option rather than actively choosing an alternative, especially when the default is presented as standard or routine.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Telemetry and indwelling catheter orders after clinical improvement",
      "decision_point_description": "Whether to continue or modify auto-populated five-day telemetry and indwelling catheter orders after the patient's vitals and mental status improved.",
      "affected_reasoning_operation": "Reassessment of monitoring and device orders following a change in clinical status.",
      "bias_specific_mechanism": "The sepsis order set auto-populated five days of continuous telemetry and continued the indwelling catheter as standard; the participant signed them as configured and did not re-derive whether they remained appropriate after the patient improved.",
      "manifestation_in_interview": "Participant explicitly says he signed the orders as they were configured and did not shorten telemetry or pull the catheter, noting it is what comes up and what most patients get.",
      "effect_on_reasoning_or_decision": "Unnecessary telemetry and catheter were continued; case management noted prolonged catheter use increases infection risk and length of stay.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I signed off on them as they were configured. Didn't actively shorten the telemetry window or pull the catheter order at that point.",
          "evidence_explanation": "Shows passive acceptance of existing pre-populated orders rather than active reassessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I didn't sit down and re-derive whether five days was still appropriate. It's just what comes up when you open the pathway, and it's what most patients on this protocol get.",
          "evidence_explanation": "Confirms that the default protocol setting and common practice substituted for individualized re-evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Case management mentioned afterward that prolonged catheter use bumps up infection risk and can drag out length of stay, and telemetry didn't show anything over the next two days anyway, so it's hard to say it changed his outcome.",
          "evidence_explanation": "Illustrates the known potential harm from the continued default orders."
        }
      ],
      "correction_or_counterevidence": "Nursing asked whether the catheter was still needed, and case management later noted risks; these challenges did not alter the initial default acceptance.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context, so corpus support could not be cited for this occurrence. The classification is based on the interview evidence and the reference-ontology definition of Default Bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Anchoring Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Tendency to rely too heavily on an initial piece of information or initial hypothesis when making subsequent judgments, leading to insufficient adjustment from that anchor.",
      "attributed_to_speaker": "Participant and treating team",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Morning rounds integration of new culture results",
      "decision_point_description": "How the team interpreted negative urine culture and preliminary blood culture with gram-positive cocci after the resident framed the case as likely urosepsis.",
      "affected_reasoning_operation": "Diagnostic framing and focus of subsequent workup discussion.",
      "bias_specific_mechanism": "The initial 'likely urosepsis' diagnostic frame served as an anchor; when later data indicated a skin or line source, the group insufficiently adjusted and continued discussing urinary source actions.",
      "manifestation_in_interview": "The team acknowledged the new data but kept returning to the urinary source framing until peripheral IV site redness prompted a pivot.",
      "effect_on_reasoning_or_decision": "Delayed recognition of likely catheter-related bacteremia and prolonged discussion of urinary source management.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The overnight resident's handoff, and how she presented it verbally at rounds, framed this as 'likely urosepsis' — she'd seen mild pyuria on the early UA. That was the first thing said about the case, and honestly that framing kind of stuck for the group.",
          "evidence_explanation": "Establishes that the initial diagnostic label was presented first and became the group's reference point."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "During that same discussion, the finalized urine culture came back with no significant growth, and the blood culture flagged preliminarily as gram-positive cocci in clusters — which honestly points more toward a skin or line source than urinary.",
          "evidence_explanation": "Identifies contradicting evidence that should have prompted substantial revision away from the initial urinary framing."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We acknowledged it, but the conversation kept circling back to the urosepsis framing for a while — talking about tweaking coverage for a urinary source, whether to repeat the UA, that kind of thing.",
          "evidence_explanation": "Shows insufficient adjustment from the initial anchor despite contradictory data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably that it was the first explanation on the table. Once you've got a plausible story and a room full of people nodding along, it takes a beat for contradictory data to really land, especially if it comes in mid-discussion rather than as the headline.",
          "evidence_explanation": "Participant explicitly attributes the delayed shift to the early framing and order of information."
        }
      ],
      "correction_or_counterevidence": "The team eventually pivoted after noticing peripheral IV site redness, but only after a delay.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were supplied in the RAG context, so corpus support could not be cited for this occurrence. The classification is based on the interview evidence and the reference-ontology definition of Anchoring Bias.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_name": "Confirmation Bias",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant and treating team",
      "possible_decision_episode_label": "Morning rounds response to negative urine culture and preliminary blood culture",
      "supporting_interview_quote": "We acknowledged it, but the conversation kept circling back to the urosepsis framing for a while — talking about tweaking coverage for a urinary source, whether to repeat the UA, that kind of thing.",
      "plausible_mechanism": "The team may have continued to seek or discuss urinary-source evidence consistent with the initial 'likely urosepsis' hypothesis despite contradictory culture results.",
      "why_not_identified": "The evidence is also well explained by anchoring to the initial framing; the interview does not clearly separate confirmatory search from insufficient anchor adjustment, so this is treated as a plausible candidate rather than a distinct identified occurrence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper passages were supplied in the RAG context, so no corpus evidence could be cited for any occurrence.",
    "The interview is a retrospective self-report; the analysis is limited to what the participant described and cannot independently verify real-time cognition.",
    "Some mechanisms, particularly anchoring and confirmation bias in the rounds discussion, are closely related and may overlap."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<EVALUATION_SEGMENT_MAP>
Optional. A prevalidated, externally supplied segment map for this interview.
</EVALUATION_SEGMENT_MAP>

The evaluation segment map may be absent, empty, null, or unavailable.

CONFIDENTIALITY AND EVALUATOR BOUNDARY

The complete generation specification and hidden validation specification are evaluator-only ground truth.

The RAG system did not receive these materials. Do not penalize the RAG system for failing to state hidden labels, internal generation details, hidden intended actions, hidden requirements, or internal scenario terminology that cannot reasonably be inferred from the raw interview.

Do not use the hidden specification to invent a RAG finding the system did not make.
Do not convert a RAG candidate finding into an identified finding.
Do not assume the RAG system should have detected every hidden instance if the raw interview does not support it.
Do not grant credit based on hidden intent alone when the RAG system cited the wrong raw-interview segment or supplied an unsupported mechanism.

GROUND-TRUTH PRINCIPLE

Treat `exact_occurrence_manifest` in the hidden validation specification as exhaustive for cognitive-bias occurrences intentionally present in the specific interview under evaluation.

A hidden bias instance is defined by all applicable information in the complete generation specification, including:
- `instance_id`;
- Intended bias;
- Intended mechanism;
- Affected reasoning operation;
- Intended decision point, if applicable;
- Required textual manifestation;
- Evidence available at the time;
- Distinctiveness requirements;
- Plausible non-bias interpretation;
- Hidden mechanism constraint;
- Raw-interview evidence supporting that instance.

The reference bias ontology is not exhaustive of all conceivable cognitive biases. However, for primary benchmark scoring:
- A prediction of an outside-reference-ontology bias is not automatically correct merely because it is psychologically plausible.
- An outside-ontology prediction may be considered an approved equivalent only if its mechanism is substantively identical to a hidden target bias and the label is an established alternate name for that target construct.
- A merely related, adjacent, overlapping, or near-neighbor concept is not an exact match.
- Near-neighbor and outside-ontology predictions must receive a mechanism-overlap assessment and be reported in the diagnostic output.

EVALUATION LEVELS

Perform evaluation at both levels below. Keep their counts separate.

LEVEL 1: SEGMENT-LEVEL BIAS DETECTION

The segment-level question is:

"Does this eligible reasoning segment contain at least one manifested hidden cognitive-bias instance?"

Segment-level evaluation is binary:
- A segment is ground-truth positive if it contains one or more hidden bias instances.
- A segment is ground-truth negative if it is an eligible reasoning segment containing no hidden bias instance.
- A RAG segment detection is positive if one or more RAG `identified_occurrences` are localized to that segment.
- RAG `candidate_biases` do not count as positive detections in primary Signal Detection Theory metrics.

Use segment-level outcomes as follows:
- Hit: Ground-truth positive segment and one or more RAG identified occurrences localize to that segment.
- Miss: Ground-truth positive segment and no RAG identified occurrence localizes to that segment.
- False positive / false alarm: Ground-truth negative segment and one or more RAG identified occurrences localize to that segment.
- Correct rejection: Ground-truth negative segment and no RAG identified occurrence localizes to that segment.

Important:
- Segment-level results assess whether the system detected biased reasoning in the correct general location.
- Segment-level hits do not prove that the RAG system supplied the correct bias label or mechanism.
- A RAG prediction with the wrong bias label at a genuinely biased ground-truth segment can still produce a segment-level hit while producing an instance-level miss and an instance-level false positive.
- Do not calculate label-level correct rejections across all conceivable cognitive-bias labels. The ontology is non-exhaustive. Correct rejections are reported only at the finite segment-detection level.

LEVEL 2: INSTANCE-LEVEL BIAS IDENTIFICATION AND CLASSIFICATION

For each hidden planned bias instance, determine whether exactly one RAG `identified_occurrence` matches it.

An exact instance-level hit requires all of the following:
1. Correct target canonical bias label, or an approved established alias mapping;
2. Correct localization to the intended raw-interview reasoning segment or a substantively equivalent evidence span;
3. Materially correct bias-specific mechanism;
4. Materially correct affected reasoning operation;
5. Interview evidence that genuinely supports the hidden instance;
6. No conflict with the hidden instance's distinctiveness requirement.

The primary instance-level score is strict:
- A prediction that has the correct label but the wrong location is not an exact hit.
- A prediction that has the correct label and location but a materially wrong mechanism is not an exact hit.
- A prediction that correctly detects a biased segment but assigns the wrong bias is not an exact hit.
- A prediction with a partial but incomplete mechanism is not an exact hit.

In addition to strict primary scoring, produce secondary diagnostic classifications for:
- Correct location, wrong label;
- Correct label, wrong location;
- Correct label and location, but materially wrong mechanism;
- Correct label and location, but partially matching mechanism;
- Approved alias mapping;
- Near-neighbor label with substantial mechanism overlap;
- Outside-ontology label with substantial mechanism overlap;
- Duplicate prediction;
- Unsupported prediction;
- Invalid or fabricated quotation;
- Candidate-only omission.

INPUT VALIDATION

Before scoring:
1. Validate whether `RAG_ANALYSIS_OUTPUT` is parseable JSON.
2. Validate whether it conforms materially to the expected RAG schema.
3. Record schema violations, missing required fields, invalid confidence values, mismatched summary counts, invalid quotation claims, and other format failures.
4. Continue substantive scoring when feasible even if schema errors exist.
5. If the output cannot be parsed at all, return valid evaluator JSON indicating that substantive automated matching was not possible, with all appropriate counts set to null rather than invented.

Do not score RAG `candidate_biases` as identified cognitive-bias detections in primary SDT or instance-level counts.
Record candidates in a separate candidate-analysis section.

SEGMENT-MAP MODES

You must support two modes.

MODE A: PREVALIDATED SEGMENT MAP PROVIDED

If `<EVALUATION_SEGMENT_MAP>` contains a non-empty, valid segment map:
- Treat it as authoritative.
- Do not add, remove, merge, split, or revise its segments.
- Set `segment_map_status` to `prevalidated_provided`.
- Use its segment IDs, quotations, speaker assignments, and ground-truth bias-presence labels for segment-level scoring.
- Use the complete generation specification and raw interview only to validate RAG localization, hidden-instance mapping, quotations, and mechanism matching.

MODE B: NO PREVALIDATED SEGMENT MAP PROVIDED

If `<EVALUATION_SEGMENT_MAP>` is absent, empty, null, or invalid:
- Derive an evaluation segment map from the raw interview and complete generation specification.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Create the map before evaluating the RAG output.
- Derive the map using the raw interview and complete generation specification only.
- Do not let the RAG system's output determine which segments exist, where boundaries are placed, or whether segments are positive or negative.
- Return the complete generated segment map in the evaluator output so it can be reviewed, frozen, and reused in later benchmark runs.

SEGMENT-MAP CONSTRUCTION RULES

When generating a segment map:

1. Construct an exhaustive set of non-overlapping eligible reasoning segments.
2. Use the smallest contiguous speaker-attributed text span that contains one coherent reasoning operation.
3. An eligible reasoning segment must contain one or more of:
   - A judgment;
   - A decision;
   - An interpretation;
   - An inference;
   - A causal attribution;
   - A choice between alternatives;
   - A reason for action;
   - A resource-allocation rationale;
   - A prediction;
   - A communication or labeling choice;
   - A reason for weighting, ignoring, or prioritizing evidence;
   - A stated rationale for continuing, changing, rejecting, escalating, or deferring a course of action.
4. Do not create an eligible segment solely for:
   - Greetings;
   - Rapport-building;
   - Pure factual scene-setting with no reasoning;
   - Interviewer questions containing no expressed reasoning;
   - Neutral acknowledgements;
   - Generic educational discussion;
   - Mere mentions of bias terminology;
   - Hypothetical prompts that do not themselves express an adopted reasoning process;
   - Rhetorical repetition with no distinct reasoning operation.
5. Split a speaker turn where it contains distinct reasoning operations, distinct decisions, or separately expressed rationales.
6. Keep co-located bias mechanisms in the same segment only when they cannot be separated without losing their meaning.
7. Create separate segments for independently expressed mechanisms, even when they occur in the same speaker turn.
8. Map each hidden planned instance to the narrowest segment or segments that actually express its mechanism in the raw interview.
9. Mark a segment as ground-truth positive only when it contains at least one manifested hidden bias instance.
10. Mark every other eligible reasoning segment as ground-truth negative.
11. Do not create trivial negative segments merely to increase correct-rejection counts.
12. Do not omit substantive non-biased reasoning segments merely because the RAG system did not identify them.
13. Use exact raw-interview quotations for generated segments.
14. Assign stable sequential IDs in interview order: `seg_001`, `seg_002`, and so on.

Do not assume that all interviews have numbered phases, decision points, repeated structural patterns, or the same number of reasoning episodes.

LOCALIZATION MATCHING RULES

For every RAG `identified_occurrence`, determine its best segment-level localization using:
- Exact quote overlap;
- Substantively equivalent paraphrase;
- Correct speaker attribution;
- Correct reasoning episode;
- Correct decision context where one exists;
- Consistency with the raw interview.

Use these localization outcomes:

- `exact_quote_match`:
  The RAG quote is exact, valid, and directly overlaps the mapped segment's primary evidence span.

- `substantive_span_match`:
  The RAG quote differs from the mapped anchor but accurately identifies a substantively equivalent raw-interview statement in the same reasoning segment.

- `same_episode_adjacent_span`:
  The RAG evidence is in the same broader reasoning or decision episode but is not the specific mapped mechanism span.

- `wrong_segment`:
  The RAG output refers to a different reasoning episode, different decision, unrelated speaker statement, or a segment that does not contain the intended mechanism.

- `unsupported_or_fabricated_quote`:
  The claimed quote does not appear in the raw interview, is materially altered, is attributed to the wrong speaker, or does not support the claimed finding.

Only `exact_quote_match` and `substantive_span_match` qualify as correct localization for an exact instance-level hit.

A `same_episode_adjacent_span` result may support a secondary partial-location diagnostic but is not an exact instance-level hit unless the intended mechanism is still clearly supported.

BIAS-LABEL MATCHING RULES

For each RAG predicted bias label, apply this hierarchy:

1. `exact_canonical_match`:
   The RAG canonical label equals the hidden target canonical bias label.

2. `approved_alias_match`:
   The predicted label is an established spelling variant, alias, or equivalent term for the hidden target label, and the stated mechanism is substantively identical to the target mechanism.

3. `near_neighbor_label`:
   The predicted label is conceptually related to the target label but not an established synonym or equivalent. Assess mechanism overlap but do not count it as an exact label match.

4. `outside_ontology_equivalent`:
   The predicted label is outside the benchmark reference ontology but is an established alternate name for the target construct and has substantively identical mechanism. This may be approved as an alias match only when the equivalence is clear and explicitly justified.

5. `outside_ontology_non_equivalent`:
   The predicted label is outside the reference ontology and does not have a substantively identical mechanism to a target label. It is not an exact match.

6. `wrong_label`:
   The predicted label does not match the target label and does not qualify as an approved equivalent.

Do not approve an alias or outside-ontology equivalence merely because:
- The labels often co-occur;
- The labels are both broad cognitive-bias concepts;
- The labels concern the same decision;
- The labels share some evidence;
- The predicted label is plausible;
- The predicted label is a more general or more specific construct.

MECHANISM-OVERLAP SCORING

For each predicted occurrence and best candidate hidden instance, assess mechanism overlap independently of label agreement.

Use exactly one of:

- `full_mechanism_match`:
  The RAG explanation captures the defining hidden mechanism, relevant evidence weighting or reasoning distortion, and affected reasoning operation.

- `substantial_mechanism_overlap`:
  The RAG explanation captures the central mechanism but omits or weakly states one meaningful element, such as the relevant competing evidence, temporal feature, social-proof feature, prior-investment feature, ordering feature, or reasoning operation.

- `partial_mechanism_overlap`:
  The RAG explanation identifies a related mechanism but misses one or more central defining elements.

- `minimal_mechanism_overlap`:
  The RAG explanation is broadly related to the situation but does not identify the hidden bias-specific mechanism.

- `no_mechanism_overlap`:
  The RAG explanation does not correspond meaningfully to the hidden mechanism.

To receive an exact instance-level hit, the RAG occurrence must have `full_mechanism_match`.

A `substantial_mechanism_overlap` may be recorded as a secondary diagnostic partial match but is not a primary exact hit.

When evaluating near-neighbor or outside-ontology labels:
- Always report their mechanism-overlap level.
- State the specific shared and non-shared mechanism elements.
- Do not award an exact hit unless the label qualifies under the approved alias/equivalence rules and the mechanism is a full match.

ONE-TO-ONE INSTANCE MATCHING

Use one-to-one matching between RAG `identified_occurrences` and hidden planned instances.

Apply this matching priority:
1. Exact or approved-equivalent label match;
2. Correct localization;
3. Full mechanism match;
4. Correct affected reasoning operation;
5. Strongest exact raw-quote evidence;
6. Earliest occurrence order as a deterministic tie-breaker.

Each hidden instance can match at most one RAG occurrence.
Each RAG occurrence can match at most one hidden instance.

If multiple RAG occurrences match the same hidden instance:
- Select the best matching occurrence as the potential match.
- Classify remaining unmatched duplicates as instance-level false positives.
- Record them as `duplicate_prediction`.

If one RAG occurrence appears relevant to multiple hidden instances:
- Match it to only one hidden instance according to the priority rules.
- Do not award one prediction multiple exact hits.
- Record insufficiently separated co-located predictions in the diagnostic output.

PRIMARY INSTANCE-LEVEL ACCOUNTING

Use the following strict accounting:

- True positive / hit:
  One RAG occurrence exactly matches one hidden instance according to label, localization, and full-mechanism rules.

- False negative / miss:
  One hidden instance has no exact matching RAG occurrence.

- False positive:
  One RAG identified occurrence has no exact matching hidden instance.

A RAG occurrence that identifies the correct biased segment but uses the wrong label:
- Counts as one instance-level false positive for the predicted label;
- Counts as one instance-level false negative for the unmatched hidden target;
- Must additionally be recorded as `correct_location_wrong_bias_label`;
- May produce a segment-level hit if it localizes to a ground-truth positive segment.

A RAG occurrence with the correct label but wrong segment:
- Counts as one instance-level false positive;
- Leaves the true hidden instance as an instance-level false negative;
- Must be recorded as `correct_label_wrong_location`.

A RAG occurrence with correct label and correct location but a materially incorrect mechanism:
- Counts as one instance-level false positive;
- Leaves the true hidden instance as an instance-level false negative;
- Must be recorded as `correct_label_location_wrong_mechanism`.

A RAG occurrence with correct label and location but substantial, not full, mechanism overlap:
- Does not count as an exact primary true positive;
- Counts as one primary false positive and leaves the hidden instance as one primary false negative;
- Must be recorded as `partial_mechanism_match`;
- Must receive the appropriate mechanism-overlap level.

CONFIDENCE EVALUATION

The RAG system may return `high`, `moderate`, or `low` confidence identified occurrences.

For primary scoring:
- Include high-, moderate-, and low-confidence findings equally in the all-confidence confusion matrices.
- Do not treat low-confidence findings as candidates.
- Do not exclude low-confidence findings from false-positive counts.

Also calculate three nested threshold analyses:
1. `high_only`: Include only RAG findings with confidence `high`.
2. `high_and_moderate`: Include RAG findings with confidence `high` or `moderate`.
3. `all_identified_confidence_levels`: Include RAG findings with confidence `high`, `moderate`, or `low`.

For each threshold:
- Recalculate segment-level TP, FN, FP, and TN.
- Recalculate instance-level TP, FN, and FP.
- Report precision, recall, and F1 where denominators permit.
- Use null, not zero, when a metric denominator is zero.

Do not include `candidate_biases` in any confidence threshold.

CANDIDATE ANALYSIS

Evaluate RAG `candidate_biases` separately.

For each candidate:
- Determine whether it overlaps a hidden instance.
- Determine whether its quoted evidence is valid.
- Determine whether it would have been correct if promoted to an identified occurrence.
- Do not count it as a primary hit, miss, false positive, false alarm, or correct rejection.
- Record whether it represents a useful abstention, an unsupported speculation, a near miss, or a correctly localized but underconfident target.

ZERO-BIAS AND CONTROL INTERVIEWS

Some interviews contain no hidden cognitive-bias instances.

For an interview whose hidden manifest contains zero planned occurrences:
- Every eligible reasoning segment in the authoritative or generated segment map is ground-truth negative.
- Every RAG identified occurrence is an instance-level false positive.
- Every RAG localized bias prediction on an eligible segment is a segment-level false positive / false alarm.
- Every eligible segment with no RAG identified occurrence is a segment-level correct rejection.
- Candidates remain outside primary SDT counts but must be reported in candidate analysis.
- Do not create artificial positive segments merely because the RAG output identifies a bias.

COUNTERFACTUAL AND AMBIGUOUS-VOCABULARY INTERVIEWS

For counterfactual and ambiguous-vocabulary interviews:
- Use the complete generation specification to distinguish facts available at the time of the target reasoning from post-decision information.
- Do not credit a RAG system for using hindsight-only facts as evidence that a bias occurred.
- Do not assume a bias remains present merely because it existed in a paired scenario or is familiar from another scenario.
- Treat ambiguity as evidence of a bias only when the hidden mechanism and raw interview demonstrate the required biased resolution, weighting, or use of ambiguity.
- Do not confuse vague wording, uncertainty, or missing information with Ambiguity Bias unless the specific hidden mechanism is present.
- Consider the documented plausible non-bias interpretation when determining whether the RAG mechanism is full, substantial, partial, minimal, or unsupported.

RAG EVIDENCE AND CORPUS-SUPPORT AUDIT

The primary purpose of this evaluation is overlap with hidden generation ground truth, not retrieval-quality scoring.

Do not independently score corpus-grounding fidelity unless the actual retrieved corpus passages or retrieval logs are supplied as inputs.

However, record:
- Whether each RAG identified occurrence claims retrieved corpus support;
- Whether corpus-support fields are present or absent;
- Whether citation metadata appears internally inconsistent, fabricated, or unverifiable from the supplied inputs;
- Whether the RAG output explicitly reports unavailable retrieved support;
- Whether lack of corpus support is disclosed.

Do not use the presence, absence, quality, or plausibility of paper citations to convert a correct or incorrect hidden-instance classification into another primary classification result.

METRICS

For each applicable score, calculate:

precision = TP / (TP + FP)

recall = TP / (TP + FN)

F1 = 2 × TP / (2 × TP + FP + FN)

Use null for a metric whose denominator is zero.

Report:

1. Segment-level all-confidence SDT counts:
   - True positives / hits;
   - False negatives / misses;
   - False positives / false alarms;
   - True negatives / correct rejections;
   - Hit rate;
   - False alarm rate;
   - Accuracy;
   - Precision;
   - Recall;
   - F1.

2. Instance-level all-confidence counts:
   - Exact true positives;
   - False negatives;
   - False positives;
   - Precision;
   - Recall;
   - F1;
   - Exact-occurrence-match rate;
   - Occurrence-count-match rate.

3. Per-bias instance-level counts:
   - Hidden requested occurrences;
   - RAG identified occurrences;
   - Exact matches;
   - Misses;
   - False positives;
   - Precision;
   - Recall;
   - F1.

4. Confidence-threshold analyses:
   - High only;
   - High plus moderate;
   - All identified confidence levels.

5. Diagnostic counts:
   - Correct-location/wrong-bias-label errors;
   - Correct-label/wrong-location errors;
   - Correct-label-location/wrong-mechanism errors;
   - Partial-mechanism matches;
   - Duplicate predictions;
   - Unsupported predictions;
   - Fabricated or invalid quotations;
   - Approved alias mappings;
   - Near-neighbor predictions;
   - Outside-ontology predictions;
   - Candidate findings;
   - Candidate near misses;
   - Candidate useful abstentions.

6. Localization-quality counts:
   - Exact quote matches;
   - Substantive span matches;
   - Same-episode adjacent-span matches;
   - Wrong-segment predictions;
   - Unsupported or fabricated quote predictions.

REQUIRED OUTPUT SCHEMA

Return exactly this JSON structure:

{
  "evaluation_metadata": {
    "task": "rag_cognitive_bias_benchmark_evaluation",
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "raw_interview_available": true,
    "complete_generation_specification_available": true,
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable",
    "primary_scoring_policy": "strict_instance_matching_plus_segment_level_sdt",
    "candidate_policy": "excluded_from_primary_metrics",
    "outside_ontology_policy": "mechanism_overlap_assessed_separately"
  },
  "input_validation": {
    "rag_output_schema_violations": [
      {
        "violation_type": "string",
        "details": "string"
      }
    ],
    "rag_summary_count_consistency": {
      "status": "consistent | inconsistent | not_assessable",
      "details": "string"
    },
    "evaluation_limitations": [
      "string"
    ]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "string",
        "speaker": "string",
        "segment_type": "string",
        "raw_interview_anchor": "string",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["string"],
        "ground_truth_rationale": "string"
      }
    ]
  },
  "segment_level_adjudications": [
    {
      "segment_id": "string",
      "ground_truth_status": "positive | negative",
      "ground_truth_instance_ids": ["string"],
      "rag_identified_occurrence_ids": ["string"],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit | miss | false_positive | correct_rejection",
      "localization_basis": "string",
      "adjudication_note": "string"
    }
  ],
  "instance_level_adjudications": [
    {
      "hidden_instance_id": "string",
      "hidden_canonical_bias_name": "string",
      "hidden_decision_or_episode": "string | null",
      "hidden_mechanism": "string",
      "hidden_affected_reasoning_operation": "string | null",
      "hidden_evidence_source": "string | null",
      "matched_rag_occurrence_id": "string | null",
      "rag_predicted_bias_name": "string | null",
      "rag_confidence": "high | moderate | low | null",
      "label_match_type": "exact_canonical_match | approved_alias_match | near_neighbor_label | outside_ontology_equivalent | outside_ontology_non_equivalent | wrong_label | no_prediction",
      "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
      "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
      "affected_reasoning_operation_match": "full | partial | none | not_assessable",
      "primary_instance_outcome": "true_positive | false_negative",
      "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | candidate_only_near_miss | no_matching_prediction",
      "mechanism_overlap_explanation": "string",
      "evidence_fidelity_assessment": "string",
      "adjudication_note": "string"
    }
  ],
  "unmatched_rag_predictions": [
    {
      "rag_occurrence_id": "string",
      "rag_predicted_bias_name": "string",
      "rag_ontology_status": "reference_ontology | outside_reference_ontology | unknown",
      "rag_confidence": "high | moderate | low | null",
      "best_related_hidden_instance_id": "string | null",
      "best_related_hidden_bias_name": "string | null",
      "localized_segment_id": "string | null",
      "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
      "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
      "classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | outside_ontology_non_equivalent",
      "why_not_an_exact_match": "string"
    }
  ],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [
      {
        "candidate_id": "string",
        "proposed_bias_name": "string",
        "localized_segment_id": "string | null",
        "best_related_hidden_instance_id": "string | null",
        "quote_validity": "valid | invalid | not_assessable",
        "would_match_if_promoted": false,
        "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
        "details": "string"
      }
    ]
  },
  "segment_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    },
    "high_only": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    },
    "high_and_moderate": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    }
  },
  "instance_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    },
    "high_only": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    },
    "high_and_moderate": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    }
  },
  "per_bias_metrics": [
    {
      "canonical_bias_name": "string",
      "hidden_requested_occurrences": 0,
      "rag_identified_occurrences_all_confidence": 0,
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "count_match_status": "exact_match | underdetected | overdetected | not_applicable"
    }
  ],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_mapping_count": 0,
    "near_neighbor_prediction_count": 0,
    "outside_ontology_prediction_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "instance_level_primary_result": "string",
    "main_failure_modes": [
      "string"
    ],
    "main_strengths": [
      "string"
    ],
    "benchmark_interpretation": "string"
  }
}

OUTPUT RULES

1. Always return all top-level fields in the required schema.
2. Use empty arrays for no items.
3. Use null only where the schema permits null.
4. Use JSON booleans, not quoted booleans.
5. Use integer counts, not strings.
6. Use numeric metric values rounded to four decimal places.
7. Use null, not 0, for a rate or metric with a zero denominator.
8. Set `primary_corpus_fidelity_score_available` to false unless actual retrieved passages, source chunks, or retrieval logs are supplied as inputs.
9. Do not calculate d-prime, criterion, ROC statistics, or other advanced SDT metrics unless explicitly requested in a separate instruction and the segment-level trial data are suitable.
10. Do not report a label-level true-negative or correct-rejection count.
11. Report correct rejections only in `segment_level_metrics`.
12. Do not include RAG candidates in primary segment-level or instance-level metrics.
13. Count every unmatched RAG identified occurrence exactly once in `unmatched_rag_predictions`.
14. Ensure all instance-level false positives can be reconciled with unmatched RAG identified predictions, including wrong-label, wrong-location, wrong-mechanism, duplicate, and unsupported predictions.
15. Ensure all hidden planned instances are represented exactly once in `instance_level_adjudications`.
16. If a prevalidated segment map is used, preserve its segment IDs and ground-truth labels exactly.
17. If a segment map is generated, include every generated eligible reasoning segment in interview order.
18. Keep the segment-level and instance-level confusion matrices conceptually and numerically separate.
19. Do not award a strict instance-level true positive when the model merely identifies the correct general topic, decision episode, or speaker but misses the required cognitive mechanism.
20. Do not penalize the RAG system for not identifying biases outside the exhaustive hidden manifest.
