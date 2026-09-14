You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is for a plan-review case study, it's voluntary, and you can skip anything you'd rather not discuss. Can you start by telling me your role and how the Meridian Tower conversion landed on your desk?

Participant: Sure. I'm a plan review official in the building and fire division, mostly permitting and life-safety sign-off. Meridian Tower came to me because it was an adaptive reuse—22-story former office tower going to mixed-use residential and retail. The atrium was the whole complication. It's a big central void running most of the building height, and the geometry didn't fit the prescriptive smoke control provisions in our code. So the design team came in with a performance-based alternative instead.

Interviewer: What was your objective going in?

Participant: Get the project through review correctly and on time. We had a 30-day statutory clock, the department was short-staffed that quarter, and the city council was leaning on us to keep housing projects moving. So there was real pressure, but the job is still to make sure people are safe if there's a fire.

Interviewer: Walk me through what happened, from the beginning.

Participant: The engineering firm on record was Halkirk & Vance—they're a big regional name, they've done dozens of performance-based atrium designs, and a neighboring jurisdiction had approved a very similar design from them the year before. They submitted a CFD-based smoke control model instead of the prescriptive system. We didn't have budget that cycle for an outside peer review of the CFD assumptions, so it was really me evaluating it against the documentation package. After I signed off, we moved to writing commissioning conditions, which is where we had to pick between two verification protocols. Construction got underway, and partway through, our inspector flagged fire-door deficiencies on three floors. Then near occupancy, the developer pushed for an early certificate before full integration testing was done. Later in construction, there was a small trash-chute fire—sprinklers knocked it down fast, nobody was hurt—but it got people looking hard at the atrium smoke system again.

Interviewer: Let's reconstruct the order more precisely. What did you know before the first big decision, and what came in afterward?

Participant: Before approving the design, I had the CFD report, the firm's track record, and the neighboring jurisdiction's prior approval. After I approved it, we moved into commissioning planning—that's when the protocol question came up. After that decision, construction started, and the door issue surfaced maybe six weeks in. The occupancy request came right at the tail end, with the fire happening after that decision, not before.

Interviewer: Let's go through the first decision—approving the performance-based design. What evidence carried the most weight for you?

Participant: Honestly, the firm's name carried a lot of it. Halkirk & Vance has been doing this specific type of atrium work for years, and I knew their stamp had held up under scrutiny elsewhere—that neighboring jurisdiction's sign-off mattered to me. I read through the CFD report, but with the review clock running and no budget for an outside check, I leaned on the fact that this firm doesn't submit sloppy work. If it had been a firm I didn't recognize, I probably would have pushed harder on the input assumptions myself.

Interviewer: Was requiring an outside peer review on the table?

Participant: It was, but it would have added about three weeks, and given who submitted it, that felt like an unnecessary delay for a firm with that reputation.

Interviewer: Second decision—the commissioning protocol. What were you weighing there?

Participant: Two options. Option A was a newer risk-informed test, better matched to this atrium's actual geometry according to the guidance documents, but its pass/fail thresholds were described in fairly qualitative terms. Option B was the old prescriptive smoke test—clear binary pass or fail, easy to defend if anyone questioned it later, but known to be less sensitive to some of the failure modes this particular atrium could have.

Interviewer: Which did you pick, and why?

Participant: Option B. I'll be straight about it—part of the appeal was that I knew exactly what passing looked like and exactly what failing looked like. Option A might have been the better technical fit, the guidance basically said so, but I didn't want to be defending a judgment call on "partially qualitative" thresholds if something went sideways. B gave me a clean line.

Interviewer: Third decision—the door deficiencies. What did you see, and how did you respond?

Participant: Our inspector found bad fire-door installations on floors 8, 11, and 14. Out of the whole building, those three stood out to me, and my read was that we had a problem crew or a bad batch of hardware concentrated there. I redirected our follow-up inspection effort to those three floors specifically.

Interviewer: Were the crews assigned by floor, or rotated?

Participant: Rotated randomly across the building, actually. And it was three deficiencies out of about 150 doors we'd checked at that point, which is close to what you'd expect on a project this size just from ordinary variation. But when you see three flagged floors, it's hard not to read that as meaning something.

Interviewer: Fourth decision—the temporary occupancy request. What was your basis for granting it?

Participant: The developer had a financing deadline, and full integration testing on the alarm and smoke systems was still three weeks out. This contractor has a good record on other city jobs I've handled, so I felt reasonably confident things would come together. A colleague also mentioned a similar building nearby that had gotten early partial occupancy and it worked out fine. I did know our own five-year numbers show something like 15 percent of these atrium smoke-control integration tests need rework citywide, but that felt like a background statistic rather than something specific to this job.

Interviewer: What would have made you deny it instead?

Participant: If the contractor's record had been shakier, or if there'd been an active known defect in the smoke system at that point, I'd have held the line. Nothing like that was flagged to me at the time.

Interviewer: How much uncertainty did you feel at each of these points?

Participant: Honestly, less than maybe I should have on the first and last ones. The door issue felt more certain than it probably was, in hindsight. The protocol choice, I knew I was trading some technical fit for administrative clarity going in.

Interviewer: Looking back now, after the trash-chute fire, how do you view the original design approval?

Participant: It's hard not to think the smoke migration issue should have jumped out at someone reading that CFD report closely. There was a sensitivity assumption buried in there about stack effect under partial door-open conditions, and looking at it now, it feels like it was sitting right there in the numbers the whole time. At the time, though, it just didn't register as something that mattered—it was one line among a lot of technical detail, and nothing about it stood out as a flag worth chasing back then.

Interviewer: If you had the same information again, would you change the occupancy call?

Participant: Probably not without new information. It felt like a reasonable bet given the contractor's history at the time.

Interviewer: Last one—what would you tell a newer reviewer handling a similar submittal?

Participant: Don't let a strong firm's name substitute for reading the assumptions line by line, and don't let a small, tidy pattern in inspection data talk you out of checking the actual numbers behind it.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HE_Biased_6}}",
  "occupational_domain": "{{High-risk Engineering and Fire Engineering}}",
  "role": "{{Building/Fire Code Official (Plan Review and Permitting)}}"
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
