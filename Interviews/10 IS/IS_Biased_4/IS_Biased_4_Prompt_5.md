You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through a specific project, not whether the outcome was good or bad. Everything you share stays with the research team, and you can skip anything you'd rather not discuss. Sound okay?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role and give me a general sense of the project we're going to talk about?

Participant: Sure, I'm a UX designer on the product team at an analytics SaaS company. Back in Q4 we had a six-week window to redesign our onboarding wizard before a big client renewal review. Leadership wanted to see a real bump in activation rate going into that meeting, so there was a lot riding on it.

Interviewer: What made this project different from a routine update?

Participant: Normally we'd have more runway — like a full quarter. This one was compressed, and the budget for outside help was capped, so every dollar and every hour had to be justified. Engineering could only give us maybe one and a half people. It was tight.

Interviewer: Walk me through how it unfolded, from the start.

Participant: So the first thing on my plate was research. We knew the wizard's drop-off was concentrated in three flows, and I needed outside eyes on it fast. I got three vendor proposals in the same week. One was a cheap self-serve platform, six grand, five sessions, but basically no synthesis — you get raw recordings and that's it. Then there were two full-service options: one at twenty-one thousand for ten sessions with a written synthesis, and another at twenty-three for twelve sessions plus dashboard integration and two follow-up rounds. I ended up going with the twenty-three thousand one.

Interviewer: What tipped it that direction?

Participant: Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. For two grand more you got two more sessions, the dashboard hookup, and follow-ups baked in. The middle option just looked like a worse version of the top one at almost the same price. It felt like an easy call.

Interviewer: Did you look closely at whether the cheaper self-serve option would've covered what you actually needed?

Participant: I glanced at it. It probably could've handled the three flows we cared about, session-count-wise. But once I was comparing the two full-service packages, the smaller one kind of dropped out of the conversation — the contrast between the other two was just so stark that it became the frame I was working from.

Interviewer: Got it. What happened after you picked that vendor?

Participant: The findings were usable, but we later realized two of the twelve sessions basically repeated data we already had internally. And the dashboard integration they promised only half worked at delivery, so I had to patch a lot of that manually anyway.

Interviewer: Let's move to the next stage. What came after research?

Participant: We needed a contractor to build the actual micro-interactions for the new flow — transitions, progress indicators, that kind of thing. Two candidates were shortlisted. One, let's call him Candidate X, had done flagship interaction work at a pretty well-known unicorn startup — gorgeous portfolio. The other, Candidate Y, had a less flashy portfolio but included actual test scripts, metrics, iteration logs, the whole documented process.

Interviewer: What made you choose between them?

Participant: I went with Candidate X. The work he'd shipped at that company was the kind of polish we wanted for this wizard, and if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. It seemed like a safe bet given where he'd come from.

Interviewer: Did you verify that documentation and communication piece directly — maybe ask for writing samples or how he'd handled testing on past projects?

Participant: Not really, no. I looked at the visual work and sort of assumed the rest would follow. In hindsight, Candidate Y's portfolio had exactly what we needed evidence-wise, but it didn't have the same wow factor, so it read as less impressive overall.

Interviewer: How did that play out?

Participant: The micro-interactions themselves were beautiful. But he skipped documenting the reasoning behind two key transitions, and when the Head of Design asked for the testing basis, there wasn't really anything to show her.

Interviewer: Let's talk about the third stage — the personalization engine.

Participant: Right, so in parallel we were running a small test on the rules engine — about a hundred forty users — and I'd manually adjusted two of the onboarding rule weights that same week. The activation numbers on the dashboard ticked up right after.

Interviewer: What did you make of that?

Participant: I took it as a sign the adjustments were working. I went to the Data lead and asked to expand my manual tuning authority so I could keep pushing on it before the renewal review.

Interviewer: Was there anything at the time that complicated that read?

Participant: She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver.

Interviewer: What happened the following week?

Participant: The uptick partly reversed once the email campaign ended, and she noted the causal driver was still unconfirmed. So it's genuinely unclear how much of that first bump was actually the rule changes.

Interviewer: Last stage — tell me about the legacy component decision.

Participant: We'd spent three sprints customizing our old step-wizard component to fit the new flow. Then engineering flagged an accessibility defect and a rendering performance issue, and said a newer modular framework would fix both in about a sprint.

Interviewer: What did you decide?

Participant: I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away with the deadline bearing down on us.

Interviewer: Setting aside the sprints already spent, how did the one-sprint migration estimate compare on its own terms to continuing?

Participant: If I'm honest, the one-sprint number was probably a better bet purely on cost and risk. But it was hard to mentally let go of what we'd already built.

Interviewer: What ended up happening with that component?

Participant: The accessibility issue surfaced again during the pre-renewal QA pass, and by then the migration would've cost more than the original estimate because we'd layered on even more customization in the meantime.

Interviewer: If Vendor B had been priced the same as Vendor C, would you have chosen differently?

Participant: Maybe — without that price gap, I probably would've looked harder at whether we needed everything in the top package at all.

Interviewer: If Candidate Y's portfolio had come from a more recognizable company, would the hiring call have gone differently?

Participant: Probably, yeah. It's uncomfortable to admit, but the name recognition was doing more work in my head than it should have.

Interviewer: And if the significance threshold had been strictly enforced before you could act on the rules engine data?

Participant: I'd have waited, or at least run the isolated test first. I just didn't want to lose the momentum.

Interviewer: Last one — if none of the three sprints had already gone into the legacy component, would you still have kept it?

Participant: No. If we were starting fresh, the defects alone would've pushed me toward the new framework immediately. It was really the work already sunk into it that kept pulling me back.

Interviewer: This has been really useful. Thank you for being so candid about where things were uncertain.

Participant: Of course — it's easier to see some of this clearly now than it was in the middle of the sprint.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IS_Biased_4}}",
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
