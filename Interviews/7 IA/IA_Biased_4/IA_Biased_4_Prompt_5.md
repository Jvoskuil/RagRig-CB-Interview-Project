You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal case-review and training purposes only, and I'll be asking you to walk me through a specific case in detail. You're free to skip anything you're not comfortable discussing. Can you first tell me your role and how long you've been doing this kind of work?

Participant: Sure. I'm a financial crime intelligence analyst on the FIU team, been here about six years, mostly focused on trade finance and sanctions-related typologies. Before that I did two years in transaction monitoring.

Interviewer: Great, thanks. I want to focus on a specific case — the Meridian Trading matter. Can you walk me through how it first came to your attention and what you were trying to accomplish?

Participant: Right, so this came in through an automated alert — three invoices from Meridian Trading LLC with quantity and value mismatches, which is a classic flag for trade-based money laundering. My objective was straightforward on paper: figure out whether this was probable sanctions evasion and, if so, get a defensible escalation to compliance and law enforcement before the filing window closed. We had ten business days from the alert.

Interviewer: What did the alert batch actually contain?

Participant: A cluster of counterparties. Meridian was the obvious one — the ultimate beneficial owner shared a registered agent with a company from a case I'd worked about eighteen months earlier, which had ended in a successful sanctions-evasion referral. There was also a separate counterparty in the same batch, a logistics firm, that didn't match anything I recognized. And it was a heavy week — alert volume across the team was well above average, so I needed to move efficiently.

Interviewer: Let's reconstruct the sequence. What did you do right after opening the alert?

Participant: I scoped the review. Given the registered-agent overlap with the prior case, I focused my initial workup on Meridian and its immediate corporate web — pulling registry filings, past KYC refresh notes, that kind of thing. The logistics counterparty I noted but set aside as lower priority since it didn't fit any typology I'd seen before.

Interviewer: What specifically made you decide to scope it that way rather than, say, broadly across everyone in the batch?

Participant: Honestly, the registered-agent match jumped out immediately. That pattern had been reliable before — same agent, similar shell structure, same region. With the volume we were under that week, I didn't feel I had the bandwidth to give equal weight to an entity that had no connection to anything I'd seen. I did glance at the logistics firm's file, but there was nothing that screamed "look here," so I moved on.

Interviewer: Did you consider requesting broader automated screening before locking in that scope?

Participant: I thought about it, but that would've added a day or two, and the Meridian angle felt like the more productive use of time.

Interviewer: What happened with the logistics counterparty afterward?

Participant: A few days later it showed an unusual same-day wire pattern — nothing I'd examined at that point. My team lead actually asked why it wasn't in my initial scoping note. I didn't have a great answer beyond "it didn't fit the pattern I was chasing."

Interviewer: Let's move to the vendor report. Walk me through what happened when that arrived.

Participant: About three days in, our OSINT vendor sent a report concluding Meridian was highly likely tied to the sanctioned end-user. Their argument traced a chain of corporate registry links. The bottom line matched exactly what I already suspected from the registered-agent overlap, so it felt like strong corroboration.

Interviewer: Did anyone raise concerns about the report?

Participant: One of our junior analysts flagged that a step in the vendor's chain — where they treated two similarly named entities as the same legal entity — hadn't been independently verified. I remember thinking that was a fair point to note, but it read to me as a technicality rather than something that undercut the conclusion, since the overall picture fit so well with what I was already building.

Interviewer: What made you weight the report the way you did?

Participant: The conclusion aligned with my working theory, and the vendor has a decent track record. I treated the alignment itself as a kind of confirmation. I didn't go back and independently re-verify that specific entity-matching step before folding the report into the case file.

Interviewer: What did you later learn about that?

Participant: A document pull afterward showed the two entities were actually legally distinct, different beneficial owners entirely. Compliance counsel asked directly what independent verification had been done on that claim, and I had to admit — not much, beyond the vendor's own chain.

Interviewer: Let's talk about the correspondent bank. What was the situation there?

Participant: We'd requested SWIFT records — MT202 and MT103 messages — to confirm the fund flow to the suspected end-user. That correspondent bank, in a secondary jurisdiction, is notoriously slow; historically those requests take twelve to fifteen business days. We were six days from the filing deadline with nothing back yet, no confirmation timeline in writing.

Interviewer: What did you decide to do about the escalation while waiting?

Participant: I held off drafting it. I figured the records would probably come through in time — I wanted the file to be complete with that corroborating piece rather than submit something with a gap in it.

Interviewer: What gave you that expectation, given the track record you mentioned?

Participant: Honestly, more that I wanted it to land that way. Nothing had actually changed with the correspondent bank's typical pace. On day six they came back and said it'd be another ten days.

Interviewer: What happened to the case file at that point?

Participant: My team lead pointed out there wasn't a contingency escalation path drafted, so we were now scrambling.

Interviewer: Let's cover the last piece — the time estimate for remaining work.

Participant: With reconciliation, narrative drafting, and compliance sign-off left, I estimated two business days. I walked through the sequence assuming everything went smoothly — no rework.

Interviewer: How does that estimate compare to similar cases?

Participant: Comparable cross-border verification cases have typically run five to seven days. I didn't really reference that when I made the call, and I still had two other active cases pulling at me.

Interviewer: What happened once you started?

Participant: Reconciliation turned up a discrepancy that needed a follow-up query — cost an extra day. Sign-off took longer too, over a routine question I hadn't anticipated.

Interviewer: Looking back across all four points, what were you least certain about at the time?

Participant: Probably the entity-matching step and whether the records would actually show up. Those felt like the shakiest parts, even while I was moving forward on them.

Interviewer: A couple of hypotheticals. If the logistics counterparty had been flagged as high-risk from the start, how would your approach have changed?

Participant: I'd have split my attention much earlier and probably caught the wire pattern days sooner.

Interviewer: And if you'd known upfront the correspondent bank would take fifteen days?

Participant: I would have drafted a conditional escalation immediately rather than waiting.

Interviewer: Last one — if a colleague had reviewed your time estimate before you committed to it, what do you think they'd have flagged?

Participant: The base rate, probably, and the fact that I was already stretched across two other cases. Fair critique.

Interviewer: That's really helpful, thank you.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IA_Biased_4}}",
  "occupational_domain": "{{Intelligence analysis and information-intensive analytic work}}",
  "role": "{{Financial Crime/Threat Intelligence Analyst}}"
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
