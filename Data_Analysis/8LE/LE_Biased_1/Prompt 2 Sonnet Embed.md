You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a training-review case study, your name won't be attached to the write-up, and you can skip any question you're not comfortable with. That work for you?

Participant: Yeah, that's fine. I've done these before for the sergeant's after-action reviews.

Interviewer: Good. Can you tell me your role and roughly how long you've been doing patrol work?

Participant: Patrol officer, field response, going on seven years now. Mostly nights the last three.

Interviewer: Let's start with the incident itself. Walk me through it from the top.

Participant: Sure. This was about 1:40 in the morning, dispatch got an anonymous call about somebody loitering near the strip mall on Route 9—the one with the electronics store, the nail salon, couple other places, all closed. Caller just said the guy was "acting suspicious," no clothing description, nothing about a weapon, nothing specific. That stretch has had a run of break-ins the last couple months, so it's on our radar anyway. I was closest unit, backup was maybe six, seven minutes out. I rolled up, parked down the row a bit instead of pulling right up on him, and just watched for a minute. Saw one guy standing near a parked car outside the electronics store, looking at his phone. Nothing dramatic—no forced entry, no tools, nothing like that.

Interviewer: What made you hold back and observe instead of approaching right away?

Participant: Habit, mostly. If somebody's actually up to something, walking straight in tips them off and you lose the read you'd get from watching them not know you're there. He wasn't doing anything urgent-looking, so there wasn't a reason to rush it.

Interviewer: Okay, so you approach. What happens next?

Participant: I get out, identify myself, ask what he's doing there. He's calm, looks right at me, no hesitation. Says he's a delivery driver, waiting on a store employee to come let him drop a late shipment—one of those after-hours restock things some retailers do. He's got a company badge clipped to his jacket, hands me his license without me even asking twice. Answers are straight, no stumbling. While we're talking I notice there's a noticeable bulge in his jacket pocket, kind of squared off. That's the thing that stuck with me.

Interviewer: What did you do with that observation?

Participant: I asked him to keep his hands visible and I patted him down. Given the hour, the area, the break-in history, and then seeing something in the pocket I couldn't identify—that's enough for me to check. I'm not going to stand there and just hope it's nothing.

Interviewer: Before we get further into that, let's build out the full timeline so I've got the order right. After the pat-down, what happened?

Participant: Pat-down's clean. Bulge turns out to be a rolled invoice clipboard and a phone charger brick. No weapon. I still hadn't confirmed his story independently, though, and backup still wasn't there yet, so I had him stay put while I ran his info and had dispatch try to verify the delivery account. That came back a few minutes later—company does have an active account with that electronics store, late drop-offs are apparently normal for their overnight restock cycle. Store employee showed up shortly after that to actually take the delivery. I cut him loose, wrote up the field contact, noted the pat-down and the reason for it, and that was the end of it.

Interviewer: Let's go back through this decision by decision. First one: choosing to observe from the car before approaching. What alternatives did you consider there?

Participant: I could've walked straight up, or called dispatch back for more detail before doing anything. I didn't see the point in calling back—caller didn't leave much to work with anyway. Watching first just gives me information without giving up the advantage.

Interviewer: Second decision point—the pat-down. What was the single biggest factor driving that?

Participant: Honestly, the bulge. That's what made me act. Everything else about him was pretty unremarkable at that point.

Interviewer: You mentioned he was calm, made eye contact, answered clearly, didn't move away. How did those factor into the decision?

Participant: I mean, I noticed them, sure. But that's not really something I weighed much in the moment. Plenty of people are composed and still turn out to be a problem, so I don't put a lot of stock in somebody acting normal. The pocket's the thing I can't see into, so that's what needs resolving.

Interviewer: If you think about it as two things pointing in opposite directions—the bulge saying there might be something to worry about, him being calm and cooperative saying there might not be—how did those actually balance out for you in the moment?

