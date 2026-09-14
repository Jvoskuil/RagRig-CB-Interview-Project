You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for sitting down with me. This is part of a research review on design decision-making, it's recorded, nothing gets tied to your name, and you can pass on anything you'd rather not get into. Okay?

Participant: Sure, no problem.

Interviewer: Tell me about your role on this project and what it involved.

Participant: I was lead design engineer on a sprinkler retrofit for a distribution warehouse, 140,000 square feet, tilt-up concrete. The owner was bringing in a new third-party logistics tenant who needed part of the floor converted to high-piled rack storage, double-row selective rack up to 32 feet. I had to redesign the existing system, which was sized for a lighter occupancy, get it through plan review, and get it installed before the tenant's lease started.

Interviewer: How did the schedule on this one compare to a typical retrofit?

Participant: Actually pretty comfortable, for once. We had six weeks from kickoff to permit submission, which is more breathing room than I usually get. The existing water supply and riser sizing were still set up for the old, lower-hazard use, so that part of the challenge was still there, but I wasn't fighting the calendar the way I sometimes am.

Interviewer: Walk me through the incident from the start.

Participant: Early on I needed to settle the commodity classification, since that drives the density, the rack sprinkler requirements, everything downstream. I didn't have a finalized SKU or packaging list from the tenant yet, they were still working that out on their end, and the owner wanted the classification locked so he could fix the retrofit budget. There wasn't really a schedule reason it had to happen that week, I could have waited and asked for a sample of their packaging list, but I'd done two other jobs for similar 3PL operators and had a good sense of what that kind of tenant typically stores. I went with Class III based on that pattern and moved on. Then I pulled the NFPA density and area curves for that classification at 32 feet, picked a point that cleared the code minimum, and built the hydraulic calculations. There was still plenty of runway before submission, so I could have run a few more combinations against the actual rack layout, but I didn't loop back to compare. That package went to the owner, who wanted a value-engineering pass since it came in over budget, and we talked about trimming the in-rack sprinkler allowance. Once the system was installed, we got to commissioning, and with the schedule no longer tight, we did the full witnessed flow test without any rush.

Interviewer: Let's reconstruct that in order. What happened first?

Participant: Classification, in the first week or so. Density and area selection maybe two and a half weeks in. Value engineering came after plan review comments, around week four. Commissioning was near the end, but we still had days to spare before move-in.

Interviewer: What did you learn after the classification that you didn't know when you made it?

Participant: A partial inventory list came in later and showed more exposed unexpanded plastics mixed with the cartoned goods than I'd assumed, closer to a plastics classification than straight Class III.

Interviewer: Going back to that first call, what did you actually have in hand, and how much time did you have to get more?

Participant: I had the tenant's general business type and my history with two comparable clients. I didn't have their SKU list, but with six weeks on the clock, I probably had time to ask for a preliminary sample and wait a bit.

Interviewer: Did you consider requesting that data before finalizing?

Participant: I thought about it briefly. But in my experience, this type of tenant runs cartoned retail goods, maybe some mixed packaging, and both of the prior jobs landed at Class III. I went with that pattern instead of waiting on their list.

Interviewer: If you'd had the SKU list before classifying, would you have done anything differently?

Participant: Probably, yeah, if the plastics share had been visible upfront I'd have leaned more conservative from the start.

Interviewer: What would have made you press for that data given you had the time?

Participant: Something specific standing out, like if they'd mentioned electronics or aerosols. Nothing in the early conversations flagged that, so it didn't feel urgent to chase down.

Interviewer: Moving to the density selection. What alternatives were actually available to you?

Participant: Several density and area points would have satisfied code minimum for Class III at that height, some needing more in-rack sprinklers. I could have compared those against the specific rack configuration and aisle widths, or checked the manufacturer's guide for something tailored to the layout.

Interviewer: With several weeks still on the calendar, what determined which one you picked?

Participant: I took the first point that cleared the minimum for the assumed classification and built the calc package around it. I had the time to run more comparisons, honestly, I just didn't loop back once I had something that worked.

Interviewer: Did the plan reviewer comment on that later?

Participant: Yeah, flagged that the point I'd chosen was close to the edge of the applicable curve for the actual rack configuration. Not a rejection, just a note to be aware of.

Interviewer: What went through your mind when the owner asked for value engineering?

Participant: He wanted the number under budget, and the in-rack allowance was the biggest thing I could trim. Keeping it would've given more margin against the classification uncertainty I already knew about. But we've got two more retrofit jobs pending with him, and I didn't want friction over one line item, so I recommended pulling the allowance to hit his number.

Interviewer: Did you walk him through the classification uncertainty as part of that?

Participant: Not in much depth. I mentioned it, but I framed the removal as a reasonable trade rather than spelling out how much margin we'd be giving up.

Interviewer: If there'd been no ongoing relationship with the owner, would that conversation have gone differently?

Participant: Possibly. I'd like to think I'd have pushed harder to keep the allowance, but I can't say for sure.

Interviewer: Last decision point, commissioning. What determined the testing you pursued?

Participant: The AHJ requires the witnessed flow test regardless, and with days to spare before move-in, there wasn't a reason to cut corners. I did the full test.

Interviewer: How did it turn out?

Participant: Passed comfortably, well above the required minimum. No concerns there.

Interviewer: Looking back, given that schedule wasn't really the constraint here, is there a decision you'd make differently?

Participant: The classification, still. Everything downstream followed from that first call, and I had the time to ask for more data before locking it in. I just didn't use it that way.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HE_Counterfactual_3}}",
  "occupational_domain": "{{High-risk Engineering and Fire Engineering}}",
  "role": "{{Fire Protection System Designer (Sprinkler/Suppression Design Engineer)}}"
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
