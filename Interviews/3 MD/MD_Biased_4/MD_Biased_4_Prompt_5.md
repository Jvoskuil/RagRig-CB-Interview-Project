You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for taking the time. Just to confirm, this is a voluntary cognitive task analysis debrief—we're reconstructing your decision-making during a specific fire support mission, not evaluating performance for any board or investigation. You can decline any question. Comfortable proceeding?

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Great. Can you describe your role and the mission?

Participant: I was the FSO attached to the company during a daylight clearing operation. We had an enemy 82mm mortar team that had been harassing our forward positions for about two days, and intel flagged a possible staging compound near a village on the objective's north edge. My job was coordinating mortars, then CAS, then artillery, to clear both threats before the company crossed the line of departure. Objective was straightforward—suppress the mortar team, clear the compound, keep it clean for friendlies and the village.

Interviewer: What made this mission nonroutine?

Participant: Timeline was tight—we had about thirty minutes before the assault window closed, ammo for the 81s was limited since we'd already used a chunk of it earlier that morning, and comms between me and FSCC kept dropping in and out. Plus the compound was close enough to friendly squads that anything there was going to be danger-close. And the only real-time picture we had on the compound was one ISR feed, no second source.

Interviewer: Walk me through the sequence as it happened.

Participant: First mission was against the mortar position with the 81s. Fired an adjustment round, it landed short. Fired a second one, still short. Section chief checked the gun-line data once, said no fault found. Around that time, I also had two conflicting reports on where the staging activity actually was—our battalion JTAC had one grid, and the partner-force liaison next to us had a grid about three hundred meters off. Then CAS checked in for the compound piece, and finally we had that ISR cue on the compound itself right before the artillery mission.

Interviewer: Let's take these one at a time. Start with the mortar adjustment rounds.

Participant: Right, so two rounds down, both short. Section chief ran through the data once and didn't find anything wrong. At that point I had a decision—stop and have them do a full re-lay, checking level, deflection, everything from scratch, or fire the next adjustment round and see what happens.

Interviewer: What did you decide, and why?

Participant: I told them to fire again. Two shorts in a row, statistically we were about due to get one on target, and a full re-lay eats time we didn't have with the window closing.

Interviewer: What did that third round do?

Participant: Also landed short. Turned out later there was a leveling error on the gun that had nothing to do with the first two rounds—separate issue entirely. We caught it on the fourth check.

Interviewer: If the section chief had reported a confirmed fault after the first miss, would your third-round call have gone differently?

Participant: Probably, yeah. If there'd been a flagged fault I'd have stopped immediately for the recheck. Without one, I read the pattern as random scatter that would sort itself out on its own.

Interviewer: Let's move to the grid discrepancy. What information did you have?

Participant: Battalion JTAC—same battalion as me—called in Grid A for the staging activity. Almost at the same time, the partner-force liaison on our flank called Grid B, about three hundred meters away, similar confidence level in both reports, nothing that clearly outranked the other on paper.

Interviewer: How did you resolve that?

Participant: I went with Grid A, the JTAC's grid. It came through our own FSCC net, format I was used to, and honestly it's the source I'd worked with the whole deployment. The partner-force report came through a different relay and took longer to cross-check.

Interviewer: Did you request verification on Grid B?

Participant: Not before we acted on Grid A. Follow-on recon actually picked up some indicators near Grid B too, so it wasn't nothing—we just didn't chase it down at the time.

Interviewer: If the partner-force liaison's report had come through your own channel instead, do you think you'd have weighted it the same as Grid A?

Participant: Honestly, probably would've given it more credit. There's something about hearing it through your own net that makes it feel more solid, even if I can't point to a real reason the information itself was better.

Interviewer: Let's talk about the CAS run. What was the situation?

Participant: Pilot was on station, ready for a danger-close run supporting the compound clearance. We'd run several strikes with this same squadron over the deployment, all clean, standard margins, no issues. This time the friendly squad's position put us tighter than our usual margin, and we'd had a couple of comms dropouts with the lead squad in the minutes before.

Interviewer: What were your options?

Participant: Widen the margin, which meant delaying and possibly missing the window, or hold the comms until we got a stable check, versus just clearing it with the tighter margin we had.

Interviewer: What did you choose?

Participant: I cleared it hot with the tighter margin. This squadron had been reliable every time, so I expected it to go the same way.

Interviewer: What happened with comms during the final attack heading confirmation?

