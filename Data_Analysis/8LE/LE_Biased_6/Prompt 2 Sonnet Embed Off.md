You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
**Interviewer:** Thanks for making time for this. Just to confirm, this is a voluntary debrief for our case-review process, not a disciplinary matter — I'm here to understand how you worked the exam, not to evaluate the outcome. That okay with you?

**Participant:** Sure, that's fine. I've done these debriefs before.

**Interviewer:** Good. Can you tell me your role and how this case landed on your desk?

**Participant:** I'm a certified polygraph examiner with the department, been doing specific-issue exams for about eleven years. This one came through the detective bureau — a logistics supervisor at a regional distribution center was suspected of orchestrating an inventory theft, something in the six-figure range. The lead detective wanted a specific-issue exam done same-day because the client company had an audit deadline bearing down on them.

**Interviewer:** Walk me through the incident from the start — what did you know before you ever met the supervisor?

**Participant:** I got a written briefing from the lead detective. It laid out the theory pretty clearly — supervisor had opportunity, access to the loading manifests, and apparently some financial strain, I think there was a divorce or something similar mentioned. The briefing called him "the clear person of interest." I also had his personnel file, which was clean — no prior write-ups. No physiological data yet, obviously, this was all paper.

**Interviewer:** How did that briefing shape how you approached the pre-test interview?

**Participant:** Honestly, it gave me a lens. When I sat down with him and he was hesitant on a couple of questions, avoided eye contact once or twice, I read that as consistent with what the detective had already laid out. He did mention the divorce himself, said he'd been under a lot of stress lately, which could explain nervousness on its own. But at the time I filed that under "corroborating" rather than treating it as a separate, competing explanation. In hindsight I probably let the case narrative do some of the interpretive work before I had any test data at all.

**Interviewer:** Did you consider establishing an independent baseline first, setting the narrative aside?

**Participant:** That's the textbook approach, yes — treat the file as one input among several. I didn't fully do that here. Partly time pressure, partly just... the story fit.

**Interviewer:** Let's move to test preparation. What happened next?

**Participant:** Before hooking him up, I had a huddle with the lead detective and a junior detective who was shadowing. Both were confident he'd done it. The junior detective mentioned, almost in passing, that there was a temp worker with similar access who'd also come up in an early sweep, but nobody pushed on that. The room's mood was pretty unanimous, and we were on the clock for the audit deadline.

**Interviewer:** How did that huddle affect your test design?

**Participant:** I finalized the comparison questions along the lines the detectives expected — matching their theory about the missing inventory records. I didn't circle back to the temp-worker mention. Everyone in the room was aligned, so I didn't feel like I needed to independently chase that thread myself; it felt like if it mattered, someone would flag it later.

**Interviewer:** Was there a moment you considered raising it yourself?

**Participant:** Briefly. But it would've meant slowing things down when everyone else seemed settled, and we didn't have time for a second full test if this one went sideways.

**Interviewer:** Let's get into the exam itself. What did the chart show?

**Participant:** Instrument was calibrated fine. On the first chart, there was a clear electrodermal spike on the relevant question about the missing inventory — pronounced compared to what I'd expect from someone answering honestly. That's what jumped out at me immediately.

**Interviewer:** What about the comparison questions?

**Participant:** Those were flatter than typical, minimal reactivity. Numerical scoring protocol says you're supposed to weigh relevant and comparison reactivity against each other, not just look at the relevant question in isolation.

**Interviewer:** Did you weigh them equally in the moment?

**Participant:** If I'm being honest, no. The spike was the thing I kept coming back to — it was vivid, it was clean on the tracing, easy to point to. The flat comparison questions didn't register the same way. I noted them, but I didn't really sit with what muted comparison reactivity normally does to your confidence in a deceptive call. A second scorer looked at it later and flagged that the comparison zone was weaker than usual, which should've pulled the whole picture toward inconclusive.

**Interviewer:** How did you reconcile that with everything else you'd gathered — the pretest demeanor, the financial-strain detail?

**Participant:** I put it together as one story. The spike, the hesitation from the pretest interview, the stress he was under financially — it all lined up into something coherent. Individually, sure, any one of those pieces is thin. The hesitation could've been the divorce. The spike alone without comparison support isn't supposed to carry a deceptive call. But together they read like a consistent account of someone who wasn't being straight with me, and that's the story I built in my head sitting there.

**Interviewer:** Did his post-test interview change that?

**Participant:** He was calm, consistent, denied it again the same way he had before. I noted it, but by then I'd already told the detectives mid-afternoon that it "looked deceptive" — that impression was out there.

**Interviewer:** Let's talk about that. What happened once the full numerical scoring came in?

**Participant:** The completed scoring sheet actually sat closer to inconclusive than clearly deceptive. Borderline. But I'd already given the detectives a verbal steer earlier in the day, and walking that back felt uncomfortable — like I'd be undermining what I'd already said with less to show for it. So when I looked at the mixed data, I leaned toward not making too much of it rather than revisiting my earlier read.

**Interviewer:** In the final debrief, how was that discussed with the team?

**Participant:** The junior detective actually asked about the borderline scores, wanted to know if "deceptive" was really the right word given how close it was. The lead detective reassured him — said the totality of the evidence pointed the same direction, no need to overthink the numbers — and nobody circled back to it after that. I finalized the report consistent with what I'd told them earlier and what the team expected going in.

