<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process-improvement purposes only, and I'll be asking you to walk me through a specific incident in detail. Can you tell me your role and how long you've been in it?

Participant: Sure. I'm a maintenance reliability engineer, been in this plant about eight years, and in reliability specifically for the last four. I cover rotating equipment mostly—pumps, compressors, some turbines.

Interviewer: Great. I want to focus on the recent situation with feedwater pump P-204. Can you walk me through what first told you something was wrong?

Participant: So this was the third bearing failure on P-204 in about five months. Each one roughly five to six weeks apart, which is not normal—this pump used to run a year or more between issues. I got the call from the control room that vibration alarms had tripped, and by the time I got out there the bearing housing was already running hot. We pulled the vibration spectrum and it showed both a thermal signature and some mechanical components, so it wasn't a clean single-cause picture right away.

Interviewer: What was your goal walking into that?

Participant: Get the pump back in service inside our outage window—we had 48 hours before production needed full output—and actually figure out why this keeps happening instead of just swapping the bearing again and hoping.

Interviewer: Can you reconstruct the sequence of what happened next?

Participant: First I pulled maintenance history on all three failures. Then I looked at who'd done the last PM—that was Marco, one of our newer techs, about six weeks before this failure. After that I looped in our vibration analyst to get a second opinion on the spectrum data. Once we had a working theory, I had to decide on an alignment approach, and in parallel we were sourcing a replacement bearing. Each of those steps fed into the next, and we were watching the clock the whole time.

Interviewer: Let's start with the root cause piece. What information did you have when you were trying to explain this third failure?

Participant: I had Marco's work order from the PM, and I noticed he'd used a slightly different locknut torque sequence than the guy who did the prior two PMs—not wrong exactly, just not identical to what I'd have done. I also knew our lubrication interval had been stretched from three months to four months a couple of quarters back, that was a corporate cost initiative. And I had the ambiguous vibration data.

Interviewer: How did you weigh those pieces of information against each other?

Participant: Honestly, the technique difference jumped out at me first. Marco's newer, he's still building his feel for these bigger pumps, and when I saw the different sequence I figured that was probably it—a slightly under- or over-torqued locknut can absolutely walk itself into a bearing failure over a few weeks. I flagged it in the RCFA as the primary contributing factor and had him redo that step with me watching next time.

Interviewer: Did you weigh the lubrication interval change the same way?

Participant: I noted it in the report, sure, but I didn't dig into it hard at that point. It felt like a secondary factor—we'd been running on that interval for a couple of quarters without an obvious spike in failures across the fleet, so my attention went to what was different about this specific failure, which was Marco's install.

Interviewer: What would have made you look harder at the interval instead?

Participant: If I'd pulled the records on the other two failures side by side right then, I'd have seen all three happened under that same extended interval, regardless of who did the install. I did eventually see that, just not at that first pass.

Interviewer: Let's move to the next decision—whether to add any extra monitoring before the next run. What was on the table?

Participant: Two options. Run it on the standard schedule, or add interim vibration checks partway through the run, maybe even shorten the run interval until we trusted the fix. The interim monitoring would've added a few hours to the outage.

Interviewer: What tipped you toward the standard schedule?

Participant: Time pressure was real—production wanted the pump back. But if I'm honest, part of my thinking was that we'd just had three failures in a row, and it felt like we were due for a clean run. Three bad ones back to back, statistically it seemed like the streak had to break at some point.

Interviewer: Was there anything in the failure data that supported that expectation specifically?

Participant: Not really, when you put it that way. Each failure had its own distinct cause—heat, then lubrication, then this install variance. They weren't linked to each other mechanically. I think I was reading the run of bad luck as meaning something about what came next, more than the data actually supported.

Interviewer: How confident were you in that call at the time?

Participant: Fairly confident, honestly. It felt intuitive in the moment.

Interviewer: Third decision point—the alignment work. What were you weighing there?

Participant: Our vibration analyst wanted a specialist in with the laser alignment rig, because we still weren't 100% sure if misalignment or thermal growth was the bigger driver. Problem was, the specialist and the laser tool weren't available for 24 hours, and that would've eaten deep into our window.

Interviewer: What made you decide to do it yourself instead?