Participant: They didn't really go on the same scale for me, if I'm honest. The bulge was a fact I could point to—something's there, I don't know what. Him being relaxed about it, answering fine, not flinching—yeah, in hindsight that probably should've counted for something on the other side. Normally in an uncertain stop like that, somebody being that calm and cooperative does ease things off for me a notch, gives me a little more room to slow down. But here, once I clocked the bulge, that easing just didn't happen—the calm didn't really buy him anything against the pocket. It felt like the pocket was the open question and everything else was just... him being fine, which didn't move the needle on it one way or the other.

Interviewer: If he'd been visibly nervous or wouldn't make eye contact, would that have changed what you did?

Participant: Yeah, probably would've moved things along faster, maybe called for backup to get there before I even engaged that closely. Nervousness adds to it.

Interviewer: And if there'd been no bulge at all, same calm demeanor, same story?

Participant: Then there's nothing to pat down for. No visible object, no pat-down. It'd just be a field interview and I'd let him go once the story checked out.

Interviewer: Third decision point—after the pat-down comes back clean, you keep him at the scene rather than releasing him right away. What's the reasoning?

Participant: His story wasn't confirmed yet. ID and badge looked legitimate, but I've had people carry legit-looking credentials for jobs they don't actually have anymore, or badges that are old. Backup still hadn't arrived. Holding him a few extra minutes to get dispatch confirmation felt like the reasonable middle ground—not cutting him loose on an unverified story, but not escalating into an arrest either.

Interviewer: Did you consider walking him up to the store to check in person?

Participant: Thought about it, but the store's locked and dark, nobody's answering that door at 1:45 a.m. Waiting on dispatch and the employee showing up made more sense than dragging him around the parking lot.

Interviewer: Fourth decision point—closing it out. Why release with no citation rather than something like a loitering warning?

Participant: Once dispatch confirmed the account and the employee showed up right after, there wasn't anything left to hang a citation on. He had a legitimate reason to be there and it checked out. Writing him up at that point would've just been punishing him for existing near a business at night, which isn't fair or defensible.

Interviewer: Stepping back—how much did being alone without backup shape the pace of any of this?

Participant: Some. I'm more careful about closing distance and more inclined to check things I can't see, like the pocket, when I don't have a second set of eyes yet. If backup had already been on scene, I might've taken a slower approach to the pat-down, maybe just asked him to show me what's in the pocket instead of doing it myself.

Interviewer: At what point were you least certain about what was actually going on?

Participant: Probably right when I first saw the bulge, before the pat-down. Everything else about him read fine, but that one thing was the piece I genuinely couldn't explain yet, and until I could, I wasn't going to relax.

Interviewer: Has something like that bulge turned out to be a weapon for you before?

Participant: Not personally, no. It's just an unidentified object, and until I know what it is, I treat it as something to resolve—that's really it.

Interviewer: Last question—looking back at how the whole stop played out, is there anything you'd weigh differently next time?

Participant: Maybe I'd ask him to show me the pocket contents himself before going straight to a pat-down, since he was cooperative the whole time. But given what I knew standing there, I don't think I'd change the core call. The pocket was the unresolved piece, and resolving unresolved pieces is the job.

Interviewer: That's helpful, thank you. I think that covers everything I need.

