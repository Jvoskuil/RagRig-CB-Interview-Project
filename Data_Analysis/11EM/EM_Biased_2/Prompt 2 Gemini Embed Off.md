You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
**Interviewer:** Thanks for making time for this. Just to confirm — this is a voluntary debrief for our after-action learning file, not a performance review. I'll ask you to walk me through the Riverside facility fire from your role as PIO, and I may pause to dig into specific moments. Sound okay?

**Participant:** Sure, happy to do it. It's still pretty fresh — that was a long shift.

**Interviewer:** Good. Before we get into detail, can you give me a quick overview of the incident and what you were trying to accomplish?

**Participant:** Basically, we had a fire break out at the solvent recycling facility on the east side, maybe three hundred meters from a residential block and not far from the elementary school. My job was to get accurate public messaging out fast — warn people if they needed to shelter, keep the media from running ahead of us, and coordinate with the school and health officer so nobody's getting conflicting instructions. Objective was simple to state, hard to execute: protect people without causing panic, and don't say anything we'd have to walk back.

**Interviewer:** Walk me through how it started.

**Participant:** Dispatch got the call a little after 1pm. Within ten minutes we had confirmation of a working fire, heavy smoke, and wind carrying it toward the neighborhood. 911 was lighting up with people reporting a chemical smell. Problem was, we didn't have the facility's chemical manifest yet — that takes time to pull and verify with the fire marshal. So I'm standing in the JIC with a wind direction, an odor complaint pattern, and no confirmed hazard identity. I recommended we go out with a precautionary shelter-in-place advisory rather than wait, because closing windows and staying put costs us very little if it turns out to be nothing, but waiting costs a lot if it's not nothing.

**Interviewer:** What information came in after that first call?

**Participant:** Within about forty minutes the manifest came back — mostly low-toxicity solvents, not the worst-case chemical we'd feared. Wind also shifted slightly, pushing the plume a bit more over open ground. So the initial risk picture actually eased some, which was a relief, but by then we'd already committed to the advisory, which I think was still the right call given what we knew at the time.

**Interviewer:** Let's reconstruct the next couple hours. What happened after that initial advisory went out?

**Participant:** We had about a ninety-minute window where the air monitoring wasn't fully stood up yet, so we were operating a little blind on the contaminant side. Meanwhile the Incident Commander is focused on suppression, the health officer wants to weigh in on any health guidance, and our elected officials are asking me for updates every twenty minutes. Then social media started moving faster than we could — somebody posted early speculation that it was a "chemical explosion," which wasn't accurate, and we had to spend cycles knocking that down instead of just informing.

**Interviewer:** That's around when you had to choose how to actually push out that first advisory — which system to use. Tell me about that decision.

**Participant:** Right, so our comms team had two options. There's the reverse-911 system, which got upgraded last year — it can geotarget down to the block level, so you're only alerting people actually in the plume path. Then there's our Community Alert Network, the CAN system, which is the one we've used in every drill and every real incident for at least five years. I know that script cold, I know how the spokesperson delivery works with it, I know what it sounds like when it goes out.

**Interviewer:** And you went with CAN.

**Participant:** I did. It's just the one that's always worked for us. Somebody on the comms desk mentioned reverse-911 had a couple of successful tests on the books, but I didn't pull the test log or ask the on-call tech what the fallback would be if it hiccupped mid-broadcast — I just had this sense that a system I hadn't personally run live could have bugs, and that was enough to steer me back to what I already knew. I was aware CAN would blast countywide instead of just the plume area, which isn't really a great fit for a localized smoke event, but that didn't weigh very heavily against just going with the familiar option.

**Interviewer:** Did you weigh the two options against each other on any specific criteria — reach accuracy, message length, anything like that?

**Participant:** Not in a formal sense, no. It was more that CAN is the one I trust because I've been using it for years. In hindsight the countywide reach did cause some issues — we got a bunch of calls from people way outside the plume who got scared for no reason — but at the time it felt like the safer choice just because it was the tool I knew.

**Interviewer:** Let's move to the third decision point — the escalation discussion. What was happening then?

**Participant:** About two hours in, the health officer's sensor readings were coming through — text table, updated every fifteen minutes — and contaminant levels were sitting in the advisory range, not danger range. But right around the same time, a resident's photo of this huge black smoke plume went viral locally, just an incredibly dramatic shot, rooftops with this black column behind them. Media started calling, asking if we were about to order an evacuation.

**Interviewer:** How did that shape your thinking?

**Participant:** Honestly, looking at that photo, my gut said this looks bad, we should be moving toward evacuation language. I actually had a draft evacuation recommendation half-written. The sensor table was open right there on my second monitor the whole time, showing levels weren't at that threshold, but the image was what I kept coming back to when I was talking through it with the team — how thick and dark that smoke looked. We ended up holding at shelter-in-place because the health officer pushed back hard on the data, not because I'd fully talked myself out of the escalation.

