You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a safety review process, your responses are confidential to the review team, and you can decline any question. That work for you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start with your role and a quick summary of the flight in question?

Participant: Sure. I was captain on a scheduled morning turn, regional jet, about ninety minutes of flying time. First officer was experienced, we'd flown together a handful of times before. Destination has a known fog problem in the early morning — radiation fog that usually burns off by mid-morning.

Interviewer: Walk me through the flight from your initial review of the dispatch release that morning.

Participant: The release showed the destination TAF with fog down to a half mile visibility starting around 0500, improving to three miles by 0900. Our ETA was 0845, so we were arriving right at the edge of that improvement window. Dispatch had us at minimum contract fuel plus standard contingency — nothing extra flagged. I'd flown into that airport probably a dozen times with similar fog setups, so the pattern was familiar to me.

Interviewer: What was your overall read of the weather situation before departure?

Participant: Honestly, I felt fine about it. The forecast lined up with what I'd typically seen there — fog clears out once the sun gets some angle on it. Nothing about the release stood out as unusual.

Decision Point 1

Interviewer: When you accepted the fuel load in dispatch, what specifically drove that decision — was it purely the release numbers, or did your own experience with this airport factor in?

Participant: It was really just what the release called for. Dispatch runs the numbers, and if they don't flag anything extra, that's usually a good signal it's a normal day. I didn't see a reason to second-guess it.

Interviewer: Did you consider requesting additional fuel for holding, given the airport's fog history?

Participant: I thought about it briefly — my first officer actually mentioned the improvement time was pretty close to our ETA, not a lot of cushion. But the release was within limits, and asking for extra fuel when the paperwork already supports the flight can slow things down at the gate. We had a full connection bank behind us. I went with what was filed.

Interviewer: What did the TAF and dispatch release actually say about the fog, and when did you expect it to clear?

Participant: Half mile visibility overnight, improving to three miles by 0900. I expected it to be lifting by the time we got there, based on how that pattern usually goes at that field.

Decision Point 2

Interviewer: What did you hear from dispatch and from other aircraft as you got closer to the airport?

Participant: About an hour in, we got an ACARS update — METAR still showing half mile visibility, no improvement yet. Then a PIREP came through from an aircraft that had landed twenty minutes earlier, saying they broke out at minimums after two attempts.

Interviewer: When the updated METAR still showed fog an hour into the flight, what options did you weigh, and why did you not request additional fuel or a route change at that point?

Participant: We talked about it for a minute. I called dispatch to check in, and they acknowledged it was running a little behind the forecast but didn't amend anything on their end. Fuel was still on profile for the planned arrival, just with less room for extended holding than I'd have liked. Since dispatch wasn't changing the release, and the delay didn't seem dramatic yet, we kept proceeding toward the field and started working the descent.

Interviewer: Looking back, what other options were realistically available at that stage?

Participant: We could've asked for holding fuel proactively, or had dispatch start building an early diversion picture. We didn't do either — it felt premature at that point, since one lagging METAR isn't necessarily a trend.

Decision Point 3

Interviewer: Describe what happened during the approach and the missed approach in your own words.

Participant: As we got in range, ATIS had visibility at three-quarters of a mile, right at minimums for the approach we were flying. Tower told us the last two aircraft in landed fine, but a third had just gone missed. Looking at the last few METARs, one had ticked up slightly and then the next held flat — not really a clear trend either way.

Interviewer: At that point, what alternatives did you consider besides continuing the approach, and what tipped the decision toward continuing?

Participant: We could have diverted straight to the alternate right then instead of shooting the approach. But two of the three recent arrivals had gotten in, and the forecast had always called for improvement by our arrival window, so I expected we'd break out. We briefed it as a normal approach and continued.

Interviewer: Did the go-around report from the third aircraft factor into that briefing?

Participant: We noted it, but it didn't really shift the plan. We were still within minimums, legally fine to try, and the overall picture matched what we'd expected going in.

Interviewer: What happened at decision altitude?

Participant: We didn't get the visual references we needed, so we went missed. Fuel after that put us close to the point where we needed to commit to the alternate.

Decision Point 4

Interviewer: After the missed approach, what changed in how you evaluated the situation compared to before?

Participant: Everything got a lot more concrete. Fuel was no longer theoretical — I had a hard number and a hard decision. ATIS still showed the same visibility as before, no real improvement. The alternate was reporting clear skies and we had comfortable fuel to get there, and ops confirmed ground handling was ready for us.

Interviewer: What alternatives did you weigh at that point?

Participant: Try one more approach at the destination since we were still technically legal, or commit to the alternate now while we had solid reserves. I ran the fuel numbers again independently rather than assuming we'd get in this time, and it was clear the smarter move was to divert. We coordinated with dispatch, confirmed the numbers, and headed to the alternate.

Interviewer: What ultimately drove that choice?

Participant: The fuel math, plain and simple. There wasn't a strong reason to think a second attempt would go differently, and I didn't want to erode our margins further chasing it.

Closing Reflection

Interviewer: If the go-around PIREP had come in before you accepted the fuel load that morning, would that have changed your decision?

Participant: Possibly. If I'd known that early, I might have asked for a bit more contingency fuel going out the door. It's easier to build in margin before departure than to manufacture it later.

Interviewer: If you had to explain your fuel-planning decision to a new first officer, how would you describe the basis for it?

Participant: I'd tell them dispatch runs a solid process, and if the release supports the flight without flags, that's generally trustworthy. It's a pretty standard call.

Interviewer: What would you do differently if you flew this exact scenario again next month?

Participant: I'd probably push a little harder for extra fuel given how tight that improvement window was relative to our ETA, and maybe ask dispatch for a firmer trend picture before committing to the approach rather than the destination. But nothing that happened was outside normal limits at any single point — it was more about the margins tightening up as we went.

Interviewer: That's really helpful, thank you. I think that covers what I need.

Participant: No problem, glad to help.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{AV_Biased_2}}",
  "occupational_domain": "{{Aviation}}",
  "role": "{{Airline Transport Pilot (ATP) – Scheduled Carrier}}"
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
