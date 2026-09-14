You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
**Interviewer:** Thanks for making time for this. As explained, this is a routine debrief for our scene-processing case review — not a disciplinary review. I'll ask you to walk me through a specific call, how you made certain decisions on scene, and what information you had at each point. Nothing you say here goes into the case file. Sound okay?

**Participant:** Sure, that's fine. Happy to walk through it.

**Interviewer:** Can you tell me a bit about your role and how long you've been doing scene work?

**Participant:** I've been a scene examiner for about nine years, six with this department. I handle sudden deaths, burglaries, occasionally violent crime scenes when the primary unit's tied up. This one was a sudden death — elderly male, found at the bottom of a staircase.

**Interviewer:** Let's start with the call itself. What did you know before you arrived?

**Participant:** Dispatch had it as an unresponsive elderly male at the bottom of interior stairs. That's it, pretty bare-bones. When I pulled up, patrol was already inside — they'd been there maybe fifteen minutes. The responding officer met me at the door and gave me a quick rundown: decedent was 82, lived with his daughter and son-in-law, used a walker, and had fallen twice before in the past year according to the family. He said something like, "unsteady on his feet lately, this looks like another one of those." I logged that context, and honestly it lined up with what I was seeing — walker knocked over near the body, body at the base of the stairs. So my opening note in the scene log was "apparent accidental fall, elderly male with mobility history." I started my walkthrough from there.

**Interviewer:** Take me through the walkthrough itself — order of operations, what you looked at first.

**Participant:** Standard sequence: overall scene photos, then work inward toward the body. I did wide shots of the staircase and landing, then focused on the walker — it was tipped over about two feet from him. I got several angles and measurements on that. The stair runner itself didn't show any drag marks or scuffing, which I noted but didn't flag as anything — that's pretty normal, carpet doesn't always take marks well. The walker gave me something concrete to point to, whereas the lack of marks didn't really register as pointing anywhere — there was nothing there to work from, even though I'd have expected at least some trace under a lot of fall scenarios. Then I moved to the body. That's when I noticed a bruise on his upper left arm, faint, not an obvious point of contact with the stairs or railing. I photographed it once, no scale marker, and moved on because I was also thinking about the second scene I had queued that afternoon — a burglary that needed processing before the residents got back.

**Interviewer:** You mentioned the family and a neighbor spoke with you. When did that happen?

**Participant:** Family — his daughter and son-in-law — talked to me maybe forty minutes in, once I'd cleared the immediate area around the body. Daughter told me he'd started a new blood pressure medication a couple weeks back and it made him dizzy, especially getting up from sitting. There was a pill bottle on the nightstand upstairs, I saw it but didn't check the dosage or when he'd last taken it. Then, right as I was wrapping up interior work, the next-door neighbor came over and mentioned she'd heard raised voices from the house two nights before. I asked her a few follow-ups — how sure she was of the night, whether she recognized the voices — because that's the kind of detail you want to pin down before you put weight on it.

**Interviewer:** Let's go back to that first framing decision — adopting the fall narrative from patrol's briefing. What were you weighing there?

**Participant:** I mean, patrol's often right about the general shape of these calls, they see a lot of them too. The alternative would've been to hold off on writing anything down until I'd done a full read of the scene myself. I did think about that, but with a second scene waiting, taking the officer's context as a starting point saved time. It wasn't a conclusion, just an orientation.

**Interviewer:** Did that orientation affect what you looked for first?

**Participant:** Probably some. I went to the walker and the stairs before anything else, because that's where a fall-consistent scene tells its story. I don't think I would've done it drastically differently otherwise — that's just where the informative evidence usually is on a fall call.

**Interviewer:** On the documentation itself — you gave the walker and stairs multiple angles and measurements, but a single unscaled photo for the arm bruise. Walk me through that call.

**Participant:** Time was a factor, honestly. The stairs and walker are the geometry that either supports or complicates a fall, so that's where I put my effort. The bruise — it wasn't clearly inconsistent with anything, it was just unexplained. I didn't have a reason at that moment to treat it as more significant than what I was already documenting.

**Interviewer:** Was there a point where you considered giving it the same treatment — scale marker, multiple angles?

**Participant:** I thought about it briefly. But I was already committed to the stairs documentation being the priority, and I didn't want to lose time second-guessing my own sequence.

**Interviewer:** Let's talk about the family's statement versus the neighbor's. You said you followed up with the neighbor about timing and voice recognition. Did you do anything similar with the daughter's medication account?

**Participant:** Not really, no. I wrote it down as given — new medication, dizziness, that fit with what I was already seeing. I didn't check the bottle's fill date or ask when his last dose was.

**Interviewer:** Why the difference in how you approached those two accounts?

**Participant:** The family knows him day to day. She'd know if he was dizzy. The neighbor's account felt more like something I needed to nail down before I gave it any weight — could've been a TV, could've been a different night. It just needed more pinning down.

**Interviewer:** When you sat down to draft your working narrative, how did the pieces come together?

**Participant:** It came together pretty naturally — dizziness from the medication, reaches for the walker, misses a step, goes down. The bruise fit into that too; arms flail during a fall, contact happens in ways that aren't always obvious from the final position. It read as one coherent sequence.

**Interviewer:** Did you test that explanation for the bruise against the fall trajectory specifically, or was it more that it fit the overall story?

**Participant:** More the latter, I'd say. It wasn't contradicting anything, so it slotted in.

**Interviewer:** Let's move to later in the visit. Your earlier notes had a line about the bruise warranting further review. What happened to that language?

