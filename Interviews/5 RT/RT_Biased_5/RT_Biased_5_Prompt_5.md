You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time. Before we start, I want to confirm you're okay with me recording this for internal process-improvement purposes, and that we can talk candidly about a project that didn't go entirely to plan.

Participant: Sure, that's fine. This one's still fresh for me anyway.

Interviewer: Can you describe your role and what the project was meant to accomplish?

Participant: I'm the capital projects manager for a corridor interlocking replacement — we were swapping out an aging interlocking and signal system on one of our busiest commuter segments, integrating it with our PTC interface. Federal grant money covered a good chunk of it, which meant a fixed obligation deadline. Miss it, and we risk losing part of the funding.

Interviewer: What made this project different from others you'd run?

Participant: The combination, really. Live revenue service running through the work zone, so we only had certain possession windows at night and weekends. A fixed-price design-build contract, so change orders were painful. And a hard federal clock ticking the whole time.

Interviewer: Walk me through what happened, start to finish.

Participant: We kicked off with a baseline schedule and budget. Then during early design we hit a scope question around underground utilities — old conduit, some of it undocumented. We made a call there and moved forward. Mid-construction, that came back to bite us: crews hit an unmapped high-voltage duct and we had a safety stand-down for a couple weeks. Contractor followed that up with a big risk report on cost and schedule impact. Then near the end, we had to decide how to handle systems integration testing with the deadline bearing down on us. We got through commissioning, the system passed, and we hit the funding deadline. But it was tighter than I'd like.

Interviewer: Let's go back to that baseline. What information did you have when you set the schedule?

Participant: The contractor's proposal assumed pretty efficient crew productivity — their best-case numbers. We also had data from a couple of peer agencies that had done similar interlocking swaps, and those ran 28 to 34 months typically. Leadership wanted to show the board real progress against the grant, so there was pressure to commit to something aggressive.

Interviewer: How did you weigh the contractor's numbers against those peer projects?

Participant: Honestly, I leaned on the contractor's proposal more. The peer projects weren't identical setups — different signal vendors, different corridor configurations — so I didn't think the comparison held up perfectly. We went with 24 months. I figured our team was sharper on execution than what those other durations reflected.

Interviewer: Did you revisit that historical range later, once things started slipping?

Participant: Yeah, once productivity started trailing plan, it looked a lot more like those other projects than I'd assumed going in.

Interviewer: Let's move to the utility question. What were you facing there, and what were your options?

Participant: Our utility maps for that stretch were over five years old, and the contractor flagged a few spots near the bore path where they weren't confident what was actually in the ground. We could pay for an updated survey — about $150,000 and three extra weeks — or proceed on the existing maps and manage anything that came up through our normal process.

Interviewer: What tipped it toward proceeding without the survey?

Participant: We have a solid weekly risk-review cadence, and a change-order tracking process that's pretty tight. I felt like if something came up, we'd catch it fast and deal with it through that mechanism rather than paying upfront to eliminate the uncertainty. It felt like an acceptable trade — spend the time and money there, or trust the oversight we already had running.

Interviewer: And what happened after that decision?

Participant: A few months into construction, crews struck a high-voltage duct that wasn't on any of our maps. Full stop on that segment for safety, about two weeks lost, plus the cost of the incident response and re-sequencing.

Interviewer: Looking back at that now, how foreseeable does it feel?

Participant: Honestly? In hindsight it feels almost obvious — that corridor's old, the utility ownership records were a mess, of course something was going to be down there that we didn't know about. It's the kind of thing you look at now and think, how did we not expect that.

Interviewer: At the time, though, how was that risk actually rated?

Participant: Our risk register had it logged as low likelihood. The team didn't flag it as a top concern going in.

Interviewer: Let's talk about the risk report the contractor sent after the strike. What did that process look like?

Participant: It was a substantial document — forty pages, laying out a projected 12 percent cost overrun and about ten weeks of schedule impact. Those numbers were bad enough that I didn't really want to carry them over to the grant side until the next monitoring cycle gave us something a little less ugly to bring forward. I had five business days to sign off. Problem was, that same week I was buried in quarterly board prep.

Interviewer: How did you handle the review given that?

Participant: I read the executive summary, delegated the detailed analysis to one of my leads, and told the team to keep monitoring things as they came in. I didn't ask my lead for a readout on what the detailed numbers actually showed, and I didn't loop in the grant administrator or escalate it up the chain at that point — I figured we'd get a clearer picture once the monitoring caught up.

Interviewer: Did the risk picture change in the following weeks?

Participant: It got worse before we brought it back into focus. We ended up escalating later and requesting a schedule accommodation from the grant side, which added its own headache.

Interviewer: Let's go to the testing decision near the end. What was the situation?

Participant: We had six weeks left before the grant obligation deadline. Standard systems integration testing protocol for this kind of interlocking work is eight weeks. Our signal engineering lead wanted the full eight weeks — no shortcuts. But the grants officer was clear that missing the milestone put around $4 million of funding at risk.

Interviewer: What alternatives did you consider?

Participant: We could ask the federal administrator for a formal extension and keep the full eight-week protocol, or compress testing to five weeks, trimming some of the redundant verification cycles, and hit the deadline as scheduled.

Interviewer: How did you land on compressing it?

Participant: We couldn't afford to lose that $4 million. That was really the driver. The engineering lead's case for the full protocol was sound, but against a funding number that size, protecting the grant took priority.

Interviewer: If the funding situation had been reversed — say that $4 million wasn't already secured, but finishing on time would have earned you an extra $4 million instead — do you think you'd have made the same call?

Participant: Probably not, honestly. If it were more like a bonus we might land versus something we already had in hand, I think we'd have leaned toward keeping the full eight weeks. Protecting money that was already ours felt different than chasing the same amount as upside.

Interviewer: How did the testing decision play out?

Participant: Testing finished in the compressed window, system passed, we hit the deadline and kept the funding. Whether those trimmed verification cycles matter down the road, I honestly don't know yet — too early to say.

Interviewer: If you'd had unlimited time and budget for that survey, would the utility decision have gone differently?

Participant: Probably, yeah — I'd have just paid for it and taken the three weeks. It wasn't that much money relative to the project.

Interviewer: If the grant deadline had had more flexibility, would the testing call have changed?

Participant: Almost certainly. Without that clock, I think we default straight to the full eight weeks, no debate.

Interviewer: What would you tell a peer walking into a similar fixed-price, fixed-deadline project?

Participant: Get your ground-truth data early, before you're locked into a schedule you can't easily unwind. And build in a real buffer against the funding clock so you're not making testing-scope decisions under that kind of pressure at the very end.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{RT_Biased_5}}",
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
