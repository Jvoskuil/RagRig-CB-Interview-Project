You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about how you approach clinical decisions, and I'll be asking about a specific case you flagged from a recent shift. Nothing you say will be attached to your name in any report. Sound okay?

Participant: Sure, that's fine. I've done a couple of these before for QI purposes, so I know the drill.

Interviewer: Great. Can you tell me your role and roughly how long you've been practicing?

Participant: I'm a hospitalist, internal medicine. I've been an attending for about nine years now, mostly at this hospital. I take the day handoff from the night team and round on the general medicine floor.

Interviewer: Perfect. Let's start broad — walk me through the case you had in mind.

Participant: Sure. This was a 68-year-old man who came in overnight through the ED. Fever, around 38.9, heart rate up around 112, blood pressure a little soft, 98 over 62, and the nurse noted he was mildly confused for a bit overnight. No clear source jumped out — no cough, no dysuria that he reported, no obvious skin findings on the ED note. Labs showed a mild leukocytosis. So basically a nonspecific presentation that could've been urinary, pulmonary, early skin or soft tissue, honestly a handful of things.

Interviewer: What was going through your mind when you first saw this?

Participant: Two things, really. Clinically, it's a fairly textbook SIRS picture without a clear source yet — common enough. But I'll be honest, it reminded me a lot of a patient I had maybe three weeks earlier. Similar vitals, similar vague presentation, and that one turned out to be a very fast-moving soft tissue infection that we caught late. It didn't go well. So when I saw this chart, that case was sitting in the back of my mind.

Interviewer: How did that shape what you did next?

Participant: I ordered a CT of the torso pretty much right away, before we even had urinalysis back. My reasoning at the time was I didn't want to be in that position again where we're playing catch-up on a soft tissue source. In hindsight, if I strip away that recent memory, this patient didn't actually have any exam findings pointing that direction — no erythema, no crepitus, nothing focal. But it felt like the responsible thing given what I'd just been through.

Interviewer: Got it. What other options were on the table?

Participant: I could've done a more stepwise workup — basic labs, urinalysis, maybe a chest film first, and reserved cross-sectional imaging if something localized. Or waited to see how his vitals trended over the next hour or two before committing to advanced imaging. Both were reasonable. I just didn't feel comfortable waiting.

Interviewer: What did the imaging show?

Participant: Came back about three hours later — clean. No abscess, no fasciitis, no intra-abdominal process. Urinalysis was still pending at that point anyway.

Interviewer: Let's move to antibiotics. What happened there?

Participant: Once the SIRS criteria were clearly met, I pulled up our sepsis order set. It gives you three empiric bundles — a narrow single-agent option, a broad two-drug "standard" bundle, and then a three-drug "extended" bundle that basically tacks on an extra agent covering organisms the standard bundle already handles for a case like this, just with more infusion time and extra renal monitoring tacked on.

Interviewer: How did you choose among those?

Participant: He was hemodynamically stable enough — SIRS positive but not meeting severe sepsis criteria. Looking at the three side by side, that third option didn't really buy you anything extra for a stable patient like him, it just added burden. But honestly, seeing it sitting there next to the standard bundle made the standard one look like the obviously sensible choice — clearly more coverage than the narrow option, without the extra baggage of the third one. So that's what I went with.

Interviewer: Did you separately work out what spectrum his actual severity called for, independent of the three options in front of you?

Participant: That's a fair question. Looking back, I think seeing that third bundle sitting there made the standard one look better by comparison, more than me actually starting from his numbers and building up from there. Pharmacy flagged later that the extended bundle is rarely indicated at this severity level anyway, and when ID called back, they said the standard bundle was reasonable but that the narrow one probably would've covered him fine given how stable he was.

Interviewer: How did you take that feedback?

Participant: A little bit of "huh, okay." Not wrong exactly, just broader than strictly necessary in retrospect.

Interviewer: Let's talk about the monitoring orders — telemetry and the catheter.

Participant: Right, so by mid-morning he was much improved. Heart rate down to 88, pressure 118 over 74, mentating clearly. Our sepsis order set auto-populates five days of continuous telemetry and continues the indwelling catheter as part of the standard pathway. Nursing actually flagged that he was up and walking around and asked whether the catheter was still needed.

Interviewer: What did you do with those orders?

Participant: I signed off on them as they were configured. Didn't actively shorten the telemetry window or pull the catheter order at that point.

Interviewer: Was there a specific reason you left them as configured versus reassessing given how much better he looked?

Participant: Honestly, I didn't sit down and re-derive whether five days was still appropriate. It's just what comes up when you open the pathway, and it's what most patients on this protocol get. Case management mentioned afterward that prolonged catheter use bumps up infection risk and can drag out length of stay, and telemetry didn't show anything over the next two days anyway, so it's hard to say it changed his outcome. But I probably could have revisited it earlier than I did.

Interviewer: Now the rounds discussion the next morning — what happened there?

Participant: The overnight resident's handoff, and how she presented it verbally at rounds, framed this as "likely urosepsis" — she'd seen mild pyuria on the early UA. That was the first thing said about the case, and honestly that framing kind of stuck for the group.

Interviewer: What new information came in around that time?

Participant: During that same discussion, the finalized urine culture came back with no significant growth, and the blood culture flagged preliminarily as gram-positive cocci in clusters — which honestly points more toward a skin or line source than urinary.

Interviewer: How did the team handle that shift in the data?

Participant: We acknowledged it, but the conversation kept circling back to the urosepsis framing for a while — talking about tweaking coverage for a urinary source, whether to repeat the UA, that kind of thing. It wasn't until a bit later, after we looked at his peripheral IV site and saw some redness there, that we really pivoted and started treating it as a likely catheter-related bacteremia instead.

Interviewer: Looking back, what do you think anchored the conversation to the urinary framing for as long as it did?

Participant: Probably that it was the first explanation on the table. Once you've got a plausible story and a room full of people nodding along, it takes a beat for contradictory data to really land, especially if it comes in mid-discussion rather than as the headline.

Interviewer: If the culture results had come back before rounds even started, do you think the discussion would've gone differently?

Participant: Probably, yeah. If gram-positive cocci and a negative urine culture were the opening facts instead of "likely urosepsis," I think we'd have gone straight to the IV site exam.

Interviewer: How much time pressure were you under across the shift overall?

Participant: Constant, honestly. ED wanted the bed, rounds have a hard start time, and you're juggling four or five other patients too. None of these felt like decisions I had the luxury of sitting with for twenty minutes each.

Interviewer: If you were handed this exact same information again tomorrow, is there a point you'd approach differently?

Participant: I think I'd force myself to write down the actual severity-based reasoning before looking at the order set options, rather than comparing across them first. And on the monitoring orders, I'd build in a habit of re-checking defaults once the patient's status changes, instead of just carrying them forward. The imaging call I'm less sure about — I still don't know that I'd talk myself out of it given how that last case ended.

Interviewer: That's really helpful. Anything else stand out from this case you think is worth noting?

Participant: Just that none of these felt like bad calls in the moment. It's only looking back at the sequence that you notice how much the earlier stuff — a past case, the first diagnosis mentioned, what's already checked in the system — shapes what happens next.

Interviewer: Thanks, this has been really useful.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HC_Biased_4}}",
  "occupational_domain": "{{Healthcare}}",
  "role": "{{Hospital Medicine Attending Physician (Internal Medicine Hospitalist)}}"
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
