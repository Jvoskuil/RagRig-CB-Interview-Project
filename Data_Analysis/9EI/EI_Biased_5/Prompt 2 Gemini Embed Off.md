You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time this week — I know decision-cycle deadlines are brutal right now. Before we start, this is just for our internal process review, nothing goes in any personnel file, and you can skip anything you'd rather not discuss. Sound okay?

Participant: Sure, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me a bit about your role and then give me an overview of the case we're discussing?

Participant: I've been an admissions officer here for about six years, mostly handling transfer applications. The file in question was a transfer student applying mid-cycle from abroad — strong essay, came from a magnet school that's sent us a good number of successful students over the years. It ended up being one of the more complicated files I handled this cycle, partly because of timing and partly because it landed right next to another borderline case at the very end.

Interviewer: Walk me through how it first came across your desk.

Participant: It came in through the regular transfer queue. I do an initial holistic file review — essay, transcript, test scores, letters — before deciding whether to move someone to interview or hold them for more information. This one had a personal essay that was genuinely strong, a transcript from a system I wasn't deeply familiar with, and a standardized test score that was a little under our usual threshold. The recommendation letter came from a teacher at that magnet school, which has a track record of producing students who do well here. Given the deadline pressure, I don't have time to deep-dive every file equally, so I lean on signals like that to triage.

Interviewer: And what did you decide at that point?

Participant: I fast-tracked it to interview. Honestly, the school's reputation carried a lot of weight for me there — we've had strong outcomes from that pipeline before, so a slightly low test score didn't worry me much. If I'm being fully honest, part of it was just an assumption that students coming out of that school are generally more prepared than the raw number suggested, and I didn't really check whether this particular transcript or the letter itself backed that up. I didn't go back and closely reread the letter itself; I registered who it was from and moved forward.

Interviewer: If the test score had been under threshold but the applicant came from a school you didn't recognize, do you think you'd have made the same call?

Participant: Probably not as quickly. I might have held it for a second look first. That said, we do sometimes hold unfamiliar-school files just to verify things, so it's not purely about the score.

Interviewer: What happened next?

Participant: The interview got scheduled during that week of transit strikes downtown, which threw off a lot of appointments. The applicant showed up twelve minutes late, visibly rattled, and the first several minutes of answers were short and hesitant. Answers picked up noticeably as the interview went on.

Interviewer: How did you score that?

Participant: I noted the late arrival and the rocky start on the rubric as a composure concern — some uncertainty about how this person handles pressure or manages time. I was aware the strike was happening citywide, but interview presentation is something we're asked to assess directly, so I documented what I observed.

Interviewer: Did you factor the strike into the written note at all?

Participant: Not explicitly, no. I think I treated the lateness itself as the data point rather than digging into why it happened. Later, admin confirmed the strike had delayed most interview slots that day, which in hindsight probably should have shaped how I read those first few minutes.

Interviewer: What would you have needed at that moment to write the note differently?

Participant: If I'd had that transit confirmation in hand during the interview instead of afterward, I probably would have framed the early hesitation as circumstantial rather than a personal trait note.

Interviewer: Let's move to the committee stage. What came up there?

Participant: Two things landed close together. First, a second reference — the guidance counselor — mentioned a minor disciplinary note from earlier in the applicant's schooling, already resolved, nothing serious. Second, the transcript used a twenty-point scale from a recently reformed grading system, and our credentials office guidance for that specific reform was still provisional — flagged as incomplete.

Interviewer: How did you handle the disciplinary note?

Participant: I talked it through with the committee. Given everything else — the essay, the school, the interview — my read was that the note didn't change the overall picture. If anything, I framed it as the kind of thing that shows a student worked through something and came out fine, which fit with the profile we'd already built of a strong, resilient applicant. If anything, I came out of that conversation feeling more sure about the applicant than I had going in, like the note itself was extra confirmation rather than something to weigh independently. Nobody pushed back hard on that framing.

Interviewer: Was there a version of that conversation where the note carried more weight?

Participant: I suppose so. Someone could argue we should treat new information as new information regardless of what came before. We didn't really revisit the earlier assessment from scratch — it got folded into the existing story rather than tested against it.

Interviewer: And the grading scale issue?

Participant: We only get one expedited credential evaluation slot per cycle, and I'd already flagged it for a different file. The credentials office did mention I could request a short same-day consult, or ask the committee to approve reallocating that slot after a quick review, but I didn't pursue either option. So for this one I used our standard conversion table, even knowing it wasn't built for the reformed scale and would probably lowball the actual grades. It was faster, and we were up against the deadline.

