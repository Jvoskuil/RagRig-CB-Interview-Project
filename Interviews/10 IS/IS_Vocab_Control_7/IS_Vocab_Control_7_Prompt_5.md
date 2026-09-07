You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the LumenKit evaluation, not whether the outcome was "right." Everything stays in the design systems research archive. Sound okay?

Participant: Sure, happy to walk through it.

Interviewer: Can you remind me of your role and what triggered this whole evaluation?

Participant: I lead design systems for the platform org — three designers, two engineers under me. Legal flagged that we needed to hit WCAG 2.2 AA across two customer-facing squads within about ten weeks, and our internal component library had known contrast and focus-state debt. LumenKit came up because a couple of competitors use it and it's picked up some industry recognition.

Interviewer: What was your goal going into the vendor demo?

Participant: Mainly to see whether adopting something pre-built could shortcut months of remediation work, given the timeline.

Interviewer: Walk me through what happened, in order.

Participant: The solutions engineer ran about forty minutes, mostly on their accordion component — motion, keyboard handling, graceful degradation. Genuinely well done. They also said the library ships with AA-compliant color defaults. Rather than take that at face value, I asked for their contrast-ratio spec sheet on the core color and elevation tokens before deciding anything about pilot scope. When it came back, I noticed it only covered default, unthemed values — nothing about how those tokens would behave once we applied our own theming layer. That gap mattered, since our actual implementation would always be themed.

Interviewer: What did that lead you to do?

Participant: I scoped the pilot narrowly — just the token categories tied directly to our compliance gap, not the whole library — since the spec sheet couldn't tell me how the tokens would hold up once themed. We got a three-week sandbox limited to that smaller set. Both squad leads said they were interested but wanted pricing before committing engineering time.

Interviewer: Did anything push you toward a broader commitment at that point?

Participant: Not really. The demo was impressive, but impressive motion design on one component doesn't tell you much about contrast behavior on a different set of tokens, so I kept those separate in my head.

Interviewer: Let's move to licensing. What did that look like?

Participant: Procurement needed a recommendation in two weeks. Three tiers: Basic, five components, no support; Team, twelve components, limited support, priced not far below Enterprise; Enterprise, full library with dedicated support. I mapped what the narrow pilot actually needed against each tier's component list rather than just comparing the tiers to each other.

Interviewer: What did that comparison show?

Participant: Team actually covered our confirmed needs — the components we'd already scoped plus reasonable headroom for the second squad. Enterprise had things we weren't using yet. I recommended Team and flagged that we could revisit Enterprise later if adoption grew.

Interviewer: And the rollout timeline?

Participant: I hadn't set a date yet at that point. I asked both squad leads directly what their earliest realistic integration window was, given their existing release calendars, before committing to anything.

Interviewer: What did they say?

Participant: One could start in three weeks, the other in five. I set the rollout date to the later window rather than picking something in between and hoping it would work out.

Interviewer: What information would have changed that recommendation, looking back?

Participant: Honestly, not much — checking actual needs against the tier list and getting real calendar commitments from both squads is basically what I'd do again.

Interviewer: Let's get to the audit. What came back?

Participant: About seven weeks in, our internal accessibility audit found that several LumenKit color and elevation tokens failed contrast requirements in three of five tested components. I'd told the VP and both squad leads earlier that the defaults tested well in the initial spec review and pilot, but I'd also flagged at the time that full-scale testing was still pending.

Interviewer: What was your first move on the discrepancy?

Participant: I wanted to know whether the failure was in our theming layer or in the vendor's own default tokens, so I requested an independent retest of LumenKit's out-of-box tokens with no internal theming applied. I didn't want to guess at the cause.

Interviewer: What did the retest show?

Participant: It confirmed the failures originated in the vendor's default token values, not our theming. That was useful because it told us exactly which components needed to change.

Interviewer: What did you decide to do with that?

Participant: We'd put some engineering hours into customizing those tokens already, but once the retest pointed at the vendor defaults specifically, I reverted just the three affected components to our already-remediated legacy tokens and left the rest of the LumenKit components in place, since those had tested clean.

Interviewer: Did the VP or squad leads react?

Participant: The VP asked for a written explanation for the compliance file, which I could give directly from the retest data. Both squads were fine with the partial reversion once they saw which components were affected.

Interviewer: That brings us to the final call. What were the options three weeks before the deadline?

Participant: Expand LumenKit organization-wide, including the categories that had failed; adopt a hybrid — keep LumenKit's motion and layout components but source color and elevation tokens internally; or revert fully to legacy.

Interviewer: How did you weigh those?

Participant: The retest data was specific to color and elevation, not layout or motion, so a full revert seemed like it would throw away components that had actually tested fine. Full expansion seemed to reintroduce the exact risk we'd just found. The hybrid matched what the evidence actually showed — keep what tested clean, source internally what didn't.

Interviewer: So what did you recommend?

Participant: The hybrid. I documented the retest findings, the expected migration effort for each option, and the compliance risk if we expanded the failing categories anyway, and sent that to the VP and counsel before finalizing it.

Interviewer: If the audit had come in during week one instead of week seven, would your approach to the retest have changed?

Participant: Probably not the approach — I'd still want to isolate vendor tokens from theming before deciding anything. It might have just meant less customization work to unwind.

Interviewer: If the vendor's demo hadn't included that contrast-ratio spec sheet at all, do you think your initial pilot scope would have looked different?

Participant: I likely would have asked for one anyway before scoping anything broadly — a strong demo on one component isn't evidence about a different set of tokens.

Interviewer: If procurement had only offered two tiers instead of three, would Team still have been your pick?

Participant: Depends on what the two were, but I'd still have checked actual component needs against whatever was offered rather than picking based on how the options looked next to each other.

Interviewer: Starting over today, what would you keep, and what would you change?

Participant: I'd keep asking for direct evidence before scoping decisions and getting real commitments from the squads before setting dates. I'm not sure I'd change much — the one thing I'd tighten up is flagging the "pending full-scale testing" caveat more visibly in written updates, so it's not just something I remember saying.

Interviewer: This has been really useful. Thanks for walking through the reasoning in this much detail.

Participant: No problem — it's a good exercise to lay it out step by step like this.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IS_Vocab_Control_7}}",
  "occupational_domain": "{{Information Systems, human-computer interaction, and interaction design}}",
  "role": "{{Interaction Designer (Design Systems Lead)}}"
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
