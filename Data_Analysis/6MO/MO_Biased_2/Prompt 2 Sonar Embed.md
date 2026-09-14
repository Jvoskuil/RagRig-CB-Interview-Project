You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. Just to confirm, this is a routine debrief about a watchkeeping incident during your last strait transit — nothing punitive, and it's fine to speak candidly about how you worked through it. Can you tell me your role and roughly how long you've been standing bridge watches?

Participant: Sure. I'm second officer, been sailing as OOW for about four years now, mostly on container ships this size. That night I had the 0000 to 0400 watch on our own, with one AB as lookout. We were transiting the strait, which is always busy — crossing traffic, fishing boats, the usual squally weather this time of year.

Interviewer: Can you walk me through what happened that night, from the start of the watch?

Participant: When I took over, ARPA already had five targets acquired, nothing alarming — CPAs all comfortable. VHF chatter mentioned fishing activity ahead, and the forecast had squalls coming through, visibility dropping under a mile at times. Passage plan had us holding course into the next TSS leg, so early on it was just normal monitoring — checking the plot, cross-referencing with a visual sweep every few minutes since I know some of these wooden boats don't paint well on radar. That's actually how we caught the first one — the lookout spotted a small boat visually at about three miles before ARPA ever picked it up. Its light was dim, flickering, hard to get a steady bearing on at first.

Interviewer: What did you do once that boat was sighted?

Participant: We kept watching it. It was converging, but slowly, and ARPA still wasn't holding a firm track — weak return, in and out. I logged it mentally as one to watch rather than something urgent.

Interviewer: Let's go through the timeline a bit more before we get into specifics. After that first sighting, what came next?

Participant: The boat kept closing, down to about two miles. Around the same time we hit a squall band — visibility dropped, and radar showed a loose cluster of three or four more small contacts near the next waypoint. That waypoint rang a bell because there'd been a bulletin from the office a couple weeks back about a near-miss with a fishing cluster right around there, in fog, very similar setup. On top of that, a bulk carrier showed up on the starboard bow, CPA tightening. So for a while I had three things going at once. Eventually the bulk carrier needed a real course adjustment, and the fishing cluster passed wider than I expected. Nothing hit, watch ended, I briefed the master and handed over.

Interviewer: Let's go back to that first boat at three miles. What alternatives did you weigh?

Participant: Honestly it was between letting the ARPA scan handle prioritization since nothing was flagged, or doing extra manual sweeps myself. I went with splitting attention — mostly trusting the system's target list but throwing in visual checks specifically because I've been burned before by small wooden hulls not showing up well. That's standard practice for me in these waters.

Interviewer: And when the boat closed to two miles, still without ARPA elevating it — what happened at that point?

Participant: That one I keep turning over. The lookout said the boat seemed to be zigzagging, not settling into a track you could plot cleanly, which usually would make me nervous. But ARPA's overall ranking still had nothing above the alarm threshold — none of the five original targets or this one had crossed into the alert zone. Two VHF calls to it got no answer. I decided to keep monitoring rather than take early avoiding action, mainly because the system wasn't telling me anything was critical yet and I didn't want to make an unnecessary alteration inside the TSS lane over a contact the system itself hadn't escalated.

Interviewer: What would have changed that decision for you?

Participant: If the ARPA alarm had actually tripped on it, I'd have gone straight to manual plotting and probably altered early. As it was, the numbers on the display weren't backing up what the lookout was describing, so I leaned on the display.

Interviewer: How much time pressure did you feel at that point?

Participant: Not extreme, maybe ten, fifteen minutes before it would've mattered. Enough room to keep watching, is how it felt.

Interviewer: Let's move to the squall and the cluster near the waypoint. What drove your read of the danger there?

Participant: That one hit me fast. Visibility dropped, this loose cluster showed up right at the spot from the bulletin, and my first thought honestly was "this is the same setup as that near-miss." That report had been pretty vivid — fog, fishing boats, a ship that barely missed hitting one. So I started orienting my planning toward the cluster, working out an evasive course for it, getting the lookout focused that direction.

Interviewer: How did that compare with how you handled the bulk carrier at the same time?

Participant: The bulk carrier was actually the one with the tightening CPA on the numbers — inside a mile and closing. I noticed it, but for a bit my attention was more on the cluster because that scenario felt like the one about to go wrong. It wasn't until a little later that I really focused back on the bulk carrier's plot and realized that was the one needing the firmer action.