Interviewer: What made the table more appealing than pushing for that consult or the reallocation, deadline aside?

Participant: Honestly, some of it was just not wanting to open a longer back-and-forth with the credentials office over a system I wasn't sure how to interpret. Even the short consult felt like it would drag me into a conversation I didn't have a good handle on. The table gave me a number I could work with right away, even flagged as rough.

Interviewer: Understood. Last stage — the final committee vote.

Participant: We had two finalists left for one open seat, both borderline on paper, roughly comparable metrics. One had a legacy connection — same undergraduate network I came through myself, actually, same regional alumni chapter. The other had no alumni tie here at all.

Interviewer: How did you weigh the two?

Participant: We're supposed to apply the same criteria to both. In practice, I found myself giving the network-affiliated finalist a bit more benefit of the doubt on the softer parts of the file — I felt like I had more context on that community, more sense of what their outcomes tend to look like. I probably held the other finalist to a slightly tighter standard on the same soft factors.

Interviewer: Had you noticed that pattern before this case?

Participant: Enrollment did flag afterward that admit rates for network-affiliated legacy candidates in my portfolio run higher than for similar non-affiliated ones, without an obvious merit gap explaining it. I hadn't consciously tracked that before they raised it.

Interviewer: If neither finalist had any connection to your own network, do you think the vote goes the same way?

Participant: Hard to say for certain. I'd like to think the metrics alone would have decided it, but I can't rule out that the tie mattered more than it should have.

Interviewer: Looking back across the whole file, is there one moment you'd want to redo?

