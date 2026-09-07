You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operational learning file, not a disciplinary review — you can decline any question. Can you state your role and how long you've been in it?

Participant: Sure. I'm shift captain on nights, been supervising underground crews about nine years, this site for four. Before that I was a ground control tech, so I came up through that side.

Interviewer: Good. Let's start broad — walk me through what you knew at the start of the shift, before anything unusual happened.

Participant: Standard handover. Day shift left a note that there'd been a small seismic event overnight near Panel 3, magnitude around 1.1, logged as minor, within normal range for that ground. They also flagged some wet ground near the access drift — more seepage than usual, nothing alarming on its own. Production schedule had us blasting Panel 3 within the first couple hours, and mucking and haulage after that. That was the plan.

Interviewer: What was the main objective for the night?

Participant: Keep Panel 3 on schedule. We were behind for the week, so there was some pressure from the surface to not lose another shift. Safety first, obviously, but the blast cycle was already tight.

Interviewer: Take me through the incident itself, in order.

Participant: Okay. First couple hours were the blast — I authorized it after the ground control tech did a visual pass, no visible loose rock, so we went ahead as scheduled. Didn't call for an instrumented convergence check, just a visual scaling look, because the seismic event had been small and logged as normal range. Blast went fine, mucking started.

A while after that, microseismic monitoring started showing a cluster of small events near the panel next to our old mined-out area — not bigger events, just more of them, more frequent. Haul trucks run a road that passes under part of that adjacent panel, so I had to decide whether to keep hauling that route. Ventilation was reading normal across the circuit, no gas issues reported, so I let haulage continue as-is.

About fifteen minutes after trucks started moving again, a methane sensor near that haul intersection logged a brief spike, then went back to baseline. Ventilation officer logged it as transient, no recurrence, didn't think much of it at the time — that kind of blip happens.

Then we got the fall of ground. Small one, near the haul intersection, damaged a section of mesh, no injuries, but it needed re-support before we could keep running trucks through there.

Interviewer: When that happened, what did you think was going on?

Participant: Honestly, by that point it felt pretty clear. You had the seismic event overnight, the wet ground, then the seismic cluster building up near the old workings, plus the blast vibration from our own cycle — it all lined up. Stress transfer off the old mined-out panel, aggravated by the water getting into the joints and then our blast adding vibration on top. Once you saw it laid out like that, it made sense — it was almost the story you'd expect given that ground history.

Interviewer: And the methane spike from earlier?

Participant: That I set aside. It didn't fit with a ground stability event — different system, different sensor, and it hadn't recurred. Ventilation had already called it transient. I didn't loop back on it specifically once we had a ground explanation that accounted for everything else.

Interviewer: Let's go back through each decision point one at a time. Starting with the blast authorization — what alternatives did you weigh?

Participant: Three options really. Go ahead with just the visual check, delay and call for an instrumented geotech inspection, or go ahead but scale back charge size and add scaling time as a buffer. I went with the first. The seismic event was classified minor, the tech didn't see loose rock, and we were already behind schedule.

Interviewer: What cues mattered most there?

Participant: The classification on the seismic log, mostly. "Minor, within normal range" carries weight — that's the geotech team's own threshold, not something I'm second-guessing casually.

Interviewer: Any uncertainty at that point?

Participant: Some. The wet ground note nagged at me a little, but on its own it's common enough that shift.

Interviewer: Second decision — continuing haulage under the adjacent panel despite the seismic cluster.

Participant: I considered rerouting the trucks, or halting until the geotech engineer looked at the cluster. But it was frequency increasing, not magnitude — that pattern is something I've seen before near old workings settling out. Ventilation was clean. Given the schedule pressure, I let it continue.

Interviewer: Whose input did you lean on there, and whose didn't you seek?

Participant: Leaned on the ventilation officer's readings. Didn't call the on-call geotech engineer — he's not on-site overnight, and I judged the cluster wasn't urgent enough to wake him for.

Interviewer: Third — the fall of ground and the remediation decision. What alternatives existed?

Participant: I could've treated the cause as undetermined and ordered an instrumented investigation of both the ground and the gas anomaly before deciding on re-support. Or gotten the geotech engineer's real-time input before committing to any explanation. Instead I went with the stress-transfer account and had the crew re-support directly on that basis.

Interviewer: What made that explanation feel solid enough to act on without waiting for engineering input?

Participant: It tied together everything we'd seen that night in one line — the timing worked, the location worked, the mechanism was one I understood from my ground control days. When it clicks together that cleanly, you don't feel like you're guessing anymore.

Interviewer: Did anything not fit that account?

Participant: The methane spike, technically. But it was a single blip, different monitoring system, already logged as transient. It didn't feel like it belonged in the same picture as a ground support issue.

Interviewer: Fourth decision — resuming production after re-support.

Participant: Re-support was done, no new seismic or gas readings since the FOG, and we were losing more schedule the longer we sat. I could've resumed limited production with continued monitoring, or suspended the panel until formal sign-off. I resumed full production. The explanation held together and the repair was solid, so I didn't see a reason to hold back further.

Interviewer: How confident were you in the cause at that point, on reflection?

Participant: Pretty confident in the moment. Looking back, I'll admit the geotech engineer wanted the raw seismic and gas data before he'd sign off on it as the definitive cause — he mentioned it could also be a localized joint failure or even sensor drift, unrelated to the stress-transfer idea entirely.

Interviewer: What information, if you'd had it earlier, might have changed your read?

Participant: Probably the engineer's data review itself, before we committed to re-support. If that had flagged the methane sensor as a calibration issue right away, or ruled out joint failure, I'd have felt more sure. Without it, I was working off what fit together in front of me.

Interviewer: If the methane spike had recurred a second time that night, would that have changed anything?

Participant: Yeah, I think so. A repeat would've been harder to wave off as unrelated. One blip is easy to set aside; two starts looking like its own problem.

Interviewer: Looking back, what part of your explanation are you least sure about now?

Participant: Whether the stress transfer story was really the whole cause, or just the part that was easiest to see. The pieces fit together well enough that I didn't push hard on what didn't fit.

Interviewer: What would you tell a newer supervisor facing a similar sequence?

Participant: That a clean-sounding explanation isn't the same as a confirmed one — get the data checked even when the story already feels complete.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MU_Biased_1}}",
  "occupational_domain": "{{Mining and underground industrial operations}}",
  "role": "{{Underground Shift Supervisor / Mine Captain}}"
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
