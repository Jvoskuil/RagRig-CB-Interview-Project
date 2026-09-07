You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for taking the time. Just to confirm before we start — this is a routine cognitive task analysis interview, not an investigation. Nothing you say here goes into a disciplinary file, and you can decline any question. Comfortable to proceed?

Participant: Yeah, that's fine, happy to go through it.

Interviewer: Great. Can you tell me your role and how long you've been controlling this branch?

Participant: I'm a Rail Traffic Controller, six years on this desk, mostly overnight and weekend turns. I cover the Falcon Bank branch pretty regularly — it's single line, absolute block working, so only one train in the section at a time.

Interviewer: And what's a normal possession handback look like on a section like that?

Participant: Gang foreman calls in on the trackside telephone, confirms the line's clear of personnel and equipment, I log the time, and then it's back to normal working. Nothing unusual about that part.

Interviewer: Walk me through what actually happened that night.

Participant: Handback came through at 23:40, all routine. I had 6M42, a freight, sitting at the entry signal waiting for the road, and 2T19, a passenger service, running about eighteen minutes late further up the line. Objective was simple enough — get 6M42 through Falcon Bank and get 2T19 back on time without anyone sitting in a queue longer than they needed to. Shortly after the handback, the track circuit for the section showed occupied for about four seconds, then cleared. It did that twice in ten minutes. Light rain had just started.

Interviewer: What went through your mind when you saw that?

Participant: Honestly, my first thought was "here we go again." That circuit's had three nuisance trips in the last eight months, all rain or leaf-fall related, all logged. So I looked at it and thought, that's the same signature — short blip, self-clears, no correlation with anything physically on the track. It fit the pattern well enough that I didn't feel I needed to chase it further.

Interviewer: What alternatives did you actually have at that point?

Participant: I could've rung the foreman again on the trackside phone to get him to re-walk it, or got the on-call technician out to test the circuit, or gone to pilotman working as a precaution. All were on the table.

Interviewer: What made you choose to just proceed?

Participant: The pattern, mostly. Three prior trips, same weather trigger, same short duration. It read like the circuit doing its usual thing. Calling the foreman back would've meant holding 6M42 another ten, fifteen minutes for what I was fairly confident was nothing, and pilotman working is even longer than that to arrange. Once I had it slotted into that nuisance-trip bucket in my head, verifying it didn't feel like it was really adding anything — I'd already accounted for it, if that makes sense.

Interviewer: How confident would you say you were, on reflection, that it was genuinely just the nuisance trip and not something else?

Participant: At the time, quite confident — enough that I didn't feel the need to build in a check. Looking back, I suppose I treated it as basically closed rather than just "probably fine but still open." I gave 6M42 the road.

Interviewer: What happened next?

Participant: 6M42 entered the section, and for a few minutes everything was quiet — no more flickers, so it looked like a good call at that point. Then the foreman came back on the radio to do his readback, confirming the gang and equipment were fully clear, but the transmission was garbled by static. I caught "clear" and something like "trolley," but it wasn't a full clean readback.

Interviewer: What were your options there?

Participant: Accept it as good enough since the formal handback had already happened before that call, try to re-raise him for a clean repeat, or ring my supervisor to get a second opinion on whether a partial transmission was adequate.

Interviewer: Which did you go with, and why?

Participant: I logged it as adequate. The handback itself was already formally done and clean at 23:40 — this was just the follow-up readback, and the gang was already moving off to their next job, so re-contacting wasn't straightforward. No rule had actually been broken; the section was already possession-free by the book. It felt like a reasonable judgment call given what I had, not a great one, but reasonable.

Interviewer: Then what?

Participant: Weather got worse. Rain picked up, and a junction signal further along — separate from Falcon Bank — started throwing intermittent signal failure warnings. 2T19 was approaching that junction and needed a routing call within a couple of minutes.

Interviewer: What were you weighing there?

Participant: Send it through on the affected signal relying on backup indication and the driver's caution, divert it onto the loop line which adds six minutes, or hold it at the previous station until the fault's diagnosed. Meanwhile 6M42 was still moving through Falcon Bank fine, no further anomalies.

Interviewer: What did you decide?

Participant: I sent 2T19 round the loop. That signal issue felt different in character — a live "failure" warning rather than a short clean blip — and I didn't have any history on that particular fault to lean on, so I wasn't willing to trust backup indication on an unfamiliar problem. Six minutes felt like a cheap price for not gambling on something I hadn't seen before.

Interviewer: Interesting that you treated that one differently to the Falcon Bank flicker.

Participant: Yeah — I didn't have a pattern to fall back on there, so holding back felt like the safer default. Turned out to be an unrelated relay fault, nothing to do with Falcon Bank at all, but I didn't know that at the time.

Interviewer: What happened after that?

Participant: The Falcon Bank circuit flickered again — same kind of brief occupied indication — but this time 6M42 was confirmed still inside the section. I finally got hold of the on-call technician, who told me the circuit's wiring has a known moisture-sensitivity problem that's never been fully run down. Driver of 6M42 reported nothing unusual, normal progress, no obstruction visible. And 2T19 was closing in behind, having rejoined the main line off the loop.

Interviewer: What options did you have at that point?

Participant: Carry on as normal and let 2T19 follow into Falcon Bank once clear, treating the second flicker the same way as the first. Suspend normal working and go to pilotman working for everything through that section until it's properly looked at. Or hold 2T19 short and get the technician to physically inspect before anything else moves.

Interviewer: What did you choose?

Participant: I went to pilotman working. Once the technician mentioned there was an actual unresolved wiring issue behind it, the flicker stopped feeling like the same closed case from earlier — it felt like there was something real and undiagnosed sitting underneath it, so I wanted a person physically controlling movement rather than relying on the circuit again.

Interviewer: Suppose everything else that night had stayed exactly the same — the weather, the maintenance log, the garbled readback, the junction fault, and how the wiring issue eventually turned out — but at that very first flicker you'd taken thirty seconds to ring the foreman back on the trackside phone before giving 6M42 the road. Do you think that changes anything about how you'd have gone into the rest of the night?

Participant: Probably, yeah. I still think the pattern would've weighed heavily either way — three prior trips is three prior trips. But if I'd made that one extra call and gotten a clean confirmation, I'd have gone into the rest of the shift with something on record rather than just my own read of the log. It wouldn't have changed the facts on the ground, but it might've meant I wasn't relying quite so much on the pattern doing all the work by itself.

Interviewer: Looking back, what would you change about the initial decision?

Participant: I'd probably still weigh the history heavily, but I think I'd want some cheap independent check alongside it rather than letting the pattern alone close the question. A quick call doesn't cost that much against holding a train.

Interviewer: What would need to change, procedurally, for you to verify faster next time?

Participant: Direct line to the technician's diagnostic panel instead of routing through the on-call rota — that delay probably shaped a couple of my later calls too.

Interviewer: Last one — how do you think a colleague would've handled that first flicker?

Participant: Honestly, most of the desk would've read it the same way I did. That log is well known on our shift. Whether that's the right instinct or not, I couldn't tell you for certain — nothing went wrong that night, but I know that doesn't prove it was the right call either.

Interviewer: That's a good place to stop. Thanks for your time.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{RT_Biased_1}}",
  "occupational_domain": "{{Rail Transportation}}",
  "role": "{{Rail Traffic Controller / Train Dispatcher}}"
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
