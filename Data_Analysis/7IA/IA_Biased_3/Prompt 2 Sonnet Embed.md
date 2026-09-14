You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. As discussed, this is a cognitive task analysis interview — I'm interested in how you actually worked through the KESTREL tasking, not in grading the outcome. Everything's for internal research purposes only. Can you confirm you're comfortable walking through it in detail?

Participant: Yeah, that's fine. I've got about forty minutes before my next shift block.

Interviewer: Great. Can you start by telling me what you were asked to do and how the tasking landed on your desk?

Participant: Sure. It came in mid-shift, out of the normal cycle. The regional J2 wanted a reassessment of Site KESTREL — it's a logistics site near the border we track seasonally. A partner-nation liaison had flagged "unusual activity" and their initial write-up used the phrase "buildup consistent with offensive staging." That report came in before I'd looked at any imagery myself. Then almost right after, three new tiles dropped into my queue: a wide-area overview, a close-look EO frame from two days earlier, and a same-day close-look frame that was partially obscured by cloud and netting. My job was to figure out whether this was staging, a routine rotation, or a defensive exercise, and get a confidence-leveled write-up to command inside an eighteen-hour window.

Interviewer: What was your gut read before you'd opened anything?

Participant: Honestly, the liaison language stuck with me a bit — "offensive staging" is a strong phrase. But I've learned not to take those at face value, so I told myself I'd let the imagery speak first.

Interviewer: Let's reconstruct the timeline. What did you actually look at first?

Participant: I opened the wide-area overview first, mostly because it was the tile tagged alongside the liaison report in the queue — they'd been bundled together. It showed a dispersal pattern that reminded me of a staging posture we'd seen in a prior offensive buildup a couple years back. That became my working read. After that I pulled the two-day-old close-look frame, and it actually looked more like routine consolidation — vehicles bunched near the motor pool, nothing dispersed. I noted that but kept moving.

Interviewer: Did the order you reviewed things in change how you weighed them?

Participant: I don't think so — I mean, I looked at everything. But I'll admit the overview set the frame. Once I had that staging impression in my head, I was sort of checking whether the other tiles fit or didn't fit that picture, rather than starting fresh with each one. If I'd opened the two-day-old consolidation shot first, I might've framed the whole thing as routine and been checking the overview against that instead.

Interviewer: Let's go through the first real decision point. You had the liaison report, three tiles, and a seasonal baseline. What were your options for how to proceed?

Participant: I could've started with the same-day frame since it was the most current, even though it was partially obscured. Or gone strictly in capture-time order, oldest to newest. Or done what I did — open the one paired with the liaison flag first. I went with the third option.

Interviewer: Why that one?

Participant: Partly habit — cued reporting tends to get first look in triage. And partly, I wanted to see what had prompted the liaison's language before I looked at anything else.

Interviewer: Second decision point — interpreting the dispersal pattern itself. What was ambiguous there?

Participant: The vehicle count and spread could go either way — offensive staging or a defensive exercise rehearsal. There was no confirmed OB change, no unit redesignation reported. And I knew this partner force's doctrine tends to be pretty centralized, garrison-based, when they're doing defensive work — they don't usually disperse forward the way an offensive push would require.

Interviewer: So how did you resolve the ambiguity?

Participant: I looked at the spacing and thought about how we'd stage armor forward and hold logistics back before an offensive operation — that's fairly standard doctrine on our side. The pattern I was seeing matched that shape closely enough that I called it staging.

Interviewer: Did you weigh how this particular force typically organizes before an offensive move, versus how your own service would do it?

Participant: I considered it, but honestly the visual match to an offensive posture was strong enough that it drove the call. I flagged the doctrinal difference in my notes as something to watch, but it didn't change my primary read at the time. A follow-on report came in afterward noting the units hadn't received the fuel and ammo resupply that usually precedes an offensive push in this force's doctrine — that came after I'd already leaned into the staging interpretation.

Interviewer: What would have needed to be different for you to call it a defensive exercise instead?

Participant: Probably if I'd seen the resupply gap before I made the call, not after. Or if I'd had a clean OB update.

Interviewer: Third decision point. Tell me about the obscured object.

Participant: In the same-day frame there was a large object under netting, maybe sixty percent hidden by the net and afternoon shadow. No thermal or multispectral pass available for that specific tile. The visible edges could've been artillery, engineering equipment, or even a fuel bowser array — genuinely a few plausible fits.

Interviewer: How did you classify it?

Participant: I'd worked a very similar case about three weeks earlier — a netted shape that turned out to be a self-propelled artillery piece, confirmed later. This silhouette looked close enough to that one that I called it the same type.

Interviewer: What alternatives did you have at that point?

Participant: I could've marked it "unidentified, obscured" and waited, or pushed for a multispectral re-task before committing. I considered both but went with the artillery call because the shape match to the recent case felt solid.