**Participant:** Right, I'd written that mid-visit as a placeholder, just flagging it for myself. Then near the end, the detective called — he'd gotten the family's account secondhand and said it sounded like a straightforward fall, matched the history. By that point I'd already told him over the phone that the scene looked consistent with a fall, so when I sat down to finalize my report, I wrote it up along those lines. The hedge language didn't make it into the final version.

**Interviewer:** Did the detective's call bring any new scene evidence with it, or was it mainly restating the fall account?

**Participant:** No new evidence, no — nothing about the bruise or anything physical had changed since I'd written that note earlier. It was really just him repeating the family's version back to me. But hearing it right then, fresh, kind of pushed the earlier placeholder to the back of my mind when I was actually typing up the report.

**Interviewer:** Was there anything between that mid-visit note and the final report that would have resolved the uncertainty behind it?

**Participant:** Not really resolved, no. It just didn't come up again until I was doing the final body check before the ME investigator arrived, and I noticed the lividity pattern seemed a little off for how he was positioned when found.

**Interviewer:** What did you do with that observation?

**Participant:** It sat a little uneasily with me, honestly, because I'd already told the detective it looked like a fall. Going back and flagging something that cut against that felt like it would undo what I'd just told him. So I chalked it up to possible shifting during discovery — first responders checking for a pulse, that kind of thing — without actually confirming that anyone had moved him. It let me leave the account I'd given intact.

**Interviewer:** If the lividity finding had come up earlier in the visit instead of near the end, do you think you'd have handled it differently?

**Participant:** Maybe. If I'd seen it before I talked to the detective, I probably would've flagged it more prominently rather than folding it into a footnote.

**Interviewer:** What would have changed your handling of the bruise or the neighbor's statement, looking back?

**Participant:** Honestly, if I'd photographed the bruise with a scale marker right away, or pushed the family a bit on the medication timing the same way I pushed the neighbor, I'd have more to work with now. At the time none of it felt urgent enough to slow down for.

**Interviewer:** Last one — if the neighbor had spoken to you before the family did, do you think your notes would look different?

**Participant:** Possibly. I might've gone in asking the family more pointed questions instead of just recording what they offered. Order mattered more than I probably realized in the moment.

**Interviewer:** That's helpful, thank you. I think that covers what I needed.

