You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. This is being recorded for a training-review case study, your name won't be attached to the write-up, and you can skip anything you'd rather not answer. That work for you?

Participant: Yeah, that's fine. I've sat through a few of these for the sergeant's after-action reviews before.

Interviewer: Good. What's your role, and how long have you been doing patrol work?

Participant: Patrol officer, field response, seven years now. Nights mostly the last three.

Interviewer: Let's start with the incident. Walk me through it from the top.

Participant: Sure. About 2:05 in the morning, dispatch got an anonymous call about a vehicle idling suspiciously near the loading dock at the distribution warehouse off Route 12. Caller didn't give a vehicle description, nothing about occupants, no specifics at all. That area's had a run of cargo theft the last couple months, so it's a place we keep an eye on anyway. I was closest unit, backup was a few minutes out. I rolled up, parked back a bit instead of pulling right up on the dock, and watched for a minute. Saw one guy standing next to a parked pickup truck near the dock, looking at a clipboard. Nothing dramatic—no forced entry, no tools out, nothing urgent-looking.

Interviewer: What made you hold back and observe instead of approaching right away?

Participant: Habit, really. If somebody's actually up to something, walking straight up tips them off before you get a read on them. He wasn't doing anything that needed immediate action, so there wasn't a reason to rush it.

Interviewer: Okay, so you approach. What happens next?

Participant: I get out, identify myself, ask what he's doing there. He's calm, looks right at me, answers straight away—says he's a contracted HVAC tech waiting on the site manager to let him in for a scheduled after-hours repair. Shows me a contractor badge clipped to his jacket, hands over his license without me asking twice. While we're talking I notice a bulge in his coat pocket, kind of squared off, hard to tell what it is.

Interviewer: What did you do with that?

Participant: I asked him to keep his hands visible while I thought it through. He's calm, cooperative, story's consistent, paperwork on the clipboard lines up with an HVAC job—that all counts for something. But I still don't know what's in that pocket, and an unidentified object at two in the morning, alone, isn't something I can just wave off because the guy seems relaxed. So I weighed it as: the demeanor and the story lower the odds it's a problem, but they don't rule it out, and the bulge is still an open question either way. Ended up doing a brief pat-down, but I told him why—said something like, "you seem fine, but I've got to check this."

Interviewer: Let's build the full timeline before we go decision by decision. What happened after the pat-down?

Participant: Clean. Bulge was a folded work order and a multimeter. No weapon. His story still wasn't independently confirmed though, and backup hadn't shown up yet, so I had him stay put while dispatch checked whether the HVAC company actually had a work order with that warehouse for that night. Came back a few minutes later—yes, active account, scheduled after-hours repair, all legitimate. Site manager showed up right around then to let him in. I released him, wrote up the field contact, noted the pat-down and why, and that was it.

Interviewer: Let's go through it decision by decision. First: choosing to observe before approaching. What alternatives did you weigh?

Participant: I could've walked right up, or called dispatch back for more detail first. Calling back didn't seem worth it—the caller hadn't given much to work with anyway. Watching first gets me information without giving up the advantage of him not knowing I'm there yet.

Interviewer: Second—the pat-down decision. How did the calm demeanor and the pocket bulge actually factor together into that call?

Participant: Pretty directly, honestly. The demeanor mattered—if he'd been jumpy or wouldn't look at me, I'd have treated the bulge as a lot more urgent and probably backed off to wait for backup before getting that close. Since he was calm and the story checked out on its face, that brought my concern down some. But it didn't erase it, because none of that tells me what's actually in his pocket. So both things were in the mix—the calm cuts one way, the unidentified object cuts the other, and I made the call knowing neither one fully resolved the other.

Interviewer: Did the subject's explanation change how you saw the bulge?

Participant: Some. Once he mentioned the work order and the multimeter before I even patted him down, I had a guess what it probably was. But "probably" isn't the same as confirmed, so I still checked.

Interviewer: If he'd been visibly nervous instead of calm, would that have changed things?

Participant: Yeah, I'd have been quicker to create distance and wait on backup rather than getting in close for a pat-down solo. Nervousness plus an unknown object is a different risk picture than calm plus an unknown object.

Interviewer: And if there'd been no bulge at all, same calm demeanor, same story?

Participant: Then there's nothing physical to check. It'd just be a field interview, verify the story, and let him go once it holds up.

Interviewer: Third decision point—after the pat-down's clean, you keep him at the scene instead of releasing him right away. Why?

Participant: The story wasn't verified yet. Badge and ID looked legit, but I've seen contractor badges that were expired or from a job somebody didn't actually have anymore. Backup still hadn't arrived. Holding him a few extra minutes for dispatch to confirm the work order felt like the reasonable middle ground—not cutting him loose on an unconfirmed story, but not treating him like a suspect either.

Interviewer: Did you consider escorting him to the site office instead?

Participant: Thought about it, but the office was locked, nobody there to answer. Waiting on dispatch and the site manager made more sense than walking him around the property in the dark.

Interviewer: Fourth—closing it out. Why release with no citation instead of a trespassing warning?

Participant: Once dispatch confirmed the work order and the site manager showed up right after, there wasn't a factual basis left for a citation. He had a legitimate reason to be there, and it held up. Writing him up at that point would've just been penalizing him for being at his own job site.

Interviewer: What single piece of information, if it had come in earlier, would have changed how you handled this?

Participant: Honestly, if dispatch had been able to confirm the work order before I even got out of the car, most of this would've been a formality. The whole thing hinged on not having that confirmation up front.

Interviewer: How much did being alone without backup shape your pace?

Participant: Some. I moved a little more carefully closing distance, and I was more inclined to resolve the pocket question myself rather than just let it sit unanswered while I waited.

Interviewer: Looking back, is there anything you'd weigh differently next time?

Participant: Not really. I think I got the balance about right—gave the calm and the story their due, but didn't let them talk me out of checking something I genuinely couldn't identify. That's about as fair as you can be with limited information at two in the morning.

Interviewer: That's helpful, thank you. I think that covers everything I need.

Participant: No problem. Glad it worked out clean for him.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{LE_Vocab_Control_1}}",
  "occupational_domain": "{{Law enforcement}}",
  "role": "{{Patrol Officer (Field Response)}}"
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
