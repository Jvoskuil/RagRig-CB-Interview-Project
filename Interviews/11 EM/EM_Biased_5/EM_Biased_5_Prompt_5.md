You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. This is a debrief interview, not a review — nothing here goes into your personnel file, and you can decline to answer anything. Is that okay?

Participant: Yeah, that's fine. I figured you'd want to talk about the Riverside call eventually.

Interviewer: Exactly. Can you start by telling me your role that shift and what you knew before you got there?

Participant: I was IC, first-due battalion. Dispatch had it as a small trash fire, exterior, rear alley of an industrial unit — auto parts store up front, warehouse space in the back. No hazmat flag, no history on the address. Two engines and a truck were coming with me.

Interviewer: What was your objective once you rolled up?

Participant: Same as always — knock it down fast, keep it from extending into the structure, make sure nobody's inside. Straightforward call, or so it looked.

Interviewer: Walk me through what actually happened, start to finish.

Participant: We pulled up and there was a moderate smoke column, more than I'd expect from a trash fire, but honestly that's not unusual — dumpster fires with pallets or packaging can push a decent amount of smoke. Dispatch had said small and exterior, so I put my first-in crew on a quick knockdown line rather than sending someone around back first. We got water on it within a couple minutes. Once the crew got to the rear of the building, that's when things changed — heavier smoke, a chemical smell, and they found a stack of drums against the rear wall, a couple of them with fire exposure. So now I've got a fire that started as trash-can-sized turning into a possible hazmat exposure.

Interviewer: What did you do at that point?

Participant: Called for a hazmat tech and requested a second alarm for staffing. We shifted into more of a hybrid posture — fire attack continuing, but treating the rear as an isolation zone until we knew what we were dealing with.

Interviewer: Let's go back to that very first call — committing the line before checking the rear. What went into that?

Participant: Dispatch said small trash fire, and that's usually reliable enough to act on immediately — you don't want to sit on a fire waiting for a full 360 when speed matters. The smoke was heavier than I'd expect for that call type, I noticed it, but I didn't want to lose time doing a full walk-around on what was described as a contained exterior fire.

Interviewer: What would have made you hold back and do the 360 first?

Participant: If dispatch had said anything about chemical storage back there, I'd have gone defensive immediately and skipped the quick-attack option entirely. Without that flag, I went with what was called in.

Interviewer: Was time pressure a factor?

Participant: Some. Every minute a small fire sits, it can grow, so there's always pressure to commit. But if I'm honest, the call type is what I leaned on more than the visual.

Interviewer: Once the hazmat tech got there, how did you go about identifying what was in those drums?

Participant: There was a placard on one drum, partially legible — rust and fire damage had eaten some of the numbers. The tech's read was that it lined up with a common solvent, the kind sold in the retail section up front, which made sense to us — warehouse storing overflow of what they sell. The night manager was on scene too, pretty shaken, and he said something like "no, that's not what's back there, it's something different," but he was contradicting himself on other details too — couldn't remember which door led where, that kind of thing.

Interviewer: How did that statement factor into your PPE and agent decisions?

Participant: We didn't weight it heavily. He was rattled, giving inconsistent answers generally, and the placard read supported what we already expected to find. We moved forward with PPE and foam suited for that solvent class.

Interviewer: Did you look for a second placard or manifest confirmation before committing?

Participant: We didn't stop operations to go find one. In hindsight, there was a second drum with an intact placard a few feet away, and it showed a different hazard class. We found the manifest fragment later, in a file cabinet, and it didn't match either.

Interviewer: What would have changed your read at the time?

Participant: A clean placard would've done it immediately. The occupant's statement alone — I probably needed more than that, given how confused he was on everything else.

Interviewer: Let's talk about the perimeter. How did that get set?

Participant: The first-arriving officer put an initial isolation line at 150 meters, standard distance for an unknown chemical exposure situation. By the time I was thinking hard about it, mutual aid units were already staging off that line, and the battalion chief who came in was operating off it too — didn't question it, just built his sector around it.

Interviewer: Did you have any reservations about that distance?

Participant: A little. Wind had started shifting toward the residential block, and I remember thinking we might want to push it out, but everybody was already set up on 150, command posts, staging, hose lays — recalculating and moving all of that would've been a real disruption, and nobody else seemed to be flagging it as a problem. So I left it.

Interviewer: What happened with the wind?

Participant: It fully shifted about twenty minutes later, confirmed by a weather update, and then air monitoring near the edge of our line came back close to the action threshold. We had to push the perimeter out on short notice, which is never clean — reshuffling people, moving apparatus.

Interviewer: If you'd recalculated independently earlier, do you think it would've gone differently?

Participant: Possibly. I had the wind information sooner than we acted on it.

Interviewer: Last decision point — the search. Tell me about that.

Participant: Interior team had cleared about ninety percent of the structure. The last piece was a small storage room right next to the drum stack, and by then the crew had been in there over half an hour, visibly gassed. The chemical ID still wasn't nailed down, and drum integrity in that room was unknown.

Interviewer: What was the call?

Participant: The battalion chief said something like, "we can't call this search done and leave one room unaccounted for — that's the difference between a cleared building and one we're guessing about." Framed that way, leaving it unresolved felt like accepting a gap we couldn't defend. So I authorized the crew to go finish it.

Interviewer: What did you find?

Participant: Room was empty. But one of the drums in there was leaking slightly, so that crew got more exposure time near an unresolved hazard than I'd have liked, in a room we didn't need to enter for life safety, since it turned out to be unoccupied.

Interviewer: Looking back at that whole call — does anything stand out as something that should have been obvious at the time?

Participant: Honestly, yeah. That smoke column at the very start was heavier than a trash fire should produce. I think if I'd trusted that visual over the dispatch description, I'd have sent someone to check the rear before committing the line. It feels like the signs were there from minute one.

Interviewer: What would you tell a newer commander to watch for in a similar situation?

Participant: Don't let the initial call type set your whole picture — cross-check it against what you're actually seeing, especially smoke volume and color. And when a perimeter's already been set by someone else, still run your own numbers if conditions change, because everyone assumes someone else already checked it.

Interviewer: Anything else you want to add?

Participant: Just that none of these calls looked wrong in the moment. It's only once you line them all up afterward that you see where it could've gone differently.

Interviewer: That's helpful. Thanks for walking through it in this much detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EM_Biased_5}}",
  "occupational_domain": "{{Emergency management and Civil Protection}}",
  "role": "{{Incident Commander (Structural Fire/Hazmat Response)}}"
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