**Interviewer:** What did you learn afterward?

**Participant:** The follow-up readings thirty minutes later confirmed levels had stayed stable the whole time. And it turned out that black smoke was mostly from a stockpile of packaging material catching fire, not the solvents themselves. So visually it looked like the worst-case scenario, but the actual air data never supported that story.

**Interviewer:** Last decision point — the all-clear.

**Participant:** By hour five, suppression's basically done, Incident Commander says fire's under control. But we've got parents showing up at the school reunification point, some residents still smelling residual smoke, and the health officer recommends lifting shelter-in-place but keeping a window-closure advisory for two more hours as a buffer. I went with that phased approach instead of a full all-clear right away.

**Interviewer:** Any pushback on that?

**Participant:** A handful of residents said the phased message was confusing — they wanted a clean yes-or-no. But given we still had some odor reports, I felt the cautious, staged approach was more defensible than an immediate blanket all-clear, even if it wasn't as tidy a message.

**Interviewer:** If the reverse-911 system had already been used successfully in a live incident before this one, do you think you'd have made a different channel choice?

**Participant:** Probably, yeah. If I'd seen it perform live even once, I think I'd have trusted it enough to use it instead of CAN, especially given the geotargeting benefit.

**Interviewer:** And if that photo had never circulated — does the escalation conversation go differently?

**Participant:** I think it's calmer, honestly. The sensor data alone was pretty steady the whole time. Without that image driving the room's mood, we probably stay at shelter-in-place without ever drafting the evacuation language.

**Interviewer:** Anything you'd evaluate differently with the same information again?

