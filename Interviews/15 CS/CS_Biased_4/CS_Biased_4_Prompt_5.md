You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a debrief on the finance-server incident from a few weeks back, it's being recorded for internal process review, and you're free to skip anything you're not comfortable detailing. Sound okay?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start with your role that night and what you were responsible for?

Participant: I'm the on-call DFIR analyst, so I was solo overnight — it was a Sunday going into quarter-end close, which matters because that file server is basically untouchable without a director sign-off during that window. My senior lead was reachable on chat but not really available to jump on calls. So triage, scoping, containment, remediation — all of it was on me until morning.

Interviewer: Walk me through what happened.

Participant: Around 1 a.m. I got a SIEM alert for an off-hours process spawning a staging directory on the finance file server. Honestly, my first reaction was "here we go again" — I'd closed six tickets in the past three weeks that all started exactly like this, staging directory, off-hours process, and every one of those turned out to be ransomware-precursor activity. So the pattern was extremely familiar. There was also a quieter log line underneath it — a single authenticated session copying files in small batches out to an external cloud storage endpoint over a few hours. But no ransom note, no encryption, no mass renaming, so nothing screaming "this is it" yet.

Interviewer: How did you weigh those two signals?

Participant: I opened the ticket under the ransomware-precursor category. That staging-directory behavior is just what I've been seeing constantly lately, so it felt like the obvious bucket. The batch-copy line registered, but it felt secondary — slower, quieter, didn't match the urgency of what I'd been dealing with recently. In hindsight, when I actually looked at what was in those batches later, they were finance close spreadsheets, not the file types those recent ransomware precursors usually go after. And the external endpoint had no ransomware C2 history in threat intel. But at 1 a.m. I went with the category that matched what I'd just spent three weeks fighting.

Interviewer: Let's reconstruct the rest of the timeline. What came next?

Participant: Within the first ten minutes I set the ticket scope at 3 endpoints, based on the initial SIEM correlation window. About 40 minutes later, an EDR sweep came back showing authentication artifacts touching 9 more hosts — lower confidence, but there. Around then, the finance director started pinging for an update ahead of the 6 a.m. close deadline, so there was real pressure to say something concrete. I decided the 9-host signal was probably noise from that same original window and kept the scope close to 3. A later, fuller sweep ended up confirming lateral movement had actually touched 7 of those 9 hosts.

Interviewer: What made you treat that second signal as noise rather than expansion?

Participant: Partly the confidence rating on it, it wasn't a clean hit. But I'll be honest, I'd already told the director "3 hosts, contained," and adjusting that number upward with only 40 minutes of new low-confidence data felt like it'd cause more panic than it was worth before I had something firmer. So I stuck close to the original number and figured I'd revisit if something else lit up.

Interviewer: Move on to containment. What did you actually do?

Participant: I ran my own PowerShell isolation and log-collection script — I wrote that thing two years ago, and it's worked well on plenty of past incidents. My lead pinged me suggesting I use the EDR platform's one-click network isolation feature instead, said it'd be faster and less error-prone, especially now that we were looking at more hosts. That feature's only been live about three months and I've used it maybe twice.

Interviewer: What went into sticking with your script over that suggestion?

Participant: I know exactly how my script behaves, what it logs, where it's failed before and how I fixed that. The EDR feature, I just don't have the same feel for it yet. My lead's point about the host count was fair, and I didn't really have anything showing my script would hold up better at that scale — I just wanted to give it the benefit of the doubt because it's mine, I built it, I've kept it running this long, and it felt like it deserved the first shot before I'd fall back on the platform's version. So I kept running my script across the hosts, and only tried the EDR isolation on a couple of them after my lead brought it up a second time. In the end, isolating everything with my script took a good 90 minutes longer than the EDR route probably would have at that host count. It wasn't built for a scope that size, honestly, it's more of a one-or-two-host tool.

Interviewer: Did the delay change your view of which tool to use for the rest of containment?

Participant: Not really in the moment — I was mid-process and switching tools halfway through felt like it'd create more inconsistency in the logs than just finishing what I started.

Interviewer: Let's talk remediation. What options were in front of you?

Participant: The ticketing system's playbook for that category gave me exactly two actions: reset affected credentials, and reimage the affected endpoints. Neither one said anything about preserving a forensic image of the staging directory first, or checking whether that external cloud endpoint triggered any legal notification requirement.

Interviewer: Did you consider anything outside those two?

Participant: There's an escalation path to our external IR retainer that could've given a broader set of options, but it's not built into the playbook flow, you have to go looking for it separately. I didn't go down that road. I just worked through the two actions on the screen since that's what the category pointed me to.

Interviewer: Was there a point where that choice got revisited?

Participant: Two days later, compliance asked whether we'd preserved a forensic image of the staging directory before reimaging, since that affects whether this gets reported as a data exposure. That's when it became clear the playbook's two options hadn't covered that angle at all.

Interviewer: Looking back, if the staging-directory pattern hadn't been so common in your recent caseload, do you think you'd have categorized this the same way?

Participant: Probably not as quickly. If I hadn't just closed six of those tickets, I think the batch-copy line would've stood out more on its own merits instead of getting overshadowed.

Interviewer: If the EDR isolation feature had been the tool you knew best instead of your script, would containment have gone differently?

Participant: Almost certainly faster. I think I'd have reached for it first instead of treating it as the backup option.

Interviewer: And if the playbook screen had shown four remediation options instead of two?

Participant: Hard to say for sure, but I'd like to think the forensic-preservation piece would've been visible instead of something I only heard about after compliance asked.

Interviewer: Last question — what's one point where more time or information would have changed your approach?

Participant: Probably right after that second EDR sweep. If I'd had another 20 minutes before the director needed an answer, I think I'd have pushed the scope number instead of holding it, and maybe things downstream would've looked a bit different.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{CS_Biased_4}}",
  "occupational_domain": "{{Cyber Security}}",
  "role": "{{Incident Responder (Digital Forensics and Incident Response)}}"
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
