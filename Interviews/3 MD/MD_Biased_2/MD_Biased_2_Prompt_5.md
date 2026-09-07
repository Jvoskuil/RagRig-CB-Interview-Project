You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is for a cognitive task analysis review, not part of any disciplinary or legal proceeding. I'll ask you to walk me through a specific investigation and how you made key calls along the way. Sound okay?

Participant: Yeah, that's fine. I've done these debriefs before after case closures.

Interviewer: Great. Can you tell me your role and give me a general sense of the case we're discussing?

Participant: I'm a CID Special Agent, been doing investigative work about six years now, three of those in this billet. The case was a motor pool theft situation—fuel and some small equipment going missing over about six weeks. Battalion asked us to look into it because the losses were adding up and it was becoming a readiness issue.

Interviewer: Can you walk me through how it first came to your attention and what your objective was going in?

Participant: The motor pool NCOIC flagged discrepancies in the fuel reconciliation report—basically more fuel being drawn than accounted for in vehicle usage. My job was to figure out who was responsible and build something solid enough for command to act on, ideally a case the Provost Marshal's Office could actually run with. We didn't have camera coverage on four of the six bays, so a lot of this was going to come down to logs, statements, and timeline work rather than catching someone on video.

Interviewer: What constraints were you working with?

Participant: Time, mostly. Command wanted this wrapped before an inspection that was maybe ten days out. I was also the only agent assigned full-time, so I couldn't run parallel interview tracks the way I would've liked. And the duty roster rotated every few days, which made lining up who was actually present on which theft date more of a puzzle than it should've been.

Interviewer: Let's reconstruct the timeline. What did you do first?

Participant: First thing was pulling the fuel reconciliation report and cross-referencing it against the duty roster to see who was on shift during the loss windows. That gave me a pool of about five soldiers with some overlap. Around the same time, I talked to the NCOIC to get a feel for the shop—who's reliable, who's had issues before, that kind of context.

Interviewer: What came out of that conversation?

Participant: He walked me through the shop culture, mentioned a few names. One that stuck was PFC Doyle—the NCOIC mentioned he rides a motorcycle off-post, has some ink, keeps to himself outside of work. Nothing disciplinary in his file, but the NCOIC framed him as someone who "runs in a rougher crowd." That was really just color commentary at that point, but it's the kind of thing that sticks in your head when you're trying to narrow a field.

Interviewer: So walk me through your first real decision point—how you picked who to focus on initially.

Participant: Right, so I had this list of five soldiers with shift overlap, and I hadn't finished building out the full matrix yet—cross-checking every single person against every theft date. But given what the NCOIC said about Doyle, and honestly just going with my gut on who seemed like the type to be involved in something like this, I decided to bring him in first. I figured if there was smoke, better to check the most likely spot before grinding through everyone else.

Interviewer: What alternative did you consider there?

Participant: I could have finished the full overlap matrix first and let the data alone tell me who had the most matching dates before talking to anyone. That's probably the cleaner way to do it. But time was tight, and starting somewhere felt more productive than sitting with spreadsheets.

Interviewer: What did you learn after making that call?

Participant: Once I did finish the matrix a couple days later, Doyle actually only matched two of the five theft dates. Two other guys on the list—pretty unremarkable, no distinguishing traits, nothing the NCOIC had flagged—matched more dates than he did. So the initial pick wasn't wrong exactly, he stayed a person of interest, but he wasn't actually the strongest match on paper.

Interviewer: Moving to the next stage—what happened with the physical evidence?

Participant: I pulled the key control log and found irregular sign-outs on two of the theft nights, and the fuel truck's odometer logs showed mileage that didn't line up with the routes people were logging. No fingerprints off the fuel caps, which wasn't surprising given how many hands touch that equipment daily.

Interviewer: How did you weigh that odometer discrepancy?

Participant: At the time I logged it as an open anomaly rather than settling on what it meant right away. It could fit with someone taking the truck off-route to move fuel, but it could just as easily be something administrative, so I flagged it in the case file as unresolved and put in a request to pull the maintenance records before I leaned on it either way.

Interviewer: What did you find out later?

Participant: Turned out maintenance had done a documented test drive on the truck that accounted for the extra mileage. Completely unrelated to the thefts. Good thing I hadn't already built it into the narrative, because I would've had to go back and pull that thread out.

Interviewer: Let's get to the dispatcher's statement. What happened there?

Participant: The night-shift dispatcher gave a sworn statement that she'd been on the phone with Doyle the entire window during one of the suspected theft incidents. She's got a clean record, no personal relationship with him beyond work contact.

Interviewer: How did you handle that when it came in?

Participant: Honestly, my first reaction was skepticism. It landed right in the middle of me building out the case around him, and it directly cut against that. I noted in the file that the timing was convenient and that dispatchers and shop personnel sometimes cover for each other, so I flagged it as needing more corroboration before I'd weigh it heavily, and I kept the investigative focus where it was rather than treating it as something that reshaped the picture.

Interviewer: What made you lean that direction rather than treating it as exculpatory on its face?

Participant: I think partly it's just experience—alibi statements from coworkers aren't always clean, people help each other out. But if I'm being honest, I also didn't want to have to unwind everything I'd already built. It's easier to question the new thing than the whole structure you've put together.

Interviewer: What happened with that statement afterward?

Participant: Phone records came back later and independently confirmed the call happened exactly when she said. So it held up. I don't think I handled that piece as carefully as I should have when it first came in.

Interviewer: Let's talk about how you closed this out, given the command timeline.

Participant: Right around the inspection deadline, I still didn't have a clean forensic or eyewitness link to any one person. There was also a fourth soldier, fairly unremarkable duty history, who had an odd fuel-card transaction that hadn't been fully run down. My options were to expand the investigation to properly vet that anomaly, or close out with what I had, centered on the original track, and let the Provost Marshal's Office pick it up from there.

Interviewer: What drove that final call?

Participant: Command needed something before the inspection, and I'd invested most of my ten days building out the case around the original suspect pool. Fully vetting the fourth soldier's transaction would've meant more interviews and probably blowing past the deadline. So I referred it up with a recommendation, flagging the fuel-card anomaly as something needing follow-up rather than running it down myself.

Interviewer: If the dispatcher's statement had come in earlier, do you think it would've changed your approach?

Participant: Probably would've made me slow down sooner and go back to the full personnel matrix instead of staying anchored on Doyle. Hard to say for sure.

Interviewer: And if command hadn't been pushing a deadline?

Participant: I'd have chased the fourth soldier's anomaly before referring anything. That's the piece that still bugs me a little—we never fully closed that loop.

Interviewer: Looking back, is there anything in your reasoning you'd revisit?

Participant: Probably how quickly I latched onto Doyle at the start, and how long it took me to really sit with that dispatcher's statement instead of finding reasons to set it aside. Neither one broke the case, but they're the parts I think about.

Interviewer: That's helpful, thank you. I think that covers what I need.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MD_Biased_2}}",
  "occupational_domain": "{{Military and defense operations}}",
  "role": "{{Military Police Investigator / Criminal Investigations Division (CID) Special Agent}}"
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
