# Study-for-Deepeval
DeepEval Metrics
├── 1. Response Quality (RAG / General RAG Metrics)
│   ├── Answer Relevancy          → AnswerRelevancyMetric
│   ├── Faithfulness              → FaithfulnessMetric
│   ├── Hallucination             → HallucinationMetric
│   ├── Summarization             → SummarizationMetric
│   └── G-Eval (Custom Metric)    → GEval
│
├── 2. RAG Context Metrics (Retrieval Evaluation)
│   ├── Contextual Precision      → ContextualPrecisionMetric
│   ├── Contextual Recall         → ContextualRecallMetric
│   └── Contextual Relevancy      → ContextualRelevancyMetric
│
├── 3. Agent Metrics
│   ├── Task Completion           → TaskCompletionMetric
│   ├── Tool Correctness          → ToolCorrectnessMetric
│   ├── Step Efficiency           → StepEfficiencyMetric
│   ├── Plan Quality              → PlanQualityMetric
│   └── Plan Adherence            → PlanAdherenceMetric
│
├── 4. Conversational / Multi-turn Metrics
│   ├── Conversation Completeness → ConversationCompletenessMetric
│   ├── Conversation Relevancy    → ConversationRelevancyMetric
│   ├── Conversational Coherence  → ConversationalCoherenceMetric
│   ├── Role Adherence            → RoleAdherenceMetric
│   └── Knowledge Retention       → KnowledgeRetentionMetric
│
└── 5. Safety & Guardrails Metrics
    ├── Toxicity                  → ToxicityMetric
    ├── Bias                      → BiasMetric
    ├── PII Leakage               → PIILeakageMetric
    ├── Non-Advice                → NonAdviceMetric
    └── Role Violation            → RoleViolationMetric