Participant: I've done manual dial-indicator alignments on pumps like this dozens of times, going back years, generally with good results. I know how it should feel when the shaft's tracking right. So I told the team I'd handle it manually and we'd keep the outage on schedule.

Interviewer: Did anything give you pause about that approach specifically for this pump?

Participant: In hindsight, yes—the alignment tolerance standard for this bearing class has actually tightened since I first learned my manual method. My old technique was validated against a looser tolerance band. And we still didn't know for sure that misalignment was even the main driver versus thermal growth. But at the time I was pretty confident my hands-on feel would get it close enough.

Interviewer: Last decision—the bearing part itself. What were the two options?

Participant: Reorder the same legacy bearing we've always used, or install the OEM's newer sealed-bearing housing. The legacy part has a known pattern—it's not great, failures roughly every five to six weeks under current conditions, but at least we know exactly what we're dealing with. The OEM upgrade is supposedly more reliable, but their literature was vague—no actual failure-rate numbers for our application, just general claims.

Interviewer: What drove your final choice?

Participant: The lack of hard numbers on the OEM side bothered me. I didn't want to swap in something with an unclear track record during a tight outage when I at least understood the legacy part's behavior, even if it wasn't good behavior. So we reordered the same bearing.

Interviewer: Looking back, how do you weigh that against the fact that the legacy part's known performance was already failing every five to six weeks?

Participant: When you say it like that, it does sound strange to stick with something I know is inadequate over something that might be better just because I couldn't quantify the "might." I think not having a number to point to made it feel riskier than it maybe was.

Interviewer: If the lubrication interval had never been extended, do you think this would have played out differently?

Participant: Probably—less thermal stress, maybe none of the three failures happen the way they did. Hard to know for sure with the sample we have.

Interviewer: If the OEM had given you a specific failure-rate figure, would that have changed your bearing decision?

Participant: Possibly. If they'd said something like a documented multiple-of-improvement over our legacy MTBF, I think I'd have pushed harder to make the schedule work for the upgrade.

Interviewer: Anything you'd do differently if this came up again?

