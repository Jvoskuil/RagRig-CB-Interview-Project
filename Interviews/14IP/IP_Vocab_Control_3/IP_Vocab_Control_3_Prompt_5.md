You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a confidential process-improvement debrief, not part of any disciplinary record. Okay to proceed?

Participant: Yes, that's fine.

Interviewer: Can you describe your role and what you were responsible for during this incident?

Participant: I'm the Environmental/Safety Compliance Officer at the plant. I own air permit compliance site-wide, including the Solvent Recovery Unit in Building 3. My job here was to figure out what was actually happening, decide what needed to be reported under our Title V permit, and try to keep the production line moving if that could be justified.

Interviewer: Walk me through what happened.

Participant: At 6:40 in the morning, a VOC sensor near the SRU tripped above the action threshold. At that point there was nothing else—no complaints, no other data. We'd had two drift-related false alarms on that same sensor array in the past month, so I flagged that as relevant background, but I didn't want to just assume drift and move on. I sent a technician out with a handheld meter right away rather than waiting to see if anything else developed. About half an hour later, the hotline got a call about a chemical smell near the fenceline, which raised the stakes. The handheld readings came back elevated but in a grey zone—not clearly over the limit. We were also mid-batch on a large customer order due in two days, so an unnecessary shutdown wasn't something anyone wanted. I talked it through with the production supervisor and we agreed to tighten our sampling interval and schedule a full continuous emissions monitoring pull within a short, defined window rather than letting it drift indefinitely or shutting down that same morning. That held for about two days until a contractor doing unrelated maintenance work flagged a data logger showing sustained high readings during that exact alarm window. That's when we moved to a fuller investigation. I pulled the three-year maintenance history, which showed gasket seep as the most common cause of past VOC events here by a wide margin. I was also aware of a valve failure at our sister plant in Ohio a couple weeks earlier—big fine, local news, we'd covered it in a corporate webinar—but I didn't want that one dramatic case to drive where we looked first. I prioritized the gasket line based on the site's own history, and separately scheduled a quick, low-cost check of the valve as a precaution, given how bad a valve failure would be if it did happen. The teardown confirmed a worn gasket seal, consistent with our historical pattern. From there I had to decide how to calculate cumulative emissions, since the outcome affected whether we crossed into reportable territory under our 24-hour notification clock, with the production deadline two days out.

Interviewer: Let's reconstruct the timeline a bit more precisely. What did you do in the first thirty minutes?

Participant: I looked at the alarm log, noted the drift history, but didn't stop there—I dispatched the technician immediately to get independent field data rather than waiting to see if the alarm cleared on its own.

Interviewer: And between the odor complaint and the teardown?

Participant: The handheld readings came in that same morning. Then it was about two days of tighter monitoring until the contractor flagged the data logger, which is what triggered the deeper investigation.

Interviewer: When did the teardown findings come in relative to your reporting decision?

Participant: Right before. Once the gasket was confirmed, I moved straight into the emissions calculation question.

Interviewer: Going back to that first decision—how did you decide not to just classify it as drift outright?

Participant: The drift history was real, and it made drift a reasonable starting hypothesis, but two false alarms in a month isn't the same as certainty. I didn't want to commit to an explanation before I had any field data to check it against, so getting the technician out immediately felt like the right way to test the hypothesis rather than just assume it.

Interviewer: What information sources did you weigh before deciding on the CEM data pull, and how did you land on timing?

Participant: I looked at the grey-zone handheld readings, the cost of a partial shutdown—about $40,000 a day—and the fact that a full data pull would take real analyst hours we didn't have a lot of slack for. I talked to the production supervisor about the batch schedule. Rather than treating it as an all-or-nothing choice, we tightened the interim sampling and locked in a specific date for the full pull, so we weren't just sitting on ambiguous data indefinitely.

Interviewer: What alternatives did you weigh when deciding where to start the physical inspection?

Participant: Gasket seep versus the valve. The maintenance log made the gasket the statistically obvious first stop—it's what's caused nearly every minor event here for three years. The Ohio case was in the back of my mind because the consequences there were so severe, so I added a quick valve check as a low-cost precaution, but I was explicit with the team that the log, not the Ohio story, was driving where we started.

Interviewer: What was your basis for the exceedance calculation methodology?

Participant: I compared both calculation approaches against the permit language and how we'd handled similar situations in past audits, and picked the one that held up best under that precedent.

Interviewer: How much time pressure did you feel at each stage?

Participant: It was there throughout, especially with the production deadline, but it didn't override any single step—it mostly meant we had to be efficient about sequencing rather than skipping analysis.

Interviewer: How confident were you at each stage, and what would have shifted that?

Participant: Early on, moderate confidence at best—drift was plausible but unproven. By the time the data logger turned up, confidence dropped further until the teardown gave us a physical answer. Clearer field readings on day one would have resolved a lot of that uncertainty sooner.

Interviewer: If the sensor drift history hadn't existed, would your initial response have gone differently?

Participant: Probably not dramatically—I still would have wanted field confirmation before classifying anything, though I might have dispatched with a bit more urgency from the start.

Interviewer: If you hadn't known about the Ohio incident, would your inspection order have changed?

Participant: Honestly, I don't think so. The maintenance log was doing the real work there; the Ohio case just justified adding a cheap secondary check.

Interviewer: Looking back, what single piece of information, if available earlier, would have most changed your approach?

Participant: The data logger readings from day one. Getting those immediately instead of two days later would have let us move to the teardown that much sooner.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IP_Vocab_Control_3}}",
  "occupational_domain": "{{Industrial Production Processes}}",
  "role": "{{Environmental/Safety Compliance Officer (Manufacturing Plant)}}"
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
