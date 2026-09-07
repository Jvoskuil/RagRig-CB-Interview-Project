You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time. Before we start, I want to confirm you're okay with me recording this for internal process-improvement purposes, and that we can talk candidly about a project that didn't go entirely to plan.

Participant: Sure, no problem. It's a good one to talk through.

Interviewer: Can you describe your role and what the project was meant to accomplish?

Participant: I'm the capital projects manager for a corridor interlocking replacement — swapping out an aging interlocking and signal system on one of our busiest commuter segments, integrating it with our PTC interface. Federal grant money covered a good chunk of it, so we had a fixed obligation deadline. Miss it, and part of that funding is at risk.

Interviewer: What made this project different from others you'd run?

Participant: Live revenue service running through the work zone, so limited possession windows at night and weekends. A fixed-price design-build contract, which makes change orders painful. And that federal clock running the whole time.

Interviewer: Walk me through what happened, start to finish.

Participant: We set a baseline schedule and budget up front. During early design we had a utility-survey question — the corridor's underground records were old — and we decided to commission an updated survey before locking the schedule. That survey came back mostly clean, but it flagged one segment where the position data had a stated tolerance, meaning the utility was there but not pinned down precisely. We handled that finding a certain way. Mid-construction, crews still hit a conduit conflict in that exact segment, and we had a shorter safety stand-down than you'd get from a totally unknown strike, but a stand-down all the same. Contractor followed with a risk report on the cost and schedule impact. Then near the end we had to decide how to run systems integration testing against the deadline. We got through commissioning, the system passed, and we hit the funding deadline, but it was tight.

Interviewer: Let's start with the baseline schedule. What information did you have?

Participant: The contractor's proposal assumed efficient crew productivity — their best-case numbers. We also had data from peer agencies that had done similar interlocking swaps, running 28 to 34 months typically. Leadership wanted visible progress against the grant, so there was pressure to commit to something aggressive.

Interviewer: How did you weigh those two data points?

Participant: I leaned harder on the contractor's numbers. The peer projects weren't identical — different vendors, different corridor layouts — so the comparison felt soft. We went with 24 months.

Interviewer: Once the survey added three weeks up front, how did that affect the schedule?

Participant: We didn't push the overall target out. We absorbed those three weeks by tightening later construction phases so the external date stayed at 24 months.

Interviewer: Let's go to the survey itself. What did the results tell you, and what did you do with them?

Participant: Utility maps had been over five years old, so we commissioned the updated survey — about $150,000 and three weeks. It came back solid overall, but one segment near the bore path came with a stated tolerance, something like two feet of uncertainty on exact position, because the underlying municipal records for that block were poor to begin with.

Interviewer: What were your options once you saw that tolerance note?

Participant: We could fund extra contingency time and budget specifically for that segment, or rely on our normal process — weekly risk reviews plus the field crew's verification work during excavation — to handle it as it came up.

Interviewer: Which way did you go, and why?

Participant: We didn't add contingency. Field crews verify positions as a matter of course before they dig in any segment, so it felt like that tolerance note was already covered by standard practice. I knew that verification would really only confirm the actual position once we were mobilized inside that possession window — so if something was off, we'd find out on the clock, not ahead of it — but that still felt like enough to keep the segment on plan. Two feet isn't a huge miss, and I didn't see it as something that needed separate budget.

Interviewer: What happened once construction reached that segment?

Participant: Crews still caught a conduit edge that was outside where the drawing showed it, inside that same flagged area. Shorter stand-down than a full unknown-utility strike would cause — a few days, not weeks — but it did stop work on that segment.

Interviewer: Looking back on that now, how foreseeable does it feel?

Participant: Honestly, the survey told us that segment was uncertain. So in hindsight, of course something was going to be slightly off there — it's almost obvious once you say it that way.

Interviewer: At the time, though, how was that segment actually rated?

Participant: Our risk register logged it as low residual risk once the survey came back. We treated the tolerance note as basically resolved by process, not as an open risk.

Interviewer: Let's move to the contractor's risk report. What did that process look like?

Participant: It came in projecting around a 6 percent cost overrun and about four weeks of schedule impact from the segment conflict. Those numbers weren't something I wanted to sit with heading into board season, honestly — reviewing and pushing that forward before the next monitoring cycle gave us anything better felt premature. I had five business days to sign off, and that same week I was buried in quarterly board prep.

Interviewer: How did you handle the review given that?

Participant: I read the executive summary, delegated the detailed analysis to one of my leads without asking for a real readout on what it actually showed, and told the team to keep monitoring. I didn't escalate to the grant administrator during that window.

Interviewer: Did the picture change in the following weeks?

Participant: It crept up a bit before we brought it into focus and eventually asked the grant side for a smaller schedule accommodation than we would have needed with a full unmapped strike.

Interviewer: Now the testing decision near the end. What was the situation?

Participant: Six weeks left before the grant deadline. Standard systems integration testing runs eight weeks. Our engineering lead wanted the full eight, no shortcuts. Grants officer was clear that missing the milestone risked about $4 million of funding we already had secured.

Interviewer: What alternatives did you weigh?

Participant: Request a formal extension and keep the full eight weeks, or compress to five weeks, trimming some redundant verification cycles, to hit the date.

Interviewer: How did you land on compressing it?

Participant: We couldn't afford to lose $4 million that was already ours. That was the deciding factor, even though the engineering lead's case for the full protocol was solid.

Interviewer: If that $4 million had instead been potential new funding you could gain by finishing on time, rather than money you already had, would the call have gone differently?

Participant: Probably, yeah. If it were more like a bonus on the table instead of something already secured, I think we hold the full eight weeks. Losing money we already had in hand felt different from missing out on the same amount.

Interviewer: How did testing play out?

Participant: Finished in the compressed window, system passed, we hit the deadline and kept the funding. Whether the trimmed verification cycles matter down the line, I honestly don't know yet.

Interviewer: What additional information about that tolerance zone would have changed your decision not to add contingency?

Participant: If the survey firm had given us a tighter confidence range, or flagged that segment as a priority-verify area rather than routine, I think we'd have budgeted differently.

Interviewer: Looking back, was the conflict something the team could have anticipated?

Participant: The information was there. We just read the tolerance note as already handled rather than as a live risk.

Interviewer: What would you tell a peer facing a similar project?

Participant: Get your survey done early, but don't stop there — treat any flagged uncertainty as an open item with its own budget line, not something your normal process automatically covers. And build real slack against the funding clock before you're forced into testing-scope decisions at the end.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{RT_Counterfactual_5}}",
  "occupational_domain": "{{Rail Transportation}}",
  "role": "{{Project Manager / Capital Projects Manager (Rail Infrastructure)}}"
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
