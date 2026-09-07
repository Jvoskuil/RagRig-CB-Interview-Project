You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal analytic training purposes only, not for any evaluation of your performance. Is that alright with you?

Participant: Yes, that's fine. I've done these debriefs before.

Interviewer: Great. Can you tell me a bit about your role and your relationship to this particular account?

Participant: I'm a strategic all-source analyst. I've owned the border garrison account for a little over three years now, alongside six other accounts. It's one of those long-running files where the judgment hasn't moved much — low activity, defensive posture, nothing indicating an offensive buildup. That's been the analytic line since before I inherited it.

Interviewer: Let's start with a general account of the incident we're here to discuss. What happened?

Participant: Over about two weeks, we started getting a handful of reports that didn't fit neatly into the existing picture. First was an imagery report — earth-moving equipment and some new foundation work near a motor pool that had been inactive for as long as anyone could remember. Then a SIGINT analyst flagged an intercept referencing something called "phase two" in the garrison's comms, which nobody could immediately place. And then our liaison partner reported unusual convoy movement at night, three nights running. All of this came in while I was prepping for the quarterly warning board, where I'd need to either sustain or revise the standing assessment.

Interviewer: What was your objective during this period?

Participant: Get it right without overreacting. We've had cycles before where a single ambiguous report triggers a scramble, collection gets retasked away from higher-priority theaters, and it turns out to be nothing. I didn't want to cry wolf on an account that's been stable for three assessment cycles. At the same time, obviously, if something real was changing, I needed to catch it before the board, not after.

Interviewer: What constraints were you working under?

Participant: The usual ones — collection assets are shared across theaters that are ranked higher priority than this one, so tasking anything extra takes justification. I had my other six accounts competing for the same hours in the day. And the liaison service that reported the convoys has a mixed track record — historically maybe six in ten of their reports pan out. So I had to weigh all of that against a board deadline that was about ten days out.

Interviewer: Let's reconstruct the timeline in order. What came in first?

Participant: The imagery report came first, maybe twelve days before the board. Then the SIGINT intercept about five days after that. The liaison convoy reporting came in over the last three nights before the board prep really kicked into gear, so maybe four to six days out.

Interviewer: How did each of those get logged or routed when they arrived?

Participant: The imagery went into the case file as an update — it gets reviewed at the next scheduled cycle unless something flags it for early attention. The intercept got filed under the existing account entry. The convoy reporting got an annotation from me once I looked at it. None of them got kicked upstairs individually; they came to me first since I own the account.

Interviewer: Let's go through the imagery report specifically. What stood out to you, and what did you decide to do?

Participant: The equipment and foundation work were new, that's true — no anomalies like that in the imagery for at least eighteen months. But construction near a motor pool isn't inherently alarming; garrisons refurbish infrastructure for all kinds of reasons, maintenance, logistics upgrades. Given three straight years of assessments concluding no material change, I logged it as a routine update rather than flagging it as a deviation from baseline. I didn't task follow-on collection immediately — the next available window was about ten days out anyway.

Interviewer: What alternatives did you consider at that point?

Participant: I thought about pushing for immediate follow-on imagery, and I thought about flagging it to my branch chief right then for an out-of-cycle conversation. But collection is scarce, and a single unexplained construction indicator didn't feel like enough to justify jumping the queue ahead of higher-priority theaters.

Interviewer: How confident were you in that call?

Participant: Reasonably. Not fully — there's always some uncertainty with a single indicator. But nothing about it screamed urgent.

Interviewer: Moving to the SIGINT intercept. Walk me through your reasoning there.

Participant: The SIGINT analyst brought me the "phase two" reference and asked whether it should be treated as a new indicator. I looked at the broader communications pattern, and outside that one phrase, everything else matched historical baselines — same frequency, same general traffic volume. So I characterized it as ambiguous, non-actionable language, consistent with how this garrison's comms have looked for years.

Interviewer: Did you compare it against the imagery report from a few days earlier?

Participant: Not directly, no. They came from different collection disciplines and different analysts brought them to me separately. At the time it didn't occur to me to sit them side by side — the intercept read as ambiguous on its own terms, so I treated it that way.

Interviewer: What sources did you consult before making that call?

Participant: Mainly the SIGINT analyst's write-up and the historical comms baseline in our database. I didn't pull the imagery file back up at that point.

Interviewer: Let's talk about the convoy reporting. What was your process there?

Participant: My branch chief asked for a preliminary read ahead of the board. I looked at the liaison's track record — about sixty percent corroboration historically — and given that base rate, I annotated the report as uncorroborated and consistent with the liaison's usual noise level. I didn't request independent verification from our own overhead assets against those specific nights.

Interviewer: What alternatives were available to you there?

Participant: I could have tasked an independent asset to check those nights specifically, or I could have flagged it as an open item requiring resolution before the board instead of discounting it outright. Given the timeline and the asset competition, I leaned on the liaison's reliability history as the main basis for how much weight to give it.

Interviewer: Did you connect the convoy reporting with the imagery or the intercept at that stage?

Participant: Not really — each one got assessed against its own history and its own source reliability. It wasn't until later, when I sat down to draft the board summary, that I had all three in front of me together.

Interviewer: Tell me about that moment — pulling the recommendation together for the board.

Participant: With about forty-eight hours left, I had the construction indicator, the intercept, and the convoy reporting all in the case file at once, which was actually the first time I'd looked at them side by side rather than one at a time. My recommendation was to sustain the existing steady-state judgment, with a caveat flagging the three items for continued monitoring. My reasoning was that we've had three consecutive years of stable assessments, and each of these three items, taken on its own, fell within the kind of noise this account has produced before. That track record carried a lot of weight in how much additional verification effort I felt was warranted before finalizing the call.

Interviewer: Did you consider treating the three together as a potential pattern rather than as separate items?

Participant: I noted them together in the write-up, but I didn't reframe the overall confidence level because of it. The account's history of stability was the anchor point for the recommendation.

Interviewer: What happened after the board?

Participant: The board accepted the sustained judgment with the caveats noted. About three weeks later, additional reporting came in that suggested the garrison's posture might actually have shifted, which triggered a retrospective look back at the quarterly call. That review is still ongoing, so I can't tell you definitively yet whether the original read was wrong or whether this new reporting is its own separate development.

Interviewer: If the imagery report had come in on a brand-new account with no track record behind it, do you think you'd have handled it differently?

Participant: Probably, yes. Without three years of stable assessments sitting behind it, I think a single unexplained construction indicator would have gotten more immediate scrutiny, maybe an earlier push for follow-on collection.

Interviewer: What information, if it had arrived earlier, would have changed your recommendation at the board?

Participant: If I'd had independent confirmation on the convoy nights, or if the SIGINT and imagery had been flagged together earlier instead of separately, that combination might have shifted my confidence level enough to recommend an upgrade rather than a caveat.

Interviewer: Looking back, what would you tell a junior analyst handling a similar long-running low-threat account?

Participant: I'd say don't let a good track record become the reason you stop cross-checking new reporting against everything else that's come in recently. It's easy to evaluate each report against its own history in isolation. I'd tell them to make a habit of pulling related indicators together sooner, not just when you're already sitting down to write the board summary.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IA_Biased_1}}",
  "occupational_domain": "{{Intelligence analysis and information-intensive analytic work}}",
  "role": "{{All-Source Intelligence Analyst (Strategic)}}"
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