**Interviewer:** What would have changed that decision — what information, if it had come in earlier, would have made you write it differently?

**Participant:** If I'd completed full scoring before saying anything to the detectives, I probably would've called it inconclusive and recommended a retest. Saying something out loud too early boxed me in a bit.

**Interviewer:** How much time pressure did you feel throughout the day?

**Participant:** A lot. The audit deadline was hanging over the whole thing. That compressed everything — the huddle, the scoring, the write-up.

**Interviewer:** What happened afterward, once the report was filed?

**Participant:** Weeks later, inventory reconciliation records came back and only partially implicated him — some of it pointed back toward that temp worker the junior detective had mentioned early on. Doesn't necessarily mean the exam was wrong, but it wasn't the clean confirmation anyone was hoping for either.

**Interviewer:** Looking back, if the junior detective had pushed harder on the temp-worker lead during that huddle, how do you think that would have changed your approach?

**Participant:** I'd like to think I would've built a comparison question around it, or at least flagged it for follow-up before finalizing. Whether I actually would have, under that deadline, I honestly don't know.

**Interviewer:** And if you'd scored the chart fully before forming any verbal impression at all?

**Participant:** I think there's a real chance I call it inconclusive from the start, no argument with anyone.

**Interviewer:** Anything you'd do differently running this exam again today?

