You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for taking the time. This is being recorded for internal case-review purposes only, and you can skip anything you'd rather not go into. Can you start by telling me your role and background?

Participant: Sure. I'm a financial crime intelligence analyst on the FIU team, been in this specific role about six years, mostly trade finance and sanctions typologies before that.

Interviewer: I want to walk through a specific case — the Halcyon Freight matter. Can you tell me how it came to your attention and what you were trying to achieve?

Participant: It came in as part of a batch alert — four counterparties flagged together. Halcyon Freight Partners was one of them, along with a commodities trader, a small logistics subcontractor, and a shipping agent. My objective was the usual one: figure out whether there was enough here to warrant an escalation to compliance and possibly law enforcement, and do it within the ten-day filing window.

Interviewer: What did the batch actually show you?

Participant: Halcyon had one indicator that stood out — an invoice value gap, meaning the declared value didn't match what we'd expect for the goods described. No beneficial-ownership overlap with anything I'd seen before, so it wasn't ringing any specific bells. The commodities trader had a minor documentation gap, but nothing typologically interesting. It was a fairly normal week workload-wise, nothing especially heavy.

Interviewer: Walk me through what you did once you had that picture.

Participant: I prioritized Halcyon first, since the invoice gap was the clearest indicator I had to work with, and documented a plan to get through the other three that same week. I didn't ignore them — I just sequenced based on which indicator looked most substantive on its face.

Interviewer: What made you order it that way rather than, say, splitting time evenly or going by transaction size?

Participant: Honestly, either of those would have been defensible too. I went with indicator strength because that's usually a decent proxy for where the real risk sits, but I'll admit transaction size might have surfaced something different. I made a note of the reasoning in case anyone asked.

Interviewer: Did anyone ask?

Participant: Yeah, my team lead did, later. Wanted to know why I'd sequenced it that way. I walked her through the invoice-gap rationale and she was fine with it — it wasn't the only reasonable choice, but it wasn't unreasonable either.

Interviewer: What came out of the other three once you got to them?

Participant: The shipping agent turned out to have an administrative filing delay — paperwork lag, not a risk issue at all. Nothing on the logistics subcontractor either. So the sequencing didn't really cost us anything in the end, though I can't say for certain it wouldn't have mattered in a different case.

Interviewer: Let's move to the vendor report. What happened there?

Participant: A few days in, our OSINT vendor sent a report saying Halcyon's ownership structure was "plausibly consistent" with a known layering pattern. Importantly, they flagged it as moderate confidence themselves and noted one registry link hadn't been independently verified yet.

Interviewer: How did you decide how much weight to give that?

Participant: A colleague suggested we get a second data pull to firm up that specific link before leaning on the report too heavily. I thought that was reasonable, so I treated the report as partial corroboration — enough to keep building the file, not enough to treat as settled — while the second pull was requested in parallel.

Interviewer: Was there a version of this where you'd have leaned harder on the report, or set it aside entirely?

Participant: Sure, both were on the table. If it had come in with high confidence and no caveats, I probably would have moved faster. If a colleague hadn't raised the registry-link point, I might have just taken it at face value. Setting it aside completely felt like it would slow us down without much benefit, since the report was self-aware about its own gap.

Interviewer: What did the second data pull show?

Participant: It confirmed the registry link, actually. Compliance counsel later said treating it as partial rather than definitive was the right call, though I don't think that outcome alone tells you the initial judgment was necessarily correct — it could've gone the other way too.

Interviewer: Let's talk about the correspondent bank. What was that situation?

Participant: We'd requested SWIFT records and hadn't heard back. This particular correspondent's turnaround history is all over the place — I've seen requests take anywhere from five to fourteen business days, no real pattern to it. We were six days out from the filing deadline, and the liaison had just logged it as "standard priority," no timeline attached either way.

Interviewer: What did you decide to do while you waited?

Participant: Kept building the file and wrote up a contingency note — basically, what we'd file if the records didn't show up in time. Given how mixed the history was on turnaround, I didn't feel like I had grounds to assume either a fast or slow outcome, so I planned for both.

Interviewer: What actually happened?

Participant: Partial records came back on day six. Enough to inform the file, not enough to close every gap. My team lead noted we'd at least had the contingency plan ready, which helped.

Interviewer: Last stretch — the time estimate for remaining work.

Participant: Reconciling two invoice sets, drafting the narrative, compliance sign-off. Comparable cases have run anywhere from four to eight days historically — a pretty wide band. I landed on four days, near the lower end, based on the specific tasks left and the fact that neither of my other two cases was at a critical point that week.

Interviewer: What made you lean toward the lower end rather than the middle or upper end of that range?

Participant: The task list itself looked manageable, and I didn't have anything else competing hard for my time. I did flag internally that if a reconciliation issue came up, that number could slip.

Interviewer: How did it actually play out?

Participant: Pretty close. One clarifying question came up during reconciliation that cost half a day, and sign-off took about as long as I'd have expected given the case's complexity. Nothing dramatic.

Interviewer: Looking back across all four points, what were you least sure about at the time?

Participant: Probably the correspondent bank timing — that one genuinely could have gone either way, and I don't think there was a way to know in advance. The vendor report's registry link was a close second.

Interviewer: A few hypotheticals. If the shipping agent's delay had turned out to be substantive rather than administrative, what would you have done?

Participant: I'd have reshuffled priorities immediately and probably pulled in a second analyst.

Interviewer: If the vendor's report had come in high-confidence instead of moderate?

Participant: I likely would have moved to drafting the escalation sooner rather than waiting on the second pull.

Interviewer: If you'd known the records would land on day six rather than later?

Participant: Honestly, not much would've changed — the contingency plan already assumed something like that.

Interviewer: And if a colleague had reviewed your time estimate beforehand?

Participant: They might have pushed me toward the midpoint just to be safe, but I think they'd have accepted four days as reasonable given the task list.

Interviewer: That's really helpful, thank you.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IA_Ambigious_4}}",
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