Interviewer: What was your sense of the cluster's actual plotted risk at the time, separate from the bulletin?

Participant: Looking back, the spacing and drift on the cluster weren't actually showing a fast closing rate yet. It was more that the situation reminded me strongly of that report.

Interviewer: If there'd been no bulletin about a similar incident, do you think you'd have split your attention differently?

Participant: Probably, yeah. Without that in my head, I think the bulk carrier's numbers would've grabbed me first, since objectively that was the tighter CPA.

Interviewer: Last decision point — after both situations resolved, you briefed the master. How did you decide what to recommend?

Participant: Both contacts passed clear, no drama, so I could've just logged it as routine. But given how much fishing activity we'd seen, and one more area coming up with reported fishing boats, I recommended posting an extra lookout for the rest of the transit. Felt like the sensible call based on what we'd actually observed that watch, not tied to any one incident.

Interviewer: Had you seen a comparable multi-contact situation before this?

Participant: A few times, though usually not three things converging together like that. Normally it's one contact at a time.

Interviewer: Looking back, what are you most uncertain about?

Participant: Whether I gave the first boat too much benefit of the doubt because the system wasn't flagging it. And whether I'd have caught the bulk carrier sooner if that bulletin hadn't been sitting in the back of my mind.

Interviewer: If you faced this same combination again, what would you do differently?

Participant: I'd probably force myself to independently plot any contact the lookout flags as behaving oddly, regardless of what the ranking shows. And I'd try to rank contacts by their actual numbers first before letting any one of them feel more urgent just because it resembles something I'd heard about.

