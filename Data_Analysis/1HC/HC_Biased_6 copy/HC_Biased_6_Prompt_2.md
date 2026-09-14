You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HC_Biased_6",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Clinical Research Coordinator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Enrollment Pressure and Adverse Event Judgment in a Multi-Site Oncology Trial",
    "scenario_summary_internal": "A Clinical Research Coordinator (CRC) at a mid-size academic oncology site is midway through a Phase III trial with a lagging enrollment target. Over roughly three weeks she must screen a borderline-eligible patient, decide whether to keep pushing an underperforming recruitment pathway given prior effort already spent, assess causality on a new adverse event report, and decide how to escalate a protocol deviation to the sponsor. The incident is nonroutine because it combines clinical judgment, operational resource allocation, and safety reporting under time pressure and incomplete guidance from the protocol and sponsor communications.",
    "occupational_realism": {
      "objective": "Keep the trial site compliant with protocol and reporting requirements while meeting the site's enrollment target for the current quarter.",
      "setting": "Academic medical center oncology clinical trials unit, multi-site Phase III trial, weeks 9-12 of a 16-week enrollment window.",
      "constraints": [
        "Quarterly enrollment target set by the sponsor with financial implications for site continuation",
        "Ambiguous inclusion/exclusion criteria language in an amended protocol version",
        "Limited coordinator hours split across three concurrent trials",
        "24-72 hour adverse event reporting window",
        "Dependence on PI availability for eligibility sign-off and causality assessment"
      ],
      "stakeholders": [
        "Clinical Research Coordinator (primary actor)",
        "Principal Investigator",
        "Sponsor Clinical Trial Manager",
        "Study Monitor (CRA)",
        "Enrolled/screened patient",
        "Coordinators at peer trial sites (indirect, via network calls/newsletters)"
      ],
      "technical_terms_to_use": [
        "inclusion/exclusion criteria",
        "screening visit",
        "protocol amendment",
        "adverse event (AE) causality assessment",
        "case report form (CRF)",
        "protocol deviation",
        "enrollment target",
        "site initiation visit",
        "sponsor monitor",
        "eligibility waiver request"
      ],
      "technical_terms_to_avoid": [
        "ambiguity bias",
        "sunk cost",
        "representativeness heuristic",
        "bandwagon effect",
        "framing effect",
        "recency bias",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "A prospective patient meets most but not all criteria under the amended protocol language, which uses the phrase 'adequate organ function' without a specific lab threshold table",
          "The PI is traveling and only reachable by short message",
          "The site is 4 patients behind its quarterly enrollment target"
        ],
        "new_information_after_decision": [
          "The sponsor later issues a clarifying memo defining 'adequate organ function' with explicit lab cutoffs that the patient's labs do not clearly meet",
          "The monitor flags the enrollment for a query at the next visit"
        ],
        "alternatives": [
          "Enroll the patient using the coordinator's own interpretation of the ambiguous language, favoring inclusion",
          "Hold the screening and escalate the ambiguous wording to the PI or sponsor medical monitor before deciding",
          "Decline enrollment outright pending clarified language"
        ],
        "intended_action": "Coordinator resolves the ambiguous eligibility language on her own, interpreting it in the direction that allows enrollment, without documenting the ambiguity or escalating for clarification."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The referral pathway the coordinator built with a partner clinic (outreach materials, staff training, scheduling templates) has produced only one enrollee in six weeks despite roughly 40 hours of setup work",
          "A newsletter from the trial's coordinator network reports that two peer sites are 'ahead of pace' using a similar outreach approach",
          "An alternative pathway (chart review of existing oncology patients) has not yet been tried and could plausibly yield faster results"
        ],
        "new_information_after_decision": [
          "Two more weeks pass with only one additional low-quality referral from the partner-clinic pathway",
          "A colleague mentions the chart-review approach worked quickly at another site once someone finally tried it"
        ],
        "alternatives": [
          "Continue investing coordinator time into the partner-clinic pathway because of the effort already put into building it",
          "Redirect available hours to the untried chart-review pathway",
          "Split time evenly between both pathways for a trial period"
        ],
        "intended_action": "Coordinator continues committing the bulk of her remaining hours to the partner-clinic pathway, citing the work already invested in setting it up, and additionally decides to keep pace with it partly because peer sites reported success with a similar approach, rather than reassessing pathway performance on its own recent yield."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A newly enrolled patient reports a grade 2 rash and mild fatigue nine days after the first infusion",
          "The presentation superficially resembles a 'classic' hypersensitivity pattern described in the investigator brochure's illustrative case vignette",
          "The patient also has a recent unrelated antibiotic course and a documented history of seasonal allergies, both plausible alternative causes",
          "A different peer-site AE report attributing a similar rash to the study drug was discussed on a coordinator call the previous day"
        ],
        "new_information_after_decision": [
          "Follow-up allergy testing later suggests the antibiotic as a more likely trigger",
          "The PI's independent causality read differs from the coordinator's initial draft assessment"
        ],
        "alternatives": [
          "Draft the causality assessment giving weight to the antibiotic and allergy history as competing explanations before defaulting to the vignette pattern",
          "Draft the causality assessment treating the case as a probable match to the 'classic' vignette pattern because the symptoms resemble it, and lean toward the peer-site report discussed the day before as confirming evidence",
          "Request additional diagnostic workup before drafting any causality opinion"
        ],
        "intended_action": "Coordinator drafts the causality assessment leaning toward 'related to study drug,' judging primarily by how closely the case resembles the textbook vignette pattern, and gives the peer-site case discussed the previous day disproportionate weight relative to the antibiotic and allergy history already in the chart."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The eligibility ambiguity from Phase 1 has now surfaced as a monitor query that must be escalated",
          "The coordinator must summarize the situation for the sponsor's clinical trial manager in a written note",
          "The PI has suggested two possible ways to describe the issue: as a 'minor administrative eligibility clarification' or as a 'protocol deviation requiring corrective action'",
          "Both descriptions are factually defensible given the ambiguous protocol wording"
        ],
        "new_information_after_decision": [
          "The sponsor's response and required corrective action plan differ substantially depending on which description was used",
          "The monitor's subsequent audit note treats the framing chosen by the coordinator as the operative characterization of the event"
        ],
        "alternatives": [
          "Report the event using the 'minor administrative clarification' framing suggested first",
          "Report the event using the 'protocol deviation' framing and treat both descriptions as equally worth stating with full detail",
          "Ask the sponsor medical monitor to independently characterize the event before choosing wording"
        ],
        "intended_action": "Coordinator adopts the milder 'minor administrative eligibility clarification' framing in her written note largely because it was presented first and sounds less consequential, shaping how she and the sponsor subsequently treat the required follow-up."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this trial and your role in it looked like during that quarter?",
        "What was the overall goal you were trying to protect during this period?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from the screening visit to the sponsor note, in order.",
        "What did you know at each point, and what changed afterward?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you right before you decided on eligibility?",
        "What alternatives did you consider for the referral-pathway hours, and why did you weight them the way you did?",
        "Walk me through how you arrived at your causality read for the adverse event.",
        "What made you choose that particular wording for the sponsor note?",
        "What sources or people influenced each of these calls?",
        "How much time pressure were you under at each step?",
        "How confident were you at the time, and what would have changed that confidence?"
      ],
      "closing_hypotheticals": [
        "If the sponsor's clarifying memo had arrived a day earlier, would the screening decision have gone differently?",
        "If you had not heard about the peer-site pathway update or the peer-site AE report, do you think your calls would have been the same?",
        "If the PI had suggested the 'protocol deviation' wording first instead, what do you think would have happened?",
        "Looking back, is there a point where you'd want more explicit guidance before deciding?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "hc6_01",
        "bias": "Ambiguity Bias",
        "decision_point": 1,
        "mechanism": "Coordinator resolves genuinely ambiguous protocol language unilaterally in the direction that favors a preferred/easier outcome (enrollment) rather than treating the ambiguity as something to escalate or document.",
        "affected_reasoning_operation": "Interpretation of underspecified eligibility criteria",
        "evidence_available_at_time": [
          "Amended protocol text lacking explicit lab thresholds",
          "PI unavailable for real-time consult",
          "Enrollment shortfall against quarterly target"
        ],
        "required_textual_manifestation": "Coordinator explicitly states she 'read it the way that let the patient in' or equivalent, without describing any escalation or documentation of the ambiguity before enrolling.",
        "plausible_nonbias_interpretation": "A reasonable coordinator might make a good-faith clinical judgment call under time pressure when a PI is unreachable, which is defensible practice, not necessarily biased.",
        "strength": "subtle",
        "do_not_make_explicit": ["ambiguity bias", "ambiguous", "biased interpretation"]
      },
      {
        "instance_id": "hc6_02",
        "bias": "Sunk Costs Bias",
        "decision_point": 2,
        "mechanism": "Continued allocation of scarce coordinator time to the partner-clinic pathway is justified by reference to prior hours already invested in building it, rather than by its recent yield or comparison to the untried alternative.",
        "affected_reasoning_operation": "Resource-reallocation decision under a sunk prior investment",
        "evidence_available_at_time": [
          "~40 hours already spent building the partner-clinic pathway",
          "Only one enrollee produced in six weeks",
          "An untried chart-review pathway with plausible faster yield"
        ],
        "required_textual_manifestation": "Coordinator's stated reason for continuing includes the amount of past effort/setup work already put in, presented as a reason to keep going rather than as a sunk cost.",
        "plausible_nonbias_interpretation": "Switching pathways has real transition costs, and giving a new pathway a fair trial period before abandoning it is a legitimate operational judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["sunk cost", "wasted effort", "escalation of commitment"]
      },
      {
        "instance_id": "hc6_03",
        "bias": "Bandwagon effect",
        "decision_point": 2,
        "mechanism": "Decision to keep pace with the partner-clinic pathway is additionally influenced by hearing that peer sites using a similar approach report being 'ahead of pace,' rather than by the coordinator's own site-level yield data.",
        "affected_reasoning_operation": "Weighting of peer/network social proof versus own-site performance data in a continue/redirect decision",
        "evidence_available_at_time": [
          "Coordinator-network newsletter describing peer sites as ahead of pace with a similar approach",
          "Own site's yield data showing only one enrollee",
          "No verification that peer sites' approach or patient population matches the coordinator's own site"
        ],
        "required_textual_manifestation": "Coordinator cites what other sites are reportedly doing/achieving as a distinct reason (separate from the prior-effort reason) for staying the course, without checking whether the comparison is apt.",
        "plausible_nonbias_interpretation": "Learning from peer-site practices is a normal and often valuable part of coordinator networking and trial operations.",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon", "social proof", "peer pressure", "everyone else is doing it"]
      },
      {
        "instance_id": "hc6_04",
        "bias": "Representativeness",
        "decision_point": 3,
        "mechanism": "Causality judgment is driven by how closely the AE's surface features match a 'classic' textbook vignette pattern, rather than by weighing base-rate-relevant competing explanations (recent antibiotic course, allergy history) already present in the chart.",
        "affected_reasoning_operation": "Diagnostic/causal categorization of an adverse event",
        "evidence_available_at_time": [
          "Grade 2 rash and fatigue nine days post-infusion",
          "Investigator brochure's illustrative 'classic' hypersensitivity vignette",
          "Documented recent antibiotic course and seasonal allergy history in the same chart"
        ],
        "required_textual_manifestation": "Coordinator explains her causality lean primarily in terms of how much the case 'looked like' the described pattern, with the competing chart evidence mentioned only in passing or after the fact.",
        "plausible_nonbias_interpretation": "Pattern-matching to known drug-reaction presentations is a legitimate part of clinical training and can be a valid starting hypothesis.",
        "strength": "subtle",
        "do_not_make_explicit": ["representativeness", "stereotype", "base rate", "typical case"]
      },
      {
        "instance_id": "hc6_05",
        "bias": "Recency Bias",
        "decision_point": 3,
        "mechanism": "The peer-site AE report discussed on a call the day before the coordinator's own assessment is given disproportionate evidentiary weight relative to the patient's own chart history, purely because it was the most recently encountered similar case.",
        "affected_reasoning_operation": "Integration of external comparator evidence into an individual causality judgment",
        "evidence_available_at_time": [
          "Peer-site AE report discussed on a coordinator call the day before",
          "Patient's own antibiotic and allergy history already documented for days",
          "No structural similarity assessment performed between the peer case and this patient's case"
        ],
        "required_textual_manifestation": "Coordinator refers to the just-discussed peer case as a reason that tipped her toward the drug-related read, distinct from and additional to the pattern-matching reasoning in hc6_04, tied specifically to its recency rather than its relevance.",
        "plausible_nonbias_interpretation": "Recent, similar external safety signals can be legitimately relevant to a causality assessment and are a normal part of pharmacovigilance reasoning.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency bias", "most recent", "just heard about"]
      },
      {
        "instance_id": "hc6_06",
        "bias": "Framing Effect",
        "decision_point": 4,
        "mechanism": "Choice of wording for the sponsor note ('minor administrative clarification' vs. 'protocol deviation') is driven by which description was presented first and sounds less consequential, even though both are factually defensible and materially change downstream sponsor action.",
        "affected_reasoning_operation": "Selection of description/label for a factually ambiguous compliance event",
        "evidence_available_at_time": [
          "Two PI-suggested, equally defensible ways to describe the same underlying event",
          "Awareness that the sponsor's response differs depending on which description is used",
          "The milder description was suggested first"
        ],
        "required_textual_manifestation": "Coordinator states she went with the wording that 'sounded less serious' or was suggested first, rather than choosing based on an independent assessment of the underlying facts.",
        "plausible_nonbias_interpretation": "Coordinators often defer to a PI's suggested language as a matter of role hierarchy and workflow efficiency.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "framing", "loss framing", "gain framing"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, no paired control generated in this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "not_applicable_condition_is_biased",
      "original_state": "not_applicable",
      "counterfactual_state": "not_applicable",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "not_applicable",
      "causal_test_question": "not_applicable"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and numbered 1-4",
      "Confirm exactly 6 total bias instances embedded, one per manifest entry",
      "Confirm no two instances at the same decision point share a bias label",
      "Confirm hc6_02 and hc6_03 at decision point 2 use distinct evidence sources (prior effort vs. peer-network report)",
      "Confirm hc6_04 and hc6_05 at decision point 3 use distinct evidence sources (vignette pattern-match vs. recency of peer report)",
      "Confirm no bias name, definition, or psychological label appears in the public interview text",
      "Confirm each decision point includes at least two plausible alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm final interview draft falls between 1,215 and 1,485 words",
      "Confirm consequences described do not conclusively prove or disprove bias presence"
    ]
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
