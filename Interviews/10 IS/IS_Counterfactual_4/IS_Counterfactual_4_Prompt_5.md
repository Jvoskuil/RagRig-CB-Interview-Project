You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for sitting down with me. Quick reminder — this is a cognitive task analysis interview, so I'm interested in how you reasoned through things, not in grading the outcome. You can decline any question. Okay to start?

Participant: Sure, sounds good.

Interviewer: Can you give me your role and a general sense of the project?

Participant: I'm a UX designer on the product team at a B2B analytics company. Last year I led a redesign of our onboarding wizard, aiming to cut first-week drop-off. We had a twelve-week window that lined up with our quarterly product review — nothing contractual riding on it, just the usual expectation that we'd show some lift in activation rate.

Interviewer: Twelve weeks is a decent runway. What made this project stand out otherwise?

Participant: Mostly the scope — three flows needed real research, we needed outside build help, and there was a personalization system already running in the background that we wanted to lean on more.

Interviewer: Walk me through how it played out from the start.

Participant: Sure. Early on, three research vendor proposals came in. One was a cheap self-serve platform — six thousand dollars, five sessions, no synthesis, just raw recordings. Then two full-service options: twenty-one thousand for ten sessions with a written synthesis, and twenty-three thousand for twelve sessions plus dashboard integration and two follow-up rounds. I had plenty of time to sit with these, and I ended up going with the twenty-three thousand option.

Interviewer: What drove that?

Participant: When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it.

Interviewer: Did you weigh the cheaper self-serve option against your actual scope — you only needed three flows validated?

Participant: I looked at it briefly. It probably could have covered what we needed session-count-wise. But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly.

Interviewer: What came of that vendor choice?

Participant: The findings were fine, though two of the twelve sessions turned out to duplicate internal data we already had. And the dashboard piece only half worked when it was delivered — I ended up patching a lot of it myself.

Interviewer: Next stage?

Participant: Hiring a contractor for the micro-interactions — transitions, progress indicators. Two candidates: one had flagship work at a well-known unicorn startup, gorgeous portfolio, but not much documented process. The other had a plainer portfolio but included actual test scripts, metrics, iteration logs.

Interviewer: How did you choose, given you had time for a trial task if you wanted one?

Participant: I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too. I did consider running a paid trial with both — we had the weeks for it — but it felt like an unnecessary step given his track record.

Interviewer: Did you check the documentation and communication side directly?

Participant: Not really. I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in.

Interviewer: What happened with his deliverables?

Participant: Beautiful interactions, but he skipped documenting the reasoning for two key transitions, and when the Head of Design asked for the testing basis later, there wasn't much to show her.

Interviewer: Let's talk about the personalization engine.

Participant: We had a small test running — about a hundred forty users — on the rules engine, and I'd manually tuned two onboarding rule weights that same week. Right after, the activation number ticked up on the dashboard.

Interviewer: What did you take from that?

Participant: That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it.

Interviewer: Was there anything complicating that read?

Participant: She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.

Interviewer: What happened afterward?

Participant: The bump partly reversed once the email campaign ended, and she noted the actual driver was still unconfirmed.

Interviewer: Last stage — the legacy component.

Participant: We'd put three sprints into customizing our old step-wizard component for the new flow. Then engineering flagged an accessibility defect and a rendering issue, and said a newer modular framework would fix both in about a sprint. We still had roughly six weeks left, so a one-sprint migration wouldn't have threatened the review date at all.

Interviewer: What did you decide?

Participant: I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare.

Interviewer: Setting the prior sprints aside, how did the one-sprint estimate compare to continuing, on its own terms?

Participant: Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me.

Interviewer: What happened with the component?

Participant: The accessibility issue came back up during QA before the review, and by then migrating would have cost more than the original estimate, since we'd layered on even more customization by that point.

Interviewer: If Vendor B had been priced the same as Vendor C, would you have decided differently?

Participant: Possibly — I might've actually gone back and checked whether we needed the top-tier package at all.

Interviewer: If the second candidate's portfolio had come from a more recognizable company?

Participant: Probably would have hired her instead. That recognition factor carried more weight than it should have.

Interviewer: If the significance threshold had been strictly enforced before you could act?

Participant: I'd have waited — we had the schedule for it, I just didn't want to lose momentum.

Interviewer: And if none of those three sprints had already gone into the legacy component?

Participant: No question, I'd have migrated right away given the defects.

Interviewer: Last one — if this had been the original six-week sprint with the hard renewal deadline instead, do you think any of this would have gone differently?

Participant: Maybe the vendor and hiring calls would've felt more forced. But honestly, looking back, I'm not sure the extra time changed as much as it should have — I still landed in mostly the same places.

Interviewer: That's really helpful context. Thank you for walking through it so openly.

Participant: No problem — easier to spot in hindsight than it was in the moment.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IS_Counterfactual_4}}",
  "occupational_domain": "{{Information Systems, human-computer interaction, and interaction design}}",
  "role": "{{UX/Product Designer}}"
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