Interviewer: That's helpful, thank you. I think that covers what I needed.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MO_Biased_2",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Watchkeeping Officer (Bridge Watch)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Fishing Fleet Crossing in the Strait Squall",
    "scenario_summary_internal": "A second officer stands a night watch aboard a mid-size containership transiting a congested strait during intermittent monsoon squalls. A low-radar-cross-section fishing boat closes on a crossing track while ARPA ranks it as low priority relative to larger tracked targets. As visibility drops further, a cluster of fishing boats appears near a waypoint where a serious near-miss was documented in a recent company safety bulletin. The officer must manage attention across multiple contacts, decide when to depart from the automated system's risk ranking, and judge the actual probability of a repeat incident versus the vivid recalled case, while a genuinely converging bulk carrier requires separate assessment.",
    "occupational_realism": {
      "objective": "Maintain a safe, COLREGs-compliant passage through a congested strait during the 0000-0400 watch, correctly prioritizing collision risk among multiple concurrent contacts under degraded visibility.",
      "setting": "Bridge of a mid-size containership transiting a busy international strait at night, intermittent monsoon squalls, moderate fishing-fleet activity, ARPA/ECDIS-equipped bridge, single OOW plus lookout, Master on standby call.",
      "constraints": [
        "Reduced visibility from intermittent squalls",
        "Multiple simultaneous radar/AIS contacts of varying reliability",
        "Small wooden fishing vessels with low radar cross-section and no functioning AIS",
        "Fixed passage schedule and traffic separation scheme requirements",
        "Single qualified lookout available to supplement OOW",
        "Master not immediately on the bridge, contactable but not present"
      ],
      "stakeholders": [
        "Officer of the Watch (subject)",
        "Lookout/AB on watch",
        "Master (on standby call)",
        "Crews of nearby fishing vessels",
        "Approaching bulk carrier's bridge team",
        "Company safety/fleet office (source of prior bulletin)"
      ],
      "technical_terms_to_use": [
        "ARPA", "CPA", "TCPA", "COLREGs", "AIS", "OOW", "VHF", "radar plot",
        "safe speed", "close-quarters situation", "lookout", "squall",
        "fishing fleet", "waypoint", "bridge team", "Master", "traffic separation scheme",
        "radar cross-section", "give-way vessel", "stand-on vessel"
      ],
      "technical_terms_to_avoid": [
        "automation bias", "availability bias", "availability heuristic",
        "overreliance", "anchoring", "cognitive bias", "heuristic", "algorithm trust"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "ARPA has acquired and is tracking 5 targets, none flagged critical by CPA/TCPA",
          "VHF traffic mentions active fishing fleet operating in the area",
          "Weather forecast indicates intermittent squalls reducing visibility to under 1nm for short intervals",
          "Passage plan requires holding course to next waypoint in the TSS"
        ],
        "new_information_after_decision": [
          "A small wooden fishing boat, not previously acquired by ARPA, is sighted visually at approximately 3nm on a converging bearing",
          "The lookout reports the boat's navigation light is dim and intermittent"
        ],
        "alternatives": [
          "Rely on the ARPA-generated target list and its CPA/TCPA ranking to allocate scanning attention",
          "Conduct an independent visual and radar sweep specifically to catch low-cross-section contacts not shown by ARPA"
        ],
        "intended_action": "OOW splits attention between ARPA monitoring and periodic manual visual sweeps, catching the unacquired fishing boat via lookout report rather than system alert."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The fishing boat is now within 2nm, still not firmly held by ARPA due to weak radar return",
          "ARPA's overall risk ranking (based on the 5 tracked targets) still shows no target above the alarm threshold",
          "The lookout reports the fishing boat appears to be altering course erratically, inconsistent with a steady CPA solution",
          "Own ship's speed and heading are within the TSS lane requirements"
        ],
        "new_information_after_decision": [
          "The fishing boat continues on a track that reduces range faster than the manually estimated plot suggested",
          "No response is received to two VHF calls directed at the fishing boat"
        ],
        "alternatives": [
          "Treat the fishing boat as low-priority because the ARPA system has not elevated it on the ranked target list, and continue standard monitoring",
          "Independently plot the fishing boat by hand using visual bearings and take early avoiding action regardless of its ARPA ranking"
        ],
        "intended_action": "OOW defers to the system's overall low-priority ranking and delays independent maneuvering action, continuing to monitor rather than altering course early. [AUTOMATION_BIAS_INSTANCE: ab_01]"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A squall reduces visibility sharply; radar shows a loose cluster of 3-4 small contacts near the upcoming waypoint",
          "This waypoint is the same location referenced in a company safety bulletin describing a serious near-miss with a fishing-boat cluster two weeks earlier in similar fog conditions",
          "A separate, larger contact identified as a bulk carrier is closing from the OOW's starboard bow with a computed CPA inside 1nm",
          "Current plotted spacing and bearing drift of the fishing cluster do not yet indicate an especially high closing rate"
        ],
        "new_information_after_decision": [
          "The bulk carrier's CPA continues to tighten and requires a genuine collision-avoidance response shortly after",
          "The fishing cluster passes at a wider margin than initially feared, without requiring emergency action"
        ],
        "alternatives": [
          "Judge the current risk level primarily by how closely the situation resembles the vividly recalled bulletin incident, prioritizing attention and evasive planning toward the fishing cluster",
          "Judge current risk using the actual plotted spacing, bearing drift, and closing rates of all contacts, including the bulk carrier, independent of the recalled incident"
        ],
        "intended_action": "OOW reallocates attention and prepares an evasive maneuver oriented toward the fishing cluster because the recalled bulletin incident makes that outcome feel highly likely, temporarily under-attending to the bulk carrier's tightening CPA. [AVAILABILITY_BIAS_INSTANCE: av_01]"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Both the fishing cluster and the bulk carrier situations have been resolved without collision",
          "The Master calls the bridge for a status update before the watch handover",
          "The remainder of the watch will pass through one more area with reported fishing activity"
        ],
        "new_information_after_decision": [
          "The relieving officer requests a full brief on both contacts and the reasoning used during the encounter"
        ],
        "alternatives": [
          "Log the encounter as routinely resolved and hand over the watch without changes to standing orders",
          "Recommend to the Master that an additional lookout be posted for the remainder of the transit given the fishing activity"
        ],
        "intended_action": "OOW briefs the Master and recommends an additional lookout for the remaining fishing-activity area, based on the plotted contact behavior observed during the watch."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe the overall situation on the bridge that night and what you were responsible for.",
        "What was your main objective during this watch?"
      ],
      "timeline_reconstruction": [
        "Walk me through the sequence of contacts you dealt with, in order.",
        "At what point did the fishing boat become a concern, and how did that unfold?",
        "What happened when visibility dropped near the waypoint?"
      ],
      "decision_point_probes": [
        "At the point you first noticed the unacquired fishing boat, what information sources were you using, and how did you decide where to focus attention?",
        "When the fishing boat closed to about 2nm without ARPA elevating it, what made you decide to continue monitoring rather than take early action? What alternatives did you consider?",
        "When the squall hit and the cluster appeared near that waypoint, what specifically drove your sense of how dangerous the situation was? How did that compare with the bulk carrier's situation?",
        "When you briefed the Master afterward, how did you decide what to recommend for the rest of the watch?"
      ],
      "cues": [
        "What specific cues told you the fishing boat's light was unreliable?",
        "What cues, if any, made the fishing cluster feel similar to the earlier bulletin incident?"
      ],
      "information_sources": [
        "Which instruments or reports did you rely on most at each stage, and why?"
      ],
      "goals": [
        "How did you balance schedule/passage requirements against collision-avoidance caution?"
      ],
      "alternatives": [
        "What other options did you consider and reject at each decision point?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision at the point you delayed action on the fishing boat?",
        "What ultimately tipped your attention toward the fishing cluster over the bulk carrier?"
      ],
      "prior_experience": [
        "Had you encountered a similar situation before, and did that affect how you read this one?"
      ],
      "time_pressure": [
        "How much time did you feel you had to decide at each of these points?"
      ],
      "uncertainty": [
        "What were you most uncertain about at each stage, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the ARPA had flagged the fishing boat early as high-risk, do you think you would have acted differently?",
        "If there had been no recent bulletin about a similar incident, do you think your attention would have been distributed differently between the fishing cluster and the bulk carrier?",
        "What would you do differently if you faced this same combination of contacts again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "decision_point": 2,
        "mechanism": "OOW defers to ARPA's aggregate risk ranking (based on well-tracked large targets) as the basis for inaction on a weakly-tracked, erratically-moving small craft, despite an independent lookout report suggesting elevated risk.",
        "affected_reasoning_operation": "Risk prioritization and choice of when to escalate to manual avoidance action",
        "evidence_available_at_time": [
          "ARPA target list showing no target above alarm threshold",
          "Lookout report of erratic small-craft movement inconsistent with a steady ARPA-style solution",
          "Two unanswered VHF calls"
        ],
        "required_textual_manifestation": "OOW explicitly cites the system's ranking/alarm status as the reason for not escalating, while acknowledging the lookout's conflicting visual read, and delays independent plotting or maneuver until range has closed further.",
        "plausible_nonbias_interpretation": "It is reasonable domain practice to trust a calibrated ARPA alarm threshold when workload is high and to avoid premature helm action on an unconfirmed contact.",
        "strength": "moderate",
        "do_not_make_explicit": ["automation bias", "overreliance on automation", "algorithm trust"]
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 3,
        "mechanism": "OOW's estimate of the fishing cluster's danger is driven by the vividness and recency of a specific bulletin-reported near-miss at the same waypoint, rather than by the current plotted spacing/closing-rate data, leading to a temporary misallocation of attention away from the bulk carrier, whose CPA data indicated the more pressing risk.",
        "affected_reasoning_operation": "Probability/risk estimation and attention allocation across concurrent contacts",
        "evidence_available_at_time": [
          "Recalled bulletin narrative describing a similar fog/fishing-cluster near-miss at the same waypoint",
          "Current radar plot showing fishing cluster spacing and bearing drift not yet indicating high closing rate",
          "Bulk carrier's tightening CPA data"
        ],
        "required_textual_manifestation": "OOW explains the shift in attention toward the fishing cluster primarily by reference to how similar the situation felt to the recalled incident, rather than by citing the cluster's own plotted numbers, while the bulk carrier's tightening CPA is mentioned as secondary or noticed late.",
        "plausible_nonbias_interpretation": "Drawing on a recent, relevant safety bulletin about the same waypoint is a legitimate use of institutional learning and precaution, not necessarily a distortion of current risk assessment.",
        "strength": "moderate",
        "do_not_make_explicit": ["availability bias", "availability heuristic", "recency effect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, not a control condition."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence/absence and vividness of the recent company safety bulletin describing a near-miss at the same waypoint (autoselected as the most causally testable factor for a future counterfactual pairing)",
      "original_state": "Bulletin exists and is vivid/recently discussed, shaping the OOW's risk estimate at Decision Point 3",
      "counterfactual_state": "No such bulletin exists or was never discussed on board; OOW must estimate cluster risk purely from current plotted data",
      "variables_to_hold_constant": [
        "Vessel type and passage route",
        "Weather sequence (squall timing and severity)",
        "Contact set and their kinematics (fishing boat, fishing cluster, bulk carrier)",
        "Watch composition and workload",
        "Decision count and structure"
      ],
      "expected_causal_difference": "Without the bulletin, attention allocation at Decision Point 3 should track the bulk carrier's tightening CPA more directly, since the fishing cluster no longer benefits from anecdotal salience.",
      "causal_test_question": "Does the OOW's attention shift toward the fishing cluster depend on the recalled bulletin narrative rather than on the cluster's own plotted risk data?"
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two alternatives.",
      "Automation Bias instance is confined to Decision Point 2; Availability Bias instance is confined to Decision Point 3.",
      "Decision Points 1 and 4 contain no intentionally planned bias instances.",
      "No bias terminology or psychological labels appear in timeline, probes, or intended actions.",
      "Each planned instance has a distinct evidence source and reasoning operation from any other instance.",
      "Scenario content and probe set are sized to fit 1,215-1,485 words without repetitive exposition.",
      "Consequences (safe passage of both contacts) do not by themselves confirm or refute whether either decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Automation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as deference to ARPA's aggregate risk ranking over a conflicting independent lookout report, at Decision Point 2 only."
      },
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as risk estimation anchored to a vividly recalled prior incident rather than current plotted data, at Decision Point 3 only."
      }
    ],
    "target_bias_names": ["Automation Bias", "Availability Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Automation Bias", "requested_occurrences": 1},
      {"bias": "Availability Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "ab_01", "bias": "Automation Bias"},
      {"instance_id": "av_01", "bias": "Availability Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "ab_01", "bias": "Automation Bias", "decision_point": 2},
      {"instance_id": "av_01", "bias": "Availability Bias", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "mechanism": "Deference to ARPA's aggregate target-ranking output over a conflicting independent visual/lookout signal, delaying escalation to manual plotting or avoidance action.",
        "affected_reasoning_operation": "Risk prioritization / escalation decision",
        "evidence_source": "ARPA target list and alarm threshold vs. lookout's visual report of erratic small-craft movement",
        "distinctiveness_requirement": "Must be textually distinct from av_01 by involving system-output deference rather than recalled-incident salience, and must occur only at Decision Point 2."
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Risk probability estimate for the fishing cluster driven by ease of recall and vividness of a recent bulletin incident rather than current plotted spacing/closing-rate data, causing temporary under-attention to the bulk carrier's tightening CPA.",
        "affected_reasoning_operation": "Probability estimation and attention allocation across concurrent contacts",
        "evidence_source": "Recalled bulletin narrative vs. current radar plot of fishing cluster and bulk carrier CPA/TCPA",
        "distinctiveness_requirement": "Must be textually distinct from ab_01 by involving recalled-incident salience rather than system-output deference, and must occur only at Decision Point 3."
      }
    ],
    "intended_strength": [
      {"instance_id": "ab_01", "bias": "Automation Bias", "strength": "moderate"},
      {"instance_id": "av_01", "bias": "Availability Bias", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence/vividness of the recent safety-bulletin near-miss narrative (autoselected; not activated under the biased condition)",
      "original_state": "Bulletin exists and is vivid/recently discussed",
      "changed_state": "not_applicable_condition_is_biased",
      "variables_to_hold_constant": [
        "Vessel type and passage route",
        "Weather sequence",
        "Contact kinematics",
        "Watch composition",
        "Decision count and structure"
      ]
    },
    "scenario_id": "MO_Biased_2",
    "domain_id": "MO",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences spread one-per-bias across two distinct decision points (2 and 3), chosen for mechanism fit: Automation Bias tied to system-output deference during active target tracking, Availability Bias tied to recalled-incident salience during a spatially/thematically matching hazard (fishing cluster near the bulletin's waypoint). Decision Points 1 and 4 left free of intentional bias instances to preserve narrative realism and avoid over-saturation.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vessel type, route, and TSS constraints",
      "Weather/squall sequence",
      "Number and identity of contacts (fishing boat, fishing cluster, bulk carrier)",
      "Watch composition (single OOW plus lookout, Master on standby)",
      "Four-decision-point structure and probe set"
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
          "segment_type": "monitoring_strategy",
          "raw_interview_anchor": "checking the plot, cross-referencing with a visual sweep every few minutes since I know some of these wooden boats don't paint well on radar",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Independent visual cross-checking is a sensible monitoring strategy and is not an intentionally biased instance."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "initial_prioritization",
          "raw_interview_anchor": "It was converging, but slowly, and ARPA still wasn't holding a firm track ... I logged it mentally as one to watch rather than something urgent.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is the initial low-urgency assessment before the hidden Automation Bias decision point; the specification assigns no planned bias here."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "attention_allocation",
          "raw_interview_anchor": "I went with splitting attention — mostly trusting the system's target list but throwing in visual checks specifically because I've been burned before by small wooden hulls not showing up well.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The response describes a mixed ARPA and visual monitoring plan at Decision Point 1, which is explicitly non-biased in the hidden specification."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "evidence_weighting_and_escalation",
          "raw_interview_anchor": "The lookout said the boat seemed to be zigzagging ... But ARPA's overall ranking still had nothing above the alarm threshold ... I decided to keep monitoring rather than take early avoiding action, mainly because the system wasn't telling me anything was critical yet.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ab_01"
          ],
          "ground_truth_rationale": "The decision defers to ARPA's aggregate ranking and non-alarm state despite the conflicting lookout report, delaying independent plotting or avoidance."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "risk_estimation_and_attention_allocation",
          "raw_interview_anchor": "this loose cluster showed up right at the spot from the bulletin, and my first thought honestly was 'this is the same setup as that near-miss' ... I started orienting my planning toward the cluster",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "av_01"
          ],
          "ground_truth_rationale": "The vivid recalled bulletin drives the estimated danger and attention allocation despite the cluster's weaker plotted risk relative to the bulk carrier."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "comparative_attention_correction",
          "raw_interview_anchor": "The bulk carrier was actually the one with the tightening CPA on the numbers ... for a bit my attention was more on the cluster ... later ... realized that was the one needing the firmer action.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a later recognition and correction within the same episode; the hidden instance is mapped to the earlier salience-driven judgment in seg_005."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "communication_and_resource_recommendation",
          "raw_interview_anchor": "I recommended posting an extra lookout for the rest of the transit ... based on what we'd actually observed that watch, not tied to any one incident.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The post-watch recommendation is an evidence-based precaution and Decision Point 4 contains no planned bias instance."
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
    "analysis_scope_note": "Analyzed the participant's reported reasoning during watchkeeping decisions; no bias inferred from interviewer questions or outcomes alone."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "automation complacency",
      "alternative_labels": [
        "automation bias",
        "automation-induced complacency"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Insufficient monitoring or overtrust of an automated system, such that the absence of an automated alarm or hazard designation is treated as evidence that no hazard requires action, leading to omission errors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to keep monitoring the first visually sighted boat rather than taking early avoiding action",
      "decision_point_description": "After the lookout reported the boat zigzagging and VHF calls received no answer, the participant chose continued monitoring over early avoidance because ARPA had not escalated the contact.",
      "affected_reasoning_operation": "Risk appraisal and action threshold for an ambiguous radar/visual contact; prioritization of automated target ranking over conflicting lookout report.",
      "bias_specific_mechanism": "Automation-related omission: the absence of an ARPA alarm or target ranking was used as evidence that the contact was not yet critical, reducing the felt need to independently plot or maneuver despite conflicting visual observations.",
      "manifestation_in_interview": "The participant explicitly says he leaned on the ARPA display rather than the lookout's report, and that an ARPA alarm would have triggered manual plotting and early alteration.",
      "effect_on_reasoning_or_decision": "Delayed early avoiding action and independent plotting, prolonging passive monitoring of a closing, erratically behaving contact.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The lookout said the boat seemed to be zigzagging, not settling into a track you could plot cleanly, which usually would make me nervous. But ARPA's overall ranking still had nothing above the alarm threshold — none of the five original targets or this one had crossed into the alert zone.",
          "evidence_explanation": "Shows a conflicting cue from the lookout was de-prioritized because the automated system's ranking did not cross an alarm threshold."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I decided to keep monitoring rather than take early avoiding action, mainly because the system wasn't telling me anything was critical yet and I didn't want to make an unnecessary alteration inside the TSS lane over a contact the system itself hadn't escalated.",
          "evidence_explanation": "Attributes the no-action decision primarily to system non-escalation, a core automation-complacency pattern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the ARPA alarm had actually tripped on it, I'd have gone straight to manual plotting and probably altered early. As it was, the numbers on the display weren't backing up what the lookout was describing, so I leaned on the display.",
          "evidence_explanation": "Explicitly states reliance on displayed automated information over the visual lookout report when deciding not to take early action."
        }
      ],
      "correction_or_counterevidence": "The participant did perform periodic visual sweeps and the lookout's initial sighting was used; also, avoiding unnecessary maneuvers inside a TSS lane is a legitimate operational consideration, so the decision was not entirely driven by complacency.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Parasuraman and Manzey passage supports the automation complacency construct, including overreliance on ARPA and insufficient monitoring of other sources.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The National Transportation Safety Board (1997) report on the incident cited crew overreliance on the ARPA system and complacency associated with insufficient monitoring of other sources of navigational information, such as the Loran  C radar and visual lookout.",
          "mechanism_supported_by_source": "Overreliance on automated radar plotting and complacency-related insufficient monitoring of available non-automated information sources.",
          "relevance_to_this_occurrence": "Parallels the participant's overreliance on ARPA target ranking and failure to act on the lookout's visual/behavioral information."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which the perceived likelihood, urgency, or risk of an event is influenced by how easily similar instances come to mind, especially vivid or recent cases.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Allocation of attention and risk planning between the fishing cluster near the waypoint and the bulk carrier during the squall",
      "decision_point_description": "When a loose fishing cluster appeared at the location of a previous near-miss bulletin, the participant immediately framed it as the same setup and began planning for it, while temporarily underweighting the bulk carrier's tighter CPA.",
      "affected_reasoning_operation": "Risk prioritization and attentional allocation across multiple contacts.",
      "bias_specific_mechanism": "A recent vivid near-miss bulletin made the fishing-cluster scenario mentally available, so the participant judged its danger as higher based on resemblance/salience rather than the objective plotted closing data, delaying attention to the bulk carrier with the tightening CPA.",
      "manifestation_in_interview": "The participant states his first thought was 'this is the same setup as that near-miss' and that he oriented planning toward the cluster even though its plotted spacing and drift did not yet show a fast closing rate; he says without the bulletin the bulk carrier's numbers would have grabbed him first.",
      "effect_on_reasoning_or_decision": "Delayed focus on the objectively tighter bulk-carrier CPA and led to planning for the cluster first.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That one hit me fast. Visibility dropped, this loose cluster showed up right at the spot from the bulletin, and my first thought honestly was 'this is the same setup as that near-miss.' That report had been pretty vivid — fog, fishing boats, a ship that barely missed hitting one. So I started orienting my planning toward the cluster, working out an evasive course for it, getting the lookout focused that direction.",
          "evidence_explanation": "Shows the vivid bulletin-driven identification of the situation and the resulting prioritization of the cluster."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The bulk carrier was actually the one with the tightening CPA on the numbers — inside a mile and closing. I noticed it, but for a bit my attention was more on the cluster because that scenario felt like the one about to go wrong.",
          "evidence_explanation": "Demonstrates that attention followed subjective felt urgency from the available scenario rather than objective plotted data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, the spacing and drift on the cluster weren't actually showing a fast closing rate yet. It was more that the situation reminded me strongly of that report.",
          "evidence_explanation": "Confirms the risk perception was driven by remindfulness/similarity to a previous report, not objective closing rate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. Without that in my head, I think the bulk carrier's numbers would've grabbed me first, since objectively that was the tighter CPA.",
          "evidence_explanation": "Counterfactual acknowledgment by the participant that the bulletin-biased allocation came at the expense of the objectively tighter contact."
        }
      ],
      "correction_or_counterevidence": "The participant did eventually shift attention back to the bulk carrier and took firmer action, so the bias affected prioritization timing rather than final outcome; reduced visibility and actual fishing activity made some caution toward the cluster reasonable.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the availability heuristic label was not available in the provided passages; the label is applied from general knowledge of the Tversky and Kahneman availability heuristic.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Analysis is based on a single self-report debrief, which may be subject to retrospective reconstruction or post-hoc rationalization.",
    "Retrieved corpus support directly covered automation complacency, but no retrieved passage directly covered the availability heuristic.",
    "The transcript provides no independent objective performance baseline or experimental condition; bias judgments are based on the participant's reported reasoning and outcomes."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MO_Biased_2_Sonar_on",
  "interview_id": "MO_Biased_2",
  "system_prompt_id": "Sonar",
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