**Participant:** No problem. Let me know if the ME's findings change anything — I'd want to know either way.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Biased_7",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Crime Scene Investigator (CSI) / Forensic Scene Examiner",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Staircase Fall: Elderly Decedent Scene Processing",
    "scenario_summary_internal": "A CSI is dispatched to a residence where an 82-year-old man is found deceased at the base of an interior staircase. Patrol has already framed the incident as an accidental fall consistent with the decedent's known mobility issues. Over the course of a single scene visit, the CSI documents physical evidence, interviews family and a neighbor, and synthesizes findings into a scene report, while an ambiguous bruise pattern and lividity inconsistency are never fully resolved. The scenario is designed to embed exactly seven bias instances across four decision points without any decision or outcome mechanically proving bias.",
    "occupational_realism": {
      "objective": "Independently and objectively document, interpret, and report physical evidence at a sudden-death scene to support the medical examiner's and detective's determination of manner of death.",
      "setting": "Single-family residence, interior staircase and first-floor landing, mid-afternoon call, single CSI working with one assisting patrol officer, family present nearby, detective reachable by phone but not on scene until later.",
      "constraints": [
        "CSI is queued for a second scene later that day, creating time pressure",
        "Family is present and distressed, limiting length/intrusiveness of on-scene interviews",
        "Medical examiner investigator has not yet arrived to formally assess the body",
        "Detective is handling the case remotely by phone for most of the visit",
        "Scene has already been lightly disturbed by first responders checking for signs of life"
      ],
      "stakeholders": [
        "CSI (protagonist/interviewee)",
        "First-arriving patrol officer",
        "Decedent's adult daughter and son-in-law (family present at scene)",
        "Next-door neighbor",
        "Lead detective (by phone)",
        "Medical examiner investigator (arrives late in timeline)"
      ],
      "technical_terms_to_use": [
        "scene walkthrough",
        "chain of custody",
        "livor mortis / lividity",
        "scale marker",
        "point-of-origin documentation",
        "manner of death",
        "scene reconstruction",
        "corroborating statement"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "cognitive dissonance",
        "contextual bias",
        "feature positive effect",
        "recency effect",
        "coherence-based reasoning",
        "asymmetrical skepticism",
        "heuristic",
        "any explicit bias-naming or psychological jargon"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch note: 'elderly male, found at bottom of stairs, unresponsive'",
          "Patrol officer's verbal briefing on arrival: decedent has fallen twice before, uses a walker, family says he was 'unsteady lately'",
          "Decedent found supine at base of staircase, walker overturned nearby"
        ],
        "new_information_after_decision": [
          "CSI's initial framing note in the scene log: 'apparent accidental fall, elderly male with mobility history'"
        ],
        "alternatives": [
          "Adopt the fall framing conveyed by patrol as the working orientation for the walkthrough",
          "Conduct a neutral, framing-free walkthrough first and form a working hypothesis only after independent observation",
          "Request the patrol officer withhold prior-history commentary until after the CSI's own initial assessment"
        ],
        "intended_action": "CSI accepts and adopts patrol's fall framing before completing an independent walkthrough, orienting subsequent documentation around confirming that frame."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Overturned walker approximately two feet from the body",
          "Staircase runner shows no visible drag or scuff marks",
          "Faint bruising visible on the decedent's upper left arm, not obviously explained by the fall trajectory",
          "Limited time before the CSI must relocate to a second queued scene"
        ],
        "new_information_after_decision": [
          "Multiple detailed photographs and measurements taken of the stairs and walker",
          "Single, non-scaled photograph taken of the arm bruise"
        ],
        "alternatives": [
          "Give the walker/staircase area and the arm bruise equal photographic and measurement rigor",
          "Prioritize documentation of the walker and stairs as the most probative fall-consistent evidence",
          "Flag the absent drag marks as an explicit data point requiring follow-up",
          "Treat the bruise as a priority item warranting scaled photography and measurement before other evidence"
        ],
        "intended_action": "CSI documents the walker/staircase area with high rigor, treats the absence of drag marks as a non-event, and gives the arm bruise only cursory, non-scaled documentation."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Family states decedent was on a new blood-pressure medication that 'made him dizzy'",
          "A pill bottle is visible on the nightstand but dosage/timing is not verified",
          "Neighbor volunteers that she heard 'raised voices' from the house two nights earlier",
          "The bruise and the fall trajectory remain only loosely reconciled"
        ],
        "new_information_after_decision": [
          "Scene notes record the medication explanation as an established fact",
          "Scene notes annotate the neighbor's statement as unconfirmed and note inability to corroborate the timeline",
          "A running narrative is drafted linking dizziness, medication, the walker, and the stairs into a single fall sequence, with the bruise folded in as fall-related"
        ],
        "alternatives": [
          "Apply the same corroboration standard to both the family's and the neighbor's statements",
          "Treat the medication claim as unconfirmed pending verification and pursue the neighbor's statement with equal or lesser scrutiny",
          "Separately test the bruise against the fall trajectory before folding it into the narrative",
          "Note the bruise as an open, unresolved item rather than integrating it into the fall account"
        ],
        "intended_action": "CSI treats the family's account as established without verification while subjecting the neighbor's account to pointed scrutiny, and separately drafts a single fluent fall narrative that absorbs the unexplained bruise without independent testing."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Earlier field notes (mid-visit) contain a hedge: 'bruise pattern warrants further review'",
          "Detective calls near the end of the visit and reiterates that the case 'looks like a straightforward fall'",
          "During a final body check before the ME investigator arrives, lividity pattern appears inconsistent with the body's found position",
          "CSI has already verbally told the detective the scene appears consistent with a fall"
        ],
        "new_information_after_decision": [
          "Final scene report closing summary echoes the detective's fall framing and omits the earlier hedge language",
          "Lividity inconsistency is noted briefly and attributed to 'possible positional shift during discovery' without further testing"
        ],
        "alternatives": [
          "Preserve the earlier hedge language and flag the lividity inconsistency as unresolved in the final report",
          "Contact the ME investigator immediately to jointly evaluate the lividity finding before finalizing the report",
          "Revise the classification pending toxicology and autopsy rather than closing the narrative on scene",
          "Finalize the report consistent with the detective's most recent framing and the already-stated fall conclusion"
        ],
        "intended_action": "CSI's final report adopts the detective's last-stated framing over earlier ambiguous notes, and the lividity inconsistency is minimized/rationalized to remain consistent with the conclusion already communicated to the detective."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you knew before you got out of your vehicle at this scene.",
        "What was your first impression when you arrived, and where did that impression come from?"
      ],
      "timeline_reconstruction": [
        "Take me step by step through the order in which you examined and photographed the scene.",
        "At what point did family members or the neighbor speak with you, and what did each of them say?",
        "When did you first notice the bruise on the arm, and what did you do with that observation at the time?"
      ],
      "decision_point_probes": [
        "Why did you orient your initial walkthrough the way you did? What options did you consider?",
        "How did you decide how much documentation effort to give the walker and stairs versus the bruise? What alternatives did you weigh?",
        "How did you evaluate the family's statement about medication compared to the neighbor's statement about raised voices? What would have made you treat them differently?",
        "Walk me through how the final classification in your report came together. What changed between your mid-visit notes and your closing summary?"
      ],
      "decision_basis": [
        "What specific piece of evidence most influenced each of these decisions?",
        "Was there a moment where two pieces of evidence seemed to point in different directions? How did you resolve that?"
      ],
      "prior_experience": [
        "Have you worked similar elderly-fall scenes before? How did that experience shape what you looked for here?"
      ],
      "time_pressure": [
        "How did having another scene queued that day affect how you allocated your time here?"
      ],
      "uncertainty": [
        "At any point, did you feel unsure about the fall explanation? What did you do with that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the neighbor had spoken to you before the family did, do you think your notes would look different?",
        "If the detective had called earlier in the visit instead of near the end, would your final report have come out the same way?",
        "If the lividity finding had come up first thing at the scene instead of near the end, how might you have handled it?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "CB_01",
        "bias": "Contextual Bias",
        "decision_point": 1,
        "mechanism": "Extraneous prior information from patrol's briefing (fall history, unsteady gait) is adopted as the initial interpretive frame before independent observation of the scene occurs, shaping what is subsequently looked for.",
        "affected_reasoning_operation": "Initial hypothesis formation / perceptual framing of the scene",
        "evidence_available_at_time": [
          "Dispatch note",
          "Patrol officer's verbal history summary",
          "Body position and overturned walker"
        ],
        "required_textual_manifestation": "CSI's opening scene-log entry and description of the walkthrough order explicitly reflect having adopted the 'accidental fall' frame from patrol before independently assessing the scene.",
        "plausible_nonbias_interpretation": "Using an experienced patrol officer's on-scene assessment as an efficient starting point for triage is a reasonable operational heuristic.",
        "strength": "subtle",
        "do_not_make_explicit": ["contextual bias", "priming", "framing effect"]
      },
      {
        "instance_id": "FPE_01",
        "bias": "Feature positive effect",
        "decision_point": 2,
        "mechanism": "A salient present cue (the overturned walker) is heavily weighted in the documentation, while the absence of an expected corroborating cue (drag/scuff marks) is not registered as a comparably weighted data point.",
        "affected_reasoning_operation": "Evidence weighting during on-scene documentation",
        "evidence_available_at_time": [
          "Position of overturned walker",
          "Condition of staircase runner (no visible drag marks)"
        ],
        "required_textual_manifestation": "CSI describes noting and photographing the walker's position in detail, but describes the absence of drag marks only as something 'not really relevant to note' or omits discussing it as a finding in its own right.",
        "plausible_nonbias_interpretation": "Photographing a conspicuous displaced object before assessing subtler surface conditions is standard scene practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["feature positive effect", "absence blindness"]
      },
      {
        "instance_id": "CB2_01",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "decision_point": 2,
        "mechanism": "Documentation effort and evidentiary rigor are applied unevenly: high rigor (multiple angles, measurements) to evidence supporting the fall theory, minimal rigor (single unscaled photo) to a physical finding that could complicate it.",
        "affected_reasoning_operation": "Selective allocation of documentation effort based on fit with the working hypothesis",
        "evidence_available_at_time": [
          "Walker and staircase geometry",
          "Faint bruise on upper left arm"
        ],
        "required_textual_manifestation": "CSI's account of photographing/measuring the stairs and walker in detail contrasts with a described lack of scale marker or close-up treatment of the bruise, framed as a lower priority.",
        "plausible_nonbias_interpretation": "Time constraints require triaging documentation toward the most spatially central evidence first.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "asymmetrical skepticism"]
      },
      {
        "instance_id": "CB2_02",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "decision_point": 3,
        "mechanism": "Two witness statements are held to different evidentiary standards: one supporting the working hypothesis is accepted without corroboration, the other (potentially complicating) is flagged for lack of corroboration and pursued more skeptically.",
        "affected_reasoning_operation": "Testimonial evidence evaluation / differential scrutiny of witness statements",
        "evidence_available_at_time": [
          "Family's statement about medication-induced dizziness",
          "Unverified pill bottle on nightstand",
          "Neighbor's statement about raised voices two nights earlier"
        ],
        "required_textual_manifestation": "CSI describes recording the family's medication explanation as settled while describing follow-up questions, caveats, or corroboration concerns applied specifically to the neighbor's account.",
        "plausible_nonbias_interpretation": "Family members are often better positioned to know a decedent's recent health status than a neighbor.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "asymmetrical skepticism", "differential scrutiny"]
      },
      {
        "instance_id": "COH_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 3,
        "mechanism": "Disparate evidentiary elements are assembled into a single fluent narrative, and the narrative's internal fit is treated as evidence of its accuracy, allowing an unexplained detail to be absorbed rather than independently tested.",
        "affected_reasoning_operation": "Narrative synthesis / causal reconstruction of events",
        "evidence_available_at_time": [
          "Medication claim",
          "Walker position",
          "Staircase geometry",
          "Unexplained arm bruise"
        ],
        "required_textual_manifestation": "CSI narrates a smooth sequential account (dizziness → reaching for walker → missed step → fall) that folds the bruise in as 'likely from the fall' without describing any biomechanical basis for that attribution.",
        "plausible_nonbias_interpretation": "Constructing a plausible sequence of events is a normal and necessary part of scene reconstruction.",
        "strength": "moderate",
        "do_not_make_explicit": ["coherence-based reasoning", "rationalization", "narrative fallacy"]
      },
      {
        "instance_id": "REC_01",
        "bias": "Recency Effects",
        "decision_point": 4,
        "mechanism": "Information received most recently (the detective's closing phone call) is given disproportionate weight relative to earlier, more ambiguous field observations recorded hours before, shaping the final judgment.",
        "affected_reasoning_operation": "Final synthesis and weighting of accumulated evidence over time",
        "evidence_available_at_time": [
          "Earlier hedge note: 'bruise pattern warrants further review'",
          "Detective's late call reiterating the fall theory"
        ],
        "required_textual_manifestation": "CSI's description of the closing report explicitly echoes the detective's just-received phrasing and describes the earlier hedge as having been dropped or softened in the final version.",
        "plausible_nonbias_interpretation": "A detective may have legitimately new information justifying an updated framing.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "primacy-recency", "last information dominance"]
      },
      {
        "instance_id": "CD_01",
        "bias": "Cognitive dissonance",
        "decision_point": 4,
        "mechanism": "Having already verbally committed to the fall conclusion with the detective, the CSI encounters evidence (lividity inconsistency) that conflicts with that commitment; the resulting discomfort is resolved by minimizing/reinterpreting the evidence rather than revisiting the conclusion.",
        "affected_reasoning_operation": "Post-commitment evaluation of disconfirming evidence",
        "evidence_available_at_time": [
          "Lividity pattern observed during final body check",
          "Prior verbal statement already given to the detective"
        ],
        "required_textual_manifestation": "CSI describes noticing the lividity mismatch, a moment of hesitation or discomfort, and then explains it away (e.g., 'positional shift') without describing any attempt to test that explanation, tying the resolution to having already told the detective the scene looked like a fall.",
        "plausible_nonbias_interpretation": "Livor mortis timing can genuinely be affected by minor repositioning of a body during discovery or first-responder checks.",
        "strength": "moderate",
        "do_not_make_explicit": ["cognitive dissonance", "commitment consistency", "post-decisional rationalization"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' with no paired control scenario supplied."
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
      "Confirm exactly 7 total bias instances are embedded: 1 Feature positive effect, 1 Contextual Bias, 1 Coherence-based reasoning/Rationalisation, 1 Cognitive dissonance, 1 Recency Effects, 2 Confirmation Bias and Asymmetrical skepticism.",
      "Confirm no bias term, definition, or psychological label appears in the public interview text.",
      "Confirm exactly 4 decision points, each with at least 2 plausible alternatives.",
      "Confirm CB2_01 and CB2_02 use distinct evidence sources (physical evidence documentation vs. testimonial scrutiny) and distinct decision points.",
      "Confirm FPE_01 and CB2_01, though co-located at decision point 2, address different reasoning operations (salience weighting vs. differential documentation rigor) and different evidence framing.",
      "Confirm total interview length target is 1,350 words within 1,215–1,485 word range without repetitive exposition.",
      "Confirm each instance has a plausible non-bias explanation available in the text.",
      "Confirm no consequence in the timeline mechanically proves or disproves bias (manner-of-death determination remains open/pending ME and toxicology at scenario close)."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Feature positive effect", "occurrences": 1, "mechanism_constraint": "presence of walker overweighted vs absence of drag marks"},
      {"bias": "Contextual Bias", "occurrences": 1, "mechanism_constraint": "patrol briefing adopted as initial frame before independent walkthrough"},
      {"bias": "Coherence-based reasoning or Rationalisation", "occurrences": 1, "mechanism_constraint": "fluent narrative absorbs unexplained bruise without independent testing"},
      {"bias": "Cognitive dissonance", "occurrences": 1, "mechanism_constraint": "post-commitment minimization of lividity inconsistency"},
      {"bias": "Recency Effects", "occurrences": 1, "mechanism_constraint": "detective's late call overrides earlier hedge language"},
      {"bias": "Confirmation Bias and Asymmetrical skepticism", "occurrences": 2, "mechanism_constraint": "two distinct evidence sources: physical-evidence documentation rigor, and testimonial corroboration standard"}
    ],
    "target_bias_names": [
      "Feature positive effect",
      "Contextual Bias",
      "Coherence-based reasoning or Rationalisation",
      "Cognitive dissonance",
      "Recency Effects",
      "Confirmation Bias and Asymmetrical skepticism"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Feature positive effect", "requested_occurrences": 1},
      {"bias": "Contextual Bias", "requested_occurrences": 1},
      {"bias": "Coherence-based reasoning or Rationalisation", "requested_occurrences": 1},
      {"bias": "Cognitive dissonance", "requested_occurrences": 1},
      {"bias": "Recency Effects", "requested_occurrences": 1},
      {"bias": "Confirmation Bias and Asymmetrical skepticism", "requested_occurrences": 2}
    ],
    "planned_instance_ids": [
      {"instance_id": "CB_01", "bias": "Contextual Bias"},
      {"instance_id": "FPE_01", "bias": "Feature positive effect"},
      {"instance_id": "CB2_01", "bias": "Confirmation Bias and Asymmetrical skepticism"},
      {"instance_id": "CB2_02", "bias": "Confirmation Bias and Asymmetrical skepticism"},
      {"instance_id": "COH_01", "bias": "Coherence-based reasoning or Rationalisation"},
      {"instance_id": "REC_01", "bias": "Recency Effects"},
      {"instance_id": "CD_01", "bias": "Cognitive dissonance"}
    ],
    "intended_decision_points": [
      {"instance_id": "CB_01", "bias": "Contextual Bias", "decision_point": 1},
      {"instance_id": "FPE_01", "bias": "Feature positive effect", "decision_point": 2},
      {"instance_id": "CB2_01", "bias": "Confirmation Bias and Asymmetrical skepticism", "decision_point": 2},
      {"instance_id": "CB2_02", "bias": "Confirmation Bias and Asymmetrical skepticism", "decision_point": 3},
      {"instance_id": "COH_01", "bias": "Coherence-based reasoning or Rationalisation", "decision_point": 3},
      {"instance_id": "REC_01", "bias": "Recency Effects", "decision_point": 4},
      {"instance_id": "CD_01", "bias": "Cognitive dissonance", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "CB_01",
        "bias": "Contextual Bias",
        "mechanism": "Adoption of patrol's fall framing as the initial interpretive lens prior to independent observation",
        "affected_reasoning_operation": "Initial hypothesis formation",
        "evidence_source": "Patrol officer's verbal briefing and dispatch note",
        "distinctiveness_requirement": "Must be tied to pre-walkthrough framing, not to selective evidence gathering during documentation"
      },
      {
        "instance_id": "FPE_01",
        "bias": "Feature positive effect",
        "mechanism": "Overweighting of a salient present cue (walker) relative to an absent expected cue (drag marks)",
        "affected_reasoning_operation": "Evidence weighting during documentation",
        "evidence_source": "Walker position vs. staircase runner condition",
        "distinctiveness_requirement": "Must center on presence/absence salience asymmetry, not on differential documentation effort between two present pieces of evidence"
      },
      {
        "instance_id": "CB2_01",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "mechanism": "Unequal documentation rigor applied to physical evidence based on fit with working hypothesis",
        "affected_reasoning_operation": "Selective allocation of documentation effort",
        "evidence_source": "Walker/staircase vs. arm bruise (physical evidence)",
        "distinctiveness_requirement": "Must involve physical-evidence documentation asymmetry at decision point 2, distinct from CB2_02's testimonial asymmetry at decision point 3"
      },
      {
        "instance_id": "CB2_02",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "mechanism": "Unequal corroboration standards applied to two witness statements based on fit with working hypothesis",
        "affected_reasoning_operation": "Testimonial evidence evaluation",
        "evidence_source": "Family's medication statement vs. neighbor's raised-voices statement",
        "distinctiveness_requirement": "Must involve testimonial/witness-statement asymmetry at decision point 3, distinct from CB2_01's physical-evidence asymmetry"
      },
      {
        "instance_id": "COH_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "mechanism": "Narrative fluency substitutes for independent testing of an anomalous detail",
        "affected_reasoning_operation": "Narrative synthesis / causal reconstruction",
        "evidence_source": "Composite of medication claim, walker, stairs, and bruise",
        "distinctiveness_requirement": "Must show the anomalous bruise being folded into a coherent story without independent testing, distinct from mere selective attention (confirmation bias instances)"
      },
      {
        "instance_id": "REC_01",
        "bias": "Recency Effects",
        "mechanism": "Most recently received information (detective's call) dominates final judgment over earlier ambiguous field notes",
        "affected_reasoning_operation": "Final synthesis / temporal weighting of evidence",
        "evidence_source": "Earlier hedge note vs. detective's late call",
        "distinctiveness_requirement": "Must be attributable specifically to temporal recency of the input, not to the content's inherent persuasiveness or to hypothesis-consistency alone"
      },
      {
        "instance_id": "CD_01",
        "bias": "Cognitive dissonance",
        "mechanism": "Discomfort from disconfirming evidence after a prior verbal commitment is resolved by minimizing the evidence rather than revising the conclusion",
        "affected_reasoning_operation": "Post-commitment evaluation of disconfirming evidence",
        "evidence_source": "Lividity pattern vs. prior verbal statement to detective",
        "distinctiveness_requirement": "Must be tied explicitly to the discomfort of a prior stated commitment, distinct from ordinary selective evidence gathering (confirmation bias) or narrative smoothing (coherence-based reasoning)"
      }
    ],
    "intended_strength": [
      {"instance_id": "CB_01", "bias": "Contextual Bias", "strength": "subtle"},
      {"instance_id": "FPE_01", "bias": "Feature positive effect", "strength": "subtle"},
      {"instance_id": "CB2_01", "bias": "Confirmation Bias and Asymmetrical skepticism", "strength": "subtle"},
      {"instance_id": "CB2_02", "bias": "Confirmation Bias and Asymmetrical skepticism", "strength": "subtle"},
      {"instance_id": "COH_01", "bias": "Coherence-based reasoning or Rationalisation", "strength": "moderate"},
      {"instance_id": "REC_01", "bias": "Recency Effects", "strength": "subtle"},
      {"instance_id": "CD_01", "bias": "Cognitive dissonance", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Biased_7",
    "domain_id": "LE",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across distinct decision points where mechanism fit and narrative realism allowed; the two Confirmation Bias/Asymmetrical skepticism occurrences were placed at separate decision points (2 and 3) using distinct evidence sources (physical-evidence documentation rigor vs. testimonial corroboration standard) per exact-occurrence rule 7; Feature positive effect and one Confirmation Bias instance co-located at decision point 2 were differentiated by distinct reasoning operations (salience weighting vs. differential documentation effort) and distinct evidence types.",
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
    "analysis_scope_note": "The transcript was evaluated as the sole factual source for demonstrated bias mechanisms; retrieved corpus passages were used only for terminology validation and mechanistic support."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "contextual bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "contextual bias",
      "alternative_labels": [
        "anchoring bias",
        "expectation bias",
        "premature closure"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for contextual information that is not task-relevant to shape evaluative or evidentiary judgments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial scene framing after patrol briefing",
      "decision_point_description": "Whether to adopt the patrol officer's fall account as the opening scene-log narrative or withhold classification pending independent scene examination.",
      "affected_reasoning_operation": "Hypothesis generation and initial evidence-search prioritization",
      "bias_specific_mechanism": "The patrol officer's pre-walkthrough statement that the death looked like 'another one of those' and the family's reported fall history acted as an early contextual anchor. The participant wrote 'apparent accidental fall' before completing the walkthrough and then directed early attention to fall-consistent locations, especially the staircase and walker.",
      "manifestation_in_interview": "The participant logged the opening note as an apparent accidental fall and started the walkthrough from that frame, later acknowledging the orientation probably affected what he looked at first.",
      "effect_on_reasoning_or_decision": "It narrowed the initial investigative frame and gave fall-consistent evidence early priority.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He said something like, 'unsteady on his feet lately, this looks like another one of those.' I logged that context, and honestly it lined up with what I was seeing — walker knocked over near the body, body at the base of the stairs. So my opening note in the scene log was 'apparent accidental fall, elderly male with mobility history.' I started my walkthrough from there.",
          "evidence_explanation": "This quote shows an early classification based on the patrol narrative before the participant completed a full independent scene assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably some. I went to the walker and the stairs before anything else, because that's where a fall-consistent scene tells its story.",
          "evidence_explanation": "This confirms the prior contextual frame influenced early evidence-search priorities."
        }
      ],
      "correction_or_counterevidence": "The participant also noted the walker and body position were independently consistent with a fall and described the patrol context as 'not a conclusion, just an orientation.' Standard scene work often begins with available briefings. However, the opening note and search sequence still show the contextual anchor shaping the evaluation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved forensic decision-making literature supports the existence of contextual information distorting forensic evaluation.",
      "corpus_evidence": [
        {
          "source_identifier": "Journal of Forensic Sciences - 2021 - Dror - Cognitive bias in forensic pathology decisions.pdf",
          "paper_title": "Cognitive bias in forensic pathology decisions",
          "authors": "Dror",
          "publication_year": "2021",
          "retrieved_passage_or_finding": "Cognitive bias is not about denying the need for certain relevant contextual information, but rather about the need to identify and recognize what contextual information is relevant to the decisionmaking process.",
          "mechanism_supported_by_source": "Contextual information that should not directly drive forensic conclusions can nevertheless bias decision-making when its relevance is not properly managed.",
          "relevance_to_this_occurrence": "The patrol officer's pre-scene causal narrative and fall-history context operated as contextual information that biased the participant's initial scene frame."
        },
        {
          "source_identifier": "Human expert performance in forensic decision making  Seven different sources of bias .pdf",
          "paper_title": "Human expert performance in forensic decision making  Seven different sources of bias",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "evidence conveys irrelevant information that may bias the forensic evaluation. For example, a bite mark present on a young child may reveal the nature of the crime, and voice recording may convey a whole range of irrelevant information that goes beyond what is relevant to the forensic examiner analysing the voice.",
          "mechanism_supported_by_source": "Contextual information can bias forensic evaluation when it exceeds task-relevant evidence.",
          "relevance_to_this_occurrence": "The patrol officer's pre-scene narrative provided case context that went beyond the participant's own initial task-relevant scene observations."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "biased assimilation",
        "selective scrutiny",
        "expectancy-based information search"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and evaluate evidence in ways that favor an existing hypothesis or belief.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of family and neighbor accounts",
      "decision_point_description": "Whether to apply equivalent investigative scrutiny to the daughter's dizziness/medication account and the neighbor's raised-voices account.",
      "affected_reasoning_operation": "Evidence weighting and witness follow-up",
      "bias_specific_mechanism": "The prior fall hypothesis led to asymmetric scrutiny: the daughter's fall-consistent account was accepted with little verification, while the neighbor's fall-inconsistent account was probed for possible weaknesses before being given weight.",
      "manifestation_in_interview": "The participant wrote down the daughter's medication/dizziness account 'as given' and did not check the pill bottle, but he asked the neighbor several follow-up questions to pin down timing and voice recognition.",
      "effect_on_reasoning_or_decision": "Fall-consistent information was accepted more readily, and fall-inconsistent information was held to a higher evidentiary standard.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Daughter told me he'd started a new blood pressure medication a couple weeks back and it made him dizzy, especially getting up from sitting. There was a pill bottle on the nightstand upstairs, I saw it but didn't check the dosage or when he'd last taken it.",
          "evidence_explanation": "Shows low verification of the fall-consistent medical account despite available checks."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The neighbor's account felt more like something I needed to nail down before I gave it any weight — could've been a TV, could've been a different night. It just needed more pinning down.",
          "evidence_explanation": "Shows higher scrutiny of the inconsistent account."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. I wrote it down as given — new medication, dizziness, that fit with what I was already seeing.",
          "evidence_explanation": "Explicitly links acceptance of the daughter's account to consistency with the existing fall narrative."
        }
      ],
      "correction_or_counterevidence": "Family information may legitimately be more reliable than a neighbor's uncertain report, and the neighbor's account was vague. However, the participant did not verify the medication despite easy access and explicitly explained the difference by consistency with what he was already seeing.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit study identifies confirmation bias as a common cognitive bias in professional decision incidents; the present occurrence matches the standard confirmatory-evidence mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation",
          "mechanism_supported_by_source": "Confirmation bias is identified as one of the most common cognitive biases in the analyzed incidents.",
          "relevance_to_this_occurrence": "The participant preferentially accepted hypothesis-consistent information and scrutinized hypothesis-inconsistent information, a classic confirmation-bias pattern."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "coherence-based reasoning",
        "story model bias",
        "belief consistency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to evaluate new or ambiguous information by whether it coheres with an already preferred causal narrative rather than by independent diagnostic value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Drafting the working narrative",
      "decision_point_description": "Whether to test the unexplained arm bruise against the fall trajectory or accept it as part of an overall coherent fall story.",
      "affected_reasoning_operation": "Causal integration and hypothesis evaluation",
      "bias_specific_mechanism": "The participant accepted the bruise as fall-related because it did not contradict the preferred fall narrative, rather than testing it against the specific fall trajectory. This coherence-based acceptance is a confirmatory reasoning pattern.",
      "manifestation_in_interview": "The participant said the pieces 'came together pretty naturally' and admitted he evaluated the bruise as fitting the overall story rather than testing it specifically.",
      "effect_on_reasoning_or_decision": "The unexplained bruise was absorbed into the fall narrative without independent verification, reducing its anomalous weight.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The bruise fit into that too; arms flail during a fall, contact happens in ways that aren't always obvious from the final position. It read as one coherent sequence.",
          "evidence_explanation": "Shows the bruise was accepted because it fit a coherent fall story."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "More the latter, I'd say. It wasn't contradicting anything, so it slotted in.",
          "evidence_explanation": "Directly states the bruise was accepted because it did not contradict the preferred narrative, not because it was independently verified."
        }
      ],
      "correction_or_counterevidence": "Constructing a coherent narrative is a normal expert heuristic; the bruise could plausibly be fall-related. The occurrence is low confidence because coherence-based evaluation is common and not necessarily patently biased, but the participant's own description supports a confirmatory integration mechanism.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit study supports the label of confirmation bias in professional decision-making, though it does not provide a formal coherence-mechanism definition.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation",
          "mechanism_supported_by_source": "Confirmation bias is identified as a common professional cognitive bias.",
          "relevance_to_this_occurrence": "The participant's acceptance of the bruise because it did not contradict the favored fall narrative is a confirmatory evaluation pattern."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "recency effect",
      "alternative_labels": [
        "recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for recent information to be remembered or weighted more heavily than earlier information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final report synthesis after detective phone call",
      "decision_point_description": "Whether to retain the mid-visit hedge about the arm bruise in the final report or omit it after the detective's late restatement of the fall account.",
      "affected_reasoning_operation": "Recall and final report writing",
      "bias_specific_mechanism": "The detective's recent restatement of the fall account, though containing no new scene evidence, was disproportionately accessible and 'pushed the earlier placeholder to the back of my mind,' leading the participant to omit the earlier hedge from the final report.",
      "manifestation_in_interview": "The participant explicitly attributed the omission to the freshness of the detective's phone call rather than to any new resolution of the underlying uncertainty.",
      "effect_on_reasoning_or_decision": "Earlier uncertainty about the bruise was omitted from the final report, altering the documented assessment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "No new evidence, no — nothing about the bruise or anything physical had changed since I'd written that note earlier. It was really just him repeating the family's version back to me. But hearing it right then, fresh, kind of pushed the earlier placeholder to the back of my mind when I was actually typing up the report.",
          "evidence_explanation": "This directly demonstrates a recency-based weighting of the detective's late call over earlier unresolved observations."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The hedge language didn't make it into the final version.",
          "evidence_explanation": "Confirms the behavioral consequence on the final report."
        }
      ],
      "correction_or_counterevidence": "The detective's call may have been treated as a status update, and final reports often synthesize the latest information. But the participant said there was no new information, and the recency of the call specifically displaced his earlier note.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved usability-testing paper provides a direct operational definition of recency effect.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive bias in usability testing",
          "authors": "Natesan et al.",
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly. For example, as participants use a device, they become more familiar...",
          "mechanism_supported_by_source": "Recent events are more easily recalled and can influence subsequent judgments.",
          "relevance_to_this_occurrence": "The participant's late report writing was influenced by the recent detective call even though it added no new evidentiary content."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "plan continuation bias",
      "alternative_labels": [
        "escalation of commitment",
        "commitment bias",
        "consistency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an initial course of action or conclusion despite new cues indicating it may no longer be appropriate.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of lividity pattern during final body check",
      "decision_point_description": "Whether to flag the lividity pattern as inconsistent with the fall account after having already told the detective the scene looked like a fall.",
      "affected_reasoning_operation": "Evidence interpretation and hypothesis updating",
      "bias_specific_mechanism": "Because the participant had already committed publicly to the detective that the scene looked like a fall, the lividity pattern was rationalized as possible body movement during discovery, without confirmation. This preserved the prior account instead of updating it.",
      "manifestation_in_interview": "The participant said the lividity observation sat uneasily, but he did not want to undo what he had told the detective, so he attributed it to first responders without verifying movement.",
      "effect_on_reasoning_or_decision": "A potentially contradictory finding was downgraded to an assumption and not integrated into the reported fall conclusion.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It sat a little uneasily with me, honestly, because I'd already told the detective it looked like a fall. Going back and flagging something that cut against that felt like it would undo what I'd just told him. So I chalked it up to possible shifting during discovery — first responders checking for a pulse, that kind of thing — without actually confirming that anyone had moved him. It let me leave the account I'd given intact.",
          "evidence_explanation": "This quote directly links the rationalization of contradictory evidence to a desire to preserve the prior stated conclusion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd seen it before I talked to the detective, I probably would've flagged it more prominently rather than folding it into a footnote.",
          "evidence_explanation": "This counterfactual supports the causal role of the prior commitment in downgrading the lividity finding."
        }
      ],
      "correction_or_counterevidence": "First responders may indeed have moved the body, so the lividity explanation could be true. However, the participant did not confirm this and explicitly stated that the desire to avoid undoing the account given to the detective drove the interpretation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit study identifies plan continuation bias in professional decision-making; the mechanism here is an investigative conclusion continuation after contradictory cues.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation",
          "mechanism_supported_by_source": "Plan continuation bias is identified as a common cognitive bias in the analyzed incident set.",
          "relevance_to_this_occurrence": "The participant continued the initial fall account despite the lividity cue that was inconsistent with the account, paralleling plan continuation behavior."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": [
        "selective attention",
        "expectancy-based evidence documentation"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Documentation allocation between stairs/walker and arm bruise",
      "supporting_interview_quote": "Time was a factor, honestly. The stairs and walker are the geometry that either supports or complicates a fall, so that's where I put my effort. The bruise — it wasn't clearly inconsistent with anything, it was just unexplained.",
      "plausible_mechanism": "Fall expectation may have biased evidence documentation toward fall-consistent items and away from the unexplained bruise.",
      "why_not_identified": "Time pressure and legitimate evidence triage provide a plausible non-bias explanation; the transcript does not unambiguously show that the fall expectation, rather than resource constraints, caused the differential documentation."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Single participant self-report; cognitive processes are inferred from narrative rather than directly observed.",
    "Retrieved corpus was used for terminology and mechanistic support, but formal diagnostic criteria were not available for every label.",
    "Some episodes could be attributed partly to legitimate professional judgment, time constraints, or normal expert heuristics.",
    "No independent scene findings or outcome data were available to verify the actual impact of the identified biases."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Biased_7_Gemini_on",
  "interview_id": "LE_Biased_7",
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
