"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_assessment",
        "raw_interview_anchor": "My first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant judges the alert likely benign from prior false-positive experience. The hidden complacency instance requires the later decision to let the automated score suppress manual verification; this initial impression alone does not meet that mechanism."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "objective_and_resource_rationale",
        "raw_interview_anchor": "Get through the queue, keep the shift moving, and not waste the incident response lead's time on something that turns out to be benign. We only had about three hours left in the shift, and I wanted whatever I handed off to be solid, not a guess.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an explicit workload and handoff objective, a plausible non-bias constraint rather than a hidden target mechanism."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant defers because of time and queue pressure. Without the later statement that the score did the deciding, this span alone remains consistent with the documented reasonable-triage interpretation."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_interpretation",
        "raw_interview_anchor": "I found a registry-key artifact that matched something documented in a GreyFalcon campaign from about six months back — I remembered writing that report myself, so it stuck with me.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The previously known registry-key match is treated as salient evidence in the attribution sequence. This is one chronological manifestation of cb_01, not an additional planned occurrence."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "Around the same time, internal telemetry showed an attempted connection to the HR benefits database from that host, which was strange, but I moved forward with attribution anyway.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant notes an anomaly and proceeds, but this span does not yet express the hidden mirror-imaging mechanism of projecting the analyst’s own strategic logic onto the adversary."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "time_allocation_rationale",
        "raw_interview_anchor": "The vendor portal access was closing soon, so I read it quickly.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a time-based reading decision and does not establish a presentation-driven source-credibility judgment."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "scope_choice",
        "raw_interview_anchor": "It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "oe_01"
        ],
        "ground_truth_rationale": "The first-listed IOC is the scope anchor in the chronological account; this is a manifestation of the single planned order-effects instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "source_credibility_rationale",
        "raw_interview_anchor": "I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of \"possibly\" and \"unclear.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "fl_01"
        ],
        "ground_truth_rationale": "The participant favors the bulletin by reference to its clean and confident presentation over hedged notes; this is the same planned DP4 fluency instance described again later."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "cue_weighting",
        "raw_interview_anchor": "Mainly the auto-triage score and my own memory of that server generating false alarms before. No unusual business disruption was reported either, which reinforced it felt routine.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant lists multiple operational cues, including historical false positives and no reported disruption. This does not by itself meet the hidden requirement that the score explicitly substitutes for independent verification."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_and_verification",
        "raw_interview_anchor": "Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cp_01"
        ],
        "ground_truth_rationale": "This directly manifests the hidden complacency mechanism: the Low score overrides an available anomalous cue and suppresses manual review."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "escalation_rationale",
        "raw_interview_anchor": "I thought about it, but that seemed like overkill for a Low score with no other signal at that point. In hindsight, I probably could've spent the fifteen minutes given how the next forty minutes went, but at the time it didn't seem to justify interrupting anyone.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant gives a plausible triage and interruption-cost rationale, while the statement is not needed to establish the explicit tool-overrides-cue mechanism mapped to seg_010."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "attribution_evidence_weighting",
        "raw_interview_anchor": "The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The familiar registry match is elevated into the GreyFalcon frame. This is another textual span for the one planned confirmation-bias instance."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "disconfirming_evidence_weighting",
        "raw_interview_anchor": "It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant acknowledges and underweights the discordant infrastructure evidence instead of testing whether it should lower attribution confidence; this is the narrowest full expression of cb_01 and the best RAG localization."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "adversary_intent_inference",
        "raw_interview_anchor": "My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "mi_01"
        ],
        "ground_truth_rationale": "The analyst explains adversary target selection through the analyst’s own strategic logic, the defining mirror-imaging mechanism."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "alternative_hypothesis_assessment",
        "raw_interview_anchor": "Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "mi_01"
        ],
        "ground_truth_rationale": "The participant accepts the projected motive without testing the alternative attribution; this is a separate interview span reiterating the same planned MI instance."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "scope_evidence_weighting",
        "raw_interview_anchor": "The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "oe_01"
        ],
        "ground_truth_rationale": "The first-listed IOC and prior working frame shape the chosen scope; this is another span of the same planned order-effects occurrence."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "narrative_based_scope_justification",
        "raw_interview_anchor": "It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ex_01"
        ],
        "ground_truth_rationale": "The narrative’s coherence is offered as the reason to allocate hunt resources, matching the hidden explanation-bias mechanism."
      },
      {
        "segment_id": "seg_018",
        "speaker": "Participant",
        "segment_type": "alternative_explanation_assessment",
        "raw_interview_anchor": "There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ex_01"
        ],
        "ground_truth_rationale": "The participant explicitly declines a test of the alternative because the existing GreyFalcon story seems to explain the evidence; this is the narrowest full expression of ex_01."
      },
      {
        "segment_id": "seg_019",
        "speaker": "Participant",
        "segment_type": "IOC_order_effect_assessment",
        "raw_interview_anchor": "Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "oe_01"
        ],
        "ground_truth_rationale": "The participant explicitly underweights later, more diagnostic hashes because of their list position and says reversing order would change the anchor. This is the best localization for obs_003."
      },
      {
        "segment_id": "seg_020",
        "speaker": "Participant",
        "segment_type": "business_constraint_scope_rationale",
        "raw_interview_anchor": "There was, briefly — business owners wanted it narrow anyway to avoid downtime on trading-adjacent systems, so narrow scope aligned with what they wanted too. That made it easier to just go with the scope that already made sense to me.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant cites a legitimate business constraint that independently supports a narrow scope; it does not add a distinct planned bias instance."
      },
      {
        "segment_id": "seg_021",
        "speaker": "Participant",
        "segment_type": "source_credibility_weighting",
        "raw_interview_anchor": "But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — \"possibly,\" \"unclear if,\" that kind of thing. The vendor version gave me something concrete to act on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "fl_01"
        ],
        "ground_truth_rationale": "Presentation and confident tone substitute for a comparison of underlying evidence, directly manifesting the hidden fluency instance."
      },
      {
        "segment_id": "seg_022",
        "speaker": "Participant",
        "segment_type": "source_comparison_rationale",
        "raw_interview_anchor": "Not directly side by side, no. I read the vendor one, it felt solid, and I went with it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "fl_01"
        ],
        "ground_truth_rationale": "The participant confirms that the subjective solidity of the bulletin drove the choice without an evidence comparison; this repeats the same planned fluency instance."
      },
      {
        "segment_id": "seg_023",
        "speaker": "Participant",
        "segment_type": "confidence_and_validation_judgment",
        "raw_interview_anchor": "Reasonably confident, maybe seven out of ten. Enough uncertainty that I flagged it as needing follow-up validation next shift, but I felt the containment steps were defensible given what I had.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant calibrates confidence and requests later validation; this does not itself manifest one of the hidden instances."
      },
      {
        "segment_id": "seg_024",
        "speaker": "Participant",
        "segment_type": "retrospective_counterfactual",
        "raw_interview_anchor": "I might have caught the odd outbound connection sooner, maybe before the vendor window closed, which could've changed how much I leaned on that bulletin later. Hard to say for certain.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a hindsight prediction about an alternative timeline, not a new bias manifestation."
      },
      {
        "segment_id": "seg_025",
        "speaker": "Participant",
        "segment_type": "counterfactual_order_assessment",
        "raw_interview_anchor": "Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "oe_01"
        ],
        "ground_truth_rationale": "The explicit reverse-order counterfactual confirms the positional mechanism for the single planned order-effects instance."
      },
      {
        "segment_id": "seg_026",
        "speaker": "Participant",
        "segment_type": "retrospective_review_judgment",
        "raw_interview_anchor": "Probably the attribution step. That's where I moved fastest from one piece of strong evidence to a full working theory, and a second set of eyes might have pushed back on the infrastructure mismatch or the HR access pattern before I built the rest of the shift around it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is hindsight recognition of a point that could use review. Per the rubric it does not create or extend a hidden bias occurrence."
      }
    ]
  }
