You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific incident from your work as a production planner, and I'll be asking you to walk me through what happened and why you made the calls you did. Nothing you say here affects your performance record. Sound good?

Participant: Yeah, that's fine. Happy to walk through it. It was a memorable afternoon.

Interviewer: Can you tell me a bit about your role, then give me the overview of the incident?

Participant: I'm the production planner for three parallel lines at our plant — discrete assembly, mid-volume SKUs, frequent changeovers. I sequence what runs where, manage changeover windows, and hit ship cutoffs without blowing labor budgets. This was a Friday. A subcomponent we needed for two customer orders — Order A and Order B — came in four hours late from the supplier. Both had the same end-of-shift ship cutoff, so as soon as I heard about the delay I knew I had a compressed window to get everything sequenced and out the door.

Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened after you learned about the late delivery?

Participant: Once I confirmed the component landed, I pulled up the MES to see where Line 1 and Line 2 stood — both mid-run on other SKUs, so I needed changeovers on both to get to the rush SKUs. Problem was, I only had one certified changeover tech on shift. That was my first call — which line gets the tech first. Around the same time, an operator flagged that Line 3 had thrown an intermittent alarm twice in the past hour. That line wasn't part of the original plan, but it had open capacity, so it became relevant as a potential overflow resource. Then there was a batch sitting in the Line 2 output buffer that QA hadn't released yet, which mattered because Order B needed some of those units. Finally, toward the end, a labeling issue on part of that batch ate into our remaining time right as the ship cutoff closed in. So four points where I had to make a call under pressure.

Interviewer: Let's reconstruct the timeline before we dig into each decision.

Participant: Component lands around 1pm, four hours later than the morning window. I make the technician call almost immediately, maybe 1:15. The Line 3 alarm conversation happens about 20 minutes after, while the first changeover is underway. The QA buffer question comes up around 2:30, once I'm mapping how many units Order B still needs. QA doesn't call back until 3:10, which is when the labeling discrepancy surfaces. From there it's a sprint — cutoff is 5pm, so the last call, about overtime and the carrier, happens around 3:30.

Interviewer: Let's start with the technician assignment. What information did you have?

Participant: I knew Order A was the bigger order by unit count, and Line 2 had a tighter downstream packaging slot later on. Technically Line 2's changeover being late would ripple further because packaging was booked tight. In the moment I went with unit count — Order A first — partly because that's our default rule when picking between two rush jobs. I didn't split the tech's time across both lines in shorter blocks, which was an option, because that would have delayed both changeovers instead of finishing one cleanly.

Interviewer: Any hesitation about the packaging slot issue?

Participant: A little. But finishing one line's changeover completely felt more reliable than half-finishing two, and Order A's volume backed that up.

Interviewer: Let's move to the Line 3 alarm. Walk me through that call.

Participant: The operator told me the alarm had come up before and "usually clears itself" — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience. Given that, and given I had two other things actively unfolding — the changeover and the ship cutoff clock — I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue.

Interviewer: Did you look into whether anything else depended on Line 3's output during that window?

Participant: Honestly, no. I didn't check. My focus was entirely on Order A and Order B — those were the two fires in front of me — so I didn't cross-reference the schedule for anything else running through Line 3. It turned out a smaller order, Order C, also needed Line 3 output that same shift, but I didn't find that out until later. I wasn't ignoring it on purpose, it just wasn't on my radar with everything else going on.

Interviewer: When you found out about Order C afterward, what was your reaction?

Participant: A bit of an "oh, right" moment. Not catastrophic — we fit it in later — but it made me realize I'd made that overflow call pretty quickly without stepping back to check what else was in play on that line.

Interviewer: Let's talk about the QA buffer decision. What was going through your mind?

Participant: Order B needed units from that batch plus new production to hit full quantity. QA hadn't confirmed release yet, and their lead was off-site with spotty response time. I decided to provisionally build the buffer units into the Order B plan rather than wait, because waiting with no ETA on a callback risked losing time I couldn't get back. I told the team we'd adjust if QA flagged something.

Interviewer: What made provisional inclusion feel right versus excluding those units?

Participant: Excluding them would have guaranteed a lower fill rate regardless of what QA said, and historically that batch type passes more often than not. It felt like a reasonable bet given the clock, not a guarantee.

Interviewer: And QA did call back?

Participant: About forty minutes later. They confirmed the batch passed, but flagged a labeling discrepancy on a subset of units, meaning rework.

Interviewer: That leads to the final decision — rework and shipment. What were you weighing?

Participant: The rework was going to eat twenty minutes of Line 2 time, and cutoff was ninety minutes out. Order A was tracking fine. Order B was now at risk. Overtime authorization had just come through, but it adds cost. I could also have accepted a partial shipment and expedited the rest next shift, or called the account manager to renegotiate the cutoff.

Interviewer: Why overtime and carrier coordination instead of the other two?

Participant: Partial shipment felt like a worse customer experience than a slightly late full shipment, and renegotiating the cutoff was a last resort I wanted to avoid if I could still make it work operationally. Overtime plus talking to the carrier directly gave me a shot at getting the full order out with minimal disruption, even shipping a few minutes past official cutoff.

Interviewer: How did that play out?

Participant: Order B shipped about twelve minutes past cutoff after the carrier agreed to hold pickup briefly. Order A shipped on time. Not a clean day, but nothing was lost.

Interviewer: Looking back, if you'd known upfront that Order C depended on Line 3, would you have handled that decision differently?

Participant: Probably. I likely would have taken two minutes to check the schedule before committing Line 3 as overflow, rather than just going with the operator's read on the alarm. It wouldn't have changed the outcome much, but I'd have made the call with a clearer picture.

Interviewer: And if you'd had fifteen more minutes before the technician assignment, would anything have changed?

Participant: Maybe I'd have looked harder at splitting the tech's time, but I think I still land on Order A first given the volume difference.

Interviewer: Is there a point in this sequence where, in hindsight, you wish you'd gathered more information before deciding?

Participant: The Line 3 call, for sure. Everything else I feel like I had a reasonable handle on given what was knowable at the time. That one I moved through fast because I was juggling two other things, and it's the one place where a little more digging would have given me a fuller picture before I committed the line.

Interviewer: That's really helpful, thank you. I think that covers everything I need.

Participant: No problem, glad it was useful.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IP_Biased_1}}",
  "occupational_domain": "{{Industrial Production Processes}}",
  "role": "{{Production Planner / Scheduler}}"
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
