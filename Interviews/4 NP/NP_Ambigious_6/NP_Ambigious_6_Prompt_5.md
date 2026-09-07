You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for sitting down with me. This is a routine cognitive task analysis interview — I want to understand how you actually worked through the feedwater heater trend during the ascension test, not evaluate your performance. It'll be de-identified for training and procedure review. Okay with you?

Participant: Sure, no problem.

Interviewer: Let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend?

Participant: We were about three hours into the ascension test, sitting around 90 percent power, working toward a dispatch commitment at end of shift. I was doing my normal rounds on the trend recorders and caught that heater 1B outlet temperature had come up about three degrees over maybe twenty minutes. Train 1A was steady, no alarm, nothing outside our Tech Spec limit. My first thought was that it looked like the calibration deviation we'd had on that sensor last cycle — but I didn't want to just assume that, because I didn't actually remember the details of that event well enough to say it matched.

Interviewer: What was going through your head in terms of goals and pressures?

Participant: Getting to a hundred percent within the dispatch window, with about two hours of slack at that point. I wasn't rushed, but I was aware of the clock. At the same time, I didn't want to just label the drift and move on without checking whether it actually fit.

Interviewer: Let's reconstruct the timeline before we get into the decisions. What happened after you noticed the drift?

Participant: I pulled the closed-out fault report from last cycle to compare against what I was seeing. About fifteen minutes later the trend was still creeping, still shallow. Then, maybe forty minutes in total, a maintenance tech on an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. I asked him to take a second reading. Shortly after that the trend recorder started flattening as we came up on the final ascension step.

Interviewer: Okay, let's go through this decision by decision. First: when you noticed the drift, what alternatives did you actually weigh?

Participant: Either treat it as the same calibration issue from last cycle, or treat it as an open question and get an independent check before assuming anything. I ended up somewhere in between — I pulled up the old fault log to see how closely the pattern matched.

Interviewer: What did that comparison tell you?

Participant: Honestly, it was partial. The timing and the size of the rise were similar. But the rate of onset — how fast it ramped at the very start — wasn't something the old log tracked consistently, so I couldn't really say whether that piece matched or not. I logged it as a probable but unconfirmed recurrence, which felt like the most honest way to write it up given what I had.

Interviewer: Did that ambiguity bother you?

Participant: A little. I would've liked a cleaner match one way or the other. But I didn't think it was worth pulling I&C off other work for a value that was still well inside limits.

Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available to brief the STA before continuing. What went into that call?

Participant: That one I thought about for a bit. The STA was right there. Part of me thought, with the comparison being inconclusive, maybe I should just brief him now and let him weigh in. But I also didn't have much to brief him with yet — just an unconfirmed resemblance to an old fault. So I decided to keep trending for a defined stretch, I think I gave it another fifteen minutes in my head, with the idea that either the data would firm up enough to justify a briefing, or it would settle down and not need one.

Interviewer: Was the schedule part of that?

Participant: A bit, sure. But it wasn't the deciding factor — I genuinely thought waiting a short, bounded amount of time would give me better information either way.

Interviewer: Right after that, the technician's infrared call came in. How did you weigh that against the trend recorder?

Participant: That's the one where I felt most uncertain. His reading suggested localized heating, which could point to fouling, but it could also just be a warm spot from wherever that drifted sensor sits — I honestly wasn't sure which. The trend recorder showed a smooth rise, which didn't obviously rule either explanation in or out. Rather than pick one, I asked him to take a second reading and tell me what the scan conditions were, since I wanted something to compare against rather than deciding off one data point.

Interviewer: What came back?

Participant: A similar but not identical reading. He mentioned the scan angle and surface conditions weren't perfectly controlled either time, so even the comparison didn't fully resolve it. At that point I had two data sources that each pointed somewhere, but neither one closed the question.

Interviewer: How did you feel about leaving it open like that?

Participant: A little uneasy, if I'm honest. Usually you want a cleaner answer before you keep moving. But nothing in front of me demanded an immediate call, so I didn't force one.

Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed?

Participant: The flattening helped, but I didn't treat it as proof the earlier question was settled. I still had that inconclusive infrared comparison sitting unresolved. What I did was log it as an open item — wrote it up for the oncoming shift and put in a request for maintenance to follow up — and then proceeded with the step, since there wasn't a procedural or Tech Spec basis to hold at that point.

Interviewer: Did you consider holding anyway, just to close out the comparison first?

Participant: I did think about it. It came down to whether an unconfirmed field reading, with no limit approached, was enough reason to interrupt a scheduled step. I decided documenting it and handing it off was the more defensible path, but I won't pretend that was the only reasonable call.

Interviewer: What single piece of information would have changed that decision?

Participant: If the repeat scan had come back clean and consistent — clearly showing localized heating with good scan conditions both times — I think I would've held and gotten the STA involved before the final step.

Interviewer: And if the trend had kept climbing instead of flattening?

Participant: Then the flattening wouldn't have been there to lean on, and I think the open item alone would've been enough to justify a hold.

Interviewer: Looking back, is there a point where you wish you'd had better information, even if the decision felt reasonable at the time?

Participant: The infrared piece, definitely. I'd have liked a way to get a controlled comparison reading rather than two scans taken under different conditions. That's really where most of my uncertainty sat the whole time.

Interviewer: One last thing for the record, unrelated to how you reasoned through it at the time — a maintenance work order filed after your shift ended found early-stage fouling on the 1B heater, separate from the old calibration issue. That wasn't information you had available during the ascension, so I'm just noting it for the file.

Participant: Understood — that's good to have documented either way.

Interviewer: That's really helpful, thank you.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{NP_Ambigious_6}}",
  "occupational_domain": "{{Nuclear power and Process-control operations}}",
  "role": "{{Reactor Operator (NRC-licensed)}}"
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
