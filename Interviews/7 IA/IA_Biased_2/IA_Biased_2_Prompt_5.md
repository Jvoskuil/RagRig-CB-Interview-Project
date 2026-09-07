You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the border-sector traffic assessment from last month, purely for how you approached the analysis. Nothing here goes in your file.

Participant: Sure, no problem. That one's still fresh anyway.

Interviewer: Good. Can you give me your role in the fusion cell and what your objective was that day?

Participant: I'm the SIGINT desk analyst for that regional cell. My job that day was to turn a raw traffic spike into a confidence-graded assessment for the fusion cell lead—basically, tell him whether what we were seeing near the Sector 7 logistics hub was something operational or just noise.

Interviewer: Take me through the incident from the top.

Participant: Around 0700 the automated system flagged a jump in encrypted burst traffic near the Sector 7 hub—well above baseline, and Sector 7 is normally quiet outside scheduled rotations. About the same time, Sector 4 showed a smaller bump too, but that's a different area entirely, no obvious connection. I had a hard deadline: the lead wanted a briefing in six hours. My linguists were already sitting on an eight-hour backlog from other tasking, so I knew from the jump I wasn't going to get everything translated.

Interviewer: What did you know before you made any calls?

Participant: Just the signal signature data—volume, timing, burst patterns—and the historical baseline for both sectors. No content yet. Sector 7's hub has strategic weight, it's tied to a known logistics node in the order of battle, so a spike there gets attention regardless. Sector 4's pattern was actually less typical, statistically, but there was no obvious link to anything sensitive.

Interviewer: So what did you do with your linguist hours?

Participant: I pushed almost all three available hours to Sector 7 and queued Sector 4 for later. The alternative was splitting time evenly, or even flipping it and doing Sector 4 first because its pattern was more unusual. But given the deadline, I couldn't do both properly, and Sector 7's hub mattered more if something real was happening there.

Interviewer: What came back from that first batch of translation?

Participant: A mix. Some convoy-movement language, some resupply terms, and two coded phrases that weren't in our standard glossary. Also some fairly mundane rotation talk. It wasn't clean either way.

Interviewer: How did you interpret that mix?

Participant: I started drafting a working note. My instinct was that convoy references plus burst traffic plus unexplained code phrases fit a pattern I'd want to flag—an emerging logistics buildup ahead of some posture change. I laid it out step by step: the signal surge, then the convoy chatter, then the coded terms as probable concealment for something they didn't want plain-language. Writing it out that way, it held together. It read like a coherent sequence, and honestly, once I had it typed up in that form, I felt more confident it was the right read than when I'd started.

Interviewer: Was there anything at that point that argued the other way?

Participant: The exercise calendar showed a rotation window that plausibly overlapped, and no imagery corroboration had come in yet. I noted the rotation possibility in the draft, but I led with the buildup framing because it explained more of the pieces at once—the convoy talk, the burst pattern, and the coded phrases all fit under one story, whereas the rotation explanation left the coded phrases dangling.

Interviewer: Did anything come in afterward that touched that account?

Participant: Yes—a later intercept had maintenance-cycle terminology in it, which cuts somewhat against the buildup idea. And one of those two coded phrases turned out to be in a maintenance-schedule glossary, not anything to do with offensive posture. That came in after I'd already built the note around the buildup framing.

Interviewer: Let's move to sourcing. You had two corroborating options—walk me through that.

Participant: Right, I had an open-source digest, well-written, clearly formatted, forecasting regional tension in a way that lined up with what I already had drafted. And I had an IMINT report on vehicle dispersal at the hub—more directly relevant to the actual location, but dense, heavy on sensor jargon, and I only had time to fully absorb one of them before the deadline. The IMINT analyst wasn't reachable for a quick walk-through either.

Interviewer: What tipped it toward the digest?

Participant: Time, mostly. The digest was quick to read and slotted right into the write-up I already had going—it reinforced the framing without extra work parsing sensor terminology I'd have needed help interpreting anyway. It read so cleanly and confidently that its regional forecast felt like it applied straight to Sector 7, more than I could really back up just from what was on the page. The IMINT report would've taken longer to properly digest and I wasn't fully confident I was reading the dispersal imagery correctly on my own.

Interviewer: Did you consider weighting them evenly, or leaning on IMINT instead?

Participant: I considered it. IMINT is sensor-based and specific to that hub, so on paper it's the stronger source. But given the time I had, citing the source I could actually process well and confidently seemed like the more responsible choice than citing something I might misread under pressure.

Interviewer: What did you learn about those sources afterward?

Participant: After the briefing, going back through the IMINT report more carefully, the dispersal pattern was actually just as consistent with a maintenance stand-down as with a buildup. And the digest, it turned out, was drawing on general regional reporting that didn't specifically tie back to Sector 7 at all.

Interviewer: Now the final call—how did you land on your confidence level for the briefing?

Participant: I had twenty minutes before I had to walk in. I had a buildup narrative, partial open-source support, and this unresolved contradiction with the maintenance terminology. I considered going high confidence, but the contradiction made that feel wrong. Low confidence felt like it undersold the pattern I was seeing. So I went moderate—buildup assessment, explicitly flagged the maintenance-terminology contradiction, and recommended a follow-up collection tasking to resolve it.

Interviewer: How did the lead respond?

Participant: He took the moderate framing at face value and tasked the follow-up collection, which was really the right outcome regardless of which way the underlying truth eventually goes.

Interviewer: And has that follow-up traffic settled it either way?

Participant: Not really. Two days on, the new traffic is still genuinely mixed. It hasn't confirmed the buildup and it hasn't ruled it out either.

Interviewer: If you'd had one more linguist-hour before the briefing, what would you have done differently?

Participant: Probably gone back to that second coded phrase earlier rather than letting it sit unresolved in the draft. It might have surfaced the maintenance angle sooner.

Interviewer: If the IMINT report had been your only corroborating option, how do you think your assessment would have looked?

Participant: Honestly, I think I'd have spent more time forcing myself through the sensor detail, and the ambiguity in the dispersal pattern might have shown up in my write-up earlier instead of after the fact. I might have hedged more going into the briefing.

Interviewer: Looking back, is there a point in this you'd want to revisit?

Participant: Probably the moment I locked in the buildup framing in the working note. It wasn't wrong to consider it, but I built it out pretty fully before I'd seen the maintenance-terminology intercept, and once it was written that clearly, it was hard to hold as loosely as I probably should have.

Interviewer: That's helpful. I think that covers everything I need.

Participant: Glad to walk through it.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IA_Biased_2}}",
  "occupational_domain": "{{Intelligence analysis and information-intensive analytic work}}",
  "role": "{{Signals Intelligence (SIGINT) Analyst}}"
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
