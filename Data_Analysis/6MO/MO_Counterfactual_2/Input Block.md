<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm — this is a routine debrief about a watchkeeping incident, not disciplinary, and it's fine to be candid about your reasoning. Can you tell me your role and roughly how long you've been standing bridge watches?

Participant: Sure. I'm second officer, been standing OOW watches about four years now, mostly on container ships this size. That night I had the 0000 to 0400, on my own with one AB as lookout. We were transiting the strait — always busy, crossing traffic, fishing activity, and this time of year the squalls come through fast.

Interviewer: Can you walk me through what happened, from the start of the watch?

Participant: When I took over, ARPA had five targets acquired already, all comfortable CPAs. VHF chatter mentioned fishing boats working the area, and the forecast had squalls coming, visibility dropping under a mile at times. Passage plan had us holding course into the next TSS leg, so early on it was ordinary monitoring — checking the plot, doing a visual sweep every few minutes since I know some of these wooden hulls don't paint well on radar. That's how we caught the first one, actually — the lookout spotted a small boat visually at about three miles before ARPA ever held it. Dim light, flickering, hard to get a steady bearing.

Interviewer: What did you do once that boat was sighted?

Participant: Kept watching it. It was converging, but slowly, and ARPA still wasn't holding a firm track on it — weak return, in and out. I logged it as one to watch rather than urgent.

Interviewer: Let's build out the timeline a bit more before we get into specifics. What came after that?

Participant: The boat kept closing, down to about two miles. Around then we hit a squall band, visibility dropped, and radar showed a loose cluster of three or four more small contacts near the next waypoint. That spot stuck with me — a few months back I'd had a close call there myself, similar fog, fishing boats everywhere, never wrote it up formally, just one of those nights that sticks with you. On top of that, a bulk carrier showed up on the starboard bow, CPA tightening. So for a stretch I had three things going at once. Eventually the bulk carrier needed a real course adjustment, and the fishing cluster passed wider than I'd expected. Nothing hit, watch ended, I briefed the master and handed over.

Interviewer: Let's go back to that first boat at three miles. What alternatives did you weigh?

Participant: It was between letting the ARPA scan drive my attention since nothing was flagged, or doing extra manual sweeps myself. I split it — mostly trusting the target list but adding visual checks specifically because I've been caught before by small wooden hulls not showing up well. Standard practice for me in these waters.

Interviewer: When the boat closed to two miles, still without ARPA elevating it — what happened at that point?

Participant: That one I keep turning over. The lookout said the boat seemed to be zigzagging, not settling into anything you could plot cleanly, which normally would worry me. But ARPA's overall ranking still had nothing above the alarm threshold — none of the five original targets or this one had crossed into the alert zone. Two VHF calls got no answer. I decided to keep monitoring rather than take early avoiding action, mainly because the system wasn't telling me anything critical yet, and I didn't want to make an unnecessary alteration inside the TSS lane over a contact the system itself hadn't escalated.

Interviewer: What would have changed that decision for you?

Participant: If the ARPA alarm had actually tripped on it, I'd have gone straight to manual plotting and probably altered early. As it was, the numbers on the display weren't backing up what the lookout was describing, so I leaned on the display.

Interviewer: How much time pressure did you feel at that point?

Participant: Not extreme — maybe ten, fifteen minutes before it would've mattered. Enough room to keep watching, is how it felt.

Interviewer: Let's move to the squall and the cluster near the waypoint. What drove your read of the danger there?

Participant: That one hit me fast. Visibility dropped, this loose cluster showed up right at the spot where I'd had my own close call, and my first thought was, "this feels exactly like that night." That memory is pretty vivid for me — fog, boats everywhere, us barely clearing one. So I started orienting my planning toward the cluster, working out an evasive course for it, getting the lookout focused that direction.

Interviewer: How did that compare with how you handled the bulk carrier at the same time?

Participant: The bulk carrier actually had the tightening CPA on the numbers — inside a mile and closing. I noticed it, but for a bit my attention was more on the cluster because that scenario felt like the one about to go wrong again. It wasn't until a little later that I really focused back on the bulk carrier's plot and realized that was the one needing the firmer action.

Interviewer: What was your sense of the cluster's actual plotted risk at the time, separate from that memory?

Participant: Looking back, the spacing and drift on the cluster weren't actually showing a fast closing rate yet. It was more that the situation reminded me strongly of what I'd been through.

Interviewer: If you'd never had that earlier close call at this waypoint, do you think you'd have split your attention differently?

Participant: Probably, yeah. Without that in my head, I think the bulk carrier's numbers would've grabbed me first, since objectively that was the tighter CPA.

Interviewer: Last decision point — after both situations resolved, you briefed the master. How did you decide what to recommend?

