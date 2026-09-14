You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for sitting down with me. As discussed, this is for our post-incident learning review, not a disciplinary process — I want to understand how you saw and processed the situation as it developed. Anything you share stays within the review process. You good to start?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role and a bit about your background before we get into the incident itself?

Participant: I'm the on-shift Incident Commander for the site brigade — I've been in this role about six years, twelve years on the brigade total. Mostly hydrocarbon and solvent handling areas, so tank farm fires aren't unfamiliar to me.

Interviewer: Good. So walk me through what you saw and were told when you arrived on scene.

Participant: Control room paged it as a flammable liquid tank fire in the solvent storage area, described as contained, dark smoke visible. When I pulled up, I had a heavy black column coming off one of the four tanks in the bunded area. Wind was light, shifting a bit, not pushing smoke hard in any one direction. Visually it looked almost identical to a fire we had three years back in the same general area — same kind of column, same rough intensity. That one we knocked down clean with an offensive foam attack, crews in with exposure lines, no real drama. So my first read was, this looks like that one.

Interviewer: What was your main objective at that point?

Participant: Get the fire knocked down before it could threaten the second tank or the production building next door, and do it without losing anybody. Standard priorities — life safety, then stabilize, then protect property.

Interviewer: And the manifest — did you know exactly what was burning?

Participant: Not confirmed yet, no. Four tanks in that bund, different products, and hazmat hadn't given me a firm ID. But the call came through as contained, and visually it read the same as the one I already knew how to fight, so I went with what I had. Honestly, hearing it called contained made it sound like it was staying inside the kind of tank fire we handle all the time — so getting the manifest nailed down didn't feel like something I had to sort out before we started moving lines in.

Interviewer: Let's reconstruct the sequence phase by phase. What happened right after you made that initial call?

Participant: I committed two crews in with foam lines and set exposure protection on the neighboring tank. Shortly after that, hazmat got on scene and told me the burning tank actually held a more volatile mix than the one from that earlier fire — different product entirely, just looked similar from the outside. By then the lines were already in and crews were positioned close, maybe fifteen meters off the shell.

Interviewer: How did that change your read of the situation?

Participant: It should have, and it registered, but we were already committed at that point. Pulling two charged lines and repositioning crews mid-attack isn't something you do lightly — there's real risk in that movement itself. So the plan stayed as it was; we didn't stop and rebuild the IAP around the new information, we just kept pushing the attack we'd already started.

Interviewer: Let's stay on that moment. What options did you actually weigh once you had the shell temperature alarms rising?

Participant: Either pull back to a defensive perimeter and go to unmanned monitors, or hold position and add a second foam line for more knockdown. We'd only really sat down and reviewed the plan once, right at the start. Nothing after that forced a formal stop-and-reassess — no single trigger big enough on its own — so we just kept executing what we'd already briefed. Looking back, the volatile-product call and the climbing temperature together probably should have been enough to warrant a fresh look, but since nobody formally called for a stop, we treated that as reason enough to keep running with the plan we already had.

Interviewer: What told you to add the second line rather than withdraw?

Participant: Partly the alarms themselves, wanting more suppression on the seat of the fire. But honestly, part of it was that we already had people and hose in position — pulling that back felt like giving up ground we'd already paid for in terms of setup time and risk getting in.

Interviewer: Understood. Let's move to the next phase. What was happening on the radio and at your command post around this time?

Participant: The mutual aid engine companies were on our shared channel, and a couple of their officers came on saying it looked like a standard tank fire, keep pushing the interior attack. Multiple voices, same read. At the post, our safety officer raised a concern about how close our crews were sitting relative to the second tank's exposure. We talked about it for maybe a minute.

Interviewer: How was that concern handled?

Participant: We acknowledged it, but the room moved fast — everybody sort of nodded that we were fine to continue, and we didn't really dig into it past that. It wasn't dismissed outright, it just didn't get a long conversation before we moved on.

Interviewer: Once the group had nodded along, did anyone go back and test the safety officer's concern more directly?

Participant: Not really. Nobody asked him to lay out specifically what he was seeing or walk us through why he thought the exposure risk was higher than we'd assessed. No one was assigned to argue the other side or double-check it. Once the room had settled on continuing, it just didn't come back up.

Interviewer: Did the mutual aid officers' agreement factor into your decision?

Participant: Yeah, some. When you've got multiple experienced officers on the net independently saying the same thing, that carries weight. It reinforced that we were reading the incident the way most people out there were reading it.

Interviewer: What came in right after that?

Participant: A relief crew came off shift and mentioned they thought they saw the second tank shell bulging slightly, maybe some vibration. Nothing measured, just an observation.

Interviewer: Let's go to the final phase. What did the data look like as you approached the withdrawal decision?

Participant: We'd had a shell temperature trend on that second tank climbing steadily for about twenty minutes, radioed in multiple times, consistent rise. Then right at the point where I was deciding whether to call full withdrawal, a spotter came on and said it looked stable now, based on a quick visual check.

Interviewer: How did you weigh those two things against each other?

Participant: The spotter's call was the most current thing I had in my ear at that exact moment, so it carried real weight in the decision. I held off on ordering the full pull-back a bit longer than the trend alone probably would have justified, because that last report suggested things had settled.

Interviewer: How confident were you in that spotter's assessment versus the trend data?

Participant: Reasonably — he's experienced, and a visual read from someone right there has value the instruments don't always capture. But looking back, that trend had been consistent for twenty minutes, and one quick look doesn't necessarily overturn that.

Interviewer: What ended up happening?

Participant: The tank vented on its own, no rupture, nobody hurt. Fire was knocked down maybe forty minutes after that. Could've gone worse; can't say for certain the timing of withdrawal is what mattered most.

Interviewer: Looking back, if the hazmat report on tank contents had come in before you committed crews, would your first call have gone differently?

Participant: Possibly — I might have held the lines back until we confirmed exactly what we were dealing with rather than moving straight to the offensive attack.

Interviewer: And if the mutual aid officers on the net had been split or silent at that middle phase, do you think the outcome there changes?

Participant: Maybe. Without that agreement, the safety officer's point might have gotten more airtime, and we might've paused longer before continuing.

Interviewer: Last one — what single piece of information do you wish had carried more weight at the very end?

Participant: The twenty-minute trend, honestly. It was right there the whole time. I let one fresh comment outweigh a much longer pattern that had already told a consistent story.

Interviewer: Appreciate you walking through all of that in detail.

Participant: No problem. It's useful to go back over it like this.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HE_Biased_7}}",
  "occupational_domain": "{{High-risk Engineering and Fire Engineering}}",
  "role": "{{Emergency Response/Incident Commander (Industrial Fire Brigade)}}"
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
