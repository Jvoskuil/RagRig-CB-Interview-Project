You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary cognitive task analysis interview about your handling of the Millbrook Creek flash flood event. I'll ask you to walk me through what happened, and I may pause to dig into specific decisions. Nothing you say here is used for discipline or performance review. Can you state your role for the record?

Participant: Sure. I'm the county's emergency manager, been in the role about nine years, and I oversee EOC activation, evacuation orders, and shelter coordination for the whole county, but Millbrook Creek is one of our higher-attention areas because of the mobile home park down there.

Interviewer: Good. Before we get into specifics, give me the general shape of the incident.

Participant: It started as a fairly normal night shift. We had a flash flood watch come in from the National Weather Service for a storm system that was moving slower than usual and carrying a lot of moisture. The duty forecaster actually called me directly, which isn't standard for a watch-level product, and mentioned the storm structure looked different from what we typically see. I noted it, but Millbrook Creek has a long track record of handling these watches fine. Fifteen years of data at that gauge, and it's never gone past minor nuisance flooding on any watch I've been part of. So I kept us at routine monitoring rather than activating the EOC. A couple hours later, radar rainfall estimates blew past the watch threshold, and the gauge started climbing faster than anything I'd seen there before. NWS upgraded to a warning. From there we had to evacuate the mobile home park, manage two shelters with uneven capacity, and eventually request mutual aid. We got through it without any deaths, but there was a close call with a transport vehicle on the access road right as it was closing.

Interviewer: Let's reconstruct the timeline in a bit more detail. What information did you have at each stage, and where did it come from?

Participant: Initially it was NWS products plus the forecaster's call, and our own gauge telemetry, which was reading normal. About two hours in, we got updated radar rainfall totals from the regional office, and that's when the gauge began rising sharply. Once the warning was issued, our field liaison at the mobile home park confirmed water was already approaching the lowest units. After the evacuation was underway, Public Works reported the access road was narrowing due to runoff, and that's when the shelter and mutual aid pieces came into play.

Interviewer: Let's go through the decisions one at a time, starting with that initial watch. What alternatives did you consider before deciding to hold at routine monitoring?

Participant: I could've activated the EOC to Level 2 right when the watch came in, gotten resources pre-positioned. I also could've just called the forecaster back and asked more questions before deciding anything. But activating the EOC has real costs — staff overtime, pulling people off other duties — and I didn't want to cry wolf again after we'd done that twice last year on systems that fizzled. Given that gauge has never done anything but minor overflow on a watch, I made the call to hold at routine monitoring and wait for an actual warning before committing resources.

Interviewer: The forecaster flagged this one as structurally different. How did that factor into your decision?

Participant: I heard it, and I noted it, but honestly what carried more weight for me was the track record. That gauge just doesn't misbehave. I've watched a dozen watches come and go there with nothing to show for it, so a watch alone wasn't enough to move me off routine monitoring.

Interviewer: Moving to the evacuation decision once the warning came in. What alternatives did you weigh there?

Participant: We could evacuate with contingency time built in and pre-stage extra transport before ordering it, or issue a partial shelter-in-place for upper units and just pull the ground floor first. I chose to order a full evacuation, and I built the timeline off our fastest previous evacuation of that same park, which was under 90 minutes.

Interviewer: How did you arrive at that specific estimate?

Participant: We'd done it before in daylight with full staffing and it went under 90 minutes, so that was my benchmark. In hindsight, this time was nighttime, we had a skeleton crew until the EOC ramped up, and a chunk of those residents don't have their own vehicles, so it needs door-to-door contact. It ended up taking over three hours, and the shuttle buses from Public Works arrived later than I'd planned for. That gap surprised me at the time, honestly.

Interviewer: What made three hours surprising, given those differences were known going in?

Participant: I suppose I anchored on the best version of that evacuation rather than really adjusting for what was different this time. The information was there — nighttime, staffing, no-vehicle households — I just didn't weight it heavily enough when I set the timeline.

Interviewer: Let's talk about the shelter and mutual aid decision. What were the alternatives?

Participant: We could submit the mutual aid request immediately alongside the shelter routing calls, or split evacuees evenly across both shelters regardless of real-time numbers, or wait on mutual aid until we had firmer capacity data. I routed most evacuees to shelter A based on our initial capacity numbers and held off on mutual aid until we could confirm the picture more fully.

Interviewer: What happened as a result?

Participant: Shelter B actually filled up faster than shelter A because of how people were routed in from the road closures, and by the time we submitted mutual aid, the access road had already closed, so those resources arrived too late to help with the routing problem directly.

Interviewer: Was there information available at that point that could have changed the routing or timing decision?

Participant: The Red Cross coordinator had flagged that shelter B would need extra staff for overflow, and Public Works said the road might close within the hour. I had both of those inputs before I made the call. I was leaning on the initial capacity assumptions more than the live warnings coming in.

Interviewer: Let's move to the after-action review. Walk me through that discussion.

Participant: The panel was going through the timeline, and there was some pointed conversation about the Sheriff's watch commander, who had pushed back internally when the watch first came in, arguing it probably wasn't going to amount to much. People in the room were fairly critical of that, saying he let the historical pattern cloud his judgment on a night when the forecaster was explicitly saying this one was different.

Interviewer: How did you see your own role in that same conversation?

Participant: I felt for him, but I also think there's a difference — he was pushing back without really engaging with the forecaster's call, whereas I did hear it and made a judgment based on the full track record we had. My escalation timing and the evacuation plan were built on real experience with that location, so I'd characterize my decisions as sound given what I knew at each point.

Interviewer: Looking at your own decision log next to his account, do you see any similarities in the pattern?

Participant: I mean, on paper the timing gap looks similar, and I did build the evacuation estimate off a best-case prior run. But I still think context matters — I was managing a lot more moving pieces than he was, so I'd hesitate to put us in the same category.

Interviewer: Last few questions. If the storm had behaved like a typical watch-level event, what would you have done differently?

Participant: Probably nothing — routine monitoring would've been the right call, and we'd have avoided the overtime and disruption. That's part of why the decision felt reasonable going in.

Interviewer: If you'd had unlimited staffing from the very start, what would change about the evacuation?

Participant: I'd have pre-staged the shuttle buses and had more people for door-to-door contact from minute one, which probably closes most of that three-hour gap.

Interviewer: What would you tell a newer emergency manager to watch for in a similar situation?

Participant: Trust the data, but don't dismiss a forecaster who's willing to pick up the phone on something that's usually just a form letter. That's not something they do casually.

Interviewer: Thank you, this has been very helpful.

Participant: Happy to help. Hope it's useful for the next one of these we run into.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EM_Biased_3}}",
  "occupational_domain": "{{Emergency management and Civil Protection}}",
  "role": "{{Local Emergency Manager (County/Municipal Level)}}"
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