Participant: Both contacts passed clear, no drama, so I could've just logged it as routine. But given how much fishing activity we'd seen, and one more area coming up with reported boats, I recommended posting an extra lookout for the rest of the transit. Felt like the sensible call based on what we'd actually observed that watch, not tied to any one incident.

Interviewer: Had you told anyone about that earlier close call, or was it something you carried on your own?

Participant: Just me, really. Never came up in a bulletin or briefing, it wasn't that kind of event — no damage, no report filed. Just something I remembered vividly whenever I passed that spot again.

Interviewer: Looking back, what are you most uncertain about?

Participant: Whether I gave the first boat too much benefit of the doubt because the system wasn't flagging it. And whether I'd have caught the bulk carrier sooner if that old memory hadn't been sitting in the back of my head.

Interviewer: If you faced this same combination again, what would you do differently?

Participant: I'd probably force myself to independently plot any contact the lookout flags as behaving oddly, regardless of what the ranking shows. And I'd try to rank contacts by their actual numbers first before letting any one of them feel more urgent just because it reminds me of something from my own experience.

Interviewer: That's helpful, thank you. I think that covers what I needed.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MO_Counterfactual_2",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Watchkeeping Officer (Bridge Watch)",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Fishing Fleet Crossing in the Strait Squall (Personal-Memory Variant)",
    "scenario_summary_internal": "Counterfactual pairing of MO_Biased_2. A second officer stands the same night watch aboard the same containership transiting the same congested strait during intermittent monsoon squalls, facing the same low-radar-cross-section fishing boat, the same fishing cluster near the same waypoint, and the same converging bulk carrier. The single causal variable changed is the source of the vivid recalled incident that colors the officer's risk judgment at the waypoint: instead of a recent company safety bulletin describing a near-miss there, the officer's own vivid personal recollection of a near-miss they experienced at that same waypoint several months earlier (never formally documented or circulated) now plays that role. All other material facts, the decision structure, and the automation-bias mechanism at the fishing-boat encounter remain unchanged.",
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
        "Approaching bulk carrier's bridge team"
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
          "This waypoint is the same location where the OOW personally experienced a serious near-miss with a fishing-boat cluster several months earlier, in similar fog conditions, an event never formally documented in any company bulletin",
          "A separate, larger contact identified as a bulk carrier is closing from the OOW's starboard bow with a computed CPA inside 1nm",
          "Current plotted spacing and bearing drift of the fishing cluster do not yet indicate an especially high closing rate"
        ],
        "new_information_after_decision": [
          "The bulk carrier's CPA continues to tighten and requires a genuine collision-avoidance response shortly after",
          "The fishing cluster passes at a wider margin than initially feared, without requiring emergency action"
        ],
        "alternatives": [
          "Judge the current risk level primarily by how closely the situation resembles the vividly remembered personal near-miss, prioritizing attention and evasive planning toward the fishing cluster",
          "Judge current risk using the actual plotted spacing, bearing drift, and closing rates of all contacts, including the bulk carrier, independent of the remembered event"
        ],
        "intended_action": "OOW reallocates attention and prepares an evasive maneuver oriented toward the fishing cluster because the personally remembered near-miss makes that outcome feel highly likely, temporarily under-attending to the bulk carrier's tightening CPA. [AVAILABILITY_BIAS_INSTANCE: av_01]"
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
        "What cues, if any, made the fishing cluster feel similar to what you'd experienced before?"
      ],
      "information_sources": [
        "Which instruments, reports, or personal recollections did you rely on most at each stage, and why?"
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
        "Had you encountered a similar situation before, and did that affect how you read this one?",
        "What information would have changed how much weight you gave to that earlier experience?"
      ],
      "time_pressure": [
        "How much time did you feel you had to decide at each of these points?"
      ],
      "uncertainty": [
        "What were you most uncertain about at each stage, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the ARPA had flagged the fishing boat early as high-risk, do you think you would have acted differently?",
        "If you had never personally experienced that earlier near-miss at this waypoint, do you think your attention would have been distributed differently between the fishing cluster and the bulk carrier?",
        "What would you do differently if you faced this same combination of contacts again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "decision_point": 2,
        "mechanism": "OOW defers to ARPA's aggregate risk ranking (based on well-tracked large targets) as the basis for inaction on a weakly-tracked, erratically-moving small craft, despite an independent lookout report suggesting elevated risk. Unchanged from the paired biased scenario since it is not the manipulated causal variable.",
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
        "mechanism": "OOW's estimate of the fishing cluster's danger is driven by the vividness and personal salience of the officer's own remembered near-miss at the same waypoint, rather than by the current plotted spacing/closing-rate data, leading to a temporary misallocation of attention away from the bulk carrier, whose CPA data indicated the more pressing risk. This is the manipulated variant: the vivid recalled event is a personal firsthand memory rather than an institutional bulletin.",
        "affected_reasoning_operation": "Probability/risk estimation and attention allocation across concurrent contacts",
        "evidence_available_at_time": [
          "Personally recalled near-miss experience at the same waypoint several months earlier, never documented in a bulletin",
          "Current radar plot showing fishing cluster spacing and bearing drift not yet indicating high closing rate",
          "Bulk carrier's tightening CPA data"
        ],
        "required_textual_manifestation": "OOW explains the shift in attention toward the fishing cluster primarily by reference to how similar the situation felt to their own earlier experience, rather than by citing the cluster's own plotted numbers, while the bulk carrier's tightening CPA is mentioned as secondary or noticed late.",
        "plausible_nonbias_interpretation": "Drawing on firsthand experience at a specific hazardous waypoint is a legitimate use of seasoned judgment, not necessarily a distortion of current risk assessment.",
        "strength": "moderate",
        "do_not_make_explicit": ["availability bias", "availability heuristic", "recency effect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "MO_Biased_2",
      "features_to_match": [
        "Vessel type, route, and TSS constraints",
        "Weather/squall sequence",
        "Contact set and kinematics (fishing boat, fishing cluster, bulk carrier)",
        "Watch composition and workload",
        "Four-decision-point structure and probe categories",
        "Automation-bias mechanism at Decision Point 2 (unchanged)"
      ],
      "features_to_remove_or_change": [
        "Source of the vivid recalled incident driving the availability-bias judgment at Decision Point 3: replace the company safety bulletin with the officer's own undocumented personal near-miss experience at the same waypoint"
      ],
      "ambiguity_boundary": "Not applicable: this is a counterfactual condition with a non-empty manifest, not an ambiguous or vocabulary control."
    },
    "counterfactual_specification": {
      "causal_variable": "Source of the vivid remembered incident that anchors the officer's risk judgment near the waypoint: an institutional safety bulletin (base scenario) versus the officer's own personal, undocumented near-miss memory (counterfactual)",
      "original_state": "The vivid recalled event is a company safety bulletin describing a near-miss with a fishing cluster at the same waypoint two weeks earlier",
      "counterfactual_state": "The vivid recalled event is the officer's own personal near-miss experience at the same waypoint several months earlier, never circulated or documented in any bulletin",
      "variables_to_hold_constant": [
        "Vessel type and passage route",
        "Weather sequence (squall timing and severity)",
        "Contact set and their kinematics (fishing boat, fishing cluster, bulk carrier)",
        "Watch composition and workload",
        "Decision count and structure",
        "Automation-bias mechanism and evidence trace at Decision Point 2"
      ],
      "expected_causal_difference": "The availability-bias manifestation should still occur, but its verbal grounding shifts from citing an external institutional source to citing personal firsthand recollection, testing whether the source of salience (institutional vs. experiential) changes how the officer narrates and justifies the same attentional distortion.",
      "causal_test_question": "Does the officer's disproportionate attention to the fishing cluster over the bulk carrier persist when the vivid recalled incident is a personal memory rather than an institutional bulletin, and does the officer's justification language differ accordingly?"
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two alternatives.",
      "Automation Bias instance is confined to Decision Point 2, unchanged from the paired biased scenario.",
      "Availability Bias instance is confined to Decision Point 3, with only the source of the recalled incident altered.",
      "Decision Points 1 and 4 contain no intentionally planned bias instances.",
      "No bias terminology or psychological labels appear in timeline, probes, or intended actions.",
      "Only one causal variable (source of vivid recalled incident) differs from the paired biased scenario; all other material facts, actors, and structure are held constant.",
      "Scenario content and probe set are sized to fit 1,215-1,485 words without repetitive exposition.",
      "Consequences (safe passage of both contacts) do not by themselves confirm or refute whether either decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Automation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as deference to ARPA's aggregate risk ranking over a conflicting independent lookout report, at Decision Point 2 only. Unaffected by the counterfactual manipulation."
      },
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as risk estimation anchored to a vividly recalled prior incident rather than current plotted data, at Decision Point 3 only, with the recalled incident sourced from personal memory rather than an institutional bulletin."
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
        "mechanism": "Deference to ARPA's aggregate target-ranking output over a conflicting independent visual/lookout signal, delaying escalation to manual plotting or avoidance action. Identical mechanism and evidence trace to the paired biased scenario.",
        "affected_reasoning_operation": "Risk prioritization / escalation decision",
        "evidence_source": "ARPA target list and alarm threshold vs. lookout's visual report of erratic small-craft movement",
        "distinctiveness_requirement": "Must be textually distinct from av_01 by involving system-output deference rather than recalled-incident salience, and must occur only at Decision Point 2. Must remain unchanged relative to MO_Biased_2's ab_01 since it is not the manipulated variable."
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Risk probability estimate for the fishing cluster driven by ease of recall and vividness of a personally experienced prior near-miss rather than current plotted spacing/closing-rate data, causing temporary under-attention to the bulk carrier's tightening CPA.",
        "affected_reasoning_operation": "Probability estimation and attention allocation across concurrent contacts",
        "evidence_source": "Recalled personal near-miss memory vs. current radar plot of fishing cluster and bulk carrier CPA/TCPA",
        "distinctiveness_requirement": "Must be textually distinct from ab_01 by involving recalled-incident salience rather than system-output deference, and must occur only at Decision Point 3. Must differ from MO_Biased_2's av_01 only in the source of the recalled incident (personal memory vs. institutional bulletin), not in the underlying mechanism."
      }
    ],
    "intended_strength": [
      {"instance_id": "ab_01", "bias": "Automation Bias", "strength": "moderate"},
      {"instance_id": "av_01", "bias": "Availability Bias", "strength": "moderate"}
    ],
    "paired_scenario_id": "MO_Biased_2",
    "counterfactual_variable": {
      "name": "Source of the vivid remembered incident anchoring the officer's waypoint risk judgment: institutional safety bulletin versus personal undocumented memory",
      "original_state": "Vivid recalled event is a company safety bulletin describing a near-miss with a fishing cluster at the same waypoint two weeks earlier",
      "changed_state": "Vivid recalled event is the officer's own personal near-miss experience at the same waypoint several months earlier, never documented or circulated",
      "variables_to_hold_constant": [
        "Vessel type and passage route",
        "Weather sequence (squall timing and severity)",
        "Contact set and their kinematics (fishing boat, fishing cluster, bulk carrier)",
        "Watch composition and workload",
        "Decision count and structure",
        "Automation-bias mechanism and evidence trace at Decision Point 2"
      ]
    },
    "scenario_id": "MO_Counterfactual_2",
    "domain_id": "MO",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences spread one-per-bias across two distinct decision points (2 and 3), identical allocation to the paired biased scenario MO_Biased_2, chosen for mechanism fit and to preserve causal minimality: only the evidentiary source underlying the Availability Bias instance at Decision Point 3 was altered (institutional bulletin to personal memory), while the Automation Bias instance at Decision Point 2 and all other material facts were held constant.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vessel type, route, and TSS constraints",
      "Weather/squall sequence",
      "Number and identity of contacts (fishing boat, fishing cluster, bulk carrier)",
      "Watch composition (single OOW plus lookout, Master on standby)",
      "Four-decision-point structure and probe set",
      "Automation-bias mechanism and evidence trace"
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
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "The lookout first spots the small boat visually; as it converges slowly and ARPA has no firm track, the participant keeps watching and logs it as one to watch rather than urgent.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Decision Point 1 is an intentional non-bias control: using both ARPA and visual sweeps is plausible for low-radar-cross-section craft."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "The participant weighs letting ARPA drive attention against extra manual sweeps and splits attention, adding visual checks because wooden hulls may not show on radar.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a deliberate complementary monitoring strategy and an intended non-bias segment."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "At two miles the lookout reports zigzagging; participant cites the untripped ARPA alarm and keeps monitoring rather than taking early avoiding action.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ab_01"
          ],
          "ground_truth_rationale": "Decision Point 2 contains deference to ARPA non-escalation over the conflicting lookout report, delaying independent plotting or maneuvering."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "During the squall, the cluster appears at the waypoint of the vivid personal near-miss; attention and evasive planning shift to it while the bulk carrier has tighter CPA, and participant later says the memory drove prioritization.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "av_01"
          ],
          "ground_truth_rationale": "Decision Point 3 contains vivid personal-memory-driven risk estimation and attention allocation away from the objectively tighter bulk-carrier CPA."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "After both contacts pass clear, participant briefs the Master and recommends an extra lookout for the remaining fishing-activity area based on observed activity.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Decision Point 4 is an intended non-bias recommendation grounded in observed fishing activity."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "retrospective_corrective_reasoning",
          "raw_interview_anchor": "The participant says they would independently plot any contact the lookout flags as behaving oddly, regardless of ARPA ranking.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a post-event corrective plan, not an additional manifested bias instance."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "retrospective_corrective_reasoning",
          "raw_interview_anchor": "The participant says they would rank contacts by actual numbers before letting one feel urgent because it recalls a prior experience.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a post-event corrective plan, not an additional manifested bias instance."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
