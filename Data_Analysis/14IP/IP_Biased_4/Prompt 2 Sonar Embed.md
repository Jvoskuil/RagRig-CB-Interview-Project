You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focuses on the participant's reasoning during the P-204 feedwater pump incident, using retrieved corpus passages where available and general cognitive-science labels where corpus support is absent."
  },
  "identified_bias_summary": [
    {
      "bias_label": "ambiguity aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "gambler's fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely heavily on an initial value or idea and to make insufficient adjustments from that anchor when later information becomes available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Root-cause attribution for the third P-204 bearing failure",
      "decision_point_description": "Selecting the primary contributing factor for the RCFA after the third bearing failure",
      "affected_reasoning_operation": "Causal attribution / root-cause inference",
      "bias_specific_mechanism": "An initial salient explanation—Marco's locknut torque sequence—served as an anchor; the later-noted lubrication interval extension was treated as secondary and not investigated deeply, consistent with insufficient adjustment from the anchor.",
      "manifestation_in_interview": "The participant reports that the technique difference 'jumped out' first, flagged it as primary, and only later recognized that all three failures occurred under the extended lubrication interval.",
      "effect_on_reasoning_or_decision": "Prematurely assigned primary causation to the installer's technique and did not fully evaluate the systemic lubrication-interval change before filing the RCFA.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the technique difference jumped out at me first. Marco's newer, he's still building his feel for these bigger pumps, and when I saw the different sequence I figured that was probably it—a slightly under- or over-torqued locknut can absolutely walk itself into a bearing failure over a few weeks. I flagged it in the RCFA as the primary contributing factor and had him redo that step with me watching next time.",
          "evidence_explanation": "Shows an early, salient cause becoming the primary conclusion before alternative causes were compared."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I noted it in the report, sure, but I didn't dig into it hard at that point. It felt like a secondary factor—we'd been running on that interval for a couple of quarters without an obvious spike in failures across the fleet, so my attention went to what was different about this specific failure, which was Marco's install.",
          "evidence_explanation": "Indicates insufficient adjustment away from the initial cause even though another plausible systemic factor was known."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd pulled the records on the other two failures side by side right then, I'd have seen all three happened under that same extended interval, regardless of who did the install. I did eventually see that, just not at that first pass.",
          "evidence_explanation": "Retrospective acknowledgment that a relevant comparison would have weakened the initial causal anchor."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized the extended lubrication interval may have been more important; time pressure and ambiguous vibration data were legitimate constraints.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label derives from the retrieved corpus passage on anchoring and adjustment in engineering.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "Initial answers anchor judgment, and subsequent adjustment from those anchors is typically insufficient.",
          "relevance_to_this_occurrence": "The participant anchored on the initial install-sequence explanation and did not adjust sufficiently when the lubrication-interval information was available."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "gambler's fallacy",
      "alternative_labels": [
        "Monte Carlo fallacy",
        "negative recency bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The mistaken belief that a sequence of independent events makes a different outcome more likely, such as expecting a streak of failures to be followed by a clean run.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interim monitoring schedule selection after third failure",
      "decision_point_description": "Whether to run on the standard vibration-monitoring schedule or add interim checks",
      "affected_reasoning_operation": "Probabilistic forecasting / risk judgment",
      "bias_specific_mechanism": "The participant treated the three prior failures as a streak that had to break, despite acknowledging the failures were mechanically independent.",
      "manifestation_in_interview": "He says he felt 'due for a clean run' because three bad failures had occurred back to back.",
      "effect_on_reasoning_or_decision": "Contributed to choosing the standard monitoring schedule rather than adding interim vibration checks or shortening the run interval.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But if I'm honest, part of my thinking was that we'd just had three failures in a row, and it felt like we were due for a clean run. Three bad ones back to back, statistically it seemed like the streak had to break at some point.",
          "evidence_explanation": "Direct statement of negative recency reasoning: prior independent failures were treated as predictive of future relief."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Each failure had its own distinct cause—heat, then lubrication, then this install variance. They weren't linked to each other mechanically. I think I was reading the run of bad luck as meaning something about what came next, more than the data actually supported.",
          "evidence_explanation": "Retrospective self-correction that the failures were independent and the streak did not support the forecast."
        }
      ],
      "correction_or_counterevidence": "The participant himself acknowledges the failures had distinct causes and that the expectation was not supported by data.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for gambler's fallacy was not available; the label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "heritage bias",
        "overconfidence effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely heavily on an initial value, existing method, or known quantity and adjust insufficiently to new requirements or information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Alignment method selection for P-204 repair",
      "decision_point_description": "Whether to wait for the specialist with a laser alignment rig or proceed with manual dial-indicator alignment",
      "affected_reasoning_operation": "Method/option evaluation under uncertainty",
      "bias_specific_mechanism": "The participant anchored on his long-used manual dial-indicator technique as a proven heritage method and did not sufficiently adjust for the newer, tighter alignment tolerance that did not apply when he learned the method.",
      "manifestation_in_interview": "He cited years of successful manual alignments and 'feel' to justify doing it himself, even though the tolerance standard had tightened since his original method was validated.",
      "effect_on_reasoning_or_decision": "Led him to reject the specialist/laser option and perform a manual alignment during the outage window.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've done manual dial-indicator alignments on pumps like this dozens of times, going back years, generally with good results. I know how it should feel when the shaft's tracking right. So I told the team I'd handle it manually and we'd keep the outage on schedule.",
          "evidence_explanation": "Shows the existing manual method as the dominant reference point for his confidence and scheduling decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "the alignment tolerance standard for this bearing class has actually tightened since I first learned my manual method. My old technique was validated against a looser tolerance band. And we still didn't know for sure that misalignment was even the main driver versus thermal growth. But at the time I was pretty confident my hands-on feel would get it close enough.",
          "evidence_explanation": "Acknowledges new information that should have reduced confidence or prompted adjustment, but the old method still drove the choice."
        }
      ],
      "correction_or_counterevidence": "The specialist/laser rig was unavailable for 24 hours and the outage window created real pressure; the participant later acknowledges his old technique was validated against a looser tolerance band.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label derives from the retrieved corpus passage on anchoring and adjustment in engineering, including heritage-based design reasoning.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "One arena in engineering where this can be seen is in the use of socalled “heritage”. the component, system, or concept level, the initia people have in mind when they first consider a prob dominate the entire development process.",
          "mechanism_supported_by_source": "Existing/heritage methods and known quantities can dominate engineering reasoning even when new circumstances change the assessment.",
          "relevance_to_this_occurrence": "The participant's established manual alignment technique acted like a heritage method, dominating his evaluation despite the tightened tolerance standard."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "ambiguity aversion",
      "alternative_labels": [
        "status quo bias",
        "uncertainty aversion"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A preference for known risks over unknown risks, even when the known option is objectively poor or clearly inadequate.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Bearing replacement part selection",
      "decision_point_description": "Whether to reorder the legacy bearing or install the OEM's newer sealed-bearing housing",
      "affected_reasoning_operation": "Risk/option evaluation under uncertainty",
      "bias_specific_mechanism": "The participant treated missing failure-rate data for the OEM upgrade as making it feel riskier than the legacy part, despite knowing the legacy part's performance was inadequate.",
      "manifestation_in_interview": "He chose the known-but-inadequate legacy bearing because the OEM's claims were vague and lacked hard failure-rate numbers.",
      "effect_on_reasoning_or_decision": "Led to reordering the same legacy bearing even though its known failure pattern was five to six weeks under current conditions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The lack of hard numbers on the OEM side bothered me. I didn't want to swap in something with an unclear track record during a tight outage when I at least understood the legacy part's behavior, even if it wasn't good behavior. So we reordered the same bearing.",
          "evidence_explanation": "Direct statement of preferring a known negative track record over an option with missing quantitative reliability data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When you say it like that, it does sound strange to stick with something I know is inadequate over something that might be better just because I couldn't quantify the 'might.' I think not having a number to point to made it feel riskier than it maybe was.",
          "evidence_explanation": "Retrospective recognition that missing numbers influenced perceived risk disproportionately."
        }
      ],
      "correction_or_counterevidence": "A tight outage schedule and genuinely missing OEM failure-rate data are legitimate reasons for caution; the participant later questions whether the preference was biased.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for ambiguity aversion was not available; the label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a retrospective self-report; some statements may be colored by hindsight or attempts at self-explanation.",
    "Time pressure, operational constraints, and missing data were present and serve as plausible non-bias explanations for some choices.",
    "Retrieved corpus passages are OCR-garbled in places and did not cover all identified labels."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IP_Biased_4_Sonar_on",
  "interview_id": "IP_Biased_4",
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
