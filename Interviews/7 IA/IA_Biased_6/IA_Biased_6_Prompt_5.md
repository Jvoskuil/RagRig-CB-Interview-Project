You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and I'll ask you to walk me through a specific shift in detail. You can skip anything you're not comfortable sharing. Can you tell me your role and how long you've been doing it?

Participant: Sure. I'm a threat intelligence analyst on the SOC team, been in this seat about four years, mostly financial services environments. My job during shift is triage, attribution, and hunt scoping when something looks like it's more than commodity noise.

Interviewer: Good. Let's start broad. Can you walk me through what this shift looked like when the alert cluster first appeared?

Participant: It was maybe two hours into an overnight shift. EDR kicked out a cluster of alerts on a trading-support server — not the trading engine itself, but a box that feeds reporting data to it. The auto-triage score came back Low. Historically, that queue throws a lot of low-severity noise, especially from that server, so my first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing.

Interviewer: What was your primary objective at that point?

Participant: Get through the queue, keep the shift moving, and not waste the incident response lead's time on something that turns out to be benign. We only had about three hours left in the shift, and I wanted whatever I handed off to be solid, not a guess.

Interviewer: Take me through what happened next, chronologically.

Participant: So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet. About forty minutes later, a follow-up alert showed an outbound connection from that same host to an IP I didn't recognize. That's when I actually opened the case properly. I found a registry-key artifact that matched something documented in a GreyFalcon campaign from about six months back — I remembered writing that report myself, so it stuck with me. Around the same time, internal telemetry showed an attempted connection to the HR benefits database from that host, which was strange, but I moved forward with attribution anyway. Then I pulled a vendor bulletin that had just come in — the vendor portal access was closing soon, so I read it quickly. It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that. Near the end of shift, I had to write up a containment recommendation for the IR lead, and I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of "possibly" and "unclear."

Interviewer: Let's slow down and go through each of those decisions one at a time. First one — the initial Low-severity alert. What cues were you weighing right then?

Participant: Mainly the auto-triage score and my own memory of that server generating false alarms before. No unusual business disruption was reported either, which reinforced it felt routine.

Interviewer: What made you decide to defer the manual log pull rather than doing it right away?

Participant: Time, mostly. The score was Low, I had precedent that Low from that host usually meant nothing, and pulling raw logs is a real time cost. Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me. It felt like a reasonable use of triage priority rather than checking every single alert by hand.

Interviewer: Did you consider escalating to the IR lead first instead?

Participant: I thought about it, but that seemed like overkill for a Low score with no other signal at that point. In hindsight, I probably could've spent the fifteen minutes given how the next forty minutes went, but at the time it didn't seem to justify interrupting anyone.

Interviewer: Understood. Let's move to the attribution decision after the outbound connection appeared. What was the basis for assigning GreyFalcon?

Participant: The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in.

Interviewer: You mentioned the C2 domain's registration pattern looked different from GreyFalcon's usual infrastructure. How did that factor in?

Participant: It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then.

Interviewer: And the HR database access attempt — GreyFalcon has typically gone after trading or financial data in your prior tracking. How did you read that mismatch?

Participant: My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly. So it didn't strike me as inconsistent with the group, more like an opportunistic pivot they'd make if they were being efficient about it.

Interviewer: Did you weigh that explanation against the possibility that it wasn't GreyFalcon at all?

Participant: Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself.

Interviewer: Let's talk about the hunt scope decision, once the vendor bulletin came in. Walk me through how you decided what to include.

Participant: The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up. It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources. There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary.

Interviewer: The bulletin listed two file-hash IOCs last — how much did those factor into the scope?

Participant: Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely.

Interviewer: Was there consideration of scoping broadly across all five IOCs regardless of order?

Participant: There was, briefly — business owners wanted it narrow anyway to avoid downtime on trading-adjacent systems, so narrow scope aligned with what they wanted too. That made it easier to just go with the scope that already made sense to me.

Interviewer: Last decision point — the containment recommendation. You mentioned leaning on the vendor bulletin over a colleague's notes. What drove that?

Participant: Time pressure, for one — I needed something to hand the IR lead within the hour. But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — "possibly," "unclear if," that kind of thing. The vendor version gave me something concrete to act on.

Interviewer: Did you compare the actual evidence underlying each source, separate from how they were written?

Participant: Not directly side by side, no. I read the vendor one, it felt solid, and I went with it.

Interviewer: How confident were you overall in the final recommendation you handed off?

Participant: Reasonably confident, maybe seven out of ten. Enough uncertainty that I flagged it as needing follow-up validation next shift, but I felt the containment steps were defensible given what I had.

Interviewer: Looking back across the shift, if you'd pulled the raw logs immediately in phase one instead of deferring, how do you think things would've unfolded differently?

Participant: I might have caught the odd outbound connection sooner, maybe before the vendor window closed, which could've changed how much I leaned on that bulletin later. Hard to say for certain.

Interviewer: If the vendor bulletin had listed its IOCs in reverse order, hash-based ones first, do you think your scoping would have changed?

Participant: Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope.

Interviewer: Is there a point in this sequence where you'd want a second analyst's independent read before proceeding?

Participant: Probably the attribution step. That's where I moved fastest from one piece of strong evidence to a full working theory, and a second set of eyes might have pushed back on the infrastructure mismatch or the HR access pattern before I built the rest of the shift around it.

Interviewer: That's helpful, thank you. I think that covers what I need.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IA_Biased_6}}",
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
