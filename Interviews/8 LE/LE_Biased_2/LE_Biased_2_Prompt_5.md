You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, I just want to confirm—this is a routine case-review interview, we're reconstructing your reasoning on a specific case, and it's fine to speak candidly since this isn't a disciplinary review. Sound good?

Participant: Sure, that's fine. I've done these debriefs before.

Interviewer: Great. Can you tell me a bit about your role and how this case landed on your desk?

Participant: I'm a latent print examiner, been doing casework about nine years. This one came through as a burglary submission—pry bar recovered from a residential break-in, latent lifted off the metal surface, plus a known print card for a suspect already booked. Standard comparison request, but they wanted it fast, ahead of a bail hearing.

Interviewer: Walk me through how the case actually came in—what did you know before you looked at the print itself?

Participant: The detective dropped the evidence off personally, which doesn't always happen. He mentioned, kind of in passing, that the suspect had already confessed and had two prior burglary convictions. I remember thinking, okay, that's helpful context, but my job is still to look at the ridges. I logged it in, noted his comments in the file, and got started. We don't have a strict blind-review setup here—some labs do, we don't—so it's normal for that kind of information to come with the evidence.

Interviewer: Did you consider handling the intake differently, given what he told you?

Participant: I thought about it for a second. I could've asked someone else to look at it fresh, or flagged it to my supervisor since he'd shared outcome information. But honestly, with the turnaround we had, that would've meant a delay we didn't have room for, and it's not like the confession changes what's on the pry bar. I proceeded normally.

Interviewer: Let's reconstruct the timeline. What was the physical state of the latent when you got into the analysis?

Participant: Partial print, fair amount of smudging, and there was a distorted region around the periphery—looked like it picked up texture from the tool grip itself, which throws off the ridge flow. The core area, though, was clean. Ten minutiae in that clear zone, no question about it.

Interviewer: And after you drafted your preliminary read?

Participant: I wrote it up, sent it to verification. Then the verifying examiner came back with a flag on that same peripheral area—didn't see it the way I did. That's when I had to reconcile things before the report went out.

Interviewer: Let's slow down on the comparison itself. When you got to that distorted peripheral region, what were you actually looking at, and how did you land on your read?

Participant: The ten minutiae in the clear zone were enough on their own, honestly—textbook sufficiency. The peripheral area was rougher, ridge flow was broken up by the distortion. I went back and forth on it. But when I lined it up against the known card, the flow direction seemed to pick back up in a way that fit the suspect's print. I remember thinking, given everything else pointing his way—he'd already admitted to it—this piece just confirmed what was already lining up. So I folded it into the individualization call as consistent rather than calling it indeterminate.

Interviewer: What alternatives were on the table at that point?

Participant: I could've treated that region as indeterminate and rested the conclusion purely on the ten clear minutiae—which honestly would've been sufficient by itself. Or I could've called for better imaging before committing either way. Those were both live options.

Interviewer: What would you say tipped you toward reading it as consistent rather than going with one of those?

Participant: The pattern looked plausible to me. I won't pretend the case context wasn't in my head at that point—it's hard to fully compartmentalize once you've heard something like that. But I also want to be clear, the ridge flow genuinely looked continuous to me in that section.

Interviewer: Moving to the verification step—what did you send over, and did you weigh other options?

Participant: I sent the full worksheet with my conclusion attached, along with the images. I could've sent just the images without my determination, let the verifier come in blind. We only had one other qualified examiner available that day, and with the clock running on the bail hearing, I went with the standard route—full packet, conclusion included.

Interviewer: Any hesitation there?

Participant: A little. Blind verification is theoretically cleaner, I know that. But it's not our default practice, and slowing things down to arrange it felt like more friction than the situation called for.

Interviewer: Let's talk about the discrepancy. The verifying examiner flagged that same peripheral region differently than you did. What went through your mind?

Participant: My first reaction was, okay, this is the distorted area, that's exactly the kind of spot where two examiners can read things differently. The ten core minutiae weren't in dispute—she agreed on those. So I looked at the discrepancy again and thought about what could explain it without it actually being a mismatch. Tool-surface texture causing pressure variance in that specific region made sense to me, and it's a documented thing that happens with textured surfaces like pry bars. I wrote that into the file as the explanation and kept the individualization conclusion standing.

Interviewer: Did you consider downgrading the conclusion instead?

Participant: I thought about calling it inconclusive until we could get a better lift or additional processing. That was on the table. But the ten minutiae were solid regardless, the deadline was same-day, and the distortion explanation accounted for what she was seeing without requiring me to throw out the whole determination.

Interviewer: What else, besides distortion, could have explained what she saw?

Participant: Could've genuinely been a non-matching area—maybe that region just doesn't belong to the same source. I didn't rule that out entirely, but it felt less likely to me once I had the distortion explanation in hand.

Interviewer: How confident were you in that peripheral read, if you had to put a number on it?

Participant: Maybe a six or seven out of ten on its own. But paired with the ten minutiae, I felt solid on the overall call.

Interviewer: Has this kind of distortion situation come up before in your casework?

Participant: Yeah, textured tool surfaces are a known headache. Usually if the core detail's strong, we don't let a rough edge area derail things.

Interviewer: Last few questions. If the detective had never mentioned the confession or the priors, do you think your read of that ambiguous region would've gone differently?

Participant: Possibly. I'd like to think I'd have called it the same way, but I can't say for certain the extra confidence wasn't doing some work there.

Interviewer: If the verifier's discrepancy had come up before you drafted your conclusion instead of after, would things have gone differently?

Participant: Maybe. Seeing it flagged first might've made me treat that region as indeterminate from the start rather than reconciling it after the fact.

Interviewer: What would you change if you had this case again with no deadline?

Participant: I'd probably request a fresh lift or enhanced imaging on that peripheral area before committing to anything, and maybe ask for a blind second look. Not because I think the outcome was wrong, but because that region deserved more room than we gave it that day.

Interviewer: Appreciate the candor. That's everything I need.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{LE_Biased_2}}",
  "occupational_domain": "{{Law enforcement}}",
  "role": "{{Latent Fingerprint Examiner}}"
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