Interviewer: What would you have needed to see to classify it differently?

Participant: Clearer edges, or a thermal signature. As it happened, a better-lit pass came through about two hours later and the outline actually read more like an engineering vehicle than artillery. That was after my initial classification had already gone into the working file.

Interviewer: Fourth decision point — the actual write-up. What was the situation there?

Participant: Deadline was two hours out, the multispectral re-task I'd requested wasn't going to land in time, and a second, unrelated urgent tasking got dropped on me mid-shift, which ate maybe forty percent of my remaining review time. My supervisor wanted a confidence-leveled assessment covering all three hypotheses — staging, rotation, exercise.

Interviewer: What options did you weigh?

Participant: Submit a moderate-confidence write-up laying out the competing hypotheses and where the evidence gaps were, submit a high-confidence staging call consistent with where I'd been leaning all shift, or ask for a short extension to fold in the multispectral data once it arrived. Given the time crunch and the extra tasking eating into my window, I went with a written assessment that reflected my working view, flagged as moderate-to-high confidence, with the gaps noted in an annex.

Interviewer: How confident were you overall, and what was that based on?

Participant: Moderate-to-high on staging, mostly resting on the dispersal pattern and the object classification. I noted the resupply gap and the pending multispectral pass as open items. Command actually asked for a follow-up call afterward to walk through the confidence rationale before they acted on it.

Interviewer: Looking back, if the liaison report had arrived after your own imagery review instead of before it, how do you think your initial read would have gone?

Participant: I've wondered about that. If I'd opened the two-day-old consolidation frame first, with no liaison language in my head yet, I might have leaned rotation initially and then had to argue myself into staging rather than the other way around. Hard to say for certain, but the starting point probably matters more than I'd like to admit.

Interviewer: And if the netted object had been fully visible from the start?

Participant: Then it's just a straightforward ID call, no ambiguity to resolve. The recent case wouldn't have needed to do any work for me — I'd have just read the shape directly.

Interviewer: Last one — if you'd been looking at a force that organized nothing like your own, how do you think you'd have approached the dispersal question?

