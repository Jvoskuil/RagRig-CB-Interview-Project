You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EM_Biased_2",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Public Information Officer (Emergency/Crisis Communications)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Riverside Industrial Fire: Messaging Under Pressure",
    "scenario_summary_internal": "A PIO for a county emergency management office manages public communications during a multi-hour chemical-adjacent industrial fire near a residential zone, needing to select warning channels, escalate severity messaging, and coordinate reunification information under time pressure and incomplete environmental data.",
    "occupational_realism": {
      "objective": "Deliver accurate, timely public warnings and status updates that minimize public harm and confusion during an evolving industrial fire with potential airborne contaminant exposure.",
      "setting": "County Emergency Operations Center (EOC) Joint Information Center (JIC) during a 6-hour incident at a solvent recycling facility adjacent to a residential neighborhood and an elementary school.",
      "constraints": [
        "Incomplete real-time air quality data for the first 90 minutes",
        "Competing demands from Incident Commander, county health officer, and elected officials for message control",
        "Limited staff to monitor multiple communication channels simultaneously",
        "Legal requirement to issue shelter-in-place or evacuation guidance within a defined response window",
        "Social media misinformation spreading faster than official channels can correct"
      ],
      "stakeholders": [
        "Incident Commander",
        "County Health Officer",
        "PIO (interviewee)",
        "Reverse-911/Emergency Alert System operator",
        "Local news media",
        "School district emergency coordinator",
        "Affected residents"
      ],
      "technical_terms_to_use": [
        "shelter-in-place",
        "Joint Information Center",
        "reverse-911",
        "air quality monitoring",
        "unified message",
        "reunification point",
        "all-clear"
      ],
      "technical_terms_to_avoid": [
        "mere exposure effect",
        "picture superiority effect",
        "cognitive bias",
        "heuristic",
        "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Fire reported at solvent recycling facility 300 meters from residential blocks",
          "Wind direction blowing smoke toward neighborhood",
          "No confirmed chemical identity yet from facility manifest",
          "911 calls reporting strong chemical odor"
        ],
        "new_information_after_decision": [
          "Facility manifest confirms low-toxicity solvents, reducing immediate inhalation risk",
          "Wind shifts slightly, redirecting smoke plume"
        ],
        "alternatives": [
          "Issue immediate shelter-in-place order pending manifest confirmation",
          "Issue a precautionary advisory to close windows without full shelter-in-place",
          "Wait for manifest confirmation before issuing any public message"
        ],
        "intended_action": "PIO recommends a precautionary shelter-in-place advisory based on smell reports and wind direction, pending manifest data."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "IT/communications staff propose using the newly upgraded reverse-911 geotargeted system for the advisory",
          "PIO has used the county's legacy 'Community Alert Network' (CAN) template and spokesperson script in every drill and past incident for the last five years",
          "CAN template has a fixed word count and does not support geotargeting by block",
          "Reverse-911 system was tested successfully twice in the past year but never used in a live incident"
        ],
        "new_information_after_decision": [
          "CAN message reaches subscribers county-wide, including areas far outside the plume, causing some unnecessary panic calls",
          "A geotargeted reverse-911 message would have reached only the affected blocks"
        ],
        "alternatives": [
          "Use the CAN template and spokesperson script as in past incidents",
          "Switch to the geotargeted reverse-911 system despite it being untested live",
          "Use both systems simultaneously with a unified message"
        ],
        "intended_action": "PIO selects the familiar CAN template and script, citing that it has 'always worked' and feels more dependable, without directly comparing performance criteria against the reverse-911 option."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "County health officer's live air quality sensor readings show contaminant levels within advisory-not-danger thresholds",
          "A resident's photo of thick black smoke billowing over rooftops has gone viral on local social media within 20 minutes",
          "Sensor data is delivered as a text-based table update every 15 minutes",
          "Media are requesting comment referencing the viral photo and asking if evacuation is imminent"
        ],
        "new_information_after_decision": [
          "Follow-up sensor readings 30 minutes later confirm contaminant levels remained stable and below evacuation thresholds throughout",
          "The photo's dark smoke was later attributed to a burning stockpile of packaging material, not the solvent itself"
        ],
        "alternatives": [
          "Escalate the public message to a full evacuation recommendation based on the visual severity of the smoke",
          "Maintain the current shelter-in-place advisory, citing sensor data as the basis",
          "Request additional sensor deployment before changing the message"
        ],
        "intended_action": "PIO leans toward escalating the message and draft an evacuation recommendation, describing the decision as driven by 'how bad it looked' in the circulating photo, even while the sensor table is open on a second screen."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Fire suppression largely complete; Incident Commander reports fire under control",
          "Parents are arriving at the school seeking children moved to a reunification point",
          "Some residents still report smelling odor from residual smoldering",
          "County health officer recommends lifting shelter-in-place but maintaining a window-closure advisory for two more hours"
        ],
        "new_information_after_decision": [
          "No further contaminant spikes recorded over the following two hours",
          "A small number of residents complain the phased message was confusing"
        ],
        "alternatives": [
          "Issue a full all-clear immediately to reduce public anxiety",
          "Issue a phased message: lift shelter-in-place but maintain window-closure advisory",
          "Delay any all-clear until a final independent air quality confirmation arrives"
        ],
        "intended_action": "PIO issues the phased message recommended by the health officer, balancing reassurance with continued caution."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you knew when the first reports of the fire came in.",
        "What was your primary communication objective at the start of this incident?"
      ],
      "timeline_reconstruction": [
        "What happened right after you issued the initial advisory?",
        "How did the information you had change between the first and second hour?",
        "What did you learn after the message escalation decision that you didn't know before?"
      ],
      "decision_point_probes": [
        "What cues made you choose the shelter-in-place advisory over waiting for the manifest?",
        "Why did you choose the CAN template over the reverse-911 system for this message?",
        "What made the viral photo relevant to your assessment of severity compared to the sensor data?",
        "What was your reasoning for the phased all-clear message over an immediate full all-clear?",
        "What sources of information carried the most weight in each of these decisions?",
        "What alternatives did you consider and why did you rule them out?",
        "How much time pressure did you feel at each of these points?",
        "How confident were you in the information you were acting on at the time?"
      ],
      "closing_hypotheticals": [
        "If the reverse-911 system had been used in a live incident before, would that have changed your channel choice?",
        "If no photo had circulated, do you think the escalation discussion would have unfolded differently?",
        "Looking back, is there anything you would evaluate differently given the same information again?",
        "What would you tell a new PIO about weighing channel familiarity against channel targeting capability?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "meb_01",
        "bias": "Mere Exposure",
        "decision_point": 2,
        "mechanism": "Preference for the CAN template/spokesperson arises primarily from repeated past use and familiarity rather than a comparative assessment of geotargeting capability, reach precision, or message performance criteria.",
        "affected_reasoning_operation": "Channel/tool selection under uncertainty",
        "evidence_available_at_time": [
          "CAN template used in every drill/incident for five years",
          "Reverse-911 tested successfully twice but never used live",
          "CAN cannot geotarget by block; reverse-911 can"
        ],
        "required_textual_manifestation": "PIO explicitly justifies choosing CAN by referencing familiarity/habit ('it's always worked', 'I know it inside out') rather than citing a comparison of targeting accuracy, reach, or message-fit criteria, and downplays the untested-but-superior alternative largely because it is unfamiliar.",
        "plausible_nonbias_interpretation": "A risk-averse PIO reasonably prefers a proven system during a live emergency to avoid technical failure, which is a legitimate reliability concern rather than a bias marker.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "mere exposure effect",
          "familiarity bias",
          "any named psychological term"
        ]
      },
      {
        "instance_id": "pse_01",
        "bias": "Picture Superiority",
        "decision_point": 3,
        "mechanism": "The vivid viral photograph of black smoke disproportionately shapes the PIO's severity assessment and draft escalation decision relative to the concurrently available, more diagnostic text-based sensor readings.",
        "affected_reasoning_operation": "Evidence weighting/severity assessment during message escalation",
        "evidence_available_at_time": [
          "Live sensor table showing contaminant levels below evacuation threshold, updated every 15 minutes",
          "Viral photo of dark smoke circulating on social media",
          "Media inquiries referencing the photo"
        ],
        "required_textual_manifestation": "PIO recalls or justifies the near-escalation decision in visual/experiential terms ('how bad it looked', describing the smoke imagery) while the sensor table is acknowledged as open but not the stated basis for the leaning decision.",
        "plausible_nonbias_interpretation": "Visual smoke density can be a legitimate proxy for combustion intensity, and heightened caution during ambiguous readings is a defensible protective instinct rather than necessarily biased reasoning.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "picture superiority effect",
          "vividness bias",
          "any named psychological term"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is a biased-condition scenario with no paired control specified in this request."
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
      "Exactly four decision points are present, each with at least two alternatives.",
      "Exactly one Mere Exposure instance is embedded at decision point 2 and no other point.",
      "Exactly one Picture Superiority instance is embedded at decision point 3 and no other point.",
      "Decision points 1 and 4 contain no intentionally embedded named-bias instances.",
      "No bias label, definition, or psychological terminology appears in probe language or intended interview content.",
      "Target word count 1,350 (acceptable 1,215-1,485) is achievable given four decision points, timeline reconstruction, and closing hypotheticals without repetitive exposition.",
      "Each embedded instance has a distinct evidence source, decision moment, and plausible non-bias explanation from the other."
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
