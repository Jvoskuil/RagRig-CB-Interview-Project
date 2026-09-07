You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{**Interviewer:** Thanks for making time for this. Just to confirm, this is a routine debrief — I want to walk through a specific job you handled, how you made the calls you made, what information you had at each point. Nothing here is about assigning fault. Can you tell me your role?

**Participant:** Sure. I'm a Maintenance-of-Way Supervisor, I run a panel tie gang on the secondary main. I've got about eleven years in track maintenance, six as a supervisor. I handle scoping, scheduling, crew assignment, coordination with dispatch and the roadmaster on outage windows.

**Interviewer:** Good. Tell me about the incident you flagged for this conversation.

**Participant:** We had an ultrasonic rail flaw car come through and flag a detail fracture indication at mile post 47.3 — that's a curve on the secondary main. Dispatch gave us a 60-hour track window to get in there, pull the bad rail, do tie renewal on the segment, get it tamped and squared, and get the slow order lifted before a contracted freight customer's holiday surge started. There was a penalty clause in that contract tied to when the slow order came off, so timing mattered a lot to the regional office.

**Interviewer:** What was your main objective going in?

**Participant:** Get it done safe, get it done in the window. Those two things are supposed to line up, but this one had some tension in it — rain was forecast within about 48 hours, which cuts into ballast curing time, and we only had one tamper and one ballast regulator, shared with the gang working the adjacent territory. So there wasn't a lot of slack.

**Interviewer:** Walk me through what happened, start to finish.

**Participant:** The flaw car report came in on a Tuesday morning. Our last full inspection on that curve was about two weeks old, and it had rated the ties as fair, some deterioration noted, nothing urgent. I used our standard production rate for a 500-foot renewal — so many ties an hour with a full crew — and built a 60-hour schedule off that, plus the fair rating. We mobilized that afternoon.

Once we started pulling ties Wednesday morning, the count came in higher than what I'd planned for — more of them were rotted through than the fair rating suggested. So the roadmaster, two of our inspectors, and my foreman got together that afternoon to talk about how to handle the revised scope inside the same window. The foreman pitched running an extra tamper pass and cutting ballast dwell time to make up the lost hours. One of the inspectors mentioned a similar-looking curve we'd worked three years back that came in light on tie count too, and it held up fine long-term. That gave the room some confidence, and we went with the faster method.

By Thursday's mid-course check-in with the regional engineering manager, we were still behind where the revised plan said we should be, though some segments were actually ahead of pace. I gave him my read on the status. Then Friday morning, six hours before the freight window opened, we hadn't gotten the geometry car through yet — only manual gauge checks — and I had to decide whether to hold the slow order or lift it.

**Interviewer:** Let's go back to Tuesday. What made you comfortable locking in that 60-hour schedule off the fair rating and the standard rate table?

**Participant:** Honestly, the fair rating was the most recent data point I had, and the production table's what we use on every job like this — it's not something I second-guess unless there's a specific reason to. There is a longer defect history on that segment in our system, going back five years, that tracks flaw growth over time. I didn't pull it. At the time it felt like it'd just slow down getting the crew mobilized, and the two-week-old inspection seemed current enough to plan against.

**Interviewer:** Did anything about the flaw car flag itself suggest looking further back?

**Participant:** Looking back, probably. A detail fracture indication at that specific location wasn't the first flag we'd had there, I found out later. But at the time, I treated it as a standalone event and scoped it like a typical renewal.

**Interviewer:** When the tie count came back high on Wednesday, how did the group land on the faster method?

**Participant:** We talked through it for maybe twenty minutes. Nobody walked in pushing hard either way — my foreman had a proposal, the inspectors had questions about dwell time and compaction. But once the prior curve came up, the one that "always held up fine" with a lighter tie count, the room's mood shifted. By the end, everybody was more on board with running fast than any one of us had been at the start of that meeting.

**Interviewer:** Was that prior curve comparable in other respects — soil, drainage?

**Participant:** Not exactly, no. Our site report from the day before had actually flagged the subgrade drainage at 47.3 as worse than typical for that district. Nobody brought that back up once the other curve got mentioned. It just didn't come up again.

**Interviewer:** On Thursday's status call, how did you frame things for the regional manager?

**Participant:** I told him we'd had a late ballast delivery and lost some hours to a rain delay overnight, which was true, both happened. For the segments that were tracking on pace, I credited the crew's execution and the call to add the extra tamper pass. He signed off on keeping the existing timeline.

**Interviewer:** Did the original scope estimate come up as a factor in the slippage?

**Participant:** Not really, no. I didn't bring it up in that call. In hindsight it probably belonged in the conversation, since the tie count coming in high was part of why we were behind in the first place.

**Interviewer:** Friday morning — six hours out from the window opening, geometry car not through yet. What went into that call?

**Participant:** The penalty clause was the thing sitting heaviest on me at that point. Missing that window meant a real financial hit to the region, and I didn't want to be the reason for that. I knew the geometry car would give us a continuous read across the whole segment that manual checks just can't match, but with that loss already sitting right in front of us and the verification still open-ended, avoiding the hit was what drove the call more than anything else. We'd done manual gauge spot-checks across the segment and they came back clean, and I'd set up extra hand-inspection rounds plus a pilot train running the curve at reduced speed before we opened it to normal traffic. The roadmaster pointed out that the hand rounds and the pilot train wouldn't give us the same continuous profile the car would, but I figured between what we already had and those extra rounds, we'd catch anything that mattered. Between those, I felt like we had the risk covered well enough to lift the slow order without waiting on the geometry car.

**Interviewer:** What was the alternative you weighed against that?

**Participant:** Holding the slow order until the geometry car actually ran it, even if that meant eating the penalty. We talked about it briefly with the roadmaster, but the inspection rounds and the pilot train felt like enough of a safety net that we didn't need to wait.

**Interviewer:** What happened with the geometry car pass?

**Participant:** It ran the next day and came back within tolerance. So the track was fine. But I'll say that doesn't necessarily tell you whether lifting it early that morning was the right call or just the way it worked out.

**Interviewer:** If you'd had that five-year defect history in hand on Tuesday, what do you think would've changed?

**Participant:** Probably the initial schedule. If I'd seen recurring flaw growth at that spot, I'd have scoped it heavier from the start instead of finding out mid-job.

**Interviewer:** If the contract penalty hadn't existed, would Friday's decision have gone differently?

**Participant:** I think I'd have been more willing to just wait for the geometry car. It wasn't the only factor, but it was a big part of why six hours felt urgent instead of just cautious.

**Interviewer:** Last one — if a different inspector had been in that Wednesday meeting, someone without that prior-curve story, do you think the method decision changes?

**Participant:** Maybe. That story didn't have hard data behind it, just a memory of how a similar-looking job turned out. Take it out of the room and the conversation might've stayed more cautious. Hard to say for sure.

**Interviewer:** That's helpful. Thanks for walking through it in this much detail.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{RT_Biased_7}}",
  "occupational_domain": "{{Rail Transportation}}",
  "role": "{{Maintenance-of-Way Supervisor / Track Maintenance Supervisor}}"
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
