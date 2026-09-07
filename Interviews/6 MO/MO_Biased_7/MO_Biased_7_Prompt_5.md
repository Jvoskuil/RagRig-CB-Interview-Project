You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. As explained, this is a confidential debrief to understand the reasoning behind decisions during the cargo transfer alongside the platform last month — not a disciplinary review. Anything you share helps refine our procedures. Are you comfortable proceeding?

Participant: Yes, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by describing your role on that job?

Participant: I was the DPO on watch, running station-keeping in DP2 mode while we did a scheduled cargo transfer — deck cargo and some bulk — to the platform. Normally that's a fairly routine job. We hold position off the leg, crane operator on the platform takes the lifts off our deck, and we just maintain the watch circle until it's done.

Interviewer: And what made this particular job different, if anything?

Participant: Weather was closing in faster than the forecast suggested first thing that morning. We had maybe a four-hour window before significant wave height would push past the platform crane's operating limit. So there was a bit more time pressure than usual, but nothing outside normal parameters when we started.

Interviewer: Take me through what happened, from approach onward.

Participant: On final approach, I noticed a discrepancy between the HPR and one of the DGPS units — about 1.8 meters. DGPS1 and DGPS2 were agreeing closely with each other, and the system had auto-weighted those two into the primary solution, showing green across the board. HPR didn't have any maintenance flag against it, but given the other two were lined up, I read the HPR number as the odd one out and carried on with the approach. We got alongside, started the transfer, cargo went smoothly for the first several lifts. About halfway through — call it 55% of the load transferred — Thruster 3 threw a yellow caution, reduced power availability. Consequence analysis still showed adequate capability, so I kept going in the same configuration. Superintendent called in around then too, just a reminder about the transit schedule afterward. Later, on the second-to-last lift, there was a wind shift that changed the footprint plot recommendation. I was heads-down on the crane boom position at that point, watching the load come across, and I didn't clock the footprint change until the Master mentioned the vessel's attitude had shifted. Checked afterward — the indicator had been sitting there on the secondary screen the whole time. Then for the last lift, OIM asked if we could finish or wanted to stand off. I told him we were maybe eight to ten minutes out, so we pushed on. Partway through that final lift our separation from the leg closed up more than I expected, and we ended up suspending early and backing off to a safer distance. No contact, no loss of position beyond the watch circle, but closer than I'd have liked.

Interviewer: Let's reconstruct that in order. What were you actually monitoring at each stage?

Participant: Early on, reference systems and the DP status page — standard for closing distance. Once we were alongside and lifting, my attention split between the crane display, thruster status, and periodic checks of the environmental trend. As the job went on, honestly, more of my attention shifted toward the crane display than the DP overview, especially in that last third.

Interviewer: Let's go back to the reference discrepancy. Walk me through your decision process there.

Participant: DGPS1 and DGPS2 agreed within normal tolerance, HPR was off by 1.8 meters, no fault logged on it. Two out of three lined up, and once I'd settled on the DGPS pair as the good solution, I didn't see much point going back into the HPR trace since it was just going to keep disagreeing with a picture I'd already accepted. So I proceeded on that basis.

Interviewer: Did you do anything to independently check which reference was actually correct, beyond the system's selection?

Participant: Not really — the pairing agreed and the status was green, so I didn't dig into the raw HPR trace further at that point. In hindsight the offset was a multipath effect from being close to the structure, so HPR wasn't actually wrong, but at the time the two-out-of-three read as good enough.

Interviewer: What would have made you look harder at that discrepancy?

Participant: If the DGPS units had disagreed with each other too, I'd have stopped and manually cross-checked before closing in. It was really the agreement between the two that settled it for me.

Interviewer: Now the thruster caution at the halfway point — what went into staying in the same mode?

Participant: The consequence analysis still showed us within capability, so procedurally there wasn't a hard requirement to change anything. We'd already gotten through a bit more than half the cargo, and the weather window was closing, so stopping to reassess felt like it would cost us more than it bought us at that stage.

Interviewer: Did you consider switching to a more conservative setup — tightening the watch circle, adjusting reference weighting — rather than continuing exactly as before?

Participant: Not actively, no. It wasn't red, so it didn't really register as something requiring a change in how we were running things. We'd been in that configuration all shift and it had been fine.

Interviewer: Move to the final lift and the footprint change. What was pulling your attention at that point?

Participant: The crane boom, almost entirely. That's the highest-consequence thing to watch during an active lift — if the load swings or the boom's position goes wrong, that's an immediate hazard. Checking the footprint plot is normally part of the scan during a lift like that, and the co-operator was on the bridge and could have picked it up, but with only one lift left I figured it was quick enough that it didn't need pulling him off what he was doing to specifically watch environmental trends. The footprint indicator itself is a visual cue only, no audible alarm tied to it, so it's easy for it to sit there unnoticed if you're not specifically glancing over.

Interviewer: What would have changed that — would delegating the environmental watch to your co-operator have helped?

Participant: Probably, yes. We didn't explicitly split that responsibility during the lift. In hindsight that would have been the more robust setup.

Interviewer: Last one — the OIM's question about finishing the final lift. What did you weigh in your answer?

Participant: Mainly the time — eight to ten minutes to complete it, and the equipment status hadn't escalated past caution level. So I told him we were good to finish rather than framing it around how much margin we actually had left, which by that point had narrowed more than I'd tracked.

Interviewer: At that moment, did you actually have the separation and capability numbers available to answer in terms of margin instead of time, or was that information harder to pull together?

Participant: It was there if I'd called it up — separation, remaining thrust reserve, all on the DP overview. But the eight-to-ten-minute figure was just quicker and more concrete to give the OIM, and once I'd framed it that way in my head, finishing felt like the obvious answer. If I'd led with the margin number instead, I think it would have looked like a less comfortable call.

Interviewer: Looking back at that sequence overall, do you think there were earlier indications of how close things got at the end?

Participant: Looking back, yes — the reference offset and the thruster caution together were quietly eating into our margin the whole time, and honestly it feels like it should have been fairly obvious that was building toward something. In the moment, though, neither one individually crossed a threshold that flagged it.

Interviewer: If you were advising a newer DPO going into a similar job, what would you tell them to watch for?

Participant: Don't let a green status or a majority agreement between references close the door on checking the outlier. And separate out who's watching the environmental picture versus the load, especially late in a job when you're tired and task-focused.

Interviewer: Anything you'd do differently if this came up again?

Participant: I'd probably reassess capability actively at the first caution rather than just confirming it was still within limits, and frame those late-stage go/no-go calls around remaining margin rather than remaining minutes. Otherwise the job itself was manageable — we just let a few small things ride longer than we should have.

Interviewer: That's really helpful detail. Thank you for walking through it so thoroughly.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MO_Biased_7}}",
  "occupational_domain": "{{Maritime Operations}}",
  "role": "{{Dynamic Positioning Operator (Offshore Support Vessel)}}"
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