Participant: I'd probably pull the full failure history side by side earlier, before settling on a cause. And I'd think twice about doing the alignment myself if the tolerance standard has moved since I last checked my technique against it.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IP_Biased_4",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Maintenance Reliability Engineer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Recurring Bearing Failures on Feedwater Pump P-204",
    "scenario_summary_internal": "A maintenance reliability engineer investigates the third bearing failure in five months on a critical boiler feedwater pump (P-204) inside a tight 48-hour outage window. The engineer must determine the root cause of the latest failure, decide whether extra interim monitoring is warranted before the pump returns to service, choose between a specialist-led laser alignment and a personally performed manual alignment, and select between a well-known legacy bearing part and a newer OEM-upgraded bearing housing with less field history. The narrative embeds one instance each of Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, and Ambiguity Effect at four distinct decision points, with consequences left genuinely ambiguous so no single decision is proven biased by outcome alone.",
    "occupational_realism": {
      "objective": "Diagnose the cause of a recurring bearing failure on a critical feedwater pump and select a repair and monitoring strategy that returns the pump to reliable service before the outage window closes.",
      "setting": "A continuous-process industrial plant (e.g., chemical or power generation) with a centralized reliability engineering function, a 48-hour scheduled outage window, and limited access to OEM technical support.",
      "constraints": [
        "48-hour outage window before production demands full pump output",
        "OEM technical representative and laser alignment specialist have limited availability",
        "Corporate pressure to minimize unplanned downtime and repair cost",
        "Recent budget-driven change to lubrication interval (3 to 4 months)",
        "Staffing shortage limiting who can perform diagnostics",
        "Multiple other rotating assets competing for reliability team attention"
      ],
      "stakeholders": [
        "Reliability Engineer (interviewee)",
        "Marco, junior maintenance technician who performed the prior PM",
        "Plant Maintenance Manager",
        "Production Supervisor",
        "OEM technical representative",
        "Vibration analysis specialist"
      ],
      "technical_terms_to_use": [
        "bearing housing",
        "vibration spectrum",
        "alignment tolerance",
        "MTBF",
        "lubrication interval",
        "root cause failure analysis (RCFA)",
        "condition-based maintenance (CBM)",
        "OEM spec sheet",
        "shaft misalignment",
        "thermal growth",
        "laser alignment",
        "locknut torque"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "cognitive",
        "psychological",
        "fallacy",
        "attribution error",
        "illusion",
        "ambiguity aversion"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "P-204 bearing has failed a third time in five months, each roughly 5-6 weeks apart",
          "Vibration data from the failure is ambiguous, showing both thermal and mechanical signatures",
          "Marco performed the most recent preventive maintenance six weeks earlier and used a slightly different locknut tightening sequence than his predecessor",
          "The lubrication interval was changed from 3 to 4 months two quarters ago as a cost-saving measure",
          "The two prior failures were handled by different technicians using the standard sequence"
        ],
        "new_information_after_decision": [
          "Later records show technicians on all three failures followed varying but plant-approved procedures, and all three failures occurred under the same extended lubrication interval"
        ],
        "alternatives": [
          "Attribute the failure primarily to Marco's specific installation technique",
          "Broaden the investigation to situational/systemic factors such as the lubrication interval change, bearing batch quality, or ambient heat load"
        ],
        "intended_action": "The engineer concludes the failure was mainly caused by Marco's personal carelessness/inexperience, citing his nonstandard tightening sequence, while giving comparatively little weight to the recently changed lubrication interval that applied across all three failures."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three consecutive bearing failures have occurred at roughly similar intervals",
          "Failure interval data shows no statistical dependency between successive events; each failure has been linked to a distinct proximate condition (heat, lubrication, installation variance)",
          "An interim inspection or additional monitoring during the next run would require extending the outage window by several hours"
        ],
        "new_information_after_decision": [
          "The pump completes the next run without incident, which is consistent with both a genuine improvement and simple chance given the small sample size"
        ],
        "alternatives": [
          "Proceed with the standard run schedule without added monitoring, reasoning that the run is 'due' to succeed after three failures",
          "Add interim vibration checks or a shortened run interval given the still-unresolved root cause"
        ],
        "intended_action": "The engineer decides against extra monitoring, remarking that after three failures in a row the pump is 'bound to run clean this time,' despite the lack of any causal link between the independent failure events."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The vibration analyst recommends a specialist-led laser alignment given persistent uncertainty about whether misalignment or thermal growth is driving the failures",
          "The laser alignment specialist and tool are not available for 24 hours, which threatens the outage window",
          "The engineer has personally performed manual dial-indicator alignments on similar pumps in the past with generally acceptable results",
          "Industry alignment tolerances for this pump class have tightened since the engineer's manual technique was last validated"
        ],
        "new_information_after_decision": [
          "The manual alignment falls within the older, looser tolerance band the engineer used to judge success, though it is unclear whether it meets the newer tighter tolerance now recommended for this bearing type"
        ],
        "alternatives": [
          "Wait 24 hours for the specialist and laser tool to get a more precise alignment reading",
          "Perform the alignment manually himself using dial indicators and feel, to keep the outage on schedule"
        ],
        "intended_action": "The engineer chooses to personally perform the manual alignment, stating that his years of hands-on experience mean he can 'feel' when it's right, effectively believing his personal skill can reliably control the alignment outcome despite the unresolved diagnostic uncertainty about whether misalignment is even the dominant failure driver."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The legacy bearing part has a well-documented failure pattern: predictable but recurring failures roughly every 5-6 weeks under current conditions",
          "The OEM's newer sealed-bearing housing has limited field data, with only vague vendor claims of 'improved reliability' and no specific failure-rate figures for this application",
          "The OEM upgrade costs more and would require a minor housing modification within the outage window",
          "Both options are available for installation within the remaining outage time"
        ],
        "new_information_after_decision": [
          "The reordered legacy bearing installs without incident during the outage, but its long-term failure pattern remains statistically unresolved based on this single data point"
        ],
        "alternatives": [
          "Install the OEM's upgraded sealed-bearing housing despite the lack of specific failure-rate data",
          "Reorder the same legacy bearing part because its failure behavior, while poor, is at least well known"
        ],
        "intended_action": "The engineer selects the legacy bearing part, explicitly citing the lack of concrete failure-rate numbers for the OEM upgrade as the reason to avoid it, even though the legacy part's known failure history is itself clearly unsatisfactory."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first told you something was wrong with P-204 this time?",
        "What was your overall goal when you started this investigation?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do next?",
        "At what point did you bring in other people, like Marco or the vibration analyst?",
        "What information came in after each step that changed your thinking?"
      ],
      "decision_point_probes": [
        "What cues made you settle on that explanation for the failure?",
        "What information sources did you rely on most at that moment, and which did you set aside?",
        "What were you trying to achieve or protect when you made that call?",
        "What other options did you consider, and why did you rule them out?",
        "What was the main basis for your final decision at that point?",
        "Has something like this come up before in your experience, and how did that shape your thinking here?",
        "How much time pressure were you under when you made that call?",
        "How confident were you in the information you had at that moment?",
        "If you'd had more time or different data, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If the lubrication interval had never been changed, do you think the outcome would have been different?",
        "If the OEM had provided specific failure-rate numbers for the new bearing, would that have changed your choice?",
        "Looking back, is there a point where you'd handle things differently next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "IP_Biased_4_FAB_01",
        "bias": "Fundamental Attribution Bias",
        "decision_point": 1,
        "mechanism": "Engineer attributes the bearing failure primarily to Marco's personal disposition (carelessness, inexperience) rather than to the situational factor common to all three failures (the extended lubrication interval).",
        "affected_reasoning_operation": "Causal attribution during root cause diagnosis",
        "evidence_available_at_time": [
          "Marco's nonstandard tightening sequence",
          "Recently changed lubrication interval applying to all three failures",
          "Ambiguous vibration signature"
        ],
        "required_textual_manifestation": "The engineer explicitly links the failure to Marco's individual technique/character while giving minimal or dismissive weight to the shared situational factor, despite having the interval-change data available at the time.",
        "plausible_nonbias_interpretation": "It is reasonable domain practice to review the most recent technician's work first when a failure follows shortly after a PM.",
        "strength": "subtle",
        "do_not_make_explicit": ["fundamental attribution bias", "dispositional vs situational", "attribution error"]
      },
      {
        "instance_id": "IP_Biased_4_GF_01",
        "bias": "Gambler's Fallacy",
        "decision_point": 2,
        "mechanism": "Engineer reasons that because three independent failures have occurred in a row, the next run is 'due' to succeed, treating statistically independent failure events as if they were sequentially dependent.",
        "affected_reasoning_operation": "Prediction of future equipment reliability based on recent outcome streak",
        "evidence_available_at_time": [
          "Three consecutive failures at similar intervals",
          "Data showing each failure has a distinct proximate cause (no dependency between events)"
        ],
        "required_textual_manifestation": "The engineer states or implies that the recent run of failures makes a clean run more likely now, and uses this reasoning to justify skipping added monitoring.",
        "plausible_nonbias_interpretation": "Declining to add monitoring could be justified purely by outage-time constraints rather than a belief in a 'streak' correcting itself.",
        "strength": "subtle",
        "do_not_make_explicit": ["gambler's fallacy", "independent events", "law of small numbers"]
      },
      {
        "instance_id": "IP_Biased_4_IOC_01",
        "bias": "Illusion of control",
        "decision_point": 3,
        "mechanism": "Engineer overestimates his personal ability to achieve a correct alignment by feel/experience, treating a diagnostically uncertain, partly random outcome as primarily within his personal control.",
        "affected_reasoning_operation": "Decision on repair method and confidence in personally controlling the outcome",
        "evidence_available_at_time": [
          "Specialist recommendation for laser alignment",
          "Tightened industry tolerance standards since the engineer's technique was last validated",
          "Unresolved uncertainty about whether misalignment is even the dominant failure driver"
        ],
        "required_textual_manifestation": "The engineer expresses confidence that personal skill/experience will ensure a correct outcome ('I can feel when it's right') despite acknowledging the underlying diagnostic uncertainty and tighter tolerances.",
        "plausible_nonbias_interpretation": "Choosing the faster manual method could be a reasonable time-pressure tradeoff rather than overconfidence in personal control.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusion of control", "overconfidence", "personal control bias"]
      },
      {
        "instance_id": "IP_Biased_4_AE_01",
        "bias": "Ambiguity effect",
        "decision_point": 4,
        "mechanism": "Engineer avoids the OEM upgraded bearing option specifically because its success probability is unknown/ambiguous, choosing the legacy part whose failure probability is known even though it is clearly worse.",
        "affected_reasoning_operation": "Choice between two repair options under differing levels of probability information",
        "evidence_available_at_time": [
          "Legacy part's well-documented ~5-6 week recurring failure pattern",
          "OEM upgrade's vague reliability claims without specific failure-rate data"
        ],
        "required_textual_manifestation": "The engineer explicitly cites the lack of concrete numbers for the OEM option as the deciding reason to avoid it, in favor of the known-but-poor legacy option.",
        "plausible_nonbias_interpretation": "Sticking with the legacy part could be justified by cost or by genuine skepticism of unverified vendor marketing claims rather than aversion to ambiguity itself.",
        "strength": "subtle",
        "do_not_make_explicit": ["ambiguity effect", "ambiguity aversion", "known vs unknown probability"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for this biased-condition specification; no paired control scenario was supplied."
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
      "Confirm exactly one instance each of Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, and Ambiguity Effect, none repeated or paraphrased elsewhere.",
      "Confirm exactly four decision points, each with at least two plausible alternatives.",
      "Confirm no bias names, definitions, or psychological terminology appear in the interview text.",
      "Confirm each decision point includes probes for cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and at least one hypothetical.",
      "Confirm consequences after each decision remain ambiguous and do not mechanically prove bias or correctness.",
      "Confirm final interview word count falls between 1,215 and 1,485 words, targeting 1,350.",
      "Confirm each occurrence has a distinct evidence source and reasoning operation distinguishing it from the others."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Fundamental Attribution Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as dispositional attribution (Marco's character/skill) overriding an available situational cause (lubrication interval change) at decision point 1 only."
      },
      {
        "bias": "Gambler's Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as treating independent failure events as sequentially dependent ('due for a clean run') at decision point 2 only."
      },
      {
        "bias": "Illusion of control",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overestimating personal skill's ability to determine a diagnostically uncertain outcome at decision point 3 only."
      },
      {
        "bias": "Ambiguity effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as avoidance of the option with unknown/ambiguous probability information in favor of a known-but-worse option at decision point 4 only."
      }
    ],
    "target_bias_names": [
      "Fundamental Attribution Bias",
      "Gambler's Fallacy",
      "Illusion of control",
      "Ambiguity effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Fundamental Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Gambler's Fallacy", "requested_occurrences": 1 },
      { "bias": "Illusion of control", "requested_occurrences": 1 },
      { "bias": "Ambiguity effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "IP_Biased_4_FAB_01", "bias": "Fundamental Attribution Bias" },
      { "instance_id": "IP_Biased_4_GF_01", "bias": "Gambler's Fallacy" },
      { "instance_id": "IP_Biased_4_IOC_01", "bias": "Illusion of control" },
      { "instance_id": "IP_Biased_4_AE_01", "bias": "Ambiguity effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "IP_Biased_4_FAB_01", "bias": "Fundamental Attribution Bias", "decision_point": 1 },
      { "instance_id": "IP_Biased_4_GF_01", "bias": "Gambler's Fallacy", "decision_point": 2 },
      { "instance_id": "IP_Biased_4_IOC_01", "bias": "Illusion of control", "decision_point": 3 },
      { "instance_id": "IP_Biased_4_AE_01", "bias": "Ambiguity effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "IP_Biased_4_FAB_01",
        "bias": "Fundamental Attribution Bias",
        "mechanism": "Dispositional attribution of failure to Marco's personal technique/character rather than the shared situational lubrication-interval change.",
        "affected_reasoning_operation": "Causal attribution during root cause diagnosis",
        "evidence_source": "Maintenance PM record, lubrication interval change log",
        "distinctiveness_requirement": "Only intended instance of this bias; must not recur as a summary or outcome explanation later in the interview."
      },
      {
        "instance_id": "IP_Biased_4_GF_01",
        "bias": "Gambler's Fallacy",
        "mechanism": "Belief that a streak of independent failures makes the next outcome more likely to be favorable, absent any causal dependency.",
        "affected_reasoning_operation": "Prediction of near-term equipment reliability",
        "evidence_source": "Failure interval history, statistical independence of proximate causes across the three failures",
        "distinctiveness_requirement": "Must use failure-streak reasoning distinct from the attribution reasoning in decision point 1; no overlap in evidence source."
      },
      {
        "instance_id": "IP_Biased_4_IOC_01",
        "bias": "Illusion of control",
        "mechanism": "Overestimation of personal skill's capacity to guarantee a correct outcome despite unresolved diagnostic uncertainty and tightened external tolerance standards.",
        "affected_reasoning_operation": "Selection of repair method and self-assessed confidence in outcome control",
        "evidence_source": "Specialist recommendation, current alignment tolerance standard, engineer's self-reported track record",
        "distinctiveness_requirement": "Distinct from ambiguity effect at decision point 4: this instance concerns confidence in personal action, not comparison of two probability-labeled options."
      },
      {
        "instance_id": "IP_Biased_4_AE_01",
        "bias": "Ambiguity effect",
        "mechanism": "Avoidance of the OEM option due to its unknown/ambiguous success probability, favoring a known-but-inferior legacy option.",
        "affected_reasoning_operation": "Choice between two repair options under differing information quality",
        "evidence_source": "OEM vendor claims (no specific failure-rate data), legacy bearing's documented failure history",
        "distinctiveness_requirement": "Distinct from illusion of control at decision point 3: this instance concerns comparative evaluation of two options' probability information, not personal-control belief."
      }
    ],
    "intended_strength": [
      { "instance_id": "IP_Biased_4_FAB_01", "bias": "Fundamental Attribution Bias", "strength": "subtle" },
      { "instance_id": "IP_Biased_4_GF_01", "bias": "Gambler's Fallacy", "strength": "subtle" },
      { "instance_id": "IP_Biased_4_IOC_01", "bias": "Illusion of control", "strength": "subtle" },
      { "instance_id": "IP_Biased_4_AE_01", "bias": "Ambiguity effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IP_Biased_4",
    "domain_id": "IP",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per bias assigned to a distinct decision point (1:1 mapping across the four decision points), selected for mechanism fit and narrative realism per allocation rules 1-4; no decision point received more than one bias instance, so the shared-decision-point distinctiveness rule was not triggered.",
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
          "segment_id": "DP1_ROOT_CAUSE",
          "speaker": "Participant",
          "segment_type": "eligible_reasoning_segment",
          "raw_interview_anchor": "Root-cause analysis: the participant weighs Marco's different locknut torque sequence against the extended lubrication interval and ambiguous vibration data.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "IP_Biased_4_FAB_01"
          ],
          "ground_truth_rationale": "The participant initially attributes the recurring failure primarily to Marco's personal installation technique while underweighting the shared extended lubrication interval."
        },
        {
          "segment_id": "DP2_MONITORING",
          "speaker": "Participant",
          "segment_type": "eligible_reasoning_segment",
          "raw_interview_anchor": "Monitoring decision: the participant chooses the standard schedule after three failures because the pump felt due for a clean run.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "IP_Biased_4_GF_01"
          ],
          "ground_truth_rationale": "The participant treats a streak of independent failures as making a clean next run more likely."
        },
        {
          "segment_id": "DP3_ALIGNMENT",
          "speaker": "Participant",
          "segment_type": "eligible_reasoning_segment",
          "raw_interview_anchor": "Alignment decision: the participant performs the manual alignment himself rather than waiting for the specialist and laser rig.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "IP_Biased_4_IOC_01"
          ],
          "ground_truth_rationale": "The participant overestimates his personal hands-on skill's ability to control an uncertain alignment outcome despite tightened tolerances."
        },
        {
          "segment_id": "DP4_BEARING_SELECTION",
          "speaker": "Participant",
          "segment_type": "eligible_reasoning_segment",
          "raw_interview_anchor": "Bearing selection: the participant chooses the known legacy bearing over the OEM upgrade because the upgrade lacks specific failure-rate data.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "IP_Biased_4_AE_01"
          ],
          "ground_truth_rationale": "The participant avoids the ambiguous OEM option in favor of a known but demonstrably inadequate legacy option."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