Participant: Dropped out again for about ten seconds. We got it back before the pilot needed the final call, so it worked out, but it was closer than I'd like on reflection.

Interviewer: If this had been the squadron's first-ever danger-close run with you, would you have set the same margin?

Participant: No. I'd have wanted the wider margin and a cleaner comms check. The history with them is what made the tighter margin feel acceptable.

Interviewer: Last decision point—the artillery mission on the compound.

Participant: Right before we committed the 155s, the ISR feed flagged one cue, "possible enemy activity" at the compound. That sector had been quiet the whole deployment, mostly normal village pattern-of-life, and that particular sensor had a track record of throwing false hits in that terrain.

Interviewer: What were the alternatives?

Participant: Get a second source to confirm before firing, given how quiet that area had been, or approve the mission off the one cue since the window was closing.

Interviewer: What did you decide?

Participant: I approved it off the single cue. We were inside the last few minutes before the assault, and the cue matched what we were looking for, so I went with it.

Interviewer: What did the post-strike assessment show?

Participant: Mixed. Some indicators of prior enemy presence, but also signs it might've been unoccupied by the time we fired. Inconclusive, honestly.

Interviewer: If the sector had a recent history of confirmed enemy activity, would that one cue have been enough on its own?

Participant: Probably would've felt the same either way at the time—I was focused on the cue itself, not really running the sector's track record against it.

Interviewer: Looking back across all four decisions, where do you think time pressure affected you most?

Participant: Probably the mortar rounds and the compound call—those felt the most rushed. The grid call and the CAS run felt more like judgment calls based on what I knew about the sources and the squadron.

Interviewer: Anything you'd do differently?

Participant: Maybe push harder for that re-lay check early, and get a second look at the compound cue. But given the clock we were working against, I think most FSOs would've made similar calls that day.

Interviewer: That's helpful. Thanks for walking through it in this much detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MD_Biased_4}}",
  "occupational_domain": "{{Military and defense operations}}",
  "role": "{{Fire Support Officer (FSO) / Joint Fires Observer}}"
}

TAXONOMY

This taxonomy distinguishes three aspects of work:

1. Task content: what the worker does.
2. Work methods: how the work is organised.
3. Tools: what machinery or technology is used.

Classify only categories supported by observable evidence. Multiple categories may be present. Select one primary content category and any defensible secondary categories. Do not force a category when evidence is insufficient.

A. TASK CONTENT — WHAT THE WORKER DOES

A1. PHYSICAL TASKS

A1.1 Strength
The worker exerts physical force or effort, handles loads, pushes, pulls, lifts, carries, restrains, or uses bodily strength as a meaningful part of the task.

A1.2 Dexterity
The worker performs precise, coordinated, or fine-grained physical movements, manipulates objects or instruments, assembles, repairs, operates controls manually, or uses hand-eye coordination as a meaningful part of the task.

A1.3 Navigation
The worker physically moves through or around an environment, routes people or objects, or maintains orientation and position in a spatial setting as a meaningful part of the task.

A2. INTELLECTUAL TASKS

A2.1 Uncodified visual or auditory information processing
The worker interprets visual, auditory, or other perceptual information that is difficult to reduce to a fully explicit rule, including recognizing patterns, anomalies, conditions, or signals.

A2.2 Literacy
The worker reads, writes, composes, edits, interprets, or communicates using written language as a meaningful part of the task.

A2.3 Numeracy
The worker calculates, quantifies, estimates, compares numerical values, interprets numerical information, or reasons about proportions, probabilities, measurements, or financial quantities.

A2.4 Information search, retrieval, gathering, and evaluation
The worker seeks, retrieves, gathers, compares, verifies, filters, or evaluates information from records, people, systems, documents, observations, or other sources.

A2.5 Conceptualisation, learning, and abstraction
The worker forms concepts, learns from experience, generalises, diagnoses, explains relationships, builds mental models, applies abstract principles, or understands a system beyond the immediate facts.

A2.6 Creativity, planning, and resolution
The worker generates, designs, or adapts solutions to a problem; develops and compares possible courses of action; plans their implementation; anticipates dependencies or consequences; or resolves a novel, non-routine situation by combining information in an original or context-sensitive way. Planning counts when it involves organising a sequence of actions, timing, resources, contingencies, or dependencies toward a goal—not merely selecting or carrying out a routine next step.

A3. SOCIAL TASKS

