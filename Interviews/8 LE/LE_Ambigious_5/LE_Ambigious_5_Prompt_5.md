You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time. This is a voluntary session for internal research on how IA reviews get worked, not a disciplinary matter. You can decline any question. Good with that?

Participant: Sure, that's fine.

Interviewer: Can you tell me your role and experience with complaint reviews?

Participant: Internal Affairs investigator, about five years. I handle use-of-force complaints mostly, some policy violations.

Interviewer: Walk me through the case.

Participant: Traffic stop on Cedar Street, expired registration, ended with a takedown. The driver, Mr. Alvarez, alleges excessive force by Officer Marquez, came away with a wrist fracture. Marquez's report says Alvarez became resistant and pulled his arm away, necessitating the takedown. His partner, Officer Chen, corroborates that. Marquez has nine years in, two prior complaints, both closed unfounded. Alvarez has two prior arrests, one for resisting.

Interviewer: What was your initial read on credibility before you'd seen any footage?

Participant: Genuinely unresolved. Two competing accounts, both plausible on their face, and I didn't have enough yet to prefer one.

Interviewer: What did you do first when you opened the file?

Participant: Requested background on both sides—Alvarez's arrest history and Marquez's disciplinary and training file. Alvarez's record came back within a day, since it's just a records-system pull. Marquez's full file took almost a week because it required a request through the union rep and a records custodian. So for several days I had a fuller picture of one side than the other, which I noted explicitly in my log as a limitation, not a conclusion.

Interviewer: Did that timing gap affect how you approached the rest of the review?

Participant: I tried not to let it. I flagged it as an open item—"complainant background received, officer background pending"—so anyone reading the file later would know the record was uneven at that point, not that I'd already decided anything based on it. Dispatch audio later confirmed it was a routine stop, not flagged high-risk. Medical report confirmed the fracture but didn't tell me which account caused it.

Interviewer: Let's go to the footage.

Participant: Eighteen minutes, with a forty-second gap right after initial contact—his camera didn't reactivate cleanly. Early part is calm, verbal exchange, some de-escalation language from Marquez. Final ninety seconds: Alvarez pulls his arm back, Marquez takes him down.

Interviewer: How did you weigh the earlier footage against that final sequence?

Participant: Honestly, I couldn't fully resolve it on the first pass. The takedown is obviously central since that's where the injury happened, but the gap sits right before the point where things start escalating, and I don't know what's in it. I logged both segments as carrying weight and noted the gap as a limiting factor on any proportionality conclusion I might draw. I didn't want to lock in a read before the consultant weighed in.

Interviewer: What came out of the consultant review?

Participant: A slowed-frame audio pass caught Marquez raising his voice and stepping closer about three minutes before the takedown. The consultant said it's relevant context but not dispositive on its own—doesn't resolve whether the final force was proportionate, just adds texture.

Interviewer: How did that sit with you?

Participant: It complicated things more than it clarified them, if I'm honest. It's the kind of detail that could support either read, depending on what else you believe about the encounter.

Interviewer: Tell me about the case conference.

Participant: Day six. Me, the sergeant, two peer investigators. The sergeant supervised Marquez for three years, said something like "he's generally solid, but I wasn't in the car, so take that for what it's worth." One of the other investigators raised the forty-second gap, said it needed to be addressed before we went further.

Interviewer: How did the room handle that?

Participant: We actually sat with it. There wasn't a quick consensus—two of us thought the gap was potentially significant given the timing relative to the escalation audio, one thought Chen's corroboration and the visible resisting motion carried it regardless. We didn't resolve that disagreement in the room. I logged the dissenting view by name in the case file and noted the preliminary summary as tentative pending the gap issue.

Interviewer: Did the sergeant's history with Marquez shape the discussion?

Participant: It was mentioned, and it's fair to say it's not nothing—people listen when a three-year supervisor speaks. But he qualified it himself, and the discussion kept coming back to what was and wasn't on the tape rather than settling on his character read. I can't say for certain it had zero influence, but I also can't point to a moment where it overrode the evidentiary discussion.

Interviewer: What happened with the eyewitness on day ten?

Participant: A civilian witness we'd had trouble reaching finally called back. She said Marquez was "aggressive from the start," which cuts against how I'd been characterizing the early footage. That came two days after I'd sent the Deputy Chief a preliminary note—explicitly marked tentative, pending the gap and the consultant review.

Interviewer: How did you weigh her statement against what you already had?

Participant: We ran a supplemental check—she had an unobstructed view but was about thirty-five feet out, evening light. I weighed that against the footage on its own terms: is a thirty-five-foot, unobstructed view enough to outweigh eighteen minutes of direct recording? I didn't think it fully was, but I also didn't think it was nothing, especially given the earlier escalation audio the consultant had flagged. I ended up revising the briefing language to reflect that the finding remained more open than the initial note suggested, rather than either adopting her account outright or setting it aside.

Interviewer: Did the fact that you'd already briefed command shape how you handled her statement?

Participant: Command asked whether the preliminary note still held, and I told them it needed updating. It wasn't comfortable revising something I'd already sent up, but the distance and lighting were the actual basis for how much weight I gave her account—not really about protecting what I'd said earlier. I'd rather have gotten it right than tidy.

Interviewer: What's the part of this case you're least confident about?

Participant: The forty-second gap, still. I don't know what happened in it, and I don't know how much that should move the needle either way.

Interviewer: If the eyewitness statement had come in on day two instead of day ten, would your review have gone differently?

Participant: Possibly. I'd have had it earlier alongside the footage instead of layering it onto a note I'd already sent, though I think I'd have weighed it the same way on the merits—distance and view, not timing.

Interviewer: If you'd been the only reviewer, without the case conference, same finding?

Participant: Hard to say. I might have sat with the gap even longer alone. The conference didn't rush me toward a view, but group discussion does move differently than solo review.

Interviewer: Anything you'd sequence differently next time?

Participant: I'd push to get officer background files moving faster at intake, so that gap doesn't sit open as long. Otherwise, I think the uncertainty here was mostly the case itself, not how I worked it.

Interviewer: Appreciate you walking through it.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{LE_Ambigious_5}}",
  "occupational_domain": "{{Law enforcement}}",
  "role": "{{Internal Affairs Investigator}}"
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