Participant: I'd hope I'd have leaned harder on their documented patterns instead of what looked visually familiar to me. That's probably the piece I'd flag for myself to slow down on next time.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Biased_3",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Imagery/GEOINT Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Unscheduled Tasking at Site KESTREL: Border Staging Area Reassessment",
    "scenario_summary_internal": "A GEOINT analyst receives an urgent, out-of-cycle tasking to reassess a border-area logistics site after a partner-nation liaison flags 'unusual activity.' Over roughly 18 hours, the analyst reviews a mixed batch of commercial and national-system imagery, historical exercise-pattern archives, and a partially obscured collection frame, then produces a time-sensitive written assessment of whether the site indicates offensive staging, routine rotation, or defensive exercise activity. The scenario is designed to elicit exactly one instance each of Mirror Imaging Bias (interpreting adversary intent through the lens of how the analyst's own force would operate), Order Effects (the sequence in which imagery tiles are reviewed anchors the analyst's working hypothesis before all evidence is weighed), and Perceptual Bias (an ambiguous, partially obscured object is pattern-matched to a familiar template based on expectation rather than available detail).",
    "occupational_realism": {
      "objective": "Determine, within a compressed reporting window, whether observed activity at Site KESTREL represents offensive force staging, routine logistics rotation, or a defensive exercise, and issue a written assessment to the requesting command.",
      "setting": "A national-level imagery exploitation cell supporting a regional command; the analyst works a rotating shift with access to commercial electro-optical imagery, national reconnaissance system tasking, a historical pattern-of-life archive, and a liaison cell from a partner nation.",
      "constraints": [
        "18-hour reporting window driven by an operational planning deadline",
        "Partial cloud cover and camouflage netting obscure key portions of the site in the most recent collect",
        "Limited additional tasking capacity; only one follow-on collect can be requested before the deadline",
        "Partner-nation liaison report is unverified and arrived before the analyst's own imagery review",
        "Competing priority: a second, unrelated tasking request arrives mid-shift"
      ],
      "stakeholders": [
        "Requesting regional command J2",
        "Partner-nation liaison officer",
        "Analyst's shift supervisor / quality-control reviewer",
        "Collection management office responsible for follow-on tasking"
      ],
      "technical_terms_to_use": [
        "electro-optical (EO) imagery",
        "pattern-of-life analysis",
        "order of battle (OB)",
        "collection tasking",
        "activity-based intelligence",
        "confidence level",
        "obscuration",
        "signature"
      ],
      "technical_terms_to_avoid": [
        "mirror imaging",
        "order effects",
        "perceptual bias",
        "confirmation bias",
        "anchoring",
        "cognitive bias",
        "heuristic"
      ],
      "notes_for_generator": "Do not name, define, or hint at any bias term in the interview text. All three intended biases must be inferable only from the analyst's described reasoning, evidence handling, and word choice, not from explicit labeling."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "A partner-nation liaison report, received first, states the site shows 'buildup consistent with offensive staging'",
          "Three new imagery tiles have just arrived in the queue: one wide-area overview, one close-look EO frame from two days prior, and one same-day close-look frame with partial obscuration",
          "Historical baseline shows the site is used seasonally for logistics rotations"
        ],
        "new_information_after_decision": [
          "The wide-area overview (reviewed first) shows vehicle dispersal patterns resembling a staging posture from a prior known offensive buildup",
          "Later review of the two-day-old close-look frame shows features more consistent with routine consolidation"
        ],
        "alternatives": [
          "Review the same-day, most-complete frame first to establish a baseline before consulting the liaison-flagged overview",
          "Review all tiles in capture-time order regardless of which arrived in the queue first",
          "Review the wide-area overview first because it arrived with the liaison report, letting it frame the rest of the review"
        ],
        "intended_action": "Analyst reviews the wide-area overview first (the one paired with the liaison report), forms an initial 'staging' working hypothesis, and then reviews the remaining tiles largely to fit or refine that hypothesis rather than re-weighing it from scratch."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vehicle count and dispersal at the site are ambiguous between offensive staging and a defensive exercise rehearsal",
          "The analyst's own service doctrine would disperse armor forward and concentrate logistics rearward before an offensive push",
          "No confirmed order-of-battle change or unit redesignation has been reported for the units near the site",
          "The partner nation's known doctrine historically favors centralized, garrison-based defensive postures rather than forward dispersal"
        ],
        "new_information_after_decision": [
          "A follow-on report notes the units nearby have not received the fuel and ammunition resupply that typically precedes offensive operations in this force's doctrine"
        ],
        "alternatives": [
          "Assess the dispersal pattern against the partner nation's documented doctrinal norms for defensive exercises",
          "Flag the doctrinal ambiguity explicitly and request additional collection before committing to an interpretation",
          "Interpret the dispersal pattern as offensive staging because it resembles how the analyst's own force would posture before an offensive push"
        ],
        "intended_action": "Analyst interprets the vehicle dispersal as offensive staging primarily because it matches how their own force would organize such an operation, without adequately weighing the target force's documented doctrinal differences."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The same-day close-look frame shows a large object under camouflage netting, roughly 60% obscured by netting and afternoon shadow",
          "The analyst's most recent prior case (three weeks earlier) involved a near-identical netted shape that was confirmed as a self-propelled artillery piece",
          "Visible edges in the current frame are consistent with several object classes, including artillery, engineering equipment, and a fuel bowser array",
          "No thermal or multispectral pass is available for this specific tile"
        ],
        "new_information_after_decision": [
          "A subsequent, better-lit pass two hours later shows the object's outline is more consistent with an engineering vehicle than with artillery"
        ],
        "alternatives": [
          "Classify the object as 'unidentified, obscured' pending clearer imagery",
          "Request a multispectral or thermal re-task before classifying the object",
          "Classify the object as the same artillery type identified in the recent prior case based on the similarity of the netted silhouette"
        ],
        "intended_action": "Analyst identifies the obscured object as the same artillery type seen in the recent prior case, matching the ambiguous silhouette to that recent template rather than treating the visible cues as genuinely indeterminate."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Reporting deadline is two hours away",
          "The follow-on multispectral pass has been requested but will not return before the deadline",
          "The shift supervisor asks for a confidence-leveled written assessment covering staging, rotation, or exercise hypotheses",
          "A second, unrelated urgent tasking has just been assigned to the analyst, reducing available review time by roughly 40%"
        ],
        "new_information_after_decision": [
          "The regional command requests a follow-up call to clarify the analyst's confidence rationale before acting on the report"
        ],
        "alternatives": [
          "Submit a moderate-confidence assessment that explicitly lists competing hypotheses and the evidence gaps behind each",
          "Submit a high-confidence 'offensive staging' assessment consistent with the working hypothesis formed earlier in the shift",
          "Request a short extension to incorporate the pending multispectral pass before submitting any assessment"
        ],
        "intended_action": "Analyst submits a written assessment under time pressure; this decision point is intentionally neutral and does not carry an intended bias instance, though its consequences do not confirm or refute the quality of the earlier reasoning."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were asked to do when this tasking came in.",
        "What was your first impression of the situation before you opened any imagery?"
      ],
      "timeline_reconstruction": [
        "What did you look at first, and why did you start there?",
        "What order did you review the imagery tiles in, and did that order matter to how you read them?",
        "What new information came in after each of your assessments, and how did it change your view, if at all?"
      ],
      "decision_point_probes": [
        "What alternatives did you consider at that point, and why did you rule the others out?",
        "What specific cues in the imagery drove that call?",
        "How did the partner nation's typical way of operating factor into your read of the dispersal pattern?",
        "What made you confident enough to classify that object the way you did?",
        "What would you have needed to see to change your classification?"
      ],
      "decision_basis_and_experience": [
        "Had you seen something like this before? How did that prior experience shape this call?",
        "How much time pressure did you feel at each stage, and did it affect how thoroughly you reviewed the evidence?",
        "How confident were you in each assessment, and what was that confidence based on?"
      ],
      "closing_hypotheticals": [
        "If the liaison report had never arrived, or arrived after your own imagery review, how might your initial read have differed?",
        "If the netted object had been fully visible from the start, would your classification approach have changed?",
        "If you had been assessing a force that organizes very differently from your own, how might you have approached the dispersal pattern?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "oe_01",
        "bias": "Order effects",
        "decision_point": 1,
        "mechanism": "The sequence in which imagery tiles are reviewed (liaison-linked overview first) establishes an anchoring working hypothesis that shapes interpretation of subsequently reviewed tiles, rather than each tile being weighed independently on its own merits.",
        "affected_reasoning_operation": "Evidence sequencing and initial hypothesis formation",
        "evidence_available_at_time": [
          "Liaison report received first",
          "Three imagery tiles queued: wide-area overview, two-day-old close-look, same-day partially obscured close-look",
          "Seasonal logistics-rotation baseline for the site"
        ],
        "required_textual_manifestation": "Analyst explicitly states they reviewed the liaison-linked overview first and describes forming a working view from it that subsequent tiles were then read against or fit into, rather than describing an independent re-evaluation of the later tiles.",
        "plausible_nonbias_interpretation": "Reviewing the tile paired with the liaison flag first could simply reflect standard triage practice of prioritizing cued information, not necessarily biased sequencing.",
        "strength": "subtle",
        "do_not_make_explicit": ["order effects", "anchoring", "primacy"]
      },
      {
        "instance_id": "mi_01",
        "bias": "Mirror Imaging Bias",
        "decision_point": 2,
        "mechanism": "The analyst interprets the ambiguous vehicle dispersal pattern by reasoning from how their own force would organize an offensive operation, rather than applying the partner/target force's documented and doctrinally distinct operating patterns.",
        "affected_reasoning_operation": "Intent inference from ambiguous evidence",
        "evidence_available_at_time": [
          "Ambiguous dispersal pattern consistent with either offensive staging or defensive exercise",
          "Analyst's own doctrine for pre-offensive vehicle posturing",
          "Documented partner-nation doctrine favoring centralized, garrison-based defense",
          "No confirmed order-of-battle change"
        ],
        "required_textual_manifestation": "Analyst justifies the offensive-staging interpretation primarily by reference to how their own force would posture in this configuration, and gives comparatively little weight to the target force's documented doctrinal differences when probed on decision basis.",
        "plausible_nonbias_interpretation": "The dispersal pattern genuinely resembles known offensive-staging signatures from past cases, which is a legitimate pattern-matching heuristic independent of whose doctrine is being assumed.",
        "strength": "moderate",
        "do_not_make_explicit": ["mirror imaging", "assumed similarity", "ethnocentric"]
      },
      {
        "instance_id": "pb_01",
        "bias": "Perceptual Bias",
        "decision_point": 3,
        "mechanism": "A recent, superficially similar prior case primes the analyst to pattern-match an ambiguous, largely obscured object silhouette to a specific known object class, overriding attention to the genuinely indeterminate visible cues.",
        "affected_reasoning_operation": "Object classification from incomplete visual evidence",
        "evidence_available_at_time": [
          "Object roughly 60% obscured by netting and shadow",
          "Recent prior case (three weeks earlier) with a visually similar netted silhouette confirmed as artillery",
          "Multiple plausible object classes consistent with visible edges",
          "No thermal or multispectral confirmation available at time of classification"
        ],
        "required_textual_manifestation": "Analyst describes classifying the obscured object as the same type identified in the recent prior case, citing the visual similarity of the silhouette as sufficient grounds, while probes reveal the visible cues alone were genuinely ambiguous across multiple object classes.",
        "plausible_nonbias_interpretation": "Silhouette matching to a recently confirmed case is a standard and often valid tradecraft technique in imagery analysis, not necessarily evidence of biased perception.",
        "strength": "subtle",
        "do_not_make_explicit": ["perceptual bias", "priming", "template matching"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' with no paired control specified for this generation pass."
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
      "Verify each of the three intended bias instances appears exactly once, attached to a single decision point, with no repeated instantiation in probes, summaries, or hypotheticals.",
      "Verify decision point 4 remains neutral and introduces no additional bias instance despite time pressure and competing-task framing.",
      "Verify no bias name, definition, or psychological label appears anywhere in the generated interview text.",
      "Verify the interview totals between 1,215 and 1,485 words, targeting approximately 1,350.",
      "Verify exactly four decision points, each with at least two explicit alternatives.",
      "Verify probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Verify consequences described (e.g., the later multispectral pass, the follow-up clarification call) do not mechanically confirm or deny whether earlier reasoning was biased.",
      "Verify mirror-imaging instance is distinguished from perceptual-bias instance by reasoning operation (intent inference vs. object classification) and by evidence type (doctrinal comparison vs. visual silhouette matching)."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Mirror Imaging Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as intent inference reasoning from the analyst's own doctrine rather than the target force's documented doctrine, at decision point 2."
      },
      {
        "bias": "Order effects",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as sequencing of imagery-tile review anchoring the initial working hypothesis, at decision point 1."
      },
      {
        "bias": "Perceptual Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as silhouette/template pattern-matching of an obscured object to a recent prior case, at decision point 3."
      }
    ],
    "target_bias_names": [
      "Mirror Imaging Bias",
      "Order effects",
      "Perceptual Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Mirror Imaging Bias", "requested_occurrences": 1 },
      { "bias": "Order effects", "requested_occurrences": 1 },
      { "bias": "Perceptual Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "oe_01", "bias": "Order effects" },
      { "instance_id": "mi_01", "bias": "Mirror Imaging Bias" },
      { "instance_id": "pb_01", "bias": "Perceptual Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "oe_01", "bias": "Order effects", "decision_point": 1 },
      { "instance_id": "mi_01", "bias": "Mirror Imaging Bias", "decision_point": 2 },
      { "instance_id": "pb_01", "bias": "Perceptual Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "oe_01",
        "bias": "Order effects",
        "mechanism": "Review-sequence anchoring: the liaison-linked overview tile is reviewed first and establishes a working hypothesis that frames subsequent tile interpretation.",
        "affected_reasoning_operation": "Evidence sequencing and initial hypothesis formation",
        "evidence_source": "Order of imagery-tile queue review relative to liaison report arrival",
        "distinctiveness_requirement": "Must be located at the evidence-intake stage (decision point 1), distinct from the intent-inference operation at decision point 2 and the classification operation at decision point 3."
      },
      {
        "instance_id": "mi_01",
        "bias": "Mirror Imaging Bias",
        "mechanism": "Substituting own-force doctrinal logic for the target force's documented doctrine when inferring intent from ambiguous dispersal evidence.",
        "affected_reasoning_operation": "Intent inference from ambiguous evidence",
        "evidence_source": "Comparison of own doctrine vs. documented partner-nation doctrine regarding vehicle dispersal patterns",
        "distinctiveness_requirement": "Must be located at the doctrinal-comparison decision point (decision point 2), distinct from the tile-sequencing operation at decision point 1 and the silhouette-matching operation at decision point 3."
      },
      {
        "instance_id": "pb_01",
        "bias": "Perceptual Bias",
        "mechanism": "Priming from a recent superficially similar case causes an ambiguous, obscured silhouette to be classified via template match rather than genuinely indeterminate visible cues.",
        "affected_reasoning_operation": "Object classification from incomplete visual evidence",
        "evidence_source": "Comparison of current obscured silhouette to a recent (three-week-prior) confirmed case",
        "distinctiveness_requirement": "Must be located at the object-classification decision point (decision point 3), distinct from the sequencing operation at decision point 1 and the intent-inference operation at decision point 2."
      }
    ],
    "intended_strength": [
      { "instance_id": "oe_01", "bias": "Order effects", "strength": "subtle" },
      { "instance_id": "mi_01", "bias": "Mirror Imaging Bias", "strength": "moderate" },
      { "instance_id": "pb_01", "bias": "Perceptual Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_3",
    "domain_id": "IA",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (1, 2, 3) selected for mechanism fit and narrative realism per rules 1-4; decision point 4 held neutral by design since no fourth bias instance was requested; no bias shares a decision point, so the two-occurrences-per-point cap and cross-source separation rule were not triggered.",
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
        "segment_type": "initial_impression",
        "raw_interview_anchor": "\u201cHonestly, the liaison language stuck with me a bit \u2026 I\u2019d let the imagery speak first.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Initial reaction and stated intention to resist the liaison framing, before imagery review; it does not by itself manifest a hidden target mechanism."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "visual_interpretation",
        "raw_interview_anchor": "\u201cI opened the wide-area overview first \u2026 It showed a dispersal pattern that reminded me of a staging posture \u2026 That became my working read.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Visual resemblance and an initial read are present, but this span alone does not show that review order distorted interpretation of later tiles or that target-specific doctrine was displaced."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_weighting",
        "raw_interview_anchor": "\u201cThe two-day-old close-look frame \u2026 looked more like routine consolidation \u2026 I noted that but kept moving.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This reports conflicting imagery being noticed. The order-driven framing mechanism is explicitly articulated in the next response; this span alone is not mapped as a separate intended occurrence."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "sequence_effect_reflection",
        "raw_interview_anchor": "\u201cThe overview set the frame \u2026 I was sort of checking whether the other tiles fit \u2026 If I\u2019d opened the two-day-old consolidation shot first, I might\u2019ve framed the whole thing as routine.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "oe_01"
        ],
        "ground_truth_rationale": "Directly states that the liaison-linked overview was reviewed first, established the frame, and shaped evaluation of subsequent tiles; the counterfactual identifies review order as causal."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "choice_among_review_options",
        "raw_interview_anchor": "\u201cI could\u2019ve started with the same-day frame \u2026 gone strictly in capture-time order \u2026 or done what I did \u2026 I went with the third option.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Describes the chosen triage sequence; mere prioritization of a cued tile is consistent with routine triage. The hidden instance is localized to the explicit framing mechanism in seg_004."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "choice_rationale",
        "raw_interview_anchor": "\u201cPartly habit \u2014 cued reporting tends to get first look \u2026 I wanted to see what had prompted the liaison\u2019s language.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A plausible standard-triage rationale for looking at the cued tile first; without the subsequent framing in seg_004 it is not independently a hidden bias instance."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "ambiguity_and_contextual_evidence",
        "raw_interview_anchor": "\u201cThe vehicle count and spread could go either way \u2026 no confirmed OB change \u2026 this partner force\u2019s doctrine tends to be \u2026 centralized.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Lays out ambiguity and target-force doctrine as available context; it does not yet show own-force doctrine being substituted for it."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "intent_inference",
        "raw_interview_anchor": "\u201cI looked at the spacing and thought about how we\u2019d stage armor forward \u2026 The pattern \u2026 matched that shape closely enough that I called it staging.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Own-force analogy informs the call, but the interview also describes a genuine signature match. The decisive underweighting of partner-force doctrine is localized in seg_009."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "doctrinal_evidence_weighting",
        "raw_interview_anchor": "\u201cThe visual match \u2026 drove the call \u2026 I flagged the doctrinal difference \u2026 but it didn\u2019t change my primary read.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "mi_01"
        ],
        "ground_truth_rationale": "Explicitly gives primary weight to own-force familiarity over the target force\u2019s known doctrinal difference when inferring intent from ambiguous dispersal."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "hindsight_information_timing",
        "raw_interview_anchor": "\u201cA follow-on report came in afterward noting the units hadn\u2019t received the fuel and ammo resupply \u2026 that came after I\u2019d already leaned into the staging interpretation.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The resupply information arrived after the interpretation, so it is hindsight-only and does not establish what caused the earlier decision."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "counterfactual_evidence_requirement",
        "raw_interview_anchor": "\u201cProbably if I\u2019d seen the resupply gap before I made the call, not after. Or if I\u2019d had a clean OB update.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States what evidence might have changed the decision; counterfactual, not a separate manifested bias occurrence."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "uncertainty_assessment",
        "raw_interview_anchor": "\u201cThe object [was] maybe sixty percent hidden \u2026 No thermal or multispectral pass \u2026 genuinely a few plausible fits.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Accurately describes ambiguity and several plausible object classes before classification; no bias is established in this statement alone."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "object_classification",
        "raw_interview_anchor": "\u201cI\u2019d worked a very similar case \u2026 a self-propelled artillery piece \u2026 This silhouette looked close enough \u2026 I called it the same type.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "pb_01"
        ],
        "ground_truth_rationale": "Classifies a substantially obscured, ambiguous object by matching its silhouette to a recent superficially similar case rather than treating visible cues as indeterminate."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "classification_choice_rationale",
        "raw_interview_anchor": "\u201cI could\u2019ve marked it \u2018unidentified, obscured\u2019 \u2026 or pushed for a multispectral re-task \u2026 I went with the artillery call because the shape match \u2026 felt solid.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Follow-up restatement of the same DP3 choice already localized to seg_013, not a distinct additional hidden occurrence."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "hindsight_visual_update",
        "raw_interview_anchor": "\u201cClearer edges, or a thermal signature \u2026 a better-lit pass \u2026 read more like an engineering vehicle.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Later pass is hindsight information and shows a subsequent update; it cannot establish evidence available for the original classification."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "resource_and_communication_choice",
        "raw_interview_anchor": "\u201cGiven the time crunch and the extra tasking \u2026 I went with a written assessment \u2026 flagged as moderate-to-high confidence, with the gaps noted in an annex.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Decision point 4 is explicitly neutral; time pressure and a legitimate reporting requirement explain this choice."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "confidence_and_open_items",
        "raw_interview_anchor": "\u201cModerate-to-high on staging, mostly resting on the dispersal pattern and the object classification. I noted the resupply gap and the pending multispectral pass as open items.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Confidence rationale discloses unresolved evidence; hidden specification explicitly makes the final write-up decision point neutral."
      },
      {
        "segment_id": "seg_018",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "\u201cIf I\u2019d opened the two-day-old consolidation frame first \u2026 I might have leaned rotation \u2026 the starting point probably matters.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Closing counterfactual corroborates the already-mapped DP1 occurrence, not a second contemporaneous instance; primary manifestation remains seg_004."
      },
      {
        "segment_id": "seg_019",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "\u201cIf the netted object had been fully visible \u2026 it\u2019s just a straightforward ID call.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Hypothetical changed evidence condition; it adds no occurrence beyond the contemporaneous classification mapped to seg_013."
      },
      {
        "segment_id": "seg_020",
        "speaker": "Participant",
        "segment_type": "counterfactual_reflection",
        "raw_interview_anchor": "\u201cI\u2019d hope I\u2019d leaned harder on their documented patterns instead of what looked visually familiar \u2026 slow down next time.\u201d",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Hindsight reflection about the already-mapped DP2 decision, not a second contemporaneous occurrence; primary manifestation remains seg_009."
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
    "analysis_scope_note": "Analyzed the participant's reasoning for affirmatively evidenced cognitive bias mechanisms; did not infer condition, benchmark, or intended bias count."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring and adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information when making subsequent judgments, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial review order and early staging interpretation",
      "decision_point_description": "The participant chose to open the wide-area overview first because it was paired with the liaison report, and formed a staging working read before reviewing other tiles.",
      "affected_reasoning_operation": "Initial hypothesis formation and triage of imagery review order",
      "bias_specific_mechanism": "The liaison report phrase 'offensive staging' and the first bundled imagery tile served as an initial anchor that shaped the participant's working hypothesis; subsequent review was not sufficiently de-anchored despite mixed evidence.",
      "manifestation_in_interview": "The participant stated that the liaison language stuck with him, opened the paired wide-area tile first, and admitted that the overview set the frame for interpreting the other tiles.",
      "effect_on_reasoning_or_decision": "The staging hypothesis gained an initial advantage and, by the participant's account, a different starting tile likely would have produced a different frame.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the liaison language stuck with me a bit — 'offensive staging' is a strong phrase. But I've learned not to take those at face value, so I told myself I'd let the imagery speak first.",
          "evidence_explanation": "Shows the initial anchor from liaison language, even though he expressed an intention to set it aside."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I opened the wide-area overview first, mostly because it was the tile tagged alongside the liaison report in the queue — they'd been bundled together. It showed a dispersal pattern that reminded me of a staging posture we'd seen in a prior offensive buildup a couple years back. That became my working read.",
          "evidence_explanation": "Demonstrates the anchored starting point: the bundled cue made the anchor salient and immediately produced a staging working read."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But I'll admit the overview set the frame. Once I had that staging impression in my head, I was sort of checking whether the other tiles fit or didn't fit that picture, rather than starting fresh with each one. If I'd opened the two-day-old consolidation shot first, I might've framed the whole thing as routine and been checking the overview against that instead.",
          "evidence_explanation": "Explicitly acknowledges that the first tile anchored the interpretive frame and that a different starting point would likely have changed the read."
        }
      ],
      "correction_or_counterevidence": "The participant initially said he would let the imagery speak first and not take the liaison language at face value; however, his later description shows the initial cue still anchored the interpretation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved grounding for anchoring-and-adjustment comes from Rastogi et al. (2022).",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source describes anchoring-and-adjustment as an initial answer or prediction that individuals may adjust away from only insufficiently depending on conditions; it supports the core mechanism of being tied to an initial anchor.",
          "relevance_to_this_occurrence": "Here the initial tasking language and first bundled tile acted as the anchor, and the participant's subsequent interpretation remained tied to that staging frame."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Biased hypothesis testing",
        "Confirmatory evidence selection"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or strengthens one's pre-existing hypothesis or belief while giving disproportionately less attention to disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Weighing subsequent imagery and doctrinal/resupply evidence against the staging working read",
      "decision_point_description": "After forming a staging working read, the participant evaluated a two-day-old close-look frame showing routine consolidation, a doctrinal difference, and later resupply-gap information.",
      "affected_reasoning_operation": "Subsequent evidence interpretation and hypothesis testing",
      "bias_specific_mechanism": "Once the staging hypothesis was formed, the participant tested other tiles by checking whether they 'fit or didn't fit' that picture and downweighted contradictory evidence such as routine consolidation, partner-force doctrine, and missing resupply.",
      "manifestation_in_interview": "The participant reported noting routine consolidation but kept moving, described checking other tiles against the staging frame, and said the doctrinal difference did not change his primary read at the time.",
      "effect_on_reasoning_or_decision": "Contradictory evidence was insufficiently integrated, so the staging interpretation remained the primary conclusion in the write-up despite mixed evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "After that I pulled the two-day-old close-look frame, and it actually looked more like routine consolidation — vehicles bunched near the motor pool, nothing dispersed. I noted that but kept moving.",
          "evidence_explanation": "A disconfirming close-look frame was acknowledged but not allowed to reset the staging working read."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once I had that staging impression in my head, I was sort of checking whether the other tiles fit or didn't fit that picture, rather than starting fresh with each one.",
          "evidence_explanation": "Describes confirmatory hypothesis testing rather than balanced evidence evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered it, but honestly the visual match to an offensive posture was strong enough that it drove the call. I flagged the doctrinal difference in my notes as something to watch, but it didn't change my primary read at the time.",
          "evidence_explanation": "Shows disconfirming doctrinal evidence was noted and set aside while the confirming visual match drove the call."
        }
      ],
      "correction_or_counterevidence": "The participant did record the doctrinal difference and noted the resupply gap and pending multispectral pass as open items; command also requested a follow-up call on the confidence rationale. These did not change the primary read at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by Cook and Smallman (2008) on confirmation bias in intelligence analysis.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Results revealed no bias at assessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "The source documents a strong confirmation bias in selecting and prioritizing evidence, which underlies the participant's weighting of corroborating over disconfirming evidence.",
          "relevance_to_this_occurrence": "The participant selected and prioritized the initial staging-supporting visual match while underweighting routine consolidation and doctrinal mismatch."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Representativeness bias",
      "alternative_labels": [
        "Representativeness heuristic",
        "Availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the probability or identity of an ambiguous target based primarily on its similarity to a known category or prior exemplar, while underweighting base rates, missing information, and alternative possibilities.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Obscured object classification in same-day frame",
      "decision_point_description": "The participant classified a netted, partially obscured object as self-propelled artillery despite plausible alternatives and absent thermal or multispectral data.",
      "affected_reasoning_operation": "Classification or identification under ambiguity",
      "bias_specific_mechanism": "The participant judged the obscured object's identity by similarity to a recent resolved case, using representativeness rather than waiting for diagnostic information or accepting the classification as unidentified.",
      "manifestation_in_interview": "He stated that the silhouette looked close enough to a prior artillery case and called it the same type because the shape match to the recent case felt solid.",
      "effect_on_reasoning_or_decision": "The initial classification was entered into the working file as artillery; a later better-lit pass suggested it was actually an engineering vehicle.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "In the same-day frame there was a large object under netting, maybe sixty percent hidden by the net and afternoon shadow. No thermal or multispectral pass available for that specific tile. The visible edges could've been artillery, engineering equipment, or even a fuel bowser array — genuinely a few plausible fits.",
          "evidence_explanation": "Establishes the ambiguity and missing diagnostic information at the time of the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd worked a very similar case about three weeks earlier — a netted shape that turned out to be a self-propelled artillery piece, confirmed later. This silhouette looked close enough to that one that I called it the same type.",
          "evidence_explanation": "Shows the classification was driven by similarity to a recent exemplar rather than feature-level identification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered both but went with the artillery call because the shape match to the recent case felt solid.",
          "evidence_explanation": "Directly states that the recent similar case was the decisive reason for the classification."
        }
      ],
      "correction_or_counterevidence": "The participant considered marking it 'unidentified, obscured' or requesting a multispectral re-task before committing; a later better-lit pass suggested engineering vehicle, but only after the initial classification had already been entered.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No adequate retrieved passage in the provided corpus defined the representativeness mechanism; the label is used from established cognitive-science knowledge, not from retrieved papers. A passing mention of 'representativeness bias' in a retrieved clinical-decision-support paper was not definitional enough to use as support.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Write-up after evidence gaps",
      "supporting_interview_quote": "Given the time crunch and the extra tasking eating into my window, I went with a written assessment that reflected my working view, flagged as moderate-to-high confidence, with the gaps noted in an annex.",
      "plausible_mechanism": "Continuing with the previously formed staging plan despite contrary cues such as the resupply gap and pending multispectral pass.",
      "why_not_identified": "The participant explicitly attributes the action to deadline and a competing tasking, which is more consistent with ordinary time-pressure prioritization than a distinct bias-specific mechanism; it therefore does not meet the conservative evidence standard."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved passages contained OCR degradation and limited definitional coverage for representativeness.",
    "The interview is a single self-report; memory and reconstruction may limit certainty about the original reasoning."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Biased_3_Sonnet_on",
  "interview_id": "IA_Biased_3",
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
