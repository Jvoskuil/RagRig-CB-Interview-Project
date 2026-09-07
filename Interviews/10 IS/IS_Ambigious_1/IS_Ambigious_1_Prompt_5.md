You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time. Before we start, do you consent to discussing this incident for the interview?

Participant: Yes, go ahead.

Interviewer: Could you describe your role and the situation we'll be talking through?

Participant: I'm a Product Manager on the onboarding team at CollabHub. We're a B2B collaboration platform, mostly self-serve signups with some sales-assisted accounts that go through the same flow. About five weeks before a board review, we saw a jump in abandonment at account setup, and I had to figure out what to do about it without blowing up the sprint plan or the roadmap we'd already committed to.

Interviewer: What first alerted you to it?

Participant: Our weekly funnel dashboard. Drop-off at account setup increased 32% over three weeks, which was unusual because upstream traffic and acquisition numbers hadn't shifted. At that stage the dashboard only broke things down at a fairly coarse level, so I could see something had changed but not exactly where in the flow people were leaving. The VP of Product wanted an explanation fast because activation rate is one of the numbers the board tracks closely. Sales was also getting questions in a couple of active deals about whether we had more guided setup options, since that had come up in demos. Engineering had a full sprint already, mostly enterprise bug fixes.

Interviewer: What was your objective at that point?

Participant: Immediate goal was to understand the cause well enough to act. Longer term, protect activation rate and have something credible to show the board, without pulling engineering off commitments that mattered to existing customers.

Interviewer: Walk me through what happened, roughly in order.

Participant: First few days were spent figuring out whether the dashboard number was even reliable, then narrowing down where in the funnel people were dropping. Once we had a clearer signal, I had to decide how to respond — that's the piece that took the most judgment. After that came a staffing call, since the response required engineering time we didn't really have spare. Then, closer to the board date, there was a launch decision under time pressure with incomplete testing.

Interviewer: Let's start with the first decision — how you investigated.

Participant: Right. I had the 32% increase, no user feedback yet, and a note from our analyst that payment-step instrumentation was incomplete. Options were: commission proper interviews, which research said would take two weeks to get sessions running; do a fast internal analytics and heatmap pass; or scan what competitors were doing for quick context. I went with the analytics pass plus a light competitor scan, and deferred interviews. Five weeks isn't much runway once you add design, build, QA, and release, so waiting two weeks just for interviews to start felt like too much of the budget gone before we even had a direction.

Interviewer: Any downside to skipping interviews at that stage?

Participant: Sure — analytics tells you where people drop, not always why. I flagged that trade-off to the team and kept research on standby in case the data stayed ambiguous.

Interviewer: What came out of that analysis?

Participant: The sharper signal was abandonment right after the payment-detail field, concentrated in a newer account subgroup — about 140 users. Small, and the cohort had only existed a month, so I wasn't fully confident it was stable. The heatmaps showed some repeated field edits around payment, but because instrumentation there was incomplete, I couldn't tell if that was a validation error or people just backing out.

Interviewer: That brings us to the second decision — choosing how to respond.

Participant: This was the harder one. I had two things in front of me. On one side, the payment-field signal, real but statistically thin. On the other, our Sales director told me two active enterprise deals had specifically asked, during demos, whether we had a more guided setup experience — not a general market comment, two named accounts with real revenue attached. Around the same time I'd noticed a few competitors had shipped something similar, but that wasn't really what drove the call for me.

Interviewer: What did drive it?

Participant: Honestly, it was close. The deal-specific requests gave me something concrete to point to — an actual account, an actual objection in a sales cycle — whereas the internal cohort data, while suggestive, was small enough that I didn't want to bet three sprints on it alone. I decided to build the guided setup wizard, partly because of those two deals, partly because I wasn't confident the payment-field fix alone would move the number given how thin the sample was. I'll be honest, if I look back at it, I'm not entirely sure I weighted that correctly — it's possible a more targeted fix would have addressed the real problem faster, or it's possible the deal risk was the right thing to prioritize. I don't think the data gave a clean answer either way.

Interviewer: Did you consider testing both directions before committing?

Participant: Our analyst suggested a small controlled comparison — one version fixing payment fields, another adding limited guidance — before committing engineering time. I didn't go that route because it would have delayed a decision the deals needed answered, and because I felt the payment data alone wasn't strong enough to anchor the whole response.

Interviewer: If those two deals hadn't come up, would you have decided differently?

Participant: Probably, yes. Without that pressure I think I'd have leaned toward the payment-field fix first and treated broader onboarding changes as a separate, later initiative.

Interviewer: Third decision — staffing.

Participant: Building the wizard meant pulling two engineers off the bug backlog for three sprints. That backlog had real enterprise-reported defects sitting in it. Sales wanted the wizard ready to reference in the two deals. I chose full reallocation rather than splitting time or delaying, because a split effort usually means both things ship late and half-tested, in my experience.

Interviewer: What followed?

Participant: Two of those backlog tickets escalated in severity while the engineers were reassigned. Not an outage, but real friction for those customers. Wizard build stayed on schedule. Follow-up analytics also showed the payment-field friction hadn't changed, which wasn't surprising since we hadn't touched that code.

Interviewer: Fourth decision — the launch itself.

Participant: Four days before the board meeting, QA had only done partial regression testing, the canary group was too small to read cleanly, and payment abandonment was unchanged. Options were full launch, a longer 10% canary, or a one-week delay for better testing and instrumentation. I chose full launch. A longer canary wouldn't have given us clean results in time, and delaying meant showing up to the board with a plan instead of something shipped. Engineering and QA weren't thrilled, but agreed the risk was manageable with monitoring and a rollback ready.

Interviewer: What were the results?

Participant: No statistically meaningful change in activation rate versus the prior month, and support tickets kept mentioning the payment step. Not a disaster, but not the fix either. We shifted focus afterward to a proper look at the payment validation and getting the instrumentation gap closed.

Interviewer: With two more weeks before the board review, what would you change?

Participant: I'd have run that controlled comparison the analyst proposed, and probably gotten a handful of user sessions from the affected cohort before committing three sprints anywhere.

Interviewer: What information would have made the second decision clearer at the time?

Participant: A larger, stable sample showing payment friction was the dominant cause, or direct evidence from users about why they stopped there. Either would have given me more to weigh against the deal pressure.

Interviewer: And if the payment-field data had come from a larger cohort?

Participant: I think it would have carried more weight against the deal requests. Hard to say for certain — it's the kind of call where reasonable people could have gone either way with what we actually had.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IS_Ambigious_1}}",
  "occupational_domain": "{{Information Systems, human-computer interaction, and interaction design}}",
  "role": "{{Product Manager (Digital Platform)}}"
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
