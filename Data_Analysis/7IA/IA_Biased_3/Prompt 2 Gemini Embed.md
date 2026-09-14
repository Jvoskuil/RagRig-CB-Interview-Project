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
null
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
    "analysis_scope_note": "Evaluated the participant's self-reported reasoning during an imagery analysis task for affirmative evidence of cognitive biases; only mechanism-grounded occurrences are reported."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment",
        "anchoring heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely heavily on an initial piece of information as an anchor and to make insufficient adjustments from that anchor in subsequent judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial working-read formation upon receipt of liaison report and wide-area overview",
      "decision_point_description": "Choosing which imagery to open first and what initial hypothesis or working read to adopt.",
      "affected_reasoning_operation": "Initial hypothesis generation and probability estimation",
      "bias_specific_mechanism": "The strong liaison phrase \"offensive staging\" and the first wide-area imagery established an initial staging anchor; subsequent conflicting evidence, especially the two-day-old consolidation frame, was insufficient to move the participant off that anchor.",
      "manifestation_in_interview": "The participant reported that the liaison language stuck with him, that the wide-area overview became his working read, and that the starting point likely mattered more than he would like to admit.",
      "effect_on_reasoning_or_decision": "The participant entered the evidence review with an initial staging-oriented working read, making later adjustment toward a routine-rotation or defensive-exercise interpretation more difficult.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the liaison language stuck with me a bit — 'offensive staging' is a strong phrase. But I've learned not to take those at face value, so I told myself I'd let the imagery speak first.",
          "evidence_explanation": "The participant identifies an initial informational anchor from the liaison report phrase \"offensive staging\" while also acknowledging an intention to resist it, indicating that the anchor was salient enough to require explicit resistance."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That became my working read.",
          "evidence_explanation": "The wide-area overview, which was bundled with the liaison report, became the participant's initial hypothesis or anchor before the other imagery was evaluated."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd opened the two-day-old consolidation frame first, with no liaison language in my head yet, I might have leaned rotation initially and then had to argue myself into staging rather than the other way around. Hard to say for certain, but the starting point probably matters more than I'd like to admit.",
          "evidence_explanation": "This counterfactual explicitly demonstrates the participant's recognition that the initial anchor shaped the direction of subsequent interpretation, which is the core mechanism of anchoring bias."
        }
      ],
      "correction_or_counterevidence": "The participant stated he had learned not to take liaison reports at face value and intended to let imagery speak first, but the subsequent self-report indicates that the initial framing nevertheless anchored the working read.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source documents anchoring-and-adjustment as a cognitive heuristic in which decision makers anchor on an initial value and adjust insufficiently away from it.",
          "relevance_to_this_occurrence": "This supports the classification of the participant's initial staging read as an anchor from which he did not sufficiently adjust despite encountering conflicting consolidation imagery."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmation heuristic",
        "confirmatory hypothesis testing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, or weigh evidence in ways that support an existing hypothesis or belief.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Sequential evaluation of close-look imagery after working-read formation",
      "decision_point_description": "How to weigh the two-day-old close-look frame and subsequent imagery against the initial staging hypothesis.",
      "affected_reasoning_operation": "Evidence search and evidence weighting",
      "bias_specific_mechanism": "Once the staging hypothesis was formed, the participant evaluated subsequent imagery by checking whether it fit or did not fit that picture rather than evaluating each image independently; the disconfirming routine-consolidation appearance was noted but not given sufficient weight.",
      "manifestation_in_interview": "The participant explicitly described checking whether other tiles fit the staging picture rather than starting fresh with each one, and he acknowledged noting the routine-looking consolidation but keeping moving.",
      "effect_on_reasoning_or_decision": "Evidence that was inconsistent with the staging hypothesis, particularly the two-day-old consolidation frame, was underweighted, allowing the staging interpretation to persist.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "After that I pulled the two-day-old close-look frame, and it actually looked more like routine consolidation — vehicles bunched near the motor pool, nothing dispersed. I noted that but kept moving.",
          "evidence_explanation": "The participant encountered evidence that suggested a non-staging interpretation but did not revise his working read, indicating hypothesis-consistent filtering."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once I had that staging impression in my head, I was sort of checking whether the other tiles fit or didn't fit that picture, rather than starting fresh with each one.",
          "evidence_explanation": "This is a direct self-report of confirmatory hypothesis testing: the participant framed subsequent evidence around the initial staging hypothesis rather than evaluating alternatives on equal footing."
        }
      ],
      "correction_or_counterevidence": "The participant did examine all imagery and later noted open items such as the resupply gap and pending multispectral pass, but this occurred after the staging hypothesis had already shaped the evaluation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The goals for this study were to document the extent of the conﬁrmation bias exhibited by ana- lysts working the initial steps of a problem...",
          "mechanism_supported_by_source": "Confirmation bias is documented as a measurable tendency in intelligence analysis to select and prioritize evidence in a hypothesis-consistent manner.",
          "relevance_to_this_occurrence": "This supports classifying the participant's hypothesis-driven evaluation of subsequent imagery as confirmation bias in an intelligence analysis context."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness bias",
      "alternative_labels": [
        "representativeness heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the probability or category of something by its similarity to a prototype or familiar pattern while ignoring base rates or source-specific characteristics.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of ambiguous dispersal pattern as offensive staging or defensive exercise",
      "decision_point_description": "Resolving the ambiguity of the dispersal pattern between staging, rotation, or defensive exercise.",
      "affected_reasoning_operation": "Categorization and diagnostic inference under ambiguity",
      "bias_specific_mechanism": "The participant judged the ambiguous dispersal pattern by its visual similarity to his own service's familiar offensive staging template, while underweighting partner-force-specific doctrine and base-rate information that pointed toward centralized garrison-based defensive behavior.",
      "manifestation_in_interview": "The participant said the pattern matched the shape of how his own side would stage armor forward and hold logistics back before an offensive operation, and acknowledged that this visual match drove the call despite noting a doctrinal difference.",
      "effect_on_reasoning_or_decision": "The ambiguous activity was categorized as offensive staging rather than a defensive exercise rehearsal, in part because it resembled a known offensive template rather than because partner-force base rates supported that conclusion.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at the spacing and thought about how we'd stage armor forward and hold logistics back before an offensive operation — that's fairly standard doctrine on our side. The pattern I was seeing matched that shape closely enough that I called it staging.",
          "evidence_explanation": "The participant explicitly used similarity to a familiar offensive-staging prototype from his own service to classify the ambiguous pattern, which is the core of representativeness-based judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered it, but honestly the visual match to an offensive posture was strong enough that it drove the call. I flagged the doctrinal difference in my notes as something to watch, but it didn't change my primary read at the time.",
          "evidence_explanation": "This shows that base-rate or source-specific information about the partner force's doctrine was available but did not outweigh the similarity-based judgment."
        }
      ],
      "correction_or_counterevidence": "The participant did flag the doctrinal difference as something to watch, but this did not change the primary read; a later follow-on report noting the absence of pre-offensive fuel and ammo resupply emerged only after the staging interpretation had been made.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage provided a direct operational definition of representativeness bias. Classification relies on established cognitive-science knowledge; a retrieved source only mentioned representativeness bias in a clinical decision-support context without supplying diagnostic criteria.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge likelihood, identity, or frequency by the ease with which examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Classification of partially obscured object in same-day imagery",
      "decision_point_description": "Whether to classify the obscured object as artillery, mark it unidentified and wait, or request a multispectral re-task.",
      "affected_reasoning_operation": "Object classification under ambiguity",
      "bias_specific_mechanism": "A recent and easily recalled case of a netted self-propelled artillery piece became the dominant template for classifying the ambiguous object, despite the participant recognizing other plausible fits such as engineering equipment or a fuel bowser array.",
      "manifestation_in_interview": "The participant reported having worked a very similar case about three weeks earlier and that the silhouette looked close enough to that case that he called it the same type.",
      "effect_on_reasoning_or_decision": "The obscured object was classified as self-propelled artillery rather than left unidentified or deferred for multispectral confirmation; a later better-lit pass suggested it was actually more like an engineering vehicle.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd worked a very similar case about three weeks earlier — a netted shape that turned out to be a self-propelled artillery piece, confirmed later. This silhouette looked close enough to that one that I called it the same type.",
          "evidence_explanation": "The recent case was highly available in memory and was used as the primary basis for classifying an ambiguous silhouette, illustrating availability-based judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered both but went with the artillery call because the shape match to the recent case felt solid.",
          "evidence_explanation": "The participant chose the recent-example match over the more conservative options of marking the object unidentified or waiting for multispectral data, showing that the available recent case influenced the decision."
        }
      ],
      "correction_or_counterevidence": "The participant did consider marking the object as unidentified and requesting a multispectral re-task, but the recent case exerted a stronger influence; a later better-lit pass indicated the object was more consistent with engineering equipment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly defined or operationalized the availability heuristic. Classification relies on established cognitive-science knowledge rather than RAG-corpus support.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "plan continuation"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final confidence-leveled write-up under time pressure",
      "supporting_interview_quote": "Given the time crunch and the extra tasking eating into my window, I went with a written assessment that reflected my working view, flagged as moderate-to-high confidence, with the gaps noted in an annex.",
      "plausible_mechanism": "The participant may have continued with the existing staging assessment despite accumulating open items such as the resupply gap and pending multispectral pass, consistent with plan continuation bias.",
      "why_not_identified": "Time compression, the late-arriving unrelated tasking, and the legitimate requirement to provide a confidence-leveled write-up are strong non-bias structural explanations; the participant also explicitly noted gaps and did not claim maximal confidence."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "overconfidence bias",
      "alternative_labels": [
        "overconfidence effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Confidence calibration for the final assessment",
      "supporting_interview_quote": "Moderate-to-high on staging, mostly resting on the dispersal pattern and the object classification. I noted the resupply gap and the pending multispectral pass as open items.",
      "plausible_mechanism": "Subjective confidence may have exceeded what the available evidence could justify given the unresolved resupply gap and object-classification uncertainty.",
      "why_not_identified": "The participant expressed moderate-to-high rather than extreme confidence, explicitly noted open items, and was subsequently asked by command to walk through the confidence rationale, which suggests the occurrence of a distinct overconfidence distortion is not sufficiently established."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on retrospective self-report, which may be subject to recall or self-presentation distortions.",
    "Direct RAG corpus support was available for anchoring and confirmation bias only; representativeness and availability classifications rely on established cognitive-science knowledge rather than retrieved passages.",
    "Anchoring, confirmation, representativeness, and availability mechanisms can interact and may share a common initial trigger, so boundaries among occurrences are analytic rather than fully independent."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Biased_3_Gemini_on",
  "interview_id": "IA_Biased_3",
  "system_prompt_id": "Gemini",
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