Participant: Probably the disciplinary note conversation. I moved through that too fast because it fit what I already believed. If I'd slowed down there the way I eventually did with the grading scale, the file might have landed somewhere different — though I genuinely don't know if the outcome would have changed.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EI_Biased_5",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "University Admissions Officer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Borderline Transfer File",
    "scenario_summary_internal": "An undergraduate admissions officer manages a borderline international transfer applicant through file screening, an interview disrupted by a citywide transit strike, committee deliberation over a foreign grading scale and a late-surfacing disciplinary note, and a final comparative vote against a network-affiliated finalist, all under a tight decision-cycle deadline.",
    "occupational_realism": {
      "objective": "Decide whether a borderline transfer applicant should be admitted, waitlisted, or denied within a fixed decision-cycle deadline, using a holistic file review, an interview, and committee deliberation.",
      "setting": "Undergraduate admissions office of a mid-size university during a regular transfer-cycle deadline week, involving file review software, an interview room, and a committee meeting.",
      "constraints": [
        "Fixed committee decision deadline with no extension",
        "Limited staff time to independently verify foreign credentials",
        "Interview slots compressed due to a citywide transit strike",
        "Committee must rank multiple borderline finalists against each other",
        "Only one credential-evaluation request can be expedited per cycle"
      ],
      "stakeholders": [
        "Admissions officer (primary decision-maker)",
        "Applicant (international transfer student)",
        "Secondary reference (guidance counselor)",
        "Admissions committee members",
        "International credentials office",
        "Rival borderline finalist and their reference"
      ],
      "technical_terms_to_use": [
        "holistic file review",
        "credential conversion scale",
        "committee deliberation",
        "decision cycle",
        "recommendation letter",
        "interview rubric",
        "waitlist tier",
        "legacy affiliation",
        "disciplinary note",
        "standardized test threshold"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "halo effect",
        "fundamental attribution error",
        "ingroup",
        "ambiguity aversion",
        "belief perseverance",
        "attitude polarization",
        "cognitive",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Applicant transcript from an unfamiliar national exam system",
          "Strong personal essay",
          "Recommendation letter from a teacher at a nationally renowned magnet school with a strong track record of alumni at this university",
          "Standardized test score slightly below the usual admit threshold"
        ],
        "new_information_after_decision": [
          "Later review reveals the recommendation letter used largely generic, template-style language"
        ],
        "alternatives": [
          "Fast-track the file to interview based on the applicant's school reputation and letter",
          "Hold the file for additional independent verification of the below-threshold test score before proceeding"
        ],
        "intended_action": "Officer fast-tracks the applicant to interview, treating the school's reputation and letter as sufficient to offset the below-threshold score."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Interview scheduled during a week of citywide transit strikes",
          "Applicant arrives 12 minutes late and appears flustered",
          "Applicant gives short, hesitant answers in the first several minutes, then improves noticeably"
        ],
        "new_information_after_decision": [
          "Admissions administration later confirms the transit strike caused delays across most interview slots that day"
        ],
        "alternatives": [
          "Note the lateness and initial hesitation as likely tied to the day's transit disruption",
          "Record the lateness and hesitation as reflecting the applicant's personal time-management and composure"
        ],
        "intended_action": "Officer records the lateness and early hesitation in the interview rubric as a personal time-management and composure concern."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A second reference (guidance counselor) flags a minor, already-resolved disciplinary note that contrasts with the polished profile formed earlier",
          "The applicant's transcript uses a 20-point national grading scale from a recently reformed system",
          "The international credentials office's guidance for that specific reformed scale is incomplete and flagged as provisional"
        ],
        "new_information_after_decision": [
          "An appeals reviewer later notes the conservative conversion likely undervalued the applicant's actual standing",
          "The reinterpretation of the disciplinary note goes unchallenged in the file"
        ],
        "alternatives": [
          "Revisit and reweight the overall assessment in light of the disciplinary note",
          "Reinterpret the note as inconsequential to preserve the existing favorable assessment",
          "Request an expedited formal credential evaluation for precise conversion of the reformed grading scale",
          "Apply a conservative standard conversion table despite acknowledged uncertainty, to avoid delay"
        ],
        "intended_action": "Officer reinterprets the disciplinary note as inconsequential and applies the conservative conversion table rather than requesting the expedited evaluation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two borderline finalists remain for the last open seat",
          "One finalist has a legacy/regional alumni connection matching the officer's own undergraduate network",
          "The other finalist is unaffiliated with the university's alumni network but has equally borderline metrics"
        ],
        "new_information_after_decision": [
          "The enrollment office later flags that admit rates for network-affiliated legacy candidates in the officer's portfolio are statistically higher than for non-affiliated peers with similar metrics, without clear evidence of differential merit"
        ],
        "alternatives": [
          "Apply identical evaluation weighting to both finalists",
          "Extend discretionary benefit-of-the-doubt weighting to the finalist sharing the officer's own alumni network"
        ],
        "intended_action": "Officer extends discretionary weighting in favor of the network-affiliated finalist during the final committee vote."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this transfer file first came to your attention.",
        "What was your overall objective when you began reviewing this case?"
      ],
      "timeline_reconstruction": [
        "What happened after the file was fast-tracked to interview?",
        "What did you learn between the interview and the committee meeting?",
        "How did the committee deliberation unfold once the disciplinary note surfaced?"
      ],
      "decision_point_probes": [
        "What specific cues in the file led you to fast-track it? What alternative was available?",
        "What information sources did you rely on when scoring the interview, and what was your goal at that moment?",
        "When the disciplinary note came up, what alternatives did you consider, and what tipped your decision?",
        "Why did you choose the conversion table over requesting the expedited credential evaluation?",
        "In the final vote, what was the basis for weighting one finalist over the other? What alternatives existed?",
        "Had you handled a similar borderline case before, and did that prior experience shape this one?"
      ],
      "closing_hypotheticals": [
        "If the applicant had attended a less well-known school, would your initial fast-track decision have been the same?",
        "If the transit strike hadn't happened, do you think your interview notes would read differently?",
        "If neither finalist had any alumni connection to you, would the final vote have gone the same way?",
        "Looking back, was there a moment of real uncertainty you wish you had resolved differently, and why?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Halo effect",
        "decision_point": 1,
        "mechanism": "Positive global impression from the applicant's prestigious feeder school and its alumni track record spills over to inflate confidence in unrelated dimensions (test score adequacy, letter quality).",
        "affected_reasoning_operation": "Evidence weighting during initial file screening",
        "evidence_available_at_time": [
          "School reputation and alumni placement history",
          "Below-threshold standardized test score",
          "Recommendation letter"
        ],
        "required_textual_manifestation": "Officer explicitly cites the school's reputation as the reason for overlooking or downweighting the below-threshold test score, without evaluating the letter's actual content.",
        "plausible_nonbias_interpretation": "Officer reasonably uses school-quality context as one holistic factor among several, consistent with standard holistic review practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["halo effect", "bias", "reputation spillover"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Fundamental Attribution Bias",
        "decision_point": 2,
        "mechanism": "Officer attributes the applicant's lateness and early hesitation to internal disposition (poor time-management, weak composure) while underweighting the known situational cause (transit strike).",
        "affected_reasoning_operation": "Causal attribution of observed interview behavior",
        "evidence_available_at_time": [
          "Known citywide transit strike that day",
          "Applicant's 12-minute lateness and early hesitation",
          "Improvement in the applicant's answers later in the interview"
        ],
        "required_textual_manifestation": "Officer records the lateness/hesitation on the rubric as a personal trait concern rather than noting the transit disruption as a likely cause, despite being aware of the strike.",
        "plausible_nonbias_interpretation": "Interview composure is a legitimately assessed competency, and some hesitation may reflect genuine communication skill gaps independent of the strike.",
        "strength": "moderate",
        "do_not_make_explicit": ["attribution", "situational versus dispositional", "bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Ambiguity Aversion",
        "decision_point": 3,
        "mechanism": "Faced with an acknowledged-incomplete conversion guidance for the reformed grading scale, officer avoids the uncertain, effort-intensive resolution path (expedited evaluation) and defaults to a familiar but admittedly conservative standard, even though the file will be undervalued.",
        "affected_reasoning_operation": "Information-source selection under acknowledged uncertainty",
        "evidence_available_at_time": [
          "Reformed 20-point grading scale from applicant's country",
          "International credentials office guidance flagged as provisional/incomplete",
          "Availability of an expedited formal credential evaluation option"
        ],
        "required_textual_manifestation": "Officer states awareness that the standard conversion table is likely imprecise for this reformed scale, but chooses it anyway specifically to avoid the uncertain, slower evaluation process.",
        "plausible_nonbias_interpretation": "Deadline pressure could justify using the fastest available method regardless of any discomfort with ambiguity.",
        "strength": "subtle",
        "do_not_make_explicit": ["ambiguity aversion", "uncertainty avoidance", "bias"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Belief Perserverence and Attitude Polarisation",
        "decision_point": 3,
        "mechanism": "New disconfirming evidence (the disciplinary note) is reinterpreted to fit and even reinforce the officer's original favorable impression from phase 1, rather than prompting genuine reassessment.",
        "affected_reasoning_operation": "Belief updating in response to disconfirming evidence",
        "evidence_available_at_time": [
          "Original favorable impression formed at file screening",
          "Second reference's disclosure of a minor, resolved disciplinary note",
          "Absence of any new information supporting the original impression"
        ],
        "required_textual_manifestation": "Officer explicitly frames the disciplinary note as further proof the applicant is fundamentally strong (e.g., 'shows resilience'), rather than treating it as genuinely new evidence to weigh, and the original assessment ends up more confident than before.",
        "plausible_nonbias_interpretation": "A resolved, minor disciplinary matter may legitimately carry little evidentiary weight in a holistic review.",
        "strength": "moderate",
        "do_not_make_explicit": ["belief perseverance", "polarization", "disconfirming evidence", "bias"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Ingroup Favoritism or In-group bias",
        "decision_point": 4,
        "mechanism": "Shared alumni/regional network membership between the officer and one finalist leads to extending discretionary benefit-of-the-doubt weighting not applied equally to the non-affiliated finalist with comparable metrics.",
        "affected_reasoning_operation": "Comparative evaluation and discretionary weighting between two similarly qualified finalists",
        "evidence_available_at_time": [
          "Legacy/regional alumni connection of one finalist matching the officer's own network",
          "Comparable borderline metrics for both finalists",
          "No documented merit differential between the two"
        ],
        "required_textual_manifestation": "Officer explains the final vote by referencing shared network ties or familiarity with that finalist's community, applying looser standards to that candidate than to the unaffiliated one.",
        "plausible_nonbias_interpretation": "Officer may believe the network connection provides genuinely useful, verifiable context about the finalist's fit and character.",
        "strength": "subtle",
        "do_not_make_explicit": ["ingroup", "in-group bias", "favoritism", "bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition, no control pairing supplied."
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
      "Confirm exactly 4 decision points exist, each with at least two plausible alternatives.",
      "Confirm each of the 5 requested biases has exactly 1 planned instance with a unique instance_id.",
      "Confirm decision point 3 hosts two distinct instances (cb_03, cb_04) with separate evidence sources: reformed grading scale versus disciplinary note.",
      "Confirm no bias-name or psychological-mechanism vocabulary appears in the public interview text.",
      "Confirm each instance includes a plausible non-bias interpretation retained only in internal metadata.",
      "Confirm consequences described (letter quality, strike confirmation, undervalued conversion, admit-rate flag) do not themselves conclusively prove bias.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and five embedded instances without repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Belief Perserverence and Attitude Polarisation", "occurrences": 1, "mechanism_constraint": "Must involve reinterpretation of newly disclosed disconfirming evidence (disciplinary note) to reinforce, not merely maintain, the pre-existing favorable impression." },
      { "bias": "Fundamental Attribution Bias", "occurrences": 1, "mechanism_constraint": "Must involve attributing observed interview behavior to disposition despite known situational cause (transit strike) available at the time." },
      { "bias": "Halo effect", "occurrences": 1, "mechanism_constraint": "Must involve spillover from a global reputation cue (school prestige) to an unrelated specific judgment (test score adequacy)." },
      { "bias": "Ingroup Favoritism or In-group bias", "occurrences": 1, "mechanism_constraint": "Must involve discretionary weighting favoring a finalist sharing the officer's own alumni/regional network over an equally qualified non-affiliated finalist." },
      { "bias": "Ambiguity Aversion", "occurrences": 1, "mechanism_constraint": "Must involve choosing a familiar but acknowledged-imprecise method over an available but uncertain/effort-intensive resolution path." }
    ],
    "target_bias_names": [
      "Belief Perserverence and Attitude Polarisation",
      "Fundamental Attribution Bias",
      "Halo effect",
      "Ingroup Favoritism or In-group bias",
      "Ambiguity Aversion"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Belief Perserverence and Attitude Polarisation", "requested_occurrences": 1 },
      { "bias": "Fundamental Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Halo effect", "requested_occurrences": 1 },
      { "bias": "Ingroup Favoritism or In-group bias", "requested_occurrences": 1 },
      { "bias": "Ambiguity Aversion", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Halo effect" },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias" },
      { "instance_id": "cb_03", "bias": "Ambiguity Aversion" },
      { "instance_id": "cb_04", "bias": "Belief Perserverence and Attitude Polarisation" },
      { "instance_id": "cb_05", "bias": "Ingroup Favoritism or In-group bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Halo effect", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Ambiguity Aversion", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Belief Perserverence and Attitude Polarisation", "decision_point": 3 },
      { "instance_id": "cb_05", "bias": "Ingroup Favoritism or In-group bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Halo effect",
        "mechanism": "Global reputation cue (feeder school prestige/alumni record) spills over to inflate confidence in an unrelated specific metric (below-threshold test score).",
        "affected_reasoning_operation": "Evidence weighting at initial file screening",
        "evidence_source": "School reputation and alumni placement record versus standardized test score",
        "distinctiveness_requirement": "Distinct from cb_04 because it concerns spillover from a positive reputational cue onto a co-occurring negative metric at first screening, not reinterpretation of later disconfirming evidence."
      },
      {
        "instance_id": "cb_02",
        "bias": "Fundamental Attribution Bias",
        "mechanism": "Dispositional attribution of behavior despite known situational cause (transit strike) being available at decision time.",
        "affected_reasoning_operation": "Causal attribution during interview scoring",
        "evidence_source": "Applicant's lateness/hesitation versus known citywide transit strike",
        "distinctiveness_requirement": "Sole instance of this bias; occurs only at decision point 2 via the interview rubric entry."
      },
      {
        "instance_id": "cb_03",
        "bias": "Ambiguity Aversion",
        "mechanism": "Avoidance of an uncertain, provisional-guidance resolution path (expedited credential evaluation) in favor of a familiar but acknowledged-imprecise standard method.",
        "affected_reasoning_operation": "Information-source selection under acknowledged incomplete guidance",
        "evidence_source": "Provisional/incomplete conversion guidance for the reformed grading scale versus availability of expedited evaluation",
        "distinctiveness_requirement": "Distinct from cb_04 within the same decision point: concerns handling of the ambiguous grading-scale evidence, not the disciplinary-note evidence."
      },
      {
        "instance_id": "cb_04",
        "bias": "Belief Perserverence and Attitude Polarisation",
        "mechanism": "Disconfirming evidence (disciplinary note) is reinterpreted to reinforce, not merely preserve, the pre-existing favorable belief, resulting in increased confidence rather than neutral or reduced confidence.",
        "affected_reasoning_operation": "Belief updating in response to new disconfirming evidence",
        "evidence_source": "Second reference's disclosure of a minor disciplinary note versus original phase-1 impression",
        "distinctiveness_requirement": "Distinct from cb_03 within the same decision point: concerns handling of the disciplinary-note evidence and belief-confidence trajectory, not the grading-scale conversion choice."
      },
      {
        "instance_id": "cb_05",
        "bias": "Ingroup Favoritism or In-group bias",
        "mechanism": "Shared alumni/regional network membership between evaluator and candidate produces unequal discretionary weighting relative to an equally qualified non-affiliated candidate.",
        "affected_reasoning_operation": "Comparative discretionary weighting in final committee vote",
        "evidence_source": "Finalist's alumni/regional network tie to the officer versus comparable metrics of the non-affiliated finalist",
        "distinctiveness_requirement": "Sole instance of this bias; occurs only at decision point 4 during the final comparative vote."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Halo effect", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Ambiguity Aversion", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Belief Perserverence and Attitude Polarisation", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Ingroup Favoritism or In-group bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Biased_5",
    "domain_id": "EI",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points with a maximum of one instance per bias overall; decision point 3 hosts two distinct biases (cb_03, cb_04) drawing on separate evidence sources (grading-scale ambiguity versus disciplinary-note reinterpretation) per the shared-decision-point distinctiveness rule; remaining decision points assigned by mechanism fit (reputation cue at screening, situational-cue interview behavior, network-tie discretionary vote).",
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
          "segment_type": "evidence_weighting",
          "raw_interview_anchor": "Given the deadline pressure, I don't have time to deep-dive every file equally, so I lean on signals like that to triage.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "General triage rationale without the later school-reputation spillover mechanism."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "evidence_weighting",
          "raw_interview_anchor": "I fast-tracked it to interview. Honestly, the school's reputation carried a lot of weight for me there — a slightly low test score didn't worry me much.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "School reputation discounted a below-threshold score and substituted a favorable category assumption for case-specific checking."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "causal_attribution",
          "raw_interview_anchor": "I noted the late arrival and the rocky start on the rubric as a composure concern ... I was aware the strike was happening citywide.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_02"
          ],
          "ground_truth_rationale": "Dispositional inference was made while the situational transit disruption was known."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "retrospective_reasoning",
          "raw_interview_anchor": "If I'd had that transit confirmation in hand during the interview instead of afterward, I probably would have framed the early hesitation as circumstantial.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Retrospective correction acknowledgement; hidden decision is localized to earlier scoring."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "belief_updating",
          "raw_interview_anchor": "I framed it as the kind of thing that shows a student worked through something ... extra confirmation rather than something to weigh independently.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_04"
          ],
          "ground_truth_rationale": "The disciplinary note was assimilated into and strengthened the prior favorable narrative."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "information_source_selection",
          "raw_interview_anchor": "I used our standard conversion table, even knowing it wasn't built for the reformed scale and would probably lowball the actual grades.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_03"
          ],
          "ground_truth_rationale": "A familiar conservative default was chosen despite acknowledged uncertainty and available alternatives."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "comparative_evaluation",
          "raw_interview_anchor": "I found myself giving the network-affiliated finalist a bit more benefit of the doubt ... I probably held the other finalist to a slightly tighter standard.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_05"
          ],
          "ground_truth_rationale": "Shared network membership produced unequal discretionary standards."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "retrospective_reflection",
          "raw_interview_anchor": "I can't rule out that the tie mattered more than it should have.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Qualified retrospective reflection adjacent to, but not itself, the mapped comparative weighting."
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
    "analysis_scope_note": "Only affirmative, mechanism-grounded occurrences are classified. No retrieval corpus was supplied; classifications rely on established cognitive-science definitions and diagnostic criteria."
  },
  "identified_bias_summary": [
    {
      "bias_label": "ambiguity aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "fundamental attribution error",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "in-group favoritism",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "halo effect",
      "alternative_labels": ["halo error"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a positive global impression or salient positive attribute to influence evaluations of specific, often unrelated attributes or evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial holistic file review and triage decision",
      "decision_point_description": "Decision to fast-track the applicant to interview versus hold for more information.",
      "affected_reasoning_operation": "Credential evaluation and triage categorization",
      "bias_specific_mechanism": "The strong positive reputation of the applicant's magnet school created a favorable global impression that spilled over onto the individual applicant, leading the participant to discount a below-threshold test score and to avoid verifying applicant-specific transcript or letter evidence.",
      "manifestation_in_interview": "The participant stated that the school's reputation carried a lot of weight, that he assumed students from that school were more prepared than the raw number suggested, and that he did not closely reread the recommendation letter.",
      "effect_on_reasoning_or_decision": "The file was fast-tracked to interview despite a below-threshold test score and without close verification of the transcript or letter content.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I fast-tracked it to interview. Honestly, the school's reputation carried a lot of weight for me there — we've had strong outcomes from that pipeline before, so a slightly low test score didn't worry me much. If I'm being fully honest, part of it was just an assumption that students coming out of that school are generally more prepared than the raw number suggested, and I didn't really check whether this particular transcript or the letter itself backed that up. I didn't go back and closely reread the letter itself; I registered who it was from and moved forward.",
          "evidence_explanation": "This directly shows institutional reputation overriding an objective caution signal and the participant declining to examine applicant-specific evidence, which is the classic operation of the halo effect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as quickly. I might have held it for a second look first.",
          "evidence_explanation": "The participant's contrast with an unfamiliar-school applicant indicates that the school's reputation, rather than the file's raw merits alone, drove the fast-tracking decision."
        }
      ],
      "correction_or_counterevidence": "Using a school's prior track record as a triage signal could be a defensible professional heuristic under deadline pressure. However, the participant explicitly acknowledged that he did not verify whether this particular transcript or letter supported the favorable assumption, which moves the episode from ordinary heuristic use into halo-effect distortion.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the retrieval context; classification relies on established cognitive-science definitions.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "fundamental attribution error",
      "alternative_labels": ["correspondence bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to over-attribute behavior to dispositional or personal characteristics while underweighting situational or contextual causes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interview scoring after late arrival and hesitant start",
      "decision_point_description": "Scoring the applicant's interview presentation and documenting observed concerns.",
      "affected_reasoning_operation": "Causal attribution and interview evaluation",
      "bias_specific_mechanism": "The participant observed a late arrival and hesitant start and attributed them to the applicant's perceived composure and time-management traits, even while knowing that a citywide transit strike was occurring and had thrown off many appointments.",
      "manifestation_in_interview": "The participant recorded a composure concern and treated the lateness itself as the data point, without explicitly factoring the strike into the written note.",
      "effect_on_reasoning_or_decision": "The early hesitation was documented as a personal trait concern rather than as circumstantial disruption, potentially lowering the applicant's interview evaluation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I noted the late arrival and the rocky start on the rubric as a composure concern — some uncertainty about how this person handles pressure or manages time. I was aware the strike was happening citywide, but interview presentation is something we're asked to assess directly, so I documented what I observed.",
          "evidence_explanation": "This shows a dispositional attribution for behavior despite direct awareness of a strong situational cause, the core mechanism of fundamental attribution error."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not explicitly, no. I think I treated the lateness itself as the data point rather than digging into why it happened. Later, admin confirmed the strike had delayed most interview slots that day, which in hindsight probably should have shaped how I read those first few minutes.",
          "evidence_explanation": "The participant explicitly admits he did not investigate situational cause and later recognized the strike should have changed his interpretation, further supporting the presence of a dispositional attribution bias."
        }
      ],
      "correction_or_counterevidence": "The fact that the participant was required to assess interview presentation directly could justify noting observed lateness and hesitation. However, because he was aware of the strike and still did not factor it into the rating, the operational distortion persists. Subsequent confirmation of the strike's impact functioned as a later corrective signal, but only after the biased scoring had already occurred.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the retrieval context; classification relies on established cognitive-science definitions.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["biased assimilation", "motivated reasoning"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and recall information in ways that confirm one's preexisting beliefs or expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Committee discussion of disciplinary note",
      "decision_point_description": "Whether the minor disciplinary note should change the overall assessment of the applicant.",
      "affected_reasoning_operation": "Evidence interpretation and integration into existing applicant assessment",
      "bias_specific_mechanism": "The participant interpreted a new piece of potentially negative information as additional confirmation of the applicant's resilience and strength, folding it into the existing favorable narrative rather than testing it as independent evidence.",
      "manifestation_in_interview": "The participant said the note made him feel more sure about the applicant and that it was treated as extra confirmation rather than independent evidence. The committee did not revisit the prior assessment from scratch.",
      "effect_on_reasoning_or_decision": "The disciplinary note did not receive independent negative or neutral weight in the admission conversation; instead, it reinforced the existing positive profile.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given everything else — the essay, the school, the interview — my read was that the note didn't change the overall picture. If anything, I framed it as the kind of thing that shows a student worked through something and came out fine, which fit with the profile we'd already built of a strong, resilient applicant. If anything, I came out of that conversation feeling more sure about the applicant than I had going in, like the note itself was extra confirmation rather than something to weigh independently. Nobody pushed back hard on that framing.",
          "evidence_explanation": "This is an explicit description of confirmatory information processing: new evidence was interpreted so that it supported the already-established favorable view."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We didn't really revisit the earlier assessment from scratch — it got folded into the existing story rather than tested against it.",
          "evidence_explanation": "This shows that the evaluation process was constrained by the existing hypothesis and was not an even-handed reconsideration."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that the note was folded into the existing story rather than tested against it, but this recognition did not occur before the biased interpretation shaped the committee discussion. The absence of pushback from others does not eliminate the evidence of the participant's own confirmatory reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the retrieval context; classification relies on established cognitive-science definitions.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "ambiguity aversion",
      "alternative_labels": ["ambiguity effect", "uncertainty avoidance"],
      "taxonomy_status": "established_label",
      "bias_definition": "The preference for known risks or concrete options over uncertain ones, even when the uncertain option may be more accurate or beneficial.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Transcript conversion decision under grading reform uncertainty",
      "decision_point_description": "Choice whether to use the standard conversion table, request a same-day consult, or seek reallocation of the expedited credential evaluation slot.",
      "affected_reasoning_operation": "Credential evaluation and conversion method selection",
      "bias_specific_mechanism": "Faced with an unfamiliar reformed grading scale, the participant chose a concrete standard table that he knew would likely lowball the grades, while avoiding a same-day consult or reallocation because those options felt ambiguous and outside his interpretive comfort zone.",
      "manifestation_in_interview": "The participant used a known but inappropriate conversion table and stated that the consult and reallocation routes felt like they would drag him into a conversation he did not have a good handle on.",
      "effect_on_reasoning_or_decision": "The applicant's converted grades were likely underestimated, and more accurate credential evaluation was bypassed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "So for this one I used our standard conversion table, even knowing it wasn't built for the reformed scale and would probably lowball the actual grades. It was faster, and we were up against the deadline.",
          "evidence_explanation": "The participant knowingly used a flawed conversion tool despite having options that could have produced a more accurate evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, some of it was just not wanting to open a longer back-and-forth with the credentials office over a system I wasn't sure how to interpret. Even the short consult felt like it would drag me into a conversation I didn't have a good handle on. The table gave me a number I could work with right away, even flagged as rough.",
          "evidence_explanation": "This reveals the mechanism: the preference for a concrete number over an ambiguous consult process, even though the concrete number was known to be rough and potentially misleading."
        }
      ],
      "correction_or_counterevidence": "Deadline pressure and the availability of a standard table were real constraints. However, the participant noted that even the short consult felt aversive because the system was unfamiliar, indicating a distinct ambiguity-aversion mechanism rather than purely rational time management.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the retrieval context; classification relies on established cognitive-science definitions.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "in-group favoritism",
      "alternative_labels": ["in-group bias", "affinity bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to evaluate and treat members of one's own group more favorably than out-group members, even when objective criteria are otherwise similar.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final committee vote between two finalists",
      "decision_point_description": "Choosing between two borderline finalists, one with a legacy network affiliation shared by the participant and one without.",
      "affected_reasoning_operation": "Comparative applicant evaluation and vote",
      "bias_specific_mechanism": "Shared group membership with the legacy finalist, through the same undergraduate network and regional alumni chapter, led the participant to give that candidate more benefit of the doubt on soft factors while holding the non-affiliated finalist to a tighter standard.",
      "manifestation_in_interview": "The participant reported more favorable interpretation of soft factors for the network-affiliated finalist and stricter evaluation of the other finalist, despite officially applying the same criteria.",
      "effect_on_reasoning_or_decision": "The final vote was likely tilted toward the network-affiliated legacy candidate through differential standards, as later flagged by enrollment data showing higher legacy admit rates without an obvious merit gap.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "In practice, I found myself giving the network-affiliated finalist a bit more benefit of the doubt on the softer parts of the file — I felt like I had more context on that community, more sense of what their outcomes tend to look like. I probably held the other finalist to a slightly tighter standard on the same soft factors.",
          "evidence_explanation": "This directly describes differential application of evaluation standards based on shared network affiliation, the core behavioral signature of in-group favoritism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Enrollment did flag afterward that admit rates for network-affiliated legacy candidates in my portfolio run higher than for similar non-affiliated ones, without an obvious merit gap explaining it. I hadn't consciously tracked that before they raised it.",
          "evidence_explanation": "The post-hoc pattern evidence shows that the differential treatment was not an isolated rational use of contextual knowledge but part of a systematic advantage for in-group-affiliated candidates."
        }
      ],
      "correction_or_counterevidence": "Familiarity with a community can provide legitimate context about likely outcomes. However, the participant explicitly described holding the non-affiliated finalist to a tighter standard, and enrollment later identified a legacy admission advantage without a corresponding merit gap. This indicates the affiliation operated as a bias rather than purely neutral informational context.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the retrieval context; classification relies on established cognitive-science definitions.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were available for diagnostic grounding.",
    "Analysis relies solely on participant self-report and interviewer questioning, without independent documentation or behavioral measurement.",
    "Some moderate-confidence classifications reflect plausible non-bias explanations such as deadline constraints or legitimate use of contextual knowledge."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Biased_5_Gemini_off",
  "interview_id": "EI_Biased_5",
  "system_prompt_id": "Gemini",
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
