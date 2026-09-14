You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time today. This is a cognitive task analysis interview — I'm just trying to understand how you actually worked through a real production issue, step by step, including what you knew at each point and how you decided what to do. Nothing here is evaluative of you personally, and I may ask you to reconstruct things in detail even if they seem obvious. Sound okay?

Participant: Sure, happy to walk through it. I've got a good one — the Line 3 flash issue before the Meridian shipment a few weeks back.

Interviewer: Perfect. Before we get into the decisions, can you just describe the incident overall — what was the situation and what were you trying to achieve?

Participant: We run three shifts on Line 3, automotive interior clips for Meridian, and we had a 72-hour window to hit a shipment. Partway through a night shift, our scrap rate jumped from about 1.8% up to 6.4%, mostly flash defects, a few short shots mixed in. My objective was straightforward on paper — get quality back under 2% without blowing the ship date and without a full shutdown, since corporate wants VP sign-off for that and we didn't have time to chase approvals.

Interviewer: What were the first signs something was wrong?

Participant: Quality flagged the scrap numbers at shift change, and when I pulled the SPC chart, you could see cavity pressure had started drifting mid-shift. That's usually a decent early indicator. Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper.

Interviewer: So walk me through what you did with that first.

Participant: I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case. In hindsight, tooling wear was already flagged as a possibility by the tooling lead, but I didn't prioritize pulling that data until humidity came back clean.

Interviewer: What did you learn once the humidity results came in?

Participant: They were normal, well within range, so that ruled it out. That's when the tooling lead came back and said the mold had racked up wear cycles since the last inspection — more than we'd expected. So we lost a bit of time chasing the humidity angle before we got to the actual contributing factor.

Interviewer: If you'd had the pressure and wear data side by side from the start, would you have sequenced it differently?

Participant: Possibly. I think if I hadn't had that six-month-old case so fresh in mind, I might have pulled wear data in parallel instead of after.

Interviewer: Let's move to the fix itself. Once wear was confirmed, what were your options?

Participant: Wear was moderate, not severe. We had two real options — an incremental hold-pressure adjustment, which is lower risk but takes longer to validate, or a full mold-insert swap, which is more disruptive but felt like the more thorough fix. We had a press-down window shared with two other product runs, so timing was tight either way.

Interviewer: What tipped you toward the insert swap?

Participant: Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that. When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted.

Interviewer: Did you compare the wear numbers to your swap criteria directly?

Participant: Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing.

Interviewer: What happened after the swap?

Participant: It got done inside the window, which was good. But results were partial — scrap improved but didn't fully get back to baseline, so there was still something unresolved.

Interviewer: Let's go to the third point — the sister-plant call.

Participant: Right, around day two our quality engineer was out sick, so I had less statistical support than I wanted. I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network.

Interviewer: What did you decide?

Participant: I adopted it. Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out.

Interviewer: Did you consider waiting for that validation, or a modified version?

Participant: I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally.

Interviewer: What came out of that?

Participant: Short-term, flash defects dropped, which felt like a win. But two shifts later we started seeing a new warping issue on a subset of parts that hadn't shown up before.

Interviewer: Let's get to the final decision — the rollout call.

Participant: Right, so by the time Meridian's deadline was closing in, our most recent shift — the last eight hours — showed scrap down to 1.5%, best number we'd seen in four days. Corporate quality asked whether we should roll the fix out to Lines 4 and 6 as well.

Interviewer: What was your reasoning?

Participant: Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines.

Interviewer: How did that stack up against the full four-day trend?

Participant: The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call.

Interviewer: Did the warping incident factor into your confidence level at that point?

Participant: Less than it probably should have, looking back. I was focused on getting a clean answer to corporate fast.

Interviewer: What happened with the rollout?

Participant: Lines 4 and 6 looked fine initially, but one of them later threw a tooling alarm we hadn't seen before. And a fuller week-long review afterward showed the wear-related root cause was only partly addressed, not fully resolved like I'd said.

Interviewer: If the last shift's numbers had come in worse instead of better, do you think you'd have made the same call?

Participant: No, honestly, probably not — I think that reading was a big part of why I felt ready to greenlight it.

Interviewer: What would you do differently if this happened again?

Participant: Pull wear and pressure data in parallel from the start instead of chasing the familiar explanation first. And probably wait for a full trend view, not just the best shift, before telling corporate we were done.

Interviewer: This has been really useful — thank you for walking through it in this much detail.

Participant: No problem, happy to help.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IP_Biased_5}}",
  "occupational_domain": "{{Industrial Production Processes}}",
  "role": "{{Plant/Industrial Production Manager}}"
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
