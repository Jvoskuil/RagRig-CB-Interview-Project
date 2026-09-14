You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for taking the time. Quick check-in before we start — this is just a walkthrough of how you handled a specific case, for process review, not a performance evaluation. Can you tell me your role and background?

Participant: Sure. I'm a Vulnerability Management Analyst, been doing this about three years, SOC monitoring before that. I own triage and remediation tracking for our internet-facing assets — patch coordination, compensating controls, closing tickets against our SLA.

Interviewer: Good. Tell me how this case started and what you were trying to achieve.

Participant: Our threat intel feed flagged a new CVE — critical, 9.8 on CVSS, with confirmed exploitation already happening in the wild. It hit the web framework under our legacy order-processing gateway, which is Tier-1 criticality — internet-facing, handles checkout. My objective was to close this within our 30-day SLA without taking that system down during peak sales. Complication: the gateway needs vendor coordination to patch, we had a partial change freeze ten days out, and I was also carrying two other high-severity tickets at the same time.

Interviewer: How did it unfold, in order?

Participant: Day one, alert comes in, I do triage and have to decide between the standard 21-day cycle and pushing for an emergency change board slot. I escalate, and we get a two-hour emergency window — not enough for full regression testing. Around day three we deploy a WAF rule as an interim compensating control. While setting that up I also noticed some odd outbound DNS traffic on the same host, unrelated to the CVE signature, so I opened a separate low-priority item to look into that. About a week in, IT Ops flags that a vendor SIEM correlation rule for this CVE family is now available, so I have to decide what to do with the detection script I'd built for it myself. Then around day 27, with the SLA clock almost out and the real patch still not deployed, I have to decide how to position the ticket for closure.

Interviewer: Let's go through the first one. What made you push for the emergency CAB slot instead of the 21-day cycle?

Participant: I actually wrote up a short comparison for my manager. On one side, waiting 21 days with an exploit already active in the wild against a Tier-1 asset — that's a meaningful probability of exposure over three weeks. On the other side, an emergency patch attempt with a compressed testing window has its own risk of breaking checkout during a high-traffic period. To ground that comparison I pulled the threat intel feed's confidence rating on the exploitation reports, confirmed with the app owner that the gateway was actually reachable from the internet segment the CVE assumed, and asked IT Ops for a rough sense of rollback feasibility if an emergency deploy went wrong. I laid all of that out, roughly weighted the likelihood of exploitation against the likelihood of a bad deploy, and the exploit-in-the-wild status tipped it toward escalating, but it was close enough that I documented the disruption risk too, in case leadership wanted to weigh it differently.

Interviewer: Did anyone push back on that framing?

Participant: The app owner did, mostly on the disruption side — worried about the two-hour window not being enough for proper testing. That's actually what happened; the window turned out to be too short for full regression, which is why we ended up needing the WAF rule as a bridge.

Interviewer: Second decision — the WAF rule and that DNS anomaly. Walk me through it.

Participant: The dashboard showed a clear spike matching the known exploit payload pattern, so I deployed the WAF rule against that first. In the same dashboard view, there was also this burst of unusual outbound DNS queries from the same host. It wasn't part of the CVE's known indicators, so it didn't belong in this ticket, but I didn't want it sitting unlogged either. I opened a separate, lower-priority task for it right away and assigned it to be looked at in parallel rather than folding it into the CVE investigation or just noting it and moving on.

Interviewer: What was your thinking behind treating it separately rather than either ignoring it or merging it into the main ticket?

Participant: Mixing an unconfirmed anomaly into a critical CVE ticket muddies the SLA tracking for the actual vulnerability. But two things showing up on the same host in the same week is worth someone's attention, so a parallel low-priority task felt like the right way to keep both threads visible without conflating them. That anomaly ended up tracing back to an internal monitoring job that had recently been reconfigured — unrelated to the CVE, closed without further action, but it was worth the half hour it took to check.

Interviewer: Third decision — the script versus the vendor rule.

Participant: Right, I'd written a detection script six months earlier that covered the one payload variant we'd seen. When the vendor rule came out covering multiple variants with less upkeep, IT Ops suggested standardizing on it. I put together a quick comparison — variants covered, maintenance overhead, how each had performed in testing — and decided to run both in parallel for a transition period rather than cutting over immediately or keeping mine as the sole primary. Before setting that up, I agreed with IT Ops on a specific exit condition: a two-week observation window comparing alert volume and false-positive rate between the two rules, after which whichever one was performing better on those metrics would become primary and the other would step down to backup.

Interviewer: Why parallel instead of just switching over, given the vendor rule's broader coverage looked better on paper?

Participant: Mainly because neither one had a track record long enough yet in our environment to bet everything on it alone. Running both meant if the vendor rule had an unexpected gap or false-positive issue during rollout, my script was still catching the one variant we knew about, and vice versa. A week later a slightly different variant did show up, and the vendor rule flagged it — which is exactly the kind of gap the parallel run was meant to catch.

Interviewer: Last one — closing the ticket near day 27.

Participant: At that point the actual vendor patch still wasn't deployed, just the WAF rule and both detection tools. Compliance asked for a documented risk position before the SLA deadline. I pulled together everything outstanding — the unpatched root cause, the current dual-tool coverage, the DNS item that had already closed clean — and instead of closing the ticket outright, I escalated the residual risk summary to the CISO for a formal risk-acceptance call, since the underlying patch was still pending.

Interviewer: What made you escalate rather than just close it as adequately mitigated?

Participant: The compensating controls looked solid on paper, but the root cause was still open, and I didn't think that decision should rest on my sign-off alone given it was going past the SLA target. Documenting the gaps and pushing it up felt like the more defensible move than declaring it done.

Interviewer: How confident were you in the compensating controls at that point?

Participant: Reasonably, based on what the dual-tool coverage data showed, but I was explicit in the writeup that "reasonably confident" isn't the same as "resolved," which is part of why I sent it up rather than closing it myself.

Interviewer: If you'd had another week before the deadline, anything different?

Participant: Probably would have pushed harder to get the actual maintenance window scheduled before the freeze, rather than relying on the compensating controls for as long as we did.

Interviewer: If the vendor rule hadn't existed at all, how would detection have looked?

Participant: We'd have been leaning entirely on my script, which only covered the one variant — so that later variant might have slipped through until something else caught it.

Interviewer: If the DNS anomaly had turned out to be related to the CVE, would your sequencing have changed?

Participant: Yes, it would have gotten folded straight into the main ticket and probably accelerated the escalation call. It just happened not to be connected.

Interviewer: Anywhere you think more information up front would have changed a decision?

Participant: Knowing earlier that the emergency window would only be two hours might have changed how much I leaned on the WAF rule versus pushing for a longer maintenance slot from the start.

Interviewer: This has been really useful, thank you.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{CS_Vocab_Control_5}}",
  "occupational_domain": "{{Cyber Security}}",
  "role": "{{Vulnerability Management Analyst}}"
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