A3.1 Serving and attending
The worker responds to another person's immediate needs, provides a service, receives requests, attends to a customer, patient, client, user, colleague, or member of the public, or manages an interaction aimed at assistance.

A3.2 Teaching, training, and coaching
The worker explains, instructs, demonstrates, trains, develops, mentors, or coaches another person.

A3.3 Selling and influencing
The worker persuades, negotiates, recommends, markets, advocates, manages expectations, seeks agreement, or attempts to influence another person's decision or behaviour.

A3.4 Managing and coordinating
The worker allocates work, coordinates people or activities, manages dependencies, sets priorities, resolves organisational conflicts, supervises, or aligns multiple stakeholders.

A3.5 Caring
The worker provides emotional, personal, health-related, protective, or welfare-oriented support in which attention to another person's condition or well-being is central.

B. WORK METHODS — HOW THE WORK IS ORGANISED

B1. AUTONOMY

B1.1 Latitude
The worker has discretion over objectives, priorities, timing, sequence, methods, or decisions. Classify low, moderate, or high only when the interview provides evidence about the worker's discretion.

B1.2 Control and monitoring
The worker's work is supervised, measured, audited, monitored, reviewed, or constrained by another person, policy, procedure, system, target, or formal approval process. Classify low, moderate, or high based on the strength and frequency of such control.

B2. TEAMWORK

Direct collaboration with co-workers or other actors to accomplish a shared task, exchange information, coordinate actions, hand off work, or reach a joint decision. Classify low, moderate, or high based on the worker's dependence on collaboration in the described episode.

B3. ROUTINE

B3.1 Repetitiveness
The same or highly similar actions, inputs, decisions, or outputs recur frequently.

B3.2 Standardisation
The task follows prescribed procedures, scripts, checklists, templates, rules, or consistent sequences.

B3.3 Certainty and response to unforeseen situations
Certainty refers to how predictable the relevant inputs, conditions, and consequences are. Response to unforeseen situations refers to how much the worker must handle exceptions, novelty, ambiguity, disruptions, or unexpected developments.

For this dimension, report both:
- certainty: low, moderate, high, or not_observable;
- unforeseen_response_requirement: low, moderate, high, or not_observable.

C. TOOLS — MACHINERY AND TECHNOLOGY USED

C1. Non-digital machinery
Analog or mechanical devices and machinery without meaningful digital control, sensing, computing, or networked information processing.

C2. Digitally enabled machinery
Machinery or equipment using digital control, sensors, software, automation, robotics, or networked digital systems. Classify the most specific supported subtype:

C2.1 Autonomous machinery or robots
The equipment performs meaningful operations with limited direct human control after initiation.

C2.2 Non-autonomous digitally enabled machinery
The worker directly operates or controls digitally enabled physical equipment.

C2.3 Basic ICT
Routine use of computers, smartphones, email, office software, standard databases, or basic digital communication and information systems.

C2.4 Advanced ICT or programming
Programming, data analysis, modelling, system configuration, advanced computational tools, or complex software-based information processing.

C2.5 Specialised ICT
Special-purpose professional software or digital systems used for a particular occupation or work process, where the system is more specialised than ordinary office or communication software.

C2.6 Other digitally enabled tools
Digital tools that clearly matter to the work but do not fit the preceding subcategories.

CLASSIFICATION RULES

1. Classify the described episode, not the entire occupation.
2. A category must have textual evidence. Do not infer it from the role title.
3. Assign one primary task-content category: the category most central to the operational objective and decision episode.
4. Assign secondary content categories only when they are substantively involved, not merely mentioned.
5. Content categories may come from different families. For example, an interview may contain intellectual information evaluation as primary content and social influencing as secondary content.
6. Methods and tools are separate from content. Do not label a task intellectual merely because it uses a computer, or social merely because other people are mentioned.
7. Distinguish information search/evaluation from conceptualisation: the former concerns obtaining and assessing information; the latter concerns forming models, diagnoses, abstractions, or generalisations.
8. Distinguish creativity/resolution from ordinary choice: creativity requires adaptation, novel solution generation, or non-routine problem resolution.
9. Distinguish serving/attending from selling/influencing: assistance and responsiveness are not necessarily persuasion or negotiation.
10. Distinguish managing/coordinating from teamwork: teamwork is collaboration; managing/coordinating involves organising dependencies, priorities, people, or activities.
11. Do not infer strength, dexterity, navigation, or caring without direct evidence.
12. For autonomy, monitoring, teamwork, repetitiveness, standardisation, and certainty, use `not_observable` when the interview does not support a reliable level.
13. Multiple tools may be present. Record only tools that play a meaningful role in the episode.
14. If a classification is ambiguous, record the competing categories and explain the ambiguity.
15. Do not treat the participant's cognitive bias, if any, as a task category.
16. Do not use external web research. The supplied taxonomy is the authority for this annotation.

