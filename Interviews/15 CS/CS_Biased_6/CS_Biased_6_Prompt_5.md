You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm — this is for internal process research, not a performance review, and you can decline to answer anything. Okay?

Participant: Yeah, that's fine.

Interviewer: Can you tell me a bit about your role?

Participant: I'm a vulnerability management analyst on the security operations team. I triage scanner findings, vendor advisories, coordinate patch timelines with IT ops, and escalate anything that looks like active exploitation to incident response. I also chase our open findings backlog for compliance reporting.

Interviewer: Let's talk about the CVE that came in a few weeks back. Walk me through what happened.

Participant: It was mid-morning when a vendor advisory landed — a new CVE, CVSS 9.8, remote code execution, affecting our internet-facing authentication API. At the same time I had roughly forty open findings from the previous week's scan sitting in my queue, with forty-eight hours until our compliance audit report was due. One backlog item was an unpatched database server with excessive service-account privileges, open ninety-plus days. And the week before, there'd been a big breach in the news — a VPN appliance that hadn't been patched — it caused a mess for that company and was all over our internal Slack.

Interviewer: When the new CVE came in, what did you do first?

Participant: My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere. I moved it to the top of the queue and started routing it into our standard remediation workflow. The database finding stayed where it was.

Interviewer: Where did the routing go?

Participant: Into our web-application remediation queue. Honestly, when I saw "authentication" and "internet-facing" together, my head just went straight to the same kind of injection-style tickets that make up most of what crosses my desk — that's the pattern I see constantly, so it's the one that came to mind first. There was a line in the advisory pointing more toward the API-gateway team being the better owner, but I didn't stop on it long enough to change course, and it went into the usual queue.

Interviewer: Did you look closely at the advisory's technical detail before routing it?

Participant: I skimmed it — saw "authentication," saw "internet-facing," saw the CVSS score, and that was enough to know it needed to move fast. I didn't dig into the exploit chain right away because time was tight.

Interviewer: Later you found it wasn't quite a standard web-app issue?

Participant: Right — it turned out to be an authentication bypass in the API gateway, a different exploit path than the injection-style stuff that queue usually handles. It got redirected eventually, but that cost some time.

Interviewer: Going back to that first decision — the new CVE and the ninety-day-old database finding were competing for urgency. What made the new one win?

Participant: Honestly, it felt more urgent. The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull.

Interviewer: If you'd ranked them purely on asset criticality and exposure, independent of the news, how would that have gone?

Participant: The database server probably deserved more attention than I gave it. It ended up flagged by the audit team afterward as our most severe open item. But at the time, the CVE felt like the more pressing thing.

Interviewer: Later that day you were cross-referencing the CVE against the asset inventory when something else came up.

Participant: Yeah, while going host by host through the inventory, the SIEM threw an alert — "privilege escalation, low confidence" — on an internal box. That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on.

Interviewer: Was there anything specific in that alert that stood out?

Participant: There was a log entry with a lateral-movement timestamp that was a little unusual. I registered it existed, but I was heads-down trying to finish the asset match, so I didn't stop to dig in.

Interviewer: Was there anything else on that dashboard view at the time?

Participant: [pause] I'd have to think about that. I was really focused on the inventory cross-reference right then.

Interviewer: There was an anomalous outbound traffic entry flagged on that same host, visible in the same panel. Do you recall it?

Participant: I don't specifically remember it. I was scrolling through host records, not scanning that side panel. It's possible it was there and I just didn't register it — my attention was on matching CVE-affected assets, not general alert triage.

Interviewer: That entry was later linked to a confirmed low-level compromise on that host. Does that change how you see the decision to move past the alert?

Participant: It's easy to say now I should've stopped. At the time, given how often that label turns out to be routine, continuing with the task in front of me felt reasonable. I didn't have a strong signal telling me to drop what I was doing.

Interviewer: Let's talk about the change window request. What went into that?

Participant: IT ops needed written justification to approve an emergency window during business hours instead of the weekend cycle, since patching would disrupt customer transactions for about twenty minutes. I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast.

Interviewer: What did the exploitation data actually say?

Participant: The EPSS score put it at moderate probability, comparable to a handful of things we've handled on the normal weekend schedule over the past year. Not in the exceptional range.

Interviewer: So the justification leaned more on what the company could lose than on that probability figure?

Participant: Yeah, that's fair. When I sat down to write it, thinking through what we'd lose if it went wrong — the contract, the reputation hit, the audit exposure — made it feel like this had to move now. If I'd framed the same numbers around just getting ahead of the patch cycle or keeping things running smoothly, it probably wouldn't have felt as urgent to me, even though the underlying EPSS score and the twenty-minute disruption were exactly the same either way.

Interviewer: Did it work?

Participant: It did — they approved the window. Though nothing was actually observed exploiting that CVE the following week, so it's hard to say in hindsight whether the urgency was fully warranted.

Interviewer: Last decision point — finalizing which systems to patch.

Participant: The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out.

Interviewer: Did you check the asset inventory outside that default view?

Participant: Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture.

Interviewer: There were actually three more hosts with the same vulnerable library, tagged under a different asset category, visible in the inventory with a manual filter change.

Participant: One of those turned up still vulnerable in the follow-up audit scan a week later. A manual cross-check would have caught it, but with the clock running down, the scanner's output was what I had in front of me and it looked complete.

Interviewer: If the VPN breach hadn't been in the news that week, would you have triaged the CVE the same way?

Participant: Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding.

Interviewer: If the scanner had surfaced five hosts instead of two, would scoping have gone differently?

Participant: Probably — I'd have just patched whatever the tool showed me. I wasn't second-guessing whether the list was complete.

Interviewer: Anything you'd flag differently now?

Participant: The outbound traffic entry, for sure. And maybe relying less on how an alert label has resolved in the past versus what's specifically in front of me each time.

Interviewer: If you had to write that justification again today, would you frame it differently?

Participant: I might lead with the actual numbers instead of the worst-case story. Though the worst-case framing is usually what gets things approved quickly around here.

Interviewer: That's really helpful, thank you.

Participant: No problem, happy to help.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{CS_Biased_6}}",
  "occupational_domain": "{{Cyber Security}}",
  "role": "{{Threat Intelligence Analyst}}"
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
