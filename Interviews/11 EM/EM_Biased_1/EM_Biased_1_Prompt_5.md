You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for taking the time to talk through this. Before we start, I want to confirm you're comfortable having this incident discussed for training-development purposes, and that we can pause or skip anything you'd rather not detail.

Participant: Yeah, that's fine. This one's worth talking through anyway.

Interviewer: Good. Can you start by telling me who you are in this context and roughly what your role was supposed to be that day?

Participant: I'm a Training Officer for the county EM office. That day I was the exercise controller for a full-scale drill — a shelter-in-place and evacuation scenario at our county EOC and one of our affiliated public shelters. My job was to run injects, coordinate the simulated agencies, and evaluate how the shelter team and liaison staff performed under the exercise conditions.

Interviewer: And what actually happened?

Participant: About ninety minutes in, we got a report of a comms disruption. It was scripted — one of our injects — so at first I treated it that way. But almost immediately after, a real weather alert came through on my phone, a fast-moving winter storm, much faster than the forecast we'd built the exercise around. A couple of field reports started coming in that were ambiguous — I genuinely couldn't tell if they were part of the exercise or real conditions. So I paused the drill and checked the actual weather service data before doing anything else. That confirmed it: we had a real tower failure, not a scripted one, and roads were closing faster than forecast.

Interviewer: What made you decide to stop and verify rather than keep running the exercise?

Participant: Because the timing was too coincidental, and the reports didn't match our inject script. I've run enough of these to know when something's off-script. I didn't want to keep injecting scenario content into what might already be a real event.

Interviewer: Once you confirmed it was real, walk me through what happened next.

Participant: Right after that, two liaison officers arrived to relieve the exercise-shift shelter team — this was a scheduled shift handoff, storm or no storm. Neither of them had worked this particular shelter before. I had maybe ten minutes to brief them before I needed to shift attention to transportation, because we had buses that needed redirecting before roads closed. So I gave them a fast rundown — told them to run the usual Zone C protocol, muster the evacuees at the standard point, same as always. Then I moved on.

Interviewer: What happened after that handoff?

Participant: Maybe forty minutes later, during a headcount, it turned out a group of evacuees had been sent to the old west muster point instead of the current one — we'd changed that location about a year ago. And separately, one of the volunteer coordinators asked me point-blank what "Zone C protocol" even meant. That's when I realized the handoff hadn't landed the way I thought it had.

Interviewer: Let's slow down and go through this stage by stage. Starting with that first decision — pausing the exercise. What information did you have in front of you at that exact moment?

Participant: I had the scripted inject text, the live weather alert on my phone, and two unclear field radio reports. I didn't have direct confirmation of a real tower failure yet — that came after.

Interviewer: What alternatives did you weigh?

Participant: Either keep running the drill and treat the comms report as part of the script, or stop and check real data first. I chose to verify. If I'd been wrong, I'd have wasted a few minutes on a real drill for nothing. Given the mismatch in timing, that felt like the safer bet.

Interviewer: Fair enough. Now the liaison handoff — decision point two. What did you actually know about these two officers beforehand?

Participant: I knew they were newly rotated onto this shelter assignment. I didn't know their full experience level, but I assumed they'd have some baseline familiarity with our layout conventions, since that's fairly standard across our shelters.

Interviewer: When you gave them the shorthand briefing — "usual Zone C protocol," "standard muster point" — what did you assume they already understood?

Participant: Honestly, I assumed those terms would be self-explanatory to anyone who'd been through liaison training. I use them every day, so they don't feel like shorthand to me — they feel like the actual name of the thing. I wasn't thinking about it as skipping steps. It felt more like a normal handoff.

Interviewer: What alternative was available to you at that moment?

Participant: I could have walked them through the zone map and muster locations from scratch. That would've taken maybe five more minutes.

Interviewer: What made you choose the shorter version?

Participant: Time, mostly. I had buses to deal with. But if I'm honest, it wasn't purely a time trade-off — I didn't really stop to ask myself whether "the usual protocol" meant anything to them. It's just what I'd say to anyone on my team.

Interviewer: What would have changed your approach at that point?

Participant: If one of them had said upfront, "I've never worked this site," I probably would have slowed down. Neither of them said that, and I didn't ask.

Interviewer: Let's move to the transportation decision. What was the situation there?

Participant: Two buses available, three sites requesting transport, and the transportation chief flagged fuel and driver-hour limits. One sector's roads were closing noticeably faster than the others based on the county road updates.

Interviewer: What options did you consider?

Participant: Split the buses evenly across all three sites, or prioritize the site with the fastest-closing road first. I went with prioritizing that site.

Interviewer: Why that option over splitting evenly?

Participant: Splitting evenly sounded fair, but it risked stranding people at the site that was about to become unreachable. Prioritizing by road-closure risk meant we might delay the other two sites a bit, but nobody would get physically cut off.

Interviewer: How did that play out?

Participant: The prioritized site cleared in time. One of the other sites had a longer wait than we'd have liked, but nothing dangerous — they got transport once the first run was done.

Interviewer: Last decision point — the handoff to the Incident Commander. What was competing for your attention at that stage?

Participant: The IC had arrived to take over the real incident, but the exercise evaluators were still expecting a formal debrief, and some of the shelter arrangements were still running on the ad hoc setup from the earlier handoff.

Interviewer: What did you consider doing?

Participant: I could've tried to run the exercise debrief and real command informally side by side, or fully suspend the exercise and hand off command properly. I suspended it and gave the IC a written status briefing instead of just talking him through it.

Interviewer: Why written over verbal, given the time pressure?

Participant: Verbal felt faster, but I've seen handoffs get garbled that way, especially when comms are already degraded. Writing it down meant he had something to refer back to, and there was less chance of him missing something the way the liaison officers had earlier.

Interviewer: That's an interesting connection — did that earlier mix-up shape this choice?

Participant: A little, yeah. Not consciously at the time, but looking back, I think I was more careful here because of what happened with the muster point.

Interviewer: If you could redo the liaison briefing, what would you change?

Participant: I'd probably ask them directly what they already knew instead of assuming based on their role title. I think I treated "liaison officer" as if it came with a fixed set of knowledge attached, when really it depends a lot on which site they'd worked before.

Interviewer: And if the storm had hit an hour later, would any of your resource decisions have changed?

Participant: Probably not the bus prioritization — that logic holds regardless of timing. But I might have had more slack to do a fuller handoff briefing, which could have avoided the muster point confusion entirely.

Interviewer: Last one — what would you tell a less experienced officer stepping into a similar transition?

Participant: Don't assume shorthand travels with the title. Just because someone's qualified to be a liaison doesn't mean they've internalized your particular shelter's layout. It costs you almost nothing to check, and it can cost a lot if you don't.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EM_Biased_1}}",
  "occupational_domain": "{{Emergency management and Civil Protection}}",
  "role": "{{Emergency Management Training Officer}}"
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