**Participant:** Maybe build in a habit of stating the data source out loud before reacting to whatever's most visually striking in the moment. And for channel choice, I'd want someone to actually pull the reverse-911 test record and talk to the on-call tech before I default to the tool I already know, so familiarity isn't doing all the deciding. Otherwise, given what we knew at each point, I think the calls were reasonable.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EM_Biased_2",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Mere Exposure",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as channel/template preference driven by repeated past use/familiarity rather than comparative performance criteria."
      },
      {
        "bias": "Picture Superiority",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a vivid image disproportionately shaping severity judgment relative to concurrently available textual/numeric sensor data."
      }
    ],
    "target_bias_names": [
      "Mere Exposure",
      "Picture Superiority"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Mere Exposure",
        "requested_occurrences": 1
      },
      {
        "bias": "Picture Superiority",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "meb_01",
        "bias": "Mere Exposure"
      },
      {
        "instance_id": "pse_01",
        "bias": "Picture Superiority"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "meb_01",
        "bias": "Mere Exposure",
        "decision_point": 2
      },
      {
        "instance_id": "pse_01",
        "bias": "Picture Superiority",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "meb_01",
        "bias": "Mere Exposure",
        "mechanism": "Repeated-use familiarity with the CAN template/spokesperson drives channel selection over a comparatively superior but unfamiliar reverse-911 geotargeting option.",
        "affected_reasoning_operation": "Channel/tool selection under uncertainty",
        "evidence_source": "Five years of drill/incident usage history for CAN vs. two successful non-live tests of reverse-911",
        "distinctiveness_requirement": "Must be distinguishable from Picture Superiority by involving a tool/channel choice grounded in repetition history, not visual/imagery salience."
      },
      {
        "instance_id": "pse_01",
        "bias": "Picture Superiority",
        "mechanism": "A vivid viral photograph disproportionately shapes the severity assessment relative to concurrently available textual sensor readings.",
        "affected_reasoning_operation": "Evidence weighting/severity assessment during message escalation",
        "evidence_source": "Viral social media photo of smoke vs. live text-based air quality sensor table",
        "distinctiveness_requirement": "Must be distinguishable from Mere Exposure by involving image-driven salience during a live severity judgment, not repetition-driven familiarity with a tool."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "meb_01",
        "bias": "Mere Exposure",
        "strength": "subtle"
      },
      {
        "instance_id": "pse_01",
        "bias": "Picture Superiority",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Biased_2",
    "domain_id": "EM",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Automatic assignment: each bias assigned to a distinct decision point (2 and 3 respectively) selected for mechanism fit and narrative realism per rules 1-4; no decision point received more than one instance of a given bias since each bias has only one requested occurrence.",
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
          "segment_type": "objective_and_communication_goal",
          "raw_interview_anchor": "Overview of the Riverside fire, PIO responsibilities, and objective to protect people without causing panic or issuing statements that would need to be withdrawn.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Substantive communication objective, but no intentionally embedded bias instance."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "initial_warning_choice",
          "raw_interview_anchor": "With wind toward the neighborhood, odor reports, and no confirmed hazard identity, the participant recommends a precautionary shelter-in-place advisory rather than waiting for the manifest.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is an uncertainty-sensitive precautionary decision; the generation specification assigns no bias instance to decision point 1."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "post_update_reassessment",
          "raw_interview_anchor": "After the manifest and wind update ease the risk picture, the participant still judges the initial advisory correct given the information available at the time.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A hindsight-aware reassessment of the initial precaution; no hidden bias is planned here."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "operational_constraint_and_misinformation_response",
          "raw_interview_anchor": "The participant describes incomplete air monitoring, competing stakeholder demands, and spending response capacity correcting inaccurate chemical-explosion speculation.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Substantive prioritization and coordination context without an embedded target bias."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "channel_selection_rationale",
          "raw_interview_anchor": "The participant compares reverse-911's block-level geotargeting with CAN's five years of drill and incident use, then selects CAN because it is familiar, trusted, and known to work despite its countywide reach.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["meb_01"],
          "ground_truth_rationale": "Decision point 2 contains the single Mere Exposure instance: repeated familiarity with CAN drives selection over a more targeted unfamiliar option."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "severity_assessment_and_escalation",
          "raw_interview_anchor": "While advisory-range sensor readings remain open, the participant says the viral black-smoke photograph looks bad, drafts evacuation language, and keeps returning to the image until the health officer pushes back.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["pse_01"],
          "ground_truth_rationale": "Decision point 3 contains the single Picture Superiority instance: the vivid image disproportionately shapes severity judgment relative to contemporaneous sensor data."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "hindsight_evidence_reconciliation",
          "raw_interview_anchor": "Follow-up readings remain stable and the participant explains that the black smoke came from packaging material, so the visual appearance was not supported by the air data.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is later counterevidence and retrospective reconciliation, not a new hidden occurrence."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "all_clear_action",
          "raw_interview_anchor": "With suppression nearly complete, parents at the reunification point, residual odor reports, and health-officer guidance, the participant chooses a phased message over an immediate full all-clear.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Decision point 4 is intentionally non-biased and follows the health officer's staged recommendation."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "cautious_message_justification",
          "raw_interview_anchor": "The participant defends the staged message as more defensible than a blanket all-clear because odor reports remained, despite residents finding it confusing.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A cautious, evidence-linked communication rationale with no hidden target instance."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "channel_counterfactual",
          "raw_interview_anchor": "The participant says prior successful live use of reverse-911 would probably have increased trust enough to change the channel choice.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a closing counterfactual about the existing channel decision, not a separate manifested occurrence."
        },
        {
          "segment_id": "seg_011",
          "speaker": "Participant",
          "segment_type": "escalation_counterfactual",
          "raw_interview_anchor": "The participant predicts the escalation discussion would have been calmer and would likely have stayed at shelter-in-place without the photo.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This counterfactual supports the already mapped photo episode but does not create a second Picture Superiority occurrence."
        },
        {
          "segment_id": "seg_012",
          "speaker": "Participant",
          "segment_type": "retrospective_lesson",
          "raw_interview_anchor": "The participant recommends stating the data source before reacting to visually striking information and verifying reverse-911 before defaulting to CAN, while judging the original calls reasonable.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Retrospective corrective lessons refer back to the two existing episodes and are not additional hidden occurrences."
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
    "analysis_scope_note": "Conservative mechanism-first analysis of the interview transcript. No RAG corpus context was supplied, so classifications rely on established cognitive-science knowledge rather than retrieved corpus passages."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
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
      "confidence": "moderate",
      "bias_label": "Status quo bias",
      "alternative_labels": ["Default bias", "Status quo preference"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to prefer the current or familiar state of affairs over alternatives, and to overweight the risks or uncertainties of changing from that state even when an alternative may be objectively better suited.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Channel selection for first public advisory",
      "decision_point_description": "Choice between the familiar countywide Community Alert Network system and the newer geotargeted reverse-911 system.",
      "affected_reasoning_operation": "Option evaluation and communication-channel selection under operational time pressure",
      "bias_specific_mechanism": "The participant defaulted to the familiar Community Alert Network tool despite knowing that reverse-911 offered block-level geotargeting and had successful test records. Rather than retrieving the test log or consulting the on-call technology specialist, he treated the unfamiliarity of reverse-911 as grounds for avoiding it, allowing familiarity to dominate the channel decision.",
      "manifestation_in_interview": "The participant explicitly described choosing CAN because it was the familiar system he had used for years, and acknowledged that the countywide reach of CAN was not a good fit for a localized smoke event but that this did not heavily outweigh the familiar option.",
      "effect_on_reasoning_or_decision": "The participant selected the familiar countywide alert system instead of the geotargeted alternative, which led to unnecessary alarm among people outside the plume area.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It's just the one that's always worked for us. Somebody on the comms desk mentioned reverse-911 had a couple of successful tests on the books, but I didn't pull the test log or ask the on-call tech what the fallback would be if it hiccupped mid-broadcast — I just had this sense that a system I hadn't personally run live could have bugs, and that was enough to steer me back to what I already knew.",
          "evidence_explanation": "This shows the participant relying on familiarity and personal lack of live experience with the newer system rather than on objective testing or technical consultation, which is the core status quo mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I was aware CAN would blast countywide instead of just the plume area, which isn't really a great fit for a localized smoke event, but that didn't weigh very heavily against just going with the familiar option.",
          "evidence_explanation": "This demonstrates that a known functional mismatch was discounted in favor of the familiar tool, indicating that familiarity distorted option evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight the countywide reach did cause some issues — we got a bunch of calls from people way outside the plume who got scared for no reason — but at the time it felt like the safer choice just because it was the tool I knew.",
          "evidence_explanation": "The participant links the decision directly to familiarity-based perceived safety rather than to a systematic comparison, reinforcing the status quo explanation."
        }
      ],
      "correction_or_counterevidence": "A plausible non-bias consideration is that using a proven, familiar system under emergency conditions can be a reasonable operational heuristic. However, the participant did not retrieve available test records or compare system capabilities before deciding, and later proposed that someone should pull the reverse-911 test record and consult the on-call tech before defaulting to the known tool. At the moment of decision, the bias was not counterbalanced.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No RAG corpus passages were supplied in the prompt. This classification relies on established cognitive-science definitions of status quo bias rather than retrieved corpus evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Salience bias", "Affect heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood, severity, or importance of an event based on how easily vivid or salient instances come to mind, rather than on more diagnostic statistical or sensor-based information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Escalation discussion about evacuation language",
      "decision_point_description": "Whether to move from shelter-in-place messaging toward evacuation recommendation despite sensor readings remaining in the advisory range.",
      "affected_reasoning_operation": "Risk perception and escalation recommendation formation",
      "bias_specific_mechanism": "A dramatic viral photograph of a large black smoke plume became highly salient and cognitively available, dominating the participant's risk perception and draft escalation language even though concurrent sensor data showed contaminant levels were stable in the advisory range, not the danger range.",
      "manifestation_in_interview": "The participant reported having a draft evacuation recommendation half-written and repeatedly returning to the image of the thick black smoke while discussing escalation with the team, despite the sensor table being open and not supporting evacuation.",
      "effect_on_reasoning_or_decision": "The vivid image pushed the participant's internal reasoning and communications toward evacuation language. The final decision remained shelter-in-place only because the health officer pushed back hard on the data, so the bias materially distorted intermediate interpretation and draft communication before it was externally corrected.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, looking at that photo, my gut said this looks bad, we should be moving toward evacuation language. I actually had a draft evacuation recommendation half-written. The sensor table was open right there on my second monitor the whole time, showing levels weren't at that threshold, but the image was what I kept coming back to when I was talking through it with the team — how thick and dark that smoke looked.",
          "evidence_explanation": "This directly shows a vivid visual image overriding concurrent sensor data in the participant's risk judgment, which is the hallmark availability mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And it turned out that black smoke was mostly from a stockpile of packaging material catching fire, not the solvents themselves. So visually it looked like the worst-case scenario, but the actual air data never supported that story.",
          "evidence_explanation": "This confirms that the salient visual cue was not diagnostically valid for the underlying chemical risk, but it had nonetheless shaped escalation reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without that image driving the room's mood, we probably stay at shelter-in-place without ever drafting the evacuation language.",
          "evidence_explanation": "The counterfactual attribution shows the participant recognizes the photo, not the sensor data, as the driver of the draft escalation, supporting the availability-based distortion."
        }
      ],
      "correction_or_counterevidence": "The health officer pushed back hard on the sensor data, and the team ultimately held at shelter-in-place. The participant later acknowledged that the sensor readings stayed stable and that the dark smoke was from packaging material rather than solvents. However, the biased escalation reasoning had already materially influenced the participant's draft recommendation and team discussion before that correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No RAG corpus passages were supplied in the prompt. This classification relies on established cognitive-science definitions of the availability heuristic rather than retrieved corpus evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No RAG corpus passages were supplied, so corpus_evidence is empty and corpus_support_note relies on established cognitive-science knowledge rather than retrieved literature.",
    "The analysis is based on participant self-report during an after-action debrief, which may include retrospective framing or memory reconstruction.",
    "Confidence ratings are conservative and reflect two specific intermediate reasoning distortions rather than an overall judgment about the participant's professional competence."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Biased_2_Gemini_off",
  "interview_id": "EM_Biased_2",
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
