You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a cognitive task analysis session—I'll be asking about a specific incident you worked through, and I'd like your candid recollection of how you reasoned through it, not a polished after-the-fact summary. Everything stays anonymized. Is that okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me your role and what you were responsible for during this incident?

Participant: I lead a five-person team on our internal analytics platform—basically the tooling our support organization uses to look up customer accounts, usage history, that kind of thing. I own delivery for that dashboard and I report into the VP of Engineering. During this period I was accountable for keeping the platform stable and also for a demo we had coming up for leadership.

Interviewer: Can you walk me through what first alerted you to a problem?

Participant: Load times on the dashboard started creeping up—support tickets came in complaining pages were taking six, seven seconds instead of two. Over about two weeks it basically tripled. We hadn't touched much in that subsystem recently except our caching layer, which we'd built in-house—we call it QuickCache—about eight months earlier.

Interviewer: What did you do first?

Participant: I had two real options—run broad instrumentation across the whole stack to be safe, or go straight at QuickCache since it was the most recent change and the timing lined up. We were also getting pressure from the support lead because tickets kept climbing, so I didn't want to spend a week doing exhaustive profiling everywhere. I told the team to profile QuickCache specifically first, since it was the most likely suspect given the timing, and if that came back clean we'd widen the net.

Interviewer: What came out of that?

Participant: Profiling confirmed QuickCache was adding real latency under high load—invalidation was firing more than it should, forcing extra database round-trips. It also surfaced a separate, unrelated issue: a missing index on one of the support tables. Neither of those was hugely surprising, but it did mean two independent things needed fixing, not one.

Interviewer: How did the investigation affect team workload?

Participant: Priya, who originally built QuickCache, took point on diagnosing the invalidation logic. Dev, one of our other senior engineers, has also worked deep in that code. Everyone else picked up the index fix and other tickets. That's roughly how the two weeks split.

Interviewer: Let's step through it chronologically. After profiling confirmed the QuickCache issue, what was the next major decision?

Participant: That's where it got harder. QuickCache had taken us about eight months to build and stabilize—three separate patch rounds just to get it production-ready in the first place. Priya was adamant we were close, that one more targeted patch to the invalidation logic would fix it. On the other hand, there's a mature Redis-backed option out there that could probably replace QuickCache in about a sprint, with a track record we could actually point to.

Interviewer: What did you decide?

Participant: I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up. I figured one more focused patch, with the team that knows it best, would get us there.

Interviewer: What information did you rely on most heavily for that call?

Participant: Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily.

Interviewer: What happened after that decision?

Participant: The patch only bought us about fifteen percent improvement. Not enough to hit the demo deadline. And the extra sprint stretched the team thin on top of everything else going on.

Interviewer: Third decision point—who owned the urgent fix at that stage?

Participant: Right, so at this point we're down to days, not weeks. Dev has the deepest knowledge of QuickCache internals, but Dev had also been at the center of a production outage about three weeks earlier—a rushed deploy under pressure that caused a real incident, though the postmortem showed it was handled well and fixed fast. Marcus was the other option; he's been solid but has missed several deadlines over the past year, nothing dramatic, just a slower, steadier pattern of slipping.

Interviewer: What did you decide, and why?

Participant: I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet.

Interviewer: How did that play out?

Participant: Handoff was messy—Dev had context Marcus didn't, so there was friction getting him up to speed, and the fix took longer than it would have with Dev leading it outright.

Interviewer: Looking back, how did you weigh Dev's eighteen months of strong delivery against that one incident?

Participant: I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either.

Interviewer: With three days left before the demo, what did you decide about reporting status?

Participant: Latency was better but not fully resolved. I could've asked to push the demo, shipped quietly and hoped nobody noticed the remaining lag, or just told leadership straight where things stood. I went with transparency—laid out what was fixed, what wasn't, and proposed a follow-up sprint with monitoring in place. They accepted that.

Interviewer: What was the reasoning behind choosing that option over delaying the demo?

Participant: Delaying felt like it would cost more politically than it would gain technically—the partial fix was real progress, and monitoring would catch anything that slipped. Hiding it wasn't really on the table once I thought about it seriously.

Interviewer: If you'd had the profiling data suggesting a structural rework earlier, would that have changed your patch-versus-switch decision?

Participant: Possibly. If I'd seen it that clearly before committing the extra sprint, I might have pushed harder for the parallel evaluation option instead.

Interviewer: If Dev's outage had happened a year earlier rather than three weeks before this decision, would you have assigned the fix differently?

Participant: Probably, yeah. With more distance from it, I likely would have just given it to him outright given his familiarity with the system.

Interviewer: Anything you'd tell a peer facing a similar in-house-build-versus-alternative call?

Participant: Try to separate how much you've already put into something from what it's actually going to cost you going forward. Easier said than done when your team's pride and expertise are wrapped up in it.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IS_Biased_2}}",
  "occupational_domain": "{{Information Systems, human-computer interaction, and interaction design}}",
  "role": "{{Software Engineering Team Lead}}"
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
