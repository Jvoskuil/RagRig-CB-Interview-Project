You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. As a reminder, this session is for the after-action cognitive review, not for attribution of blame—I just want to understand how decisions actually got made. That okay with you?

Participant: Yeah, that's fine. I've done these before.

Interviewer: Good. Can you start by giving me your role and what the mission was?

Participant: I'm the battalion S3 for the task force. Our mission was to secure and hold the Route BLUE crossing so brigade could push their main effort across within a 48-hour window. We had one Mobile Gap-Crossing Bridge, limited float capacity, and weather was closing in on our aerial ISR window. It mattered because if we didn't hold that crossing on schedule, brigade's whole synchronization plan slid.

Interviewer: Walk me through how the incident actually unfolded, start to finish.

Participant: Sure. About 48 hours out, S2 flagged enemy scout vehicles in a spot that didn't quite match what we'd been seeing—three months of pattern-of-life had them screening consistently off ridge NAI 12, and this sighting was lower, closer to the river. The vehicle types and rough timing matched what we'd tracked before, so it read to me like the same defensive template, and I didn't put much weight on the location itself. S2 actually noted that the river-side position wasn't really consistent with how that unit normally screened, but I still treated it as a variant of the pattern we knew rather than something that needed a second look. So we didn't request additional ISR retasking, we just kept the reconnaissance-in-force plan as built.

About six hours after that, brigade S3 called and directed us to continue on Axis BLUE per the original order, citing the synchronization requirement. At that point our engineer had already flagged a preliminary concern about the bridge's load capacity, but it wasn't a hard number yet—no full classification. I mentioned it to brigade informally but didn't push hard. If I'm honest, I thought the concern was enough to justify at least asking for a short pause to get the classification confirmed, but once brigade framed continuation as a synchronization requirement, raising that again felt like second-guessing a decision that had already been made.

Then closer to execution, the engineer came back with an actual classification report suggesting overweight risk for our heaviest vehicles. We had a planning session that same day. The plan was already rehearsed, already briefed up to brigade. The report got raised, a couple people nodded at it, but the discussion moved straight to what the plan already had going for it rather than to whether the risk itself changed anything, and nobody proposed rerouting. The session wrapped with everyone agreeing to keep the existing crossing plan.

Execution day, we had a partial bridge failure under one of the heavier platforms, and almost simultaneously took contact from dismounts near the crossing site. We ran the branch plan, secured the site, and finished the crossing over the alternate ford instead.

Interviewer: Let's slow down and rebuild that timeline with the information you had at each point, not what you know now.

Participant: Fair. At H-48, all I had was the scout sighting and the historical pattern. No confirmation either way on intent. At H-30 or so, I had brigade's directive plus an informal, unconfirmed engineer concern. At H-24, I had a real classification number and a rehearsed plan already in brigade's hands. At H-hour, I had the failure and the contact simultaneously.

Interviewer: Take me back to that first sighting. What made you read it as consistent with the known template rather than as something new?

Participant: The vehicle types matched, the timing matched roughly what we'd seen before, and three months of consistent behavior is a strong baseline. Even with S2 pointing out the location was a little off for that unit's normal screening, it still looked and moved like the same picture we'd been tracking, so I didn't treat the position as something that changed the category. If I chased every deviation with an ISR request, given how constrained our collection was, we'd never finalize anything.

Interviewer: Did you consider requesting retasking anyway, just to confirm?

Participant: S2 raised it as an option. I didn't prioritize it because the weather window for aerial support was closing and I didn't think the deviation was significant enough to justify pulling that asset off other priorities.

Interviewer: When the ground patrol later reported dismounts moving toward the crossing itself rather than the ridge, how did that land?

Participant: That's when S2 flagged it as worth another look. But we were already committed to the recon plan by then, so it didn't change what we'd built.

Interviewer: Move to brigade's call directing continuation on Axis BLUE. What alternatives did you weigh?

Participant: I could have pushed back and asked for a short delay to firm up the bridge picture or scout the alternate ford. Or I could comply and keep the timeline. I went with compliance.

Interviewer: What drove that choice specifically?

Participant: Brigade had already made the call, and it came with the synchronization argument attached. Honestly, the informal concern was probably enough on its own to justify asking for a short hold pending classification, but by the time brigade framed it as a fixed requirement, pushing that same point again felt like challenging a decision that was already settled above me. It felt like brigade owned that risk calculus at that point more than I did.

Interviewer: Did you get any pushback or written response from brigade on the bridge issue?

Participant: No, not before we committed.

Interviewer: Let's go to the planning session where the classification report came in. How did that discussion actually go?

Participant: It was quick. The engineer laid out the overweight risk, a couple of people acknowledged it, and then the conversation moved on to why the current plan was already solid rather than to what the new number actually meant for it. Nobody put a reroute on the table. We closed with agreement to keep the plan.

Interviewer: What was the reasoning for keeping the plan rather than shifting to the alternate ford?

Participant: Once the classification came in, the room still leaned on the fact that the plan was rehearsed and already briefed to brigade more than it leaned on the number itself. Rerouting would have meant reconning an unfamiliar ford in current water conditions, in daylight, with no rehearsal, and we didn't really stop to weigh a partial fix, like resequencing the heavier vehicles, against just keeping what we had.

Interviewer: Did anyone in the room actually voice disagreement with keeping the plan?

Participant: Not in the room, no. I found out afterward that one of the company commanders had reservations about the bridge but didn't say anything during the session.

Interviewer: Did he ever say why he stayed quiet?

Participant: He told me later that by the time the report came up, the room had already settled on keeping the plan, and he didn't want to be the one to reopen something that had already gone up to brigade.

Interviewer: Now the crossing itself. What would have changed your decision to keep the original plan, looking back at what you knew before execution?

Participant: A hard confirmed number earlier, or if someone had actually put the alternate ford proposal on the table instead of just the report sitting there. If we'd had even a day more, I think we'd have reconned the ford as a real branch option instead of a theoretical one.

Interviewer: How do you assess the scout sighting now, knowing what happened at the crossing?

Participant: Looking back, I think we should have caught more from that first report than we did. The river-side location was there in the original reporting, and given how it lines up with the patrol and the contact, we probably should have recognized the implication right then instead of waiting for later confirmation.

Interviewer: Last one—if the alternate ford had been reconned earlier, do you think the planning session goes differently?

Participant: Probably. If it had been a real, validated option sitting next to the bridge option, I think the report would have gotten more than a nod. As it stood, it was theoretical, so keeping the rehearsed plan felt like the lower-risk path in the room that day.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MD_Biased_5}}",
  "occupational_domain": "{{Military and defense operations}}",
  "role": "{{Battalion Operations Officer (S3)}}"
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
