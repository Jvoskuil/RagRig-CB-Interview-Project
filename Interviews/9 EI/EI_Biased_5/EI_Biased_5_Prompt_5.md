You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time this week — I know decision-cycle deadlines are brutal right now. Before we start, this is just for our internal process review, nothing goes in any personnel file, and you can skip anything you'd rather not discuss. Sound okay?

Participant: Sure, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me a bit about your role and then give me an overview of the case we're discussing?

Participant: I've been an admissions officer here for about six years, mostly handling transfer applications. The file in question was a transfer student applying mid-cycle from abroad — strong essay, came from a magnet school that's sent us a good number of successful students over the years. It ended up being one of the more complicated files I handled this cycle, partly because of timing and partly because it landed right next to another borderline case at the very end.

Interviewer: Walk me through how it first came across your desk.

Participant: It came in through the regular transfer queue. I do an initial holistic file review — essay, transcript, test scores, letters — before deciding whether to move someone to interview or hold them for more information. This one had a personal essay that was genuinely strong, a transcript from a system I wasn't deeply familiar with, and a standardized test score that was a little under our usual threshold. The recommendation letter came from a teacher at that magnet school, which has a track record of producing students who do well here. Given the deadline pressure, I don't have time to deep-dive every file equally, so I lean on signals like that to triage.

Interviewer: And what did you decide at that point?

Participant: I fast-tracked it to interview. Honestly, the school's reputation carried a lot of weight for me there — we've had strong outcomes from that pipeline before, so a slightly low test score didn't worry me much. If I'm being fully honest, part of it was just an assumption that students coming out of that school are generally more prepared than the raw number suggested, and I didn't really check whether this particular transcript or the letter itself backed that up. I didn't go back and closely reread the letter itself; I registered who it was from and moved forward.

Interviewer: If the test score had been under threshold but the applicant came from a school you didn't recognize, do you think you'd have made the same call?

Participant: Probably not as quickly. I might have held it for a second look first. That said, we do sometimes hold unfamiliar-school files just to verify things, so it's not purely about the score.

Interviewer: What happened next?

Participant: The interview got scheduled during that week of transit strikes downtown, which threw off a lot of appointments. The applicant showed up twelve minutes late, visibly rattled, and the first several minutes of answers were short and hesitant. Answers picked up noticeably as the interview went on.

Interviewer: How did you score that?

Participant: I noted the late arrival and the rocky start on the rubric as a composure concern — some uncertainty about how this person handles pressure or manages time. I was aware the strike was happening citywide, but interview presentation is something we're asked to assess directly, so I documented what I observed.

Interviewer: Did you factor the strike into the written note at all?

Participant: Not explicitly, no. I think I treated the lateness itself as the data point rather than digging into why it happened. Later, admin confirmed the strike had delayed most interview slots that day, which in hindsight probably should have shaped how I read those first few minutes.

Interviewer: What would you have needed at that moment to write the note differently?

Participant: If I'd had that transit confirmation in hand during the interview instead of afterward, I probably would have framed the early hesitation as circumstantial rather than a personal trait note.

Interviewer: Let's move to the committee stage. What came up there?

Participant: Two things landed close together. First, a second reference — the guidance counselor — mentioned a minor disciplinary note from earlier in the applicant's schooling, already resolved, nothing serious. Second, the transcript used a twenty-point scale from a recently reformed grading system, and our credentials office guidance for that specific reform was still provisional — flagged as incomplete.

Interviewer: How did you handle the disciplinary note?

Participant: I talked it through with the committee. Given everything else — the essay, the school, the interview — my read was that the note didn't change the overall picture. If anything, I framed it as the kind of thing that shows a student worked through something and came out fine, which fit with the profile we'd already built of a strong, resilient applicant. If anything, I came out of that conversation feeling more sure about the applicant than I had going in, like the note itself was extra confirmation rather than something to weigh independently. Nobody pushed back hard on that framing.

Interviewer: Was there a version of that conversation where the note carried more weight?

Participant: I suppose so. Someone could argue we should treat new information as new information regardless of what came before. We didn't really revisit the earlier assessment from scratch — it got folded into the existing story rather than tested against it.

Interviewer: And the grading scale issue?

Participant: We only get one expedited credential evaluation slot per cycle, and I'd already flagged it for a different file. The credentials office did mention I could request a short same-day consult, or ask the committee to approve reallocating that slot after a quick review, but I didn't pursue either option. So for this one I used our standard conversion table, even knowing it wasn't built for the reformed scale and would probably lowball the actual grades. It was faster, and we were up against the deadline.

Interviewer: What made the table more appealing than pushing for that consult or the reallocation, deadline aside?

Participant: Honestly, some of it was just not wanting to open a longer back-and-forth with the credentials office over a system I wasn't sure how to interpret. Even the short consult felt like it would drag me into a conversation I didn't have a good handle on. The table gave me a number I could work with right away, even flagged as rough.

Interviewer: Understood. Last stage — the final committee vote.

Participant: We had two finalists left for one open seat, both borderline on paper, roughly comparable metrics. One had a legacy connection — same undergraduate network I came through myself, actually, same regional alumni chapter. The other had no alumni tie here at all.

Interviewer: How did you weigh the two?

Participant: We're supposed to apply the same criteria to both. In practice, I found myself giving the network-affiliated finalist a bit more benefit of the doubt on the softer parts of the file — I felt like I had more context on that community, more sense of what their outcomes tend to look like. I probably held the other finalist to a slightly tighter standard on the same soft factors.

Interviewer: Had you noticed that pattern before this case?

Participant: Enrollment did flag afterward that admit rates for network-affiliated legacy candidates in my portfolio run higher than for similar non-affiliated ones, without an obvious merit gap explaining it. I hadn't consciously tracked that before they raised it.

Interviewer: If neither finalist had any connection to your own network, do you think the vote goes the same way?

Participant: Hard to say for certain. I'd like to think the metrics alone would have decided it, but I can't rule out that the tie mattered more than it should have.

Interviewer: Looking back across the whole file, is there one moment you'd want to redo?

Participant: Probably the disciplinary note conversation. I moved through that too fast because it fit what I already believed. If I'd slowed down there the way I eventually did with the grading scale, the file might have landed somewhere different — though I genuinely don't know if the outcome would have changed.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EI_Biased_5}}",
  "occupational_domain": "{{Education and instructional work}}",
  "role": "{{University Admissions Officer}}"
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