Participant: No problem. Glad it worked out clean for the guy.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Biased_1",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Patrol Officer (Field Response)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Late-Night Welfare Check at the Shuttered Strip Mall",
    "scenario_summary_internal": "A patrol officer responds to a dispatch call about a person loitering near a row of closed businesses after hours. Over the course of the stop, the officer must decide how to approach, whether to pat down, whether to detain, and how to resolve the encounter. The subject turns out to be a delivery driver waiting for a late shift-change contact. One subtle feature-positive-effect instance is embedded at the pat-down decision point: the officer weights the presence of a jacket-pocket bulge heavily toward 'weapon' while failing to give commensurate weight to the equally diagnostic absence of any nervous or evasive behavior, which would logically offset the suspicion if absence-of-cue were weighted the same as presence-of-cue.",
    "occupational_realism": {
      "objective": "Determine whether a person loitering near closed businesses after hours poses a safety or criminal risk, resolve the stop safely and lawfully, and decide on appropriate action (release, further investigation, or arrest).",
      "setting": "Suburban strip mall, closed for the night, dim parking lot lighting, single officer on patrol, backup 6 minutes out",
      "constraints": [
        "Officer is alone until backup arrives",
        "Poor lighting limits visual assessment",
        "Dispatch information is secondhand and vague ('subject acting suspicious')",
        "Department policy requires reasonable suspicion before a pat-down",
        "Time pressure: officer must decide quickly whether the situation is escalating"
      ],
      "stakeholders": [
        "Patrol officer",
        "Subject (delivery driver)",
        "Dispatch/911 caller (anonymous, not present)",
        "Backup officer (arrives late)",
        "Store owner association (indirect, property concerns)"
      ],
      "technical_terms_to_use": [
        "reasonable suspicion",
        "Terry stop",
        "pat-down",
        "field interview",
        "officer safety",
        "totality of the circumstances"
      ],
      "technical_terms_to_avoid": [
        "feature positive effect",
        "cognitive bias",
        "salience bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch call: anonymous caller reported a person 'loitering suspiciously' near closed stores",
          "No description of clothing, weapon, or specific behavior provided",
          "Time is 1:40 a.m., area has had recent break-ins"
        ],
        "new_information_after_decision": [
          "On arrival, officer sees one male standing near a parked car outside a closed electronics store, looking at his phone"
        ],
        "alternatives": [
          "Approach directly and initiate contact immediately",
          "Observe from a distance first to assess behavior before approaching",
          "Call dispatch for more details before acting"
        ],
        "intended_action": "Officer parks at a distance and briefly observes before approaching on foot."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Subject is calm, makes eye contact, answers initial questions coherently",
          "Subject explains he is a delivery driver waiting for a store employee to accept a late shipment",
          "Officer notices a visible bulge in the subject's jacket pocket",
          "Subject shows no shaking, no avoidance of eye contact, no attempt to move away, no change in breathing or speech pattern"
        ],
        "new_information_after_decision": [
          "Pat-down reveals the bulge is a rolled-up invoice clipboard and a phone charger, not a weapon"
        ],
        "alternatives": [
          "Conduct a pat-down based on the pocket bulge alone",
          "Ask the subject to voluntarily show pocket contents without a pat-down",
          "Continue the conversation and reassess after a few more questions"
        ],
        "intended_action": "Officer performs a pat-down, citing the pocket bulge as the primary basis for reasonable suspicion, without weighing the calm, non-evasive demeanor as an offsetting factor."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pat-down is clean; no weapon or contraband found",
          "Subject's ID matches a valid driver's license and a delivery company badge",
          "Backup officer has not yet arrived",
          "Subject's story about waiting for a store contact has not been independently confirmed"
        ],
        "new_information_after_decision": [
          "Dispatch confirms the delivery company has an active late-night account with the electronics store"
        ],
        "alternatives": [
          "Detain the subject further pending dispatch confirmation",
          "Release the subject pending a callback from dispatch",
          "Escort the subject to the store entrance to verify in person"
        ],
        "intended_action": "Officer requests dispatch confirmation while keeping the subject at the scene, without further escalation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch confirms the delivery account and expected late-night drop-off",
          "No further evidence of wrongdoing",
          "Store employee arrives moments later to accept the shipment"
        ],
        "new_information_after_decision": [
          "Encounter concludes without arrest; officer files a field report noting the stop"
        ],
        "alternatives": [
          "Release the subject with no further action",
          "Issue a formal warning or citation for loitering",
          "Request the subject leave the area immediately as a precaution"
        ],
        "intended_action": "Officer releases the subject and documents the stop as resolved."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you knew before you arrived on scene.",
        "What was your initial read of the situation when you pulled up?"
      ],
      "timeline_reconstruction": [
        "What did you notice first when you approached the subject?",
        "What happened between your initial observation and the pat-down decision?",
        "What did dispatch tell you, and when?"
      ],
      "decision_point_probes": [
        "What specifically made you decide to pat him down at that point?",
        "Were there any signs that suggested he wasn't a threat? How did those factor in?",
        "What made you decide to hold him at the scene rather than release him right away?",
        "What led you to close out the stop the way you did?"
      ],
      "information_sources": [
        "How much weight did you give the dispatch call versus what you observed yourself?",
        "Did the subject's explanation change how you viewed the bulge in his pocket?"
      ],
      "goals": [
        "What were you trying to accomplish at each stage of the stop?"
      ],
      "alternatives": [
        "What else could you have done instead of the pat-down?",
        "Could you have verified his story before conducting the pat-down?"
      ],
      "decision_basis": [
        "What single piece of information most drove your pat-down decision?"
      ],
      "prior_experience": [
        "Has a similar bulge or object turned out to be a weapon in past stops?"
      ],
      "time_pressure": [
        "How much did being alone, without backup, affect your pace of decisions?"
      ],
      "uncertainty": [
        "At what point were you most unsure about whether this was a real threat?"
      ],
      "closing_hypotheticals": [
        "If the subject had been visibly nervous instead of calm, would that have changed your decision?",
        "If there had been no bulge but the same calm demeanor, would you still have patted him down?",
        "Looking back, is there anything you'd weigh differently next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "fpe_01",
        "bias": "Feature positive effect",
        "decision_point": 2,
        "mechanism": "Officer's suspicion judgment is driven predominantly by the presence of a salient, discrete cue (visible pocket bulge) while the presence of an equally diagnostic countervailing cue (the absence of nervous, evasive, or agitated behavior) is not given proportional weight in the same judgment, even though a logically calibrated assessment would treat the absence of expected 'guilty' behavior as informative in the opposite direction.",
        "affected_reasoning_operation": "Weighting and integration of positive versus absent cues in a real-time risk assessment",
        "evidence_available_at_time": [
          "Visible bulge in jacket pocket",
          "Subject calm, coherent, cooperative, maintains eye contact",
          "No shaking, no avoidance, no change in breathing or speech",
          "Subject's coherent explanation for presence at the location"
        ],
        "required_textual_manifestation": "In describing the pat-down decision, the officer should explicitly cite the pocket bulge as the deciding factor ('that's what made me act') while, when probed about the calm demeanor, describing it as merely 'not really factoring in' or 'not something I weighed much,' revealing asymmetric weighting between the presence cue and the absence cue.",
        "plausible_nonbias_interpretation": "An unseen object in a pocket is an objectively higher officer-safety risk than calm demeanor is a safety reassurance, so weighting the bulge more heavily could reflect a justified officer-safety heuristic rather than a bias.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Do not name 'feature positive effect' or any bias term",
          "Do not have the officer explicitly reason about 'presence versus absence' in abstract terms",
          "Do not have the officer state the demeanor was irrelevant in a way that reads as a deliberate policy statement rather than a natural recollection"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control scenario supplied."
    },
    "counterfactual_specification": {
      "causal_variable": "presence_vs_absence_weighting_of_pocket_bulge_cue",
      "original_state": "Officer treats the visible pocket bulge as the dominant, near-sufficient basis for the pat-down decision.",
      "counterfactual_state": "Officer weighs the absence of nervous/evasive behavior as equally informative, integrating both presence and absence cues before deciding on the pat-down.",
      "variables_to_hold_constant": [
        "Time of night and lighting conditions",
        "Dispatch call content and vagueness",
        "Subject's actual identity, behavior, and explanation",
        "Absence of backup during the initial stop",
        "Outcome that the bulge is not a weapon"
      ],
      "expected_causal_difference": "If cues were weighted symmetrically, the officer would more likely delay or forgo the pat-down pending further verification, since the calm demeanor would offset the ambiguous bulge.",
      "causal_test_question": "Would the officer have proceeded to a pat-down at that exact moment if the calm demeanor had been given equal evidentiary weight to the pocket bulge?"
    },
    "generation_checks": [
      "Exactly one Feature positive effect instance planned, assigned to decision point 2 only",
      "No bias terminology appears in probe_plan or timeline",
      "Four decision points present, each with at least two alternatives",
      "Word count target 1,350 (range 1,215-1,485) achievable given four decision points and probe set without repetitive exposition",
      "Consequences (clean pat-down, confirmed delivery account) do not mechanically prove or disprove bias presence",
      "No unrequested bias intentionally embedded elsewhere in timeline or probes"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Feature positive effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as asymmetric weighting between a present salient cue (pocket bulge) and an absent but equally diagnostic cue (lack of nervous/evasive behavior) at the pat-down decision."
      }
    ],
    "target_bias_names": ["Feature positive effect"],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Feature positive effect",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "fpe_01",
        "bias": "Feature positive effect"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "fpe_01",
        "bias": "Feature positive effect",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "fpe_01",
        "bias": "Feature positive effect",
        "mechanism": "Presence of a salient cue (pocket bulge) is weighted heavily in the pat-down decision while an equally diagnostic absent cue (no nervous/evasive behavior) is discounted or ignored in the same judgment.",
        "affected_reasoning_operation": "Cue integration and weighting during real-time risk assessment",
        "evidence_source": "Officer's own account of what drove the pat-down decision versus how the calm demeanor was treated when probed",
        "distinctiveness_requirement": "Only one such asymmetric-weighting event may be embedded; it must occur at decision point 2 and must not be repeated or echoed as a second independent instance at decision points 1, 3, or 4."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "fpe_01",
        "bias": "Feature positive effect",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "presence_vs_absence_weighting_of_pocket_bulge_cue",
      "original_state": "Bulge presence dominates the pat-down decision",
      "changed_state": "Absence of nervous behavior is weighted symmetrically with bulge presence",
      "variables_to_hold_constant": [
        "Time, lighting, dispatch call content",
        "Subject identity and true behavior",
        "Backup timing",
        "Final outcome that no weapon is found"
      ]
    },
    "scenario_id": "LE_Biased_1",
    "domain_id": "LE",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point of best mechanism fit (pat-down decision, decision point 2), where a discrete present cue and a logically equivalent absent cue naturally co-occur, consistent with rules 1-4 of the allocation rules.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Time of night and lighting conditions",
      "Dispatch call vagueness",
      "Subject's true identity, behavior, and explanation",
      "Absence of backup at initial stop",
      "Pat-down outcome (no weapon found)"
    ],
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
          "segment_type": "initial_observation_reasoning",
          "raw_interview_anchor": "Watching first just gives me information without giving up the advantage.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Decision point 1 is not the hidden positive instance; the officer chooses distance-based observation from vague dispatch information and recent break-ins."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "pat_down_evidence_weighting_reasoning",
          "raw_interview_anchor": "They didn't really go on the same scale for me, if I'm honest. The bulge was a fact I could point to—something's there, I don't know what. Him being relaxed about it, answering fine, not flinching—yeah, in hindsight that probably should've counted for something on the other side. Normally in an uncertain stop like that, somebody being that calm and cooperative does ease things off for me a notch, gives me a little more room to slow down. But here, once I clocked the bulge, that easing just didn't happen—the calm didn't really buy him anything against the pocket.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "fpe_01"
          ],
          "ground_truth_rationale": "The hidden instance is at decision point 2: the present pocket bulge is weighted heavily while the absent nervous/evasive cues and calm cooperation are discounted in the same pat-down judgment."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "post_pat_down_detention_reasoning",
          "raw_interview_anchor": "Holding him a few extra minutes to get dispatch confirmation felt like the reasonable middle ground—not cutting him loose on an unverified story, but not escalating into an arrest either.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Decision point 3 is outside the single hidden instance; the officer holds briefly for independent verification after a clean pat-down."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "stop_closure_reasoning",
          "raw_interview_anchor": "Once dispatch confirmed the account and the employee showed up right after, there wasn't anything left to hang a citation on.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Decision point 4 is outside the hidden instance; verified delivery information and the employee’s arrival support release and documentation."
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
      "analysis_scope_note": "Analyzed the patrol-stop CTA interview for mechanism-specific cognitive, perceptual, memory, motivational, affective, social-influence, and group-decision biases. Weighted decisions about professional heuristics and officer-safety reasoning conservatively."
    },
    "identified_bias_summary": [
      {
        "bias_label": "Salience bias",
        "identified_occurrence_count": 1
      }
    ],
    "identified_occurrences": [
      {
        "occurrence_id": "obs_001",
        "classification_status": "identified",
        "confidence": "low",
        "bias_label": "Salience bias",
        "alternative_labels": ["Focalism", "Focusing effect", "Perceptual salience bias"],
        "taxonomy_status": "established_label",
        "bias_definition": "The tendency for attention to be disproportionately captured by a salient, novel, or visually prominent cue, leading to overweighting of that cue while less salient but diagnostic information is underweighted.",
        "attributed_to_speaker": "Participant",
        "evidence_speaker": "Participant",
        "decision_episode_label": "Decision to conduct a pat-down during the Route 9 stop",
        "decision_point_description": "After the participant observed a squared-off bulge in the subject's jacket pocket, while the subject was calm, cooperative, and answering questions without hesitation, the participant decided to conduct a pat-down rather than first asking the subject to display the pocket contents or slowing the encounter to weigh the reassuring demeanor.",
        "affected_reasoning_operation": "Weighing and integration of conflicting safety-relevant cues",
        "bias_specific_mechanism": "The visually salient and unresolved bulge captured attention and became the dominant cue; less salient but potentially diagnostic cues—calmness, cooperation, and a consistent story—were acknowledged but did not substantially adjust the threat assessment.",
        "manifestation_in_interview": "The participant described the bulge as the single biggest factor driving the pat-down. When asked to weigh the bulge against the subject's calm cooperation, the participant said the two cues did not go on the same scale and that the calm behavior did not move the needle once the pocket cue was noticed.",
        "effect_on_reasoning_or_decision": "The participant proceeded directly to a pat-down based primarily on the salient bulge. He later reflected that the cooperative demeanor should probably have counted on the other side and that he might ask the subject to show the pocket contents next time.",
        "interview_evidence": [
          {
            "speaker": "Participant",
            "verbatim_quote": "The bulge was a fact I could point to—something's there, I don't know what. Him being relaxed about it, answering fine, not flinching—yeah, in hindsight that probably should've counted for something on the other side.",
            "evidence_explanation": "This shows the participant recognized two categories of information but reports that the reassuring cues were not effectively weighed against the salient bulge during the decision."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "Normally in an uncertain stop like that, somebody being that calm and cooperative does ease things off for me a notch, gives me a little more room to slow down. But here, once I clocked the bulge, that easing just didn't happen—the calm didn't really buy him anything against the pocket.",
            "evidence_explanation": "This directly describes the mechanism: the salient pocket cue overrode the participant's usual integration of cooperative demeanor, preventing the calm behavior from moderating the threat judgment."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "It felt like the pocket was the open question and everything else was just... him being fine, which didn't move the needle on it one way or the other.",
            "evidence_explanation": "This statement shows the disproportionate weighting of the salient unresolved cue while non-salient reassuring information was treated as inert."
          }
        ],
        "correction_or_counterevidence": "The participant also offered a defensible professional rationale: 'Plenty of people are composed and still turn out to be a problem, so I don't put a lot of stock in somebody acting normal.' The stop occurred in a known break-in area, and an unidentified object in a pocket presented an officer-safety issue under uncertainty. These are plausible non-bias explanations, so the occurrence is rated low confidence.",
        "retrieved_corpus_support_available": false,
        "corpus_support_note": "No retrieved passage directly addressed salience bias or focalism. The label is assigned from widely established cognitive-science knowledge rather than retrieved corpus support.",
        "corpus_evidence": []
      }
    ],
    "candidate_biases": [],
    "no_supported_biases_found": false,
    "limitations": [
      "Retrieved corpus did not contain direct support for the identified salience bias mechanism, so the label relies on general knowledge.",
      "The transcript reflects retrospective self-report, which may involve recall or self-presentation effects that cannot be fully separated from the original on-scene judgment.",
      "The officer-safety and professional-heuristic rationale provides a plausible competing explanation, limiting confidence."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Biased_1_Sonnet_on",
  "interview_id": "LE_Biased_1",
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