EVIDENCE REQUIREMENTS

For every assigned content category, method level, and tool category, provide:
- a short quotation or faithful text span;
- the location, such as opening, timeline, decision point, or participant turn;
- an explanation of why the evidence supports the category;
- confidence from 0 to 100.

For categories not observed but potentially plausible, do not list them as present. Place them in `not_observed_or_insufficient` only if doing so helps explain a material ambiguity.

COVERAGE STATUS

Set `coverage_status` as follows:
- `complete`: the interview contains enough evidence to classify content, methods, and tools;
- `partial`: at least one major dimension is not observable;
- `ambiguous`: competing categories cannot be resolved from the text;
- `insufficient`: the interview does not contain a sufficiently identifiable work episode.

OUTPUT SCHEMA

{
  "taxonomy_version": "Fernandez-Macias_Bisello_2021",
  "interview_id": "...",
  "occupational_domain": "...",
  "role": "...",
  "classification_confidence": 0,
  "coverage_status": "complete|partial|ambiguous|insufficient",
  "content": {
    "primary_category": {
      "family": "physical|intellectual|social|unknown",
      "subcategory": "...",
      "confidence": 0,
      "evidence": [
        {
          "location": "...",
          "quote": "...",
          "explanation": "..."
        }
      ]
    },
    "secondary_categories": [
      {
        "family": "physical|intellectual|social",
        "subcategory": "...",
        "confidence": 0,
        "evidence": [
          {
            "location": "...",
            "quote": "...",
            "explanation": "..."
          }
        ]
      }
    ],
    "all_observed_categories": [],
    "not_observed_or_insufficient": [],
    "ambiguities": []
  },
  "methods": {
    "autonomy": {
      "latitude": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "control_monitoring": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      }
    },
    "teamwork": {
      "level": "low|moderate|high|not_observable",
      "confidence": 0,
      "evidence": []
    },
    "routine": {
      "repetitiveness": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "standardisation": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "certainty": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "unforeseen_response_requirement": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      }
    }
  },
  "tools": [
    {
      "category": "non_digital_machinery|autonomous_machinery_or_robot|non_autonomous_digitally_enabled_machinery|basic_ict|advanced_ict_or_programming|specialised_ict|other_digitally_enabled_tool",
      "role_in_task": "...",
      "confidence": 0,
      "evidence": [
        {
          "location": "...",
          "quote": "...",
          "explanation": "..."
        }
      ]
    }
  ],
  "task_anchors": [
    {
      "location": "...",
      "task_description": "...",
      "taxonomy_labels": [],
      "confidence": 0
    }
  ],
  "decision_point_task_map": [
    {
      "decision_point": 1,
      "dominant_task_categories": [],
      "methods_relevant": [],
      "tools_relevant": [],
      "evidence": []
    }
  ],
  "classification_quality": {
    "occupation_inference_risk": "low|moderate|high",
    "stereotype_risk": "low|moderate|high",
    "taxonomy_ambiguity": "low|moderate|high",
    "missing_evidence": [],
    "manual_review_recommended": false
  },
  "coverage_flags": {
    "physical_content_observed": false,
    "intellectual_content_observed": false,
    "social_content_observed": false,
    "methods_observed": false,
    "tools_observed": false,
    "all_major_dimensions_observable": false
  },
  "recommended_dataset_action": "retain|retain_with_low_confidence|sample_more|manual_review|exclude"
}

FINAL CHECK

Before returning JSON, verify that:
- Every present category has textual evidence.
- The primary category is central to the episode, not merely the most frequently mentioned word.
- Secondary categories are substantively involved.
- Method and tool labels are supported independently from content labels.
- `not_observable` is used where appropriate.
- Confidence reflects evidence quality, not certainty from the occupation or role.
- No cognitive-bias labels appear as task categories.
- No external sources or unstated occupational assumptions were used.
- The result is valid JSON and contains no prose outside the JSON object.