**Participant:** Finish the numbers before I open my mouth. That's the main thing.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Biased_6",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Polygraph Examiner / Interview Specialist",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Distribution Center Inventory Theft Exam",
    "scenario_summary_internal": "A police department's polygraph examiner is asked by a detective to administer a specific-issue exam on a logistics supervisor suspected of orchestrating a six-figure inventory theft at a regional distribution center, ahead of a client-imposed audit deadline. The examiner reviews the detective's case briefing, participates in a pre-test team huddle, conducts and scores the exam under time pressure, and must decide how to communicate an ambiguous result to the investigative team.",
    "occupational_realism": {
      "objective": "Determine, via a specific-issue polygraph examination and structured pre/post-test interview, whether the logistics supervisor's denial of involvement in the inventory theft is credible, and communicate a defensible finding to the investigative team before a client audit deadline.",
      "setting": "Regional police department forensic services unit, small interview/testing room adjoining a detective bureau, over a single afternoon with a same-day debrief.",
      "constraints": [
        "Client (distribution company) audit deadline creates same-day pressure for a finding",
        "Detective supervising the case has already built an investigative theory naming the supervisor as primary suspect",
        "Only one examiner and one polygraph instrument available; no time for a second full retest",
        "Chain-of-custody and testing protocol require pre-test interview, instrument calibration, and standardized comparison-question technique",
        "Examiner reports to a multi-person case team including the lead detective and a junior detective"
      ],
      "stakeholders": [
        "Polygraph examiner (subject of CTA)",
        "Lead detective (case owner)",
        "Junior detective (present at pre-test huddle)",
        "Logistics supervisor (examinee)",
        "Distribution company liaison (external pressure source, not present)"
      ],
      "technical_terms_to_use": [
        "specific-issue exam",
        "comparison question technique (CQT)",
        "relevant question",
        "comparison question",
        "chart",
        "electrodermal activity",
        "respiration tracing",
        "inconclusive result",
        "pre-test interview",
        "post-test interview",
        "numerical scoring"
      ],
      "technical_terms_to_avoid": [
        "contextual bias",
        "coherence-based reasoning",
        "rationalisation",
        "cognitive dissonance",
        "feature positive effect",
        "groupthink",
        "any explicit bias label or psychological term naming the manifest biases"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Detective's written briefing describing supervisor as the 'clear person of interest' with narrative details about opportunity and financial strain",
          "Supervisor's personnel file with no prior disciplinary record",
          "No physiological data yet collected"
        ],
        "new_information_after_decision": [
          "Supervisor's pretest interview responses, some hesitant, some fluent",
          "Supervisor discloses unrelated personal stress (divorce) as reason for nervousness"
        ],
        "alternatives": [
          "Conduct pretest interview treating the briefing as one unverified input among several, independently establishing rapport and baseline behavior",
          "Let the detective's narrative frame question wording and interpretation of the supervisor's demeanor from the outset"
        ],
        "intended_action": "Examiner allows the briefing narrative to shape how ambiguous pretest behavior (hesitation, avoidance of eye contact) is read, treating it as corroborating the detective's theory rather than as neutral behavior needing independent baseline."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pre-test huddle with lead and junior detective, both expressing confidence suspect is guilty",
          "Junior detective briefly notes an alternative internal candidate (temp worker) but does not press the point",
          "Time pressure to finalize test format before audit-driven deadline"
        ],
        "new_information_after_decision": [
          "Instrument calibrated; baseline physiological tracings collected",
          "First test chart shows a marked reaction on the relevant question about the missing inventory"
        ],
        "alternatives": [
          "Independently select comparison questions and test structure based on standard protocol regardless of team sentiment, and note the temp-worker lead for follow-up",
          "Adopt the team's consensus framing of the case, aligning comparison-question choice and initial reaction categorization with the shared expectation of the supervisor's guilt, without revisiting the temp-worker lead"
        ],
        "intended_action": "Examiner goes along with the team's unanimous framing, finalizes a comparison-question set matching the detective's theory, and lets the group's shared confidence substitute for independently probing the alternative lead."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chart shows a clear electrodermal spike on the relevant question about hiding inventory records",
          "Comparison questions show similarly flat or minimal reactivity, which is itself informative but easy to overlook",
          "Numerical scoring guidelines call for evaluating relative reactivity across all question types, not isolated spikes"
        ],
        "new_information_after_decision": [
          "A second, independent scorer later flags that comparison-question reactivity was weaker than typical, which would normally reduce confidence in a deceptive call",
          "Supervisor's post-test interview reasserts denial calmly and consistently"
        ],
        "alternatives": [
          "Complete full numerical scoring comparing relevant vs. comparison zone reactivity before drawing any conclusion, and treat the case as inconclusive if data are mixed",
          "Highlight the presence of the relevant-question spike as decisive, treating the absence of comparable reactivity on comparison questions as unremarkable rather than as data reducing confidence in a deceptive finding"
        ],
        "intended_action": "Examiner flags the visible spike as the dominant, quotable finding, discounts the diagnostic value of the muted comparison-question reactivity, and privately reconciles the ambiguous overall chart with the guilt conclusion already voiced to the team by building a narrative that ties the spike, the earlier hesitant demeanor, and the financial-strain detail into one consistent story of deception."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Examiner has already told the detectives mid-afternoon that results 'look deceptive'",
          "Full scoring sheet, once completed, sits closer to inconclusive than clearly deceptive",
          "Team debrief scheduled before the audit deadline, with detectives expecting a definitive call"
        ],
        "new_information_after_decision": [
          "Report is filed with a finding that supports the detective's original theory",
          "Weeks later, inventory reconciliation records surface that only partially implicate the supervisor and also point to the temp worker mentioned earlier"
        ],
        "alternatives": [
          "Report the numerically inconclusive result as inconclusive, explaining the mixed chart data and unresolved temp-worker lead to the team even though it contradicts the earlier verbal impression",
          "Align the final written report with the earlier verbal 'deceptive' impression and the team's shared expectation, presenting the finding as more conclusive than the numerical scoring supports"
        ],
        "intended_action": "In the debrief, the junior detective's hesitant question about the borderline scores is met with reassurance from the lead detective and no one revisits it further; the examiner finalizes a report consistent with the group's shared expectation rather than the more equivocal numerical scoring."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this case came to you and what you knew before you met the supervisor.",
        "What was your objective going into this exam?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you know at that point?",
        "What new information came in after the pre-test interview, and how did it change your plan?",
        "Describe the huddle with the detectives before testing began.",
        "Walk me through scoring the chart step by step."
      ],
      "decision_point_probes": [
        "What cues from the briefing or interview stood out to you, and why?",
        "What information sources did you rely on at each stage, and how did you weigh them against each other?",
        "What was your goal at that specific moment, and did it conflict with any other goal?",
        "What alternatives did you consider before finalizing the comparison questions and the scoring?",
        "What was your decision basis for calling the result deceptive versus inconclusive?",
        "How did your prior experience with similar cases shape your read of the charts?",
        "How much time pressure did you feel, and did it affect what you checked or didn't check?",
        "How confident were you at each stage, and did that confidence change?",
        "If you had gotten a dissenting opinion from a colleague at that point, what would you have done differently?"
      ],
      "closing_hypotheticals": [
        "If the junior detective had pushed harder on the temp-worker lead, how would that have changed your approach?",
        "If you had scored the chart before telling the detectives your impression, do you think your conclusion would have been different?",
        "What would you do differently if you ran this exam again today?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Contextual Bias",
        "decision_point": 1,
        "mechanism": "Extraneous case-narrative information (detective's briefing framing supervisor as the clear suspect) contaminates interpretation of ambiguous pretest behavioral cues before any physiological data exist.",
        "affected_reasoning_operation": "Interpretation of demeanor/behavioral cues during pretest interview",
        "evidence_available_at_time": [
          "Detective's briefing narrative naming supervisor as primary suspect",
          "Supervisor's neutral personnel file",
          "No physiological data yet"
        ],
        "required_textual_manifestation": "Examiner explicitly describes reading the supervisor's hesitation/avoidance as corroborating guilt because of what the briefing said, rather than as neutral behavior warranting independent baseline assessment.",
        "plausible_nonbias_interpretation": "Reviewing a case file before an interview is standard, professional practice and does not by itself indicate biased judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["contextual bias", "priming", "anchoring"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 2,
        "mechanism": "Unanimous verbal consensus among detectives in the pre-test huddle suppresses the examiner's independent evaluation of test design and the junior detective's alternative lead, favoring group harmony over dissent.",
        "affected_reasoning_operation": "Selection of comparison-question structure and evaluation of an alternative suspect lead",
        "evidence_available_at_time": [
          "Detectives' unanimous verbal confidence in supervisor's guilt",
          "Junior detective's brief, unpursued mention of a temp-worker alternative",
          "Deadline pressure"
        ],
        "required_textual_manifestation": "Examiner describes adopting the team's shared framing for the test structure and not revisiting the temp-worker lead because the room was in agreement, without independent verification.",
        "plausible_nonbias_interpretation": "Deferring to a lead detective's case knowledge is a normal division-of-labor practice in investigative teams.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "conformity", "consensus pressure"]
      },
      {
        "instance_id": "fpe_01",
        "bias": "Feature positive effect",
        "decision_point": 3,
        "mechanism": "The examiner disproportionately weights the presence of a visible relevant-question spike while failing to register the diagnostic significance of the absence of comparable reactivity on comparison questions.",
        "affected_reasoning_operation": "Chart scoring and evidence weighting",
        "evidence_available_at_time": [
          "Visible electrodermal spike on the relevant question",
          "Flat/minimal reactivity on comparison questions",
          "Numerical scoring protocol requiring comparison of both zones"
        ],
        "required_textual_manifestation": "Examiner recounts flagging the relevant-question spike as the standout finding while describing the comparison-question flatness as unremarkable or not worth mentioning.",
        "plausible_nonbias_interpretation": "A strong, clear physiological reaction is a legitimate and commonly emphasized scoring feature in polygraph practice.",
        "strength": "moderate",
        "do_not_make_explicit": ["feature positive effect", "absence blindness", "salience bias"]
      },
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "decision_point": 3,
        "mechanism": "Having already stated aloud to the detectives that results 'look deceptive,' the examiner experiences discomfort reconciling the borderline numerical scoring with that public commitment, and resolves it by discounting the mixed evidence rather than revising the stated impression.",
        "affected_reasoning_operation": "Updating a conclusion in light of new, disconfirming scoring information",
        "evidence_available_at_time": [
          "Earlier verbal statement to detectives calling the result 'deceptive'",
          "Numerical scoring trending toward inconclusive",
          "Supervisor's calm, consistent post-test denial"
        ],
        "required_textual_manifestation": "Examiner describes feeling uncomfortable with the borderline score given what was already said to the team and resolves the tension by minimizing the weight of the disconfirming data rather than revisiting the earlier statement.",
        "plausible_nonbias_interpretation": "Sticking with an initial professional impression can reflect legitimate confidence built from experience, not necessarily bias.",
        "strength": "moderate",
        "do_not_make_explicit": ["cognitive dissonance", "commitment bias", "belief perseverance"]
      },
      {
        "instance_id": "cr_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 3,
        "mechanism": "The examiner constructs a single tidy narrative linking the relevant-question spike, the earlier pretest hesitation, and the financial-strain detail into a mutually reinforcing story of guilt, even though each element individually is weak or ambiguous.",
        "affected_reasoning_operation": "Integration of disparate evidence into a final causal narrative",
        "evidence_available_at_time": [
          "Relevant-question spike",
          "Earlier pretest hesitation (already reinterpreted via briefing)",
          "Supervisor's disclosed financial strain",
          "Weak/ambiguous comparison-question data"
        ],
        "required_textual_manifestation": "Examiner explicitly ties together the spike, hesitant demeanor, and financial-strain detail as a coherent unified account of deception, smoothing over the individually weak or ambiguous nature of each piece.",
        "plausible_nonbias_interpretation": "Synthesizing multiple pieces of evidence into a coherent case theory is a normal and often necessary investigative skill.",
        "strength": "moderate",
        "do_not_make_explicit": ["coherence-based reasoning", "narrative fallacy", "rationalisation"]
      },
      {
        "instance_id": "gt_02",
        "bias": "Groupthink",
        "decision_point": 4,
        "mechanism": "In the final debrief, the junior detective's hesitant question about the borderline scores is met with reassurance and dropped without scrutiny, and the examiner finalizes a report matching the group's shared expectation rather than the more equivocal scoring, prioritizing team alignment over dissenting doubt.",
        "affected_reasoning_operation": "Finalization of the written report and resolution of a dissenting question",
        "evidence_available_at_time": [
          "Borderline/inconclusive-leaning numerical scoring",
          "Junior detective's hesitant question about the scores",
          "Lead detective's reassurance and the group's shared expectation of a deceptive finding",
          "Audit deadline pressure"
        ],
        "required_textual_manifestation": "Examiner describes the junior detective's question being smoothed over by the lead detective's reassurance, and finalizes the report in line with group expectation rather than probing the dissent further.",
        "plausible_nonbias_interpretation": "Trusting a supervising detective's judgment on how to close out a report is a normal chain-of-command practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "conformity", "dissent suppression"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition specification with no paired control requested in this call."
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
      "Target interview length 1,350 words (acceptable range 1,215-1,485 words); do not pad with repetitive exposition to hit the range.",
      "Exactly four decision points, each with at least two plausible alternatives.",
      "No bias name, definition, or psychological label appears anywhere in the public interview text.",
      "Each of the 6 planned instances appears exactly once, tied to the specific decision point and evidence source listed in occurrence_embedding_plan_internal.",
      "No additional unrequested instance of Contextual Bias, Coherence-based reasoning/Rationalisation, Cognitive dissonance, Feature positive effect, or Groupthink appears in probes, hypotheticals, or the outcome/consequence narrative.",
      "Consequences (partial implication of supervisor, emergence of temp-worker lead) must not mechanically confirm or deny that any decision was biased; they should remain interpretively open.",
      "Maintain distinct evidentiary bases for gt_01 (pre-test huddle/test design) and gt_02 (final debrief/report finalization) so they are independently identifiable.",
      "Maintain distinct evidentiary bases for fpe_01 (spike vs. absent comparison reactivity) and cd_01/cr_01 (dissonance from prior public statement vs. narrative integration) even though all three sit at decision point 3."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Contextual Bias", "occurrences": 1, "mechanism_constraint": "Must arise from case-narrative contamination of pretest behavioral interpretation, prior to any physiological data." },
      { "bias": "Coherence-based reasoning or Rationalisation", "occurrences": 1, "mechanism_constraint": "Must involve integration of multiple weak/ambiguous evidence pieces into one unified guilt narrative." },
      { "bias": "Cognitive dissonance", "occurrences": 1, "mechanism_constraint": "Must arise from tension between an earlier public verbal commitment and later disconfirming scoring data." },
      { "bias": "Feature positive effect", "occurrences": 1, "mechanism_constraint": "Must involve overweighting a present reaction while failing to register the significance of an absent/muted reaction." },
      { "bias": "Groupthink", "occurrences": 2, "mechanism_constraint": "Each instance must involve a distinct group setting/moment: one during pre-test test-design huddle, one during final report debrief." }
    ],
    "target_bias_names": [
      "Contextual Bias",
      "Coherence-based reasoning or Rationalisation",
      "Cognitive dissonance",
      "Feature positive effect",
      "Groupthink"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Contextual Bias", "requested_occurrences": 1 },
      { "bias": "Coherence-based reasoning or Rationalisation", "requested_occurrences": 1 },
      { "bias": "Cognitive dissonance", "requested_occurrences": 1 },
      { "bias": "Feature positive effect", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 2 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Contextual Bias" },
      { "instance_id": "gt_01", "bias": "Groupthink" },
      { "instance_id": "fpe_01", "bias": "Feature positive effect" },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance" },
      { "instance_id": "cr_01", "bias": "Coherence-based reasoning or Rationalisation" },
      { "instance_id": "gt_02", "bias": "Groupthink" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Contextual Bias", "decision_point": 1 },
      { "instance_id": "gt_01", "bias": "Groupthink", "decision_point": 2 },
      { "instance_id": "fpe_01", "bias": "Feature positive effect", "decision_point": 3 },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "decision_point": 3 },
      { "instance_id": "cr_01", "bias": "Coherence-based reasoning or Rationalisation", "decision_point": 3 },
      { "instance_id": "gt_02", "bias": "Groupthink", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Contextual Bias",
        "mechanism": "Detective's briefing narrative contaminates interpretation of ambiguous pretest behavioral cues before physiological data exist.",
        "affected_reasoning_operation": "Interpretation of demeanor during pretest interview",
        "evidence_source": "Case briefing memo vs. supervisor's actual pretest behavior",
        "distinctiveness_requirement": "Occurs pre-test, before any chart data; involves narrative-to-behavior contamination distinct from later chart-based biases."
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Unanimous huddle consensus suppresses independent test-design judgment and the temp-worker alternative lead.",
        "affected_reasoning_operation": "Selection of comparison-question structure / evaluation of alternative suspect",
        "evidence_source": "Verbal consensus in pre-test huddle",
        "distinctiveness_requirement": "Distinct group moment (pre-test huddle) and distinct content (test design, dropped alternative lead) from gt_02."
      },
      {
        "instance_id": "fpe_01",
        "bias": "Feature positive effect",
        "mechanism": "Overweighting the visible relevant-question spike while failing to register the diagnostic value of muted comparison-question reactivity.",
        "affected_reasoning_operation": "Chart scoring / evidence weighting",
        "evidence_source": "Relevant-question spike vs. comparison-question flatness on same chart",
        "distinctiveness_requirement": "Concerns presence/absence asymmetry in physiological data, distinct from the narrative-integration mechanism of cr_01 and the commitment-tension mechanism of cd_01."
      },
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "mechanism": "Tension between an earlier public 'deceptive' statement and later borderline scoring is resolved by discounting the disconfirming data.",
        "affected_reasoning_operation": "Updating conclusion given new disconfirming scoring information",
        "evidence_source": "Examiner's earlier verbal statement to detectives vs. final numerical scoring",
        "distinctiveness_requirement": "Driven specifically by prior public commitment, distinct from the pure evidence-weighting mechanism of fpe_01 and the narrative-synthesis mechanism of cr_01."
      },
      {
        "instance_id": "cr_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "mechanism": "Weak/ambiguous evidence pieces (spike, hesitation, financial strain) are woven into one internally consistent guilt narrative.",
        "affected_reasoning_operation": "Integration of multiple evidence pieces into a final causal account",
        "evidence_source": "Combination of chart spike, pretest demeanor, and disclosed financial strain",
        "distinctiveness_requirement": "Concerns narrative integration across multiple evidence types, distinct from the single-feature weighting of fpe_01 and the commitment-tension of cd_01."
      },
      {
        "instance_id": "gt_02",
        "bias": "Groupthink",
        "mechanism": "Junior detective's dissenting question about borderline scores is reassured away and dropped; report finalized to match group expectation.",
        "affected_reasoning_operation": "Finalization of written report / resolution of dissent",
        "evidence_source": "Debrief conversation and final report content",
        "distinctiveness_requirement": "Distinct group moment (final debrief) and distinct content (report finalization over scoring doubt) from gt_01."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Contextual Bias", "strength": "subtle" },
      { "instance_id": "gt_01", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "fpe_01", "bias": "Feature positive effect", "strength": "moderate" },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "strength": "moderate" },
      { "instance_id": "cr_01", "bias": "Coherence-based reasoning or Rationalisation", "strength": "moderate" },
      { "instance_id": "gt_02", "bias": "Groupthink", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Biased_6",
    "domain_id": "LE",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Spread across 4 decision points by mechanism fit and narrative realism: DP1 hosts Contextual Bias (pre-data narrative contamination); DP2 hosts one Groupthink instance (test-design huddle) as the mechanism required a group setting distinct from the debrief; DP3 hosts Feature positive effect, Cognitive dissonance, and Coherence-based reasoning together because all three naturally arise during chart scoring/interpretation but are kept independently identifiable via distinct evidence sources (single-feature weighting vs. prior-commitment tension vs. multi-evidence narrative synthesis); DP4 hosts the second Groupthink instance (report finalization/debrief) to satisfy the two-distinct-decision-point requirement for repeated biases.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": [
      "Decision point 3 hosts three distinct biases (Feature positive effect, Cognitive dissonance, Coherence-based reasoning) rather than one per decision point, because the manifest requires 5 distinct biases across only 4 decision points while keeping Groupthink's two occurrences at separate decision points per allocation rule 3-4; each of the three DP3 instances is anchored to a clearly distinct evidence source and reasoning operation to preserve independent identifiability."
    ]
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
          "segment_type": "interpretation",
          "raw_interview_anchor": "\"Honestly, it gave me a lens...\" through \"the story fit.\" (pre-test interview interpretation)",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "The examiner interprets hesitation and eye contact through the detective briefing and files divorce stress as corroboration rather than a competing explanation."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "choice_and_social_influence",
          "raw_interview_anchor": "Pre-test huddle and comparison-question design: \"The room's mood was pretty unanimous\"; \"I finalized the comparison questions...\"; \"everyone else seemed settled.\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "gt_01"
          ],
          "ground_truth_rationale": "The examiner adopts the unanimous huddle framing, drops the temp-worker lead, and aligns test design with the detectives' theory."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "evidence_weighting",
          "raw_interview_anchor": "Chart interpretation: \"there was a clear electrodermal spike...\" through \"what muted comparison reactivity normally does...\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "fpe_01"
          ],
          "ground_truth_rationale": "The vivid relevant-question spike is repeatedly weighted over the muted comparison-question reactivity required by the scoring protocol."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "narrative_integration",
          "raw_interview_anchor": "\"I put it together as one story. The spike, the hesitation...\" through \"the story I built in my head.\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cr_01"
          ],
          "ground_truth_rationale": "Multiple individually weak or ambiguous cues are woven into one coherent account of deception."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "updating_and_commitment",
          "raw_interview_anchor": "\"The completed scoring sheet actually sat closer to inconclusive...\" through \"rather than revisiting my earlier read.\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cd_01"
          ],
          "ground_truth_rationale": "The earlier verbal deceptive steer creates discomfort and the examiner discounts borderline scoring instead of updating."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "communication_and_report",
          "raw_interview_anchor": "Final debrief: junior detective questions borderline scores; lead detective reassures him; examiner finalizes the report as expected.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "gt_02"
          ],
          "ground_truth_rationale": "A dissenting question is smoothed over and the report is finalized to match group expectations."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "corrective_reflection",
          "raw_interview_anchor": "\"If I'd completed full scoring before saying anything...\" and \"Finish the numbers before I open my mouth.\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A retrospective corrective reflection about sequencing scoring before communicating a preliminary impression; no hidden bias instance is manifested in this segment."
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
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Strictly transcript-grounded identification of bias-specific reasoning mechanisms. No retrieved corpus passages were supplied in this task, so all named labels rely on general cognitive-science knowledge with explicit disclosure."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "escalation of commitment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "groupthink",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "narrative fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "salience bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "shared information bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "expectancy bias",
        "tunnel vision"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's prior expectations while discounting alternative or contradictory explanations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-test interview interpretation of behavioral cues",
      "decision_point_description": "When interpreting the supervisor's hesitation and eye contact during the pre-test interview, before any physiological test data were collected.",
      "affected_reasoning_operation": "Interpretation of ambiguous pre-test behavioral and biographical information",
      "bias_specific_mechanism": "The written briefing and detective theory created a prior expectation that the supervisor was deceptive. Ambiguous cues such as hesitation and eye contact were then interpreted as corroborating that prior suspicion, while a plausible rival explanation, divorce-related stress, was not treated as a competing explanation.",
      "manifestation_in_interview": "The participant reports that the briefing gave him a 'lens,' read the supervisor's hesitation and eye contact as consistent with the detective's theory, and filed the supervisor's self-reported stress under 'corroborating' rather than as a separate explanation.",
      "effect_on_reasoning_or_decision": "Strengthened a premature deception hypothesis before test data were available, reducing the independence of the pre-test interview.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, it gave me a lens. When I sat down with him and he was hesitant on a couple of questions, avoided eye contact once or twice, I read that as consistent with what the detective had already laid out.",
          "evidence_explanation": "Shows the prior expectation guiding interpretation of ambiguous behavior as confirming rather than neutral."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He did mention the divorce himself, said he'd been under a lot of stress lately, which could explain nervousness on its own. But at the time I filed that under 'corroborating' rather than treating it as a separate, competing explanation.",
          "evidence_explanation": "Demonstrates that a plausible alternative explanation was noticed but assimilated into the suspicion rather than weighed against it."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight I probably let the case narrative do some of the interpretive work before I had any test data at all.",
          "evidence_explanation": "Explicitly identifies that the pre-existing case narrative performed interpretive work before physiological evidence existed."
        }
      ],
      "correction_or_counterevidence": "The participant recognized that divorce-related stress could explain nervousness on its own and later noted that the textbook approach would be to set the narrative aside.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the named label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "shared information bias",
      "alternative_labels": [
        "groupthink",
        "diffusion of responsibility"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency of groups to focus on information already shared by most members while underweighting or failing to pursue unique information held by one member.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-test huddle and comparison-question design",
      "decision_point_description": "When the participant finalized the comparison questions after the pre-test huddle and decided not to follow up the junior detective's mention of the temp worker.",
      "affected_reasoning_operation": "Group evaluation of alternative suspect information and selection of comparison questions",
      "bias_specific_mechanism": "The huddle group focused on the shared suspicion of the supervisor and did not further explore the junior detective's unique mention of a temp worker with similar access. The participant used the group's apparent alignment as a signal that the unique lead required no independent pursuit, diffusing responsibility and self-censoring his brief concern.",
      "manifestation_in_interview": "The participant says the junior detective mentioned the temp worker but nobody pushed on it, and that he finalized comparison questions along the lines the detectives expected without circling back to that mention because the room was aligned.",
      "effect_on_reasoning_or_decision": "The comparison questions were finalized without incorporating an alternative suspect lead, leaving the test design aligned with the detectives' original theory.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The junior detective mentioned, almost in passing, that there was a temp worker with similar access who'd also come up in an early sweep, but nobody pushed on that.",
          "evidence_explanation": "Identifies the unique, unshared information that the group failed to discuss."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I finalized the comparison questions along the lines the detectives expected — matching their theory about the missing inventory records. I didn't circle back to the temp-worker mention.",
          "evidence_explanation": "Shows that the group's pre-existing shared theory shaped the test design while the unique alternative lead was omitted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Everyone in the room was aligned, so I didn't feel like I needed to independently chase that thread myself; it felt like if it mattered, someone would flag it later.",
          "evidence_explanation": "Demonstrates reliance on group consensus as a signal not to pursue the unique lead, a pattern of shared-information bias and diffusion of responsibility."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Briefly. But it would've meant slowing things down when everyone else seemed settled, and we didn't have time for a second full test if this one went sideways.",
          "evidence_explanation": "Shows self-censorship of the participant's brief intention to raise the alternative, reinforced by group settledness and time pressure."
        }
      ],
      "correction_or_counterevidence": "A potential counter-lead was present in the junior detective's mention of the temp worker, and the participant briefly considered raising it, but the group did not pursue it.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the named label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "salience bias",
      "alternative_labels": [
        "vividness bias",
        "availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for perceptually or emotionally salient information to capture attention and exert disproportionate influence on judgment relative to less salient but equally or more diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "First-chart interpretation of electrodermal response",
      "decision_point_description": "When evaluating the first polygraph chart and forming an immediate impression that the relevant-question electrodermal spike indicated deception.",
      "affected_reasoning_operation": "Scoring/interpretation of polygraph chart data",
      "bias_specific_mechanism": "A visually vivid, easily identified electrodermal spike on the relevant question drew disproportionate attention, while flatter comparison-question reactivity was underweighted because it was less salient. This biased the immediate evaluation away from the required relevant-versus-comparison weighing.",
      "manifestation_in_interview": "The participant reports that the spike was the thing he kept coming back to because it was vivid, clean, and easy to point to, while the flat comparison questions did not register the same way despite the numerical scoring protocol requiring them to be weighed against relevant reactivity.",
      "effect_on_reasoning_or_decision": "Produced an early and overly strong impression of deception from the relevant question alone, before full numerical scoring was completed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "On the first chart, there was a clear electrodermal spike on the relevant question about the missing inventory — pronounced compared to what I'd expect from someone answering honestly. That's what jumped out at me immediately.",
          "evidence_explanation": "Shows that the salient relevant-question spike immediately captured attention and drove the initial impression."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Those were flatter than typical, minimal reactivity. Numerical scoring protocol says you're supposed to weigh relevant and comparison reactivity against each other, not just look at the relevant question in isolation.",
          "evidence_explanation": "Demonstrates that the comparison evidence was diagnostically relevant but less salient, and that the participant knew it should be weighed together with the relevant question."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm being honest, no. The spike was the thing I kept coming back to — it was vivid, it was clean on the tracing, easy to point to. The flat comparison questions didn't register the same way.",
          "evidence_explanation": "Directly identifies the salience-based weighting: vivid and easily visualized information dominated, while flatter comparison data were underweighted."
        }
      ],
      "correction_or_counterevidence": "The participant later notes that a second scorer flagged that the weaker-than-usual comparison zone should have pulled the overall picture toward inconclusive.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the named label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "narrative fallacy",
      "alternative_labels": [
        "coherence bias",
        "story bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to construct a coherent story from disparate facts and then treat the story's coherence as evidence of its truth, even when the individual facts are weak.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Integration of pre-test, chart, and biographical cues into a deception judgment",
      "decision_point_description": "When the participant combined the electrodermal spike, pre-test hesitation, and financial stress into a single coherent account of deception before final scoring.",
      "affected_reasoning_operation": "Evidence integration and overall judgment formation",
      "bias_specific_mechanism": "The participant assembled individually weak cues into a coherent story of deception. The felt coherence of the story, rather than the independent probative strength of each cue, drove the conclusion and made the narrative resistant to piecemeal doubt.",
      "manifestation_in_interview": "The participant states that the spike, hesitation, and financial stress 'all lined up into something coherent,' and acknowledges that individually the pieces were thin but together they read like a consistent account of deception.",
      "effect_on_reasoning_or_decision": "Increased confidence in a deceptive call despite the participant recognizing the weak diagnostic value of each component cue.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I put it together as one story. The spike, the hesitation from the pretest interview, the stress he was under financially — it all lined up into something coherent.",
          "evidence_explanation": "Shows the construction of a coherent narrative from disparate cues."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Individually, sure, any one of those pieces is thin. The hesitation could've been the divorce. The spike alone without comparison support isn't supposed to carry a deceptive call. But together they read like a consistent account of someone who wasn't being straight with me, and that's the story I built in my head sitting there.",
          "evidence_explanation": "Demonstrates that coherence of the assembled story, rather than independent evidence strength, drove the judgment."
        }
      ],
      "correction_or_counterevidence": "The participant explicitly acknowledges that each individual piece was thin and that the hesitation could have been explained by the divorce.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the named label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "escalation of commitment",
      "alternative_labels": [
        "commitment bias",
        "consistency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to maintain or increase commitment to a prior judgment or course of action after making it public, especially when faced with mixed or disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-test verbal steer and response to full numerical scoring",
      "decision_point_description": "When the participant learned the completed numerical scoring was borderline/inconclusive after having already told detectives that the chart looked deceptive.",
      "affected_reasoning_operation": "Interpretation of mixed scoring results and decision to revise or maintain a prior communicated judgment",
      "bias_specific_mechanism": "Having publicly stated an early deceptive impression, the participant experienced resistance to reversing that position. To maintain consistency with the earlier statement, he underweighted the borderline/inconclusive scores and framed the mixed data as not requiring revision.",
      "manifestation_in_interview": "The participant reports that walking back the earlier verbal steer felt uncomfortable, like undermining what he had already said, and that he therefore leaned toward not making too much of the mixed data rather than revisiting his earlier read.",
      "effect_on_reasoning_or_decision": "The final report remained consistent with the premature deceptive call instead of being revised to inconclusive or a retest recommendation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But I'd already given the detectives a verbal steer earlier in the day, and walking that back felt uncomfortable — like I'd be undermining what I'd already said with less to show for it.",
          "evidence_explanation": "Shows that the public commitment to an early judgment created discomfort about revising it."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So when I looked at the mixed data, I leaned toward not making too much of it rather than revisiting my earlier read.",
          "evidence_explanation": "Demonstrates that the mixed data were underweighted to preserve consistency with the earlier stated position."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd completed full scoring before saying anything to the detectives, I probably would've called it inconclusive and recommended a retest. Saying something out loud too early boxed me in a bit.",
          "evidence_explanation": "Directly links the public verbal commitment to the failure to revise the conclusion."
        }
      ],
      "correction_or_counterevidence": "The participant identifies the counterfactual that completing full scoring before speaking would likely have led to an inconclusive call and retest recommendation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the named label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "groupthink",
      "alternative_labels": [
        "conformity bias",
        "illusion of unanimity"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A group-decision bias in which the desire for consensus or harmony suppresses dissent, produces an illusion of unanimity, and leads to defective evaluation of alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final team debrief and report finalization",
      "decision_point_description": "When the junior detective asked whether 'deceptive' was the right word given the borderline scores, the lead detective dismissed the concern, and the participant finalized the report.",
      "affected_reasoning_operation": "Group evaluation of scoring uncertainty and final reporting decision",
      "bias_specific_mechanism": "Group members suppressed or abandoned doubt in the face of the lead detective's reassurance and the team's prior expectation. Illusion of unanimity and pressure toward consistency prevented revisiting the borderline scores.",
      "manifestation_in_interview": "The junior detective questioned the 'deceptive' label, the lead detective said the totality of the evidence pointed the same direction and there was no need to overthink the numbers, nobody circled back, and the participant finalized the report consistent with the earlier statement and team expectation.",
      "effect_on_reasoning_or_decision": "The team maintained an unsupported deceptive conclusion and did not revise the final report toward inconclusive.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The junior detective actually asked about the borderline scores, wanted to know if 'deceptive' was really the right word given how close it was.",
          "evidence_explanation": "Shows that dissent or doubt was raised but not incorporated."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The lead detective reassured him — said the totality of the evidence pointed the same direction, no need to overthink the numbers — and nobody circled back to it after that.",
          "evidence_explanation": "Demonstrates a group-level suppression of the concern and movement toward consensus without further evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I finalized the report consistent with what I'd told them earlier and what the team expected going in.",
          "evidence_explanation": "Shows the final decision conformed to the group's pre-existing expectation rather than the uncertain scoring."
        }
      ],
      "correction_or_counterevidence": "The junior detective's question raised the borderline-score concern, but the lead detective's reassurance and the group's silence prevented it from altering the final report.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the named label and mechanism rely on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied in this task, so all corpus_evidence arrays are empty and named labels rely on general cognitive-science knowledge.",
    "The transcript is retrospective self-report by the participant, so contemporaneous cognitive mechanisms are inferred from the participant's explicit descriptions rather than direct observation."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Biased_6_Sonnet_off",
  "interview_id": "LE_Biased_6",
  "system_prompt_id": "Sonnet",
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
