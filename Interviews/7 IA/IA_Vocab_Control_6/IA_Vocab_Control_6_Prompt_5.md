You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. This conversation is being recorded for internal process review, and I'll ask you to walk me through a specific shift in detail. Skip anything you're not comfortable discussing. Can you tell me your role and how long you've been doing it?

Participant: Sure. I'm a threat intelligence analyst on the SOC team, about four years in, mostly financial services environments. During shift I handle triage, attribution, and hunt scoping when something looks like more than commodity noise.

Interviewer: Good. Let's start broad. Can you walk me through what this shift looked like when the alert cluster first appeared?

Participant: About two hours into an overnight shift, EDR kicked out a cluster of alerts on a trading-support server — the box that feeds reporting data to the trading engine, not the engine itself. The auto-triage score came back Low. That queue does throw a lot of low-severity noise from that host, and I'd seen similar low scores turn out benign twice before. But I also remembered one shift where a Low score turned into something real, so I didn't want to just wave it through on pattern-matching alone.

Interviewer: What was your primary objective at that point?

Participant: Cover the queue efficiently without missing something that needed attention, and produce a handoff that would hold up. About three hours were left in the shift, so I wanted to be deliberate about where I spent time.

Interviewer: Take me through what happened next, chronologically.

Participant: After the Low score, I did a quick scan of the alert summary fields — parent process, any flagged child processes, whether the trading-support role tag showed anything unusual. Nothing in that quick look overrode the Low score, so I deferred the full manual log pull, which would've run fifteen to twenty minutes, but I noted it to revisit if anything else came in. About forty minutes later it did — an outbound connection to an unfamiliar IP. That's when I opened the case properly. I found a registry-key artifact matching a GreyFalcon campaign I'd tracked myself about six months back. At the same time, two things didn't fit cleanly: the C2 domain's registration pattern looked different from GreyFalcon's usual infrastructure, and there was an attempted connection to the HR benefits database, which isn't a target GreyFalcon has gone after before. I didn't want to commit to an attribution with those loose ends open. A vendor bulletin came in with five IOCs — a rare C2 protocol signature and two file hashes among them — and I used that to build a scope. Near the end of shift, I had a vendor bulletin and a colleague's more hedged internal notes to work from for the containment write-up, and I checked both against telemetry before finalizing.

Interviewer: Let's slow down and go through each decision individually. First — the initial Low-severity alert. What cues were you weighing right then?

Participant: The auto-triage score, the server's history of false alarms, and the absence of any reported business disruption. But I also pulled up the summary fields rather than just accepting the score outright.

Interviewer: What made you decide to do that quick scan instead of either accepting the score outright or doing the full pull immediately?

Participant: It was a middle option. A full manual pull is a real time cost — fifteen, twenty minutes — and I didn't have grounds yet to justify that against the rest of the queue. But taking the score completely at face value without even glancing at the summary felt like too much trust in a score that's generated from a limited rule set. The five-minute look was a way to catch anything obviously wrong without committing the full review time.

Interviewer: Did you consider escalating to the IR lead first?

Participant: Briefly, but there wasn't anything at that point to escalate — a Low score and a quiet business environment. I planned to revisit if anything changed, which it did forty minutes later.

Interviewer: Understood. Let's move to the attribution decision after the outbound connection appeared. What was the basis for your attribution call?

Participant: The registry-key match was strong — I'd documented that artifact myself in an earlier report, so I trusted it as a data point. But I didn't want to treat it as decisive on its own, because two things cut against it: the C2 domain's registration profile didn't match GreyFalcon's usual infrastructure, and the target — an HR database — wasn't something GreyFalcon has gone after in anything I've tracked. So I called it moderate confidence rather than high, and flagged both mismatches explicitly as things the hunt would need to test.

Interviewer: How did you handle the HR-targeting mismatch specifically? Did you have an explanation for it?

Participant: I didn't try to force one. It's possible there's a reason a GreyFalcon operator would go after HR data, but I didn't have evidence for that, so rather than guess at their motive I just left it as an open inconsistency — something that either gets explained by more evidence or ends up pointing away from this actor entirely.

Interviewer: Let's talk about the hunt scope decision once the vendor bulletin came in. How did you decide what to include?

Participant: The bulletin listed five IOCs — the protocol signature and two file hashes among them, not really ranked by the vendor in any stated order. I started with the two file hashes first, since they're more specific and carry a lower false-positive risk technically, and treated the protocol signature as a second pass to expand into if the first pass didn't resolve things. It wasn't about which one stood out most on the page — it was about which ones would tell me the most per unit of hunt effort.

Interviewer: Did the business preference for a narrow scope influence that?

Participant: A bit — trading-adjacent systems are sensitive to downtime, so starting narrow and staged was partly about not disrupting things unnecessarily. But the sequencing itself was based on which indicators were more diagnostic, not on convenience alone.

Interviewer: Last decision point — the containment recommendation. You had the vendor bulletin and your colleague's notes. How did you decide between them?

Participant: I didn't pick one over the other outright. The vendor bulletin was well-formatted and specific; the colleague's notes were hedged but, as far as I could tell, accurate. I checked specific claims from both against the telemetry I had — did the timestamps line up, did the described behavior match what we actually saw — and both held up partially. So the recommendation ended up blending the vendor's specific technical steps with the broader precautionary scope from the internal notes, because that's what the corroborated evidence supported, not because one read more convincingly than the other.

Interviewer: How confident were you overall in the final recommendation you handed off?

Participant: Moderate, maybe six out of ten. There was still an open question about attribution and an unresolved partial match on an additional host from the scope sweep, so I flagged both for next-shift follow-up rather than presenting it as closed.

Interviewer: Looking back, if you'd pulled the raw logs immediately in phase one instead of doing the shorter scan, how might things have unfolded?

Participant: I might have caught the outbound connection a little sooner, which could have given me more runway before the vendor window closed. Hard to know for sure — the summary scan didn't show anything that would've changed my initial call anyway.

Interviewer: If the vendor bulletin had listed its IOCs in a different order, do you think your scoping would have changed?

Participant: I don't think so. I wasn't going by the order they came in — I was staging based on which ones were more specific technically. If anything, reordering the list wouldn't have changed which ones I started with.

Interviewer: Is there a point in this sequence where you'd still want a second analyst's independent read before proceeding?

Participant: Probably the attribution step, just because of how much rode on it downstream. Even with the mismatches flagged, a second opinion on whether the registry-key match should carry as much weight as it did might have sharpened that call earlier rather than carrying open questions all the way through the hunt.

Interviewer: That's helpful, thank you. I think that covers what I need.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IA_Vocab_Control_6}}",
  "occupational_domain": "{{Intelligence analysis and information-intensive analytic work}}",
  "role": "{{Cyber Threat Intelligence Analyst}}"
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
